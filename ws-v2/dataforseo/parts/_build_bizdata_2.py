# -*- coding: utf-8 -*-
"""Assembler for bizdata_2.content.json.

NOT a description generator: every desc_en/title_zh string below is hand-authored
per distinct semantic field (DataForSEO business_data). This script only maps the
spec's literal flat property keys (per op) onto the authored dual-field entries and
emits the content.json envelope. Per-op overrides cover real semantic variations.
"""
import json

SPEC = "/home/mira/files/aisa-docs-voyager/ws-v2/dataforseo/slices/bizdata_2.json"
OUT = "/home/mira/files/aisa-docs-voyager/ws-v2/dataforseo/parts/bizdata_2.content.json"

spec = json.load(open(SPEC))
comps = spec.get("components", {}).get("schemas", {})


def deref(node):
    seen = 0
    while isinstance(node, dict) and "$ref" in node and seen < 20:
        seen += 1
        node = comps.get(node["$ref"].split("/")[-1], {})
    return node


def e(desc_en, title_zh, annotation=None):
    d = {"desc_en": desc_en, "title_zh": title_zh}
    if annotation:
        d["annotation"] = annotation
    return d


# ---- shared response envelope (version.* / tasks.*) ----------------------------
ENV = {
    "version": e("Top-level API metadata object describing this response, including the API version and the aggregated status, timing and cost of the request.",
                 "顶层 API 元数据对象，包含本次响应的 API 版本，以及整批请求的聚合状态、耗时与计费信息。"),
    "version.status_code": e("Overall status code for the whole request. Use it as the first signal of success or failure before reading the tasks array; the full code list is in the DataForSEO errors reference.",
                             "整个请求的总体状态码。读取 tasks 数组前应先用它判断请求整体成功或失败；完整状态码列表见 DataForSEO 错误码文档。"),
    "version.status_message": e("Human-readable message that accompanies the overall status code, e.g. `Ok` or an error explanation.",
                                "与总体状态码配套的可读说明信息，例如 `Ok` 或错误原因。"),
    "version.time": e("Wall-clock time the platform spent handling the whole request, in seconds.",
                      "平台处理整个请求所花费的时间，单位为秒。"),
    "version.cost": e("Total amount charged for all tasks in this response, in USD.",
                      "本次响应中所有任务的总计费金额，单位为美元（USD）。"),
    "version.tasks_count": e("Number of task objects contained in the `tasks` array.",
                             "`tasks` 数组中包含的任务对象数量。"),
    "version.tasks_error": e("Number of task objects in the `tasks` array that finished with an error; if greater than zero, inspect each task's own status code.",
                             "`tasks` 数组中以错误结束的任务数量；若大于 0，应逐个检查任务自身的状态码。"),
    "tasks": e("Array of task objects; each entry carries the per-task status plus its `result` payload.",
               "任务对象数组，每个元素携带单个任务的状态及其 `result` 结果数据。"),
    "tasks.id": e("Unique identifier of this task in UUID format. Reuse it to fetch results from the matching `task_get` endpoint within the task's retention window.",
                  "本任务在系统中的唯一标识，UUID 格式。可在任务保留期内用它向对应的 `task_get` 端点拉取结果。"),
    "tasks.status_code": e("Status code of this individual task (range 10000-60000). A value in the 20000 range means success; other ranges signal queued, in-progress or error states.",
                           "单个任务的状态码（范围 10000-60000）。20000 区间表示成功，其它区间表示排队、处理中或错误等状态。"),
    "tasks.status_message": e("Human-readable message describing the outcome of this task, paired with `tasks.status_code`.",
                              "描述该任务处理结果的可读信息，与 `tasks.status_code` 配套。"),
    "tasks.time": e("Wall-clock time spent processing this task, in seconds.",
                    "处理该任务所花费的时间，单位为秒。"),
    "tasks.cost": e("Amount charged for this individual task, in USD.",
                    "该单个任务的计费金额，单位为美元（USD）。"),
    "tasks.result_count": e("Number of elements in this task's `result` array.",
                            "该任务 `result` 数组中的元素数量。"),
    "tasks.path": e("URL path segments of the endpoint that produced this task, useful for tracing which call the result belongs to.",
                    "生成该任务的端点 URL 路径片段，便于追溯结果对应的调用。"),
    "tasks.data": e("Echo of the parameters you submitted for this task, returned so you can correlate the result with the original request.",
                    "回显你为该任务提交的参数，便于将结果与原始请求对应起来。"),
    "result": e("Array holding the actual payload of this task.",
                "承载该任务实际结果数据的数组。"),
}

# tasks_ready result.* block (shared across all *_tasks_ready ops)
READY = {
    "result.id": e("UUID of a completed task that is now ready to be collected; pass it to the matching `task_get` endpoint to download the results.",
                   "已完成、可供拉取的任务的 UUID；将其传给对应的 `task_get` 端点即可下载结果。"),
    "result.se": e("Search engine the completed task was set for.",
                   "该已完成任务所针对的搜索引擎。"),
    "result.se_type": e("Search engine type the completed task was set for.",
                        "该已完成任务所针对的搜索引擎类型。"),
    "result.date_posted": e("Timestamp (UTC) when the task was originally submitted.",
                            "任务最初提交的时间（UTC）。"),
    "result.tag": e("User-defined label that was attached to the task when it was created, echoed back for matching.",
                    "创建任务时附加的用户自定义标签，原样回显以便匹配。"),
    "result.endpoint": e("Relative endpoint URL to call for collecting this completed task's results.",
                         "用于拉取该已完成任务结果的相对端点 URL。"),
}

# common result-level header fields reused by several task_get ops
RES_COMMON = {
    "result.keyword": e("Keyword echoed from the POST request, with percent-encoding decoded (a `+` becomes a space).",
                        "从 POST 请求回显的关键词，已解码百分号转义（`+` 会被还原为空格）。"),
    "result.type": e("Search engine type echoed from the POST request.",
                     "从 POST 请求回显的搜索引擎类型。"),
    "result.se_domain": e("Search engine domain echoed from the POST request.",
                          "从 POST 请求回显的搜索引擎域名。"),
    "result.location_code": e("Location code echoed from the POST request.",
                              "从 POST 请求回显的地区代码。"),
    "result.language_code": e("Language code echoed from the POST request.",
                              "从 POST 请求回显的语言代码。"),
    "result.check_url": e("Direct URL to the search engine results page, so you can verify the data against the live SERP.",
                          "指向搜索引擎结果页的直达 URL，可用于将数据与实时 SERP 核对。"),
    "result.datetime": e("UTC timestamp when the result was collected, formatted `yyyy-mm-dd hh-mm-ss +00:00`.",
                         "结果采集的时间（UTC），格式为 `yyyy-mm-dd hh-mm-ss +00:00`。"),
    "result.items_count": e("Number of elements returned in the `items` array; raise the `depth` parameter at task creation to get more.",
                            "`items` 数组中返回的元素数量；在创建任务时调大 `depth` 参数可获取更多。"),
}

# rating quartet reused widely
RATING = {
    "rating": e("Aggregated rating of the entity, as shown in the SERP.",
                "该实体的综合评分，与 SERP 中展示的一致。"),
    "rating_type": e("Scale used to express the rating; the business meaning is: `Max5` rated out of 5, `Percents` expressed as a percentage, `CustomMax` rated against a custom maximum.",
                     "评分所采用的标度，业务含义为：`Max5` 表示满分 5 分制，`Percents` 表示百分比制，`CustomMax` 表示自定义满分制。"),
    "value": e("Average rating value computed from all reviews.",
               "基于全部评论计算出的平均评分值。"),
    "votes_count": e("Number of votes (ratings) the rating is based on.",
                     "该评分所依据的投票（打分）数量。"),
    "rating_max": e("Maximum possible value for the given `rating_type` (for example 5 when the type is `Max5`).",
                    "对应 `rating_type` 的最大可能取值（例如类型为 `Max5` 时为 5）。"),
}

