# -*- coding: utf-8 -*-
"""Assembler for labs_1.content.json (dataforseo_labs group, first half: 19 ops).

Like _build_labs_2.py, this script invents no prose. All documentation text
lives in the hand-authored dictionaries below, or is reused from the sibling
labs_2 assembler's dictionaries for fields that carry identical meaning across
the two slices (the methodology explicitly allows reusing identical-meaning
prose for recurring fields). The script's only job is the deterministic,
mechanical mapping of each operation's actually-enumerated dotpaths onto a
matching authored entry. Anything with no genuine authored entry raises, so we
can never silently emit a meaningless template string.
"""
import json
import sys

# Reuse the verified traversal + the shared vocabulary from the labs_2 build.
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "_build_labs_2",
    "/home/mira/files/aisa-docs-voyager/ws-v2/dataforseo/parts/_build_labs_2.py")
_l2 = importlib.util.module_from_spec(_spec)
# Prevent labs_2 main() from running on import.
_orig_name = _l2.__name__
sys.modules["_build_labs_2"] = _l2
_spec.loader.exec_module(_l2)  # defines functions + dicts; main() guarded by __main__

deref, descend, walk = _l2.deref, _l2.descend, _l2.walk

SPEC = "/home/mira/files/aisa-docs-voyager/ws-v2/dataforseo/slices/labs_1.json"
OUT = "/home/mira/files/aisa-docs-voyager/ws-v2/dataforseo/parts/labs_1.content.json"
HTTP = ("get", "post", "put", "delete", "patch", "head", "options")


# ------------------------- hand-authored content (labs_1) -------------------------

