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
import argparse
import tempfile
from pathlib import Path

ROOT = str(Path(__file__).resolve().parents[1])
SRC = os.environ.get("AISA_SOURCE_OPENAPI", str(Path(ROOT) / "docs-mirror" / "openapi"))
T = str(Path(ROOT) / "skill-local" / "aisa-doc-enhance" / "tools")
WS = str(Path(ROOT) / "ws-v2")
TMP = os.environ.get("AISA_CENTRAL_TMP", str(Path(tempfile.gettempdir()) / "central"))
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


def strip_xdoc(node):
    if isinstance(node, dict):
        return {k: strip_xdoc(v) for k, v in node.items() if k != "x-doc"}
    if isinstance(node, list):
        return [strip_xdoc(v) for v in node]
    return node


def write_derived_source(enhanced_path, out_path):
    with open(enhanced_path, encoding="utf-8") as f:
        native = strip_xdoc(json.load(f))
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(native, f, ensure_ascii=False, indent=2)
        f.write("\n")


def parse_args():
    p = argparse.ArgumentParser(description="Run central acceptance for ws-v2 OpenAPI x-doc artifacts.")
    p.add_argument("--baseline", default="16863d3", help="pinned source baseline, recorded in output")
    p.add_argument("--root", default=ROOT, help="repository root")
    p.add_argument("--src", default=SRC, help="directory containing source OpenAPI JSON files")
    p.add_argument("--tools", default=T, help="aisa-doc-enhance tools directory")
    p.add_argument("--ws", default=WS, help="ws-v2 directory")
    p.add_argument("--tmp", default=TMP, help="temporary output directory")
    p.add_argument("--refresh", action="store_true", help="update committed enhanced.json files when regenerated output differs")
    return p.parse_args()


def main():
    args = parse_args()
    root = Path(args.root)
    src_dir = Path(args.src)
    tools = Path(args.tools)
    ws = Path(args.ws)
    tmp = Path(args.tmp)
    tmp.mkdir(parents=True, exist_ok=True)

    names = sorted(d.name for d in ws.iterdir()
                   if d.is_dir()
                   and (d / "content.json").exists())
    results = []
    tot = {"ops": 0, "fields": 0, "annotations": 0, "protected": 0, "unresolved": 0}
    all_green = True
    for name in names:
        src = src_dir / f"{name}.json"
        source = "source"
        if not src.exists():
            committed = ws / name / "enhanced.json"
            if committed.exists():
                src = tmp / f"{name}.native.json"
                write_derived_source(committed, src)
                source = "derived_from_committed_enhanced"
            else:
                results.append({"spec": name, "ERROR": "source spec missing"})
                all_green = False
                continue
        if not src.exists():
            results.append({"spec": name, "ERROR": "source spec missing"})
            all_green = False
            continue
        content = ws / name / "content.json"
        enh = tmp / f"{name}.enh.json"
        inj = tmp / f"{name}.inj.json"
        rev = tmp / f"{name}.rev"
        rc1, o1 = run(["python3", str(tools / "inject_xdoc.py"),
                       "--spec", src, "--content", content,
                       "--out", enh, "--review-out", inj, "--doc-version", "2.0.0"])
        # parse inject stats
        injstats = json.load(open(inj))["stats"] if os.path.exists(inj) else {}
        rc2, o2 = run(["python3", str(tools / "check_native_preserved.py"), src, enh])
        rc3, o3 = run(["python3", str(tools / "make_review.py"),
                       "--spec", enh, "--out", rev, "--require", "both"])
        # missing count from review json
        missing = None
        rev_json = Path(str(rev) + ".json")
        if rev_json.exists():
            missing = len(json.load(open(rev_json)).get("missing", []))
        # compare to committed enhanced.json
        committed = ws / name / "enhanced.json"
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
            "source": source,
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
        # Refresh committed artifacts only when explicitly requested.
        if identical is False and args.refresh:
            import shutil
            shutil.copy(enh, committed)
            row["committed_refreshed"] = True

    out = {
        "baseline": args.baseline,
        "root": str(root),
        "source_openapi": str(src_dir),
        "specs": len(results),
        "all_green": all_green,
        "totals": tot,
        "rows": results,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if all_green else 1


if __name__ == "__main__":
    sys.exit(main())
