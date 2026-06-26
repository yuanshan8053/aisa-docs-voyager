#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_review.py — 三栏并排「改了什么」对照表 + 完整性闸门

直接回应用户痛点:「我没法清晰确认到底改了什么、改得更好还是更坏」。
它遍历 enhanced spec,对每个对外字段/参数/接口输出一行三栏对照:

  字段路径 │ 源英文(原生 description,只读) │ 加强英文(x-doc.desc_en) │ 中文(x-doc.title_zh)

让审阅者一眼看清每个字段的「原文 → 加强 → 本地化」三态,逐字段判断改得更好还是更坏。
不依赖渲染器,不受平台模板(火山 Action/Version 信封)干扰——这正是旧链路看不清改动的根因。

同时充当**完整性闸门**:统计每个对外字段是否齐备 desc_en + title_zh;
缺失即列入「待补」清单并以非零退出,杜绝偷懒漏写。

输出:
  - <out>.md   人读三栏对照(Markdown 表格,按接口分节)
  - <out>.json 机读对照 + 完整性统计
退出码:全部对外字段齐备=0;有缺漏=1。

用法:
  python3 make_review.py --spec enhanced.json --out review_table [--require both]
  --require: both(默认,需 desc_en+title_zh) | zh(仅需 title_zh) | en(仅需 desc_en)
