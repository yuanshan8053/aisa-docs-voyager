#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
project_spec.py — x-doc 投影器（阶段五，路线 A）

立场
----
Scalar / Redoc / Swagger UI 都是标准 OpenAPI 渲染器，只认原生
`summary` / `description`。阶段三的加强成果刻意挂在每个节点的 `x-doc`
子树里，原生字段保持未加强的英文基线。本工具按语言把 `x-doc` **投影**
进原生字段、剥掉 `x-doc`，产出干净标准 OpenAPI，让渲染器零改动直接吃。

它是一层加性、可逆、确定性的派生产物：原始 `enhanced.json` 永不改动，
投影只产生 `ws-site/{en,zh}/<name>.json`。配套 `check_projection.py`
逐节点对账「无遗漏、无篡改、无杜撰、无串语言」。

投影规则（与 planning/PHASE-5 A.2 一字对应，无任何兜底生成）
----------------------------------------------------------------
操作节点（operation）
  en: summary ← 原生 summary（无 heading_en，回退原生；缺则留空不编）
      description ← x-doc.desc_en
  zh: summary ← x-doc.heading_zh
      description ← x-doc.description_zh
  错误表：仅当 x-doc.errors 存在才渲染；只有 errors_source 时不造表。
          errors 条目只含 code + message_zh（源无英文错误文案）：
            zh 站渲染「状态码 | 说明」表（message_zh）；
            en 站源里没有英文错误文案，按「留空」红线只列状态码、不编英文。

字段节点（parameter / schema property）
  en: description ← x-doc.desc_en
  zh: description ← x-doc.title_zh
  批注（[⚠️Note:...] / [⚠️批注:...]）已内联在上述字符串里，随文案进
  description，一字不改、不剥除。

留空红线
  没有 x-doc 的节点：原样保留（原生 description 有则保、无则空），
  严禁用原生英文顶替缺失加强文案，严禁为留空处编造文字。
  注意：本工具只触碰带 x-doc 的节点，其余节点字节不动 —— 留空规则天然满足。

x-doc 之外的键（resp_section_intro / req_section_intro 等）不在 A.2 投影
映射内，不投影、随 x-doc 一并剥除（闸门①以「description 恰等于对应语言
字段 + 错误表」兜住，多投即红）。

穿透逻辑
--------
投影器不自己实现遍历穿透，直接 import 复用阶段三 inject_xdoc.py 的
descend_object / _deref / HTTP_METHODS / native_fragment，保证与注入器
语义不分叉（array items / oneOf|anyOf / allOf / $ref / 扁平点号整键）。
操作节点用与 inject 同款的 paths×methods 结构化定位；字段节点用全树兜底
遍历（凡带 x-doc 即投影），是注入路径的超集，深层字段不会漏投。

用法
----
  python3 project_spec.py --enhanced <enhanced.json> --lang en|zh --out <out.json>
