#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_native_preserved.py — 原生结构保全闸门（关系型 diff）

红线：相对输入 spec，本流程只能【新增 x-doc】，绝不删除/篡改任何原生结构
（property 键、required[]、type/format/enum/数值约束、$ref/items、paths/method）。

做法：把 enhanced spec 里所有 x-doc 键剥掉，再与输入 spec 的原生骨架逐节点比对。
exit 0 = 完好；exit 1 = 有违规（打印到 stderr）。

用法：python3 check_native_preserved.py <input_spec.json> <enhanced.json>
"""
import json
import sys

PROTECTED = ("type", "format", "enum", "minimum", "maximum", "exclusiveMinimum",
             "exclusiveMaximum", "minLength", "maxLength", "pattern", "default",
             "$ref", "required")


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def strip_xdoc(node):
    if isinstance(node, dict):
        return {k: strip_xdoc(v) for k, v in node.items() if k != "x-doc"}
    if isinstance(node, list):
        return [strip_xdoc(v) for v in node]
    return node


def diff(base, cand, path, violations):
    if isinstance(base, dict):
        if not isinstance(cand, dict):
            violations.append(f"{path}: expected object, got {type(cand).__name__}")
            return
        for k, bv in base.items():
            cpath = f"{path}/{k}"
            if k not in cand:
                violations.append(f"{cpath}: native key DELETED")
                continue
            cv = cand[k]
            if k in PROTECTED and bv != cv:
                violations.append(f"{cpath}: native metadata TAMPERED ({bv!r} -> {cv!r})")
            diff(bv, cv, cpath, violations)
    elif isinstance(base, list):
        if not isinstance(cand, list):
            violations.append(f"{path}: expected array, got {type(cand).__name__}")
            return
        if len(base) != len(cand):
            violations.append(f"{path}: array length changed ({len(base)} -> {len(cand)})")
        for i, bv in enumerate(base):
            if i < len(cand):
                diff(bv, cand[i], f"{path}[{i}]", violations)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    base = load(sys.argv[1])
    cand = strip_xdoc(load(sys.argv[2]))
    violations = []
    diff(base, cand, "", violations)
    if violations:
        print("NATIVE-PRESERVATION VIOLATIONS:", file=sys.stderr)
        for v in violations:
            print("  - " + v, file=sys.stderr)
        sys.exit(1)
    print("OK: native metadata fully preserved (enhanced spec only adds x-doc).")
    sys.exit(0)


if __name__ == "__main__":
    main()
