#!/usr/bin/env python3
"""
AIsa Doc Reality Auditor
========================

A drift-detection agent for AIsa's developer documentation.

WHY THIS EXISTS
---------------
AIsa's docs are large (~770 indexed pages), machine-discoverable
(llms.txt + agent-card.json + ai-plugin.json), and auto-generated from a
live gateway. That combination creates a specific, recurring failure mode:
the *prose* docs and the *live* machine contracts drift apart, and an agent
that trusts the docs gets a broken instruction.

This tool fetches the live, authoritative sources on every run and compares
them against what the human-readable guides *claim*. It is designed to run
unattended in CI (see .github/workflows/doc-reality-check.yml) and fail the
build when reality and docs disagree.

It checks four classes of defect:

  1. DEAD DISCOVERY ENDPOINTS - URLs the docs/manifests tell agents to fetch
     that do not actually resolve (e.g. /openapi.yaml -> 404).
  2. COUNT DRIFT - numeric claims in the guides ("13 skills", "111+ paths")
     vs. what the live agent card / index actually contain.
  3. LOCALIZATION COVERAGE - share of the doc surface available in Chinese,
     the gateway's stated #1 model-supply market.
  4. FRESHNESS - staleness of "last refreshed" stamps in the guides.

USAGE
-----
    python -m aisa_doc_auditor.auditor                 # human report
    python -m aisa_doc_auditor.auditor --json out.json # machine report
    python -m aisa_doc_auditor.auditor --ci            # exit 1 on any blocker

No API key required - every source audited here is public.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
import urllib.request
import urllib.error
from dataclasses import dataclass, field, asdict
from typing import Optional

BASE = "https://aisa.one"
UA = "aisa-doc-reality-auditor/1.0 (+https://github.com/AIsa-team/docs)"
TIMEOUT = 25

# Discovery endpoints that the docs / manifests instruct agents to fetch.
# We assert each one resolves; a 404 here means an autonomous agent following
# the published contract hits a wall.
DISCOVERY_ENDPOINTS = [
    ("/.well-known/agent-card.json", "A2A agent card (primary discovery)"),
    ("/.well-known/ai-plugin.json", "OpenAI plugin manifest"),
    ("/.well-known/mcp.json", "MCP manifest"),
    ("/openapi.yaml", "Consolidated OpenAPI spec (cited by guide + ai-plugin)"),
    ("/docs/llms.txt", "llms.txt master index"),
]

SEVERITY_BLOCKER = "BLOCKER"
SEVERITY_WARN = "WARN"
SEVERITY_OK = "OK"


@dataclass
class Finding:
    check: str
    severity: str
    summary: str
    evidence: dict = field(default_factory=dict)
    remediation: str = ""


def _fetch(url: str) -> tuple[int, str]:
    """Return (status_code, body). status_code 0 on network failure."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.getcode(), resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


def _looks_like_html(body: str) -> bool:
    head = body.lstrip()[:200].lower()
    return head.startswith("<!doctype html") or head.startswith("<html")


# --------------------------------------------------------------------------
# Check 1: dead discovery endpoints
# --------------------------------------------------------------------------
def check_discovery_endpoints() -> list[Finding]:
    findings: list[Finding] = []
    for path, label in DISCOVERY_ENDPOINTS:
        url = BASE + path
        code, body = _fetch(url)
        # A "soft 404": Next.js apps return 200 with an HTML error shell for
        # missing static assets, so treat HTML where a spec is expected as dead.
        expects_machine = path.endswith((".json", ".yaml", ".txt"))
        is_html_shell = expects_machine and _looks_like_html(body)
        dead = code == 0 or code >= 400 or is_html_shell
        if dead:
            findings.append(Finding(
                check="discovery_endpoint",
                severity=SEVERITY_BLOCKER,
                summary=f"Discovery endpoint unusable: {path} ({label})",
                evidence={
                    "url": url,
                    "http_status": code,
                    "returned_html_shell": is_html_shell,
                },
                remediation=(
                    "Either publish the resource at this exact URL or update "
                    "every reference (ai-plugin.json `api.url`, agent-discovery "
                    "guide) to the real location. Agents following the published "
                    "contract currently hit a dead link here."
                ),
            ))
        else:
            findings.append(Finding(
                check="discovery_endpoint",
                severity=SEVERITY_OK,
                summary=f"Discovery endpoint OK: {path}",
                evidence={"url": url, "http_status": code},
            ))
    return findings