"""
import argparse
import json
import sys

HTTP_METHODS = ("get", "post", "put", "delete", "patch", "head", "options")


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def deref(spec, schema, seen=None):
    seen = seen or set()
    if isinstance(schema, dict) and "$ref" in schema:
        ref = schema["$ref"]
        if ref in seen:
            return {}
        seen.add(ref)
        if ref.startswith("#/components/schemas/"):
            name = ref.split("/")[-1]
            return deref(spec, ((spec.get("components") or {}).get("schemas") or {}).get(name, {}), seen)
    return schema


def md_cell(s):
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", "<br>")


def _branch_has_content(b, spec):
    """分支(可能是裸 $ref)解引用后是否落到带 properties 的对象或数组。
    裸 $ref 分支(如 oneOf:[{$ref:...}])必须先 deref 再判定,否则会被漏选,
    造成整棵具名响应 schema 不被遍历的「假绿」。"""
    bb = deref(spec, b, set()) if spec is not None else b
    return isinstance(bb, dict) and ("properties" in bb or bb.get("type") == "array")


def descend_object(node, spec=None):
    """穿透 array 的 items / oneOf|anyOf(单分支选取) / allOf(合并全部分支 properties) / $ref,
    落到带 properties 的对象 schema。必须与 inject_xdoc.py 的同名函数语义一致,
    否则注入到 oneOf/allOf 分支里的字段会被本对照表漏掉,造成完整性闸门「假绿/假缺」。"""
    seen = 0
    while isinstance(node, dict) and seen < 24:
        seen += 1
        if spec is not None and "$ref" in node:
            node = deref(spec, node, set())
            continue
        if "properties" in node:
            return node
        if node.get("type") == "array" and isinstance(node.get("items"), dict):
            node = node["items"]
            continue
        if isinstance(node.get("allOf"), list):
            merged = {}
            arr_node = None
            for b in node["allOf"]:
                sub = descend_object(b, spec) if isinstance(b, dict) else None
                if isinstance(sub, dict):
                    if isinstance(sub.get("properties"), dict):
                        merged.update(sub["properties"])
                    elif sub.get("type") == "array":
                        arr_node = sub
            if merged:
                return {"properties": merged}
            if arr_node is not None:
                node = arr_node
                continue
            break
        picked = False
        for comb in ("oneOf", "anyOf"):
            branches = node.get(comb)
            if isinstance(branches, list):
                cand = next((b for b in branches
                             if isinstance(b, dict) and _branch_has_content(b, spec)), None)
                if cand is not None:
                    node = cand
                    picked = True
                    break
        if not picked:
            break
    return node


def walk_schema(spec, schema, prefix, rows, stats, require, seen=None):
    seen = seen or set()
    schema = deref(spec, schema, set())
    if not isinstance(schema, dict):
        return
    schema = descend_object(schema, spec)
    schema = deref(spec, schema, set())
    if not isinstance(schema, dict):
        return
    sid = id(schema)
    if sid in seen:
        return
    seen = seen | {sid}
    props = schema.get("properties")
    if isinstance(props, dict):
        for name, pnode in props.items():
            if not isinstance(pnode, dict):
                continue
            path = f"{prefix}.{name}" if prefix else name
            # 关键：x-doc 由 inject 加性写在「属性 wrapper 节点」上（含 {$ref:..., x-doc:...}）。
            # 必须在解引用之前用 raw 节点登记,否则 $ref-to-object 属性(如 gemini 的
            # systemInstruction/generationConfig)的 x-doc 会在 deref 后丢失,造成完整性闸门「假缺」。
            # 解引用后的目标 schema 仅用于继续向下递归。
            record(path, pnode, rows, stats, require)
            dnode = deref(spec, pnode, set())
            walk_schema(spec, dnode, path, rows, stats, require, seen)


def record(path, node, rows, stats, require):
    """node 携带原生 description + x-doc 时,产一行三栏对照。"""
    xd = node.get("x-doc") if isinstance(node.get("x-doc"), dict) else {}
    src_en = node.get("description") or node.get("title") or ""
    desc_en = xd.get("desc_en") or ""
    title_zh = xd.get("title_zh") or ""
    rows.append({"path": path, "src_en": src_en, "desc_en": desc_en, "title_zh": title_zh})
    stats["total"] += 1
    need_en = require in ("both", "en")
    need_zh = require in ("both", "zh")
    missing = []
    if need_en and not desc_en.strip():
        missing.append("desc_en")
    if need_zh and not title_zh.strip():
        missing.append("title_zh")
    if missing:
        stats["missing"].append({"path": path, "missing": missing,
                                 "src_en": src_en[:80]})


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--require", default="both", choices=["both", "zh", "en"])
    args = ap.parse_args(argv)

    spec = load(args.spec)
    sections = []
    stats = {"total": 0, "missing": []}
    paths = spec.get("paths") or {}
    for path, item in paths.items():
        if not isinstance(item, dict):
            continue
        for method in HTTP_METHODS:
            op = item.get(method)
            if not isinstance(op, dict):
                continue
            opid = op.get("operationId") or f"{method.upper()} {path}"
            rows = []
            oxd = op.get("x-doc") if isinstance(op.get("x-doc"), dict) else {}
            # operation 级行
            rows.append({"path": "(operation)",
                         "src_en": op.get("description") or op.get("summary") or "",
                         "desc_en": oxd.get("desc_en") or "",
                         "title_zh": oxd.get("description_zh") or oxd.get("heading_zh") or ""})
            # 参数
            for param in (op.get("parameters") or []):
                if not isinstance(param, dict) or param.get("$ref"):
                    continue
                pxd = param.get("x-doc") if isinstance(param.get("x-doc"), dict) else {}
                pname = param.get("name", "?")
                rows.append({"path": f"param:{pname}",
                             "src_en": param.get("description") or "",
                             "desc_en": pxd.get("desc_en") or "",
                             "title_zh": pxd.get("title_zh") or ""})
                stats["total"] += 1
                need_en = args.require in ("both", "en")
                need_zh = args.require in ("both", "zh")
                miss = []
                if need_en and not (pxd.get("desc_en") or "").strip():
                    miss.append("desc_en")
                if need_zh and not (pxd.get("title_zh") or "").strip():
                    miss.append("title_zh")
                if miss:
                    stats["missing"].append({"path": f"{opid}/param:{pname}", "missing": miss})
            # 请求体
            req = (((op.get("requestBody") or {}).get("content") or {})
                   .get("application/json") or {}).get("schema")
            if isinstance(req, dict):
                walk_schema(spec, req, "req", rows, stats, args.require)
            # 响应
            for code, resp in (op.get("responses") or {}).items():
                if not isinstance(resp, dict):
                    continue
                sch = ((resp.get("content") or {}).get("application/json") or {}).get("schema")
                if isinstance(sch, dict):
                    walk_schema(spec, sch, f"resp.{code}", rows, stats, args.require)
            sections.append({"operation": opid, "rows": rows})

    # 写 Markdown
    lines = ["# 增强对照表（源英文 → 加强英文 → 中文本地化）", "",
             f"> spec 共 {len(sections)} 个接口，{stats['total']} 个对外字段/参数。"
             f"逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。", ""]
    for sec in sections:
        lines.append(f"## {sec['operation']}")
        lines.append("")
        lines.append("| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |")
        lines.append("| --- | --- | --- | --- |")
        for r in sec["rows"]:
            lines.append(f"| `{md_cell(r['path'])}` | {md_cell(r['src_en'])} | "
                         f"{md_cell(r['desc_en'])} | {md_cell(r['title_zh'])} |")
        lines.append("")
    if stats["missing"]:
        lines.append("## ⚠️ 待补字段（完整性闸门未通过）")
        lines.append("")
        for m in stats["missing"]:
            lines.append(f"- `{m['path']}` 缺：{', '.join(m['missing'])}")
        lines.append("")
    with open(args.out + ".md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    with open(args.out + ".json", "w", encoding="utf-8") as f:
        json.dump({"sections": sections, "total": stats["total"],
                   "missing": stats["missing"]}, f, ensure_ascii=False, indent=2)

    n_missing = len(stats["missing"])
    sys.stderr.write(f"make_review: total_fields={stats['total']} missing={n_missing}\n")
    if n_missing:
        sys.stderr.write("INCOMPLETE: %d field(s) missing required content.\n" % n_missing)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
