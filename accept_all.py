#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""accept_all.py — 机器可复跑总验收。

覆盖两类可执行门禁：
  1) ws-v2/central_accept.py：31 份 OpenAPI x-doc 加强产物双闸门。
  2) check_projection.py：ws-site/{en,zh} 60 份站点投影三闸门。

不把「漏报 / 误报 0 / 0」写成机器门禁；该结论来自人工/多 Agent
报告复核，不是当前仓库里可由单脚本重新判定的检查项。
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple


class ProjectionJob(NamedTuple):
    name: str
    lang: str
    enhanced: Path
    projected: Path


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def load_json_output(proc):
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None


def projection_jobs(root):
    jobs = []
    ws_v2 = root / "ws-v2"
    ws_site = root / "ws-site"
    names = sorted(p.stem for p in (ws_site / "en").glob("*.json"))
    for name in names:
        enhanced = ws_v2 / name / "enhanced.json"
        if not enhanced.exists():
            continue
        for lang in ("en", "zh"):
            projected = ws_site / lang / f"{name}.json"
            if projected.exists():
                jobs.append(ProjectionJob(name, lang, enhanced, projected))
    return jobs


def run_central(root, baseline):
    proc = run([
        sys.executable,
        str(root / "ws-v2" / "central_accept.py"),
        "--baseline",
        baseline,
    ])
    data = load_json_output(proc)
    if data is None:
        return {
            "ok": False,
            "exit_code": proc.returncode,
            "passed": 0,
            "total": 0,
            "error": (proc.stdout + proc.stderr).strip()[-1000:],
        }
    rows = data.get("rows") or []
    passed = sum(1 for row in rows if row.get("GREEN") is True)
    total = data.get("specs", len(rows))
    return {
        "ok": proc.returncode == 0 and data.get("all_green") is True,
        "exit_code": proc.returncode,
        "passed": passed,
        "total": total,
        "totals": data.get("totals", {}),
        "source_openapi": data.get("source_openapi"),
        "derived_sources": sum(1 for row in rows if row.get("source") == "derived_from_committed_enhanced"),
    }


def run_projection_gates(root):
    jobs = projection_jobs(root)
    rows = []
    for job in jobs:
        proc = run([
            sys.executable,
            str(root / "check_projection.py"),
            "--enhanced",
            str(job.enhanced),
            "--lang",
            job.lang,
            "--projected",
            str(job.projected),
        ])
        rows.append({
            "spec": job.name,
            "lang": job.lang,
            "exit_code": proc.returncode,
            "ok": proc.returncode == 0,
            "error": proc.stderr.strip()[-800:] if proc.returncode else "",
        })
    return {
        "ok": bool(jobs) and all(row["ok"] for row in rows),
        "passed": sum(1 for row in rows if row["ok"]),
        "total": len(rows),
        "rows": rows,
    }


def print_human(result):
    central = result["central"]
    projection = result["projection"]
    central_exit = 0 if central["ok"] else central["exit_code"]
    projection_exit = 0 if projection["ok"] else 1

    print(f"# 一键复跑机器验收，基线 pinned commit {result['baseline']}")
    print(f"$ python3 accept_all.py --baseline {result['baseline']}")
    print(f"  → OpenAPI 加强双闸门     {central['passed']}/{central['total']}  exit {central_exit}")
    print(f"  → 站点投影三闸门         {projection['passed']}/{projection['total']}  exit {projection_exit}")
    if central.get("derived_sources"):
        print(f"  → 派生源 spec             {central['derived_sources']}  份（源镜像缺失时从已提交 enhanced.json 剥离 x-doc）")
    print("  → 漏报 / 误报             报告复核结论，非本脚本机器门禁")
    if result["ok"]:
        print("✓ all machine gates passed")
    else:
        print("✗ machine gates failed")
        failed = [row for row in projection.get("rows", []) if not row["ok"]][:5]
        for row in failed:
            print(f"  - projection failed: {row['spec']} {row['lang']}")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Run all machine-verifiable acceptance gates.")
    ap.add_argument("--baseline", default="16863d3")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent))
    ap.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    result = {
        "baseline": args.baseline,
        "root": str(root),
        "central": run_central(root, args.baseline),
        "projection": run_projection_gates(root),
    }
    result["ok"] = result["central"]["ok"] and result["projection"]["ok"]

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_human(result)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
