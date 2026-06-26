# -*- coding: utf-8 -*-
"""Assemble parts/domain_content.content.json from hand-authored dual-field text.

DataForSEO response schemas are flat dotted-literal-key maps (e.g. the literal
property key "tasks.result.items.url"), so docs are authored per literal key.
Each unique field/param/op is authored once and mapped onto every op that exposes
that literal key; identical native fields legitimately share identical docs
(deduplicated authoring, not template spraying). Any spec key without an authored
entry raises KeyError so coverage is guaranteed by construction.
"""
import json

spec = json.load(open("slices/domain_content.json"))


def deref(s, sch, seen=None):
    seen = seen or set()
    if isinstance(sch, dict) and "$ref" in sch:
        r = sch["$ref"]
        if r in seen:
            return {}
        seen.add(r)
        if r.startswith("#/components/schemas/"):
            n = r.split("/")[-1]
            return deref(s, s["components"]["schemas"].get(n, {}), seen)
    return sch


def resp200_keys(op):
    resp = op.get("responses", {}).get("200")
    if not resp:
        return []
    sch = resp.get("content", {}).get("application/json", {}).get("schema")
    if not sch:
        return []
    d = deref(spec, sch)
    return list((d.get("properties") or {}).keys())


def req_keys(op):
    rb = op.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema")
    if not rb:
        return []
    d = deref(spec, rb)
    return list((d.get("properties") or {}).keys())


# ---------------------------------------------------------------------------
# Shared response envelope (identical native semantics across all 22 ops).
# ---------------------------------------------------------------------------
ENVELOPE = {
    "version": {
        "desc_en": "API version that produced this response; useful when reporting issues or pinning behavior across releases.",
        "title_zh": "生成该响应的 API 版本；便于上报问题或在版本迭代中锁定行为。",
    },
    "status_code": {
        "desc_en": "Top-level status code for the whole call. `20000` means the call succeeded; any other value signals a request-level failure that occurred before per-task processing.",
        "title_zh": "整次调用的总状态码。`20000` 表示调用成功；其他值代表在进入单任务处理前就发生的请求级失败。",
    },
    "status_message": {
        "desc_en": "Human-readable message paired with `status_code`; read it to learn the cause when `status_code` is not a success value.",
        "title_zh": "与 `status_code` 配套的可读说明；当 `status_code` 非成功值时据此定位原因。",
    },
    "time": {
        "desc_en": "Server-side execution time for the whole call, in seconds.",
        "title_zh": "整次调用的服务端执行耗时，单位为秒。",
    },
    "cost": {
        "desc_en": "Total amount charged for this call across all tasks, in USD; free listing endpoints (languages/locations/filters/categories/technologies) return 0.",
        "title_zh": "本次调用所有任务合计扣费，单位为美元；languages/locations/filters/categories/technologies 等免费列表接口返回 0。",
    },
    "tasks_count": {
        "desc_en": "Number of entries in the `tasks` array.",
        "title_zh": "`tasks` 数组中的条目数量。",
    },
    "tasks_error": {
        "desc_en": "How many entries in `tasks` finished with an error; if non-zero, inspect each task's own `tasks.status_code`.",
        "title_zh": "`tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `tasks.status_code`。",
    },
    "tasks": {
        "desc_en": "Array holding the individual task results of this call; the Live endpoints submit one task per call, so expect a single entry.",
        "title_zh": "承载本次调用各任务结果的数组；Live 接口每次仅提交一个任务，通常只含一个条目。",
    },
    "tasks.id": {
        "desc_en": "UUID identifying this task within DataForSEO's system; use it to correlate the result with your request.",
        "title_zh": "该任务在 DataForSEO 系统中的 UUID 标识；可用于将结果与请求对应。",
    },
    "tasks.status_code": {
        "desc_en": "Per-task status code (range 10000-60000). `20000` means the task completed successfully; other values indicate this specific task failed.",
        "title_zh": "单任务状态码（范围 10000-60000）。`20000` 表示该任务成功完成；其他值表示此任务失败。",
    },
    "tasks.status_message": {
        "desc_en": "Human-readable message for this task's status; consult it when the task code is not a success value.",
        "title_zh": "该任务状态的可读说明；当任务状态码非成功值时据此排查。",
    },
    "tasks.time": {
        "desc_en": "Execution time of this individual task, in seconds.",
        "title_zh": "该单任务的执行耗时，单位为秒。",
    },
    "tasks.cost": {
        "desc_en": "Amount charged for this individual task, in USD.",
        "title_zh": "该单任务的扣费金额，单位为美元。",
    },
    "tasks.result_count": {
        "desc_en": "Number of elements in this task's `tasks.result` array.",
        "title_zh": "该任务 `tasks.result` 数组中的元素数量。",
    },
    "tasks.path": {
        "desc_en": "API path segments that were called, echoing how the request was routed.",
        "title_zh": "本次调用的 API 路径分段，回显请求的路由方式。",
    },
    "tasks.result": {
        "desc_en": "Array carrying this task's result records; the fields below describe one record.",
        "title_zh": "承载该任务结果记录的数组；下列字段描述其中单条记录。",
    },
}

# tasks.data has two native variants: POST echoes request body; GET echoes URL params.
TASKS_DATA_POST = {
    "desc_en": "Echo of the parameters you submitted in the POST request body, useful for correlating the response with its input.",
    "title_zh": "回显你在 POST 请求体中提交的参数，便于将响应与其输入对应。",
}
TASKS_DATA_GET = {
    "desc_en": "Echo of the parameters passed in the GET request URL, useful for correlating the response with its input.",
    "title_zh": "回显 GET 请求 URL 中传入的参数，便于将响应与其输入对应。",
}

# tasks.result for the filter-listing endpoints (string-array result of available filters).
RESULT_FILTERS = {
    "desc_en": "List of parameters available for data filtration, grouped by the endpoint each filter can be used with; reference it when building the `filters` request field.",
    "title_zh": "可用于数据过滤的参数清单，按可使用该过滤器的接口分组；构建请求字段 `filters` 时参考此清单。",
}

# ---------------------------------------------------------------------------
# Per-op-family result-record field dictionaries (literal flat-dotted keys).
# ---------------------------------------------------------------------------

# Shared sentiment/category breakdown leaves reused across content-analysis ops.
TOP_DOMAINS = {
    "desc_en": "Top domains citing the target, each with its citation count, so you can see which sites dominate the citation set.",
    "title_zh": "引用目标最多的域名及各自的引用次数，可据此了解哪些站点在引用集中占主导。",
}
SENTIMENT_CONNOTATIONS = {
    "desc_en": "Breakdown of emotional reactions (e.g. anger, happiness, love, sadness, share, fun) tied to the citations, with the citation count per sentiment.",
    "title_zh": "与引用相关的情绪反应分布（如 anger、happiness、love、sadness、share、fun），并给出每种情绪的引用次数。",
}
CONNOTATION_TYPES = {
    "desc_en": "Breakdown of sentiment polarity (positive, negative, neutral) tied to the citations, with the citation count per type.",
    "title_zh": "与引用相关的情感极性分布（positive、negative、neutral），并给出每种类型的引用次数。",
}
TEXT_CATEGORIES = {
    "desc_en": "Text categories detected in the citations with the citation count in each; resolve category codes via the Categories endpoint.",
    "title_zh": "在引用中识别出的文本分类及各分类的引用次数；分类代码可通过 Categories 接口解析。",
}
PAGE_CATEGORIES = {
    "desc_en": "Page categories of the citing pages with the citation count in each; resolve category codes via the Categories endpoint.",
    "title_zh": "引用页面的页面分类及各分类的引用次数；分类代码可通过 Categories 接口解析。",
}
PAGE_TYPES = {
    "desc_en": "Distribution of citations across page types (e.g. ecommerce, news, blogs, message-boards, organization), with the count per type.",
    "title_zh": "引用按页面类型的分布（如 ecommerce、news、blogs、message-boards、organization），并给出每类的计数。",
}
COUNTRIES = {
    "desc_en": "Distribution of citations by country with the citation count per country; resolve country codes via the Locations endpoint.",
    "title_zh": "引用按国家的分布及每个国家的引用次数；国家代码可通过 Locations 接口解析。",
}
LANGUAGES = {
    "desc_en": "Distribution of citations by language with the citation count per language; resolve language codes via the Languages endpoint.",
    "title_zh": "引用按语言的分布及每种语言的引用次数；语言代码可通过 Languages 接口解析。",
}
RANK_METRIC = {
    "desc_en": "Normalized sum of the ranks of all URLs citing the target; a higher value reflects stronger overall authority of the citing pages.",
    "title_zh": "引用目标的所有 URL 排名的归一化求和；值越高表示引用页面整体权威性越强。",
}
TOTAL_COUNT = {
    "desc_en": "Total number of records in the database matching your request, which may exceed the number actually returned.",
    "title_zh": "数据库中匹配你请求的记录总数，可能多于实际返回的条数。",
}
ITEMS_COUNT = {
    "desc_en": "Number of records returned in the `items` array of this response.",
    "title_zh": "本响应 `items` 数组中返回的记录数量。",
}

