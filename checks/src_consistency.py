#!/usr/bin/env python3
"""AIsa 文档源码一致性静态检查器（阶段一交付物）。

只读 `AIsa-team/docs` 源仓库文件，判定确凿的文档硬伤。不发任何 live 网络请求，
对同一仓库多次运行结果稳定（确定性）。零误报是红线：凡标为 BLOCKER 的结论，
都必须能仅凭源仓库文件人工复核证伪。

真值来源：
  - 已提交的 openapi.yaml —— 线上 API 参考正文内联渲染所依据的同一份 spec。
    散文里关于 spec 形态（路径数 / schema 数 / 分类数）的断言，直接与它比对。
  - 目录实际计数 —— agent-skills 页数、总 .mdx 页数、中文页数。

用法:
    python checks/src_consistency.py --repo ~/files/aisa-team-docs
    python checks/src_consistency.py --repo <path> --format md
    python checks/src_consistency.py --repo <path> --ci   # 有 BLOCKER 则退出码 1

依赖: PyYAML（源仓库自身的 consolidate 脚本亦依赖它）。
"""

import argparse
import json
import os
import re
import sys
from datetime import date

try:
    import yaml
except ImportError:
    print(
        "ERROR: 需要 PyYAML 解析 openapi.yaml。安装: pip install --user pyyaml",
        file=sys.stderr,
    )
    sys.exit(2)


# ──────────────────────────────────────────────────────────────────
# 真值层：仅从源仓库文件计算事实，不依赖任何网络请求
# ──────────────────────────────────────────────────────────────────

HTTP_METHODS = ("get", "post", "put", "patch", "delete")


def _iter_mdx(repo):
    for root, dirs, files in os.walk(repo):
        # 原地裁剪隐藏目录（.git 等），不误伤仓库根
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fn in files:
            if fn.endswith(".mdx"):
                yield os.path.join(root, fn)


