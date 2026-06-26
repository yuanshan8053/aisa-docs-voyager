#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
merge_content.py — 合并多份「分片 content.json」为一份完整 content.json

大档 spec(如 dataforseo 445 op / agentmail inboxes)由多个子 agent 按互斥的
operation 分组各写一份分片 content(每片只含自己负责的 opKey),本脚本把它们深合并:
  - operations: 按 opKey 合并(同 key 冲突即报错,因为分组应互斥)
  - fields:     按 opKey 合并(同 key 冲突即报错)

冲突即非零退出,杜绝两个分片重复认领同一 operation 造成静默覆盖。

用法:
  python3 merge_content.py --out content.json part1.json part2.json ...
"""
import argparse
import json
import sys


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("parts", nargs="+")
    args = ap.parse_args(argv)

    merged = {"operations": {}, "fields": {}}
    conflicts = []
    for p in args.parts:
        c = load(p)
        for k, v in (c.get("operations") or {}).items():
            if k in merged["operations"]:
                conflicts.append(f"operations[{k}] duplicated (also in earlier part), at {p}")
            merged["operations"][k] = v
        for k, v in (c.get("fields") or {}).items():
            if k in merged["fields"]:
                conflicts.append(f"fields[{k}] duplicated (also in earlier part), at {p}")
            merged["fields"][k] = v

    if conflicts:
        sys.stderr.write("MERGE CONFLICTS (overlapping opKeys across parts):\n")
        for c in conflicts:
            sys.stderr.write("  - " + c + "\n")
        return 1

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
        f.write("\n")
    sys.stderr.write("merge_content: parts=%d operations=%d field-blocks=%d\n"
                     % (len(args.parts), len(merged["operations"]), len(merged["fields"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
