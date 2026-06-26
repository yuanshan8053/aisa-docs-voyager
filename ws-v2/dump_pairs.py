#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""dump_pairs.py — 导出全部「原生英文 → 加强英文」前后对照对，供写作模式提炼。

遍历 31 份 enhanced.json，对每个带 x-doc.desc_en 的节点（operation / parameter / property）
导出 (spec, location, name/path, native_summary_or_description, desc_en[去批注], has_annotation)。
落 /tmp/pairs.jsonl，并打印分桶统计辅助选案例。
"""
import json
import os
import re

ROOT = "/home/mira/files/aisa-docs-voyager"
WS = os.path.join(ROOT, "ws-v2")
OUT = "/tmp/pairs.jsonl"
ANNO = re.compile(r"\[⚠️(?:Note|批注)\s*[:：].*?\]", re.S)


def strip_anno(s):
    return ANNO.sub("", s or "").strip()


def main():
    pairs = []
    specs = sorted(d for d in os.listdir(WS)
                   if os.path.isdir(os.path.join(WS, d))
                   and os.path.exists(os.path.join(WS, d, "enhanced.json")))
    for name in specs:
        d = json.load(open(os.path.join(WS, name, "enhanced.json"), encoding="utf-8"))

        def walk(o, segs):
            if isinstance(o, dict):
                x = o.get("x-doc")
                if isinstance(x, dict):
                    de = strip_anno(x.get("desc_en", ""))
                    if de:
                        # operation vs field
                        is_op = "heading_zh" in x
                        native = ""
                        if is_op:
                            native = (o.get("summary") or o.get("description") or "").strip()
                            loc = "operation"
                        else:
                            native = (o.get("description") or "").strip()
                            loc = "field"
                        pairs.append({
                            "spec": name,
                            "loc": loc,
                            "name": o.get("name") or (segs[-1] if segs else ""),
                            "path": "/".join(segs[-4:]),
                            "native": native.replace("\n", " "),
                            "enh": de.replace("\n", " "),
                            "had_anno": x.get("desc_en", "") != de,
                        })
                for k, v in o.items():
                    if k == "x-doc":
                        continue
                    walk(v, segs + [str(k)])
            elif isinstance(o, list):
                for i, v in enumerate(o):
                    walk(v, segs + [str(i)])

        walk(d, [])

    with open(OUT, "w", encoding="utf-8") as f:
        for p in pairs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    # 统计：原生为空的（从无到有）、原生很短的（扩写）、operation 级
    empty = sum(1 for p in pairs if not p["native"])
    ops = sum(1 for p in pairs if p["loc"] == "operation")
    short = sum(1 for p in pairs if p["native"] and len(p["native"]) < 25)
    print("total pairs:", len(pairs))
    print("  operation-level:", ops)
    print("  native EMPTY (从无到有):", empty)
    print("  native SHORT <25c (短->扩写):", short)
    print("  had inline annotation:", sum(1 for p in pairs if p["had_anno"]))
    print("written:", OUT)


if __name__ == "__main__":
    main()