# Google reviews/extended_reviews shared result.* and items.* blocks
GR_RESULT = dict(RES_COMMON)
GR_RESULT.update({
    "result.title": e("Name of the local establishment that the 'reviews' SERP element collects reviews for.",
                      "SERP 中 'reviews' 元素所采集评论对应的本地商家名称。"),
    "result.sub_title": e("Supplementary information (such as the address) shown beneath the title of the 'reviews' element.",
                          "'reviews' 元素标题下方展示的补充信息（如地址）。"),
    "result.rating": RATING["rating"],
    "result.rating_type": RATING["rating_type"],
    "result.value": RATING["value"],
    "result.votes_count": RATING["votes_count"],
    "result.rating_max": RATING["rating_max"],
    "result.feature_id": e("Unique identifier of the 'reviews' SERP element (feature id).",
                           "SERP 中 'reviews' 元素的唯一标识（feature id）。"),
    "result.place_id": e("Google-assigned unique identifier of the business location (place id).",
                         "Google 为该商家地点分配的唯一标识（place id）。"),
    "result.cid": e("Google-defined client id (cid), a unique id of the local establishment.",
                    "Google 定义的客户端 id（cid），本地商家的唯一标识。"),
    "result.reviews_count": e("Total number of reviews available for the establishment.",
                              "该商家可获取的评论总数。"),
})

GR_ITEMS = {
    "items": e("Review entries collected for the establishment; raise `depth` at task creation to retrieve more.",
               "为该商家采集到的评论条目；创建任务时调大 `depth` 可获取更多。"),
    "items.type": e("Element type marker of the review entry.",
                    "评论条目的元素类型标记。"),
    "items.rank_group": e("Position of this entry within the group of elements sharing the same `type`.",
                          "该条目在相同 `type` 元素分组内的位置。"),
    "items.rank_absolute": e("Absolute position of this review among all listed reviews.",
                             "该评论在全部已列出评论中的绝对位置。"),
    "items.position": e("Alignment of the review within the SERP layout.",
                        "评论在 SERP 版式中的对齐位置。"),
    "items.xpath": e("XPath locating this review element within the parsed page.",
                     "在解析页面中定位该评论元素的 XPath。"),
    "items.review_text": e("Body text of the review (auto-translated when applicable).",
                           "评论正文内容（在适用时为自动翻译后的文本）。"),
    "items.original_review_text": e("Review body in its original language, with no auto-translation applied.",
                                    "评论正文的原始语言版本，未做自动翻译。"),
    "items.time_ago": e("Relative publication time of the review in 'time ago' wording.",
                        "评论发布时间的相对表述（'time ago' 格式）。"),
    "items.timestamp": e("Absolute publication time of the review in UTC, `yyyy-mm-dd hh-mm-ss +00:00`.",
                         "评论发布的绝对时间（UTC），格式 `yyyy-mm-dd hh-mm-ss +00:00`。"),
    "items.rating": e("Rating score given by the reviewer.",
                      "该评论作者给出的评分。"),
    "items.rating_type": RATING["rating_type"],
    "items.value": e("Numeric value of the reviewer's rating.",
                     "该评论作者评分的数值。"),
    "items.votes_count": e("Number of helpfulness votes this review received.",
                           "该评论获得的有用性投票数。"),
    "items.rating_max": RATING["rating_max"],
    "items.reviews_count": e("Total number of reviews the reviewer has submitted overall.",
                             "该评论作者累计提交的评论总数。"),
    "items.photos_count": e("Total number of photos the reviewer has submitted overall.",
                            "该评论作者累计提交的照片总数。"),
    "items.local_guide": e("Whether the reviewer holds Google 'Local Guide' status.",
                           "该评论作者是否拥有 Google '本地向导'（Local Guide）身份。"),
    "items.profile_name": e("Display name of the reviewer's profile.",
                            "评论作者的资料显示名称。"),
    "items.profile_url": e("URL of the reviewer's profile.",
                           "评论作者的资料页 URL。"),
    "items.review_url": e("URL pointing directly to this review.",
                          "直接指向该评论的 URL。"),
    "items.profile_image_url": e("URL of the reviewer's profile image.",
                                 "评论作者的头像图片 URL。"),
    "items.owner_answer": e("Owner's reply text to the review (auto-translated when applicable).",
                            "商家所有者对该评论的回复文本（适用时为自动翻译）。"),
    "items.original_owner_answer": e("Owner's reply in its original language, with no auto-translation applied.",
                                     "商家所有者回复的原始语言版本，未做自动翻译。"),
    "items.owner_time_ago": e("Relative time of the owner's reply in 'time ago' wording.",
                              "商家回复时间的相对表述（'time ago' 格式）。"),
    "items.owner_timestamp": e("Absolute time of the owner's reply in UTC, `yyyy-mm-dd hh-mm-ss +00:00`.",
                               "商家回复的绝对时间（UTC），格式 `yyyy-mm-dd hh-mm-ss +00:00`。"),
    "items.review_id": e("Unique identifier of the review on Google.",
                         "该评论在 Google 上的唯一标识。"),
    "items.images": e("Images attached to the review by the reviewer.",
                      "评论作者随评论附上的图片。"),
    "items.alt": e("Alt text of the review image.",
                   "评论图片的 alt 替代文本。"),
    "items.image_url": e("URL of an image featured in the review.",
                         "评论中所附图片的 URL。"),
    "items.review_highlights": e("Highlighted review criteria together with their assessments.",
                                 "评论中被高亮的评价维度及其评价结论。"),
    "items.feature": e("Reviewed feature or aspect.",
                       "被评价的特性或维度。"),
    "items.assessment": e("Assessment given for the reviewed feature.",
                          "针对被评价特性给出的评价结论。"),
}

# build per-op fields ------------------------------------------------------------
operations = {}
fields = {}


def resp_keys(opid):
    for p, ms in spec["paths"].items():
        for m, op in ms.items():
            if op.get("operationId") == opid:
                out = {}
                for code, rv in op.get("responses", {}).items():
                    sch = deref(rv.get("content", {}).get("application/json", {}).get("schema", {}))
                    out[code] = list(sch.get("properties", {}).keys())
                return out
    return {}


def req_keys(opid):
    for p, ms in spec["paths"].items():
        for m, op in ms.items():
            if op.get("operationId") == opid:
                rb = op.get("requestBody")
                if not rb:
                    return []
                sch = deref(rb.get("content", {}).get("application/json", {}).get("schema", {}))
                return list(sch.get("properties", {}).keys())
    return []


# id path param (shared)
PARAM_ID_30 = e("UUID of the task whose results you want to fetch. The task remains retrievable for 30 days after creation.",
                "要拉取结果的任务 UUID。任务自创建起 30 天内可随时取回结果。")
PARAM_ID_7 = e("UUID of the task whose results you want to fetch. The task remains retrievable for 7 days after creation.",
               "要拉取结果的任务 UUID。任务自创建起 7 天内可随时取回结果。")

# shared request param dictionary (live/task_post bodies)
REQ_D = {
    "priority": e("Execution priority of the task: `1` runs at normal priority, `2` runs at high priority for faster turnaround at an extra charge.",
                  "任务执行优先级：`1` 为普通优先级，`2` 为高优先级，可更快返回但会额外计费。"),
    "location_name": e("Full location name (e.g. `London,England,United Kingdom`) that sets the geographic context of the search. Provide this or `location_code`/`location_coordinate`; the available list comes from the corresponding `/locations` endpoint.",
                       "完整地区名称（如 `London,England,United Kingdom`），用于设定搜索的地理范围。需在此与 `location_code`/`location_coordinate` 中择一提供；可用列表来自对应的 `/locations` 端点。"),
    "location_code": e("Numeric location code that sets the geographic context of the search. Provide this or `location_name`/`location_coordinate`; the available list comes from the corresponding `/locations` endpoint.",
                       "数字地区代码，用于设定搜索的地理范围。需在此与 `location_name`/`location_coordinate` 中择一提供；可用列表来自对应的 `/locations` 端点。"),
    "location_coordinate": e("GPS coordinates that set the geographic context of the search, in `latitude,longitude` (some endpoints also accept a radius). Provide this or `location_name`/`location_code`.",
                             "用于设定搜索地理范围的 GPS 坐标，格式为 `latitude,longitude`（部分端点还接受半径）。需与 `location_name`/`location_code` 择一提供。"),
    "language_name": e("Full language name (e.g. `English`) for the search. Provide this or `language_code`; the available list comes from the corresponding `/languages` endpoint.",
                       "搜索所用语言的完整名称（如 `English`）。需与 `language_code` 择一提供；可用列表来自对应的 `/languages` 端点。"),
    "language_code": e("Language code (e.g. `en`) for the search. Provide this or `language_name`; the available list comes from the corresponding `/languages` endpoint.",
                       "搜索所用的语言代码（如 `en`）。需与 `language_name` 择一提供；可用列表来自对应的 `/languages` 端点。"),
    "tag": e("Your own label for the task (up to 255 characters). It is echoed back in the response `data` so you can match results to requests.",
             "你为任务自定义的标签（最多 255 个字符）。会在响应的 `data` 中回显，便于将结果与请求匹配。"),
    "postback_url": e("URL to which the completed task results are pushed via POST (gzip-compressed). Use the `$id`/`$tag` placeholders in the URL to have them substituted automatically.",
                      "任务完成后用于以 POST 推送结果（gzip 压缩）的回调 URL。可在 URL 中使用 `$id`/`$tag` 占位符，系统会自动替换为实际值。"),
    "pingback_url": e("URL that is pinged via GET when the task completes, signalling that results are ready to collect. Supports the `$id`/`$tag` placeholders.",
                      "任务完成时通过 GET 触达的通知 URL，用于提示结果已就绪。支持 `$id`/`$tag` 占位符。"),
}