# ---- Technologies group structures (technologies listing endpoint) ----
TECH_LIST = {
    "tasks.result.groups": {
        "desc_en": "Array of top-level technology groups, each grouping related categories and technologies.",
        "title_zh": "顶层技术分组数组，每个分组聚合相关的类别与技术。",
    },
    "tasks.result.groups.id": {
        "desc_en": "Identifier of the technology group; pass it as the `group` (or `groups`) request field on the technology query endpoints. Example: marketing, sales.",
        "title_zh": "技术分组的标识；可作为请求字段 `group`（或 `groups`）传入技术查询接口。示例：marketing、sales。",
    },
    "tasks.result.groups.title": {
        "desc_en": "Human-readable display name of the technology group.",
        "title_zh": "技术分组的可读显示名称。",
    },
    "tasks.result.groups.categories": {
        "desc_en": "Technology categories that belong to this group.",
        "title_zh": "归属于该分组的技术类别。",
    },
    "tasks.result.groups.categories.id": {
        "desc_en": "Identifier of the technology category; pass it as the `category` (or `categories`) request field. Example: crm, cart_abandonment.",
        "title_zh": "技术类别的标识；可作为请求字段 `category`（或 `categories`）传入。示例：crm、cart_abandonment。",
    },
    "tasks.result.groups.categories.path": {
        "desc_en": "Dotted path locating the category within the group hierarchy. Example: user_generated_content.content_curation.",
        "title_zh": "在分组层级中定位该类别的点号路径。示例：user_generated_content.content_curation。",
    },
    "tasks.result.groups.categories.title": {
        "desc_en": "Human-readable display name of the technology category.",
        "title_zh": "技术类别的可读显示名称。",
    },
    "tasks.result.groups.categories.technologies": {
        "desc_en": "Names of the individual technologies in this category; pass a name as the `technology` (or `technologies`) request field. Example: \"Salesforce\", \"CareCart\".",
        "title_zh": "该类别下各项技术的名称；可将名称作为请求字段 `technology`（或 `technologies`）传入。示例：\"Salesforce\"、\"CareCart\"。",
    },
}

# ---- aggregation_technologies result fields ----
AGG = {
    "tasks.result.total_count": TOTAL_COUNT,
    "tasks.result.items_count": {
        "desc_en": "Number of technology records returned in this result.",
        "title_zh": "本结果中返回的技术记录数量。",
    },
    "tasks.result.": {
        "desc_en": "Element type marker for each returned record; its fixed value `aggregation_technologies_item` lets you branch parsing by record type.",
        "title_zh": "每条返回记录的元素类型标记；固定值 `aggregation_technologies_item`，便于按记录类型分支解析。",
    },
    "tasks.result.group": {
        "desc_en": "Technology group id this record belongs to, matching the `group` you queried.",
        "title_zh": "该记录所属的技术分组 id，与你查询的 `group` 对应。",
    },
    "tasks.result.category": {
        "desc_en": "Technology category id this record belongs to, matching the `category` you queried.",
        "title_zh": "该记录所属的技术类别 id，与你查询的 `category` 对应。",
    },
    "tasks.result.technology": {
        "desc_en": "Name of the technology this record describes.",
        "title_zh": "该记录所描述的技术名称。",
    },
    "tasks.result.groups_count": {
        "desc_en": "Number of domains that match your parameters and use a technology from the indicated group.",
        "title_zh": "符合你所设参数、且使用所示分组中某项技术的域名数量。",
    },
    "tasks.result.categories_count": {
        "desc_en": "Number of domains that match your parameters and use a technology from the indicated category.",
        "title_zh": "符合你所设参数、且使用所示类别中某项技术的域名数量。",
    },
    "tasks.result.technologies_count": {
        "desc_en": "Number of domains that match your parameters and use the indicated technology.",
        "title_zh": "符合你所设参数、且使用所示该项技术的域名数量。",
    },
}

# ---- domain profile fields (domain_technologies + domains_by_* share these) ----
DOMAIN_PROFILE = {
    "tasks.result.type": {
        "desc_en": "Element type marker for the record; fixed value `domain_technology_item`.",
        "title_zh": "记录的元素类型标记；固定值 `domain_technology_item`。",
    },
    "tasks.result.domain": {
        "desc_en": "Domain name of the analyzed website.",
        "title_zh": "被分析网站的域名。",
    },
    "tasks.result.title": {
        "desc_en": "Meta title of the domain's homepage.",
        "title_zh": "域名首页的 meta 标题。",
    },
    "tasks.result.description": {
        "desc_en": "Meta description of the domain's homepage.",
        "title_zh": "域名首页的 meta 描述。",
    },
    "tasks.result.meta_keywords": {
        "desc_en": "Meta keywords declared on the domain's homepage.",
        "title_zh": "域名首页声明的 meta 关键词。",
    },
    "tasks.result.domain_rank": {
        "desc_en": "Backlink-based rank of the domain from DataForSEO's Backlink Index; a higher value reflects a stronger backlink profile.",
        "title_zh": "基于 DataForSEO 反链索引的域名反链排名；值越高表示反链档案越强。",
    },
    "tasks.result.last_visited": {
        "desc_en": "Most recent time the DataForSEO crawler visited the domain, in UTC `yyyy-mm-dd hh-mm-ss +00:00` format. Example: 2022-10-10 12:57:46 +00:00.",
        "title_zh": "DataForSEO 爬虫最近一次访问该域名的时间，采用 UTC `yyyy-mm-dd hh-mm-ss +00:00` 格式。示例：2022-10-10 12:57:46 +00:00。",
    },
    "tasks.result.country_iso_code": {
        "desc_en": "ISO country code of the country the domain is determined to belong to.",
        "title_zh": "判定该域名所属国家的 ISO 国家代码。",
    },
    "tasks.result.language_code": {
        "desc_en": "Code of the language the domain is determined to be associated with.",
        "title_zh": "判定该域名所关联的语言代码。",
    },
    "tasks.result.content_language_code": {
        "desc_en": "Code of the language the content on the domain is written in.",
        "title_zh": "该域名内容所使用语言的代码。",
    },
    "tasks.result.phone_numbers": {
        "desc_en": "Contact phone numbers detected on the target website.",
        "title_zh": "在目标网站上检测到的联系电话。",
    },
    "tasks.result.emails": {
        "desc_en": "Contact email addresses detected on the target website.",
        "title_zh": "在目标网站上检测到的联系邮箱。",
    },
    "tasks.result.social_graph_urls": {
        "desc_en": "Social media URLs and handles detected in the target website's social graph markup.",
        "title_zh": "在目标网站社交图谱标记中检测到的社交媒体 URL 与账号。",
    },
    "tasks.result.technologies": {
        "desc_en": "Technologies detected on the website, keyed by technology name and organized by group and category; cross-reference the technologies endpoint for the full structure.",
        "title_zh": "在网站上检测到的技术，以技术名称为键并按分组与类别组织；完整结构可对照 technologies 接口。",
    },
}

# ---- domains_by_* paging wrapper (around DOMAIN_PROFILE items) ----
DOMAINS_BY = {
    "tasks.result.total_count": {
        "desc_en": "Total number of relevant domains in the database matching your request, which may exceed the number returned.",
        "title_zh": "数据库中匹配你请求的相关域名总数，可能多于实际返回的条数。",
    },
    "tasks.result.items_count": {
        "desc_en": "Number of domain records returned in the `items` array.",
        "title_zh": "`items` 数组中返回的域名记录数量。",
    },
    "tasks.result.offset": {
        "desc_en": "The `offset` value applied to this result, echoing the request.",
        "title_zh": "本结果实际应用的 `offset` 值，回显请求。",
    },
    "tasks.result.offset_token": {
        "desc_en": "Token to fetch the next page; pass it as the request `offset_token` to continue paging past the timeout-prone deep-offset limit and retrieve over 100,000 results across requests.",
        "title_zh": "用于翻下一页的令牌；作为请求 `offset_token` 传入，可越过易超时的深分页上限、跨多次请求获取超过 100,000 条结果。",
    },
    "tasks.result.items": {
        "desc_en": "Array of matched domain records; each entry follows the domain profile shape described below.",
        "title_zh": "匹配的域名记录数组；每个条目遵循下文描述的域名档案结构。",
    },
}
# items.* keys reuse the DOMAIN_PROFILE text under the items. prefix
DOMAINS_BY_ITEMS = {
    "tasks.result.items.type": DOMAIN_PROFILE["tasks.result.type"],
    "tasks.result.items.domain": DOMAIN_PROFILE["tasks.result.domain"],
    "tasks.result.items.title": DOMAIN_PROFILE["tasks.result.title"],
    "tasks.result.items.description": DOMAIN_PROFILE["tasks.result.description"],
    "tasks.result.items.meta_keywords": DOMAIN_PROFILE["tasks.result.meta_keywords"],
    "tasks.result.items.domain_rank": DOMAIN_PROFILE["tasks.result.domain_rank"],
    "tasks.result.items.last_visited": DOMAIN_PROFILE["tasks.result.last_visited"],
    "tasks.result.items.country_iso_code": DOMAIN_PROFILE["tasks.result.country_iso_code"],
    "tasks.result.items.language_code": DOMAIN_PROFILE["tasks.result.language_code"],
    "tasks.result.items.content_language_code": DOMAIN_PROFILE["tasks.result.content_language_code"],
    "tasks.result.items.phone_numbers": DOMAIN_PROFILE["tasks.result.phone_numbers"],
    "tasks.result.items.emails": DOMAIN_PROFILE["tasks.result.emails"],
    "tasks.result.items.social_graph_urls": DOMAIN_PROFILE["tasks.result.social_graph_urls"],
    "tasks.result.items.technologies": DOMAIN_PROFILE["tasks.result.technologies"],
}