"""
import argparse
import copy
import json
import os
import sys

# 复用注入器的穿透/解引用语义，绝不另起炉灶（A.5.8）
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(
    _HERE, "skill-local", "aisa-doc-enhance", "tools"))
from inject_xdoc import HTTP_METHODS  # noqa: E402


def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def dump_json(obj, p):
    os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


# ---------------------------------------------------------------------------
# 错误表渲染（投影器与闸门共享同一份确定性函数，便于逐字节对账）
# ---------------------------------------------------------------------------
def render_errors(errors, lang):
    """把 x-doc.errors（[{code, message_zh}, ...]）渲染成 Markdown。

    源里错误条目只有 code + message_zh，没有英文错误文案：
      · zh：状态码 + 说明 两列表；
      · en：源无英文错误文案，按「留空」红线只列状态码、不编英文。
    返回字符串（不含前导空行）；errors 为空返回 ""。
    返回值在投影器与闸门里必须完全一致。
    """
    if not errors:
        return ""
    rows = [e for e in errors if isinstance(e, dict) and e.get("code") not in (None, "")]
    if not rows:
        return ""
    if lang == "zh":
        out = ["**错误码**", "", "| 状态码 | 说明 |", "| --- | --- |"]
        for e in rows:
            code = str(e.get("code", "")).strip()
            msg = (e.get("message_zh") or "").replace("\n", " ").strip()
            out.append(f"| `{code}` | {msg} |")
        return "\n".join(out)
    # en：仅列状态码（源无英文错误文案，留空不编）
    codes = ", ".join(f"`{str(e.get('code','')).strip()}`" for e in rows)
    return "**Error status codes:** " + codes


# ---------------------------------------------------------------------------
# 投影核心
# ---------------------------------------------------------------------------
def _strip_xdoc(node):
    """递归剥除所有 x-doc 子树（就地）。"""
    if isinstance(node, dict):
        node.pop("x-doc", None)
        for v in node.values():
            _strip_xdoc(v)
    elif isinstance(node, list):
        for v in node:
            _strip_xdoc(v)


def _collect_op_ids(spec):
    """与 inject_xdoc 同款结构定位：paths.<path>.<method> 的 operation 节点。"""
    op_ids = set()
    for path, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for m in HTTP_METHODS:
            op = item.get(m)
            if isinstance(op, dict):
                op_ids.add(id(op))
    return op_ids


def _project_operation(op, lang, stats):
    """投影操作节点的 summary / description / 错误表。"""
    xd = op.get("x-doc")
    if not isinstance(xd, dict):
        return
    errors = xd.get("errors")
    if lang == "en":
        # summary 回退原生（无 heading_en）：原生 summary 已在节点上，原样不动；
        #   缺原生 summary 的 3 个操作留空不编。
        desc = xd.get("desc_en")
    else:
        heading = xd.get("heading_zh")
        if heading not in (None, ""):
            op["summary"] = heading
        desc = xd.get("description_zh")
    body = desc if desc not in (None, "") else ""
    err_md = render_errors(errors, lang) if errors else ""
    if err_md:
        body = (body + "\n\n" + err_md) if body else err_md
        stats["error_tables"] += 1
    # 只有在有可投影正文/错误表时才落 description；否则保留原生（留空红线）。
    if body != "":
        op["description"] = body
    stats["operations"] += 1


def _project_field(node, lang, stats):
    """投影字段节点（parameter / schema property）的 description。"""
    xd = node.get("x-doc")
    if not isinstance(xd, dict):
        return
    val = xd.get("desc_en") if lang == "en" else xd.get("title_zh")
    if val not in (None, ""):
        node["description"] = val
        stats["fields"] += 1


def _walk_project(node, lang, op_ids, stats):
    """全树遍历：操作节点走 op 投影、其余带 x-doc 节点走字段投影。
    投影后剥除该节点的 x-doc 在最后统一做（_strip_xdoc）。"""
    if isinstance(node, dict):
        if isinstance(node.get("x-doc"), dict):
            if id(node) in op_ids:
                _project_operation(node, lang, stats)
            else:
                _project_field(node, lang, stats)
        for v in node.values():
            _walk_project(v, lang, op_ids, stats)
    elif isinstance(node, list):
        for v in node:
            _walk_project(v, lang, op_ids, stats)


def project(spec, lang):
    spec = copy.deepcopy(spec)
    op_ids = _collect_op_ids(spec)
    stats = {"operations": 0, "fields": 0, "error_tables": 0}
    _walk_project(spec, lang, op_ids, stats)
    _strip_xdoc(spec)  # 产出干净标准 OpenAPI
    return spec, stats


def main(argv=None):
    ap = argparse.ArgumentParser(description="x-doc 投影器（阶段五，路线 A）")
    ap.add_argument("--enhanced", required=True, help="源 enhanced.json")
    ap.add_argument("--lang", required=True, choices=("en", "zh"))
    ap.add_argument("--out", required=True, help="投影产物路径")
    args = ap.parse_args(argv)

    spec = load_json(args.enhanced)
    if not isinstance(spec, dict):
        sys.stderr.write("ERROR: enhanced spec is not a JSON object.\n")
        return 2
    out, stats = project(spec, args.lang)
    dump_json(out, args.out)
    sys.stderr.write(
        "project_spec[%s]: ops=%d fields=%d error_tables=%d -> %s\n"
        % (args.lang, stats["operations"], stats["fields"],
           stats["error_tables"], args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