def build(opid, heading_zh, desc_en, description_zh, has_id_param=None,
          req_over=None, resp_over=None, base_resp=None):
    operations[opid] = {"heading_zh": heading_zh, "desc_en": desc_en,
                        "description_zh": description_zh}
    f = {}
    rk = req_keys(opid)
    if rk:
        reqd = {}
        for k in rk:
            src = (req_over or {}).get(k) or REQ_D.get(k)
            if src is None:
                raise SystemExit("MISSING REQ AUTHOR for %s.%s" % (opid, k))
            reqd[k] = src
        f["request"] = reqd
    # responses
    respmap = {}
    for code, keys in resp_keys(opid).items():
        base = dict(ENV)
        if base_resp:
            base.update(base_resp)
        if resp_over:
            base.update(resp_over)
        d = {}
        for k in keys:
            src = base.get(k)
            if src is None:
                raise SystemExit("MISSING RESP AUTHOR for %s [%s] %s" % (opid, code, k))
            d[k] = src
        respmap[code] = d
    f["response"] = respmap
    if has_id_param:
        f["parameters"] = {"id": has_id_param}
    fields[opid] = f


# ============================ per-operation builds ============================

# 1. Google extended reviews task_get
ER_RES = dict(GR_RESULT); ER_ITEMS = dict(GR_ITEMS)
ER_ITEMS.update({
    "items.source": e("Information about the external source the review was posted on.",
                      "该评论所发布外部来源的相关信息。"),
    "items.title": e("Name of the source site where the review was posted.",
                     "该评论所发布来源站点的名称。"),
    "items.image": e("Featured image of the review source.",
                     "评论来源的特色图片。"),
    "items.domain": e("Domain of the source site where the review was posted.",
                      "该评论所发布来源站点的域名。"),
})
build("get_dataforseo_business_data_google_extended_reviews_task_get_id",
      "获取 Google 扩展评论结果 get_dataforseo_business_data_google_extended_reviews_task_get_id",
      "Fetch the results of a previously created Google Extended Reviews task by its id, returning the establishment's aggregated rating and the collected review entries, including reviews sourced from third-party sites.",
      "按任务 id 拉取此前创建的 Google 扩展评论任务结果，返回商家的综合评分及采集到的评论条目，并包含来自第三方站点的评论。",
      has_id_param=PARAM_ID_30, resp_over={**ER_RES, **ER_ITEMS})

# 2. Google extended reviews tasks_ready
build("get_dataforseo_business_data_google_extended_reviews_tasks_ready",
      "获取 Google 扩展评论已完成任务 get_dataforseo_business_data_google_extended_reviews_tasks_ready",
      "List Google Extended Reviews tasks that have finished processing and are ready to be collected via the matching task_get endpoint.",
      "列出已处理完成、可通过对应 task_get 端点拉取的 Google 扩展评论任务。",
      resp_over=READY)

# 3. Google hotel info live html
HI_RES = dict(RES_COMMON)
HI_RES.update({
    "result.keyword": e("Hotel identifier echoed for this result, formatted `hotel_id:$`.",
                        "本结果回显的酒店标识，格式为 `hotel_id:$`。"),
    "result.type": e("Result type, here `hotel_info`.",
                     "结果类型，此处为 `hotel_info`。"),
    "result.items_count": e("Number of HTML page elements returned in the `items` array.",
                            "`items` 数组中返回的 HTML 页面元素数量。"),
})
HI_ITEMS = {
    "items": e("Raw HTML pages captured for the hotel info result.",
               "为该酒店信息结果抓取到的原始 HTML 页面。"),
    "items.page": e("Sequential number of the returned HTML page.",
                    "返回 HTML 页面的序号。"),
    "items.date": e("UTC timestamp when the HTML page was scanned, `yyyy-mm-dd hh-mm-ss +00:00`.",
                    "该 HTML 页面被抓取的时间（UTC），格式 `yyyy-mm-dd hh-mm-ss +00:00`。"),
    "items.html": e("Full HTML markup of the captured page.",
                    "抓取页面的完整 HTML 源码。"),
}
HI_REQ = {
    "hotel_identifier": e("Unique identifier of a hotel entity in Google search. Obtain it from the Google SERP API `hotels` element or from the Hotel Searches endpoint.",
                          "Google 搜索中酒店实体的唯一标识。可从 Google SERP API 的 `hotels` 元素或 Hotel Searches 端点获取。"),
    "check_in": e("Check-in date in `yyyy-mm-dd`; if omitted, tomorrow's date is used.",
                  "入住日期，格式 `yyyy-mm-dd`；不填则默认使用明天的日期。"),
    "check_out": e("Check-out date in `yyyy-mm-dd`; if omitted, two days from now is used.",
                   "退房日期，格式 `yyyy-mm-dd`；不填则默认使用后天的日期。"),
    "currency": e("Currency for the returned prices, e.g. `USD`.",
                  "返回价格所用的货币，例如 `USD`。"),
    "adults": e("Number of adult guests; if omitted, two adults are assumed.",
                "成人入住人数；不填则默认按两名成人计算。"),
    "children": e("Children to include, as an array of their ages (e.g. `[13,8]`); if omitted, no children are included.",
                  "随行儿童，以年龄数组表示（如 `[13,8]`）；不填则不计入儿童。"),
}
build("post_dataforseo_business_data_google_hotel_info_live_html",
      "实时获取 Google 酒店信息 HTML post_dataforseo_business_data_google_hotel_info_live_html",
      "Synchronously retrieve Google hotel info for a given hotel identifier and stay dates, returning the captured result as raw HTML pages in a single request.",
      "针对给定酒店标识与入住日期，同步获取 Google 酒店信息，并在单次请求中以原始 HTML 页面形式返回采集结果。",
      req_over=HI_REQ, resp_over={**HI_RES, **HI_ITEMS})

# 4. Google hotel info task_get html
HI_RES2 = dict(RES_COMMON)
HI_RES2.update({
    "result.hotel_identifier": e("Hotel identifier echoed from the POST request that created the task.",
                                 "从创建任务的 POST 请求回显的酒店标识。"),
    "result.items_count": e("Number of HTML page elements returned in the `items` array.",
                            "`items` 数组中返回的 HTML 页面元素数量。"),
})
build("get_dataforseo_business_data_google_hotel_info_task_get_html_id",
      "获取 Google 酒店信息 HTML 结果 get_dataforseo_business_data_google_hotel_info_task_get_html_id",
      "Fetch the HTML results of a previously created advanced Google Hotel Info task by its id.",
      "按任务 id 拉取此前创建的高级 Google 酒店信息任务的 HTML 结果。",
      has_id_param=PARAM_ID_7,
      resp_over={**HI_RES2, **HI_ITEMS,
                 "version.result_count": e("Number of task objects contained in the `tasks` array.",
                                           "`tasks` 数组中包含的任务对象数量。")})

# 5. Google hotel info tasks_ready
build("get_dataforseo_business_data_google_hotel_info_tasks_ready",
      "获取 Google 酒店信息已完成任务 get_dataforseo_business_data_google_hotel_info_tasks_ready",
      "List Google Hotel Info tasks that have finished processing and are ready to be collected.",
      "列出已处理完成、可供拉取的 Google 酒店信息任务。",
      resp_over=READY)

