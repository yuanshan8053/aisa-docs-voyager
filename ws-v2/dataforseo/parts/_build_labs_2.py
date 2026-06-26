# -*- coding: utf-8 -*-
"""Assembler for labs_2.content.json.

This script does NOT invent prose. All documentation text lives in the
hand-authored dictionaries below (OPERATIONS, PARAMS, LEAF, PATH_OVERRIDE).
The script's only job is the deterministic, mechanical task of mapping each
operation's actually-enumerated dotpaths onto the matching hand-authored
entry — reuse of identical-meaning prose across recurring fields, which the
methodology explicitly allows. Anything with no genuine authored entry raises,
so we can never silently emit a meaningless template string.
"""
import json
import re
import sys

SPEC = "/home/mira/files/aisa-docs-voyager/ws-v2/dataforseo/slices/labs_2.json"
OUT = "/home/mira/files/aisa-docs-voyager/ws-v2/dataforseo/parts/labs_2.content.json"
HTTP = ("get", "post", "put", "delete", "patch", "head", "options")


# ------------------------- traversal (mirror of tools) -------------------------
def deref(spec, schema, seen=None):
    seen = seen or set()
    if isinstance(schema, dict) and "$ref" in schema:
        ref = schema["$ref"]
        if ref in seen:
            return {}
        seen.add(ref)
        if ref.startswith("#/components/schemas/"):
            name = ref.split("/")[-1]
            return deref(spec, ((spec.get("components") or {}).get("schemas") or {}).get(name, {}), seen)
    return schema


def branch_has(spec, b):
    bb = deref(spec, b, set())
    return isinstance(bb, dict) and ("properties" in bb or bb.get("type") == "array")


def descend(spec, node):
    seen = 0
    while isinstance(node, dict) and seen < 24:
        seen += 1
        if "$ref" in node:
            node = deref(spec, node, set())
            continue
        if "properties" in node:
            return node
        if node.get("type") == "array" and isinstance(node.get("items"), dict):
            node = node["items"]
            continue
        if isinstance(node.get("allOf"), list):
            merged = {}
            arr = None
            for b in node["allOf"]:
                sub = descend(spec, b) if isinstance(b, dict) else None
                if isinstance(sub, dict):
                    if isinstance(sub.get("properties"), dict):
                        merged.update(sub["properties"])
                    elif sub.get("type") == "array":
                        arr = sub
            if merged:
                return {"properties": merged}
            if arr is not None:
                node = arr
                continue
            break
        picked = False
        for comb in ("oneOf", "anyOf"):
            br = node.get(comb)
            if isinstance(br, list):
                cand = next((b for b in br if isinstance(b, dict) and branch_has(spec, b)), None)
                if cand is not None:
                    node = cand
                    picked = True
                    break
        if not picked:
            break
    return node


def walk(spec, schema, prefix, out, seen=None):
    seen = seen or set()
    schema = deref(spec, schema, set())
    if not isinstance(schema, dict):
        return
    schema = descend(spec, schema)
    schema = deref(spec, schema, set())
    if not isinstance(schema, dict):
        return
    sid = id(schema)
    if sid in seen:
        return
    seen = seen | {sid}
    props = schema.get("properties")
    if isinstance(props, dict):
        for name, pnode in props.items():
            if not isinstance(pnode, dict):
                continue
            path = f"{prefix}.{name}" if prefix else name
            out.append(path)
            dnode = deref(spec, pnode, set())
            walk(spec, dnode, path, out, seen)


# ------------------------- hand-authored content -------------------------
# Each entry is genuine documentation authored per METHODOLOGY.md.