def compute_truth(repo):
    """从源仓库文件计算全部真值。返回 dict，每个键附带复现命令。"""
    truth = {}

    # —— OpenAPI 已提交产物 openapi.yaml ——
    spec_path = os.path.join(repo, "openapi.yaml")
    with open(spec_path, "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)
    paths = spec.get("paths", {})
    tag_op_counts = {}
    for _p, ops in paths.items():
        for method, op in ops.items():
            if method in HTTP_METHODS and isinstance(op, dict):
                for t in op.get("tags", []):
                    tag_op_counts[t] = tag_op_counts.get(t, 0) + 1
    truth["spec_paths"] = len(paths)
    truth["spec_operations"] = sum(
        1 for ops in paths.values() for m in ops if m in HTTP_METHODS
    )
    truth["spec_schemas"] = len(spec.get("components", {}).get("schemas", {}))
    truth["spec_tags_declared"] = len(spec.get("tags", []))
    # 只统计真正承载操作的 tag，避免把空 tag 误算进“分类数”
    truth["spec_tags_with_ops"] = sorted(tag_op_counts)
    truth["spec_tag_op_counts"] = dict(sorted(tag_op_counts.items()))

    # —— 目录计数 ——
    all_mdx = sorted(_iter_mdx(repo))
    truth["total_mdx"] = len(all_mdx)
    truth["agent_skills_count"] = sum(
        1 for p in all_mdx if os.path.relpath(p, repo).startswith("agent-skills" + os.sep)
    )
    zh_re = re.compile(r"(zh|chinese|/cn|\\cn)", re.IGNORECASE)
    truth["zh_pages"] = sorted(
        os.path.relpath(p, repo) for p in all_mdx if zh_re.search(os.path.relpath(p, repo))
    )
    return truth


# ──────────────────────────────────────────────────────────────────
# 规则层：每条规则只判定能仅凭源码证伪的事
# ──────────────────────────────────────────────────────────────────

def _find_line(text, needle):
    """返回 needle 首次出现的 1-based 行号，找不到返回 None。"""
    for i, line in enumerate(text.splitlines(), 1):
        if needle in line:
            return i
    return None


def rule_spec_stat_claims(repo, truth):
    """规则 1 · spec 形态断言一致性。

    在 guides/ 散文中抽取关于 OpenAPI spec 的可量化断言（路径数、schema 数、
    分类数），与 openapi.yaml 真值比对。
      - 精确数字（无 “+” 限定）与真值矛盾 → BLOCKER（源码可直接证伪）。
      - 限定数字（“N+”）且真值 ≥ N → 断言为真，但若真值 ≥ 2N 视为陈旧低估 → INFO。
    """
    findings = []
    guides_dir = os.path.join(repo, "guides")

    # 断言模式 → 真值键。每个模式捕获 (数字, 可选的 '+')。
    specs = [
        # "121 schemas" / "121 schema"
        (re.compile(r"(\d+)(\+?)\s+schemas?\b", re.IGNORECASE), "spec_schemas", "schema"),
        # "111+ API paths" / "111 paths" / "111+ endpoints"
        (re.compile(r"(\d+)(\+?)\s+(?:API\s+)?(?:paths|endpoints)\b", re.IGNORECASE),
         "spec_paths", "path/endpoint"),
        # "10 categories"
        (re.compile(r"(\d+)(\+?)\s+categories\b", re.IGNORECASE),
         "spec_tags_with_ops_count", "category"),
    ]

    # 仅当断言确实是在描述“整份 consolidated spec”时才与全量真值比对。
    # 行内须出现以下任一全量 spec 标记，否则可能是某个子服务的局部计数
    # （如 changelog 里 “CoinGecko API (23 Endpoints)” 指的是单个集成），
    # 拿它对全量真值定罪即是误报。
    whole_spec_marker = re.compile(
        r"(openapi\.yaml|consolidated\s+OpenAPI|OpenAPI\s+(?:3\.1\s+)?[Ss]pec|"
        r"the\s+spec\b|machine-readable\s+(?:specification|contract))",
        re.IGNORECASE,
    )

    for fn in sorted(os.listdir(guides_dir)) if os.path.isdir(guides_dir) else []:
        if not fn.endswith(".mdx"):
            continue
        fpath = os.path.join(guides_dir, fn)
        rel = os.path.relpath(fpath, repo)
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        for lineno, line in enumerate(lines, 1):
            if not whole_spec_marker.search(line):
                continue  # 非全量 spec 语境，跳过，杜绝局部计数误报
            for pat, truth_key, label in specs:
                for m in pat.finditer(line):
                    claimed = int(m.group(1))
                    qualified = m.group(2) == "+"
                    if truth_key == "spec_tags_with_ops_count":
                        actual = len(truth["spec_tags_with_ops"])
                    else:
                        actual = truth[truth_key]
                    if not qualified and claimed != actual:
                        findings.append({
                            "rule": "spec_stat_claims",
                            "severity": "BLOCKER",
                            "title": f"spec {label} 数断言与产物矛盾：写 {claimed}，实为 {actual}",
                            "file": rel,
                            "line": lineno,
                            "claimed": claimed,
                            "actual": actual,
                            "evidence": line.strip(),
                            "reproduce": _reproduce_for(truth_key),
                        })
                    elif qualified and actual >= 2 * claimed:
                        findings.append({
                            "rule": "spec_stat_claims",
                            "severity": "INFO",
                            "title": f"spec {label} 数严重低估：写 {claimed}+，实为 {actual}",
                            "file": rel,
                            "line": lineno,
                            "claimed": claimed,
                            "actual": actual,
                            "evidence": line.strip(),
                            "reproduce": _reproduce_for(truth_key),
                        })
    return findings


def _reproduce_for(truth_key):
    cmds = {
        "spec_schemas":
            "python3 -c \"import yaml;d=yaml.safe_load(open('openapi.yaml'));"
            "print(len(d['components']['schemas']))\"",
        "spec_paths":
            "python3 -c \"import yaml;d=yaml.safe_load(open('openapi.yaml'));"
            "print(len(d['paths']))\"",
        "spec_tags_with_ops_count":
            "python3 -c \"import yaml;d=yaml.safe_load(open('openapi.yaml'));"
            "t=set();[t.add(x) for p in d['paths'].values() for m,o in p.items() "
            "if m in ('get','post','put','patch','delete') and isinstance(o,dict) "
            "for x in o.get('tags',[])];print(len(t))\"",
    }
    return cmds.get(truth_key, "")


def rule_category_table_coverage(repo, truth):
    """规则 2 · API 分类表完整性。

    `guides/agent-discovery.mdx` 的 “API Categories” 表声称“spec 把端点组织为以下
    分类组”，但只列出一部分。把表中列出的分类名与 spec 中真正承载操作的 tag 集合
    比对，遗漏的（且确实承载操作的）分类 → BLOCKER（spec 可直接证伪遗漏）。
    """
    findings = []
    fpath = os.path.join(repo, "guides", "agent-discovery.mdx")
    if not os.path.isfile(fpath):
        return findings
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # 定位 “### API Categories” 之后的表格，抽取第一列分类名
    in_section = False
    table_start = None
    listed = []  # (name, lineno)
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("### API Categories"):
            in_section = True
            continue
        if in_section:
            if line.startswith("##") and not line.startswith("###"):
                break  # 进入下一节
            if re.match(r"^\|\s*:?-+", line):  # 分隔行
                table_start = table_start or i
                continue
            m = re.match(r"^\|\s*([^|]+?)\s*\|", line)
            if m:
                cell = m.group(1).strip()
                if cell and cell.lower() != "category":
                    listed.append((cell, i))

    if not listed:
        return findings

    table_lineno = listed[0][1]

    # 归一化名称做集合比较（spec 用 "Twitter / X"，散文用 "Twitter/X"）
    def norm(s):
        return re.sub(r"\s+", "", s).lower()

    listed_norm = {norm(n) for n, _ in listed}
    spec_tags = truth["spec_tags_with_ops"]
    missing = [t for t in spec_tags if norm(t) not in listed_norm]

    if missing:
        findings.append({
            "rule": "category_table_coverage",
            "severity": "BLOCKER",
            "title": (
                f"API 分类表不完整：列出 {len(listed)} 类，spec 实有 "
                f"{len(spec_tags)} 个承载操作的分类，遗漏 {len(missing)} 个"
            ),
            "file": os.path.relpath(fpath, repo),
            "line": table_lineno,
            "claimed": len(listed),
            "actual": len(spec_tags),
            "missing": [
                {"tag": t, "operations": truth["spec_tag_op_counts"][t]} for t in missing
            ],
            "evidence": "; ".join(
                f"{t}({truth['spec_tag_op_counts'][t]} ops)" for t in missing
            ),
            "reproduce": _reproduce_for("spec_tags_with_ops_count"),
        })
    return findings


def rule_localization_coverage(repo, truth):
    """规则 3 · 本地化覆盖率（统计，非阻断）。

    统计中文页占比。内容缺口而非源码可证伪的“错误”，恒为 INFO。
    """
    total = truth["total_mdx"]
    zh = len(truth["zh_pages"])
    ratio = (zh / total * 100) if total else 0.0
    return [{
        "rule": "localization_coverage",
        "severity": "INFO",
        "title": f"中文覆盖率 {ratio:.1f}%（{zh}/{total}）",
        "file": ".",
        "line": 0,
        "claimed": None,
        "actual": zh,
        "evidence": "；".join(truth["zh_pages"]),
        "reproduce": (
            "find . -name '*.mdx' | grep -iE 'zh|chinese|/cn' | wc -l  # 分子\n"
            "find . -name '*.mdx' | wc -l  # 分母"
        ),
    }]


RULES = [
    rule_spec_stat_claims,
    rule_category_table_coverage,
    rule_localization_coverage,
]


# ──────────────────────────────────────────────────────────────────
# 运行 + 输出
# ──────────────────────────────────────────────────────────────────

SEVERITY_ORDER = {"BLOCKER": 0, "INFO": 1}


def run(repo):
    truth = compute_truth(repo)
    findings = []
    for rule in RULES:
        findings.extend(rule(repo, truth))
    # 确定性排序：严重度 → 文件 → 行号 → 标题
    findings.sort(key=lambda f: (
        SEVERITY_ORDER.get(f["severity"], 9), f["file"], f["line"], f["title"]
    ))
    return truth, findings


def build_report(repo, truth, findings):
    blockers = [f for f in findings if f["severity"] == "BLOCKER"]
    infos = [f for f in findings if f["severity"] == "INFO"]
    return {
        "tool": "checks/src_consistency.py",
        "repo": os.path.abspath(repo),
        "generated": date.today().isoformat(),
        "truth": {
            "spec_paths": truth["spec_paths"],
            "spec_operations": truth["spec_operations"],
            "spec_schemas": truth["spec_schemas"],
            "spec_tags_declared": truth["spec_tags_declared"],
            "spec_tags_with_ops": truth["spec_tags_with_ops"],
            "spec_tag_op_counts": truth["spec_tag_op_counts"],
            "total_mdx": truth["total_mdx"],
            "agent_skills_count": truth["agent_skills_count"],
            "zh_pages_count": len(truth["zh_pages"]),
        },
        "summary": {"blocker": len(blockers), "info": len(infos), "total": len(findings)},
        "findings": findings,
    }


def to_markdown(report):
    t = report["truth"]
    lines = []
    lines.append("# AIsa 文档硬伤报告")
    lines.append("")
    lines.append(f"> 生成日期：{report['generated']}　·　检查器：`{report['tool']}`")
    lines.append(f"> 源仓库：`{report['repo']}`")
    lines.append("")
    s = report["summary"]
    lines.append(f"本轮检出 **{s['blocker']} 项阻断硬伤（BLOCKER）**、{s['info']} 项提示（INFO）。"
                 "全部结论仅凭源仓库文件即可复核，零 live 请求。")
    lines.append("")
    lines.append("## 真值快照")
    lines.append("")
    lines.append("| 指标 | 数值 |")
    lines.append("| --- | --- |")
    lines.append(f"| openapi.yaml 路径数 | {t['spec_paths']} |")
    lines.append(f"| 操作数 | {t['spec_operations']} |")
    lines.append(f"| schema 数 | {t['spec_schemas']} |")
    lines.append(f"| 承载操作的分类（tag）数 | {len(t['spec_tags_with_ops'])} |")
    lines.append(f"| 总 .mdx 页 | {t['total_mdx']} |")
    lines.append(f"| 中文页 | {t['zh_pages_count']} |")
    lines.append("")

    if any(f["severity"] == "BLOCKER" for f in report["findings"]):
        lines.append("## 阻断硬伤（BLOCKER）")
        lines.append("")
        for i, f in enumerate([x for x in report["findings"] if x["severity"] == "BLOCKER"], 1):
            lines.append(f"### B{i} · {f['title']}")
            lines.append("")
            lines.append(f"- 位置：`{f['file']}`" + (f":{f['line']}" if f['line'] else ""))
            lines.append(f"- 散文写：`{f['claimed']}`　真值：`{f['actual']}`")
            if f.get("missing"):
                miss = "、".join(f"{m['tag']}（{m['operations']} 操作）" for m in f["missing"])
                lines.append(f"- 遗漏分类：{miss}")
            if f.get("evidence"):
                lines.append(f"- 证据：{f['evidence']}")
            lines.append(f"- 复现：")
            lines.append("")
            lines.append("  ```bash")
            for cl in f["reproduce"].splitlines():
                lines.append(f"  {cl}")
            lines.append("  ```")
            lines.append("")

    infos = [x for x in report["findings"] if x["severity"] == "INFO"]
    if infos:
        lines.append("## 提示与内容缺口（INFO）")
        lines.append("")
        for f in infos:
            loc = f"`{f['file']}`" + (f":{f['line']}" if f['line'] else "")
            lines.append(f"- **{f['title']}** —— {loc}")
        lines.append("")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="AIsa 文档源码一致性静态检查器")
    p.add_argument("--repo", required=True, help="AIsa-team/docs 源仓库工作副本路径")
    p.add_argument("--format", choices=["json", "md", "both"], default="both")
    p.add_argument("--out-json", default=None, help="JSON 输出路径")
    p.add_argument("--out-md", default=None, help="Markdown 输出路径")
    p.add_argument("--ci", action="store_true", help="检出 BLOCKER 时退出码 1")
    args = p.parse_args()

    repo = os.path.expanduser(args.repo)
    if not os.path.isfile(os.path.join(repo, "openapi.yaml")):
        print(f"ERROR: {repo} 下找不到 openapi.yaml，确认是 AIsa-team/docs 工作副本。",
              file=sys.stderr)
        sys.exit(2)

    truth, findings = run(repo)
    report = build_report(repo, truth, findings)

    md = to_markdown(report)
    js = json.dumps(report, ensure_ascii=False, indent=2)

    if args.out_json:
        with open(args.out_json, "w", encoding="utf-8") as f:
            f.write(js + "\n")
    if args.out_md:
        with open(args.out_md, "w", encoding="utf-8") as f:
            f.write(md + "\n")

    if not args.out_json and not args.out_md:
        if args.format in ("md", "both"):
            print(md)
        if args.format == "both":
            print("\n" + "=" * 60 + "\n", file=sys.stderr)
        if args.format in ("json", "both"):
            print(js)

    if args.ci and report["summary"]["blocker"] > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