OPERATIONS = {
"post_dataforseo_dataforseo_labs_amazon_bulk_search_volume_live": {
 "heading_zh": "批量查询亚马逊搜索量 post_dataforseo_dataforseo_labs_amazon_bulk_search_volume_live",
 "desc_en": "Returns Amazon search volume for a batch of keywords in a single request, so you can size demand across many keywords at once for the given location and language.",
 "description_zh": "单次请求为一批关键词返回 Amazon 搜索量,便于在指定地区与语言下一次性衡量多个关键词的需求规模。"},
"post_dataforseo_dataforseo_labs_amazon_product_keyword_intersections_live": {
 "heading_zh": "查询亚马逊商品关键词交集 post_dataforseo_dataforseo_labs_amazon_product_keyword_intersections_live",
 "desc_en": "Returns the keywords for which the supplied Amazon products appear together in the same SERP, along with each product's SERP element per keyword, revealing where multiple ASINs compete or co-rank.",
 "description_zh": "返回所传 Amazon 商品在同一 SERP 中共同出现的关键词,并给出每个关键词下各商品的 SERP 元素,揭示多个 ASIN 在何处竞争或同台排名。"},
"post_dataforseo_dataforseo_labs_amazon_ranked_keywords_live": {
 "heading_zh": "查询亚马逊商品排名关键词 post_dataforseo_dataforseo_labs_amazon_ranked_keywords_live",
 "desc_en": "Returns the keywords a target ASIN ranks for in Amazon SERPs, each with keyword metrics and the product's ranking SERP element, for the given location and language.",
 "description_zh": "返回目标 ASIN 在 Amazon SERP 中有排名的关键词,每个关键词附带关键词指标及该商品的排名 SERP 元素,按指定地区与语言限定。"},
"post_dataforseo_dataforseo_labs_apple_app_competitors_live": {
 "heading_zh": "查询 App Store 应用竞品 post_dataforseo_dataforseo_labs_apple_app_competitors_live",
 "desc_en": "Returns the apps that compete with a target App Store app across its ranking keywords, including each competitor's app ID and ranking metrics over the shared keywords.",
 "description_zh": "返回在 App Store 上与目标应用争夺相同排名关键词的竞品应用,包含各竞品的应用 ID 及在共有关键词上的排名指标。"},
"post_dataforseo_dataforseo_labs_apple_bulk_app_metrics_live": {
 "heading_zh": "批量查询 App Store 应用指标 post_dataforseo_dataforseo_labs_apple_bulk_app_metrics_live",
 "desc_en": "Returns App Store SERP ranking metrics for a batch of target apps in one request, letting you compare how multiple apps perform across their ranking keywords within one location and language.",
 "description_zh": "单次请求为一批目标应用返回 App Store SERP 排名指标,便于在同一地区、语言下横向对比多个应用在其排名关键词上的表现。"},
"get_dataforseo_dataforseo_labs_available_filters": {
 "heading_zh": "查询可用筛选字段 get_dataforseo_dataforseo_labs_available_filters",
 "desc_en": "Returns the full list of fields usable in the filters and order_by parameters, grouped by the endpoint they apply to. Call it to discover which fields each DataForSEO Labs endpoint supports for filtering and sorting.",
 "description_zh": "返回可用于 filters 与 order_by 参数的全部字段清单,并按其适用的接口分组。可借此查明各 DataForSEO Labs 接口支持哪些字段进行筛选与排序。"},
"post_dataforseo_dataforseo_labs_google_app_intersection_live": {
 "heading_zh": "查询 Google Play 应用关键词交集 post_dataforseo_dataforseo_labs_google_app_intersection_live",
 "desc_en": "Returns the keywords for which several Google Play apps appear together in the same SERP, revealing the keyword overlap among the apps you supply in app_ids.",
 "description_zh": "返回多个 Google Play 应用在同一 SERP 中共同出现的关键词,揭示 app_ids 中所列应用之间的关键词重叠。"},
"post_dataforseo_dataforseo_labs_google_bulk_app_metrics_live": {
 "heading_zh": "批量查询 Google Play 应用指标 post_dataforseo_dataforseo_labs_google_bulk_app_metrics_live",
 "desc_en": "Returns Google Play SERP ranking metrics for a batch of target apps in one request, letting you compare how multiple apps perform across their ranking keywords within one location and language.",
 "description_zh": "单次请求为一批目标应用返回 Google Play SERP 排名指标,便于在同一地区、语言下横向对比多个应用在其排名关键词上的表现。"},
"post_dataforseo_dataforseo_labs_google_bulk_traffic_estimation_live": {
 "heading_zh": "批量查询流量估算 post_dataforseo_dataforseo_labs_google_bulk_traffic_estimation_live",
 "desc_en": "Returns estimated monthly Google search traffic for a batch of target domains, broken down by SERP result type, so you can compare traffic across many domains in one request.",
 "description_zh": "为一批目标域名返回 Google 搜索的估算月度流量,并按 SERP 结果类型拆分,便于单次请求横向比较多个域名的流量。"},
"get_dataforseo_dataforseo_labs_google_categories_for_keywords_languages": {
 "heading_zh": "查询关键词类目可用语言 get_dataforseo_dataforseo_labs_google_categories_for_keywords_languages",
 "desc_en": "Returns the languages supported by the Categories for Keywords endpoint, listing each language's name and code so you can pick a valid language for that endpoint.",
 "description_zh": "返回 Categories for Keywords 接口所支持的语言,列出每种语言的名称与代码,便于为该接口选择有效语言。"},
"post_dataforseo_dataforseo_labs_google_domain_rank_overview_live": {
 "heading_zh": "查询域名排名概览 post_dataforseo_dataforseo_labs_google_domain_rank_overview_live",
 "desc_en": "Returns a domain's ranking distribution across SERP positions plus its estimated monthly organic and paid traffic, summarizing the domain's overall Google search presence.",
 "description_zh": "返回域名在各 SERP 位段的排名分布及其自然与付费的估算月度流量,概括该域名在 Google 搜索中的整体表现。"},
"post_dataforseo_dataforseo_labs_google_historical_keyword_data_live": {
 "heading_zh": "查询关键词历史数据 post_dataforseo_dataforseo_labs_google_historical_keyword_data_live",
 "desc_en": "Returns the historical Google Ads metrics for each supplied keyword, including search volume, CPC, and competition over past months, so you can study how a keyword's demand has changed over time.",
 "description_zh": "为每个传入关键词返回其历史 Google Ads 指标,包含过往各月的搜索量、CPC 与竞争度,便于研究关键词需求随时间的变化。"},
"post_dataforseo_dataforseo_labs_google_keyword_ideas_live": {
 "heading_zh": "查询关键词创意 post_dataforseo_dataforseo_labs_google_keyword_ideas_live",
 "desc_en": "Returns keyword ideas relevant to the seed keywords by drawing on the categories the seeds belong to, each enriched with Google Ads metrics, SERP data, and search history, to expand a topic into a broader keyword set.",
 "description_zh": "依据种子关键词所属类目返回相关的关键词创意,每个关键词附带 Google Ads 指标、SERP 数据与搜索历史,用于把某个主题扩展为更广的关键词集。"},
"post_dataforseo_dataforseo_labs_google_keyword_suggestions_live": {
 "heading_zh": "查询关键词联想 post_dataforseo_dataforseo_labs_google_keyword_suggestions_live",
 "desc_en": "Returns long-tail keyword suggestions that contain the seed keyword, each enriched with Google Ads metrics, SERP data, and search history, to find longer phrases built around the seed term.",
 "description_zh": "返回包含种子关键词的长尾关键词联想,每个关键词附带 Google Ads 指标、SERP 数据与搜索历史,用于发现围绕种子词构成的更长短语。"},
"post_dataforseo_dataforseo_labs_google_keywords_for_categories_live": {
 "heading_zh": "查询类目关键词 post_dataforseo_dataforseo_labs_google_keywords_for_categories_live",
 "desc_en": "Returns relevant keywords that belong to the supplied product and service categories, each enriched with Google Ads metrics, SERP data, and search history, to build a keyword set scoped to chosen categories.",
 "description_zh": "返回归属于所传产品与服务类目的相关关键词,每个关键词附带 Google Ads 指标、SERP 数据与搜索历史,用于构建限定于所选类目的关键词集。"},
"post_dataforseo_dataforseo_labs_google_related_keywords_live": {
 "heading_zh": "查询相关关键词 post_dataforseo_dataforseo_labs_google_related_keywords_live",
 "desc_en": "Returns the keywords surfaced in Google's “searches related to” block for a seed keyword, expanded recursively by search depth, each enriched with keyword metrics, to grow a keyword set around a seed term.",
 "description_zh": "返回 Google “相关搜索”模块中与种子关键词相关的关键词,可按搜索深度递归扩展,每个关键词附带关键词指标,用于围绕种子词扩充关键词集。"},
"post_dataforseo_dataforseo_labs_google_search_intent_live": {
 "heading_zh": "查询搜索意图 post_dataforseo_dataforseo_labs_google_search_intent_live",
 "desc_en": "Returns the predicted search intent of each supplied keyword, giving the primary intent label with its probability plus any secondary intents, so you can classify keywords by user intent.",
 "description_zh": "为每个传入关键词返回其预测的搜索意图,给出主意图标签及其概率以及若干次意图,便于按用户意图对关键词分类。"},
"post_dataforseo_dataforseo_labs_google_subdomains_live": {
 "heading_zh": "查询域名子域排名 post_dataforseo_dataforseo_labs_google_subdomains_live",
 "desc_en": "Returns the subdomains of a target domain together with each subdomain's ranking distribution and estimated organic and paid traffic, letting you see which subdomains drive the domain's search presence.",
 "description_zh": "返回目标域名的各个子域,并给出每个子域的排名分布及自然与付费的估算流量,便于查看哪些子域支撑了该域名的搜索表现。"},
"get_dataforseo_dataforseo_labs_status": {
 "heading_zh": "查询数据更新状态 get_dataforseo_dataforseo_labs_status",
 "desc_en": "Returns the last data-update date for the DataForSEO Labs Google, Bing, and Amazon endpoints, so you can tell how fresh each engine's database is before querying.",
 "description_zh": "返回 DataForSEO Labs 中 Google、Bing 与 Amazon 各组接口的最近数据更新日期,便于在查询前了解各引擎数据库的新鲜度。"},
}

