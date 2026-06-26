#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembler for google_2.content.json (dataforseo serp/google series, 47 ops).

All doc TEXT below is hand-authored per METHODOLOGY.md (one entry per distinct
semantic field). This script only ROUTES my authored text onto the exact literal
dotpaths the completeness gate requires (read from /tmp/g2_inv.json). It does NOT
generate text by template: every dotpath must resolve to a hand-written entry,
otherwise the build aborts (guard) — forcing me to author, never to pad.

dataforseo response schemas use flat literal property keys that themselves
contain dots and brackets (e.g. "tasks[].result[].items[].title"). The inventory
preserves those literal keys verbatim; lookups key on the literal dotpath /
leaf-name. The injector matches the longest literal integer key.
"""
import json
import sys

INV = json.load(open("/tmp/g2_inv.json"))


def E(desc_en, title_zh, **kw):
    d = {"desc_en": desc_en, "title_zh": title_zh}
    d.update(kw)
    return d


# ===========================================================================
# Operation-level metadata (hand-authored)
# ===========================================================================
OPS = {
 "post_dataforseo_serp_google_organic_task_post": E(
   "Queue a Google Organic SERP task for a keyword/location/language; you are charged only for posting, and up to 100 tasks can be sent per call. The response returns a task id used to collect the SERP later via the matching task_get endpoint or via postback/pingback.",
   "为给定 keyword/地区/语言提交一个 Google 自然搜索（Organic）SERP 任务；仅按提交计费，单次调用最多 100 个任务。响应返回 task id，稍后通过对应的 task_get 端点或 postback/pingback 收取 SERP。",
   heading_zh="提交 Google 自然搜索 SERP 任务 post_dataforseo_serp_google_organic_task_post"),
 "get_dataforseo_serp_google_organic_task_get_html_id": E(
   "Retrieve the raw HTML of a previously posted Google Organic SERP task by its id; available within 30 days of posting at no extra charge.",
   "按 task id 取回此前提交的 Google 自然搜索 SERP 任务的原始 HTML；提交后 30 天内可免费获取。",
   heading_zh="按 id 获取 Google 自然搜索 HTML 结果 get_dataforseo_serp_google_organic_task_get_html_id"),
 "post_dataforseo_serp_google_organic_live_regular": E(
   "Return Google Organic SERP results in the regular (lightweight) format immediately in the same response; each Live SERP call carries exactly one task.",
   "以常规（轻量）格式即时返回 Google 自然搜索 SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google 自然搜索 SERP（常规） post_dataforseo_serp_google_organic_live_regular"),
 "post_dataforseo_serp_google_organic_live_advanced": E(
   "Return Google Organic SERP results in the advanced (full element-level) format immediately in the same response; each Live SERP call carries exactly one task.",
   "以高级（完整元素级）格式即时返回 Google 自然搜索 SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google 自然搜索 SERP（高级） post_dataforseo_serp_google_organic_live_advanced"),
 "post_dataforseo_serp_google_ai_mode_task_post": E(
   "Queue a Google AI Mode SERP task, returning search results from Google Search's AI Mode feature; up to 100 tasks per call. Collect the completed task later by id or via postback/pingback.",
   "提交一个 Google AI Mode SERP 任务，返回 Google 搜索 AI Mode 功能的搜索结果；单次最多 100 个任务。稍后按 id 或通过 postback/pingback 收取已完成任务。",
   heading_zh="提交 Google AI Mode SERP 任务 post_dataforseo_serp_google_ai_mode_task_post"),
 "get_dataforseo_serp_google_ai_mode_task_get_advanced_id": E(
   "Retrieve advanced Google AI Mode SERP results by task id; available within 30 days of posting at no extra charge beyond the task fee.",
   "按 task id 取回 Google AI Mode SERP 的高级结果；提交后 30 天内除任务费外不再额外收费。",
   heading_zh="按 id 获取 Google AI Mode SERP 高级结果 get_dataforseo_serp_google_ai_mode_task_get_advanced_id"),
 "post_dataforseo_serp_google_ai_mode_live_advanced": E(
   "Return advanced Google AI Mode SERP results in real time in the same response; each Live SERP call carries exactly one task.",
   "以高级格式即时返回 Google AI Mode SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google AI Mode SERP（高级） post_dataforseo_serp_google_ai_mode_live_advanced"),
 "post_dataforseo_serp_google_maps_task_post": E(
   "Queue a Google Maps SERP task for a keyword/location; charged only for posting, up to 100 tasks per call, with results collected later by id or via postback/pingback.",
   "为给定 keyword/地区提交一个 Google 地图 SERP 任务；仅按提交计费，单次最多 100 个任务，结果稍后按 id 或通过 postback/pingback 收取。",
   heading_zh="提交 Google 地图 SERP 任务 post_dataforseo_serp_google_maps_task_post"),
 "post_dataforseo_serp_google_maps_live_advanced": E(
   "Return Google Maps SERP results in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回 Google 地图 SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google 地图 SERP post_dataforseo_serp_google_maps_live_advanced"),
 "post_dataforseo_serp_google_local_finder_task_post": E(
   "Queue a Google Local Finder SERP task for a keyword/location; charged only for posting, up to 100 tasks per call, with results collected later by id or via postback/pingback.",
   "为给定 keyword/地区提交一个 Google Local Finder SERP 任务；仅按提交计费，单次最多 100 个任务，结果稍后按 id 或通过 postback/pingback 收取。",
   heading_zh="提交 Google Local Finder SERP 任务 post_dataforseo_serp_google_local_finder_task_post"),
 "get_dataforseo_serp_google_local_finder_task_get_advanced_id": E(
   "Retrieve advanced Google Local Finder SERP results by task id within the retention window after the task was posted.",
   "在任务提交后的留存期内，按 task id 取回 Google Local Finder SERP 的高级结果。",
   heading_zh="按 id 获取 Google Local Finder SERP 高级结果 get_dataforseo_serp_google_local_finder_task_get_advanced_id"),
 "post_dataforseo_serp_google_local_finder_live_advanced": E(
   "Return Google Local Finder SERP results in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回 Google Local Finder SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google Local Finder SERP post_dataforseo_serp_google_local_finder_live_advanced"),
 "post_dataforseo_serp_google_news_task_post": E(
   "Queue a Google News SERP task for a keyword/location; charged only for posting, up to 100 tasks per call, with results collected later by id or via postback/pingback.",
   "为给定 keyword/地区提交一个 Google 新闻 SERP 任务；仅按提交计费，单次最多 100 个任务，结果稍后按 id 或通过 postback/pingback 收取。",
   heading_zh="提交 Google 新闻 SERP 任务 post_dataforseo_serp_google_news_task_post"),
 "get_dataforseo_serp_google_news_task_get_advanced_id": E(
   "Retrieve advanced Google News SERP results by task id within the retention window after the task was posted.",
   "在任务提交后的留存期内，按 task id 取回 Google 新闻 SERP 的高级结果。",
   heading_zh="按 id 获取 Google 新闻 SERP 高级结果 get_dataforseo_serp_google_news_task_get_advanced_id"),
 "post_dataforseo_serp_google_news_live_advanced": E(
   "Return Google News SERP results in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回 Google 新闻 SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google 新闻 SERP post_dataforseo_serp_google_news_live_advanced"),
 "get_dataforseo_serp_google_events_tasks_ready": E(
   "List completed Google Events SERP tasks that have not yet been collected; up to 1000 tasks completed within the previous 3 days are returned per call, each with the endpoint to fetch its results.",
   "列出已完成但尚未收取的 Google 活动（Events）SERP 任务；单次最多返回近 3 天内完成的 1000 个任务，每项附带取结果的端点。",
   heading_zh="列出可收取的 Google 活动 SERP 任务 get_dataforseo_serp_google_events_tasks_ready"),
 "get_dataforseo_serp_google_events_task_get_advanced_id": E(
   "Retrieve advanced Google Events SERP results by task id within the retention window after the task was posted.",
   "在任务提交后的留存期内，按 task id 取回 Google 活动 SERP 的高级结果。",
   heading_zh="按 id 获取 Google 活动 SERP 高级结果 get_dataforseo_serp_google_events_task_get_advanced_id"),
 "post_dataforseo_serp_google_events_live_advanced": E(
   "Return Google Events SERP results in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回 Google 活动 SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google 活动 SERP（高级） post_dataforseo_serp_google_events_live_advanced"),
 "get_dataforseo_serp_google_images_tasks_ready": E(
   "List completed Google Images SERP tasks that have not yet been collected; up to 1000 tasks completed within the previous 3 days are returned per call, each with the endpoints to fetch its regular and HTML results.",
   "列出已完成但尚未收取的 Google 图片 SERP 任务；单次最多返回近 3 天内完成的 1000 个任务，每项附带取常规结果与 HTML 结果的端点。",
   heading_zh="列出可收取的 Google 图片 SERP 任务 get_dataforseo_serp_google_images_tasks_ready"),
 "get_dataforseo_serp_google_images_task_get_regular_id": E(
   "Retrieve regular-format Google Images SERP results for a previously posted task by its id.",
   "按 task id 取回此前提交任务的 Google 图片 SERP 常规格式结果。",
   heading_zh="按 id 获取 Google 图片 SERP 结果 get_dataforseo_serp_google_images_task_get_regular_id"),
 "post_dataforseo_serp_google_images_live_html": E(
   "Return the raw HTML of Google Images SERP results in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回 Google 图片 SERP 结果的原始 HTML，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google 图片 SERP HTML post_dataforseo_serp_google_images_live_html"),
 "post_dataforseo_serp_google_search_by_image_task_post": E(
   "Queue a Google Search-by-Image SERP task using a publicly accessible image URL as the query; charged only for posting, up to 100 tasks per call, with results collected later by id or via postback/pingback.",
   "以一个可公开访问的图片 URL 作为查询，提交一个 Google 以图搜图（Search by Image）SERP 任务；仅按提交计费，单次最多 100 个任务，结果稍后按 id 或通过 postback/pingback 收取。",
   heading_zh="提交 Google 以图搜图 SERP 任务 post_dataforseo_serp_google_search_by_image_task_post"),
 "get_dataforseo_serp_google_search_by_image_task_get_advanced_id": E(
   "Retrieve advanced Google Search-by-Image SERP results by task id within the retention window after the task was posted.",
   "在任务提交后的留存期内，按 task id 取回 Google 以图搜图 SERP 的高级结果。",
   heading_zh="按 id 获取 Google 以图搜图 SERP 高级结果 get_dataforseo_serp_google_search_by_image_task_get_advanced_id"),
 "post_dataforseo_serp_google_jobs_task_post": E(
   "Queue a Google Jobs SERP task for a keyword/location; charged only for posting, up to 100 tasks per call, with results collected later by id or via postback/pingback.",
   "为给定 keyword/地区提交一个 Google 招聘（Jobs）SERP 任务；仅按提交计费，单次最多 100 个任务，结果稍后按 id 或通过 postback/pingback 收取。",
   heading_zh="提交 Google 招聘 SERP 任务 post_dataforseo_serp_google_jobs_task_post"),
 "get_dataforseo_serp_google_jobs_task_get_advanced_id": E(
   "Retrieve advanced Google Jobs SERP results by task id within the retention window after the task was posted.",
   "在任务提交后的留存期内，按 task id 取回 Google 招聘 SERP 的高级结果。",
   heading_zh="按 id 获取 Google 招聘 SERP 高级结果 get_dataforseo_serp_google_jobs_task_get_advanced_id"),
 "post_dataforseo_serp_google_autocomplete_task_post": E(
   "Queue a Google Autocomplete task that returns search suggestions for a keyword, cursor position, and search client; charged only for posting.",
   "提交一个 Google 自动补全（Autocomplete）任务，返回给定 keyword、光标位置与搜索客户端下的搜索建议；仅按提交计费。",
   heading_zh="提交 Google 自动补全任务 post_dataforseo_serp_google_autocomplete_task_post"),
 "post_dataforseo_serp_google_autocomplete_live_advanced": E(
   "Return Google Autocomplete suggestions in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回 Google 自动补全建议，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google 自动补全（高级） post_dataforseo_serp_google_autocomplete_live_advanced"),
 "post_dataforseo_serp_google_dataset_search_task_post": E(
   "Queue a Google Dataset Search task that returns datasets matching the keyword; charged only for posting.",
   "提交一个 Google 数据集搜索（Dataset Search）任务，返回与 keyword 匹配的数据集；仅按提交计费。",
   heading_zh="提交 Google 数据集搜索任务 post_dataforseo_serp_google_dataset_search_task_post"),
 "post_dataforseo_serp_google_dataset_search_live_advanced": E(
   "Return Google Dataset Search results in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回 Google 数据集搜索结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google 数据集搜索（高级） post_dataforseo_serp_google_dataset_search_live_advanced"),
 "post_dataforseo_serp_google_dataset_info_task_post": E(
   "Queue a Google Dataset Info task that returns detailed metadata about a specific dataset; charged only for posting.",
   "提交一个 Google 数据集信息（Dataset Info）任务，返回某个数据集的详细元数据；仅按提交计费。",
   heading_zh="提交 Google 数据集信息任务 post_dataforseo_serp_google_dataset_info_task_post"),
 "post_dataforseo_serp_google_dataset_info_live_advanced": E(
   "Return Google Dataset Info results in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回 Google 数据集信息结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google 数据集信息（高级） post_dataforseo_serp_google_dataset_info_live_advanced"),
 "get_dataforseo_serp_google_ads_advertisers_locations": E(
   "Return the list of locations supported by the Google Ads Advertisers SERP API; this endpoint is free to call.",
   "返回 Google Ads Advertisers SERP API 支持的地区列表；该端点免费调用。",
   heading_zh="列出 Google Ads Advertisers 支持地区 get_dataforseo_serp_google_ads_advertisers_locations"),
 "post_dataforseo_serp_google_ads_advertisers_task_post": E(
   "Queue a Google Ads Advertisers task that returns advertiser information from the Ads Transparency platform for a keyword and location; charged only for posting.",
   "提交一个 Google Ads Advertisers 任务，返回 Ads Transparency 平台上某 keyword 与地区下的广告主信息；仅按提交计费。",
   heading_zh="提交 Google Ads Advertisers 任务 post_dataforseo_serp_google_ads_advertisers_task_post"),
 "get_dataforseo_serp_google_ads_search_tasks_ready": E(
   "List completed Google Ads Search tasks that have not yet been collected, each with the endpoint to fetch its advanced results.",
   "列出已完成但尚未收取的 Google Ads Search 任务，每项附带取高级结果的端点。",
   heading_zh="列出可收取的 Google Ads Search 任务 get_dataforseo_serp_google_ads_search_tasks_ready"),
 "get_dataforseo_serp_google_ads_search_task_get_advanced_id": E(
   "Retrieve advanced Google Ads Search results by task id within the retention period after the task was posted.",
   "在任务提交后的留存期内，按 task id 取回 Google Ads Search 的高级结果。",
   heading_zh="按 id 获取 Google Ads Search 高级结果 get_dataforseo_serp_google_ads_search_task_get_advanced_id"),
 "post_dataforseo_serp_google_ads_search_live_advanced": E(
   "Return Google Ads Search data in real time in the same response; identify the advertiser by advertiser_ids or by target domain. Each Live SERP call carries exactly one task.",
   "即时返回 Google Ads Search 数据，结果在同一响应中给出；通过 advertiser_ids 或 target 域名指定广告主。每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Google Ads Search（高级） post_dataforseo_serp_google_ads_search_live_advanced"),
 "get_dataforseo_serp_google_finance_explore_tasks_ready": E(
   "List completed Google Finance Explore tasks that have not yet been collected, each with the endpoints to fetch its advanced and HTML results.",
   "列出已完成但尚未收取的 Google Finance Explore 任务，每项附带取高级结果与 HTML 结果的端点。",
   heading_zh="列出可收取的 Finance Explore 任务 get_dataforseo_serp_google_finance_explore_tasks_ready"),
 "get_dataforseo_serp_google_finance_explore_task_get_html_id": E(
   "Retrieve the HTML results of a previously posted Google Finance Explore task by its id.",
   "按 task id 取回此前提交的 Google Finance Explore 任务的 HTML 结果。",
   heading_zh="按 id 获取 Finance Explore HTML 结果 get_dataforseo_serp_google_finance_explore_task_get_html_id"),
 "post_dataforseo_serp_google_finance_explore_live_html": E(
   "Return the raw HTML of the Google Finance Explore tab in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回 Google Finance Explore 标签页的原始 HTML，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Finance Explore SERP HTML post_dataforseo_serp_google_finance_explore_live_html"),
 "get_dataforseo_serp_google_finance_markets_tasks_ready": E(
   "List completed Google Finance Markets tasks that have not yet been collected, each with the endpoints to fetch its advanced and HTML results.",
   "列出已完成但尚未收取的 Google Finance Markets 任务，每项附带取高级结果与 HTML 结果的端点。",
   heading_zh="列出可收取的 Finance Markets 任务 get_dataforseo_serp_google_finance_markets_tasks_ready"),
 "get_dataforseo_serp_google_finance_markets_task_get_html_id": E(
   "Retrieve the HTML results of a previously posted Google Finance Markets task by its id.",
   "按 task id 取回此前提交的 Google Finance Markets 任务的 HTML 结果。",
   heading_zh="按 id 获取 Finance Markets HTML 结果 get_dataforseo_serp_google_finance_markets_task_get_html_id"),
 "post_dataforseo_serp_google_finance_markets_live_html": E(
   "Return the raw HTML of the Google Finance Markets tab in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回 Google Finance Markets 标签页的原始 HTML，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Finance Markets SERP HTML post_dataforseo_serp_google_finance_markets_live_html"),
 "get_dataforseo_serp_google_finance_quote_tasks_ready": E(
   "List completed Google Finance Quote tasks that have not yet been collected, each with the endpoints to fetch its advanced and HTML results.",
   "列出已完成但尚未收取的 Google Finance Quote 任务，每项附带取高级结果与 HTML 结果的端点。",
   heading_zh="列出可收取的 Finance Quote 任务 get_dataforseo_serp_google_finance_quote_tasks_ready"),
 "get_dataforseo_serp_google_finance_quote_task_get_html_id": E(
   "Retrieve the HTML results of a previously posted Google Finance Quote task by its id.",
   "按 task id 取回此前提交的 Google Finance Quote 任务的 HTML 结果。",
   heading_zh="按 id 获取 Finance Quote HTML 结果 get_dataforseo_serp_google_finance_quote_task_get_html_id"),
 "post_dataforseo_serp_google_finance_quote_live_html": E(
   "Return the raw HTML of the Google Finance Quote tab for a ticker symbol in real time in the same response; each Live SERP call carries exactly one task.",
   "即时返回某股票代码在 Google Finance Quote 标签页的原始 HTML，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。",
   heading_zh="实时获取 Finance Quote SERP HTML post_dataforseo_serp_google_finance_quote_live_html"),
 "get_dataforseo_serp_google_finance_ticker_search_tasks_ready": E(
   "List completed Google Finance Ticker Search tasks that have not yet been collected, each with the endpoint to fetch its advanced results.",
   "列出已完成但尚未收取的 Google Finance Ticker Search 任务，每项附带取高级结果的端点。",
   heading_zh="列出可收取的 Finance Ticker Search 任务 get_dataforseo_serp_google_finance_ticker_search_tasks_ready"),
 "get_dataforseo_serp_google_finance_ticker_search_task_get_advanced_id": E(
   "Retrieve advanced Google Finance Ticker Search results for a previously posted task by its id.",
   "按 task id 取回此前提交任务的 Google Finance Ticker Search 高级结果。",
   heading_zh="按 id 获取 Finance Ticker Search 结果 get_dataforseo_serp_google_finance_ticker_search_task_get_advanced_id"),
}

# ===========================================================================
# Path parameters (only `id` appears, always the same meaning)
# ===========================================================================
PARAMS = {
 "id": E("UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted.",
         "要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。"),
}

# ===========================================================================
# Request body fields (hand-authored, keyed by leaf name; full-path overrides
# where context shifts the meaning)
# ===========================================================================
REQ = {
 "keyword": E("Search term to query. URL-encode it; the SERP is built around this query.",
              "要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。"),
 "location_name": E("Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP.",
                    "搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。"),
 "location_code": E("Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint.",
                    "搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。"),
 "location_coordinate": E("GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting.",
                          "目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。"),
 "language_name": E("Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language.",
                    "搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。"),
 "language_code": E("Two-letter language code (e.g. `en`); the code-based alternative to `language_name`.",
                    "两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。"),
 "depth": E("Number of SERP results to parse; deeper values cost more crawl pages and increase task price.",
            "要解析的 SERP 结果数量；取值越深消耗的抓取页数越多，任务价格也越高。"),
 "max_crawl_pages": E("Upper bound on the number of SERP pages to crawl for this task.",
                      "本任务抓取的 SERP 页面数上限。"),
 "device": E("Device profile to emulate for the search, such as `desktop` or `mobile`; affects layout and result set.",
             "搜索时模拟的设备类型，如 `desktop` 或 `mobile`，会影响版式与结果集合。"),
 "os": E("Operating system to emulate for the chosen device, refining the user-agent presented to Google.",
         "为所选设备模拟的操作系统，用于细化向 Google 呈现的 user-agent。"),
 "group_organic_results": E("When enabled, related organic results are merged and reported as grouped organic entries instead of separate items.",
                            "启用后，相关的自然结果会被合并归组为分组自然条目，而非分散的独立条目。"),
 "calculate_rectangles": E("When enabled, pixel-coordinate rankings (rectangles) are computed for elements in the advanced SERP, useful for visual position analysis.",
                           "启用后，会为高级 SERP 中的元素计算像素坐标排名（矩形框），便于做可视化位置分析。"),
 "postback_url": E("Your endpoint that DataForSEO calls with the completed task results once the task finishes.",
                   "任务完成后 DataForSEO 回调推送结果的你方接收端点。"),
 "pingback_url": E("Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload.",
                   "任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。"),
 "postback_data": E("Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed.",
                    "推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。"),
 "tag": E("Your own identifier echoed back with the task, useful for correlating results with your records.",
          "随任务回显的你方自定义标识，便于将结果与你方记录关联。"),
 "priority": E("Execution priority of the task; higher priority is processed sooner at a higher price.",
               "任务的执行优先级；更高优先级处理更快、价格更高。"),
 "browser_screen_width": E("Custom browser viewport width, in pixels, used when rendering the SERP for rectangle calculations.",
                           "渲染 SERP 以计算矩形框时使用的自定义浏览器视口宽度，单位像素。"),
 "browser_screen_height": E("Custom browser viewport height, in pixels, used when rendering the SERP for rectangle calculations.",
                            "渲染 SERP 以计算矩形框时使用的自定义浏览器视口高度，单位像素。"),
 "browser_screen_resolution_ratio": E("Device pixel ratio applied to the rendering viewport when computing rectangles.",
                                      "计算矩形框时应用于渲染视口的设备像素比。"),
 "min_rating": E("Lower bound on the place rating; results with a rating below this value are filtered out.",
                 "地点评分的下限；评分低于该值的结果会被过滤掉。"),
 "time_filter": E("Restricts results to a time window (e.g. open-now / specific hours); narrows the local results returned.",
                  "将结果限定在某时间窗口（如当前营业/特定时段），收窄返回的本地结果。"),
 "client": E("Autocomplete source client to emulate, such as `chrome`, `chrome-omni`, `gws-wiz`, `safari`, `firefox`, `img`, or `youtube`; each client returns a different suggestion set.",
             "要模拟的自动补全来源客户端，如 `chrome`、`chrome-omni`、`gws-wiz`、`safari`、`firefox`、`img` 或 `youtube`；不同客户端返回的建议集合不同。"),
 "image_url": E("Publicly accessible URL of the image to search with; Google returns results based on this image.",
                "用于搜索的可公开访问图片 URL；Google 基于该图片返回结果。"),
 "last_updated": E("Filter datasets by how recently they were updated, expressed as a relative window such as `1m`, `1y`, or `3y`.",
                   "按数据集的最近更新时间筛选，使用相对时间窗口表示，如 `1m`、`1y`、`3y`。"),
 "file_formats": E("Filter datasets by file format, such as `other`, `archive`, `text`, `image`, `document`, or `tabular`.",
                   "按文件格式筛选数据集，如 `other`、`archive`、`text`、`image`、`document` 或 `tabular`。"),
 "usage_rights": E("Filter datasets by usage rights, such as `commercial` or `noncommercial`.",
                   "按使用权限筛选数据集，如 `commercial` 或 `noncommercial`。"),
 "dataset_id": E("Identifier of the dataset to look up; find it in the dataset URL or in a Google Dataset Search result.",
                 "要查询的数据集标识；可在数据集 URL 或 Google 数据集搜索结果中找到。"),
 "advertiser_ids": E("Advertiser identifiers whose ads to retrieve; required when `target` is not provided.",
                     "要检索其广告的广告主标识；未提供 `target` 时必填。"),
 "target": E("Domain name associated with an advertiser account whose ads to retrieve; required when `advertiser_ids` is not provided.",
             "与某广告主账户关联的域名，用于检索其广告；未提供 `advertiser_ids` 时必填。"),
 "market_type": E("Which Google Finance Markets section to load (e.g. indexes, most-active, gainers/losers), selecting the market view to scrape.",
                  "要加载的 Google Finance Markets 板块（如指数、最活跃、涨跌幅榜），用于选择要抓取的行情视图。"),
 "window": E("Time window of the price graph for the quote, controlling the historical range shown.",
             "报价价格走势图的时间窗口，控制展示的历史区间。"),
}
# context override: in finance/quote keyword is a ticker symbol
REQ_BY_PATH = {
 ("post_dataforseo_serp_google_finance_quote_live_html", "keyword"): E(
   "Ticker or stock symbol to quote (e.g. `AAPL`); the SERP is built around this symbol.",
   "要查询行情的股票代码（如 `AAPL`）；SERP 围绕该代码构建。"),
 ("post_dataforseo_serp_google_dataset_search_task_post", "keyword"): E(
   "Search term used to find matching datasets.",
   "用于查找匹配数据集的搜索词。"),
 ("post_dataforseo_serp_google_dataset_search_live_advanced", "keyword"): E(
   "Search term used to find matching datasets.",
   "用于查找匹配数据集的搜索词。"),
 ("post_dataforseo_serp_google_autocomplete_task_post", "keyword"): E(
   "Seed term to fetch autocomplete suggestions for.",
   "用于获取自动补全建议的种子词。"),
 ("post_dataforseo_serp_google_autocomplete_live_advanced", "keyword"): E(
   "Seed term to fetch autocomplete suggestions for.",
   "用于获取自动补全建议的种子词。"),
 ("post_dataforseo_serp_google_ads_advertisers_task_post", "keyword"): E(
   "Search term used to find matching advertisers.",
   "用于查找匹配广告主的搜索词。"),
}

# ===========================================================================
# Response fields. Keyed by the literal dotpath suffix (with [] preserved).
# These are shared across all ops with identical meaning.
# ===========================================================================
RESP = {
 # top-level envelope
 "version": E("API version string that produced this response.",
              "生成本响应的 API 版本号。"),
 "status_code": E("Overall response status code; check it before reading the payload.",
                  "本次响应的总体状态码；读取数据前应先检查。"),
 "status_message": E("Human-readable message accompanying the overall status code.",
                     "与总体状态码对应的可读说明文字。"),
 "time": E("Server-side execution time of the request, in seconds.",
           "本次请求的服务端执行耗时，单位秒。"),
 "cost": E("Total billed cost of this response across all tasks, in USD.",
           "本响应所有任务的合计计费金额，单位美元。"),
 "tasks_count": E("Number of task entries contained in the `tasks` array.",
                  "`tasks` 数组中包含的任务条目数量。"),
 "tasks_error": E("How many tasks finished with an error; if non-zero, inspect each task's own status fields.",
                  "以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。"),
 "tasks": E("List of task objects; one entry per task in the request.",
            "任务对象列表，请求中的每个任务对应一个条目。"),
 # per-task wrapper
 "tasks[].id": E("UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint.",
                 "该任务的 UUID；在对应 task_get 端点取该任务结果时复用。"),
 "tasks[].status_code": E("Per-task status code; check it to tell whether this individual task succeeded.",
                          "单个任务的状态码，用于判断该任务是否成功。"),
 "tasks[].status_message": E("Human-readable message for this task's status code.",
                             "该任务状态码对应的可读说明文字。"),
 "tasks[].time": E("Server-side execution time spent on this task, in seconds.",
                   "该任务的服务端执行耗时，单位秒。"),
 "tasks[].cost": E("Billed cost attributed to this task, in USD.",
                   "归属于该任务的计费金额，单位美元。"),
 "tasks[].result_count": E("Number of entries in this task's `result` array.",
                           "该任务 `result` 数组中的条目数量。"),
 "tasks[].path": E("Endpoint path segments called to create this task; echoes the request routing.",
                   "创建该任务时调用的端点路径分段，回显请求路由。"),
 "tasks[].data": E("Echo of the request parameters used to create this task, for traceability.",
                   "回显创建该任务所用的请求参数，便于追溯。"),
 "tasks[].result": E("Result payload for this task; the actual SERP data is nested inside.",
                     "该任务的结果载荷，实际的 SERP 数据嵌套于内。"),
 # result[] common item-level fields (ai_mode advanced)
 "tasks[].result[].keyword": E("Keyword echoed from the POST request that this result corresponds to.",
                               "对应本结果、回显自 POST 请求的关键词。"),
 "tasks[].result[].type": E("Search type of this result block, echoed from the request.",
                            "本结果块的搜索类型，回显自请求。"),
 "tasks[].result[].se_domain": E("Search-engine domain used for this result (e.g. `google.com`).",
                                 "本结果使用的搜索引擎域名（如 `google.com`）。"),
 "tasks[].result[].location_code": E("Location code applied to this result, echoed from the request.",
                                     "应用于本结果的地区代码，回显自请求。"),
 "tasks[].result[].language_code": E("Language code applied to this result, echoed from the request.",
                                     "应用于本结果的语言代码，回显自请求。"),
 "tasks[].result[].check_url": E("Direct Google URL reproducing this SERP with the same refinement parameters; open it to verify the result.",
                                 "可复现本 SERP 且带相同细化参数的 Google 直达 URL；打开可核对结果。"),
 "tasks[].result[].item_types": E("List of element types present in this SERP (e.g. organic, ai_overview), useful to know what `items` contains.",
                                  "本 SERP 中出现的元素类型列表（如 organic、ai_overview），可据此了解 `items` 的内容。"),
 "tasks[].result[].se_results_count": E("Total number of results Google reports for the query.",
                                        "Google 为该查询报告的结果总数。"),
 "tasks[].result[].items_count": E("Number of elements returned in this result's `items` array.",
                                   "本结果 `items` 数组中返回的元素数量。"),
 "tasks[].result[].items": E("Array of SERP elements parsed for this result.",
                             "本结果解析出的 SERP 元素数组。"),
 "tasks[].result[].items[].type": E("Type of this SERP element (e.g. `ai_overview`), determining its other fields.",
                                    "该 SERP 元素的类型（如 `ai_overview`），决定其其余字段。"),
 "tasks[].result[].items[].markdown": E("Content of this element rendered as Markdown.",
                                        "该元素以 Markdown 渲染的内容。"),
 "tasks[].result[].items[].html": E("Raw HTML content of this element.",
                                    "该元素的原始 HTML 内容。"),
 # html task_get result chain
 "tasks[].result[].items[].html": E("Raw HTML content of this element.",
                                    "该元素的原始 HTML 内容。"),
 # tasks_ready completed-task references
 "tasks[].result[].id": E("Task id of the completed task, ready to be collected.",
                          "已完成、可收取任务的 task id。"),
 "tasks[].result[].se": E("Search engine specified when the task was posted.",
                          "提交任务时指定的搜索引擎。"),
 "tasks[].result[].se_type": E("Type of search-engine SERP the task targets (e.g. organic, news).",
                               "任务所针对的搜索引擎 SERP 类型（如 organic、news）。"),
 "tasks[].result[].date_posted": E("Timestamp when the task was posted, in UTC.",
                                   "任务提交的时间戳，UTC 格式。"),
 "tasks[].result[].tag": E("User-defined tag echoed for the completed task.",
                           "为已完成任务回显的用户自定义标签。"),
 "tasks[].result[].endpoint_advanced": E("Relative URL to call to collect this task's advanced results.",
                                         "用于收取该任务高级结果的相对 URL。"),
 "tasks[].result[].endpoint_regular": E("Relative URL to call to collect this task's regular results.",
                                        "用于收取该任务常规结果的相对 URL。"),
 "tasks[].result[].endpoint_html": E("Relative URL to call to collect this task's HTML results.",
                                     "用于收取该任务 HTML 结果的相对 URL。"),
 # ads_advertisers locations
 "tasks[].result[].location_name": E("Human-readable name of the supported location.",
                                     "受支持地区的可读名称。"),
 "tasks[].result[].country_iso_code": E("ISO country code of the location.",
                                        "该地区的 ISO 国家代码。"),
 "tasks[].result[].location_type": E("Type/level of the location (e.g. country, region, city).",
                                     "地区的类型/层级（如国家、地区、城市）。"),
}

# ===========================================================================
# Assembler
# ===========================================================================
def lookup_req(op, dp):
    if (op, dp) in REQ_BY_PATH:
        return REQ_BY_PATH[(op, dp)]
    leaf = dp.split(".")[-1]
    return REQ.get(leaf)


def lookup_resp(op, dp):
    return RESP.get(dp)


def build():
    missing = []
    content = {"operations": {}, "fields": {}}
    for op, d in INV.items():
        opmeta = OPS.get(op)
        if not opmeta or not opmeta.get("heading_zh"):
            missing.append(("OP", op)); continue
        content["operations"][op] = {k: opmeta[k] for k in ("heading_zh", "desc_en", "title_zh")}
        # rename title_zh -> description_zh for operation level
        content["operations"][op] = {
            "heading_zh": opmeta["heading_zh"],
            "desc_en": opmeta["desc_en"],
            "description_zh": opmeta["title_zh"],
        }
        fblock = {"parameters": {}, "request": {}, "response": {}}
        for pn in d.get("parameters", []):
            e = PARAMS.get(pn)
            if not e:
                missing.append((op, "param", pn)); continue
            fblock["parameters"][pn] = {"desc_en": e["desc_en"], "title_zh": e["title_zh"]}
        for dp in d["request"]:
            e = lookup_req(op, dp)
            if not e:
                missing.append((op, "req", dp)); continue
            fblock["request"][dp] = {"desc_en": e["desc_en"], "title_zh": e["title_zh"]}
        for code, paths in d["response"].items():
            cm = {}
            for dp in paths:
                e = lookup_resp(op, dp)
                if not e:
                    missing.append((op, "resp", code, dp)); continue
                cm[dp] = {"desc_en": e["desc_en"], "title_zh": e["title_zh"]}
            fblock["response"][code] = cm
        content["fields"][op] = fblock

    if missing:
        sys.stderr.write("UNCOVERED (%d):\n" % len(missing))
        for m in missing[:120]:
            sys.stderr.write("  " + " | ".join(map(str, m)) + "\n")
        sys.exit("ABORT: author missing entries first")

    out = "/home/mira/files/aisa-docs-voyager/ws-v2/dataforseo/parts/google_2.content.json"
    json.dump(content, open(out, "w"), ensure_ascii=False, indent=2)
    nf = sum(len(b["parameters"]) + len(b["request"]) + sum(len(c) for c in b["response"].values())
             for b in content["fields"].values())
    print("WROTE", out)
    print("ops=%d fields=%d" % (len(content["operations"]), nf))


build()
