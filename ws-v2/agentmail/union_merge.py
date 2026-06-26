#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
union_merge.py — agentmail 专用「按 opKey 深合并(union)」合并器

为什么不能用通用 merge_content.py:
  通用 merge_content.py 按 opKey 严格去重(同 key 即冲突退出),这对 dataforseo 等
  「operationId 全档唯一」的档是正确的——任何重复都意味着两个分片重复认领同一 operation。
  但 agentmail 源 spec 的 46 个 operation 只用了 12 个 operationId(get/list/delete/...
  在多条 path 上复用)。注入器 opKey = operationId(存在即用),故同一 operationId 的
  content 块会被应用到该 id 下的全部 path。两个 path-互斥 的分片(inboxes 21 path /
  rest 9 path)自然会各自持有 `get`/`list` 等同名 opKey 块——这是源 spec 的结构属性,
  不是重复认领。

合并语义(确定性):
  · operations: 按 opKey union;同 key 冲突 → 取 inboxes(主分片,21 path)优先,计数。
  · fields:     按 opKey union;每个 opKey 内再 union request / parameters / response.<code>
                的 dotpath 映射;同 dotpath 冲突 → 取 inboxes 优先,计数。
冲突计数仅用于报告透明度——两个同 operationId path 的同名字段(如 recipients/updated_at)
在 agentmail 的邮件资源语义下基本一致,union 取其一不损"两字段齐备"与"原生零改动"两道闸门。

用法: python3 union_merge.py --out content.json inboxes.content.json rest.content.json
"""
import argparse
import json
import sys


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def union_dotmap(dst, src, conflicts, ctx):
    for dp, v in (src or {}).items():
        if dp in dst and json.dumps(dst[dp], sort_keys=True, ensure_ascii=False) != \
                json.dumps(v, sort_keys=True, ensure_ascii=False):
            conflicts.append(f"{ctx}.{dp}")
            continue  # keep first (inboxes-priority by arg order)
        if dp not in dst:
            dst[dp] = v


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("parts", nargs="+")
    args = ap.parse_args(argv)

    merged = {"operations": {}, "fields": {}}
    op_conflicts, field_conflicts = [], []

    for p in args.parts:
        c = load(p)
        for k, v in (c.get("operations") or {}).items():
            if k in merged["operations"]:
                if json.dumps(merged["operations"][k], sort_keys=True, ensure_ascii=False) != \
                        json.dumps(v, sort_keys=True, ensure_ascii=False):
                    op_conflicts.append(k)
                continue  # keep first
            merged["operations"][k] = v
        for k, v in (c.get("fields") or {}).items():
            dst = merged["fields"].setdefault(k, {})
            # request
            if v.get("request"):
                union_dotmap(dst.setdefault("request", {}), v["request"],
                             field_conflicts, f"{k}.request")
            # parameters
            if v.get("parameters"):
                union_dotmap(dst.setdefault("parameters", {}), v["parameters"],
                             field_conflicts, f"{k}.parameters")
            # response by code
            for code, dmap in (v.get("response") or {}).items():
                union_dotmap(dst.setdefault("response", {}).setdefault(code, {}), dmap,
                             field_conflicts, f"{k}.response.{code}")

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
        f.write("\n")
    sys.stderr.write(
        "union_merge: parts=%d operations=%d field-blocks=%d "
        "op_conflicts=%d field_dotpath_conflicts=%d\n"
        % (len(args.parts), len(merged["operations"]), len(merged["fields"]),
           len(op_conflicts), len(field_conflicts)))
    if op_conflicts:
        sys.stderr.write("  op_conflicts(kept-first): " + ", ".join(sorted(set(op_conflicts))) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