OPERATIONS = {
"post_dataforseo_dataforseo_labs_amazon_product_competitors_live": {
 "heading_zh": "查询亚马逊商品竞品 post_dataforseo_dataforseo_labs_amazon_product_competitors_live",
 "desc_en": "Returns the products that compete with a target ASIN in Amazon SERPs, i.e. listings that rank for the same keywords as the target. Use it to map the competitive landscape of any Amazon listing; results are scoped to the supplied ASIN, location, and language.",
 "description_zh": "返回在 Amazon SERP 中与目标 ASIN 争夺相同关键词的竞品商品,用于梳理某个 Listing 的竞争格局。结果按请求中的 ASIN、地区与语言限定。"},
"post_dataforseo_dataforseo_labs_amazon_product_rank_overview_live": {
 "heading_zh": "查询亚马逊商品排名概览 post_dataforseo_dataforseo_labs_amazon_product_rank_overview_live",
 "desc_en": "Returns organic and paid Amazon SERP ranking distributions for a batch of target products, letting you compare how multiple ASINs perform side by side within one location and language.",
 "description_zh": "为一批目标商品返回其在 Amazon 自然与付费 SERP 中的排名分布,便于在同一地区、语言下横向对比多个 ASIN 的表现。"},
"post_dataforseo_dataforseo_labs_amazon_related_keywords_live": {
 "heading_zh": "查询亚马逊相关关键词 post_dataforseo_dataforseo_labs_amazon_related_keywords_live",
 "desc_en": "Returns the keywords surfaced in Amazon's “Related Searches” block for a seed keyword, expanded recursively by search depth, to help build out a keyword set around a seed term.",
 "description_zh": "返回 Amazon “Related Searches” 模块中与种子关键词相关的关键词,可按搜索深度递归扩展,用于围绕种子词扩充关键词集。"},
"post_dataforseo_dataforseo_labs_apple_app_intersection_live": {
 "heading_zh": "查询 App Store 应用关键词交集 post_dataforseo_dataforseo_labs_apple_app_intersection_live",
 "desc_en": "Returns the keywords for which several App Store apps appear together in the same SERP, revealing the keyword overlap among the apps you supply in app_ids.",
 "description_zh": "返回多个 App Store 应用在同一 SERP 中共同出现的关键词,揭示 app_ids 中所列应用之间的关键词重叠。"},
"post_dataforseo_dataforseo_labs_apple_keywords_for_app_live": {
 "heading_zh": "查询 App Store 应用关键词 post_dataforseo_dataforseo_labs_apple_keywords_for_app_live",
 "desc_en": "Returns the keywords a target App Store app ranks for, together with keyword metrics and the app's ranking position for each keyword.",
 "description_zh": "返回目标 App Store 应用所排名的关键词,并附带关键词指标及该应用在每个关键词下的排名位置。"},
"post_dataforseo_dataforseo_labs_google_app_competitors_live": {
 "heading_zh": "查询 Google Play 应用竞品 post_dataforseo_dataforseo_labs_google_app_competitors_live",
 "desc_en": "Returns the apps that compete with a target Google Play app across its ranking keywords, including competitor app IDs plus search volume and ranking data on the shared keywords.",
 "description_zh": "返回在 Google Play 上与目标应用争夺相同排名关键词的竞品应用,包含竞品应用 ID 及共有关键词的搜索量与排名数据。"},
"get_dataforseo_dataforseo_labs_google_available_history": {
 "heading_zh": "查询可用历史日期 get_dataforseo_dataforseo_labs_google_available_history",
 "desc_en": "Returns the list of dates available for the first_date and second_date fields of the Domain Metrics by Categories endpoint. Call it first to learn which historical snapshots can be requested.",
 "description_zh": "返回可用于 Domain Metrics by Categories 接口 first_date 与 second_date 字段的日期列表,通常先调用本接口确认可请求的历史快照。"},
"post_dataforseo_dataforseo_labs_google_bulk_keyword_difficulty_live": {
 "heading_zh": "批量查询关键词难度 post_dataforseo_dataforseo_labs_google_bulk_keyword_difficulty_live",
 "desc_en": "Returns the Keyword Difficulty metric for up to 1,000 keywords in a single request, scoring how hard it is to break into the top-10 organic results for each keyword.",
 "description_zh": "单次请求最多为 1000 个关键词返回 Keyword Difficulty 指标,衡量每个关键词进入前 10 自然结果的难度。"},
"post_dataforseo_dataforseo_labs_google_categories_for_domain_live": {
 "heading_zh": "查询域名所属类目 post_dataforseo_dataforseo_labs_google_categories_for_domain_live",
 "desc_en": "Returns the Google product and service categories the domain ranks for, along with aggregated ranking and traffic data for the keywords under each category.",
 "description_zh": "返回域名在搜索中有排名关键词所属的 Google 产品与服务类目,并给出各类目下关键词的汇总排名与流量数据。"},
"post_dataforseo_dataforseo_labs_google_categories_for_keywords_live": {
 "heading_zh": "查询关键词所属类目 post_dataforseo_dataforseo_labs_google_categories_for_keywords_live",
 "desc_en": "Returns the Google product and service categories associated with each supplied keyword; accepts up to 1,000 keywords per request.",
 "description_zh": "为每个传入关键词返回其关联的 Google 产品与服务类目,单次请求最多支持 1000 个关键词。"},
"post_dataforseo_dataforseo_labs_google_historical_bulk_traffic_estimation_live": {
 "heading_zh": "批量查询历史流量估算 post_dataforseo_dataforseo_labs_google_historical_bulk_traffic_estimation_live",
 "desc_en": "Returns historical monthly traffic estimates for up to 1,000 domains over a chosen time range (data available from October 2020), broken down by organic, paid, featured snippet, and local pack results.",
 "description_zh": "为最多 1000 个域名返回所选时间范围内的历史月度流量估算(数据自 2020 年 10 月起),并按自然、付费、featured snippet 与 local pack 结果拆分。"},
"post_dataforseo_dataforseo_labs_google_historical_rank_overview_live": {
 "heading_zh": "查询历史排名概览 post_dataforseo_dataforseo_labs_google_historical_rank_overview_live",
 "desc_en": "Returns a domain's historical ranking distribution across SERP positions and its estimated monthly traffic for both organic and paid results over time.",
 "description_zh": "返回域名随时间变化的历史排名分布(各 SERP 位段)及自然与付费结果的月度估算流量。"},
"post_dataforseo_dataforseo_labs_google_keyword_overview_live": {
 "heading_zh": "查询关键词概览 post_dataforseo_dataforseo_labs_google_keyword_overview_live",
 "desc_en": "Returns a comprehensive Google data profile for each supplied keyword, including cost-per-click, paid competition, search volume, search intent, monthly search history, plus SERP and backlink information; optional clickstream metrics are available via include_clickstream_data.",
 "description_zh": "为每个传入关键词返回完整的 Google 数据画像,涵盖 CPC、付费竞争度、搜索量、搜索意图、月度搜索历史以及 SERP 与外链信息;通过 include_clickstream_data 可附加点击流指标。"},
"post_dataforseo_dataforseo_labs_google_keywords_for_app_live": {
 "heading_zh": "查询 Google Play 应用关键词 post_dataforseo_dataforseo_labs_google_keywords_for_app_live",
 "desc_en": "Returns the keywords a target Google Play app ranks for, together with keyword metrics and the app's ranking position for each keyword.",
 "description_zh": "返回目标 Google Play 应用所排名的关键词,并附带关键词指标及该应用在每个关键词下的排名位置。"},
"post_dataforseo_dataforseo_labs_google_keywords_for_site_live": {
 "heading_zh": "查询域名相关关键词 post_dataforseo_dataforseo_labs_google_keywords_for_site_live",
 "desc_en": "Returns keywords relevant to a target domain, each enriched with categories, last-month search volume, cost-per-click, paid competition, and the 12-month search volume trend.",
 "description_zh": "返回与目标域名相关的关键词,每个关键词附带类目、上月搜索量、CPC、付费竞争度以及近 12 个月的搜索量趋势。"},
"post_dataforseo_dataforseo_labs_google_relevant_pages_live": {
 "heading_zh": "查询域名相关页面 post_dataforseo_dataforseo_labs_google_relevant_pages_live",
 "desc_en": "Returns ranking and traffic data for individual web pages of a target domain, letting you review each page's ranking distribution and estimated monthly traffic from organic and paid search.",
 "description_zh": "返回目标域名各个网页的排名与流量数据,便于审视每个页面的排名分布及来自自然与付费搜索的月度估算流量。"},
"post_dataforseo_dataforseo_labs_google_serp_competitors_live": {
 "heading_zh": "查询 SERP 竞争域名 post_dataforseo_dataforseo_labs_google_serp_competitors_live",
 "desc_en": "Returns the domains ranking for a set of supplied keywords, along with each domain's SERP rankings, rating, estimated traffic, and visibility derived from those keywords.",
 "description_zh": "返回为一组指定关键词排名的域名,并给出各域名基于这些关键词的 SERP 排名、评分、估算流量与可见度。"},
"post_dataforseo_dataforseo_labs_google_top_searches_live": {
 "heading_zh": "查询热门搜索关键词 post_dataforseo_dataforseo_labs_google_top_searches_live",
 "desc_en": "Returns keywords drawn from the DataForSEO Keyword Database (over 7 billion keywords), each supplied with Google Ads metrics, product categories, and Google SERP data, filtered and sorted to your criteria.",
 "description_zh": "从 DataForSEO 关键词数据库(逾 70 亿关键词)返回关键词,每个关键词附带 Google Ads 指标、产品类目及 Google SERP 数据,并按所设条件筛选与排序。"},
}