# --------------------------------------------------------------------------
# Check 2: count drift (claimed vs. live)
# --------------------------------------------------------------------------
def _live_skill_count() -> Optional[int]:
    code, body = _fetch(BASE + "/.well-known/agent-card.json")
    if code != 200 or not body:
        return None
    try:
        return len(json.loads(body).get("skills", []))
    except Exception:
        return None


def _live_openapi_spec_count() -> Optional[int]:
    """Count split OpenAPI specs enumerated in llms.txt."""
    code, body = _fetch(BASE + "/docs/llms.txt")
    if code != 200 or not body:
        return None
    return len(re.findall(r"https://aisa\.one/docs/openapi/[^\s)]+\.json", body))


def _claimed_counts() -> dict:
    """Parse numeric claims out of the agent-discovery guide."""
    code, body = _fetch(BASE + "/docs/guides/agent-discovery.md")
    out: dict = {"source": BASE + "/docs/guides/agent-discovery.md", "http_status": code}
    if code != 200 or not body:
        return out
    m_sk = re.search(r"advertises\s+(\d+)\s+skills", body)
    if not m_sk:
        m_sk = re.search(r"(\d+)\s+skills", body)
    m_paths = re.search(r"(\d+)\+?\s+API paths", body)
    if m_sk:
        out["claimed_skills"] = int(m_sk.group(1))
    if m_paths:
        out["claimed_api_paths"] = int(m_paths.group(1))
    return out


def check_count_drift() -> list[Finding]:
    findings: list[Finding] = []
    claimed = _claimed_counts()
    live_skills = _live_skill_count()

    if "claimed_skills" in claimed and live_skills is not None:
        if claimed["claimed_skills"] != live_skills:
            findings.append(Finding(
                check="count_drift_skills",
                severity=SEVERITY_BLOCKER,
                summary=(
                    f"Skill count drift: guide says {claimed['claimed_skills']}, "
                    f"live agent card advertises {live_skills}"
                ),
                evidence={
                    "claimed": claimed["claimed_skills"],
                    "live": live_skills,
                    "claimed_source": claimed["source"],
                    "live_source": BASE + "/.well-known/agent-card.json",
                },
                remediation=(
                    "The skill catalogue is generated; the guide's number is "
                    "hand-typed. Replace the literal with a build-time "
                    "injection from the agent card so it can never drift."
                ),
            ))
        else:
            findings.append(Finding(
                check="count_drift_skills", severity=SEVERITY_OK,
                summary=f"Skill count consistent ({live_skills}).",
                evidence={"live": live_skills},
            ))

    # API-path claim: the guide promises a single /openapi.yaml; reality is N
    # split specs. We report the structural mismatch rather than a raw number.
    spec_count = _live_openapi_spec_count()
    if "claimed_api_paths" in claimed and spec_count is not None:
        findings.append(Finding(
            check="count_drift_paths",
            severity=SEVERITY_WARN,
            summary=(
                f"Guide promises one consolidated spec with "
                f"{claimed['claimed_api_paths']}+ paths, but the live index "
                f"ships {spec_count} separate per-service OpenAPI files and no "
                f"consolidated spec."
            ),
            evidence={
                "claimed_api_paths": claimed["claimed_api_paths"],
                "live_split_spec_files": spec_count,
                "consolidated_spec_url": BASE + "/openapi.yaml",
            },
            remediation=(
                "Decide on one contract shape. Either build & publish the "
                "consolidated openapi.yaml the docs promise, or rewrite the "
                "guide to point at the per-service specs in /docs/openapi/."
            ),
        ))
    return findings


# --------------------------------------------------------------------------
# Check 3: localization coverage
# --------------------------------------------------------------------------
def check_localization() -> list[Finding]:
    code, body = _fetch(BASE + "/docs/llms.txt")
    if code != 200 or not body:
        return [Finding("localization", SEVERITY_WARN,
                        "Could not fetch llms.txt to measure ZH coverage.",
                        {"http_status": code})]
    doc_links = re.findall(r"https://aisa\.one/docs/[^\s)]+", body)
    total = len(doc_links)
    zh_links = [u for u in doc_links if re.search(r"(?:-zh|/zh|chinese)", u, re.I)]
    pct = round(100 * len(zh_links) / total, 1) if total else 0.0
    sev = SEVERITY_BLOCKER if pct < 5 else (SEVERITY_WARN if pct < 25 else SEVERITY_OK)
    return [Finding(
        check="localization_zh",
        severity=sev,
        summary=(
            f"Chinese doc coverage is {pct}% ({len(zh_links)}/{total} indexed "
            f"pages). China is the gateway's headline model-supply market."
        ),
        evidence={
            "zh_pages": len(zh_links),
            "total_pages": total,
            "zh_share_pct": pct,
            "examples": zh_links[:8],
        },
        remediation=(
            "Stand up a zh-CN docs tree mirroring the EN tree. Prioritise the "
            "first-success path: quickstart + chinese-llms + auth. Drive it "
            "from the same source via an automated translate-and-PR agent."
        ),
    )]