# labs_1-specific request params (beyond those already authored in labs_2.PARAMS).
PARAMS_EXTRA = {
"intersection_mode": {"desc_en": "How the supplied ASINs are matched against keywords: intersect keeps only keywords where every ASIN co-ranks, while union keeps keywords where any of them ranks.",
                      "title_zh": "所传 ASIN 与关键词的匹配方式:intersect 仅保留全部 ASIN 同台排名的关键词,union 则保留其中任一 ASIN 有排名的关键词。"},
"category_codes": {"desc_en": "Product and service category codes to draw keywords from; the full category list is downloadable from DataForSEO.",
                  "title_zh": "用于取关键词的产品与服务类目代码;完整类目清单可从 DataForSEO 下载。",
                  "annotation": "源码注明单次请求的类目数量上限,但该上限请以原生 description 为准,待研发确认。"},
"category_intersection": {"desc_en": "When true, returns only keywords featured in all specified categories; when false, returns keywords featured in any of them.",
                         "title_zh": "为 true 时,仅返回归属于全部所指定类目的关键词;为 false 时,返回归属于其中任一类目的关键词。"},
"closely_variants": {"desc_en": "Selects the match algorithm: true uses phrase-match, false uses broad-match, which widens the returned keyword set.",
                    "title_zh": "选择匹配算法:true 采用 phrase-match(短语匹配),false 采用 broad-match(广泛匹配),后者会扩大返回的关键词集。"},
"exact_match": {"desc_en": "When true, returned keywords must contain the exact seed phrase (other words may appear before or after it).",
               "title_zh": "为 true 时,返回的关键词须包含完整的种子短语(短语前后可有其他词)。"},
"replace_with_core_keyword": {"desc_en": "When true, serp_info and related_keywords are returned for the core keyword of the cluster the seed belongs to; when false, for the seed keyword itself.",
                             "title_zh": "为 true 时,serp_info 与 related_keywords 针对种子词所属簇的核心关键词返回;为 false 时,针对种子词自身返回。"},
}