# ---- technologies_summary result ----
TECH_SUMMARY = {
    "tasks.result.countries": {
        "desc_en": "Distribution of domains by country with the count of websites per country.",
        "title_zh": "域名按国家的分布及每个国家的网站数量。",
    },
    "tasks.result.languages": {
        "desc_en": "Distribution of domains by language with the count of websites per language.",
        "title_zh": "域名按语言的分布及每种语言的网站数量。",
    },
    "tasks.result.content_languages": {
        "desc_en": "Distribution of domains by content language with the count of websites per language.",
        "title_zh": "域名按内容语言的分布及每种语言的网站数量。",
    },
    "tasks.result.keywords": {
        "desc_en": "Distribution of domains by keyword (found in titles, descriptions or meta keywords) with the count of websites per keyword.",
        "title_zh": "域名按关键词（取自标题、描述或 meta 关键词）的分布及每个关键词的网站数量。",
    },
}

# ---- technology_stats result (historical series) ----
TECH_STATS = {
    "tasks.result.technology": {
        "desc_en": "Technology the historical series describes, echoing the requested `technology`.",
        "title_zh": "历史序列所描述的技术，回显请求的 `technology`。",
    },
    "tasks.result.date_from": {
        "desc_en": "Start of the time range covered by the series, echoing the request.",
        "title_zh": "序列覆盖时间范围的起始日期，回显请求。",
    },
    "tasks.result.date_to": {
        "desc_en": "End of the time range covered by the series, echoing the request.",
        "title_zh": "序列覆盖时间范围的结束日期，回显请求。",
    },
    "tasks.result.items_count": {
        "desc_en": "Number of dated data points in the `items` series.",
        "title_zh": "`items` 序列中带日期的数据点数量。",
    },
    "tasks.result.items": {
        "desc_en": "Time series of usage snapshots, one entry per date.",
        "title_zh": "按日期排列的使用量快照时间序列，每个日期一个条目。",
    },
    "tasks.result.items.type": {
        "desc_en": "Element type marker for the data point; fixed value `technology_stats_item`.",
        "title_zh": "数据点的元素类型标记；固定值 `technology_stats_item`。",
    },
    "tasks.result.items.date": {
        "desc_en": "Date this data point describes.",
        "title_zh": "该数据点所对应的日期。",
    },
    "tasks.result.items.domains_count": {
        "desc_en": "Number of domains using the specified technology on this date.",
        "title_zh": "该日期使用所指定技术的域名数量。",
    },
    "tasks.result.items.countries": {
        "desc_en": "Distribution of using websites by country on this date, with the count per country.",
        "title_zh": "该日期使用该技术的网站按国家的分布及每国计数。",
    },
    "tasks.result.items.languages": {
        "desc_en": "Distribution of using websites by language on this date, with the count per language.",
        "title_zh": "该日期使用该技术的网站按语言的分布及每种语言的计数。",
    },
    "tasks.result.items.domains_rank": {
        "desc_en": "Distribution of using websites by backlink-rank range on this date, with the count per range.",
        "title_zh": "该日期使用该技术的网站按反链排名区间的分布及每区间的计数。",
    },
}

# ---- whois_overview result (deeply nested literal keys) ----
def pos_metric(channel_en, channel_zh, band):
    return {
        "desc_en": "Number of %s SERPs where the domain ranks #%s." % (channel_en, band),
        "title_zh": "该域名在 %s SERP 中排名第 %s 位的次数。" % (channel_zh, band),
    }


def metrics_block(prefix, ch_en, ch_zh):
    bands = ["1", "2_3", "4_10", "11_20", "21_30", "31_40", "41_50",
             "51_60", "61_70", "71_80", "81_90", "91_100"]
    band_disp = ["1", "2-3", "4-10", "11-20", "21-30", "31-40", "41-50",
                 "51-60", "61-70", "71-80", "81-90", "91-100"]
    d = {prefix: {
        "desc_en": "Ranking and traffic data from %s search for the domain." % ch_en,
        "title_zh": "该域名来自%s搜索的排名与流量数据。" % ch_zh,
    }}
    for b, disp in zip(bands, band_disp):
        d["%s.pos_%s" % (prefix, b)] = pos_metric(ch_en, ch_zh, disp)
    d["%s.etv" % prefix] = {
        "desc_en": "Estimated monthly %s traffic to the domain, computed as the product of CTR and search volume across all keywords it ranks for." % ch_en,
        "title_zh": "该域名预估的每月%s流量，按其排名的所有关键词的点击率与搜索量乘积求和计算。" % ch_zh,
    }
    d["%s.count" % prefix] = {
        "desc_en": "Total count of %s SERPs that contain the domain." % ch_en,
        "title_zh": "包含该域名的%s SERP 总数。" % ch_zh,
    }
    d["%s.estimated_paid_traffic_cost" % prefix] = {
        "desc_en": "Estimated monthly cost (USD) of buying ads to cover all keywords the domain ranks for in %s search, derived from traffic and CPC values." % ch_en,
        "title_zh": "为覆盖该域名在%s搜索中排名的全部关键词而投放广告的预估每月成本（美元），由流量与 CPC 推算。" % ch_zh,
    }
    return d