# 6. Google hotel searches task_get
HS_RES = dict(RES_COMMON)
HS_RES.update({
    "result.keyword": e("Keyword echoed from the POST request (percent-encoding decoded); the location name is automatically appended to improve accuracy.",
                        "从 POST 请求回显的关键词（已解码百分号转义）；系统会自动追加地区名以提高准确度。"),
    "result.items_count": e("Number of items in the `items` array.",
                            "`items` 数组中的元素数量。"),
})
HS_ITEMS = {
    "items": e("Hotel search listing entries; possible item type: `hotel_search_item`.",
               "酒店搜索列表条目；可能的元素类型为 `hotel_search_item`。"),
    "items.type": e("Element type marker, here `hotel_search_item`.",
                    "元素类型标记，此处为 `hotel_search_item`。"),
    "items.hotel_identifier": e("Unique identifier of the hotel entity in Google search; reuse it with the Hotel Info endpoint.",
                                "Google 搜索中该酒店实体的唯一标识；可配合 Hotel Info 端点使用。"),
    "items.title": e("Hotel name.", "酒店名称。"),
    "items.stars": e("Hotel class rating, ranging from 1 to 5 stars.",
                     "酒店星级评定，范围 1 至 5 星。"),
    "items.is_paid": e("Whether the listing is a paid ad (`true`) or an organic hotel listing (`false`).",
                       "该条目是付费广告（`true`）还是自然酒店列表（`false`）。"),
    "items.location": e("GPS coordinates of the hotel's location.",
                        "酒店所在位置的 GPS 坐标。"),
    "items.latitude": e("Latitude of the hotel on Google Maps.",
                        "酒店在 Google 地图上的纬度。"),
    "items.longitude": e("Longitude of the hotel on Google Maps.",
                         "酒店在 Google 地图上的经度。"),
    "items.reviews": e("Hotel review and rating information.",
                       "酒店的评论与评分信息。"),
    "items.value": e("Average rating based on all reviews.",
                     "基于全部评论的平均评分。"),
    "items.votes_count": e("Number of votes the rating is based on.",
                           "该评分所依据的投票数。"),
    "items.mentions": e("Hotel mentions. This field is always `null` here and exists only for interoperability with the Hotel Info endpoint.",
                        "酒店提及信息。此处该字段恒为 `null`，仅为与 Hotel Info 端点保持结构互通而存在。"),
    "items.rating_distribution": e("Rating distribution by votes. This field is always `null` here and exists only for interoperability with the Hotel Info endpoint.",
                                   "按投票统计的评分分布。此处该字段恒为 `null`，仅为与 Hotel Info 端点保持结构互通而存在。"),
    "items.other_sites_reviews": e("Reviews on third-party sites. This field is always `null` here and exists only for interoperability with the Hotel Info endpoint.",
                                   "第三方站点上的评论。此处该字段恒为 `null`，仅为与 Hotel Info 端点保持结构互通而存在。"),
    "items.overview_images": e("Featured overview images of the hotel.",
                               "酒店的概览特色图片。"),
    "items.prices": e("Hotel pricing block.", "酒店价格信息块。"),
    "items.price": e("Price per night.", "每晚价格。"),
    "items.price_without_discount": e("Full price per night before any discount.",
                                      "未应用折扣前的每晚原价。"),
    "items.currency": e("Currency of the price; defaults to `USD` unless otherwise set in the POST request.",
                        "价格所用货币；除非在 POST 请求中另行指定，否则默认为 `USD`。"),
    "items.discount_text": e("Text describing the discount applied.",
                             "描述所应用折扣的文本。"),
    "items.check_in": e("Check-in date and time in UTC, `yyyy-mm-dd hh-mm-ss +00:00`.",
                        "入住日期与时间（UTC），格式 `yyyy-mm-dd hh-mm-ss +00:00`。"),
    "items.check_out": e("Check-out date and time in UTC, `yyyy-mm-dd hh-mm-ss +00:00`.",
                         "退房日期与时间（UTC），格式 `yyyy-mm-dd hh-mm-ss +00:00`。"),
    "items.visitors": e("Number of hotel visitors associated with this price.",
                        "与该价格关联的酒店入住人数。"),
    "items.items": e("Nested items array. This field is always `null` here and exists only for interoperability with the Hotel Info endpoint.",
                     "嵌套的 items 数组。此处该字段恒为 `null`，仅为与 Hotel Info 端点保持结构互通而存在。"),
}
build("get_dataforseo_business_data_google_hotel_searches_task_get_id",
      "获取 Google 酒店搜索结果 get_dataforseo_business_data_google_hotel_searches_task_get_id",
      "Fetch the results of a previously created Google Hotel Searches task by its id, returning matched hotel listings with pricing, location and rating data.",
      "按任务 id 拉取此前创建的 Google 酒店搜索任务结果，返回匹配的酒店列表及其价格、位置与评分数据。",
      has_id_param=PARAM_ID_30, resp_over={**HS_RES, **HS_ITEMS})

# 7. hotel searches tasks_ready
build("get_dataforseo_business_data_google_hotel_searches_tasks_ready",
      "获取 Google 酒店搜索已完成任务 get_dataforseo_business_data_google_hotel_searches_tasks_ready",
      "List Google Hotel Searches tasks that have finished processing and are ready to be collected.",
      "列出已处理完成、可供拉取的 Google 酒店搜索任务。",
      resp_over=READY)


