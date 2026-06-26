#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extract_annotations.py — 待研发确认清单：提取全部 109 条批注。

权威来源：ws-v2/<name>/content.json 的 annotation 字段（共 109，全部字段级）。
native 上下文（type / 原描述 en）：复用 inject_xdoc 的解析器在源 spec
(/home/mira/files/aisa-team-docs/openapi/<name>.json) 上按 opKey + dotpath 定位节点。
定位不到的（如 agentmail 重名 operationId 兄弟 path、扁平 key 边界）留空——不杜撰。

输出列：spec / operation(接口) / location(参数|请求|返回[状态码]) / field(字段) /
        type(数据类型) / desc_native_en(原描述) / desc_enhanced_en(改后描述) / annotation(批注)
落 reports/annotations-for-dev-2026-06-26.{csv,md}。
"""
import json
import os
import sys
import csv
from collections import Counter

ROOT = "/home/mira/files/aisa-docs-voyager"
WS = os.path.join(ROOT, "ws-v2")
SRC = "/home/mira/files/aisa-team-docs/openapi"
OUT_CSV = os.path.join(ROOT, "reports/annotations-for-dev-2026-06-26.csv")
OUT_MD = os.path.join(ROOT, "reports/annotations-for-dev-2026-06-26.md")

sys.path.insert(0, os.path.join(ROOT, "skill-local/aisa-doc-enhance/tools"))
import inject_xdoc as IX  # noqa: E402


def node_type(node):
    if not isinstance(node, dict):
        return ""
    t = node.get("type")
    sch = node.get("schema") if isinstance(node.get("schema"), dict) else None
    base = node
    if not t and sch:
        base = sch
        t = sch.get("type")
    if t == "array":
        items = base.get("items") if isinstance(base.get("items"), dict) else {}
        it = items.get("type")
        if it:
            t = "array<%s>" % it
    if t:
        fmt = base.get("format")
        if fmt:
            t = "%s(%s)" % (t, fmt)
        return t
    for comb in ("oneOf", "anyOf", "allOf"):
        if base.get(comb):
            return comb
    if base.get("$ref"):
        return "$ref"
    return ""


def build_op_index(spec):
    """opKey -> (method, path, op-node) 列表（一个 opKey 可能对应多条同名 path）。"""
    idx = {}
    for path, item in (spec.get("paths") or {}).items():
        if not isinstance(item, dict):
            continue
        for method in IX.HTTP_METHODS:
            op = item.get(method)
            if isinstance(op, dict):
                key = IX.op_key(method, path, op)
                idx.setdefault(key, []).append((method, path, op))
    return idx


def resolve_field(spec, opnodes, location, code, dotpath):
    """在该 opKey 的所有 path 上尝试解析字段节点，返回首个命中的 (node, native_desc, type)。"""
    for method, path, op in opnodes:
        node = None
        if location == "parameter":
            for p in (op.get("parameters") or []):
                if isinstance(p, dict) and p.get("name") == dotpath:
                    node = p
                    break
        elif location == "request":
            sch = (((op.get("requestBody") or {}).get("content") or {})
                   .get("application/json") or {}).get("schema")
            sch = IX._deref(spec, sch)
            if isinstance(sch, dict):
                node = IX.resolve_property(sch, dotpath, spec)
        elif location == "response":
            resp = (op.get("responses") or {}).get(code) or (op.get("responses") or {}).get(str(code))
            if isinstance(resp, dict):
                sch = ((resp.get("content") or {}).get("application/json") or {}).get("schema")
                sch = IX._deref(spec, sch)
                if isinstance(sch, dict):
                    node = IX.resolve_property(sch, dotpath, spec)
        if isinstance(node, dict):
            nd = (node.get("description") or "").strip().replace("\n", " ")
            return node, nd, node_type(node)
    return None, "", ""


def leaf_name(dotpath):
    # 字段名：dotpath 末段（兼容扁平点号整键——取最后一个 . 后部分）
    return dotpath.rsplit(".", 1)[-1] if dotpath else ""


def collect():
    rows = []
    specs = sorted(d for d in os.listdir(WS)
                   if os.path.isdir(os.path.join(WS, d))
                   and os.path.exists(os.path.join(WS, d, "content.json")))
    for name in specs:
        content = json.load(open(os.path.join(WS, name, "content.json"), encoding="utf-8"))
        srcpath = os.path.join(SRC, name + ".json")
        spec = json.load(open(srcpath, encoding="utf-8")) if os.path.exists(srcpath) else {}
        opidx = build_op_index(spec) if spec else {}

        for opkey, blk in (content.get("fields") or {}).items():
            opnodes = opidx.get(opkey, [])
            # 接口可读名：取该 opKey 第一条 path
            if opnodes:
                m, p, _ = opnodes[0]
                op_label = "%s %s" % (m.upper(), p)
            else:
                op_label = opkey

            def emit(location, code, dmap):
                for dotpath, citem in (dmap or {}).items():
                    if not isinstance(citem, dict):
                        continue
                    ann = (citem.get("annotation") or "").strip()
                    if not ann:
                        continue
                    _, nd, tp = resolve_field(spec, opnodes, location, code, dotpath)
                    loc_label = {"parameter": "参数(parameter)",
                                 "request": "请求体(request)",
                                 "response": "返回(response %s)" % code}[location]
                    rows.append({
                        "spec": name,
                        "operation": op_label,
                        "location": loc_label,
                        "field": dotpath if location != "parameter" else leaf_name(dotpath),
                        "type": tp,
                        "desc_native_en": nd,
                        "desc_enhanced_en": (citem.get("desc_en") or "").strip().replace("\n", " "),
                        "annotation": ann,
                    })

            emit("parameter", "", blk.get("parameters"))
            emit("request", "", blk.get("request"))
            for code, dmap in (blk.get("response") or {}).items():
                emit("response", code, dmap)

    rows.sort(key=lambda r: (r["spec"], r["operation"], r["location"], r["field"]))
    return rows


def write_csv(rows):
    cols = ["spec", "operation", "location", "field", "type",
            "desc_native_en", "desc_enhanced_en", "annotation"]
    with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def md_cell(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").strip() or "—"


def write_md(rows):
    by_spec = Counter(r["spec"] for r in rows)
    resolved = sum(1 for r in rows if r["desc_native_en"] or r["type"])
    lines = []
    lines.append("# 批注待研发确认清单（API 文档加强 · 109 条硬事实缺口）\n")
    lines.append("> 受众：AIsa 研发。这些是源 spec **未声明清楚**、文档加强时**拒绝杜撰**而显式留痕的硬事实缺口"
                 "（哈希算法取值、内部标志业务含义、运算符全集、单位/上限等）。每条都需研发补全权威说明，"
                 "补全后即可去批注、把描述升级为确定表述。\n")
    lines.append("> 来源：`ws-v2/<spec>/content.json` 的 `annotation` 字段；native 上下文由 "
                 "`ws-v2/extract_annotations.py` 在源 spec（pinned `16863d3`）上按 opKey+dotpath 解析。"
                 "复现：`python3 ws-v2/extract_annotations.py`。\n")
    lines.append("\n## 一、规模与分布\n")
    lines.append("| 指标 | 数值 |")
    lines.append("| --- | --- |")
    lines.append("| 批注总数 | **%d** |" % len(rows))
    lines.append("| 涉及 spec 数 | %d |" % len(by_spec))
    lines.append("| 可解析到 native 节点（带类型/原描述） | %d |" % resolved)
    lines.append("\n按 spec 分布（密度最高的三档占 %d/%d）：\n"
                 % (sum(n for s, n in by_spec.most_common(3)), len(rows)))
    lines.append("| spec | 批注数 |")
    lines.append("| --- | --- |")
    for s, n in by_spec.most_common():
        lines.append("| %s | %d |" % (s, n))
    lines.append("\n## 二、明细清单\n")
    lines.append("> 列含义：**接口** = METHOD + path；**位置** = 参数/请求体/返回（含状态码）；"
                 "**字段** = 参数名或字段 dotpath；**原描述** = 源 spec 原生英文（空=源未写）；"
                 "**改后描述** = 加强英文（已去内联批注）。\n")
    lines.append("| # | spec | 接口 | 位置 | 字段 | 类型 | 原描述(en) | 改后描述(en) | 批注（待研发确认） |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for i, r in enumerate(rows, 1):
        lines.append("| %d | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            i, md_cell(r["spec"]), md_cell(r["operation"]), md_cell(r["location"]),
            md_cell(r["field"]), md_cell(r["type"]),
            md_cell(r["desc_native_en"]), md_cell(r["desc_enhanced_en"]),
            md_cell(r["annotation"])))
    lines.append("")
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    rows = collect()
    write_csv(rows)
    write_md(rows)
    by_spec = Counter(r["spec"] for r in rows)
    print("TOTAL:", len(rows))
    print("resolved native:", sum(1 for r in rows if r["desc_native_en"] or r["type"]))
    print("by spec:", dict(by_spec.most_common()))


if __name__ == "__main__":
    main()
