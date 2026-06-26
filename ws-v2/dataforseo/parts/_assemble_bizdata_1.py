#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble bizdata_1.content.json from a hand-authored dual-field dictionary.

The dictionary below is authored by the agent per-field (intelligent writing, not
templated). This script only does mechanical mapping: it reads the real literal
property keys of each operation's request/response schema from the slice spec and
attaches the matching authored dual-field entry. Keys are resolved by:
  1. full literal key under the op's section (exact override) ELSE
  2. leaf field name (last dot segment) via shared dictionaries.
A KeyError is raised if any real key has no authored entry, so coverage is total.
"""
import json, sys

SPEC = "slices/bizdata_1.json"
OUT = "parts/bizdata_1.content.json"

def deref(spec, s):
    seen = 0
    sch = (spec.get("components") or {}).get("schemas") or {}
    while isinstance(s, dict) and "$ref" in s and seen < 20:
        seen += 1
        s = sch.get(s["$ref"].split("/")[-1], {})
    return s

def f(en, zh, ann=None):
    d = {"desc_en": en, "title_zh": zh}
    if ann:
        d["annotation"] = ann
    return d

# ---------------------------------------------------------------------------
# Shared response envelope (every op carries these). Authored once.
# ---------------------------------------------------------------------------
ENVELOPE = {
 "version": f("API version string that produced this response, e.g. `3.0.0`.",
              "生成该响应的 DataForSEO API 版本号，如 `3.0.0`。"),
 "version.status_code": f("Overall status code of the response envelope (DataForSEO global code, distinct from the per-task `tasks.status_code`); `20000` indicates the request was accepted successfully.",
              "整个响应信封的全局状态码（DataForSEO 全局编码，区别于单任务的 `tasks.status_code`）；`20000` 表示请求被成功受理。"),
 "version.status_message": f("Human-readable message accompanying the envelope `status_code`; read it when troubleshooting a non-success code.",
              "与信封 `status_code` 对应的可读说明；排查非成功状态码时参考此字段。"),
 "version.time": f("Wall-clock processing time of the whole request, expressed in seconds.",
              "整个请求的处理耗时，单位为秒。"),
 "version.cost": f("Total money charged for all tasks in this response, in US dollars.",
              "本次响应内全部任务合计扣费，单位美元（USD）。"),
 "version.tasks_count": f("Number of task objects contained in the `tasks` array.",
              "`tasks` 数组中包含的任务数量。"),
 "version.tasks_error": f("Number of task objects in `tasks` that finished with an error; if non-zero, inspect each task's `status_code`.",
              "`tasks` 数组中以错误结束的任务数量；若大于 0，请逐一检查任务的 `status_code`。"),
 "tasks": f("List of task objects, one per posted task, each holding its own status and `result` payload.",
              "任务对象列表，每个对应一个提交的任务，分别携带各自的状态与 `result` 数据。"),
 "tasks.id": f("Unique task identifier (UUID). Reuse it on the matching `task_get` endpoint to fetch this task's results within the retention window.",
              "任务唯一标识（UUID）。可在保留期内携带它调用对应的 `task_get` 接口取回本任务结果。"),
 "tasks.status_code": f("Per-task status code in the 10000-60000 range; `20000` means the task completed successfully while other values signal task-level errors.",
              "单个任务的状态码，取值区间 10000-60000；`20000` 表示任务成功，其它值代表任务级错误。"),
 "tasks.status_message": f("Human-readable message explaining this task's `status_code`.",
              "解释该任务 `status_code` 的可读说明。"),
 "tasks.time": f("Processing time of this individual task, in seconds.",
              "该单个任务的处理耗时，单位秒。"),
 "tasks.cost": f("Money charged for this individual task, in US dollars.",
              "该单个任务的扣费金额，单位美元（USD）。"),
 "tasks.result_count": f("Number of elements in this task's `result` array.",
              "该任务 `result` 数组中的元素数量。"),
 "tasks.path": f("URL path segments of the endpoint that produced this task, useful for tracing which call the task belongs to.",
              "生成该任务的接口 URL 路径片段，便于追溯任务归属的调用。"),
 "tasks.data": f("Echo of the parameters you supplied when posting the task, returned so you can correlate results with your input.",
              "回显你提交任务时所传的参数，便于将结果与输入对应起来。"),
 "result": f("Array holding the actual data payload of the task.",
              "承载任务实际数据的结果数组。"),
}

# Common "result.*" fields that echo POST params or describe the SERP fetch.
RESULT_COMMON = {
 "result.keyword": f("The search keyword echoed from your POST request, returned URL-decoded; if you passed a `cid:` value it is reflected here as well.",
              "回显你 POST 请求中的搜索关键词，已做 URL 解码；若传入的是 `cid:` 形式也会原样反映在此。"),
 "result.se_domain": f("Search engine domain used for this result, echoed from the POST request.",
              "本结果使用的搜索引擎域名，回显自 POST 请求。"),
 "result.location_code": f("Location code echoed from the POST request, identifying the geographic target of the search.",
              "回显自 POST 请求的地区编码，标识搜索的地理目标。"),
 "result.language_code": f("Language code echoed from the POST request, identifying the interface language of the search.",
              "回显自 POST 请求的语言编码，标识搜索的界面语言。"),
 "result.check_url": f("Direct URL to the live search engine results, so you can manually verify the data we returned.",
              "指向实时搜索引擎结果的直达链接，可用于人工核对我们返回的数据。"),
 "result.datetime": f("UTC timestamp of when this result was collected, format `yyyy-mm-dd hh-mm-ss +00:00`.",
              "采集该结果的 UTC 时间戳，格式为 `yyyy-mm-dd hh-mm-ss +00:00`。"),
 "result.cid": f("Google-defined client ID of the local establishment; can be reused with Google reviews endpoints to pull full review data.",
              "本地商户的 Google 客户端 ID（CID）；可配合 Google 评论类接口取回完整评论数据。"),
 "result.feature_id": f("Unique identifier of the SERP feature / business element returned for this result.",
              "本结果对应的 SERP 元素 / 商户的唯一标识符。"),
 "result.item_types": f("List of distinct element types present in the `items` array, letting you know which item schemas to expect.",
              "`items` 数组中出现的元素类型清单，提示你应预期哪些条目结构。"),
 "result.items_count": f("Number of items returned in the `items` array; raise it via the `depth` parameter when posting a task.",
              "`items` 数组返回的条目数量；提交任务时可用 `depth` 参数提高。"),
 "result.type": f("Element type tag of this result entry.",
              "该结果条目的元素类型标记。"),
 "result.title": f("Business / establishment name this result was collected for.",
              "本结果所采集的商户 / 场所名称。"),
 "result.location": f("Address of the establishment this result was collected for.",
              "本结果所采集场所的地址。"),
 "result.domain": f("Domain of the business entity.",
              "商户的域名。"),
 "result.url_path": f("URL path echoed from the POST request.",
              "回显自 POST 请求的 URL 路径。"),
 "result.se_type": f("Search engine type echoed from the POST request.",
              "回显自 POST 请求的搜索引擎类型。"),
}

# tasks_ready endpoints share this result shape.
TASKS_READY = {
 "result.id": f("UUID of a completed task that is ready for collection; pass it to the corresponding `task_get` endpoint.",
              "已完成、可供领取的任务 UUID；将其传给对应的 `task_get` 接口即可取回结果。"),
 "result.se": f("Search engine the completed task was set for.",
              "该已完成任务所设定的搜索引擎。"),
 "result.se_type": f("Search engine type of the completed task.",
              "该已完成任务的搜索引擎类型。"),
 "result.date_posted": f("UTC date when the task was originally posted.",
              "该任务最初提交的 UTC 日期。"),
 "result.tag": f("Your own user-defined task identifier echoed back, so you can match ready tasks to your bookkeeping.",
              "回显你自定义的任务标识，便于将就绪任务与自有记录对应。"),
 "result.endpoint": f("Ready-made endpoint path you can call to collect this task's results.",
              "可直接调用以领取该任务结果的接口路径。"),
}

# ---------------------------------------------------------------------------
# Leaf-name dictionary for nested item/listing/review fields. Authored per name.
# ---------------------------------------------------------------------------
LEAF = {
 # geometry / location
 "latitude": f("Latitude coordinate of the entity on Google Maps.", "该实体在 Google 地图上的纬度坐标。"),
 "longitude": f("Longitude coordinate of the entity on Google Maps.", "该实体在 Google 地图上的经度坐标。"),
 "location": f("Location object holding the entity's geographic coordinates.", "承载实体地理坐标的位置对象。"),
 "address": f("Street address of the business entity.", "商户的街道地址。"),
 "address_info": f("Structured object breaking the address into individual components.", "将地址拆分为各组成部分的结构化对象。"),
 "full_address": f("Full address of the entity in standardized format.", "标准化格式的实体完整地址。"),
 "borough": f("Administrative district or borough the entity belongs to.", "实体所属的行政区或区划。"),
 "city": f("City where the entity is located.", "实体所在城市。"),
 "zip": f("ZIP / postal code of the entity.", "实体的邮政编码。"),
 "region": f("DMA region of the entity's location.", "实体所在地的 DMA 区域。"),
 "country_code": f("ISO country code of the entity's location.", "实体所在地的 ISO 国家代码。"),
 "maps_url": f("URL to the entity's location on Google Maps.", "实体在 Google 地图上的位置链接。"),
 "neighborhood": f("Name of the neighborhood the hotel is located in.", "酒店所在街区的名称。"),
 "neighborhood_description": f("Free-text description of the hotel's neighborhood.", "酒店所在街区的文字描述。"),

 # identifiers / urls
 "cid": f("Google-defined client ID uniquely identifying the local establishment.", "唯一标识本地商户的 Google 客户端 ID（CID）。"),
 "feature_id": f("Unique identifier of the element / establishment in the SERP.", "该元素 / 商户在 SERP 中的唯一标识符。"),
 "place_id": f("Google Place ID of the local establishment featured in the element.", "该元素所含本地商户的 Google Place ID。"),
 "hotel_identifier": f("Unique Google identifier of a hotel entity; pass it as `hotel_identifier` to the Hotel Info endpoint.", "酒店实体的 Google 唯一标识；可作为 `hotel_identifier` 传给 Hotel Info 接口。"),
 "card_id": f("Identifier of the hotel card element.", "酒店卡片元素的标识符。"),
 "business_updates_id": f("Identifier of the business-updates element in the SERP.", "SERP 中商家动态元素的标识符。"),
 "url": f("Absolute URL associated with this element.", "与该元素关联的绝对 URL。"),
 "page_url": f("Target page URL this data was collected for, echoed from the `targets` array.", "采集该数据所针对的目标页面 URL，回显自 `targets` 数组。"),
 "domain": f("Domain of the business entity.", "商户的域名。"),
 "contact_url": f("URL of the establishment's preferred contact page.", "商户首选联系页面的 URL。"),
 "contributor_url": f("URL of the contributor's Local Guides profile, when available.", "贡献者 Local Guides 主页的 URL（若有）。"),
 "book_online_url": f("URL behind the element's 'book online' button, leading to the booking or order page.", "元素「在线预订」按钮指向的链接，通往预订或下单页面。"),
 "logo": f("URL of the logo shown in the Google My Business profile.", "Google 商家资料中展示的 logo 图片 URL。"),
 "main_image": f("URL of the main image shown in the Google My Business profile.", "Google 商家资料中展示的主图 URL。"),
 "total_photos": f("Total number of images featured in the Google My Business profile.", "Google 商家资料中收录的图片总数。"),
 "phone": f("Phone number of the business entity.", "商户的联系电话。"),
 "snippet": f("Additional descriptive snippet about the business entity.", "关于商户的附加描述片段。"),

 # names / titles / descriptions
 "title": f("Title / name shown for the element in the SERP.", "该元素在 SERP 中显示的标题 / 名称。"),
 "original_title": f("Original element title as shown by Google, before any translation.", "Google 显示的元素原始标题，未经翻译。"),
 "name": f("Display name of the reviewer or entity.", "评论者或实体的显示名称。"),
 "description": f("Description of the business entity shown in the SERP.", "SERP 中显示的商户描述。"),
 "category": f("Primary Google My Business category that best describes the entity's services.", "最能概括该实体服务的 Google 商家主分类。"),
 "category_ids": f("Global category IDs that stay constant regardless of the selected country.", "不随所选国家变化的全局分类 ID。"),
 "additional_categories": f("Additional Google My Business categories detailing the entity's services.", "更细致描述该实体服务的附加 Google 商家分类。"),
 "category_label": f("Display label of the amenity category.", "便利设施分类的展示标签。"),

 # rating block
 "rating": f("Rating object summarizing review-based popularity of the entity.", "汇总实体基于评论的人气评分对象。"),
 "rating_type": f("Rating scale in use; values include `Max5`, `Percents`, `CustomMax`, indicating how `value` should be interpreted.", "所用评分量纲，取值如 `Max5`、`Percents`、`CustomMax`，决定 `value` 的解读方式。"),
 "value": f("Numeric rating value, interpreted according to `rating_type`.", "评分数值，需结合 `rating_type` 解读。"),
 "votes_count": f("Number of votes / reviews the rating is based on.", "评分所依据的投票 / 评论数量。"),
 "rating_max": f("Maximum possible value for the given `rating_type`.", "对应 `rating_type` 的最大可能取值。"),
 "rating_distribution": f("Object breaking down vote counts per star level (1 through 5).", "按 1-5 星逐级拆分投票数的对象。"),
 "reviews_count": f("Total number of reviews for the entity.", "该实体的评论总数。"),
 "hotel_rating": f("Hotel class rating ranging 1-5 stars; `null` when no class rating exists.", "酒店星级评定，范围 1-5 星；无星级信息时为 `null`。"),
 "price_level": f("Relative price level; values: `inexpensive`, `moderate`, `expensive`, `very_expensive`; `null` when unknown.", "相对价格档次，取值 `inexpensive`、`moderate`、`expensive`、`very_expensive`；未知时为 `null`。"),

 # star-distribution numeric keys 1..5 (overridden by full-key for some ops)
 "1": f("Number of 1-star ratings.", "1 星评分的数量。"),
 "2": f("Number of 2-star ratings.", "2 星评分的数量。"),
 "3": f("Number of 3-star ratings.", "3 星评分的数量。"),
 "4": f("Number of 4-star ratings.", "4 星评分的数量。"),
 "5": f("Number of 5-star ratings.", "5 星评分的数量。"),

 # ranking / position
 "rank_group": f("Position of the element within the group of elements sharing the same `type`.", "该元素在同 `type` 元素分组内的位置。"),
 "rank_absolute": f("Absolute position of the element among all returned elements.", "该元素在全部返回元素中的绝对位置。"),
 "position": f("Layout alignment of the element in the SERP, e.g. `right`.", "该元素在 SERP 中的版面对齐方式，如 `right`。"),
 "type": f("Type tag of this element, identifying its schema.", "该元素的类型标记，用于识别其结构。"),
 "xpath": f("XPath locating the element within the source page.", "定位该元素在源页面中位置的 XPath。"),

 # attributes / topics
 "attributes": f("Service-detail checks for the entity, derived from user feedback and its `category`.", "基于用户反馈与 `category` 生成的商户服务细节勾选项。"),
 "available_attributes": f("Attributes the entity is reported to offer.", "该实体被标记为可提供的属性。"),
 "unavailable_attributes": f("Attributes the entity is reported not to offer.", "该实体被标记为不提供的属性。"),
 "place_topics": f("Most-mentioned keywords from customer reviews mapped to how many reviews mention each.", "客户评论中最常被提及的关键词及各自被提及的评论数。"),
 "people_also_search": f("Related business entities that users also searched for.", "用户还搜索过的相关商户。"),
 "is_claimed": f("Whether the entity has been verified by its owner on Google Maps.", "该实体是否已被所有者在 Google 地图上认证。"),
 "local_justifications": f("Google local justifications: snippets explaining why the business matches the query.", "Google 本地匹配理由：解释该商户为何匹配查询的文字片段。"),

 # working hours
 "work_time": f("Object describing the entity's operating-hours details.", "描述实体营业时间细节的对象。"),
 "work_hours": f("Object describing the establishment's working hours.", "描述商户营业时间的对象。"),
 "timetable": f("Weekly timetable of working hours.", "按周排列的营业时间表。"),
 "sunday": f("Working hours on Sunday.", "周日的营业时间。"),
 "monday": f("Working hours on Monday.", "周一的营业时间。"),
 "tuesday": f("Working hours on Tuesday.", "周二的营业时间。"),
 "wednesday": f("Working hours on Wednesday.", "周三的营业时间。"),
 "thursday": f("Working hours on Thursday.", "周四的营业时间。"),
 "friday": f("Working hours on Friday.", "周五的营业时间。"),
 "saturday": f("Working hours on Saturday.", "周六的营业时间。"),
 "open": f("Opening-time object with `hour` and `minute`.", "开门时间对象，含 `hour` 与 `minute`。"),
 "close": f("Closing-time object with `hour` and `minute`.", "关门时间对象，含 `hour` 与 `minute`。"),
 "hour": f("Hour component in 24-hour format.", "小时分量，采用 24 小时制。"),
 "minute": f("Minute component.", "分钟分量。"),
 "current_status": f("Current operating status; values include `open`/`opened`, `close`/`closed`, `temporarily_closed`, `closed_forever`.", "当前营业状态，取值如 `open`/`opened`、`close`/`closed`、`temporarily_closed`、`closed_forever`。"),

 # popular times
 "popular_times": f("Object describing busy-hour patterns of the establishment.", "描述商户繁忙时段规律的对象。"),
 "popular_times_by_days": f("Busy-hour breakdown for each day of the week.", "按一周每天拆分的繁忙时段。"),
 "time": f("Busy-hours time object with `hour` and `minute`.", "繁忙时段的时间对象，含 `hour` 与 `minute`。"),
 "popular_index": f("Time-bound popularity index from 0 to 100; higher means busier.", "时段人气指数，范围 0-100，越高表示越繁忙。"),

 # local business links
 "delivery_services": f("List of available delivery services for the establishment.", "该商户可用的配送服务列表。"),
 "is_directory_item": f("Whether the establishment is part of a shared-address directory (e.g. a mall); `null` for a parent directory item.", "该商户是否属于共用地址的目录条目（如商场）；若为目录父项则为 `null`。"),

 # contact info
 "contact_info": f("List of the business's available contacts (e.g. phone, website) you can use to reach it directly from search results.", "商户可用联系方式列表（如电话、网站），可直接从搜索结果发起联系。"),
 "local_business_links": f("List of available interactions with the business directly from the search results, such as booking, ordering or messaging links.", "可直接从搜索结果与商户互动的入口列表，如预订、下单或消息链接。"),
 "items_without_answers": f("Array of Google business question items that currently have no answers.", "目前尚无回答的 Google 商家问题条目数组。"),
 "source": f("Data source of the contact entry.", "该联系信息条目的数据来源。"),
 "check_url": f("Direct URL to the search results, for verifying the data.", "指向搜索结果的直达链接，用于核对数据。"),
 "last_updated_time": f("UTC timestamp when this contact data was last updated.", "该联系信息最后更新的 UTC 时间戳。"),
 "first_seen": f("UTC timestamp when our crawler first encountered this element.", "我方爬虫首次发现该元素的 UTC 时间戳。"),

 # hotel info specifics
 "about": f("Object holding descriptive information about the hotel.", "承载酒店介绍信息的对象。"),
 "sub_descriptions": f("Additional descriptive details supplementing the hotel description.", "对酒店描述加以补充的附加说明。"),
 "check_in_time": f("Hotel check-in time as listed.", "酒店挂牌的入住时间。"),
 "check_out_time": f("Hotel check-out time as listed.", "酒店挂牌的退房时间。"),
 "stars": f("Hotel class rating in stars (1-5).", "酒店星级评定（1-5 星）。"),
 "stars_description": f("Text form of the hotel class rating shown in the summary.", "摘要中以文字形式呈现的酒店星级。"),
 "amenities": f("Hotel amenities grouped by category.", "按分类归组的酒店便利设施。"),
 "amenity": f("Standardized amenity name.", "标准化的便利设施名称。"),
 "amenity_label": f("Display name of the amenity as shown to users.", "面向用户展示的便利设施名称。"),
 "hint": f("Standardized detail note about the amenity.", "关于该便利设施的标准化细节说明。"),
 "hint_label": f("Display detail note about the amenity.", "面向展示的便利设施细节说明。"),
 "is_available": f("Whether the amenity is available at the hotel.", "该便利设施在酒店是否可用。"),
 "popular_amenities": f("Hotel amenities labelled as 'popular'.", "被标记为「热门」的酒店便利设施。"),
 "location_chain": f("Elements of the hotel's location chain with their parameters.", "酒店所属位置链的各元素及其参数。"),
 "overall_score": f("Overall location score from 1 to 5, blending proximity to things to do, restaurants, transit and airports (criteria not equally weighted).", "1-5 的综合位置评分，综合考量周边景点、餐饮、交通与机场的便利度（各项权重不等）。"),
 "score_by_categories": f("Per-category location scores (things to do, restaurants, transit, airports).", "按类别拆分的位置评分（景点、餐饮、交通、机场）。"),
 "overall": f("Overall location score from 1 to 5.", "1-5 的综合位置评分。"),
 "things_to_do": f("Location score (1-5) for proximity to nearby things to do.", "周边景点便利度的位置评分（1-5）。"),
 "restaurants": f("Location score (1-5) for proximity to nearby restaurants.", "周边餐饮便利度的位置评分（1-5）。"),
 "transit": f("Location score (1-5) for proximity to transit options.", "周边交通便利度的位置评分（1-5）。"),
 "airport_access": f("Location score (1-5) for proximity to airports.", "周边机场便利度的位置评分（1-5）。"),
 "reviews": f("Object with hotel review and rating information, broken down by criteria.", "按各维度拆分的酒店评论与评分信息对象。"),
 "mentions": f("Hotel review mentions broken down by criterion.", "按维度拆分的酒店评论提及信息。"),
 "positive_score": f("Positive score for the criterion.", "该维度的正面评分。"),
 "positive_count": f("Number of positive reviews for the criterion.", "该维度的正面评论数。"),
 "negative_count": f("Number of negative reviews for the criterion.", "该维度的负面评论数。"),
 "total_count": f("Total number of reviews for the criterion.", "该维度的评论总数。"),
 "visible_by_default": f("Whether the review element is shown by default.", "该评论元素是否默认展示。"),
 "other_sites_reviews": f("Reviews aggregated from third-party sites.", "聚合自第三方站点的评论。"),
 "review_text": f("Text content of the review.", "评论的文本内容。"),
 "overview_images": f("URLs of images shown in the hotel overview.", "酒店概览中展示的图片 URL。"),
 "prices": f("Pricing details for the hotel stay.", "酒店住宿的价格明细对象。"),
 "price": f("Price per night.", "每晚价格。"),
 "price_without_discount": f("Price per night before any discount is applied.", "未应用折扣前的每晚价格。"),
 "currency": f("Currency of the price, e.g. `USD`.", "价格货币，如 `USD`。"),
 "discount_text": f("Text describing the applied discount.", "描述所应用折扣的文字。"),
 "check_in": f("Check-in date-time in UTC, format `yyyy-mm-dd hh-mm-ss +00:00`.", "入住日期时间（UTC），格式 `yyyy-mm-dd hh-mm-ss +00:00`。"),
 "check_out": f("Check-out date-time in UTC, format `yyyy-mm-dd hh-mm-ss +00:00`.", "退房日期时间（UTC），格式 `yyyy-mm-dd hh-mm-ss +00:00`。"),
 "check_in_date": f("Check-in date in UTC.", "入住日期（UTC）。"),
 "check_out_date": f("Check-out date in UTC.", "退房日期（UTC）。"),
 "visitors": f("Number of visitors the price applies to.", "该价格所对应的入住人数。"),
 "max_visitors": f("Maximum number of visitors the price offer is valid for.", "该价格方案有效的最大入住人数。"),
 "is_paid": f("Whether this is a paid listing/ad (`true`) versus an organic/free booking link (`false`).", "是否为付费展示/广告（`true`），否则为自然/免费预订链接（`false`）。"),
 "free_cancellation_until": f("UTC date until which free cancellation is available; `null` if free cancellation is not offered.", "可免费取消的截止 UTC 日期；不提供免费取消时为 `null`。"),
 "offers": f("Array of featured price offers.", "精选价格方案数组。"),
 "offer_images": f("URLs of images featured in the price offer.", "价格方案中展示的图片 URL。"),
 "prices_by_dates": f("Array of hotel stay prices broken down by date.", "按日期拆分的酒店住宿价格数组。"),
 "items": f("Array of nested item elements belonging to this entry.", "归属于该条目的嵌套子项数组。"),

 # SERP listing extras
 "count": f("Number of items in the `items` array.", "`items` 数组中的条目数量。"),
 "total_count": f("Total number of matching results available in our database for your request.", "我方数据库中与请求匹配的可用结果总数。"),
 "offset": f("Offset position within the returned businesses array.", "返回商户数组中的偏移位置。"),
 "offset_token": f("Token enabling pagination: pass it on a follow-up task to retrieve the next batch of results; each token is single-use per follow-up.", "分页令牌：在后续任务中传入即可取回下一批结果；每个令牌对应一次后续请求且互不相同。"),

 # reviews (tripadvisor / trustpilot / extended)
 "date_of_visit": f("UTC date of the reviewer's visit to the establishment.", "评论者到访该场所的 UTC 日期。"),
 "timestamp": f("UTC timestamp when the item was published, format `yyyy-mm-dd hh-mm-ss +00:00`.", "该条目发布的 UTC 时间戳，格式 `yyyy-mm-dd hh-mm-ss +00:00`。"),
 "review_id": f("Identifier of the review.", "评论的标识符。"),
 "language": f("Language of the review text.", "评论文本的语言。"),
 "original_language": f("Language of the original untranslated review text.", "未翻译的原始评论文本语言。"),
 "review_images": f("URLs of images attached to the review.", "评论附带图片的 URL。"),
 "user_profile": f("Object holding the reviewer's profile information.", "承载评论者个人资料信息的对象。"),
 "image_url": f("URL of the reviewer's profile image.", "评论者头像图片的 URL。"),
 "responses": f("Array holding the business owner's response(s) to the review.", "承载商家对评论回复内容的数组。"),
 "text": f("Text of the owner's response.", "商家回复的文本。"),
 "response_id": f("Identifier of the owner's response.", "商家回复的标识符。"),
 "review_highlights": f("Highlighted review criteria with their assessments.", "突出展示的评论维度及其评价。"),
 "feature": f("Reviewed feature being highlighted.", "被突出评价的维度特征。"),
 "assessment": f("Assessment given for the highlighted feature.", "对该突出特征给出的评价。"),
 "verified": f("Whether the review carries the 'Verified' badge.", "该评论是否带有「已验证」标记。"),

 # Q&A
 "question_id": f("Identifier of the question.", "问题的标识符。"),
 "profile_image_url": f("URL of the asking/answering user's profile image.", "提问/回答用户头像图片的 URL。"),
 "profile_url": f("URL of the user's profile.", "该用户主页的 URL。"),
 "profile_name": f("Display name of the user.", "该用户的显示名称。"),
 "question_text": f("Current text of the question.", "问题的当前文本。"),
 "original_question_text": f("Original text of the question before any edit.", "问题在被编辑前的原始文本。"),
 "time_ago": f("Approximate relative time when the item was posted.", "该条目发布的大致相对时间。"),
 "items_count": f("Number of items in the nested `items` array.", "嵌套 `items` 数组中的条目数量。"),
 "answer_id": f("Identifier of the answer.", "回答的标识符。"),
 "answer_text": f("Current text of the answer.", "回答的当前文本。"),
 "original_answer_text": f("Original text of the answer before any edit.", "回答在被编辑前的原始文本。"),

 # google business updates posts
 "author": f("Author of the post.", "动态的作者。"),
 "post_text": f("Main body text of the post.", "动态的正文文本。"),
 "images_url": f("URL of an image included in the post.", "动态中所含图片的 URL。"),
 "post_date": f("Publish date of the post, format `mm/dd/yyyy hh:mm:ss`.", "动态发布日期，格式 `mm/dd/yyyy hh:mm:ss`。"),
 "links": f("Links included in the post.", "动态中包含的链接。"),

 # pinterest
 "pins_count": f("Number of Pinterest saves (pins) made from the related `page_url` via the Pinterest Save Button.", "通过 Pinterest 保存按钮从对应 `page_url` 产生的收藏（pin）数量。"),
 "directory": f("Directory entries: businesses sharing the target establishment's address.", "目录条目：与目标商户共用地址的商户集合。"),
}

# Full-key overrides where the same leaf name carries op-specific meaning.
FULL_OVERRIDE = {
 # hotel info: hour/minute belong to check_in/out time objects
 # (kept generic; leaf already adequate)
 "items.mentions": f("Hotel mentions placeholder; in hotel-search results this field is always `null` and exists only for interoperability with the Hotel Info endpoint.", "酒店提及占位字段；在酒店搜索结果中恒为 `null`，仅为与 Hotel Info 接口保持互通而保留。"),
 "items.rating_distribution": f("Rating-distribution placeholder; in hotel-search results this field is always `null` and exists only for interoperability with the Hotel Info endpoint.", "评分分布占位字段；在酒店搜索结果中恒为 `null`，仅为与 Hotel Info 接口保持互通而保留。"),
 "items.other_sites_reviews": f("Third-party reviews placeholder; in hotel-search results this field is always `null` and exists only for interoperability with the Hotel Info endpoint.", "第三方评论占位字段；在酒店搜索结果中恒为 `null`，仅为与 Hotel Info 接口保持互通而保留。"),
 "items.items": f("Nested items placeholder; in hotel-search results this field is always `null` and exists only for interoperability with the Hotel Info endpoint.", "嵌套子项占位字段；在酒店搜索结果中恒为 `null`，仅为与 Hotel Info 接口保持互通而保留。"),
 "items.assessment": f("Assessment text for the highlighted review feature.", "对突出评论维度给出的评价文本。"),
 "items.language": f("Language of the review text.", "评论文本的语言。"),
 "items.reviews_count": f("Total number of reviews submitted by the reviewer.", "该评论者提交的评论总数。"),
 "items.location": f("Reviewer's stated location (e.g. country).", "评论者标注的所在地（如国家）。"),
}

# ---------------------------------------------------------------------------
# Request-body field dictionary (nested request schemas; authored per field).
# ---------------------------------------------------------------------------
REQUEST = {
 "keyword": f("Search keyword identifying the local establishment; URL-encode it and keep it within the endpoint's character limit. Required when neither `cid` nor `place_id` is supplied.",
              "用于定位本地商户的搜索关键词；需 URL 编码并遵守接口字符上限。未提供 `cid` 或 `place_id` 时此字段必填。"),
 "cid": f("Google-defined unique ID of the business entity. Required when neither `keyword` nor `place_id` is supplied.",
              "商户实体的 Google 唯一标识（CID）。未提供 `keyword` 或 `place_id` 时此字段必填。"),
 "place_id": f("Google Maps Place ID of the business entity. Required when neither `keyword` nor `cid` is supplied.",
              "商户实体在 Google 地图中的 Place ID。未提供 `keyword` 或 `cid` 时此字段必填。"),
 "priority": f("Task execution priority: `1` for normal priority, `2` for high priority (charged at a higher rate for faster handling).",
              "任务执行优先级：`1` 为普通优先级，`2` 为高优先级（按更高费率计费以加快处理）。"),
 "location_name": f("Full location name (e.g. `London,England,United Kingdom`) setting the geographic context. Supply this or `location_code`/`location_coordinate`; valid values come from the matching Locations endpoint.",
              "完整地区名称（如 `London,England,United Kingdom`），用于设定地理范围。需与 `location_code`/`location_coordinate` 择一提供；可用取值来自对应的 Locations 接口。"),
 "location_code": f("Numeric location code setting the geographic context. Supply this or `location_name`/`location_coordinate`; valid values come from the matching Locations endpoint.",
              "数字地区编码，用于设定地理范围。需与 `location_name`/`location_coordinate` 择一提供；可用取值来自对应的 Locations 接口。"),
 "location_coordinate": f("GPS coordinates in `latitude,longitude` (optionally with a radius) setting the geographic context. Supply this or `location_name`/`location_code`.",
              "GPS 坐标，格式 `latitude,longitude`（可附半径），用于设定地理范围。需与 `location_name`/`location_code` 择一提供。"),
 "language_name": f("Full language name (e.g. `English`) for the search. Supply this or `language_code`; valid values come from the matching Languages endpoint.",
              "搜索所用语言的完整名称（如 `English`）。需与 `language_code` 择一提供；可用取值来自对应的 Languages 接口。"),
 "language_code": f("Language code (e.g. `en`) for the search. Supply this or `language_name`; valid values come from the matching Languages endpoint.",
              "搜索所用的语言代码（如 `en`）。需与 `language_name` 择一提供；可用取值来自对应的 Languages 接口。"),
 "depth": f("Parsing depth: number of reviews to collect from the SERP. Set it in multiples of 20, since results are processed twenty at a time.",
              "解析深度：从 SERP 采集的评论数量。建议设为 20 的倍数，因系统每批处理 20 条。"),
 "tag": f("Your own task label (up to 255 characters), echoed back in the response `data` so you can correlate results with requests.",
              "你自定义的任务标签（最多 255 个字符），会在响应 `data` 中回显，便于将结果与请求对应。"),
 "postback_url": f("URL to which finished task results are POSTed (gzip-compressed). Use `$id`/`$tag` placeholders to have them substituted automatically.",
              "任务完成后用于 POST 推送结果（gzip 压缩）的回调 URL。可用 `$id`/`$tag` 占位符自动替换。"),
 "pingback_url": f("URL pinged via GET when the task completes, signalling that results are ready to collect. Supports `$id`/`$tag` placeholders.",
              "任务完成时通过 GET 触达的通知 URL，用于提示结果已就绪。支持 `$id`/`$tag` 占位符。"),
 "postback_data": f("Datatype pushed to your `postback_url`; required when `postback_url` is set. Possible values: `advanced`, `html`.",
              "推送至 `postback_url` 的数据类型；设置了 `postback_url` 时必填。取值：`advanced`、`html`。"),
 # business listings search
 "categories": f("Business categories used to filter the listings search; omit it to return all listings found in the location.",
              "用于筛选商户列表搜索的商户分类；留空则返回该地区内找到的全部商户。"),
 "description": f("Business description to match (up to 200 characters); restricts results to listings whose description matches.",
              "用于匹配的商户描述（最多 200 个字符）；将结果限定为描述匹配的商户。"),
 "title": f("Business name to match (up to 200 characters); restricts results to listings whose name matches.",
              "用于匹配的商户名称（最多 200 个字符）；将结果限定为名称匹配的商户。"),
 "is_claimed": f("Filter by owner-verification status: `true` returns only businesses verified by their owner on Google Maps.",
              "按所有者认证状态筛选：`true` 仅返回已被所有者在 Google 地图上认证的商户。"),
 "filters": f("Array of filtering conditions (up to 8) combined with `and`/`or` logical operators to narrow the listings search.",
              "筛选条件数组（最多 8 条），以 `and`/`or` 逻辑运算符组合，用于收窄列表搜索结果。"),
 "order_by": f("Sorting rules for the results, using the same fields as `filters` with direction `asc` or `desc`.",
              "结果排序规则，使用与 `filters` 相同的字段，方向为 `asc` 或 `desc`。"),
 "limit": f("Maximum number of businesses to return. Default `100`, maximum `1000`.",
              "返回商户的最大数量。默认 `100`，最大 `1000`。"),
 "offset": f("Number of leading businesses to skip in the results array. Default `0`.",
              "在结果数组中跳过的前导商户数量。默认 `0`。"),
 "offset_token": f("Pagination token returned in a prior response; pass it to fetch the next batch and avoid timeouts on very large result sets.",
              "上一次响应中返回的分页令牌；传入以取回下一批结果，避免超大结果集超时。"),
 # hotel info / searches
 "hotel_identifier": f("Unique Google identifier of a hotel entity (required). Obtain it from the advanced Google SERP API or from Hotel Searches results.",
              "酒店实体的 Google 唯一标识（必填）。可从高级 Google SERP API 或 Hotel Searches 结果中获取。"),
 "check_in": f("Check-in date in `yyyy-mm-dd`; must not be earlier than today. Defaults to tomorrow when omitted.",
              "入住日期，格式 `yyyy-mm-dd`；不得早于今天。不填默认为明天。"),
 "check_out": f("Check-out date in `yyyy-mm-dd`; must be later than `check_in`. Defaults to two days from now when omitted.",
              "退房日期，格式 `yyyy-mm-dd`；须晚于 `check_in`。不填默认为后天。"),
 "currency": f("Currency for the returned prices, e.g. `USD`.",
              "返回价格所用的货币，如 `USD`。"),
 "adults": f("Number of adult guests. Defaults to two adults when omitted.",
              "成人入住人数。不填默认为两名成人。"),
 "children": f("Children to include, given as an array of their ages (e.g. `[14]`). Defaults to no children when omitted.",
              "随行儿童，以年龄数组表示（如 `[14]`）。不填则不计入儿童。"),
 "load_prices_by_dates": f("Set to `true` to include the `prices_by_dates` array with stay prices split by date in the response.",
              "设为 `true` 时，响应中将包含按日期拆分住宿价格的 `prices_by_dates` 数组。"),
 "prices_start_date": f("Start date (`yyyy-mm-dd`) for date-split prices; requires `load_prices_by_dates=true`. Defaults to `check_in`.",
              "按日期拆分价格的起始日期（`yyyy-mm-dd`）；需 `load_prices_by_dates=true`。默认取 `check_in`。"),
 "prices_end_date": f("End date (`yyyy-mm-dd`) for date-split prices; requires `load_prices_by_dates=true`. Defaults to one month of prices.",
              "按日期拆分价格的结束日期（`yyyy-mm-dd`）；需 `load_prices_by_dates=true`。默认返回一个月的价格。"),
 "prices_date_range": f("Predefined period for date-split prices (alternative to start/end dates); requires `load_prices_by_dates=true`.",
              "按日期拆分价格的预设区间（与起止日期二选一）；需 `load_prices_by_dates=true`。"),
 "stars": f("Filter by hotel class, as an array of star values, e.g. `[3,4,5]`.",
              "按酒店星级筛选，以星级数组表示，如 `[3,4,5]`。"),
 "min_rating": f("Minimum guest rating; returns only hotels rated above the given value, e.g. `2.5`.",
              "最低住客评分；仅返回评分高于该值的酒店，如 `2.5`。"),
 "sort_by": f("Sorting of hotel-search results; values include `relevance`, `lowest_price`, `highest_rating`. For reviews, sorts review order.",
              "酒店搜索结果的排序方式，取值如 `relevance`、`lowest_price`、`highest_rating`。用于评论时则决定评论排序。"),
 "min_price": f("Minimum price per night, expressed in the currency set by `currency`.",
              "每晚最低价格，币种由 `currency` 决定。"),
 "max_price": f("Maximum price per night, expressed in the currency set by `currency`.",
              "每晚最高价格，币种由 `currency` 决定。"),
 "free_cancellation": f("Set to `true` to return only hotels offering free cancellation. Default `false`.",
              "设为 `true` 仅返回提供免费取消的酒店。默认 `false`。"),
 "is_vacation_rentals": f("Set to `true` to search vacation rentals instead of hotels. Default `false`.",
              "设为 `true` 时搜索度假租赁而非酒店。默认 `false`。"),
 "amenities": f("Filter by hotel amenities, given as an array of amenity codes (e.g. `[\"free_parking\",\"pets_allowed\"]`).",
              "按酒店便利设施筛选，以设施编码数组表示（如 `[\"free_parking\",\"pets_allowed\"]`）。"),
 # pinterest
 "targets": f("Target page URLs (required), each an absolute URL including the scheme; up to 10 targets per request.",
              "目标页面 URL（必填），每个须为含协议头的绝对 URL；每次请求最多 10 个目标。"),
}

# id path parameter (task_get endpoints).
PARAM_ID = f("UUID of the task whose results you want to fetch, as returned in `tasks.id` when the task was created.",
             "要拉取结果的任务 UUID，即创建任务时在 `tasks.id` 返回的标识。")

# ---------------------------------------------------------------------------
# Operation-level docs (heading_zh / desc_en / description_zh), authored per op.
# ---------------------------------------------------------------------------
OPERATIONS = {
 "post_dataforseo_business_data_business_listings_search_live": (
   "实时搜索商户列表",
   "Synchronously search DataForSEO's business-listings database by category, name, description, location and custom filters, returning matching local businesses with their profiles, ratings and contact details in a single request.",
   "在单次请求中，按分类、名称、描述、地区与自定义筛选条件同步检索 DataForSEO 商户列表库，返回匹配的本地商户及其资料、评分与联系信息。"),
 "post_dataforseo_business_data_google_extended_reviews_task_post": (
   "创建 Google 扩展评论任务",
   "Create an asynchronous task that collects an establishment's Google reviews, including reviews aggregated from third-party sites; poll the matching tasks_ready endpoint and then fetch results by task id.",
   "创建异步任务以采集某商户的 Google 评论（含聚合自第三方站点的评论）；随后轮询对应的 tasks_ready 接口，并按任务 id 取回结果。"),
 "post_dataforseo_business_data_google_hotel_info_live_advanced": (
   "实时获取 Google 酒店详情（advanced）",
   "Synchronously retrieve detailed Google hotel info for a given hotel identifier and stay dates, returning the hotel's description, amenities, location scores, ratings and pricing in a single request.",
   "针对给定酒店标识与入住日期，单次请求同步获取 Google 酒店详情，返回酒店介绍、便利设施、位置评分、评分与价格信息。"),
 "get_dataforseo_business_data_google_hotel_info_task_get_advanced_id": (
   "获取 Google 酒店详情任务结果（advanced）",
   "Fetch the advanced results of a previously created Google Hotel Info task by its id.",
   "按任务 id 拉取此前创建的 Google 酒店详情任务的 advanced 结果。"),
 "post_dataforseo_business_data_google_hotel_info_task_post": (
   "创建 Google 酒店详情任务",
   "Create an asynchronous Google Hotel Info task for a given hotel identifier and stay dates; collect the detailed result later via the matching task_get endpoint.",
   "针对给定酒店标识与入住日期创建异步 Google 酒店详情任务；稍后通过对应的 task_get 接口取回详细结果。"),
 "post_dataforseo_business_data_google_hotel_searches_live": (
   "实时搜索 Google 酒店",
   "Synchronously search Google hotels for a keyword and stay dates with optional price, rating, star and amenity filters, returning matched hotel listings with pricing, location and rating data in a single request.",
   "针对关键词与入住日期同步搜索 Google 酒店，支持价格、评分、星级与设施等筛选，单次请求返回匹配的酒店列表及其价格、位置与评分数据。"),
 "post_dataforseo_business_data_google_hotel_searches_task_post": (
   "创建 Google 酒店搜索任务",
   "Create an asynchronous Google Hotel Searches task for a keyword and stay dates with optional filters; collect the results later via the matching task_get endpoint.",
   "针对关键词与入住日期创建异步 Google 酒店搜索任务，支持可选筛选；稍后通过对应的 task_get 接口取回结果。"),
 "post_dataforseo_business_data_google_my_business_info_live": (
   "实时获取 Google 商家资料",
   "Synchronously retrieve the Google My Business profile for a local establishment, returning its categories, contact details, working hours, attributes, ratings and available interactions in a single request.",
   "同步获取某本地商户的 Google 商家（My Business）资料，单次请求返回其分类、联系方式、营业时间、属性、评分与可用互动入口。"),
 "post_dataforseo_business_data_google_my_business_info_task_post": (
   "创建 Google 商家资料任务",
   "Create an asynchronous Google My Business Info task for a local establishment; collect the profile result later via the matching task_get endpoint.",
   "为某本地商户创建异步 Google 商家资料任务；稍后通过对应的 task_get 接口取回资料结果。"),
 "get_dataforseo_business_data_google_my_business_updates_task_get_id": (
   "获取 Google 商家动态任务结果",
   "Fetch the results of a previously created Google My Business Updates task by its id, returning the establishment's posted business updates.",
   "按任务 id 拉取此前创建的 Google 商家动态任务结果，返回该商户发布的商家动态。"),
 "get_dataforseo_business_data_google_my_business_updates_tasks_ready": (
   "获取 Google 商家动态已完成任务",
   "List Google My Business Updates tasks that have finished processing and are ready to be collected via the matching task_get endpoint.",
   "列出已处理完成、可通过对应 task_get 接口拉取的 Google 商家动态任务。"),
 "get_dataforseo_business_data_google_questions_and_answers_task_get_id": (
   "获取 Google 问答任务结果",
   "Fetch the results of a previously created Google Questions & Answers task by its id, returning the establishment's questions, their answers and questions still awaiting answers.",
   "按任务 id 拉取此前创建的 Google 问答任务结果，返回该商户的问题、对应回答及仍待回答的问题。"),
 "get_dataforseo_business_data_google_questions_and_answers_tasks_ready": (
   "获取 Google 问答已完成任务",
   "List Google Questions & Answers tasks that have finished processing and are ready to be collected.",
   "列出已处理完成、可供拉取的 Google 问答任务。"),
 "post_dataforseo_business_data_google_reviews_task_post": (
   "创建 Google 评论任务",
   "Create an asynchronous task that collects an establishment's Google reviews; poll the matching tasks_ready endpoint and then fetch results by task id.",
   "创建异步任务以采集某商户的 Google 评论；随后轮询对应的 tasks_ready 接口，并按任务 id 取回结果。"),
 "post_dataforseo_business_data_social_media_pinterest_live": (
   "实时获取 Pinterest 收藏数",
   "Synchronously retrieve the number of Pinterest saves (pins) made from one or more target page URLs via the Pinterest Save Button, in a single request.",
   "单次请求同步获取一个或多个目标页面 URL 通过 Pinterest 保存按钮产生的收藏（pin）数量。"),
 "get_dataforseo_business_data_tripadvisor_reviews_task_get_id": (
   "获取 Tripadvisor 评论任务结果",
   "Fetch the results of a previously created Tripadvisor Reviews task by its id, returning the establishment's collected reviews and ratings.",
   "按任务 id 拉取此前创建的 Tripadvisor 评论任务结果，返回该商户已采集的评论与评分。"),
 "get_dataforseo_business_data_tripadvisor_reviews_tasks_ready": (
   "获取 Tripadvisor 评论已完成任务",
   "List Tripadvisor Reviews tasks that have finished processing and are ready to be collected.",
   "列出已处理完成、可供拉取的 Tripadvisor 评论任务。"),
 "post_dataforseo_business_data_tripadvisor_search_task_post": (
   "创建 Tripadvisor 搜索任务",
   "Create an asynchronous Tripadvisor Search task for a keyword and location; collect the matched establishments later via the matching task_get endpoint.",
   "针对关键词与地区创建异步 Tripadvisor 搜索任务；稍后通过对应的 task_get 接口取回匹配的商户。"),
 "get_dataforseo_business_data_trustpilot_reviews_task_get_id": (
   "获取 Trustpilot 评论任务结果",
   "Fetch the results of a previously created Trustpilot Reviews task by its id, returning the business's collected reviews and ratings.",
   "按任务 id 拉取此前创建的 Trustpilot 评论任务结果，返回该商户已采集的评论与评分。"),
 "get_dataforseo_business_data_trustpilot_reviews_tasks_ready": (
   "获取 Trustpilot 评论已完成任务",
   "List Trustpilot Reviews tasks that have finished processing and are ready to be collected.",
   "列出已处理完成、可供拉取的 Trustpilot 评论任务。"),
 "post_dataforseo_business_data_trustpilot_search_task_post": (
   "创建 Trustpilot 搜索任务",
   "Create an asynchronous Trustpilot Search task for a keyword (domain); collect the matched businesses later via the matching task_get endpoint.",
   "针对关键词（域名）创建异步 Trustpilot 搜索任务；稍后通过对应的 task_get 接口取回匹配的商户。"),
}


# ---------------------------------------------------------------------------
# Mechanical assembly: read real literal keys per op, map onto authored entries.
# ---------------------------------------------------------------------------
def resolve_resp(key):
    """Full-key override first, then envelope/common/ready full-key, then leaf name."""
    for d in (FULL_OVERRIDE, ENVELOPE, RESULT_COMMON, TASKS_READY):
        if key in d:
            return d[key]
    leaf = key.split(".")[-1]
    return LEAF.get(leaf)


def main():
    spec = json.load(open(SPEC))
    operations = {}
    fields = {}
    missing = []
    n_ops = 0
    for path, ms in spec["paths"].items():
        for method, op in ms.items():
            if not isinstance(op, dict):
                continue
            opid = op.get("operationId") or f"{method.upper()} {path}"
            n_ops += 1
            # operation-level
            if opid not in OPERATIONS:
                missing.append(("OP", opid))
            else:
                h, en, zh = OPERATIONS[opid]
                operations[opid] = {"heading_zh": h, "desc_en": en, "description_zh": zh}
            fobj = {}
            # request body
            rb = op.get("requestBody")
            if rb:
                sch = deref(spec, rb.get("content", {}).get("application/json", {}).get("schema", {}))
                reqd = {}
                for k in sch.get("properties", {}).keys():
                    leaf = k.split(".")[-1]
                    src = REQUEST.get(k) or REQUEST.get(leaf)
                    if src is None:
                        missing.append(("REQ", opid, k))
                    else:
                        reqd[k] = src
                if reqd:
                    fobj["request"] = reqd
            # responses
            respmap = {}
            for code, rv in op.get("responses", {}).items():
                sch = deref(spec, rv.get("content", {}).get("application/json", {}).get("schema", {}))
                d = {}
                for k in sch.get("properties", {}).keys():
                    src = resolve_resp(k)
                    if src is None:
                        missing.append(("RESP", opid, code, k))
                    else:
                        d[k] = src
                if d:
                    respmap[code] = d
            if respmap:
                fobj["response"] = respmap
            # parameters
            pmap = {}
            for pp in (op.get("parameters") or []):
                if not isinstance(pp, dict) or pp.get("$ref"):
                    continue
                if pp.get("name") == "id":
                    pmap["id"] = PARAM_ID
            if pmap:
                fobj["parameters"] = pmap
            fields[opid] = fobj

    if missing:
        sys.stderr.write("UNCOVERED (%d):\n" % len(missing))
        for m in missing[:120]:
            sys.stderr.write("  " + " | ".join(map(str, m)) + "\n")
        sys.exit("ABORT: author missing entries before writing content.json")

    content = {"operations": operations, "fields": fields}
    json.dump(content, open(OUT, "w"), ensure_ascii=False, indent=2)
    nf = sum(len(b.get("request", {}))
             + sum(len(c) for c in b.get("response", {}).values())
             + len(b.get("parameters", {}))
             for b in fields.values())
    print("WROTE", OUT)
    print("ops=%d fields=%d" % (n_ops, nf))


if __name__ == "__main__":
    main()