WHOIS = {
    "tasks.result.total_count": {
        "desc_en": "Total number of relevant results in the database matching your request, which may exceed the number returned.",
        "title_zh": "数据库中匹配你请求的相关结果总数，可能多于实际返回的条数。",
    },
    "tasks.result.items_count": {
        "desc_en": "Number of domain records returned in the `items` array.",
        "title_zh": "`items` 数组中返回的域名记录数量。",
    },
    "tasks.result.offset": {
        "desc_en": "The `offset` value applied to this result, echoing the request.",
        "title_zh": "本结果实际应用的 `offset` 值，回显请求。",
    },
    "tasks.result.offset_token": {
        "desc_en": "Token to fetch the next page; pass it as the request `offset_token` to page past the deep-offset limit and retrieve over 100,000 results across requests.",
        "title_zh": "用于翻下一页的令牌；作为请求 `offset_token` 传入，可越过深分页上限、跨多次请求获取超过 100,000 条结果。",
    },
    "tasks.result.items": {
        "desc_en": "Array of domain records, each combining Whois data with backlink, organic and paid search metrics.",
        "title_zh": "域名记录数组，每条记录将 Whois 数据与反链、自然及付费搜索指标合并。",
    },
    "tasks.result.items.domain": {
        "desc_en": "Domain name the record describes.",
        "title_zh": "该记录所描述的域名。",
    },
    "tasks.result.items.created_datetime": {
        "desc_en": "ISO 8601 date and time when the domain was first registered. Example: \"1997-03-29 03:00:00 +00:00\".",
        "title_zh": "该域名首次注册的 ISO 8601 日期时间。示例：\"1997-03-29 03:00:00 +00:00\"。",
    },
    "tasks.result.items.changed_datetime": {
        "desc_en": "ISO 8601 date and time when the domain's Whois entry was last modified. Example: \"2021-01-14 08:36:28 +00:00\".",
        "title_zh": "该域名 Whois 记录最后一次被修改的 ISO 8601 日期时间。示例：\"2021-01-14 08:36:28 +00:00\"。",
    },
    "tasks.result.items.expiration_datetime": {
        "desc_en": "ISO 8601 date and time when the domain registration is due to expire. Example: \"2022-11-26 17:21:23 +00:00\".",
        "title_zh": "该域名注册到期的 ISO 8601 日期时间。示例：\"2022-11-26 17:21:23 +00:00\"。",
    },
    "tasks.result.items.updated_datetime": {
        "desc_en": "ISO 8601 date and time when the domain was last updated. Example: \"2021-01-29 13:59:38 +00:00\".",
        "title_zh": "该域名最后一次更新的 ISO 8601 日期时间。示例：\"2021-01-29 13:59:38 +00:00\"。",
    },
    "tasks.result.items.first_seen": {
        "desc_en": "First time the DataForSEO crawler found the domain, in UTC `yyyy-mm-dd hh-mm-ss +00:00` format. Example: \"2019-11-15 12:57:46 +00:00\".",
        "title_zh": "DataForSEO 爬虫首次发现该域名的时间，采用 UTC `yyyy-mm-dd hh-mm-ss +00:00` 格式。示例：\"2019-11-15 12:57:46 +00:00\"。",
    },
    "tasks.result.items.epp_status_codes": {
        "desc_en": "EPP (Extensible Provisioning Protocol) status codes describing the domain's registration state as defined by ICANN.",
        "title_zh": "描述该域名注册状态的 EPP（可扩展配置协议）状态码，由 ICANN 定义。",
    },
    "tasks.result.items.tld": {
        "desc_en": "Top-level domain of the name within the DNS root zone.",
        "title_zh": "该域名在 DNS 根区中的顶级域。",
    },
    "tasks.result.items.registered": {
        "desc_en": "Whether the domain registration is currently active; `false` means it has expired (expired domains are retained only briefly).",
        "title_zh": "该域名注册当前是否有效；`false` 表示已过期（过期域名仅短期保留）。",
    },
    "tasks.result.items.registrar": {
        "desc_en": "Registrar managing the domain; `null` when unknown. Example: NameCheap, Inc.",
        "title_zh": "管理该域名的注册商；未知时为 `null`。示例：NameCheap, Inc.。",
    },
    "tasks.result.items.metrics": {
        "desc_en": "Ranking and traffic metrics for the domain, split into organic and paid search.",
        "title_zh": "该域名的排名与流量指标，分为自然搜索与付费搜索两部分。",
    },
    "tasks.result.items.backlinks_info": {
        "desc_en": "Backlink statistics for the domain from DataForSEO's Backlink Index.",
        "title_zh": "来自 DataForSEO 反链索引的该域名反链统计。",
    },
    "tasks.result.items.backlinks_info.referring_domains": {
        "desc_en": "Number of distinct domains that link to the target domain.",
        "title_zh": "链接到目标域名的不同域名数量。",
    },
    "tasks.result.items.backlinks_info.referring_main_domains": {
        "desc_en": "Number of distinct main (root) domains that link to the target domain.",
        "title_zh": "链接到目标域名的不同主（根）域名数量。",
    },
    "tasks.result.items.backlinks_info.referring_pages": {
        "desc_en": "Number of distinct pages that link to the target domain.",
        "title_zh": "链接到目标域名的不同页面数量。",
    },
    "tasks.result.items.backlinks_info.dofollow": {
        "desc_en": "Number of dofollow backlinks pointing to the target domain.",
        "title_zh": "指向目标域名的 dofollow 反链数量。",
    },
    "tasks.result.items.backlinks_info.backlinks": {
        "desc_en": "Total number of backlinks to the target domain, including both dofollow and nofollow links.",
        "title_zh": "指向目标域名的反链总数，包含 dofollow 与 nofollow 两类。",
    },
    "tasks.result.items.backlinks_info.time_update": {
        "desc_en": "Time the backlink data was last refreshed, in UTC `yyyy-mm-dd hh-mm-ss +00:00` format. Example: 2019-11-15 12:57:46 +00:00.",
        "title_zh": "反链数据最后一次刷新的时间，采用 UTC `yyyy-mm-dd hh-mm-ss +00:00` 格式。示例：2019-11-15 12:57:46 +00:00。",
    },
}
WHOIS.update(metrics_block("tasks.result.items.metrics.organic", "organic", "自然"))
WHOIS.update(metrics_block("tasks.result.items.metrics.paid", "paid", "付费"))

# ---- categories listing ----
CATEGORIES = {
    "tasks.result.category_code": {
        "desc_en": "Numeric code identifying the category; pass it as the `category_code` request field on Category Trends.",
        "title_zh": "标识该分类的数字代码；可作为请求字段 `category_code` 传入 Category Trends 接口。",
    },
    "tasks.result.category_name": {
        "desc_en": "Human-readable full name of the category.",
        "title_zh": "该分类的可读全名。",
    },
    "tasks.result.category_code_parent": {
        "desc_en": "Code of the parent (superordinate) category, letting you reconstruct the category hierarchy; `null` for top-level categories.",
        "title_zh": "上级（父）分类的代码，可据此重建分类层级；顶层分类为 `null`。",
    },
}

# ---- languages / locations listings ----
LANG_LIST = {
    "tasks.result.language_name": {
        "desc_en": "Human-readable full name of the language.",
        "title_zh": "该语言的可读全名。",
    },
    "tasks.result.language_code": {
        "desc_en": "ISO 639-1 code of the language; pass it as the `language_code` request field where supported.",
        "title_zh": "该语言的 ISO 639-1 代码；在支持处可作为请求字段 `language_code` 传入。",
    },
}
LOC_LIST = {
    "tasks.result.location_name": {
        "desc_en": "Human-readable full name of the location.",
        "title_zh": "该地区的可读全名。",
    },
    "tasks.result.country_iso_code": {
        "desc_en": "ISO country code of the location.",
        "title_zh": "该地区的 ISO 国家代码。",
    },
}

# ---- content_analysis trend block (category_trends + phrase_trends share) ----
TRENDS = {
    "tasks.result.type": {
        "desc_en": "Element type marker for the record; fixed value `content_analysis_trends`.",
        "title_zh": "记录的元素类型标记；固定值 `content_analysis_trends`。",
    },
    "tasks.result.date": {
        "desc_en": "Date (or period start) the trend data point describes, grouped per the request `date_group`.",
        "title_zh": "该趋势数据点对应的日期（或区间起点），按请求 `date_group` 分组。",
    },
    "tasks.result.total_count": TOTAL_COUNT,
    "tasks.result.rank": RANK_METRIC,
    "tasks.result.top_domains": TOP_DOMAINS,
    "tasks.result.sentiment_connotations": SENTIMENT_CONNOTATIONS,
    "tasks.result.connotation_types": CONNOTATION_TYPES,
    "tasks.result.text_categories": TEXT_CATEGORIES,
    "tasks.result.page_categories": PAGE_CATEGORIES,
    "tasks.result.page_types": PAGE_TYPES,
    "tasks.result.countries": COUNTRIES,
    "tasks.result.languages": LANGUAGES,
}

# ---- summary result (content_analysis summary) ----
SUMMARY = {
    "tasks.result.type": {
        "desc_en": "Element type marker for the record; fixed value `content_analysis_summary`.",
        "title_zh": "记录的元素类型标记；固定值 `content_analysis_summary`。",
    },
    "tasks.result.total_count": TOTAL_COUNT,
    "tasks.result.rank": {
        "desc_en": "Normalized sum of the ranks of all URLs citing the keyword; a higher value reflects stronger overall authority of the citing pages.",
        "title_zh": "引用该关键词的所有 URL 排名的归一化求和；值越高表示引用页面整体权威性越强。",
    },
    "tasks.result.top_domains": TOP_DOMAINS,
    "tasks.result.sentiment_connotations": SENTIMENT_CONNOTATIONS,
    "tasks.result.connotation_types": CONNOTATION_TYPES,
    "tasks.result.text_categories": TEXT_CATEGORIES,
    "tasks.result.page_categories": PAGE_CATEGORIES,
    "tasks.result.page_types": PAGE_TYPES,
    "tasks.result.countries": COUNTRIES,
    "tasks.result.languages": LANGUAGES,
}

# ---- rating_distribution result ----
RATING = {
    "tasks.result.type": {
        "desc_en": "Element type marker for the record; fixed value `content_analysis_rating_distribution`.",
        "title_zh": "记录的元素类型标记；固定值 `content_analysis_rating_distribution`。",
    },
    "tasks.result.min": {
        "desc_en": "Lower bound of the rating bucket on the distribution scale.",
        "title_zh": "分布刻度上该评分区间的下界。",
    },
    "tasks.result.max": {
        "desc_en": "Upper bound of the rating bucket on the distribution scale.",
        "title_zh": "分布刻度上该评分区间的上界。",
    },
    "tasks.result.metrics": {
        "desc_en": "Citation metrics aggregated for this rating bucket.",
        "title_zh": "针对该评分区间汇总的引用指标。",
    },
    "tasks.result.metrics.type": {
        "desc_en": "Element type marker for the metrics object; fixed value `content_analysis_summary`.",
        "title_zh": "指标对象的元素类型标记；固定值 `content_analysis_summary`。",
    },
    "tasks.result.metrics.total_count": TOTAL_COUNT,
    "tasks.result.metrics.rank": {
        "desc_en": "Normalized sum of the ranks of all URLs citing the keyword within this rating bucket.",
        "title_zh": "该评分区间内引用该关键词的所有 URL 排名的归一化求和。",
    },
    "tasks.result.metrics.top_domains": TOP_DOMAINS,
    "tasks.result.metrics.sentiment_connotations": SENTIMENT_CONNOTATIONS,
    "tasks.result.metrics.connotation_types": CONNOTATION_TYPES,
    "tasks.result.metrics.text_categories": TEXT_CATEGORIES,
    "tasks.result.metrics.page_categories": PAGE_CATEGORIES,
    "tasks.result.metrics.page_types": PAGE_TYPES,
    "tasks.result.metrics.countries": COUNTRIES,
    "tasks.result.metrics.languages": LANGUAGES,
}

