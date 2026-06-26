#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inject_xdoc.py — 双字段 x-doc 加性注入器（standalone，不依赖任何外部引擎）

设计立场（与旧 inline_inject.py 的区别）
----------------------------------------
旧链路 import 了 /data/plugins 下的 doc_engine + spectral + renderer 一整套确定性引擎。
本工具按用户新策略「只吸收 doc 内核」彻底瘦身：

  · 不 import 任何包外引擎，**完全自包含**（派遣的 agent「只读本地改造后 skill」即可跑通）。
  · 不做渲染、不跑 spectral、不 hoist、不碰原生结构。
  · 它只做一件确定性的事：把 LLM 逐字段写好的 `content.json` 加性注入 spec 的 `x-doc`。
    —— 真正的智力工作(逐参数撰写)由 LLM 按 METHODOLOGY.md 完成,本脚本绝不替写、绝不套模板。

双字段模型（本次策略的核心改动）
--------------------------------
每个字段/参数/接口的 `x-doc` 同时承载三层、可逐层对账：
  原生 `description`(源英文,只读不动)  →  `x-doc.desc_en`(加强后的英文)  →  `x-doc.title_zh`(中文本地化)
这样「改了什么、改得更好还是更坏」可由 make_review.py 三栏并排一眼看清。

content.json 约定（扁平 dotpath，便于 LLM 逐字段撰写与人工复核）
----------------------------------------------------------------
{
  "operations": {
     "<opKey>": {                       # opKey = operationId,或 "METHOD /path"
        "heading_zh": "中文动作 + Action名",
        "desc_en":    "enhanced English one/two sentences",
        "description_zh": "中文接口描述",
        "resp_section_intro": "可选",
        "errors": [{"code":"400","message_zh":"..."}]   # 可选
     }
  },
  "fields": {
     "<opKey>": {
        "request":   { "<dotpath>": {"desc_en":"...","title_zh":"...","example":<any>,"annotation":"..."} },
        "response":  { "<code>": { "<dotpath>": {...} } },
        "parameters":{ "<name>": {"desc_en":"...","title_zh":"...","example":<any>,"annotation":"..."} }
     }
  }
}

dotpath 语义：以点号分隔的 property 名链;脚本逐段下钻,自动穿透数组的 items
（如 "messages.role" = properties.messages → items → properties.role）。

源保护红线（沿用 skill 的 R3–R6 精神,简化但忠实）
------------------------------------------------
节点已有 `x-doc.source ∈ {human, ai-reviewed}` 且本次内容不同 → **不覆盖**,记入 review。
新写/重写 AI 内容 → 打 source=ai + src_hash + doc_version。原生键一律不动。

用法：
  python3 inject_xdoc.py --spec in.json --content content.json \
      --out enhanced.json --review-out review.json [--doc-version 2.0.0]