# 8. Google my business info task_get
MBI_RES = {
    "result.keyword": e("Keyword echoed from the POST request (percent-encoding decoded); if you passed a `cid` in the keyword field, it is returned here as `cid:...`.",
                        "从 POST 请求回显的关键词（已解码百分号转义）；若你在关键词字段中传入了 `cid`，此处会以 `cid:...` 形式返回。"),
    "result.se_domain": e("Search engine domain echoed from the POST request.",
                          "从 POST 请求回显的搜索引擎域名。"),
    "result.location_code": RES_COMMON["result.location_code"],
    "result.language_code": RES_COMMON["result.language_code"],
    "result.check_url": RES_COMMON["result.check_url"],
    "result.datetime": RES_COMMON["result.datetime"],
    "result.item_types": e("Item types present in the `items` array; possible value: `google_business_info`.",
                           "`items` 数组中出现的元素类型；可能取值为 `google_business_info`。"),
    "result.items_count": e("Number of items in the `items` array.",
                            "`items` 数组中的元素数量。"),
}
MBI_ITEMS = {
    "items": e("Google My Business info entries; possible item type: `google_business_info`.",
               "Google 商家信息条目；可能的元素类型为 `google_business_info`。"),
    "items.type": e("Element type marker, here `google_business_info`.", "元素类型标记，此处为 `google_business_info`。"),
    "items.rank_group": GR_ITEMS["items.rank_group"],
    "items.rank_absolute": e("Absolute rank among all the elements.", "在全部元素中的绝对排名。"),
    "items.position": e("Alignment of the element within the SERP.", "元素在 SERP 中的对齐位置。"),
    "items.title": e("Business name shown in the SERP element.", "SERP 元素中展示的商家名称。"),
    "items.original_title": e("Business title in its original language, not translated by Google.", "商家标题的原始语言版本，未经 Google 翻译。"),
    "items.description": e("Description of the business entity shown in the SERP.", "SERP 中展示的商家描述。"),
    "items.category": e("Primary Google My Business category that best describes the business.", "最能概括该商家的 Google 商家主分类。"),
    "items.category_ids": e("Universal category IDs that stay constant regardless of country.", "通用分类 ID，不随所选国家变化。"),
    "items.additional_categories": e("Additional Google My Business categories describing the business in more detail.", "更细致描述该商家的附加 Google 商家分类。"),
    "items.cid": e("Google-defined client id (cid), unique id of the local establishment.", "Google 定义的客户端 id（cid），本地商家的唯一标识。"),
    "items.feature_id": e("Unique identifier of the element in the SERP (feature id).", "SERP 中该元素的唯一标识（feature id）。"),
    "items.address": e("Street address of the business.", "商家的街道地址。"),
    "items.address_info": e("Object holding the structured address components of the business.", "包含商家结构化地址组成部分的对象。"),
    "items.borough": e("Administrative unit or district the business location belongs to.", "商家所在的行政区或辖区。"),
    "items.city": e("City where the business is located.", "商家所在城市。"),
    "items.zip": e("Postal/ZIP code of the business.", "商家的邮政编码。"),
    "items.region": e("DMA region of the business location.", "商家所在的 DMA 区域。"),
    "items.country_code": e("ISO country code of the business location.", "商家所在地的 ISO 国家代码。"),
    "items.place_id": e("Google place id of the local establishment featured in the element.", "元素中所示本地商家的 Google place id。"),
    "items.phone": e("Phone number of the business.", "商家的电话号码。"),
    "items.url": e("Absolute URL of the business website.", "商家网站的绝对 URL。"),
    "items.contact_url": e("URL of the preferred contact page.", "首选联系页面的 URL。"),
    "items.contributor_url": e("URL of the user's or entity's Local Guides profile, when available.", "用户或实体的 Local Guides 资料页 URL（如有）。"),
    "items.book_online_url": e("URL behind the element's 'book online' button, leading to the booking/order page.", "元素中 'book online' 按钮指向的 URL，通往预订/下单页面。"),
    "items.domain": e("Domain of the business website.", "商家网站的域名。"),
    "items.logo": e("URL of the logo shown on the Google My Business profile.", "Google 商家资料中展示的 logo URL。"),
    "items.main_image": e("URL of the main image shown on the Google My Business profile.", "Google 商家资料中展示的主图 URL。"),
    "items.total_photos": e("Total number of images featured on the Google My Business profile.", "Google 商家资料中收录的图片总数。"),
    "items.snippet": e("Additional descriptive information about the business.", "关于该商家的附加描述信息。"),
    "items.latitude": e("Latitude of the establishment on Google Maps.", "商家在 Google 地图上的纬度。"),
    "items.longitude": e("Longitude of the establishment on Google Maps.", "商家在 Google 地图上的经度。"),
    "items.is_claimed": e("Whether the entity is verified by its owner on Google Maps.", "该实体是否已由其所有者在 Google 地图上认领验证。"),
    "items.attributes": e("Service details presented as user-reviewed checks, based on user feedback and the business category.", "以用户核验勾选形式呈现的服务详情，依据用户反馈与商家分类生成。"),
    "items.available_attributes": e("Attributes the business is indicated to offer.", "标识为该商家提供的属性。"),
    "items.unavailable_attributes": e("Attributes the business is indicated not to offer.", "标识为该商家不提供的属性。"),
    "items.place_topics": e("Most popular keywords mentioned in customer reviews, each mapped to how many reviews mention it.", "客户评论中最常被提及的关键词，每个关键词对应其被提及的评论数。"),
    "items.rating": RATING["rating"],
    "items.rating_type": RATING["rating_type"],
    "items.value": e("Numeric value of the rating.", "评分的数值。"),
    "items.votes_count": e("Number of votes the rating is based on.", "该评分所依据的投票数。"),
    "items.rating_max": RATING["rating_max"],
    "items.rating_distribution": e("Breakdown of how many 1- to 5-star ratings the business received.", "该商家所获 1 至 5 星评分各自数量的分布。"),
    "items.1": e("Number of 1-star ratings.", "1 星评分的数量。"),
    "items.2": e("Number of 2-star ratings.", "2 星评分的数量。"),
    "items.3": e("Number of 3-star ratings.", "3 星评分的数量。"),
    "items.4": e("Number of 4-star ratings.", "4 星评分的数量。"),
    "items.5": e("Number of 5-star ratings.", "5 星评分的数量。"),
    "items.people_also_search": e("Related business entities that users also searched for.", "用户还会搜索的相关商家实体。"),
    "items.work_time": e("Operating-hours details of the business.", "商家营业时间的相关详情。"),
    "items.work_hours": e("Working hours information of the establishment.", "商家的营业时间信息。"),
    "items.timetable": e("Weekly opening-hours timetable.", "每周营业时间表。"),
    "items.sunday": e("Working hours on Sundays.", "周日的营业时间。"),
    "items.open": e("Opening time entry.", "开始营业时间。"),
    "items.hour": e("Hour component in 24-hour format.", "小时（24 小时制）。"),
    "items.minute": e("Minute component.", "分钟。"),
    "items.close": e("Closing time entry.", "结束营业时间。"),
    "items.monday": e("Working hours on Mondays.", "周一的营业时间。"),
    "items.tuesday": e("Working hours on Tuesdays.", "周二的营业时间。"),
    "items.wednesday": e("Working hours on Wednesdays.", "周三的营业时间。"),
    "items.thursday": e("Working hours on Thursdays.", "周四的营业时间。"),
    "items.friday": e("Working hours on Fridays.", "周五的营业时间。"),
    "items.saturday": e("Working hours on Saturdays.", "周六的营业时间。"),
    "items.current_status": e("Current operating status of the establishment; business meaning of values: `opened`, `closed`, `temporarily_closed`, `closed_forever`.", "商家当前的营业状态；取值业务含义：`opened` 营业中、`closed` 已关门、`temporarily_closed` 暂停营业、`closed_forever` 永久关闭。"),
    # popular_times block
    "popular_times": e("Popularity-by-hour information indicating the busy hours of the business.", "按小时统计的热门时段信息，反映商家的繁忙时间。"),
    "popular_times.popular_times_by_days": e("Busy-hours breakdown for each day of the week.", "一周内每天的繁忙时段明细。"),
    "popular_times.sunday": e("Busy hours on Sunday; the same structure applies to the other weekdays.", "周日的繁忙时段；其余各工作日采用相同结构。"),
    "popular_times.time": e("Busy-hour time entry.", "繁忙时段的时间项。"),
    "popular_times.hour": e("Hour component in 24-hour format.", "小时（24 小时制）。"),
    "popular_times.minute": e("Minute component.", "分钟。"),
    "popular_times.popular_index": e("Relative popularity index from 0 to 100; higher means a busier time of day.", "相对热度指数，范围 0 到 100；数值越高表示该时段越繁忙。"),
    # local_business_links
    "local_business_links": e("Direct interaction options offered for the business in search results.", "搜索结果中为该商家提供的直接互动入口列表。"),
    "local_business_links.type": e("Element type marker of the interaction link, e.g. `menu`.", "互动链接的元素类型标记，例如 `menu`。"),
    "local_business_links.title": e("Title of the link, e.g. the domain of the online menu system.", "链接标题，例如在线菜单系统的域名。"),
    "local_business_links.url": e("URL the interaction link points to.", "互动链接指向的 URL。"),
    "local_business_links.delivery_services": e("Available delivery services for the business.", "该商家可用的配送服务。"),
    "local_business_links.is_directory_item": e("Whether this entry belongs to a directory of businesses sharing one address (e.g. a mall); for a parent directory item the value is `null`.", "该条目是否属于共用同一地址的商家目录（如商场）；若其为目录的父级条目，取值为 `null`。"),
    # directory.* block
    "directory": e("Businesses located within the target establishment that share its address.", "位于目标商家内部、与其共用地址的商家集合。"),
    "directory.title": e("Business name of the directory entry.", "目录条目的商家名称。"),
    "directory.items": e("Array of directory items.", "目录条目数组。"),
    "directory.type": e("Element type marker of the directory item, e.g. `maps_search`.", "目录条目的元素类型标记，例如 `maps_search`。"),
    "directory.rank_group": GR_ITEMS["items.rank_group"],
    "directory.rank_absolute": e("Absolute rank among all the elements.", "在全部元素中的绝对排名。"),
    "directory.domain": e("Domain of the business website.", "商家网站的域名。"),
    "directory.url": e("Absolute URL of the business website.", "商家网站的绝对 URL。"),
    "directory.rating": RATING["rating"],
    "directory.rating_type": RATING["rating_type"],
    "directory.value": e("Numeric value of the rating.", "评分的数值。"),
    "directory.votes_count": e("Number of votes the rating is based on.", "该评分所依据的投票数。"),
    "directory.rating_max": RATING["rating_max"],
    "directory.rating_distribution": e("Breakdown of how many 1- to 5-star ratings the business received.", "该商家所获 1 至 5 星评分各自数量的分布。"),
    "directory.1": e("Number of 1-star ratings.", "1 星评分的数量。"),
    "directory.2": e("Number of 2-star ratings.", "2 星评分的数量。"),
    "directory.3": e("Number of 3-star ratings.", "3 星评分的数量。"),
    "directory.4": e("Number of 4-star ratings.", "4 星评分的数量。"),
    "directory.5": e("Number of 5-star ratings.", "5 星评分的数量。"),
    "directory.snippet": e("Additional descriptive information about the business.", "关于该商家的附加描述信息。"),
    "directory.address": e("Street address of the business.", "商家的街道地址。"),
    "directory.address_info": e("Object holding the structured address components of the business.", "包含商家结构化地址组成部分的对象。"),
    "directory.borough": e("Administrative unit or district the business location belongs to.", "商家所在的行政区或辖区。"),
    "directory.city": e("City where the business is located.", "商家所在城市。"),
    "directory.zip": e("Postal/ZIP code of the business.", "商家的邮政编码。"),
    "directory.region": e("DMA region of the business location.", "商家所在的 DMA 区域。"),
    "directory.country_code": e("ISO country code of the business location.", "商家所在地的 ISO 国家代码。"),
    "directory.place_id": e("Google place id of the local establishment featured in the element.", "元素中所示本地商家的 Google place id。"),
    "directory.phone": e("Phone number of the business.", "商家的电话号码。"),
    "directory.main_image": e("URL of the main image shown on the Google My Business profile.", "Google 商家资料中展示的主图 URL。"),
    "directory.total_photos": e("Total number of images featured on the Google My Business profile.", "Google 商家资料中收录的图片总数。"),
    "directory.category": e("Primary Google My Business category that best describes the business.", "最能概括该商家的 Google 商家主分类。"),
    "directory.category_ids": e("Universal category IDs that stay constant regardless of country.", "通用分类 ID，不随所选国家变化。"),
    "directory.work_hours": e("Working hours information of the establishment.", "商家的营业时间信息。"),
    "directory.feature_id": e("Unique identifier of the element in the SERP (feature id).", "SERP 中该元素的唯一标识（feature id）。"),
    "directory.cid": e("Google-defined client id (cid); can be used with the Google Reviews API to fetch the full review list.", "Google 定义的客户端 id（cid）；可配合 Google Reviews API 获取完整评论列表。"),
    "directory.latitude": e("Latitude of the establishment on Google Maps.", "商家在 Google 地图上的纬度。"),
    "directory.longitude": e("Longitude of the establishment on Google Maps.", "商家在 Google 地图上的经度。"),
    "directory.is_claimed": e("Whether the entity is verified by its owner on Google Maps.", "该实体是否已由其所有者在 Google 地图上认领验证。"),
    "directory.local_justifications": e("Google local justification snippets explaining why the business appears for the query.", "Google 本地佐证片段，说明该商家为何会出现在该查询结果中。"),
    "directory.is_directory_item": e("Whether this entry belongs to a directory of businesses sharing one address; for a parent directory item the value is `null`.", "该条目是否属于共用同一地址的商家目录；若其为目录的父级条目，取值为 `null`。"),
    "directory.price_level": e("Price level of the property; business meaning: `inexpensive`, `moderate`, `expensive`, `very_expensive`; `null` when unavailable.", "场所的价格档次；业务含义：`inexpensive` 便宜、`moderate` 适中、`expensive` 偏贵、`very_expensive` 非常贵；无信息时为 `null`。"),
    "directory.hotel_rating": e("Hotel class rating ranging 1-5 stars; `null` when unavailable.", "酒店星级评定，范围 1 至 5 星；无信息时为 `null`。"),
}
build("get_dataforseo_business_data_google_my_business_info_task_get_id",
      "获取 Google 商家信息结果 get_dataforseo_business_data_google_my_business_info_task_get_id",
      "Fetch the results of a previously created Google My Business Info task by its id, returning the full business profile: categories, address, contacts, ratings, attributes, working and popular hours, and any directory sub-listings.",
      "按任务 id 拉取此前创建的 Google 商家信息任务结果，返回完整的商家档案：分类、地址、联系方式、评分、属性、营业与热门时段，以及目录子条目。",
      has_id_param=PARAM_ID_30, resp_over={**MBI_RES, **MBI_ITEMS})