# labs_1-specific response leaves (beyond those already authored in labs_2.LEAF).
LEAF_EXTRA = {
 # request echoes in results
 "asins": {"desc_en": "Product ASINs echoed from the request.", "title_zh": "从请求回传的商品 ASIN。"},
 # status endpoint: per-engine update info blocks
 "google": {"desc_en": "Data-update information for the DataForSEO Labs Google endpoints.", "title_zh": "DataForSEO Labs Google 接口的数据更新信息。"},
 "bing": {"desc_en": "Data-update information for the DataForSEO Labs Bing endpoints.", "title_zh": "DataForSEO Labs Bing 接口的数据更新信息。"},
 "amazon": {"desc_en": "Data-update information for the DataForSEO Labs Amazon endpoints.", "title_zh": "DataForSEO Labs Amazon 接口的数据更新信息。"},
 "date_update": {"desc_en": "Date this engine's DataForSEO Labs database was last updated (yyyy-mm-dd).", "title_zh": "该引擎 DataForSEO Labs 数据库的最近更新日期(yyyy-mm-dd)。"},
 # categories_for_keywords_languages
 "language_name": {"desc_en": "Full name of a supported language.", "title_zh": "受支持语言的完整名称。"},
 # keyword ideas / categories endpoints
 "seed_categories": {"desc_en": "Category codes echoed from the request that the returned keyword ideas were derived from.", "title_zh": "从请求回传的类目代码,所返回的关键词创意即由其推导而来。"},
 # subdomains endpoint
 "subdomain": {"desc_en": "Subdomain of the target whose ranking metrics this record describes.", "title_zh": "目标域名的子域,本记录描述该子域的排名指标。"},
 # search intent endpoint
 "keyword_intent": {"desc_en": "Primary search intent predicted for the keyword.", "title_zh": "关键词所预测的主要搜索意图。"},
 "secondary_keyword_intents": {"desc_en": "Additional search intents the keyword exhibits beyond the primary one.", "title_zh": "关键词除主意图外还表现出的其他搜索意图。"},
 "label": {"desc_en": "The predicted intent label (informational, navigational, commercial, or transactional).", "title_zh": "预测的意图标签(informational、navigational、commercial 或 transactional)。"},
 "probability": {"desc_en": "Model confidence that this intent label applies to the keyword, from 0 to 1.", "title_zh": "模型对该意图标签适用于此关键词的置信度,取值 0 至 1。"},
 # historical keyword data: per-period history entry
 "history": {"desc_en": "Historical keyword metrics broken out per period, each entry holding that period's keyword_info snapshot.", "title_zh": "按周期拆分的历史关键词指标,每条记录承载该周期的 keyword_info 快照。"},
 # app store competitor metrics block
 "app_store_search_organic": {"desc_en": "Ranking data from App Store organic search.", "title_zh": "来自 App Store 自然搜索的排名数据。"},
 # amazon product intersection: the $asin_number-keyed product objects
 "$asin_number": {"desc_en": "The Amazon SERP element for one of the supplied ASINs; the key name is that product's ASIN.", "title_zh": "对应某一个传入 ASIN 的 Amazon SERP 元素;键名即该商品的 ASIN。"},
 "description": {"desc_en": "Product description text from the Amazon listing.", "title_zh": "Amazon Listing 的商品描述文本。"},
 "image_url": {"desc_en": "URL of the product's image in the listing.", "title_zh": "Listing 中商品图片的 URL。"},
 "image_alt": {"desc_en": "Alt text of the product image.", "title_zh": "商品图片的替代文本(alt)。"},
 "is_best_seller": {"desc_en": "Whether the listing carries Amazon's “Best Seller” badge.", "title_zh": "该 Listing 是否带有 Amazon “Best Seller” 标识。"},
 "is_amazon_choice": {"desc_en": "Whether the listing carries Amazon's “Amazon's Choice” badge.", "title_zh": "该 Listing 是否带有 Amazon “Amazon's Choice” 标识。"},
 "price_from": {"desc_en": "Lower bound of the product's price range shown in the listing.", "title_zh": "Listing 中商品价格区间的下限。"},
 "price_to": {"desc_en": "Upper bound of the product's price range shown in the listing.", "title_zh": "Listing 中商品价格区间的上限。"},
 "special_offers": {"desc_en": "Special offers or promotions listed for the product.", "title_zh": "该商品列出的特价或促销信息。"},
 "delivery_info": {"desc_en": "Delivery details for the product, including the delivery message and price.", "title_zh": "商品的配送信息,包含配送说明与配送价格。"},
 "delivery_message": {"desc_en": "Delivery message shown in the listing (e.g. estimated arrival).", "title_zh": "Listing 中显示的配送说明(如预计送达)。"},
 "delivery_price": {"desc_en": "Delivery price details for the product.", "title_zh": "商品的配送价格详情。"},
 "xpath": {"desc_en": "XPath pointing to the product element within the SERP page markup.", "title_zh": "指向该商品元素在 SERP 页面标记中位置的 XPath。"},
}