# Per-parameter (request top-level) authored docs, keyed by param name.
# Some entries are op-sensitive and handled in PARAM_BY_OP.
PARAMS = {
"asin": {"desc_en": "Target product's Amazon ASIN; competitors are computed relative to this listing. Obtain it from the Amazon Products endpoint.",
         "title_zh": "目标商品的 Amazon ASIN,竞品以此 Listing 为基准计算。可从 Amazon Products 接口获取。"},
"asins": {"desc_en": "Target products' ASINs to pull ranking data for in one batch; obtain each ASIN from the Amazon Products endpoint and supply them in uppercase.",
          "title_zh": "需批量获取排名数据的目标商品 ASIN 列表;每个 ASIN 可从 Amazon Products 接口获取,需以大写形式提供。"},
"keyword": {"desc_en": "Seed keyword to expand from; specify it in lowercase using UTF-8 encoding.",
            "title_zh": "用于扩展的种子关键词;需使用 UTF-8 编码并以小写形式指定。"},
"keywords": {"desc_en": "Target keywords to process in one request; supplied in UTF-8 and converted to lowercase before matching.",
             "title_zh": "单次请求要处理的目标关键词;以 UTF-8 提供,匹配前会被统一转为小写。"},
"app_id": {"desc_en": "Target mobile app's store ID, taken from the app's store URL; results cover the keywords this app ranks for.",
           "title_zh": "目标移动应用的商店 ID,取自应用商店页 URL;结果覆盖该应用所排名的关键词。"},
"app_ids": {"desc_en": "IDs of the target apps whose keyword overlap you want; take each ID from the app's App Store URL and supply them as an object of indexed entries.",
            "title_zh": "需求取关键词交集的目标应用 ID;每个 ID 取自 App Store 页 URL,以带序号条目的对象形式提供。"},
"target": {"desc_en": "Target domain or subdomain to analyze; specify it without the https:// scheme and without the www. prefix.",
           "title_zh": "要分析的目标域名或子域名;指定时不带 https:// 协议头,也不带 www. 前缀。"},
"targets": {"desc_en": "Target domains and subdomains to estimate traffic for in one batch; specify each without https:// and www.",
            "title_zh": "需批量估算流量的目标域名与子域名;每项指定时均不带 https:// 与 www.。"},
"location_name": {"desc_en": "Geographic target given by its full location name; supply either this or location_code. Look up valid names via the locations_and_languages endpoint.",
                  "title_zh": "以完整地区名称指定的地理目标;与 location_code 二选一提供。可通过 locations_and_languages 接口查询有效名称。"},
"location_code": {"desc_en": "Geographic target given by its numeric location code; supply either this or location_name. Look up valid codes via the locations_and_languages endpoint.",
                  "title_zh": "以数字地区代码指定的地理目标;与 location_name 二选一提供。可通过 locations_and_languages 接口查询有效代码。"},
"language_name": {"desc_en": "Target language given by its full name; supply either this or language_code. Look up valid names via the locations_and_languages endpoint.",
                  "title_zh": "以完整名称指定的目标语言;与 language_code 二选一提供。可通过 locations_and_languages 接口查询有效名称。"},
"language_code": {"desc_en": "Target language given by its short code; supply either this or language_name. Look up valid codes via the locations_and_languages endpoint.",
                  "title_zh": "以简码指定的目标语言;与 language_name 二选一提供。可通过 locations_and_languages 接口查询有效代码。"},
"limit": {"desc_en": "Caps how many records are returned in the results array.",
          "title_zh": "限定 results 数组中返回的记录条数上限。"},
"offset": {"desc_en": "Skips this many leading records in the results array, for paging through results.",
           "title_zh": "跳过 results 数组开头的指定条数记录,用于分页浏览结果。"},
"offset_token": {"desc_en": "Pagination cursor for fetching subsequent pages beyond the offset limit; pass back the offset_token value returned in the previous response. Each token is single-use for the next page.",
                 "title_zh": "用于翻取超出 offset 上限后续结果的分页游标;回传上一次响应中返回的 offset_token 值。每个 token 仅对应下一页且一次性使用。"},
"tag": {"desc_en": "Free-form label you attach to the task so you can match it to its result later; echoed back in the response data object.",
        "title_zh": "你为任务附加的自定义标签,便于事后将任务与结果对应;会在响应的 data 对象中原样回传。"},
"depth": {"desc_en": "Recursion depth for related-keyword expansion: higher levels traverse further into related searches and return progressively more keywords.",
          "title_zh": "相关关键词扩展的递归深度:层级越高,向相关搜索深入得越远,返回的关键词也越多。"},
"include_seed_keyword": {"desc_en": "When true, also returns data for the seed keyword itself in the seed_keyword_data block of the response.",
                         "title_zh": "为 true 时,响应的 seed_keyword_data 块中会一并返回种子关键词自身的数据。"},
"ignore_synonyms": {"desc_en": "When true, collapses highly similar keywords and returns only the core keyword of each cluster.",
                    "title_zh": "为 true 时,合并高度相似的关键词,每个簇仅返回核心关键词。"},
"include_subcategories": {"desc_en": "When true, results also span the subcategories of matched categories; when false, only top-level categories are considered.",
                          "title_zh": "为 true 时,结果一并覆盖命中类目的子类目;为 false 时仅考虑顶层类目。"},
"include_subdomains": {"desc_en": "When true, keywords from the domain's subdomains are included; when false, only the exact host is considered.",
                       "title_zh": "为 true 时,纳入该域名各子域的关键词;为 false 时仅考虑精确主机。"},
"include_serp_info": {"desc_en": "When true, attaches a serp_info block per keyword with SERP-level data such as result count, a check URL, and the SERP feature types present.",
                      "title_zh": "为 true 时,为每个关键词附加 serp_info 块,包含结果数量、核对 URL 及 SERP 中出现的功能类型等 SERP 级数据。"},
"include_clickstream_data": {"desc_en": "When true, enriches the response with clickstream-based metrics (such as clickstream search volume and gender/age distributions). Leaving it off keeps those fields empty.",
                             "title_zh": "为 true 时,在响应中附加基于点击流的指标(如点击流搜索量、性别/年龄分布)。不开启则相关字段为空。"},
"historical_serp_mode": {"desc_en": "Controls which SERPs are counted: live keeps only SERPs where the target currently ranks, while lost keeps SERPs where it ranked before but no longer does.",
                         "title_zh": "控制纳入统计的 SERP 范围:live 仅保留目标当前仍有排名的 SERP,lost 则保留目标曾经有过、现已失去排名的 SERP。"},
"item_types": {"desc_en": "Restricts results to the listed SERP result types; the first type listed also determines the default ordering of results.",
               "title_zh": "将结果限定为所列的 SERP 结果类型;数组中的首个类型同时决定结果的默认排序依据。"},
"date_from": {"desc_en": "Start of the historical time range, formatted yyyy-mm-dd.",
              "title_zh": "历史时间范围的起始日期,格式为 yyyy-mm-dd。"},
"date_to": {"desc_en": "End of the historical time range, formatted yyyy-mm-dd.",
            "title_zh": "历史时间范围的结束日期,格式为 yyyy-mm-dd。"},
"correlate": {"desc_en": "When enabled, aligns the returned series with previously obtained datasets to smooth over inconsistencies introduced by database changes.",
              "title_zh": "开启后,将返回的序列与此前获取的数据集对齐,以平滑因数据库变更带来的不一致。"},
"filters": {"desc_en": "Conditions that narrow the result set; combine clauses with the and / or logical operators. Reference fields by their response dotpath (e.g. metrics.organic.pos_1).",
            "title_zh": "用于收窄结果集的筛选条件;子句之间以 and / or 逻辑运算符组合。字段以其响应点路径引用(如 metrics.organic.pos_1)。",
            "annotation": "源码描述的运算符与最大条件数在各接口间不一致且部分符号被渲染截断，具体可用运算符与上限请以原生 description 为准，待研发确认。"},
"order_by": {"desc_en": "Sorting rules over the same fields usable in filters; each rule pairs a field with an asc or desc direction.",
             "title_zh": "针对 filters 中可用字段的排序规则;每条规则将一个字段与 asc 或 desc 方向配对。"},
}