# ---- search result (citation-level detail) ----
SEARCH = {
    "tasks.result.offset_token": {
        "desc_en": "Token to fetch the next page of citations; pass it as the request `offset_token` to page past the deep-offset limit and retrieve over 10,000 results across requests.",
        "title_zh": "用于翻取下一页引用的令牌；作为请求 `offset_token` 传入，可越过深分页上限、跨多次请求获取超过 10,000 条结果。",
    },
    "tasks.result.total_count": TOTAL_COUNT,
    "tasks.result.items_count": ITEMS_COUNT,
    "tasks.result.items": {
        "desc_en": "Array of individual citations and their associated content and ranking data.",
        "title_zh": "逐条引用及其相关内容与排名数据的数组。",
    },
    "tasks.result.items.type": {
        "desc_en": "Element type marker for the citation record; fixed value `content_analysis_search`.",
        "title_zh": "引用记录的元素类型标记；固定值 `content_analysis_search`。",
    },
    "tasks.result.items.url": {
        "desc_en": "URL of the page where the citation was found.",
        "title_zh": "发现该引用的页面 URL。",
    },
    "tasks.result.items.domain": {
        "desc_en": "Domain of the citing page.",
        "title_zh": "引用页面所属的域名。",
    },
    "tasks.result.items.main_domain": {
        "desc_en": "Main (root) domain of the citing page.",
        "title_zh": "引用页面的主（根）域名。",
    },
    "tasks.result.items.url_rank": {
        "desc_en": "Backlink-based rank of the specific URL from DataForSEO's Backlink Index; a higher value reflects a stronger backlink profile for the page.",
        "title_zh": "基于 DataForSEO 反链索引的该 URL 反链排名；值越高表示该页面反链档案越强。",
    },
    "tasks.result.items.spam_score": {
        "desc_en": "Backlink spam score of the URL from DataForSEO's Backlink Index; a higher value indicates a riskier backlink profile.",
        "title_zh": "基于 DataForSEO 反链索引的该 URL 反链垃圾分；值越高表示反链档案风险越大。",
    },
    "tasks.result.items.domain_rank": {
        "desc_en": "Backlink-based rank of the citing domain from DataForSEO's Backlink Index.",
        "title_zh": "基于 DataForSEO 反链索引的引用域名反链排名。",
    },
    "tasks.result.items.fetch_time": {
        "desc_en": "Time the DataForSEO crawler visited the page, in UTC `yyyy-mm-dd hh-mm-ss +00:00` format. Example: 2017-01-24 13:20:59 +00:00.",
        "title_zh": "DataForSEO 爬虫访问该页面的时间，采用 UTC `yyyy-mm-dd hh-mm-ss +00:00` 格式。示例：2017-01-24 13:20:59 +00:00。",
    },
    "tasks.result.items.country": {
        "desc_en": "Country code of the domain's registration; resolve via the Locations endpoint.",
        "title_zh": "该域名注册地的国家代码；可通过 Locations 接口解析。",
    },
    "tasks.result.items.language": {
        "desc_en": "Main language of the domain; resolve via the Languages endpoint.",
        "title_zh": "该域名的主要语言；可通过 Languages 接口解析。",
    },
    "tasks.result.items.score": {
        "desc_en": "Citation prominence score derived from url_rank, domain_rank and keyword presence in title, main_title, url and snippet; a higher score means a more valuable citation.",
        "title_zh": "引用显著度评分，由 url_rank、domain_rank 及关键词在 title、main_title、url、snippet 中的出现情况推算；分值越高引用越有价值。",
    },
    "tasks.result.items.page_category": {
        "desc_en": "Product and service categories relevant to the citing page; resolve codes via the Categories endpoint.",
        "title_zh": "与引用页面相关的产品及服务分类；分类代码可通过 Categories 接口解析。",
    },
    "tasks.result.items.page_types": {
        "desc_en": "Page types assigned to the citing page (e.g. ecommerce, news, blogs, message-boards, organization).",
        "title_zh": "为引用页面归类的页面类型（如 ecommerce、news、blogs、message-boards、organization）。",
    },
    "tasks.result.items.ratings": {
        "desc_en": "Ratings extracted from the page's microdata markup.",
        "title_zh": "从页面 microdata 标记中提取的评分。",
    },
    "tasks.result.items.social_metrics": {
        "desc_en": "Social media engagement metrics for the page, derived from platform-supported embeds.",
        "title_zh": "该页面的社交媒体互动指标，来自平台支持的嵌入组件。",
    },
    "tasks.result.items.content_info": {
        "desc_en": "Detailed information about the specific citation found at the URL.",
        "title_zh": "在该 URL 处发现的具体引用的详细信息。",
    },
    "tasks.result.items.content_info.content_type": {
        "desc_en": "Type of content the citation appears in. Example: page_content, comment.",
        "title_zh": "引用所在内容的类型。示例：page_content、comment。",
    },
    "tasks.result.items.content_info.title": {
        "desc_en": "Title of the content block carrying the citation.",
        "title_zh": "承载该引用的内容块标题。",
    },
    "tasks.result.items.content_info.main_title": {
        "desc_en": "Main title of the page.",
        "title_zh": "页面的主标题。",
    },
    "tasks.result.items.content_info.previous_title": {
        "desc_en": "Title of the content block preceding the citation, useful for locating it in the page structure.",
        "title_zh": "引用前一个内容块的标题，便于在页面结构中定位引用。",
    },
    "tasks.result.items.content_info.level": {
        "desc_en": "Heading level of the title, from 1 (top) to 6 (bottom), matching the page's h-tag depth.",
        "title_zh": "标题的标题级别，从 1（最高）到 6（最低），对应页面的 h 标签层级。",
    },
    "tasks.result.items.content_info.author": {
        "desc_en": "Author credited for the content, when available.",
        "title_zh": "内容标注的作者（如有）。",
    },
    "tasks.result.items.content_info.snippet": {
        "desc_en": "Excerpt of the content surrounding the citation.",
        "title_zh": "引用所在内容的摘录片段。",
    },
    "tasks.result.items.content_info.snippet_length": {
        "desc_en": "Character length of the snippet.",
        "title_zh": "摘录片段的字符长度。",
    },
    "tasks.result.items.content_info.social_metrics": {
        "desc_en": "Social media engagement metrics for this content block, derived from platform-supported embeds.",
        "title_zh": "该内容块的社交媒体互动指标，来自平台支持的嵌入组件。",
    },
    "tasks.result.items.content_info.highlighted_text": {
        "desc_en": "Portion of the snippet that matches the target keyword, highlighted for emphasis.",
        "title_zh": "摘录片段中与目标关键词匹配并被高亮的部分。",
    },
    "tasks.result.items.content_info.language": {
        "desc_en": "Language of the content; resolve via the Languages endpoint.",
        "title_zh": "该内容的语言；可通过 Languages 接口解析。",
    },
    "tasks.result.items.content_info.sentiment_connotations": {
        "desc_en": "Emotional reactions (e.g. anger, happiness, love, sadness) detected for this citation, each with its probability index.",
        "title_zh": "针对该引用检测到的情绪反应（如 anger、happiness、love、sadness）及各自的概率指数。",
    },
    "tasks.result.items.content_info.connotation_types": {
        "desc_en": "Sentiment polarity (positive, negative, neutral) detected for this citation, each with its probability index.",
        "title_zh": "针对该引用检测到的情感极性（positive、negative、neutral）及各自的概率指数。",
    },
    "tasks.result.items.content_info.text_category": {
        "desc_en": "Text categories assigned to this content; resolve codes via the Categories endpoint.",
        "title_zh": "为该内容归类的文本分类；分类代码可通过 Categories 接口解析。",
    },
    "tasks.result.items.content_info.date_published": {
        "desc_en": "Time the content was published, in UTC `yyyy-mm-dd hh-mm-ss +00:00` format. Example: 2017-01-24 13:20:59 +00:00.",
        "title_zh": "该内容的发布时间，采用 UTC `yyyy-mm-dd hh-mm-ss +00:00` 格式。示例：2017-01-24 13:20:59 +00:00。",
    },
    "tasks.result.items.content_info.content_quality_score": {
        "desc_en": "Content quality score derived from the number of words, sentences and characters in the content.",
        "title_zh": "内容质量评分，由内容的词数、句数与字符数推算。",
    },
    "tasks.result.items.content_info.semantic_location": {
        "desc_en": "Semantic HTML element where the keyword citation sits. Example: article, header.",
        "title_zh": "关键词引用所在的语义化 HTML 元素。示例：article、header。",
    },
    "tasks.result.items.content_info.rating": {
        "desc_en": "Rating associated with this content block.",
        "title_zh": "与该内容块关联的评分。",
    },
    "tasks.result.items.content_info.rating.name": {
        "desc_en": "Rating scale name. Possible values: Max5, Percents, CustomMax.",
        "title_zh": "评分刻度名称。可能取值：Max5、Percents、CustomMax。",
    },
    "tasks.result.items.content_info.rating.rating_value": {
        "desc_en": "The rating value on its scale.",
        "title_zh": "该评分在其刻度上的取值。",
    },
    "tasks.result.items.content_info.rating.max_rating_value": {
        "desc_en": "Maximum possible value for the named rating scale.",
        "title_zh": "所用评分刻度的最大可能值。",
    },
    "tasks.result.items.content_info.rating.rating_count": {
        "desc_en": "Number of votes behind the rating.",
        "title_zh": "构成该评分的投票数量。",
    },
    "tasks.result.items.content_info.rating.relative_rating": {
        "desc_en": "Rating normalized relative to its maximum, for cross-scale comparison.",
        "title_zh": "相对其最大值归一化后的评分，便于跨刻度比较。",
    },
    "tasks.result.items.content_info.group_date": {
        "desc_en": "Publication date or first-crawl time used to group citations chronologically.",
        "title_zh": "用于按时间分组引用的发布日期或首次抓取时间。",
    },
}