# --------------------------------------------------------------------------
# Check 4: freshness
# --------------------------------------------------------------------------
def check_freshness(max_age_days: int = 60) -> list[Finding]:
    findings: list[Finding] = []
    pages = [
        "/docs/guides/chinese-llms.md",
        "/docs/guides/getting-started-with-aisa.md",
    ]
    today = _dt.date.today()
    date_pat = re.compile(
        r"(January|February|March|April|May|June|July|August|September|"
        r"October|November|December)\s+(\d{1,2}),?\s+(\d{4})")
    months = {m: i for i, m in enumerate(
        ["January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"], 1)}
    for path in pages:
        code, body = _fetch(BASE + path)
        if code != 200 or not body:
            continue
        m = re.search(r"(?:refreshed|updated|last update[d]?)[^.\n]{0,40}?"
                      + date_pat.pattern, body, re.I)
        if not m:
            continue
        try:
            d = _dt.date(int(m.group(3)), months[m.group(1)], int(m.group(2)))
        except Exception:
            continue
        age = (today - d).days
        sev = SEVERITY_WARN if age > max_age_days else SEVERITY_OK
        findings.append(Finding(
            check="freshness",
            severity=sev,
            summary=f"{path} last refreshed {d.isoformat()} ({age} days ago).",
            evidence={"page": BASE + path, "stamp": d.isoformat(), "age_days": age},
            remediation=("Wire the 'refreshed' stamp to the auto-sync workflow "
                         "so it reflects the last successful gateway sync."),
        ))
    return findings


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------
def run_audit() -> dict:
    findings: list[Finding] = []
    findings += check_discovery_endpoints()
    findings += check_count_drift()
    findings += check_localization()
    findings += check_freshness()

    counts = {SEVERITY_BLOCKER: 0, SEVERITY_WARN: 0, SEVERITY_OK: 0}
    for f in findings:
        counts[f.severity] = counts.get(f.severity, 0) + 1

    return {
        "tool": "aisa-doc-reality-auditor",
        "version": "1.0",
        "generated_at": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "target": BASE,
        "summary": counts,
        "findings": [asdict(f) for f in findings],
    }


def to_markdown(report: dict) -> str:
    icon = {SEVERITY_BLOCKER: "🔴", SEVERITY_WARN: "🟡", SEVERITY_OK: "🟢"}
    s = report["summary"]
    lines = [
        "# AIsa Doc Reality Audit",
        "",
        f"- **Target:** {report['target']}",
        f"- **Run (UTC):** {report['generated_at']}",
        f"- **Result:** {s.get('BLOCKER',0)} blockers · "
        f"{s.get('WARN',0)} warnings · {s.get('OK',0)} ok",
        "",
        "| Sev | Check | Finding |",
        "|-----|-------|---------|",
    ]
    order = {SEVERITY_BLOCKER: 0, SEVERITY_WARN: 1, SEVERITY_OK: 2}
    for f in sorted(report["findings"], key=lambda x: order[x["severity"]]):
        lines.append(f"| {icon[f['severity']]} | `{f['check']}` | {f['summary']} |")
    lines.append("")
    blockers = [f for f in report["findings"] if f["severity"] == SEVERITY_BLOCKER]
    if blockers:
        lines.append("## Blockers — detail & remediation")
        lines.append("")
        for f in blockers:
            lines.append(f"### {f['summary']}")
            lines.append("")
            lines.append("```json")
            lines.append(json.dumps(f["evidence"], indent=2, ensure_ascii=False))
            lines.append("```")
            lines.append(f"**Fix:** {f['remediation']}")
            lines.append("")
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Audit AIsa docs against live reality.")
    ap.add_argument("--json", metavar="PATH", help="write machine report to PATH")
    ap.add_argument("--md", metavar="PATH", help="write markdown report to PATH")
    ap.add_argument("--ci", action="store_true",
                    help="exit non-zero if any BLOCKER is found")
    args = ap.parse_args(argv)

    report = run_audit()

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2, ensure_ascii=False)
    md = to_markdown(report)
    if args.md:
        with open(args.md, "w", encoding="utf-8") as fh:
            fh.write(md)
    print(md)

    if args.ci and report["summary"].get(SEVERITY_BLOCKER, 0) > 0:
        print(f"\n::error::Doc reality check failed: "
              f"{report['summary']['BLOCKER']} blocker(s).", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