# Context-sensitive overrides matched by exact dotpath SUFFIX (longest wins),
# layered on top of labs_2.PATH_OVERRIDE.
PATH_OVERRIDE_EXTRA = {
 # available_filters: result is the grouped list of filterable fields, not the usual result payload.
 "tasks.result": {"desc_en": "List of all fields available for the filters and order_by parameters, grouped by the endpoint they apply to.", "title_zh": "可用于 filters 与 order_by 参数的全部字段列表,按其适用的接口分组。"},
 # amazon product intersection product object leaves (under $asin_number)
 "intersection_result.$asin_number.title": {"desc_en": "Title of the product.", "title_zh": "商品的标题。"},
 "intersection_result.$asin_number.url": {"desc_en": "URL of the product's Amazon page.", "title_zh": "商品 Amazon 页面的 URL。"},
 "intersection_result.$asin_number.rating": {"desc_en": "Average customer rating of the product.", "title_zh": "商品的平均用户评分。"},
 "intersection_result.$asin_number.domain": {"desc_en": "Amazon domain the product was found on.", "title_zh": "检出该商品所在的 Amazon 域名。"},
 "intersection_result.$asin_number.position": {"desc_en": "Horizontal alignment of the product element within the SERP (left or right).", "title_zh": "商品元素在 SERP 中的水平对齐方位(left 或 right)。"},
 "intersection_result.$asin_number.type": {"desc_en": "Type of the SERP element.", "title_zh": "SERP 元素的类型。"},
}


def author_param(opid, leaf):
    """Top-level request param doc: op-specific override, then labs_2 PARAMS,
    then labs_1 extras."""
    ov = _l2.PARAM_BY_OP.get(opid, {})
    if leaf in ov:
        return ov[leaf]
    if leaf in _l2.PARAMS:
        return _l2.PARAMS[leaf]
    if leaf in PARAMS_EXTRA:
        return PARAMS_EXTRA[leaf]
    return None


def author_for_leaf(path):
    leaf = path.split(".")[-1]
    # longest matching dotpath suffix wins, across both override tables
    best = None
    for table in (PATH_OVERRIDE_EXTRA, _l2.PATH_OVERRIDE):
        for suffix, doc in table.items():
            if path == suffix or path.endswith("." + suffix):
                if best is None or len(suffix) > len(best[0]):
                    best = (suffix, doc)
    if best is not None:
        return best[1]
    if leaf in _l2.LEAF:
        return _l2.LEAF[leaf]
    if leaf in LEAF_EXTRA:
        return LEAF_EXTRA[leaf]
    return None


def main():
    spec = json.load(open(SPEC, encoding="utf-8"))
    content = {"operations": {}, "fields": {}}
    missing = set()
    for p, item in spec["paths"].items():
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
                        doc = author_param(opid, leaf)
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
            # operation.parameters (the GET ops carry none, but handle generically)
            for param in (op.get("parameters") or []):
                if not isinstance(param, dict) or param.get("$ref"):
                    continue
                pname = param.get("name")
                doc = author_param(opid, pname)
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