# ---- sentiment_analysis result (dynamic $positive / $anger buckets) ----
def conno_bucket(prefix, head_en, head_zh, key_en, key_zh):
    d = {
        prefix: {
            "desc_en": head_en,
            "title_zh": head_zh,
        },
        prefix + ".$" + key_en.split(",")[0].strip(): {
            "desc_en": "One %s bucket; the key takes one of: %s." % (key_en.split(":")[0], key_en.split(":")[1]),
            "title_zh": "单个%s分桶；键名取值之一：%s。" % (key_zh.split(":")[0], key_zh.split(":")[1]),
        },
    }
    return d


# Build the two sentiment distribution blocks explicitly (clearer than the helper).
SENTI = {
    "tasks.result.type": {
        "desc_en": "Element type marker for the record; fixed value `content_analysis_sentiment_analysis`.",
        "title_zh": "记录的元素类型标记；固定值 `content_analysis_sentiment_analysis`。",
    },
    "tasks.result.positive_connotation_distribution": {
        "desc_en": "Citations grouped by sentiment polarity (positive, negative, neutral), each group carrying its own full metric breakdown.",
        "title_zh": "按情感极性（positive、negative、neutral）分组的引用，每组各自携带完整的指标拆解。",
    },
    "tasks.result.positive_connotation_distribution.$positive": {
        "desc_en": "One polarity bucket; the dynamic key is one of positive, negative, or neutral, and the object holds that bucket's metrics.",
        "title_zh": "单个极性分桶；动态键名为 positive、negative 或 neutral 之一，对象内为该分桶的指标。",
    },
    "tasks.result.sentiment_connotation_distribution": {
        "desc_en": "Citations grouped by emotional reaction (anger, happiness, love, sadness, share, fun), each group carrying its own full metric breakdown.",
        "title_zh": "按情绪反应（anger、happiness、love、sadness、share、fun）分组的引用，每组各自携带完整的指标拆解。",
    },
    "tasks.result.sentiment_connotation_distribution.$anger": {
        "desc_en": "One sentiment bucket; the dynamic key is one of anger, happiness, love, sadness, share, or fun, and the object holds that bucket's metrics.",
        "title_zh": "单个情绪分桶；动态键名为 anger、happiness、love、sadness、share 或 fun 之一，对象内为该分桶的指标。",
    },
}


def _bucket_leaves(prefix):
    return {
        prefix + ".type": {
            "desc_en": "Element type marker for this bucket's metrics; fixed value `content_analysis_summary`.",
            "title_zh": "该分桶指标的元素类型标记；固定值 `content_analysis_summary`。",
        },
        prefix + ".total_count": {
            "desc_en": "Total number of relevant citations in this bucket.",
            "title_zh": "该分桶内相关引用的总数。",
        },
        prefix + ".rank": {
            "desc_en": "Normalized sum of the ranks of all relevant URLs in this bucket.",
            "title_zh": "该分桶内全部相关 URL 排名的归一化求和。",
        },
        prefix + ".top_domains": TOP_DOMAINS,
        prefix + ".sentiment_connotations": SENTIMENT_CONNOTATIONS,
        prefix + ".connotation_types": CONNOTATION_TYPES,
        prefix + ".text_categories": TEXT_CATEGORIES,
        prefix + ".page_categories": PAGE_CATEGORIES,
        prefix + ".page_types": PAGE_TYPES,
        prefix + ".countries": COUNTRIES,
        prefix + ".languages": LANGUAGES,
    }


SENTI.update(_bucket_leaves("tasks.result.positive_connotation_distribution.$positive"))
SENTI.update(_bucket_leaves("tasks.result.sentiment_connotation_distribution.$anger"))