# 9. my business info tasks_ready
build("get_dataforseo_business_data_google_my_business_info_tasks_ready",
      "获取 Google 商家信息已完成任务 get_dataforseo_business_data_google_my_business_info_tasks_ready",
      "List Google My Business Info tasks that have finished processing and are ready to be collected.",
      "列出已处理完成、可供拉取的 Google 商家信息任务。",
      resp_over=READY)

# 10. my business updates task_post
MBU_REQ = {
    "keyword": e("Name of the local establishment to look up (up to 700 characters); percent-encoding is decoded. This field can also carry a Google-defined `cid` to target a specific establishment.",
                 "要查询的本地商家名称（最多 700 个字符）；会解码百分号转义。该字段也可传入 Google 定义的 `cid` 以精确定位某个商家。"),
    "depth": e("Number of updates to parse. Best set in multiples of ten since updates are processed ten at a time; Google returns at most 4490 updates.",
               "要解析的动态更新条数。建议设为 10 的倍数，因为系统每次处理十条；Google 最多返回 4490 条更新。"),
}
build("post_dataforseo_business_data_google_my_business_updates_task_post",
      "创建 Google 商家动态任务 post_dataforseo_business_data_google_my_business_updates_task_post",
      "Create an asynchronous task that collects Google My Business posts/updates for a named establishment; poll tasks_ready and then fetch results by id.",
      "创建一个异步任务，采集指定商家的 Google 商家动态/帖子；随后轮询 tasks_ready 并按 id 拉取结果。",
      req_over=MBU_REQ,
      resp_over={"result": e("Result array; for this task-creation response the value is `null`.", "结果数组；对于本任务创建响应，其值为 `null`。")})

# 11. questions_and_answers live
QA_RES = {
    "result.keyword": MBI_RES["result.keyword"],
    "result.se_domain": e("Search engine domain echoed from the POST request.", "从 POST 请求回显的搜索引擎域名。"),
    "result.location_code": RES_COMMON["result.location_code"],
    "result.language_code": RES_COMMON["result.language_code"],
    "result.check_url": RES_COMMON["result.check_url"],
    "result.datetime": RES_COMMON["result.datetime"],
    "result.cid": e("Google-defined client id (cid), unique id of the local establishment.", "Google 定义的客户端 id（cid），本地商家的唯一标识。"),
    "result.feature_id": e("Unique identifier of the SERP feature.", "该 SERP 特性的唯一标识。"),
    "result.item_types": e("Item types present in the result; possible value: `google_business_question_item`.", "结果中出现的元素类型；可能取值为 `google_business_question_item`。"),
}
def qa_q(prefix):
    return {
        prefix: e("Array of Google Business question items without any answers." if "without" in prefix else "Array of Google Business question items that have answers.",
                  "无回答的 Google 商家问题条目数组。" if "without" in prefix else "含回答的 Google 商家问题条目数组。"),
        prefix+".type": e("Element type marker of the question item.", "问题条目的元素类型标记。"),
        prefix+".rank_group": GR_ITEMS["items.rank_group"],
        prefix+".rank_absolute": e("Absolute rank among all the elements.", "在全部元素中的绝对排名。"),
        prefix+".question_id": e("Unique id of the question.", "问题的唯一 id。"),
        prefix+".url": e("URL of the question.", "问题的 URL。"),
        prefix+".profile_image_url": e("URL of the asker's profile image.", "提问者头像图片的 URL。"),
        prefix+".profile_url": e("URL of the asker's profile.", "提问者资料页的 URL。"),
        prefix+".profile_name": e("Display name of the asker.", "提问者的显示名称。"),
        prefix+".question_text": e("Current text of the question.", "问题的当前文本。"),
        prefix+".original_question_text": e("Original text of the question.", "问题的原始文本。"),
        prefix+".time_ago": e("Relative time when the question was posted.", "问题发布时间的相对表述。"),
        prefix+".timestamp": e("Exact time when the question was posted.", "问题发布的精确时间。"),
        prefix+".items": e("Nested items belonging to this question item.", "归属于该问题条目的嵌套子项。"),
    }
QA_OVER = dict(QA_RES)
qw = qa_q("items_without_answers")
qw["items_without_answers.items_count"] = e("Number of items in this question item's `items` array.", "该问题条目 `items` 数组中的子项数量。")
QA_OVER.update(qw)
qa = qa_q("items")
qa["items.items"] = e("Answers to the Google business question; possible item type: `google_business_answer_element`.", "对该 Google 商家问题的回答；可能的元素类型为 `google_business_answer_element`。")
qa["items.answer_id"] = e("Unique id of the answer.", "回答的唯一 id。")
qa["items.answer_text"] = e("Current text of the answer.", "回答的当前文本。")
qa["items.original_answer_text"] = e("Original text of the answer.", "回答的原始文本。")
QA_OVER.update(qa)
QA_REQ = {
    "keyword": MBU_REQ["keyword"],
    "depth": e("Number of results to parse; default 20, max 100. Billing is per SERP of up to 20 results, so going above 20 may add charges; unused depth is auto-refunded.",
               "要解析的结果数量；默认 20，最大 100。计费以每 20 条结果一个 SERP 为单位，超过 20 可能额外计费；未用尽的额度会自动退还。"),
}
build("post_dataforseo_business_data_google_questions_and_answers_live",
      "实时获取 Google 商家问答 post_dataforseo_business_data_google_questions_and_answers_live",
      "Synchronously retrieve the Questions and Answers section of a Google My Business listing for the named establishment, returning both answered and unanswered questions.",
      "针对指定商家，同步获取其 Google 商家页面的问答区，返回已回答与未回答的问题。",
      req_over=QA_REQ, resp_over=QA_OVER)

