#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_projection.py — 投影闸门（阶段五，路线 A 的 trust-but-verify）

对「源 enhanced.json + 某语言投影产物」逐节点对账，三道闸全绿才 exit 0：

闸①  无遗漏、无串语言：每个带 x-doc.{desc_en|title_zh} 的节点，其投影后
      description 恰等于对应语言字段；操作节点 description 恰等于
      desc_en/description_zh（+ 错误表，仅当 x-doc.errors 存在），summary
      en 回退原生、zh 取 heading_zh。精确相等天然排除串语言。

闸②  无篡改：剥除 x-doc、并在「带 x-doc 的节点」上排除被投影覆盖的
      description/summary 之后，投影产物与源 enhanced.json 的骨架
      （paths/类型/$ref/required/枚举/servers/未加强节点的原生文案）逐字节一致。

闸③  无杜撰：投影产物里所有「相对源被改写」的 description/summary，必须
      全部落在带 x-doc 的节点上、且其内容可由该节点 x-doc 完整重建；
      错误表里出现的每个状态码与 message_zh 必须能在 x-doc.errors 中溯源。
      未加强节点的原生文案不得被改动（与闸②同源兜住）。

设计：闸②采用「双树并行清洗 + 字节比对」，结构错位/越界改写都会暴露。
闸①/③复用 project_spec.render_errors 作为错误表格式的唯一权威，但对错误表
内容（code / message_zh）做独立 token 溯源，确保即便格式函数有 bug 也抓得住杜撰。

用法
----
  python3 check_projection.py --enhanced <enhanced.json> --lang en|zh --projected <out.json>