# ---------------------------------------------------------------------------
# Request-field dictionaries.
# ---------------------------------------------------------------------------
REQ = {
    # technology query commons
    "group": {
        "desc_en": "Technology group id to query; at least one of group, category, technology or keyword must be set. Find valid ids via the technologies endpoint.",
        "title_zh": "要查询的技术分组 id；group、category、technology、keyword 四者至少需设置其一。有效 id 见 technologies 接口。",
    },
    "category": {
        "desc_en": "Technology category id to query; at least one of group, category, technology or keyword must be set. Find valid ids via the technologies endpoint.",
        "title_zh": "要查询的技术类别 id；group、category、technology、keyword 四者至少需设置其一。有效 id 见 technologies 接口。",
    },
    "technology": {
        "desc_en": "Technology name to query; at least one of group, category, technology or keyword must be set. Find valid names via the technologies endpoint.",
        "title_zh": "要查询的技术名称；group、category、technology、keyword 四者至少需设置其一。有效名称见 technologies 接口。",
    },
    "technology_single": {
        "desc_en": "Technology whose historical usage you want. Find valid names via the technologies endpoint. Example: \"Salesforce\".",
        "title_zh": "你想查询历史使用情况的技术。有效名称见 technologies 接口。示例：\"Salesforce\"。",
    },
    "keyword_meta": {
        "desc_en": "Keyword to match within a domain's meta keywords; at least one of group, category, technology or keyword must be set. UTF-8 encoded.",
        "title_zh": "要在域名 meta 关键词中匹配的关键词；group、category、technology、keyword 四者至少需设置其一。采用 UTF-8 编码。",
    },
    "mode": {
        "desc_en": "Match mode for the supplied group/category/technology terms, controlling whether results match exactly or partially.",
        "title_zh": "对所给 group/category/technology 词条的匹配模式，控制结果是精确匹配还是部分匹配。",
    },
    "filters": {
        "desc_en": "Result-filtering conditions (up to 8), combined with and/or logical operators; see the available-filters endpoint for the fields and operators you can use.",
        "title_zh": "结果过滤条件（最多 8 条），以 and/or 逻辑运算符组合；可用字段与运算符见 available-filters 接口。",
    },
    "order_by": {
        "desc_en": "Sorting rules for the results, each a field plus an asc/desc direction.",
        "title_zh": "结果排序规则，每条由字段加 asc/desc 方向组成。",
    },
    "internal_groups_list_limit": {
        "desc_en": "Cap on the number of returned items sharing the same `group`.",
        "title_zh": "限制返回结果中相同 `group` 的条目数量上限。",
    },
    "internal_categories_list_limit": {
        "desc_en": "Cap on the number of returned items sharing the same `category` within a group.",
        "title_zh": "限制同一分组内相同 `category` 的返回条目数量上限。",
    },
    "internal_technologies_list_limit": {
        "desc_en": "Cap on the number of returned items sharing the same `technology` within a category.",
        "title_zh": "限制同一类别内相同 `technology` 的返回条目数量上限。",
    },
    "internal_list_limit": {
        "desc_en": "Single cap applied to internal arrays (e.g. countries, languages, content_languages, keywords); when set, it overrides the per-level internal limits.",
        "title_zh": "对内部数组（如 countries、languages、content_languages、keywords）统一施加的上限；设置后会覆盖各级 internal 限制。",
    },
    "limit": {
        "desc_en": "Maximum number of records to return.",
        "title_zh": "返回记录数量的上限。",
    },
    "offset": {
        "desc_en": "Number of leading records to skip in the results array, for paging.",
        "title_zh": "结果数组中跳过的前导记录数，用于分页。",
    },
    "offset_token": {
        "desc_en": "Token from a prior response's identical field; supply it to fetch the subsequent batch and avoid timeouts when paging through very large result sets.",
        "title_zh": "取自上一次响应同名字段的令牌；传入以获取后续批次，并在翻阅超大结果集时避免超时。",
    },
    "tag": {
        "desc_en": "Your own task label (up to 255 characters) echoed back in the response's `tasks.data`, useful for matching results to requests.",
        "title_zh": "你自定义的任务标签（最多 255 字符），会在响应的 `tasks.data` 中回显，便于将结果与请求对应。",
    },
    # domain_technologies
    "target": {
        "desc_en": "Domain name of the website to analyze; results are returned for this domain only.",
        "title_zh": "要分析的网站域名；仅返回该域名的结果。",
    },
    # domains_by_html_terms
    "search_terms": {
        "desc_en": "HTML elements, tags, attributes or their content to match on a homepage; supplying several narrows results to domains containing all of them.",
        "title_zh": "要在首页上匹配的 HTML 元素、标签、属性或其内容；指定多个会将结果收窄为同时包含全部条件的域名。",
    },
    "keywords": {
        "desc_en": "Keywords to match in a domain's title, description or meta keywords (UTF-8, up to 10). Example: [\"seo\",\"software\"].",
        "title_zh": "要在域名标题、描述或 meta 关键词中匹配的关键词（UTF-8，最多 10 个）。示例：[\"seo\",\"software\"]。",
    },
    # domains_by_technology / technologies_summary multi-select selectors
    "technology_paths": {
        "desc_en": "Technology paths to query; one of technology_paths, groups, categories, technologies or keywords must be set. Each path pinpoints a technology within the group/category hierarchy.",
        "title_zh": "要查询的技术路径；technology_paths、groups、categories、technologies、keywords 至少需设置其一。每条路径在分组/类别层级中精确定位一项技术。",
    },
    "groups": {
        "desc_en": "Technology group ids to query; one of technology_paths, groups, categories, technologies or keywords must be set. Find valid ids via the technologies endpoint.",
        "title_zh": "要查询的技术分组 id；technology_paths、groups、categories、technologies、keywords 至少需设置其一。有效 id 见 technologies 接口。",
    },
    "categories": {
        "desc_en": "Technology category ids to query; one of technology_paths, groups, categories, technologies or keywords must be set. Find valid ids via the technologies endpoint.",
        "title_zh": "要查询的技术类别 id；technology_paths、groups、categories、technologies、keywords 至少需设置其一。有效 id 见 technologies 接口。",
    },
    "technologies": {
        "desc_en": "Technology names to query; one of technology_paths, groups, categories, technologies or keywords must be set. Find valid names via the technologies endpoint.",
        "title_zh": "要查询的技术名称；technology_paths、groups、categories、technologies、keywords 至少需设置其一。有效名称见 technologies 接口。",
    },
    # technology_stats
    "date_from_stats": {
        "desc_en": "Start date of the time range (format yyyy-mm-dd); defaults to the earliest available date when omitted. Minimum 2022-10-31. Example: \"2023-06-01\".",
        "title_zh": "时间范围的起始日期（格式 yyyy-mm-dd）；省略时默认取最早可用日期。最小值 2022-10-31。示例：\"2023-06-01\"。",
    },
    "date_to_stats": {
        "desc_en": "End date of the time range (format yyyy-mm-dd); defaults to today when omitted. Example: \"2023-01-15\".",
        "title_zh": "时间范围的结束日期（格式 yyyy-mm-dd）；省略时默认取当天。示例：\"2023-01-15\"。",
    },
    # content analysis trends/search/summary commons
    "keyword": {
        "desc_en": "Target keyword whose citations you want (UTF-8, lowercased on the server). To match an exact phrase rather than a standalone keyword, wrap it in escaped double quotes.",
        "title_zh": "你想查询其引用的目标关键词（UTF-8，服务端会转为小写）。若要匹配精确短语而非独立关键词，请用转义双引号包裹。",
    },
    "keyword_fields": {
        "desc_en": "Restrict matching to keywords that specific content fields must contain (e.g. title, main_title, previous_title); keys are field names and values are the keywords to require.",
        "title_zh": "将匹配限定为特定内容字段必须包含的关键词（如 title、main_title、previous_title）；键为字段名，值为要求包含的关键词。",
    },
    "page_type": {
        "desc_en": "Restrict results to these page types. Possible values: \"ecommerce\", \"news\", \"blogs\", \"message-boards\", \"organization\".",
        "title_zh": "将结果限定为这些页面类型。可能取值：\"ecommerce\"、\"news\"、\"blogs\"、\"message-boards\"、\"organization\"。",
    },
    "search_mode": {
        "desc_en": "How citations are grouped: `as_is` returns every citation, `one_per_domain` returns one citation per domain.",
        "title_zh": "引用的分组方式：`as_is` 返回全部引用，`one_per_domain` 每个域名只返回一条引用。",
    },
    "date_from_req": {
        "desc_en": "Start date of the time range (format yyyy-mm-dd). Example: \"2019-01-15\".",
        "title_zh": "时间范围的起始日期（格式 yyyy-mm-dd）。示例：\"2019-01-15\"。",
    },
    "date_from_cat": {
        "desc_en": "Start date of the time range (format yyyy-mm-dd); minimum 2022-10-31. Example: \"2019-01-15\".",
        "title_zh": "时间范围的起始日期（格式 yyyy-mm-dd）；最小值 2022-10-31。示例：\"2019-01-15\"。",
    },
    "date_to_req": {
        "desc_en": "End date of the time range (format yyyy-mm-dd); defaults to today when omitted. Example: \"2019-01-15\".",
        "title_zh": "时间范围的结束日期（格式 yyyy-mm-dd）；省略时默认取当天。示例：\"2019-01-15\"。",
    },
    "date_group": {
        "desc_en": "Granularity for grouping the time series. Possible values: day, week, month (default month).",
        "title_zh": "时间序列分组的粒度。可能取值：day、week、month（默认 month）。",
    },
    "initial_dataset_filters": {
        "desc_en": "Filters applied to the underlying Search dataset before trend/summary aggregation (up to 8), combined with and/or logical operators.",
        "title_zh": "在趋势/汇总聚合前对底层 Search 数据集施加的过滤条件（最多 8 条），以 and/or 逻辑运算符组合。",
    },
    "rank_scale": {
        "desc_en": "Scale used to present rank values; choose whether ranks are reported on a 0-100 or 0-1000 scale.",
        "title_zh": "用于呈现排名值的刻度；可选择以 0-100 或 0-1000 刻度报告排名。",
    },
    "category_code": {
        "desc_en": "Category code whose citations you want; obtain valid codes from the Categories endpoint.",
        "title_zh": "你想查询其引用的分类代码；有效代码见 Categories 接口。",
    },
    "positive_connotation_threshold": {
        "desc_en": "Probability threshold for positive sentiment; setting it filters which citations contribute to the connotation_types breakdown.",
        "title_zh": "正向情感的概率阈值；设置后会筛选哪些引用计入 connotation_types 拆解。",
    },
    "sentiments_connotation_threshold": {
        "desc_en": "Probability threshold for sentiment connotations; setting it filters which citations contribute to the sentiment_connotations breakdown.",
        "title_zh": "情绪连结的概率阈值；设置后会筛选哪些引用计入 sentiment_connotations 拆解。",
    },
}


def req_field(name, op_id):
    if name == "technology":
        return REQ["technology_single"] if "technology_stats" in op_id else REQ["technology"]
    if name == "keyword":
        return REQ["keyword_meta"] if "aggregation_technologies" in op_id else REQ["keyword"]
    if name == "date_from":
        if "technology_stats" in op_id:
            return REQ["date_from_stats"]
        if "category_trends" in op_id:
            return REQ["date_from_cat"]
        return REQ["date_from_req"]
    if name == "date_to":
        return REQ["date_to_stats"] if "technology_stats" in op_id else REQ["date_to_req"]
    return REQ[name]