# Op-specific param overrides where the seed concept differs by store/scope.
PARAM_BY_OP = {
 "post_dataforseo_dataforseo_labs_google_app_competitors_live": {
   "app_id": {"desc_en": "Target Google Play app's ID, taken from the store URL; competitors are computed relative to this app.",
              "title_zh": "目标 Google Play 应用的 ID,取自商店页 URL;竞品以该应用为基准计算。"}},
 "post_dataforseo_dataforseo_labs_google_keywords_for_app_live": {
   "app_id": {"desc_en": "Target Google Play app's ID, taken from the store URL; results cover the keywords this app ranks for.",
              "title_zh": "目标 Google Play 应用的 ID,取自商店页 URL;结果覆盖该应用所排名的关键词。"}},
}


def leaf_doc():
    """Hand-authored docs keyed by leaf name and, where meaning depends on
    context, by a dotpath suffix. Returns (matcher_list, exact_leaf_map)."""
    return None


# Exact leaf-name -> doc, used when meaning is stable regardless of parent.
LEAF = {
 # ---- response envelope (shared, self-explanatory: one-liners) ----
 "version": {"desc_en": "API version that produced this response.", "title_zh": "生成本响应的 API 版本。"},
 "status_code": {"desc_en": "Overall status code for the response; inspect it before reading results and handle non-success codes accordingly.",
                 "title_zh": "本响应的总体状态码;读取结果前应先检查,并对非成功状态码做相应处理。"},
 "status_message": {"desc_en": "Human-readable message that accompanies the overall status code.", "title_zh": "与总体状态码对应的可读说明信息。"},
 "time": {"desc_en": "Wall-clock time spent producing the response, in seconds.", "title_zh": "生成响应所耗费的时间,单位为秒。"},
 "cost": {"desc_en": "Total charge for all tasks in this response, in USD.", "title_zh": "本响应中所有任务的合计费用,单位为美元。"},
 "tasks_count": {"desc_en": "Number of task objects in the tasks array.", "title_zh": "tasks 数组中任务对象的数量。"},
 "tasks_error": {"desc_en": "Number of tasks in the tasks array that returned an error.", "title_zh": "tasks 数组中以错误返回的任务数量。"},
 "tasks": {"desc_en": "List of task objects, one per task in the request batch.", "title_zh": "任务对象列表,请求批次中每个任务对应一项。"},
 "result_count": {"desc_en": "Number of elements in this task's result array.", "title_zh": "本任务 result 数组中的元素数量。"},
 "result": {"desc_en": "Result payload for the task.", "title_zh": "任务的结果数据。"},
 "se_type": {"desc_en": "Search engine type the data was collected from.", "title_zh": "数据采集所来自的搜索引擎类型。"},
 "total_count": {"desc_en": "Total number of matching records in the database for this request, which may exceed the number returned.",
                 "title_zh": "数据库中匹配本请求的记录总数,可能多于实际返回的条数。"},
 "items_count": {"desc_en": "Number of records returned in this items array.", "title_zh": "本 items 数组中返回的记录数量。"},
 "items": {"desc_en": "Returned records carrying the core data of this endpoint.", "title_zh": "返回的记录,承载本接口的核心数据。"},
 # depth/related on amazon related keywords
 "related_keywords": {"desc_en": "Search queries related to the returned keyword.", "title_zh": "与返回关键词相关的搜索查询。"},
 "seed_keyword": {"desc_en": "Seed keyword echoed from the request.", "title_zh": "从请求回传的种子关键词。"},
 "seed_keywords": {"desc_en": "Keywords echoed from the request, with URL-encoding decoded.", "title_zh": "从请求回传的关键词,已对 URL 编码解码。"},
 "seed_keyword_data": {"desc_en": "Keyword data for the seed keyword itself, structured the same as each item's keyword_data.",
                       "title_zh": "种子关键词自身的关键词数据,结构与各 item 的 keyword_data 一致。"},
 "page_address": {"desc_en": "Absolute URL of the relevant page.", "title_zh": "相关页面的绝对 URL。"},
 "domain": {"desc_en": "Domain name of the detected competitor.", "title_zh": "检出竞争方的域名。"},
 # keyword block
 "keyword_data": {"desc_en": "Keyword metrics and SERP data for the returned keyword.", "title_zh": "返回关键词的指标与 SERP 数据。"},
 "keyword_info": {"desc_en": "Core keyword metrics block (volume, competition, bids, categories, and history).", "title_zh": "核心关键词指标块(搜索量、竞争度、出价、类目与历史)。"},
 "last_updated_time": {"desc_en": "When this data was last refreshed, in UTC (“yyyy-mm-dd hh-mm-ss +00:00”).", "title_zh": "该数据最近一次刷新的时间,UTC 格式(“yyyy-mm-dd hh-mm-ss +00:00”)。"},
 "previous_updated_time": {"desc_en": "When this data was refreshed prior to the most recent update, in UTC.", "title_zh": "该数据在最近一次更新之前的刷新时间,UTC 格式。"},
 "competition": {"desc_en": "Relative amount of paid competition for the keyword, derived from Google Ads data on a 0-to-1 scale.", "title_zh": "关键词的相对付费竞争程度,基于 Google Ads 数据,取值范围 0 至 1。"},
 "competition_level": {"desc_en": "Bucketed paid-competition level for the keyword; LOW, MEDIUM, and HIGH denote increasing competition, and an unknown level is null.", "title_zh": "关键词付费竞争的分档:LOW、MEDIUM、HIGH 依次表示竞争由低到高,未知时为 null。"},
 "cpc": {"desc_en": "Average historical cost per click for the keyword, in USD.", "title_zh": "关键词历史平均的单次点击成本,单位为美元。"},
 "search_volume": {"desc_en": "Approximate average monthly search volume for the keyword.", "title_zh": "关键词的近似月均搜索量。"},
 "low_top_of_page_bid": {"desc_en": "Lower-end top-of-page bid estimate (around the 20th percentile of winning bids), varying by the requested location.", "title_zh": "页首广告出价的低端估计(约为中标出价的 20 分位),随请求地区而变。"},
 "high_top_of_page_bid": {"desc_en": "Upper-end top-of-page bid estimate (around the 80th percentile of winning bids), varying by the requested location.", "title_zh": "页首广告出价的高端估计(约为中标出价的 80 分位),随请求地区而变。"},
 "categories": {"desc_en": "Product and service category IDs the keyword belongs to; the full category list is downloadable from DataForSEO.", "title_zh": "关键词所属的产品与服务类目 ID;完整类目清单可从 DataForSEO 下载。"},
 "monthly_searches": {"desc_en": "Per-month search volume history for roughly the trailing twelve months.", "title_zh": "约近 12 个月的逐月搜索量历史。"},
 "year": {"desc_en": "Calendar year the data point belongs to.", "title_zh": "该数据点所属的年份。"},
 "month": {"desc_en": "Calendar month the data point belongs to.", "title_zh": "该数据点所属的月份。"},
 "search_volume_trend": {"desc_en": "Percentage change in search volume versus prior periods.", "title_zh": "搜索量相对此前各周期的百分比变化。"},
 "monthly": {"desc_en": "Search volume change in percent versus the previous month.", "title_zh": "搜索量相对上月的百分比变化。"},
 "quarterly": {"desc_en": "Search volume change in percent versus the previous quarter.", "title_zh": "搜索量相对上季度的百分比变化。"},
 "yearly": {"desc_en": "Search volume change in percent versus the previous year.", "title_zh": "搜索量相对去年的百分比变化。"},
 "is_normalized": {"desc_en": "Whether the volume figures in this block have been normalized against the reference dataset.", "title_zh": "本块中的搜索量数值是否已对照参考数据集做归一化。"},
 # keyword_properties
 "keyword_properties": {"desc_en": "Additional descriptive properties of the keyword (clustering, difficulty, language).", "title_zh": "关键词的附加描述性属性(聚类、难度、语言)。"},
 "core_keyword": {"desc_en": "Representative keyword of the synonym cluster this keyword belongs to; null when no synonym cluster was identified.", "title_zh": "该关键词所属同义簇的代表关键词;未识别出同义簇时为 null。"},
 "synonym_clustering_algorithm": {"desc_en": "Which clustering method grouped this keyword: keyword_metrics uses keyword_info signals, text_processing uses text analysis; null when no cluster was found.", "title_zh": "对该关键词聚类所用的方法:keyword_metrics 基于 keyword_info 指标,text_processing 基于文本分析;未成簇时为 null。"},
 "keyword_difficulty": {"desc_en": "How hard it is to rank in the top-10 organic results for the keyword, on a 0-to-100 logarithmic scale derived from the link profiles of the current top-10 pages.", "title_zh": "关键词进入前 10 自然结果的难度,采用 0 至 100 的对数刻度,依据当前前 10 页面的外链情况计算。"},
 "detected_language": {"desc_en": "Language of the keyword as identified by DataForSEO's detector.", "title_zh": "DataForSEO 检测器识别出的关键词语言。"},
 "is_another_language": {"desc_en": "True when the detected keyword language differs from the language set in the request.", "title_zh": "当检测到的关键词语言与请求所设语言不一致时为 true。"},
 "words_count": {"desc_en": "Number of words the keyword phrase consists of.", "title_zh": "关键词短语包含的词数。"},
 # serp_info
 "serp_info": {"desc_en": "SERP-level data for the keyword; null unless include_serp_info was set and SERP data exists for the keyword.", "title_zh": "关键词的 SERP 级数据;除非设置了 include_serp_info 且数据库存有该关键词的 SERP 数据,否则为 null。"},
 "check_url": {"desc_en": "Direct URL to the live search results, usable to verify the returned data.", "title_zh": "指向实时搜索结果的直达 URL,可用于核对返回数据。"},
 "serp_item_types": {"desc_en": "The kinds of SERP features (items) found in the results for this keyword.", "title_zh": "该关键词结果中出现的 SERP 功能(item)类型。"},
 "se_results_count": {"desc_en": "Number of search results the engine reports for the keyword.", "title_zh": "搜索引擎为该关键词报告的搜索结果数量。"},
 # avg_backlinks_info
 "avg_backlinks_info": {"desc_en": "Average backlink profile across the top-10 organically ranking pages for the keyword.", "title_zh": "关键词前 10 自然排名页面的平均外链画像。"},
 "backlinks": {"desc_en": "Average number of backlinks among the top-ranking pages.", "title_zh": "排名靠前页面的平均外链数量。"},
 "dofollow": {"desc_en": "Average number of dofollow backlinks among the top-ranking pages.", "title_zh": "排名靠前页面的平均 dofollow 外链数量。"},
 "referring_pages": {"desc_en": "Average number of referring pages among the top-ranking pages.", "title_zh": "排名靠前页面的平均引荐页面数量。"},
 "referring_domains": {"desc_en": "Average number of referring domains among the top-ranking pages.", "title_zh": "排名靠前页面的平均引荐域名数量。"},
 "referring_main_domains": {"desc_en": "Average number of referring main (root) domains among the top-ranking pages.", "title_zh": "排名靠前页面的平均引荐主域名数量。"},
 "rank": {"desc_en": "Average page-level rank score among the top-ranking pages.", "title_zh": "排名靠前页面的平均页面级 rank 分值。"},
 "main_domain_rank": {"desc_en": "Average domain-level rank score among the top-ranking pages.", "title_zh": "排名靠前页面的平均域名级 rank 分值。"},
 # search_intent_info
 "search_intent_info": {"desc_en": "Detected search intent for the keyword.", "title_zh": "关键词的检出搜索意图。"},
 "main_intent": {"desc_en": "Primary search intent of the keyword (informational, navigational, commercial, or transactional).", "title_zh": "关键词的主要搜索意图(informational、navigational、commercial 或 transactional)。"},
 "foreign_intent": {"desc_en": "Secondary search intents the keyword also exhibits, beyond the main one.", "title_zh": "关键词除主意图外还表现出的次要搜索意图。"},
 # clickstream block
 "clickstream_keyword_info": {"desc_en": "Clickstream-derived keyword metrics; populated only when include_clickstream_data is true.", "title_zh": "基于点击流的关键词指标;仅当 include_clickstream_data 为 true 时填充。"},
 "gender_distribution": {"desc_en": "Breakdown of the clickstream audience by gender.", "title_zh": "点击流受众的性别构成。"},
 "age_distribution": {"desc_en": "Breakdown of the clickstream audience by age band.", "title_zh": "点击流受众的年龄段构成。"},
 # age-band buckets (object keys named after the age range)
 "18-24": {"desc_en": "Share of the clickstream audience in the 18-24 age band.", "title_zh": "点击流受众中 18-24 岁年龄段的占比。"},
 "25-34": {"desc_en": "Share of the clickstream audience in the 25-34 age band.", "title_zh": "点击流受众中 25-34 岁年龄段的占比。"},
 "35-44": {"desc_en": "Share of the clickstream audience in the 35-44 age band.", "title_zh": "点击流受众中 35-44 岁年龄段的占比。"},
 "45-54": {"desc_en": "Share of the clickstream audience in the 45-54 age band.", "title_zh": "点击流受众中 45-54 岁年龄段的占比。"},
 "55-64": {"desc_en": "Share of the clickstream audience in the 55-64 age band.", "title_zh": "点击流受众中 55-64 岁年龄段的占比。"},
 "female": {"desc_en": "Count of female users in the clickstream dataset.", "title_zh": "点击流数据集中女性用户的数量。"},
 "male": {"desc_en": "Count of male users in the clickstream dataset.", "title_zh": "点击流数据集中男性用户的数量。"},
 "clickstream_etv": {"desc_en": "Estimated traffic volume computed from clickstream search volumes; requires include_clickstream_data to be true.", "title_zh": "基于点击流搜索量计算的估算流量;需 include_clickstream_data 为 true。"},
 "clickstream_gender_distribution": {"desc_en": "Clickstream traffic split by gender; requires include_clickstream_data to be true.", "title_zh": "点击流流量的性别拆分;需 include_clickstream_data 为 true。"},
 "clickstream_age_distribution": {"desc_en": "Clickstream traffic split by age band; requires include_clickstream_data to be true.", "title_zh": "点击流流量的年龄段拆分;需 include_clickstream_data 为 true。"},
 "keyword_info_normalized_with_bing": {"desc_en": "Keyword search volume normalized against Bing search volume.", "title_zh": "对照 Bing 搜索量归一化后的关键词搜索量。"},
 "keyword_info_normalized_with_clickstream": {"desc_en": "Keyword search volume normalized against clickstream data.", "title_zh": "对照点击流数据归一化后的关键词搜索量。"},
 "search_partners": {"desc_en": "True when figures include Google search partner sites in addition to Google itself.", "title_zh": "为 true 时,数值除 Google 自身外还纳入 Google 搜索合作网站。"},
 # metrics container & SERP-type blocks
 "metrics": {"desc_en": "Ranking and traffic metrics for the target, grouped by SERP result type.", "title_zh": "目标的排名与流量指标,按 SERP 结果类型分组。"},
 "competitor_metrics": {"desc_en": "Ranking metrics over the keywords this competitor shares with the target.", "title_zh": "该竞争方与目标共有关键词上的排名指标。"},
 "full_metrics": {"desc_en": "Ranking metrics over all keywords this entity ranks for, not just the shared ones.", "title_zh": "该主体所有排名关键词(而非仅共有关键词)上的排名指标。"},
 "organic": {"desc_en": "Ranking and traffic data from organic search results.", "title_zh": "来自自然搜索结果的排名与流量数据。"},
 "paid": {"desc_en": "Ranking and traffic data from paid search results.", "title_zh": "来自付费搜索结果的排名与流量数据。"},
 "featured_snippet": {"desc_en": "Ranking and traffic data from featured snippet results.", "title_zh": "来自 featured snippet 结果的排名与流量数据。"},
 "local_pack": {"desc_en": "Ranking and traffic data from local pack results.", "title_zh": "来自 local pack 结果的排名与流量数据。"},
 "amazon_serp": {"desc_en": "Ranking data from Amazon organic SERPs.", "title_zh": "来自 Amazon 自然 SERP 的排名数据。"},
 "amazon_paid": {"desc_en": "Ranking data from Amazon paid SERPs.", "title_zh": "来自 Amazon 付费 SERP 的排名数据。"},
 "google_play_search_organic": {"desc_en": "Ranking data from Google Play organic search.", "title_zh": "来自 Google Play 自然搜索的排名数据。"},
 # position buckets — count of SERPs where the entity ranks in a band
 "pos_1": {"desc_en": "Count of SERPs where the entity ranks #1.", "title_zh": "实体排名第 1 的 SERP 数量。"},
 "pos_2_3": {"desc_en": "Count of SERPs where the entity ranks in positions 2-3.", "title_zh": "实体排名第 2 至 3 位的 SERP 数量。"},
 "pos_4_10": {"desc_en": "Count of SERPs where the entity ranks in positions 4-10.", "title_zh": "实体排名第 4 至 10 位的 SERP 数量。"},
 "pos_11_100": {"desc_en": "Count of SERPs where the entity ranks in positions 11-100.", "title_zh": "实体排名第 11 至 100 位的 SERP 数量。"},
 "pos_11_20": {"desc_en": "Count of SERPs where the entity ranks in positions 11-20.", "title_zh": "实体排名第 11 至 20 位的 SERP 数量。"},
 "pos_21_30": {"desc_en": "Count of SERPs where the entity ranks in positions 21-30.", "title_zh": "实体排名第 21 至 30 位的 SERP 数量。"},
 "pos_31_40": {"desc_en": "Count of SERPs where the entity ranks in positions 31-40.", "title_zh": "实体排名第 31 至 40 位的 SERP 数量。"},
 "pos_41_50": {"desc_en": "Count of SERPs where the entity ranks in positions 41-50.", "title_zh": "实体排名第 41 至 50 位的 SERP 数量。"},
 "pos_51_60": {"desc_en": "Count of SERPs where the entity ranks in positions 51-60.", "title_zh": "实体排名第 51 至 60 位的 SERP 数量。"},
 "pos_61_70": {"desc_en": "Count of SERPs where the entity ranks in positions 61-70.", "title_zh": "实体排名第 61 至 70 位的 SERP 数量。"},
 "pos_71_80": {"desc_en": "Count of SERPs where the entity ranks in positions 71-80.", "title_zh": "实体排名第 71 至 80 位的 SERP 数量。"},
 "pos_81_90": {"desc_en": "Count of SERPs where the entity ranks in positions 81-90.", "title_zh": "实体排名第 81 至 90 位的 SERP 数量。"},
 "pos_91_100": {"desc_en": "Count of SERPs where the entity ranks in positions 91-100.", "title_zh": "实体排名第 91 至 100 位的 SERP 数量。"},
 "count": {"desc_en": "Total count of SERPs of this type that contain the entity.", "title_zh": "包含该实体的此类 SERP 总数。"},
 "etv": {"desc_en": "Estimated monthly traffic volume, computed as the sum of search volume times click-through rate over the entity's ranking keywords.", "title_zh": "估算月度流量,按该实体排名关键词的搜索量与点击率乘积求和得出。"},
 "estimated_paid_traffic_cost": {"desc_en": "Estimated monthly USD cost of acquiring the equivalent traffic through paid ads, derived from etv and CPC values.", "title_zh": "通过付费广告获取等量流量的估算月度成本(美元),由 etv 与 CPC 数值推算。"},
 "is_new": {"desc_en": "How many ranked elements for the target are newly found in this check.", "title_zh": "本次检查中目标新发现的排名元素数量。"},
 "is_up": {"desc_en": "How many of the target's ranked elements moved up since the previous check.", "title_zh": "相比上次检查,目标排名上升的元素数量。"},
 "is_down": {"desc_en": "How many of the target's ranked elements moved down since the previous check.", "title_zh": "相比上次检查,目标排名下降的元素数量。"},
 "is_lost": {"desc_en": "How many of the target's previously ranked elements were not found in this check.", "title_zh": "目标此前有排名、本次检查未再找到的元素数量。"},
 # serp competitors item metrics
 "avg_position": {"desc_en": "Average SERP position of the entity across the matched keywords.", "title_zh": "实体在匹配关键词上的平均 SERP 排名位置。"},
 "median_position": {"desc_en": "Median SERP position of the entity across the matched keywords.", "title_zh": "实体在匹配关键词上的中位 SERP 排名位置。"},
 "sum_position": {"desc_en": "Sum of the entity's positions across the intersected keywords.", "title_zh": "实体在交集关键词上各排名位置之和。"},
 "intersections": {"desc_en": "Number of keywords the entity shares with the target.", "title_zh": "实体与目标共有的关键词数量。"},
 "rating": {"desc_en": "Relative SERP visibility rating for the domain over the specified keywords, accumulated from how high it ranks.", "title_zh": "域名在指定关键词上的相对 SERP 可见度评分,按其排名高低累加得出。"},
 "keywords_count": {"desc_en": "Number of the specified keywords the domain holds SERP positions for.", "title_zh": "域名在所指定关键词中拥有 SERP 排名的关键词数量。"},
 "visibility": {"desc_en": "SERP visibility rate of the domain over the specified keywords, weighting higher positions more heavily.", "title_zh": "域名在指定关键词上的 SERP 可见度,对靠前位置赋予更高权重。"},
 "relevant_serp_items": {"desc_en": "Number of SERP elements relevant to the domain across the specified keywords.", "title_zh": "在指定关键词上与该域名相关的 SERP 元素数量。"},
 "keywords_positions": {"desc_en": "SERP positions the domain holds for each of the specified keywords.", "title_zh": "该域名在每个指定关键词上所占的 SERP 排名位置。"},
 # paging offset (response)
 "offset": {"desc_en": "Offset applied to this result page.", "title_zh": "本结果页所应用的偏移量。"},
 "offset_token": {"desc_en": "Single-use cursor to fetch the next page of results; pass it back as the request's offset_token.", "title_zh": "用于获取下一页结果的一次性游标;作为请求的 offset_token 回传。"},
 # task/data/path leaves
 "id": {"desc_en": "Unique task identifier in UUID format.", "title_zh": "任务在系统中的唯一标识,采用 UUID 格式。"},
 "path": {"desc_en": "URL path segments of the endpoint that produced the task.", "title_zh": "生成该任务的接口 URL 路径分段。"},
 "data": {"desc_en": "Echo of the parameters supplied in the request.", "title_zh": "对请求中所传参数的回传。"},
 "target": {"desc_en": "Target domain echoed from the request.", "title_zh": "从请求回传的目标域名。"},
 "asin": {"desc_en": "Product ASIN; in results, the ASIN this record describes.", "title_zh": "商品 ASIN;在结果中为该记录所描述的 ASIN。"},
 "app_id": {"desc_en": "App store ID; in results, the app this record describes.", "title_zh": "应用商店 ID;在结果中为该记录所描述的应用。"},
 "app_ids": {"desc_en": "App IDs echoed from the request.", "title_zh": "从请求回传的应用 ID。"},
 "keyword": {"desc_en": "The keyword this record describes.", "title_zh": "该记录所描述的关键词。"},
 "date": {"desc_en": "An available date that can be passed to the Domain Metrics by Categories endpoint.", "title_zh": "可传入 Domain Metrics by Categories 接口的一个可用日期。"},
 "depth": {"desc_en": "Expansion depth at which this keyword was discovered.", "title_zh": "发现该关键词时所处的扩展深度。"},
 # app SERP element / serp_item leaves
 "ranked_serp_element": {"desc_en": "The app's SERP element found for the returned keyword.", "title_zh": "返回关键词对应的该应用 SERP 元素。"},
 "intersection_result": {"desc_en": "Per-app SERP data for the returned keyword, with one array per supplied app ID.", "title_zh": "返回关键词的逐应用 SERP 数据,每个传入应用 ID 对应一个数组。"},
 "1": {"desc_en": "SERP elements for one of the supplied app IDs; the key name varies from 1 to the number of app IDs you provided in app_ids.", "title_zh": "对应某一个传入应用 ID 的 SERP 元素;键名从 1 起,按 app_ids 中提供的应用 ID 数量递增。"},
 "serp_item": {"desc_en": "SERP element details for the app.", "title_zh": "该应用的 SERP 元素详情。"},
 "type": {"desc_en": "Type of the SERP element.", "title_zh": "SERP 元素的类型。"},
 "rank_group": {"desc_en": "Rank within the group of elements sharing the same type; other types are skipped in this count.", "title_zh": "在同类型元素组内的排名;其他类型不计入该计数。"},
 "rank_absolute": {"desc_en": "Absolute rank of the element among all elements in the SERP.", "title_zh": "该元素在整个 SERP 全部元素中的绝对排名。"},
 "position": {"desc_en": "Horizontal alignment of the element within the SERP (left or right).", "title_zh": "元素在 SERP 中的水平对齐方位(left 或 right)。"},
 "title": {"desc_en": "Title of the app.", "title_zh": "应用的标题。"},
 "url": {"desc_en": "URL of the app's store page.", "title_zh": "应用商店页的 URL。"},
 "icon": {"desc_en": "URL of the app icon.", "title_zh": "应用图标的 URL。"},
 "reviews_count": {"desc_en": "Total number of reviews the app has.", "title_zh": "应用的评价总数。"},
 "rating_type": {"desc_en": "Rating scale used; Max5 denotes a 0-5 scale.", "title_zh": "所用评分量表;Max5 表示 0 至 5 分制。"},
 "value": {"desc_en": "The rating value.", "title_zh": "评分数值。"},
 "votes_count": {"desc_en": "Number of ratings contributing to the value.", "title_zh": "参与构成该评分的评价数量。"},
 "rating_max": {"desc_en": "Maximum possible value for the rating scale.", "title_zh": "该评分量表的最大可能值。"},
 "is_free": {"desc_en": "Whether the app is free; the nested fields carry its pricing details when it is not.", "title_zh": "应用是否免费;非免费时其内嵌字段承载定价详情。"},
 "current": {"desc_en": "Current price shown in the listing.", "title_zh": "Listing 中显示的当前价格。"},
 "regular": {"desc_en": "Regular (non-promotional) price shown in the listing.", "title_zh": "Listing 中显示的常规(非促销)价格。"},
 "max_value": {"desc_en": "Maximum price shown in the listing.", "title_zh": "Listing 中显示的最高价格。"},
 "currency": {"desc_en": "ISO currency code applied to the listed price.", "title_zh": "Listing 价格所用的 ISO 货币代码。"},
 "is_price_range": {"desc_en": "Whether the price is given as a range rather than a single value.", "title_zh": "价格是否以区间而非单一数值给出。"},
 "displayed_price": {"desc_en": "Raw price string exactly as shown in the listing.", "title_zh": "Listing 中原样展示的价格字符串。"},
 "developer": {"desc_en": "Name of the app's developer.", "title_zh": "应用开发者的名称。"},
 "developer_url": {"desc_en": "URL of the developer's store page.", "title_zh": "开发者商店页的 URL。"},
 # location/language echoes in results
 "location_code": {"desc_en": "Location code echoed from the request; null when no data applies.", "title_zh": "从请求回传的地区代码;无对应数据时为 null。"},
 "language_code": {"desc_en": "Language code echoed from the request; null when no data applies.", "title_zh": "从请求回传的语言代码;无对应数据时为 null。"},
}

