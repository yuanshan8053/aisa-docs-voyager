#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inline_inject.py — Doc Engine 的「内联 schema 回写扩展」(additive-only)。

背景与必要性
------------
api-doc-agent 的确定性内核 doc_engine.process() 仅遍历两类节点注入 x-doc:
  (a) spec.paths.<p>.<m>            —— operation 级
  (b) spec.components.schemas.<n>   —— 具名组件 schema 的属性树
而 AIsa 的 spec(openai-chat / youte-search 等)把请求/响应体写成
**内联 schema**(requestBody.content.<mt>.schema 直接展开 properties),
并用 **operation.parameters** 承载查询参数 —— 这两类节点 process() 不触及,
但 Gate 2(docEngineChecks.js)与 Renderer 都要求/消费它们的 x-doc.title_zh。

本扩展不改引擎、不改原生结构、不做 hoist(内联→$ref 会篡改原生骨架,
违反「只增不改」红线并使 check_native_preserved.py 失败)。它只是:
  1. 先调用 doc_engine.process() 完成 (a)(b) 的 operation 级注入;
  2. 再**复用引擎自身的** doc_engine._process_schema() 在内联 schema 根上跑一遍,
     把 x-doc 注入到内联 properties / items —— 完全沿用 assemble_property_xdoc +
     merge_node(R1–R10 源保护)+ src_hash + source=ai 的同一套确定性逻辑;
  3. 对 operation.parameters 逐个复用 assemble_property_xdoc + merge_node 注入。

content.json 约定(在标准 operations/schemas 之外新增一个 inline 子树):
  content["inline"][<operationId>]["request"]  → 镜像请求体 schema 的 scontent
  content["inline"][<operationId>]["response"][<code>] → 镜像响应 schema 的 scontent
  content["inline"][<operationId>]["parameters"][<name>] → 该 query/path 参数的 pcontent
镜像 scontent 形态与引擎对组件 schema 的约定完全一致:
  {"properties": {<name>: {"title_zh":..., "properties"/"items": {...}}}}

用法:
  python3 inline_inject.py --spec spec.yaml --comments c.json \
      --invoke-meta m.json --content content.json \
      --out enhanced.yaml --review-out review.json [--doc-version 1.1.0]
"""

import argparse
import sys
import os

# 复用引擎本体(同目录),严禁复制其逻辑。
SKILL_ENGINE = "/data/plugins/custom/skills/api-doc-agent/doc-engine"
sys.path.insert(0, SKILL_ENGINE)
import doc_engine as de  # noqa: E402


def _inline_content(content, opid):
    return ((content.get("inline") or {}).get(opid)) or {}


def inject_inline(spec, content, review, doc_version, new_keys):
    """对每个 operation 的内联请求/响应 schema 与 parameters 复用引擎注入。"""
    paths = spec.get("paths") or {}
    for p, item in paths.items():
        if not isinstance(item, dict):
            continue
        for m in de.HTTP_METHODS:
            op = item.get(m)
            if not isinstance(op, dict):
                continue
            opid = op.get("operationId") or f"{m} {p}"
            ic = _inline_content(content, opid)

            # --- (1) 内联请求体 schema ---
            req_schema = (((op.get("requestBody") or {}).get("content") or {})
                          .get("application/json") or {}).get("schema")
            if isinstance(req_schema, dict):
                de._process_schema(
                    req_schema,
                    ("inline", opid, "request"),
                    f"paths.{p}.{m}.requestBody.content.application/json.schema",
                    (ic.get("request") or {}),
                    {},
                    None, review, doc_version, new_keys)

            # --- (2) 内联响应 schema(逐状态码)---
            resp_content = ic.get("response") or {}
            for code, resp in (op.get("responses") or {}).items():
                if not isinstance(resp, dict):
                    continue
                sch = ((resp.get("content") or {}).get("application/json") or {}).get("schema")
                if isinstance(sch, dict):
                    de._process_schema(
                        sch,
                        ("inline", opid, "response", str(code)),
                        f"paths.{p}.{m}.responses.{code}.content.application/json.schema",
                        (resp_content.get(str(code)) or {}),
                        {},
                        None, review, doc_version, new_keys)

            # --- (3) operation.parameters(复用 property 装配 + 合并)---
            params = op.get("parameters")
            if isinstance(params, list):
                pmap = ic.get("parameters") or {}
                for i, param in enumerate(params):
                    if not isinstance(param, dict) or param.get("$ref"):
                        continue
                    # 网关信封 Action/Version 由 Gate 2 豁免,且 Renderer 不消费,跳过。
                    if param.get("in") == "query" and param.get("name") in ("Action", "Version"):
                        continue
                    pname = param.get("name") or str(i)
                    pcontent = pmap.get(pname) or {}
                    new_xdoc = de.assemble_property_xdoc(param, pcontent, None, doc_version)
                    # 参数的 src_hash 取 name + 原生片段(剔除 x-doc),与属性同源逻辑。
                    new_xdoc["src_hash"] = de.src_hash_of(
                        "param", pname, de.native_fragment(param))
                    new_xdoc.setdefault("source", "ai")
                    de.strip_system_fields(new_xdoc)
                    final, _ = de.merge_node(
                        None, new_xdoc, de.PROP_CONTENT_FIELD,
                        source_field_exists=True, review=review,
                        path_str=f"paths.{p}.{m}.parameters[{i}].x-doc")
                    if final is not None:
                        de._attach_xdoc(param, de.ordered_xdoc(final, de.PROP_XDOC_ORDER))
                    # 参数自身若带内联 schema 的 properties/items,继续复用引擎递归。
                    pschema = param.get("schema")
                    if isinstance(pschema, dict):
                        de._process_schema(
                            pschema,
                            ("inline", opid, "param", pname, "schema"),
                            f"paths.{p}.{m}.parameters[{i}].schema",
                            pcontent if isinstance(pcontent, dict) else {},
                            {},
                            None, review, doc_version, new_keys)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Doc Engine inline-schema injection extension.")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--comments")
    ap.add_argument("--invoke-meta", dest="invoke_meta")
    ap.add_argument("--content")
    ap.add_argument("--existing")
    ap.add_argument("--out", required=True)
    ap.add_argument("--review-out", dest="review_out", required=True)
    ap.add_argument("--doc-version", dest="doc_version", default=de.DEFAULT_DOC_VERSION)
    args = ap.parse_args(argv)

    spec = de.load_yaml(args.spec)
    if not isinstance(spec, dict):
        sys.stderr.write("ERROR: spec is not a valid OpenAPI mapping.\n")
        return 2

    comments = de.load_json(args.comments) if args.comments else {}
    invoke_meta = de.load_json(args.invoke_meta) if args.invoke_meta else {}
    content = de.load_json(args.content) if args.content else {}

    existing_index = None
    if args.existing:
        existing_index = de.index_existing(de.load_yaml(args.existing))

    review = []
    new_keys = set()
    # 阶段一:复用引擎本体注入 operation 级 + 组件 schema。
    de.process(spec, comments, invoke_meta, content, existing_index, review,
               args.doc_version)
    # 阶段二:复用引擎逐节点函数,把 x-doc 补到内联 schema + parameters。
    inject_inline(spec, content, review, args.doc_version, new_keys)

    de.dump_yaml(spec, args.out)
    de.dump_json(review, args.review_out)
    sys.stderr.write(
        f"Inline inject: wrote {args.out} (+{len(review)} review entries).\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