# ---------------------------------------------------------------------------
# Operation-level docs (heading_zh + desc_en + description_zh).
# ---------------------------------------------------------------------------
OPS = {
    "post_dataforseo_domain_analytics_technologies_aggregation_technologies_live": (
        "List the technologies most commonly used alongside the technologies, categories or groups you specify, with domain counts per group, category and technology.",
        "列出与你指定的技术、类别或分组常一起使用的热门技术，并给出按分组、类别、技术统计的域名数量。",
        "聚合关联技术统计 aggregation_technologies"),
    "post_dataforseo_domain_analytics_technologies_domain_technologies_live": (
        "Return the full technology profile (plus meta, contact and locale data) of a single specified domain.",
        "返回单个指定域名的完整技术画像（含元信息、联系方式与地区数据）。",
        "查询单域名技术画像 domain_technologies"),
    "post_dataforseo_domain_analytics_technologies_domains_by_html_terms_live": (
        "Find domains whose homepage HTML contains the specified terms, returning each domain's technology profile and locale data.",
        "查找首页 HTML 包含指定词条的域名，并返回每个域名的技术画像与地区数据。",
        "按 HTML 词条反查域名 domains_by_html_terms"),
    "post_dataforseo_domain_analytics_technologies_domains_by_technology_live": (
        "Find domains that use the specified technologies, groups, categories or keywords, returning each domain's technology profile and locale data.",
        "查找使用指定技术、分组、类别或关键词的域名，并返回每个域名的技术画像与地区数据。",
        "按技术反查域名 domains_by_technology"),
    "get_dataforseo_domain_analytics_technologies_available_filters": (
        "List the filters available for the Domain Analytics Technologies endpoints, so you can build valid `filters` request fields. This endpoint is free.",
        "列出 Domain Analytics Technologies 各接口可用的过滤器，便于构建合法的请求字段 `filters`。该接口免费。",
        "查询技术接口可用过滤器 available_filters"),
    "get_dataforseo_domain_analytics_technologies_languages": (
        "List the languages supported by the Domain Analytics Technologies endpoints. This endpoint is free.",
        "列出 Domain Analytics Technologies 接口支持的语言。该接口免费。",
        "查询技术接口语言列表 languages"),
    "get_dataforseo_domain_analytics_technologies_locations": (
        "List the locations supported by the Domain Analytics Technologies endpoints. This endpoint is free.",
        "列出 Domain Analytics Technologies 接口支持的地区。该接口免费。",
        "查询技术接口地区列表 locations"),
    "get_dataforseo_domain_analytics_technologies_technologies": (
        "Return the full catalog of detectable technologies, organized into groups and categories; use the returned ids and names as selectors on the technology query endpoints.",
        "返回可检测技术的完整目录，按分组与类别组织；返回的 id 与名称可作为技术查询接口的选择器。",
        "查询全部可检测技术目录 technologies"),
    "post_dataforseo_domain_analytics_technologies_technologies_summary_live": (
        "Return how many domains, broken down by country and language, use the specified technologies, groups or categories.",
        "返回使用指定技术、分组或类别的域名数量，并按国家与语言拆分。",
        "查询技术使用汇总 technologies_summary"),
    "post_dataforseo_domain_analytics_technologies_technology_stats_live": (
        "Return a historical time series of how many domains, by country and language, used a specified technology over a date range.",
        "返回某项指定技术在某日期范围内被多少域名使用的历史时间序列，并按国家与语言拆分。",
        "查询技术使用历史趋势 technology_stats"),
    "get_dataforseo_domain_analytics_whois_available_filters": (
        "List the filters available for the Domain Analytics Whois endpoint, so you can build valid `filters` request fields. This endpoint is free.",
        "列出 Domain Analytics Whois 接口可用的过滤器，便于构建合法的请求字段 `filters`。该接口免费。",
        "查询 Whois 接口可用过滤器 available_filters"),
    "post_dataforseo_domain_analytics_whois_overview_live": (
        "Return Whois records for domains matching your filters, enriched with backlink stats and organic/paid search ranking and traffic metrics.",
        "返回匹配你过滤条件的域名 Whois 记录，并补充反链统计及自然/付费搜索的排名与流量指标。",
        "查询域名 Whois 概览 whois_overview"),
    "get_dataforseo_content_analysis_categories": (
        "Return the full list of Google product and service categories used by the Content Analysis endpoints, with their codes and parent codes.",
        "返回 Content Analysis 接口所用的 Google 产品与服务分类全表，含分类代码及父级代码。",
        "查询内容分析分类列表 categories"),
    "post_dataforseo_content_analysis_category_trends_live": (
        "Return a time series of citation data for a target category over a date range, broken down by sentiment, page type, top domains, country and language.",
        "返回某目标分类在某日期范围内的引用数据时间序列，并按情感、页面类型、热门域名、国家与语言拆分。",
        "查询分类引用趋势 category_trends"),
    "get_dataforseo_content_analysis_available_filters": (
        "List the filters available for the Content Analysis endpoints, so you can build valid `filters` request fields. This endpoint is free.",
        "列出 Content Analysis 各接口可用的过滤器，便于构建合法的请求字段 `filters`。该接口免费。",
        "查询内容分析可用过滤器 available_filters"),
    "get_dataforseo_content_analysis_languages": (
        "List the languages supported by the Content Analysis endpoints. This endpoint is free.",
        "列出 Content Analysis 接口支持的语言。该接口免费。",
        "查询内容分析语言列表 languages"),
    "get_dataforseo_content_analysis_locations": (
        "List the locations supported by the Content Analysis endpoints. This endpoint is free.",
        "列出 Content Analysis 接口支持的地区。该接口免费。",
        "查询内容分析地区列表 locations"),
    "post_dataforseo_content_analysis_phrase_trends_live": (
        "Return a time series of citation data for a target keyword over a date range, broken down by sentiment, page type, top domains, country and language.",
        "返回某目标关键词在某日期范围内的引用数据时间序列，并按情感、页面类型、热门域名、国家与语言拆分。",
        "查询关键词引用趋势 phrase_trends"),
    "post_dataforseo_content_analysis_rating_distribution_live": (
        "Return how citations of a target keyword are distributed across rating buckets, with the full citation metric breakdown per bucket.",
        "返回目标关键词的引用在各评分区间上的分布，并给出每个区间的完整引用指标拆解。",
        "查询关键词评分分布 rating_distribution"),
    "post_dataforseo_content_analysis_search_live": (
        "Return detailed, citation-level data for a target keyword, including each citing URL's content, ratings, sentiment and ranking metrics.",
        "返回目标关键词的逐条引用明细数据，包含每个引用 URL 的内容、评分、情感与排名指标。",
        "查询关键词引用明细 search"),
    "post_dataforseo_content_analysis_sentiment_analysis_live": (
        "Return sentiment analysis of a target keyword's citations, grouped by sentiment polarity and by emotional reaction, each with its own metric breakdown.",
        "返回目标关键词引用的情感分析，按情感极性与情绪反应分组，每组各带其指标拆解。",
        "查询关键词情感分析 sentiment_analysis"),
    "post_dataforseo_content_analysis_summary_live": (
        "Return an overview of the citation data available for a target keyword, including rank, sentiment, top domains and category/locale breakdowns.",
        "返回目标关键词可用引用数据的总览，含排名、情感、热门域名及分类/地区拆解。",
        "查询关键词引用总览 summary"),
}


# ---------------------------------------------------------------------------
# Per-op response extra resolver (chooses the right result-record dictionary).
# ---------------------------------------------------------------------------
def resp_extra(op_id):
    if "aggregation_technologies" in op_id:
        return AGG
    if "domain_technologies" in op_id:
        return DOMAIN_PROFILE
    if "domains_by_html_terms" in op_id or "domains_by_technology" in op_id:
        d = dict(DOMAINS_BY)
        d.update(DOMAIN_PROFILE)
        return d
    if op_id.endswith("technologies_available_filters") or op_id.endswith("whois_available_filters") \
            or op_id.endswith("content_analysis_available_filters"):
        return {}  # tasks.result handled specially (filters)
    if op_id.endswith("technologies_languages") or op_id.endswith("content_analysis_languages"):
        return LANG_LIST
    if op_id.endswith("technologies_locations") or op_id.endswith("content_analysis_locations"):
        return LOC_LIST
    if op_id.endswith("_technologies_technologies"):
        return TECH_LIST
    if "technologies_summary" in op_id:
        return TECH_SUMMARY
    if "technology_stats" in op_id:
        return TECH_STATS
    if "whois_overview" in op_id:
        return WHOIS
    if "content_analysis_categories" in op_id:
        return CATEGORIES
    if "category_trends" in op_id or "phrase_trends" in op_id:
        return TRENDS
    if "rating_distribution" in op_id:
        return RATING
    if "content_analysis_search" in op_id:
        return SEARCH
    if "sentiment_analysis" in op_id:
        return SENTI
    if "content_analysis_summary" in op_id:
        return SUMMARY
    raise KeyError("no resp_extra for " + op_id)


FILTER_OPS = ("technologies_available_filters", "whois_available_filters",
              "content_analysis_available_filters")


def resp_field(op_id, key, is_get):
    if key in ENVELOPE:
        return ENVELOPE[key]
    if key == "tasks.data":
        return TASKS_DATA_GET if is_get else TASKS_DATA_POST
    if key == "tasks.result" and any(op_id.endswith(f) for f in FILTER_OPS):
        return RESULT_FILTERS
    extra = resp_extra(op_id)
    if key in extra:
        return extra[key]
    raise KeyError("unmapped resp key %r in %s" % (key, op_id))


# ---------------------------------------------------------------------------
# Assemble.
# ---------------------------------------------------------------------------
operations = {}
fields = {}

for p, methods in spec["paths"].items():
    for m, op in methods.items():
        if m.lower() not in ("get", "post"):
            continue
        op_id = op.get("operationId") or (m.upper() + " " + p)
        de, dz, head = OPS[op_id]
        operations[op_id] = {"heading_zh": head, "desc_en": de, "description_zh": dz}

        fblock = {}
        is_get = m.lower() == "get"

        # request body
        rk = req_keys(op)
        if rk:
            fblock["request"] = {name: req_field(name, op_id) for name in rk}

        # response (only 200 carries a schema; others are empty)
        rsp = {}
        keys = resp200_keys(op)
        if keys:
            rsp["200"] = {k: resp_field(op_id, k, is_get) for k in keys}
        if rsp:
            fblock["response"] = rsp

        fields[op_id] = fblock

out = {"operations": operations, "fields": fields}
json.dump(out, open("parts/domain_content.content.json", "w"), ensure_ascii=False, indent=2)

nf = 0
for k, b in fields.items():
    nf += len(b.get("parameters", {}))
    nf += len(b.get("request", {}))
    for c, rr in b.get("response", {}).items():
        nf += len(rr)
print("ops:", len(operations), "field/param entries:", nf)