"""
import argparse
import copy
import hashlib
import json
import sys

HTTP_METHODS = ("get", "post", "put", "delete", "patch", "head", "options")
PROTECTED_SOURCES = {"human", "ai-reviewed"}
XDOC_CONTENT_KEYS = ("desc_en", "title_zh", "heading_zh", "description_zh",
                     "resp_section_intro", "req_section_intro", "example",
                     "errors", "errors_source")


def load_json(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def dump_json(obj, p):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def src_hash_of(*parts):
    h = hashlib.sha256()
    for part in parts:
        h.update(json.dumps(part, sort_keys=True, ensure_ascii=False).encode("utf-8"))
    return "sha256:" + h.hexdigest()[:12]


def native_fragment(node):
    """剔除 x-doc 后的原生片段，用于 src_hash（源码变化检测）。"""
    if isinstance(node, dict):
        return {k: native_fragment(v) for k, v in node.items() if k != "x-doc"}
    if isinstance(node, list):
        return [native_fragment(v) for v in node]
    return node


def op_key(method, path, op):
    return op.get("operationId") or f"{method.upper()} {path}"


def _branch_has_content(b, spec):
    """分支(可能是裸 $ref)解引用后是否落到带 properties 的对象或数组。
    裸 $ref 分支(如 oneOf:[{$ref:...}])必须先 deref 再判定,否则会被漏选。
    与 make_review.py 的同名函数语义一致。"""
    bb = _deref(spec, b) if spec is not None else b
    return isinstance(bb, dict) and ("properties" in bb or bb.get("type") == "array")


def descend_object(node, spec=None):
    """穿透 array 的 items / oneOf|anyOf(单分支选取) / allOf(合并全部分支 properties) / $ref，
    落到带 properties 的对象 schema。传入 spec 时逐层解引用 #/components/schemas/*。

    allOf 语义是「同时满足全部分支」,故合并所有分支的 properties(值保留对原 spec 节点的
    引用,便于注入器挂 x-doc 后持久化);oneOf/anyOf 是「择一」,保持单分支选取。
    必须与 make_review.py 的同名函数语义一致,否则会造成完整性闸门「假绿/假缺」。"""
    seen = 0
    while isinstance(node, dict) and seen < 24:
        seen += 1
        if spec is not None and "$ref" in node:
            node = _deref(spec, node)
            continue
        if "properties" in node:
            return node
        if node.get("type") == "array" and isinstance(node.get("items"), dict):
            node = node["items"]
            continue
        if isinstance(node.get("allOf"), list):
            merged = {}
            arr_node = None
            for b in node["allOf"]:
                sub = descend_object(b, spec) if isinstance(b, dict) else None
                if isinstance(sub, dict):
                    if isinstance(sub.get("properties"), dict):
                        merged.update(sub["properties"])
                    elif sub.get("type") == "array":
                        arr_node = sub
            if merged:
                return {"properties": merged}
            if arr_node is not None:
                node = arr_node
                continue
            break
        picked = False
        for comb in ("oneOf", "anyOf"):
            branches = node.get(comb)
            if isinstance(branches, list):
                cand = next((b for b in branches
                             if isinstance(b, dict) and _branch_has_content(b, spec)), None)
                if cand is not None:
                    node = cand
                    picked = True
                    break
        if not picked:
            break
    return node


def resolve_property(schema, dotpath, spec=None):
    """按 dotpath 逐段下钻 properties（自动穿透 items / $ref），返回属性 schema 节点或 None。

    关键：dataforseo/apollo 等档的响应 schema 是「扁平点号键」——真实字段是名字本身
    含点号(或 [])的字面量 property key（如 properties["tasks.result.items.keyword"]),
    而 "tasks" 自身只是 {type:array,items:string} 占位。这类 key 无法用「split('.') 逐段
    下钻」命中。故每一层先尝试「最长字面量整键匹配」(把剩余 dotpath 整段当作一个 key)，
    命中即消费该段；否则回退到单段下钻。这样：
      · 纯嵌套 schema：单段匹配，与旧行为完全一致；
      · 扁平点号 schema：整键一次命中，与 make_review.py 逐字面量枚举的口径对齐
        （消除 inject「假缺/unresolved」与 make_review「missing」的不一致）。
    """
    node = schema
    segs = dotpath.split(".")
    i = 0
    while i < len(segs):
        node = descend_object(node, spec)
        if not isinstance(node, dict):
            return None
        props = node.get("properties")
        if not isinstance(props, dict):
            return None
        matched = False
        # 最长字面量整键优先：从最长(剩余全段)到最短(单段)依次试探
        for j in range(len(segs), i, -1):
            cand = ".".join(segs[i:j])
            if cand in props:
                node = props[cand]
                i = j
                matched = True
                break
        if not matched:
            return None
    return node


def attach(node, new_xdoc, review, path_str, stats):
    """加性写入 x-doc，遵守源保护红线。node 必须是 dict。"""
    if not isinstance(node, dict):
        return
    existing = node.get("x-doc") if isinstance(node.get("x-doc"), dict) else {}
    src = existing.get("source")
    # 源保护：人工/已复核内容不静默覆盖
    if src in PROTECTED_SOURCES:
        changed = any(existing.get(k) != new_xdoc.get(k)
                      for k in XDOC_CONTENT_KEYS if k in new_xdoc)
        if changed:
            review.append({"path": path_str, "reason": "source-protected",
                           "source": src, "action": "skipped-not-overwritten"})
            stats["protected_skipped"] += 1
            return
    merged = dict(existing)
    merged.update(new_xdoc)
    node["x-doc"] = merged


def build_field_xdoc(content_item, native_node, doc_version):
    """把一条 content 字段转成 x-doc dict（仅承载文档叠加层，不复制原生元数据）。"""
    xd = {}
    desc_en = (content_item.get("desc_en") or "").strip()
    title_zh = (content_item.get("title_zh") or "").strip()
    ann = (content_item.get("annotation") or "").strip()
    if ann:
        # 批注内联进 title_zh / desc_en 末尾，格式固定
        if title_zh:
            title_zh = title_zh + "\n[⚠️批注:" + ann + "]"
        if desc_en:
            desc_en = desc_en + "\n[⚠️Note:" + ann + "]"
    if desc_en:
        xd["desc_en"] = desc_en
    if title_zh:
        xd["title_zh"] = title_zh
    if "example" in content_item and content_item["example"] not in (None, ""):
        xd["example"] = content_item["example"]
    xd["source"] = "ai"
    xd["src_hash"] = src_hash_of(native_fragment(native_node))
    xd["doc_version"] = doc_version
    return xd


def inject(spec, content, doc_version, review, stats):
    ops = content.get("operations") or {}
    fields = content.get("fields") or {}
    paths = spec.get("paths") or {}
    for path, item in paths.items():
        if not isinstance(item, dict):
            continue
        for method in HTTP_METHODS:
            op = item.get(method)
            if not isinstance(op, dict):
                continue
            key = op_key(method, path, op)
            base = f"paths.{path}.{method}"
            # --- operation 级 ---
            oc = ops.get(key) or {}
            if oc:
                xd = {}
                for k in ("heading_zh", "desc_en", "description_zh",
                          "resp_section_intro", "req_section_intro",
                          "errors", "errors_source"):
                    if oc.get(k) not in (None, "", []):
                        xd[k] = oc[k]
                if xd:
                    xd["source"] = "ai"
                    xd["src_hash"] = src_hash_of(native_fragment(op))
                    xd["doc_version"] = doc_version
                    attach(op, xd, review, base + ".x-doc", stats)
                    stats["operations"] += 1
            fc = fields.get(key) or {}

            # --- 请求体内联/具名 schema ---
            req_schema = (((op.get("requestBody") or {}).get("content") or {})
                          .get("application/json") or {}).get("schema")
            req_schema = _deref(spec, req_schema)
            for dotpath, citem in (fc.get("request") or {}).items():
                node = resolve_property(req_schema, dotpath, spec) if isinstance(req_schema, dict) else None
                _apply_field(node, citem, doc_version, review,
                             f"{base}.requestBody..{dotpath}", stats)

            # --- 响应 schema（按状态码）---
            resp_map = fc.get("response") or {}
            for code, dmap in resp_map.items():
                resp = (op.get("responses") or {}).get(code) or (op.get("responses") or {}).get(str(code))
                sch = None
                if isinstance(resp, dict):
                    sch = ((resp.get("content") or {}).get("application/json") or {}).get("schema")
                    sch = _deref(spec, sch)
                for dotpath, citem in (dmap or {}).items():
                    node = resolve_property(sch, dotpath, spec) if isinstance(sch, dict) else None
                    _apply_field(node, citem, doc_version, review,
                                 f"{base}.responses.{code}..{dotpath}", stats)

            # --- operation.parameters ---
            params = op.get("parameters") or []
            pmap = fc.get("parameters") or {}
            if isinstance(params, list):
                for i, param in enumerate(params):
                    if not isinstance(param, dict) or param.get("$ref"):
                        continue
                    pname = param.get("name")
                    citem = pmap.get(pname)
                    if not citem:
                        continue
                    xd = build_field_xdoc(citem, param, doc_version)
                    attach(param, xd, review, f"{base}.parameters[{i}].x-doc", stats)
                    stats["fields"] += 1


def _deref(spec, schema):
    """单层 $ref 解引用到 components.schemas，便于注入具名 schema。"""
    if isinstance(schema, dict) and "$ref" in schema:
        ref = schema["$ref"]
        if ref.startswith("#/components/schemas/"):
            name = ref.split("/")[-1]
            return ((spec.get("components") or {}).get("schemas") or {}).get(name, schema)
    return schema


def _apply_field(node, citem, doc_version, review, path_str, stats):
    if not isinstance(node, dict):
        review.append({"path": path_str, "reason": "dotpath-unresolved",
                       "action": "skipped-no-such-field"})
        stats["unresolved"] += 1
        return
    xd = build_field_xdoc(citem, node, doc_version)
    attach(node, xd, review, path_str + ".x-doc", stats)
    stats["fields"] += 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="双字段 x-doc 加性注入器（standalone）")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--content", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--review-out", dest="review_out", required=True)
    ap.add_argument("--doc-version", dest="doc_version", default="2.0.0")
    args = ap.parse_args(argv)

    spec = load_json(args.spec)
    if not isinstance(spec, dict):
        sys.stderr.write("ERROR: spec is not a JSON object.\n")
        return 2
    content = load_json(args.content)
    spec = copy.deepcopy(spec)
    review = []
    stats = {"operations": 0, "fields": 0, "protected_skipped": 0, "unresolved": 0}
    inject(spec, content, args.doc_version, review, stats)
    dump_json(spec, args.out)
    dump_json({"stats": stats, "entries": review}, args.review_out)
    sys.stderr.write(
        "inject_xdoc: ops=%(operations)d fields=%(fields)d "
        "protected_skipped=%(protected_skipped)d unresolved=%(unresolved)d\n" % stats)
    return 0


if __name__ == "__main__":
    sys.exit(main())
