#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""central_accept.py — 中央验收：对全部 31 档 spec 复跑两道闸门 + 统计盘点。

对每档:
  1) 从 ws-v2/<name>/content.json 在「源 spec(pinned 16863d3)」上重新 inject(trust-but-verify,
     不信任已落盘 enhanced.json,现场重算)。
  2) GATE1 check_native_preserved(源 vs 重算 enhanced)→ 必须 exit 0。
  3) GATE2 make_review --require both → 必须 missing=0。
  4) 与已落盘 enhanced.json 比对(应字节一致),不一致则刷新落盘并标注。
  5) 统计 ops / fields / annotations(批注) / source-protected / unresolved。
输出 JSON 汇总到 stdout 末尾。
"""
import json
import subprocess
import sys
import os

ROOT = "/home/mira/files/aisa-docs-voyager"
SRC = "/home/mira/files/aisa-team-docs/openapi"
T = os.path.join(ROOT, "skill-local/aisa-doc-enhance/tools")
WS = os.path.join(ROOT, "ws-v2")
TMP = "/tmp/central"
os.makedirs(TMP, exist_ok=True)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def count_annotations(content):
    n = 0
    def scan(obj):
        nonlocal n
        if isinstance(obj, dict):
            if isinstance(obj.get("annotation"), str) and obj["annotation"].strip():
                n += 1
            for v in obj.values():
                scan(v)
        elif isinstance(obj, list):
            for v in obj:
                scan(v)
    scan(content)
    return n


def main():
    names = sorted(d for d in os.listdir(WS)
                   if os.path.isdir(os.path.join(WS, d))
                   and os.path.exists(os.path.join(WS, d, "content.json")))
    results = []
    tot = {"ops": 0, "fields": 0, "annotations": 0, "protected": 0, "unresolved": 0}
    all_green = True
    for name in names:
        src = os.path.join(SRC, name + ".json")
        if not os.path.exists(src):
            results.append({"spec": name, "ERROR": "source spec missing"})
            all_green = False
            continue
        content = os.path.join(WS, name, "content.json")
        enh = os.path.join(TMP, name + ".enh.json")
        inj = os.path.join(TMP, name + ".inj.json")
        rev = os.path.join(TMP, name + ".rev")
        rc1, o1 = run(["python3", os.path.join(T, "inject_xdoc.py"),
                       "--spec", src, "--content", content,
                       "--out", enh, "--review-out", inj, "--doc-version", "2.0.0"])
        # parse inject stats
        injstats = json.load(open(inj))["stats"] if os.path.exists(inj) else {}
        rc2, o2 = run(["python3", os.path.join(T, "check_native_preserved.py"), src, enh])
        rc3, o3 = run(["python3", os.path.join(T, "make_review.py"),
                       "--spec", enh, "--out", rev, "--require", "both"])
        # missing count from review json
        missing = None
        if os.path.exists(rev + ".json"):
            missing = len(json.load(open(rev + ".json")).get("missing", []))
        # compare to committed enhanced.json
        committed = os.path.join(WS, name, "enhanced.json")
        identical = None
        if os.path.exists(committed):
            identical = open(enh).read() == open(committed).read()
        ann = count_annotations(json.load(open(content)))
        row = {
            "spec": name,
            "ops": injstats.get("operations"),
            "fields": injstats.get("fields"),
            "protected": injstats.get("protected_skipped"),
            "unresolved": injstats.get("unresolved"),
            "annotations": ann,
            "gate_native": "PASS" if rc2 == 0 else "FAIL",
            "gate_review_missing": missing,
            "committed_identical": identical,
        }
        green = (rc1 == 0 and rc2 == 0 and rc3 == 0 and missing == 0)
        row["GREEN"] = green
        if not green:
            all_green = False
            row["_native_out"] = o2.strip()[-300:]
            row["_review_out"] = o3.strip()[-300:]
        results.append(row)
        tot["ops"] += injstats.get("operations", 0) or 0
        tot["fields"] += injstats.get("fields", 0) or 0
        tot["annotations"] += ann
        tot["protected"] += injstats.get("protected_skipped", 0) or 0
        tot["unresolved"] += injstats.get("unresolved", 0) or 0
        # refresh committed if differs
        if identical is False:
            import shutil
            shutil.copy(enh, committed)
            row["committed_refreshed"] = True

    out = {"specs": len(results), "all_green": all_green, "totals": tot, "rows": results}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if all_green else 1


if __name__ == "__main__":
    sys.exit(main())