# 12. questions_and_answers task_post
QA_REQ2 = {
    "keyword": MBU_REQ["keyword"],
    "depth": e("Number of question rows to parse; default 20, max 700. Billing is per SERP of up to 20 results, so going above 20 may add charges; unused depth is auto-refunded.",
               "要解析的问题行数；默认 20，最大 700。计费以每 20 条结果一个 SERP 为单位，超过 20 可能额外计费；未用尽的额度会自动退还。"),
}
build("post_dataforseo_business_data_google_questions_and_answers_task_post",
      "创建 Google 商家问答任务 post_dataforseo_business_data_google_questions_and_answers_task_post",
      "Create an asynchronous task that collects the Questions and Answers section of a Google My Business listing; poll tasks_ready and fetch results by id.",
      "创建一个异步任务，采集 Google 商家页面的问答区；随后轮询 tasks_ready 并按 id 拉取结果。",
      req_over=QA_REQ2,
      resp_over={"result": e("Result array; for this task-creation response the value is `null`.", "结果数组；对于本任务创建响应，其值为 `null`。")})

# 13. Google reviews task_get
RV_ITEMS = dict(GR_ITEMS)
RV_ITEMS["items.url"] = e("Relevant image URL from Google.", "来自 Google 的相关图片 URL。")
build("get_dataforseo_business_data_google_reviews_task_get_id",
      "获取 Google 评论结果 get_dataforseo_business_data_google_reviews_task_get_id",
      "Fetch the results of a previously created Google Reviews task by its id, returning the establishment's aggregated rating and individual review entries.",
      "按任务 id 拉取此前创建的 Google 评论任务结果，返回商家的综合评分及单条评论条目。",
      has_id_param=PARAM_ID_30, resp_over={**GR_RESULT, **RV_ITEMS})

# 14. Google reviews tasks_ready
build("get_dataforseo_business_data_google_reviews_tasks_ready",
      "获取 Google 评论已完成任务 get_dataforseo_business_data_google_reviews_tasks_ready",
      "List Google Reviews tasks that have finished processing and are ready to be collected.",
      "列出已处理完成、可供拉取的 Google 评论任务。",
      resp_over=READY)

# 15. social media reddit live
RD_REQ = {
    "targets": e("Target page URLs to analyse, each an absolute URL including the scheme; up to 10 targets, each billed separately.",
                 "要分析的目标页面 URL，每个都需为含协议头的绝对 URL；最多 10 个目标，每个目标单独计费。"),
}
RD_RES = {
    "result.type": e("Element type marker, here `social_media_reddit_item`.", "元素类型标记，此处为 `social_media_reddit_item`。"),
    "result.page_url": e("Target page URL this Reddit data corresponds to, matching an entry from the `targets` array.", "该 Reddit 数据所对应的目标页面 URL，与 `targets` 数组中的某项一致。"),
    "result.reddit reviews": e("Reddit mentions/posts associated with the page_url.", "与 page_url 关联的 Reddit 提及/帖子。"),
    "result.subreddit": e("Name of the subreddit where the URL was shared.", "分享该 URL 所在的 subreddit 名称。"),
    "result.author_name": e("Nickname of the user who posted the URL in the subreddit.", "在该 subreddit 中发布该 URL 的用户昵称。"),
    "result.title": e("Title of the subreddit post.", "该 subreddit 帖子的标题。"),
    "result.permalink": e("Permanent URL of the subreddit post.", "该 subreddit 帖子的固定链接 URL。"),
    "result.subreddit_members": e("Number of members in the subreddit.", "该 subreddit 的成员数量。"),
}
build("post_dataforseo_business_data_social_media_reddit_live",
      "实时获取 Reddit 社媒数据 post_dataforseo_business_data_social_media_reddit_live",
      "Synchronously retrieve Reddit mentions (subreddit posts that share the URL) for one or more target pages, returning the subreddit and post details for each.",
      "针对一个或多个目标页面，同步获取其在 Reddit 上的提及（分享该 URL 的 subreddit 帖子），并返回各自的 subreddit 与帖子详情。",
      req_over=RD_REQ, resp_over=RD_RES)

# 16. tripadvisor reviews task_post
TR_REQ = {
    "url_path": e("Tripadvisor page URL path of the business entity. Provide this or `keyword`. You can obtain it from the Tripadvisor Search items' `url_path`.",
                  "商家在 Tripadvisor 上的页面 URL 路径。需与 `keyword` 择一提供。可从 Tripadvisor 搜索结果条目的 `url_path` 获取。"),
    "keyword": e("Name of an existing Tripadvisor business or place (up to 700 characters; percent-encoding decoded). Provide this or `url_path`.",
                 "Tripadvisor 上已存在的商家或地点名称（最多 700 个字符；会解码百分号转义）。需与 `url_path` 择一提供。"),
    "location_name": e("Full location name; required if you specify neither `location_code` nor `url_path`. The available list comes from the Tripadvisor `/locations` endpoint.",
                       "完整地区名称；若既未指定 `location_code` 也未指定 `url_path` 则必填。可用列表来自 Tripadvisor `/locations` 端点。"),
    "location_code": e("Numeric location code; required if you specify neither `location_name` nor `url_path`. The available list comes from the Tripadvisor `/locations` endpoint.",
                       "数字地区代码；若既未指定 `location_name` 也未指定 `url_path` 则必填。可用列表来自 Tripadvisor `/locations` 端点。"),
    "language_name": e("Full language name. Using this field incurs one extra request charge. The available list comes from the Tripadvisor `/languages` endpoint.",
                       "完整语言名称。使用该字段会额外计费一次请求。可用列表来自 Tripadvisor `/languages` 端点。"),
    "language_code": e("Language code. Using this field incurs one extra request charge. The available list comes from the Tripadvisor `/languages` endpoint.",
                       "语言代码。使用该字段会额外计费一次请求。可用列表来自 Tripadvisor `/languages` 端点。"),
    "depth": e("Number of reviews to parse; best set in multiples of ten (processed ten at a time). Default 10, max 4490. Billing is per SERP of up to 10 results.",
               "要解析的评论数量；建议设为 10 的倍数（每次处理十条）。默认 10，最大 4490。计费以每 10 条结果一个 SERP 为单位。"),
    "ratings": e("Filter reviews by Tripadvisor traveler rating; business meaning of values: `excellent`, `very_good`, `average`, `poor`, `terrible`. Multiple values allowed.",
                 "按 Tripadvisor 旅行者评分筛选评论；取值业务含义：`excellent` 极佳、`very_good` 很好、`average` 一般、`poor` 较差、`terrible` 很差。可同时指定多个值。"),
    "visit_type": e("Filter by traveler type; business meaning of values: `families`, `couples`, `solo`, `business`, `friends`. Multiple values allowed.",
                    "按出行者类型筛选；取值业务含义：`families` 家庭、`couples` 情侣、`solo` 独行、`business` 商务、`friends` 朋友。可同时指定多个值。"),
    "months": e("Filter by the month of the traveler's visit, given as month names (e.g. `january`). Multiple values allowed.",
                "按旅行者到访的月份筛选，以月份英文名给出（如 `january`）。可同时指定多个值。"),
    "search_reviews_keyword": e("Return only reviews that contain the specified keyword.",
                                "仅返回包含指定关键词的评论。"),
    "sort_by": e("Sort order of the returned reviews; business meaning: `most_recent` newest first, `detailed_reviews` most detailed first.",
                 "返回评论的排序方式；业务含义：`most_recent` 最新优先、`detailed_reviews` 内容最详尽优先。"),
    "translate_reviews": e("When `true`, reviews are translated to the language matching the `url_path` (e.g. Italian for a `tripadvisor.it` path).",
                           "为 `true` 时，评论会被翻译为与 `url_path` 匹配的语言（例如 `tripadvisor.it` 路径对应意大利语）。"),
}
build("post_dataforseo_business_data_tripadvisor_reviews_task_post",
      "创建 Tripadvisor 评论任务 post_dataforseo_business_data_tripadvisor_reviews_task_post",
      "Create an asynchronous task that collects Tripadvisor reviews for a business identified by URL path or keyword, with optional filters by rating, traveler type, visit month and review keyword.",
      "创建一个异步任务，采集由 URL 路径或关键词指定商家的 Tripadvisor 评论，并可按评分、出行者类型、到访月份及评论关键词进行筛选。",
      req_over=TR_REQ,
      resp_over={"result": e("Result array; for this task-creation response the value is `null`.", "结果数组；对于本任务创建响应，其值为 `null`。")})