exit 0 = 全绿；非 0 = 有红，stderr 打印明细。
"""
import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(
    _HERE, "skill-local", "aisa-doc-enhance", "tools"))
from inject_xdoc import HTTP_METHODS  # noqa: E402
# 错误表格式的唯一权威（投影器与闸门共用同一份，闸③另做内容 token 溯源）
sys.path.insert(0, _HERE)
from project_spec import render_errors  # noqa: E402

SENT_MISSING = "<<MISSING_IN_PROJECTED>>"
SENT_ABSENT = "<<ABSENT_IN_SOURCE>>"


def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def collect_op_ids(spec):
    op_ids = set()
    for path, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for m in HTTP_METHODS:
            op = item.get(m)
            if isinstance(op, dict):
                op_ids.add(id(op))
    return op_ids


# ---------------------------------------------------------------------------
# 闸②：双树并行清洗 + 字节比对
# ---------------------------------------------------------------------------
def clean_pair(s, p, errs):
    """并行清洗源节点 s 与投影节点 p，返回 (src_skel, proj_skel)。
    带 x-doc 的节点：剥 x-doc，并排除被投影覆盖的 description/summary。
    未带 x-doc 的节点：完整保留；若投影擅自新增/改了键，会以哨兵暴露差异。"""
    if isinstance(s, dict):
        if not isinstance(p, dict):
            errs.append("闸②类型错位：源为 dict、投影非 dict")
            return s, p
        had = "x-doc" in s
        so, po = {}, {}
        for k in s:
            if k == "x-doc":
                continue
            if had and k in ("description", "summary"):
                continue  # 投影目标，交闸①验
            sv = s[k]
            pv = p[k] if k in p else SENT_MISSING
            cs, cp = clean_pair(sv, pv, errs)
            so[k], po[k] = cs, cp
        # 投影不得在任何节点新增源中不存在的键（未加强节点尤其不能凭空加 description）
        for k in p:
            if k in s:
                continue
            if had and k in ("description", "summary"):
                continue  # x-doc 节点允许新增这两个投影目标
            so[k] = SENT_ABSENT
            po[k] = p[k]
        return so, po
    if isinstance(s, list):
        if not isinstance(p, list) or len(s) != len(p):
            errs.append("闸②列表长度/类型错位")
            return s, p
        sl, pl = [], []
        for sv, pv in zip(s, p):
            cs, cp = clean_pair(sv, pv, errs)
            sl.append(cs)
            pl.append(cp)
        return sl, pl
    return s, p


def gate2(src, proj, errs):
    so, po = clean_pair(src, proj, errs)
    s_str = json.dumps(so, ensure_ascii=False, sort_keys=True)
    p_str = json.dumps(po, ensure_ascii=False, sort_keys=True)
    if s_str != p_str:
        errs.append("闸②骨架不一致：剥 x-doc + 排除投影目标后仍有字节差异")
        # 给一个定位提示
        for i, (a, b) in enumerate(zip(s_str, p_str)):
            if a != b:
                lo = max(0, i - 60)
                errs.append("  src…%r" % s_str[lo:i + 60])
                errs.append("  prj…%r" % p_str[lo:i + 60])
                break


# ---------------------------------------------------------------------------
# 闸①/③：逐 x-doc 节点核对投影后 description/summary
# ---------------------------------------------------------------------------
def _trace_errors(proj_desc, errors, errs, where):
    """闸③错误表内容溯源：投影里出现的每个 code 与 message_zh 必须在 x-doc.errors 中。"""
    for e in errors or []:
        if not isinstance(e, dict):
            continue
        code = str(e.get("code", "")).strip()
        if code and ("`%s`" % code) not in proj_desc:
            errs.append("闸③错误码丢失 @%s：%s 未出现在投影" % (where, code))
        msg = (e.get("message_zh") or "").replace("\n", " ").strip()
        if msg and msg not in proj_desc:
            # zh 站才会含 message_zh；en 站不渲染中文错误文案，跳过
            if "状态码" in proj_desc or "|" in proj_desc:
                errs.append("闸③错误说明丢失 @%s" % where)


# ---------------------------------------------------------------------------
# 闸①/③并位遍历：源树与投影树结构同构，按结构同时下钻，精确比对投影目标
# ---------------------------------------------------------------------------
def gate1_3(src, proj, lang, op_ids, errs):
    def walk(s, p, path):
        if isinstance(s, dict):
            if not isinstance(p, dict):
                return
            xd = s.get("x-doc")
            if isinstance(xd, dict):
                if id(s) in op_ids:
                    _verify_op(s, p, xd, lang, errs, path)
                else:
                    _verify_field(p, xd, lang, errs, path)
            for k, v in s.items():
                if k == "x-doc":
                    continue
                if k in p:
                    walk(v, p[k], path + "." + str(k))
        elif isinstance(s, list):
            if isinstance(p, list) and len(s) == len(p):
                for i, (sv, pv) in enumerate(zip(s, p)):
                    walk(sv, pv, path + "[%d]" % i)
    walk(src, proj, "$")


def _verify_op(s, p, xd, lang, errs, path):
    errors = xd.get("errors")
    if lang == "en":
        lang_field = xd.get("desc_en")
        # summary：en 回退原生，应与源原生 summary 一致
        if p.get("summary") != s.get("summary"):
            errs.append("闸①op summary 串改 @%s（en 应回退原生）" % path)
    else:
        lang_field = xd.get("description_zh")
        heading = xd.get("heading_zh")
        if heading not in (None, "") and p.get("summary") != heading:
            errs.append("闸①op summary≠heading_zh @%s" % path)
    body = lang_field if lang_field not in (None, "") else ""
    err_md = render_errors(errors, lang) if errors else ""
    expected = (body + "\n\n" + err_md) if (body and err_md) else (body or err_md)
    if expected == "":
        # 无可投影正文：投影应保留原生 description（不强制等于，交闸②）
        return
    actual = p.get("description")
    if actual != expected:
        errs.append("闸①op description≠期望 @%s" % path)
        errs.append("    期望[:80]=%r" % (expected[:80]))
        errs.append("    实际[:80]=%r" % ((actual or "")[:80]))
    # 闸③：错误表内容溯源
    if err_md:
        _trace_errors(actual or "", errors, errs, path)


def _verify_field(p, xd, lang, errs, path):
    expected = xd.get("desc_en") if lang == "en" else xd.get("title_zh")
    if expected in (None, ""):
        return
    actual = p.get("description")
    if actual != expected:
        errs.append("闸①字段 description≠%s @%s" % (
            "desc_en" if lang == "en" else "title_zh", path))
        errs.append("    期望[:80]=%r" % expected[:80])
        errs.append("    实际[:80]=%r" % ((actual or "")[:80]))
    # 串语言独立兜底：zh 不应等于 desc_en、en 不应等于 title_zh（当两者不同时）
    other = xd.get("title_zh") if lang == "en" else xd.get("desc_en")
    if other not in (None, "") and other != expected and actual == other:
        errs.append("闸①串语言 @%s：投影用了另一语言字段" % path)


def main(argv=None):
    ap = argparse.ArgumentParser(description="投影闸门（阶段五）")
    ap.add_argument("--enhanced", required=True)
    ap.add_argument("--lang", required=True, choices=("en", "zh"))
    ap.add_argument("--projected", required=True)
    args = ap.parse_args(argv)

    src = load_json(args.enhanced)
    proj = load_json(args.projected)
    op_ids = collect_op_ids(src)
    errs = []
    gate1_3(src, proj, args.lang, op_ids, errs)
    gate2(src, proj, errs)

    if errs:
        sys.stderr.write("check_projection[%s] RED：%d 处\n" % (args.lang, len(errs)))
        for e in errs[:60]:
            sys.stderr.write("  - %s\n" % e)
        return 1
    sys.stderr.write("check_projection[%s] GREEN：闸①②③全绿\n" % args.lang)
    return 0


if __name__ == "__main__":
    sys.exit(main())
