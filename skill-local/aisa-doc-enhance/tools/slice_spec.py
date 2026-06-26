#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
slice_spec.py — 从大档 spec 切出「按 path 前缀/正则」的子 spec，保留 components 以便 $ref 解析。

大档(dataforseo 445 op)按 operation 分组派给多个子 agent。每个 agent 拿到的子 spec
只含自己负责的 paths(但 components.schemas 全量保留,保证 $ref 解析),即可独立跑通
inject_xdoc → check_native_preserved → make_review 三件套自验(exit 0 / missing 0)。

子 spec 的 opKey(operationId 或 "METHOD /path")与全档完全一致,故各组 content.json
可由 merge_content.py 合并后,在全档上一次性 inject + 双闸门复验。

用法:
  # 按 path 第 N 段精确匹配(1-based,/ 切分后)
  python3 slice_spec.py --spec dataforseo.json --out labs.json --seg 2 --eq dataforseo_labs
  # 按 path 第 N 段属于集合
  python3 slice_spec.py --spec dataforseo.json --out misc.json --seg 2 --in app_data,merchant
  # 按 path 正则
  python3 slice_spec.py --spec dataforseo.json --out g.json --regex '^/serp/google/'
  # 在匹配集合内再按 operationId 排序取分片 k/n(用于把超大组二分)
  python3 slice_spec.py --spec dataforseo.json --out labs_1.json --seg 2 --eq dataforseo_labs --part 1/2
"""
import argparse
import copy
import json
import re
import sys

HTTP_METHODS = ("get", "post", "put", "delete", "patch", "head", "options")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--seg", type=int, default=0, help="1-based path segment index after splitting on /")
    ap.add_argument("--eq", default=None)
    ap.add_argument("--in", dest="in_set", default=None, help="comma-separated values")
    ap.add_argument("--regex", default=None)
    ap.add_argument("--part", default=None, help="k/n: keep part k of n (1-based), ops sorted by key")
    args = ap.parse_args(argv)

    spec = json.load(open(args.spec, encoding="utf-8"))
    paths = spec.get("paths") or {}
    in_set = set(x.strip() for x in args.in_set.split(",")) if args.in_set else None
    rx = re.compile(args.regex) if args.regex else None

    def seg_val(p):
        parts = p.strip("/").split("/")
        idx = args.seg - 1
        return parts[idx] if 0 <= idx < len(parts) else None

    selected = {}
    for p, item in paths.items():
        if not isinstance(item, dict):
            continue
        ok = True
        if rx is not None:
            ok = ok and bool(rx.search(p))
        if args.seg:
            sv = seg_val(p)
            if args.eq is not None:
                ok = ok and (sv == args.eq)
            if in_set is not None:
                ok = ok and (sv in in_set)
        if ok:
            selected[p] = item

    # optional bisection by sorted path key
    if args.part:
        k, n = (int(x) for x in args.part.split("/"))
        keys = sorted(selected.keys())
        # split into n contiguous chunks
        chunks = [keys[i::n] for i in range(n)]  # round-robin to balance op count
        keep = set(chunks[k - 1])
        selected = {p: v for p, v in selected.items() if p in keep}

    out = copy.deepcopy(spec)
    out["paths"] = selected

    # count ops
    ops = 0
    for p, item in selected.items():
        for m in HTTP_METHODS:
            if isinstance(item.get(m), dict):
                ops += 1

    json.dump(out, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    sys.stderr.write(f"slice_spec: {args.out} paths={len(selected)} ops={ops}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