# 17. tripadvisor search task_get
TS_RES = dict(RES_COMMON)
TS_RES.update({
    "result.keyword": e("Keyword echoed from the POST request; if an `alias` was specified in the request it is returned here.", "从 POST 请求回显的关键词；若请求中指定了 `alias`，此处会返回该值。"),
    "result.check_url": e("Direct URL to the Tripadvisor results, so you can verify the data.", "指向 Tripadvisor 结果的直达 URL，可用于核对数据。"),
    "result.item_types": e("Item types present in the result; possible value: `tripadvisor_search_organic`.", "结果中出现的元素类型；可能取值为 `tripadvisor_search_organic`。"),
    "result.se_results_count": e("Total number of results found.", "找到的结果总数。"),
})
del TS_RES["result.type"]  # only result.type is absent; location_code/language_code are present
TS_ITEMS = {
    "items": e("Tripadvisor search listing results; raise `depth` at task creation for more.", "Tripadvisor 搜索列表结果；创建任务时调大 `depth` 可获取更多。"),
    "items.type": e("Result type, here `tripadvisor_search_organic`.", "结果类型，此处为 `tripadvisor_search_organic`。"),
    "items.rank_group": GR_ITEMS["items.rank_group"],
    "items.rank_absolute": e("Absolute rank among all the listed results.", "在全部已列出结果中的绝对排名。"),
    "items.title": e("Name of the business entity.", "商家实体的名称。"),
    "items.url_path": e("Tripadvisor page URL path of the business; reuse it with the Tripadvisor Reviews endpoint to collect its reviews.", "商家的 Tripadvisor 页面 URL 路径；可配合 Tripadvisor Reviews 端点采集其评论。"),
    "items.is_sponsored": e("Whether the item is a paid (sponsored) Tripadvisor placement.", "该条目是否为 Tripadvisor 上的付费（赞助）展示位。"),
    "items.reviews_count": e("Total number of reviews for the business.", "该商家的评论总数。"),
    "items.category": e("Place category.", "地点分类。"),
    "items.price_rate": e("Average price rate of the place.", "该地点的平均价格水平。"),
    "items.rating": e("Rating score of the establishment submitted by reviewers.", "评论者给出的该商家评分。"),
    "items.rating_type": RATING["rating_type"],
    "items.value": e("Numeric value of the rating.", "评分的数值。"),
    "items.votes_count": e("Number of votes the establishment received.", "该商家获得的投票数。"),
    "items.rating_max": RATING["rating_max"],
}
build("get_dataforseo_business_data_tripadvisor_search_task_get_id",
      "获取 Tripadvisor 搜索结果 get_dataforseo_business_data_tripadvisor_search_task_get_id",
      "Fetch the results of a previously created Tripadvisor Search task by its id, returning matched business listings with category, price rate and rating data.",
      "按任务 id 拉取此前创建的 Tripadvisor 搜索任务结果，返回匹配的商家列表及其分类、价格水平与评分数据。",
      has_id_param=PARAM_ID_30, resp_over={**TS_RES, **TS_ITEMS})

# 18. tripadvisor search tasks_ready
build("get_dataforseo_business_data_tripadvisor_search_tasks_ready",
      "获取 Tripadvisor 搜索已完成任务 get_dataforseo_business_data_tripadvisor_search_tasks_ready",
      "List Tripadvisor Search tasks that have finished processing and are ready to be collected.",
      "列出已处理完成、可供拉取的 Tripadvisor 搜索任务。",
      resp_over=READY)

# 19. trustpilot reviews task_post
TP_REQ = {
    "domain": e("Domain of the establishment on Trustpilot, found in the URL of any Trustpilot business listing, e.g. `www.thepearlsource.com`.",
                "该商家在 Trustpilot 上的域名，可在任一 Trustpilot 商家页面的 URL 中找到，例如 `www.thepearlsource.com`。"),
    "sort_by": e("Sort order of the returned reviews; business meaning: `recency` most recent first, `relevance` most relevant first (default).",
                 "返回评论的排序方式；业务含义：`recency` 最新优先、`relevance` 最相关优先（默认）。"),
    "depth": e("Number of reviews to return; best set in multiples of twenty (processed twenty at a time). Default 20, max 200. Billing is per SERP of up to 20 results.",
               "要返回的评论数量；建议设为 20 的倍数（每次处理二十条）。默认 20，最大 200。计费以每 20 条结果一个 SERP 为单位。"),
}
build("post_dataforseo_business_data_trustpilot_reviews_task_post",
      "创建 Trustpilot 评论任务 post_dataforseo_business_data_trustpilot_reviews_task_post",
      "Create an asynchronous task that collects Trustpilot reviews for an establishment identified by its domain; poll tasks_ready and fetch results by id.",
      "创建一个异步任务，采集由域名指定商家的 Trustpilot 评论；随后轮询 tasks_ready 并按 id 拉取结果。",
      req_over=TP_REQ,
      resp_over={"result": e("Result array; for this task-creation response the value is `null`.", "结果数组；对于本任务创建响应，其值为 `null`。")})

# 20. trustpilot search task_get
TPS_RES = {
    "result.keyword": e("Keyword echoed from the POST request.", "从 POST 请求回显的关键词。"),
    "result.se_domain": e("Search engine domain echoed from the POST request.", "从 POST 请求回显的搜索引擎域名。"),
    "result.check_url": RES_COMMON["result.check_url"],
    "result.datetime": RES_COMMON["result.datetime"],
    "result.items_count": e("Number of items in the results array; raise `depth` at task creation for more.", "结果数组中的元素数量；创建任务时调大 `depth` 可获取更多。"),
}
TPS_ITEMS = {
    "items": e("Trustpilot search listing results; raise `depth` at task creation for more.", "Trustpilot 搜索列表结果；创建任务时调大 `depth` 可获取更多。"),
    "items.type": e("Result type, here `trustpilot_search_organic`.", "结果类型，此处为 `trustpilot_search_organic`。"),
    "items.rank_group": GR_ITEMS["items.rank_group"],
    "items.rank_absolute": e("Absolute rank among all the listed results.", "在全部已列出结果中的绝对排名。"),
    "items.title": e("Title of the establishment.", "商家的名称。"),
    "items.domain": e("Domain of the establishment.", "商家的域名。"),
    "items.url": e("URL of the establishment on Trustpilot.", "商家在 Trustpilot 上的 URL。"),
    "items.reviews_count": e("Total number of reviews for the establishment.", "该商家的评论总数。"),
    "items.rating": e("Rating score of the establishment submitted by reviewers.", "评论者给出的该商家评分。"),
    "items.rating_type": RATING["rating_type"],
    "items.value": e("Numeric value of the rating.", "评分的数值。"),
    "items.votes_count": e("Number of votes the establishment received.", "该商家获得的投票数。"),
    "items.rating_max": RATING["rating_max"],
}
build("get_dataforseo_business_data_trustpilot_search_task_get_id",
      "获取 Trustpilot 搜索结果 get_dataforseo_business_data_trustpilot_search_task_get_id",
      "Fetch the results of a previously created Trustpilot Search task by its id, returning matched establishments with their domain, review count and rating data.",
      "按任务 id 拉取此前创建的 Trustpilot 搜索任务结果，返回匹配的商家及其域名、评论数与评分数据。",
      has_id_param=PARAM_ID_30, resp_over={**TPS_RES, **TPS_ITEMS})

# 21. trustpilot search tasks_ready
build("get_dataforseo_business_data_trustpilot_search_tasks_ready",
      "获取 Trustpilot 搜索已完成任务 get_dataforseo_business_data_trustpilot_search_tasks_ready",
      "List Trustpilot Search tasks that have finished processing and are ready to be collected.",
      "列出已处理完成、可供拉取的 Trustpilot 搜索任务。",
      resp_over=READY)


# ------------------------------------------------------------------ emit
content = {"operations": operations, "fields": fields}
json.dump(content, open(OUT, "w"), ensure_ascii=False, indent=2)
print("ops:", len(operations))
nf = 0
for k, v in fields.items():
    nf += len(v.get("request", {}))
    for code, dm in v.get("response", {}).items():
        nf += len(dm)
    nf += len(v.get("parameters", {}))
print("field entries:", nf)