# Context-sensitive overrides matched by exact dotpath SUFFIX (longest wins).
# Needed because a bare leaf name (e.g. `rating`) means different things in
# different blocks: an integer SERP-visibility score under serp_competitors
# items vs. an app's average-rating OBJECT under app SERP elements.
PATH_OVERRIDE = {
 "ranked_serp_element.serp_item.rating": {"desc_en": "Average rating of the app.", "title_zh": "应用的平均评分。"},
 "intersection_result.1.rating": {"desc_en": "Average rating of the app.", "title_zh": "应用的平均评分。"},
}


def author_for_leaf(path):
    leaf = path.split(".")[-1]
    # longest matching dotpath suffix wins
    best = None
    for suffix, doc in PATH_OVERRIDE.items():
        if path == suffix or path.endswith("." + suffix):
            if best is None or len(suffix) > len(best[0]):
                best = (suffix, doc)
    if best is not None:
        return best[1]
    if leaf in LEAF:
        return LEAF[leaf]
    return None


def main():
    spec = json.load(open(SPEC, encoding="utf-8"))
    content = {"operations": {}, "fields": {}}
    missing = set()
    paths = spec["paths"]
    for p, item in paths.items():
        for m in HTTP:
            op = item.get(m)
            if not isinstance(op, dict):
                continue
            opid = op.get("operationId") or f"{m.upper()} {p}"
            if opid not in OPERATIONS:
                continue
            content["operations"][opid] = dict(OPERATIONS[opid])
            fc = {"request": {}, "response": {}, "parameters": {}}
            # request body fields
            req = (((op.get("requestBody") or {}).get("content") or {}).get("application/json") or {}).get("schema")
            if isinstance(req, dict):
                out = []
                walk(spec, req, "", out)
                for dp in out:
                    leaf = dp.split(".")[-1]
                    doc = None
                    if "." not in dp:  # top-level request param
                        doc = (PARAM_BY_OP.get(opid, {}).get(leaf)) or PARAMS.get(leaf)
                    if doc is None:
                        doc = author_for_leaf(dp)
                    if doc is None:
                        missing.add("REQ " + opid + " :: " + dp)
                        continue
                    fc["request"][dp] = doc
            # response fields per code
            for code, resp in (op.get("responses") or {}).items():
                if not isinstance(resp, dict):
                    continue
                sch = ((resp.get("content") or {}).get("application/json") or {}).get("schema")
                if not isinstance(sch, dict):
                    continue
                out = []
                walk(spec, sch, "", out)
                cmap = {}
                for dp in out:
                    doc = author_for_leaf(dp)
                    if doc is None:
                        missing.add("RESP " + opid + " " + code + " :: " + dp)
                        continue
                    cmap[dp] = doc
                if cmap:
                    fc["response"][code] = cmap
            # operation.parameters (none expected for these POSTs, but handle)
            for param in (op.get("parameters") or []):
                if not isinstance(param, dict) or param.get("$ref"):
                    continue
                pname = param.get("name")
                doc = (PARAM_BY_OP.get(opid, {}).get(pname)) or PARAMS.get(pname)
                if doc is None:
                    missing.add("PARAM " + opid + " :: " + str(pname))
                    continue
                fc["parameters"][pname] = doc
            content["fields"][opid] = fc

    if missing:
        sys.stderr.write("MISSING AUTHORED DOCS (%d):\n" % len(missing))
        for x in sorted(missing):
            sys.stderr.write("  " + x + "\n")
        sys.exit(3)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
        f.write("\n")
    sys.stderr.write("WROTE %s ops=%d\n" % (OUT, len(content["operations"])))


if __name__ == "__main__":
    main()
