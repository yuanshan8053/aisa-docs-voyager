#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assembler for on_page.content.json.

The doc TEXT below is hand-authored by the LLM per METHODOLOGY.md (one entry per
distinct semantic field). This script only ROUTES my authored text onto the exact
dotpaths the completeness gate requires (read from /tmp/onpage_inv.json). It does
NOT generate text by template: every dotpath must resolve to a hand-written entry,
otherwise the build aborts (guard) — forcing me to author, never to pad.
"""
import json
import sys

INV = json.load(open("/tmp/onpage_inv.json"))

# ---------------------------------------------------------------------------
# Operation-level metadata (hand-authored)
# ---------------------------------------------------------------------------
OPS = {
 "post_dataforseo_on_page_task_post": {
  "heading_zh": "提交 OnPage 站点抓取任务 post_dataforseo_on_page_task_post",
  "desc_en": "Queue an OnPage crawl task for a target website; the response returns a task id used by all other OnPage endpoints (summary, pages, links, resources, etc.) to read the crawled data once the crawl completes.",
  "description_zh": "为目标站点提交一个 OnPage 抓取任务；响应返回 task id，抓取完成后用它在其它 OnPage 端点（summary、pages、links、resources 等）读取抓取结果。"},
 "get_dataforseo_on_page_tasks_ready": {
  "heading_zh": "列出可收取的 OnPage 任务 get_dataforseo_on_page_tasks_ready",
  "desc_en": "List OnPage crawl tasks that have finished and are ready to be collected via the matching summary/pages endpoints.",
  "description_zh": "列出已完成、可通过对应 summary/pages 端点收取的 OnPage 抓取任务。"},
 "get_dataforseo_on_page_summary_id": {
  "heading_zh": "获取 OnPage 抓取汇总 get_dataforseo_on_page_summary_id",
  "desc_en": "Return the overall crawl summary for a task id: crawl progress, aggregate page metrics, and the site-wide checks breakdown.",
  "description_zh": "按 task id 返回整体抓取汇总：抓取进度、聚合页面指标与全站检查项统计。"},
 "post_dataforseo_on_page_force_stop": {
  "heading_zh": "强制停止 OnPage 抓取 post_dataforseo_on_page_force_stop",
  "desc_en": "Force-stop an in-progress OnPage crawl by task id; already crawled pages remain available for retrieval.",
  "description_zh": "按 task id 强制停止进行中的 OnPage 抓取；已抓取的页面仍可读取。"},
 "post_dataforseo_on_page_pages": {  # placeholder, not in slice
  "heading_zh": "", "desc_en": "", "description_zh": ""},
 "post_dataforseo_on_page_links": {
  "heading_zh": "获取页面链接 post_dataforseo_on_page_links",
  "desc_en": "Return the internal and external links discovered during the crawl for a task id, with per-link attributes, anchor text, and broken-link status.",
  "description_zh": "返回某 task id 抓取过程中发现的内外部链接，含每条链接的属性、锚文本与失效状态。"},
 "post_dataforseo_on_page_resources": {
  "heading_zh": "获取页面资源 post_dataforseo_on_page_resources",
  "desc_en": "Return the resources (images, scripts, stylesheets, etc.) found during the crawl for a task id, with load timing, size, and per-resource checks.",
  "description_zh": "返回某 task id 抓取过程中发现的资源（图片、脚本、样式表等），含加载耗时、体积与逐资源检查。"},
 "post_dataforseo_on_page_duplicate_tags": {
  "heading_zh": "获取重复标签页面 post_dataforseo_on_page_duplicate_tags",
  "desc_en": "Return groups of pages that share duplicate title or meta description tags for a task id, to help locate cannibalization and SEO tag issues.",
  "description_zh": "返回某 task id 中存在重复 title 或 meta description 标签的页面分组，用于定位标签重复与 SEO 问题。"},
 "post_dataforseo_on_page_duplicate_content": {
  "heading_zh": "获取重复内容页面 post_dataforseo_on_page_duplicate_content",
  "desc_en": "Return pages whose body content is highly similar to a reference page for a task id, ranked by similarity, to surface duplicate-content risks.",
  "description_zh": "返回某 task id 中与参考页正文高度相似的页面，按相似度排序，用于发现重复内容风险。"},
 "post_dataforseo_on_page_keyword_density": {
  "heading_zh": "获取关键词密度 post_dataforseo_on_page_keyword_density",
  "desc_en": "Return keyword-density statistics (single words or n-grams) computed from crawled pages for a task id.",
  "description_zh": "返回某 task id 抓取页面计算出的关键词密度统计（单词或 n-gram）。"},
 "post_dataforseo_on_page_raw_html": {
  "heading_zh": "获取页面原始 HTML post_dataforseo_on_page_raw_html",
  "desc_en": "Return the stored raw HTML of a crawled page for a task id (requires store_raw_html to have been enabled on the task).",
  "description_zh": "返回某 task id 已抓取页面的原始 HTML（需在任务上启用 store_raw_html）。"},
 "post_dataforseo_on_page_content_parsing": {
  "heading_zh": "解析已抓取页面内容 post_dataforseo_on_page_content_parsing",
  "desc_en": "Parse a previously crawled page (by task id and url) into structured content blocks: topics, primary/secondary content, tables, ratings, offers, and contacts.",
  "description_zh": "对此前已抓取的页面（按 task id 与 url）进行结构化内容解析：主题、主/次要内容、表格、评分、报价与联系方式。"},
 "post_dataforseo_on_page_content_parsing_live": {
  "heading_zh": "实时解析页面内容 post_dataforseo_on_page_content_parsing_live",
  "desc_en": "Crawl a single url on the fly and return its parsed, structured content in the same response, with no separate OnPage task to queue.",
  "description_zh": "即时抓取单个 url，并在同一响应中返回其结构化解析内容，无需另行排队 OnPage 任务。"},
 "post_dataforseo_on_page_microdata": {
  "heading_zh": "获取页面结构化数据 post_dataforseo_on_page_microdata",
  "desc_en": "Extract and validate the structured-data markup (Microdata / JSON-LD / schema.org) found on a crawled page for a task id and url.",
  "description_zh": "提取并校验某 task id 与 url 的已抓取页面上的结构化数据标记（Microdata / JSON-LD / schema.org）。"},
 "post_dataforseo_on_page_non_indexable": {
  "heading_zh": "获取不可索引页面 post_dataforseo_on_page_non_indexable",
  "desc_en": "Return pages that search engines cannot index for a task id, together with the reason each page is blocked from indexing.",
  "description_zh": "返回某 task id 中搜索引擎无法索引的页面，并给出每页被阻止索引的原因。"},
 "post_dataforseo_on_page_waterfall": {
  "heading_zh": "获取页面加载瀑布图 post_dataforseo_on_page_waterfall",
  "desc_en": "Return the per-resource load-timing waterfall for a single crawled page (by task id and url), exposing how each resource contributed to total load time.",
  "description_zh": "返回某单页（按 task id 与 url）的逐资源加载时序瀑布，展现各资源对总加载耗时的贡献。"},
 "post_dataforseo_on_page_uncrawlable_resources": {
  "heading_zh": "获取不可抓取资源 post_dataforseo_on_page_uncrawlable_resources",
  "desc_en": "Return resources the crawler failed to fetch for a task id, with the error details for each one.",
  "description_zh": "返回某 task id 中抓取器未能获取的资源，并附每项的错误详情。"},
 "post_dataforseo_on_page_page_screenshot": {
  "heading_zh": "抓取页面截图 post_dataforseo_on_page_page_screenshot",
  "desc_en": "Capture a screenshot of a url in a real browser and return its image location, with controls for viewport size, user agent, and full-page capture.",
  "description_zh": "在真实浏览器中对某 url 截图并返回图片地址，可控制视口尺寸、User-Agent 与整页截图。"},
 "get_dataforseo_on_page_available_filters": {
  "heading_zh": "列出可用过滤字段 get_dataforseo_on_page_available_filters",
  "desc_en": "Return the reference list of fields and operators usable in the filters parameter of OnPage endpoints.",
  "description_zh": "返回 OnPage 端点 filters 参数中可用的字段与运算符参考列表。"},
 "post_dataforseo_on_page_lighthouse_task_post": {
  "heading_zh": "提交 Lighthouse 审计任务 post_dataforseo_on_page_lighthouse_task_post",
  "desc_en": "Queue a Google Lighthouse audit for a url; the response returns a task id you later fetch via the matching lighthouse task_get endpoint. Optionally set pingback_url to be notified on completion.",
  "description_zh": "为某 url 提交 Google Lighthouse 审计任务；响应返回 task id，稍后通过对应的 lighthouse task_get 端点取回结果。可选地设置 pingback_url 以在完成时获得通知。"},
 "get_dataforseo_on_page_lighthouse_tasks_ready": {
  "heading_zh": "列出可收取的 Lighthouse 任务 get_dataforseo_on_page_lighthouse_tasks_ready",
  "desc_en": "List completed Lighthouse audit tasks that are ready to be collected via the lighthouse task_get endpoint.",
  "description_zh": "列出已完成、可通过 lighthouse task_get 端点收取的 Lighthouse 审计任务。"},
 "get_dataforseo_on_page_lighthouse_task_get_json_id": {
  "heading_zh": "获取 Lighthouse 审计结果 get_dataforseo_on_page_lighthouse_task_get_json_id",
  "desc_en": "Retrieve the full JSON report of a previously queued Lighthouse audit task by its task id.",
  "description_zh": "按 task id 取回此前排队的 Lighthouse 审计任务的完整 JSON 报告。"},
 "post_dataforseo_on_page_lighthouse_live_json": {
  "heading_zh": "实时运行 Lighthouse 审计 post_dataforseo_on_page_lighthouse_live_json",
  "desc_en": "Run a Google Lighthouse audit on a url synchronously and return the full JSON report in the same response, with no task to poll.",
  "description_zh": "对某 url 同步运行 Google Lighthouse 审计，并在同一响应中返回完整 JSON 报告，无需轮询任务。"},
 "get_dataforseo_on_page_lighthouse_audits": {
  "heading_zh": "列出 Lighthouse 审计项 get_dataforseo_on_page_lighthouse_audits",
  "desc_en": "Return the reference list of individual Lighthouse audit ids that can be requested via the audits parameter.",
  "description_zh": "返回可通过 audits 参数请求的 Lighthouse 单项审计 id 参考列表。"},
 "get_dataforseo_on_page_lighthouse_versions": {
  "heading_zh": "列出 Lighthouse 版本 get_dataforseo_on_page_lighthouse_versions",
  "desc_en": "Return the list of Lighthouse engine versions available to the version parameter.",
  "description_zh": "返回 version 参数可选的 Lighthouse 引擎版本列表。"},
 "get_dataforseo_on_page_lighthouse_languages": {
  "heading_zh": "列出 Lighthouse 语言 get_dataforseo_on_page_lighthouse_languages",
  "desc_en": "Return the languages supported for Lighthouse report localization via the language_name/language_code parameters.",
  "description_zh": "返回 Lighthouse 报告本地化支持的语言，对应 language_name/language_code 参数。"},
}

# ---------------------------------------------------------------------------
# Field text dictionary. Keyed primarily by leaf-name (the final dotpath segment)
# where meaning is identical regardless of nesting; full-dotpath keys override
# where context changes meaning. All text hand-authored.
# ---------------------------------------------------------------------------
def E(desc_en, title_zh, **kw):
    d = {"desc_en": desc_en, "title_zh": title_zh}
    d.update(kw)
    return d

# Response envelope + task wrapper (shared across all ops)
ENVELOPE = {
 "version": E("API version string that produced this response; useful when reporting issues.",
              "生成本响应的 API 版本号，反馈问题时可一并提供。"),
 "status_code": E("Overall response status code; check it before reading the payload and handle error cases.",
                  "本次响应的总体状态码；读取数据前应先检查并处理异常情况。"),
 "status_message": E("Human-readable message accompanying the overall status code.",
                     "与总体状态码对应的可读说明文字。"),
 "time": E("Server-side processing time for the request.",
           "本次请求的服务端处理耗时。"),
 "cost": E("Total billed cost of this response across all tasks, in USD.",
           "本响应所有任务的合计计费金额，单位美元。"),
 "tasks_count": E("Number of task entries contained in the tasks array.",
                  "tasks 数组中包含的任务条目数量。"),
 "tasks_error": E("How many tasks finished with an error; if non-zero, inspect each task's own status fields.",
                  "以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。"),
 "tasks": E("List of task results; one entry per task created by the request.",
            "任务结果列表，请求创建的每个任务对应一个条目。"),
 "tasks.id": E("Unique identifier (UUID) of this task; reuse it to fetch the task's data from other OnPage endpoints.",
               "该任务的唯一标识（UUID）；在其它 OnPage 端点读取该任务数据时复用。"),
 "tasks.status_code": E("Per-task status code; check it to tell whether this individual task succeeded.",
                        "单个任务的状态码，用于判断该任务是否成功。"),
 "tasks.status_message": E("Human-readable message for this task's status code.",
                           "该任务状态码对应的可读说明文字。"),
 "tasks.time": E("Server-side processing time spent on this task.",
                 "该任务的服务端处理耗时。"),
 "tasks.cost": E("Billed cost attributed to this task, in USD.",
                 "归属于该任务的计费金额，单位美元。"),
 "tasks.result_count": E("Number of entries in this task's result array.",
                         "该任务 result 数组中的条目数量。"),
 "tasks.path": E("Endpoint path segments that were called to create this task; echoes the request routing.",
                 "创建该任务时调用的端点路径分段，回显请求路由。"),
 "tasks.data": E("Echo of the request parameters used to create this task, for traceability.",
                 "回显创建该任务所用的请求参数，便于追溯。"),
 "tasks.result": E("Result payload for this task; the actual OnPage data is nested inside.",
                   "该任务的结果载荷，实际的 OnPage 数据嵌套于内。"),
}

# ---------------------------------------------------------------------------
# REQUEST parameters (hand-authored, keyed by leaf-name)
# ---------------------------------------------------------------------------
REQ = {
 "target": E("Domain of the website to crawl, without scheme or trailing slash (e.g. `example.com`).",
             "要抓取的网站域名，不含协议头与末尾斜杠（如 `example.com`）。"),
 "max_crawl_pages": E("Upper bound on how many pages the crawler will fetch for this task; the crawl stops once the limit is reached.",
                      "本任务抓取器最多抓取的页面数；达到上限即停止抓取。"),
 "start_url": E("First page the crawler visits; if omitted the crawl starts from the target home page.",
                "抓取器访问的首个页面；省略时从 target 首页开始抓取。"),
 "force_sitewide_checks": E("Run site-wide checks even when only a subset of pages is crawled.",
                            "即使仅抓取部分页面，也强制执行全站级检查。"),
 "priority_urls": E("URLs the crawler should fetch first, ahead of normal queue order.",
                    "抓取器应优先抓取、排在常规队列之前的 URL。"),
 "max_crawl_depth": E("Maximum link depth from the start page that the crawler will follow.",
                      "抓取器自起始页向下跟踪链接的最大层级深度。"),
 "crawl_delay": E("Delay the crawler waits between consecutive page requests, to ease load on the target server.",
                  "抓取器在连续页面请求之间等待的延迟，用于减轻目标服务器压力。"),
 "store_raw_html": E("Whether to keep each page's raw HTML so it can later be retrieved via the raw_html endpoint.",
                     "是否保留每页原始 HTML，以便之后通过 raw_html 端点取回。"),
 "enable_content_parsing": E("Whether to parse page content into structured blocks during the crawl, enabling the content_parsing endpoint.",
                             "是否在抓取时将页面内容解析为结构化块，从而启用 content_parsing 端点。"),
 "support_cookies": E("Whether the crawler accepts and sends cookies while crawling.",
                      "抓取过程中抓取器是否接受并发送 Cookie。"),
 "accept_language": E("Value sent in the crawler's Accept-Language header, controlling the language variant of fetched pages.",
                     "抓取器 Accept-Language 请求头的取值，控制所取页面的语言版本。"),
 "custom_robots_txt": E("Custom robots.txt content the crawler should obey instead of the site's own.",
                        "抓取器应遵循的自定义 robots.txt 内容，替代站点自身的版本。"),
 "robots_txt_merge_mode": E("How custom_robots_txt combines with the site's robots.txt: enum values select merge vs. override behavior.",
                            "custom_robots_txt 与站点 robots.txt 的结合方式：枚举值选择合并或覆盖行为。"),
 "custom_user_agent": E("User-Agent string the crawler presents to the target server.",
                        "抓取器向目标服务器呈现的 User-Agent 字符串。"),
 "browser_preset": E("Named device preset that sets viewport and rendering defaults; enum values map to common device profiles.",
                     "命名设备预设，设定视口与渲染默认值；枚举值对应常见设备配置。"),
 "browser_screen_width": E("Viewport width in pixels used when rendering the page in a browser.",
                           "在浏览器中渲染页面时使用的视口宽度，单位像素。"),
 "browser_screen_height": E("Viewport height in pixels used when rendering the page in a browser.",
                            "在浏览器中渲染页面时使用的视口高度，单位像素。"),
 "browser_screen_scale_factor": E("Device pixel ratio applied to the rendering viewport.",
                                  "应用于渲染视口的设备像素比。"),
 "respect_sitemap": E("Whether the crawler uses the site's sitemap to discover pages.",
                      "抓取器是否依据站点 sitemap 发现页面。"),
 "custom_sitemap": E("URL of a sitemap to crawl instead of auto-discovering the site's own.",
                     "指定要抓取的 sitemap 地址，替代自动发现的站点 sitemap。"),
 "crawl_sitemap_only": E("Restrict the crawl to URLs listed in the sitemap, skipping link discovery.",
                         "仅抓取 sitemap 中列出的 URL，跳过链接发现。"),
 "load_resources": E("Whether the crawler also fetches page resources (images, scripts, stylesheets) for analysis.",
                     "抓取器是否同时获取页面资源（图片、脚本、样式表）以供分析。"),
 "enable_www_redirect_check": E("Whether to test the www / non-www redirect configuration of the site.",
                                "是否检测站点 www 与非 www 之间的重定向配置。"),
 "enable_javascript": E("Whether to execute JavaScript when rendering pages, capturing client-rendered content.",
                        "渲染页面时是否执行 JavaScript，以捕获客户端渲染内容。"),
 "enable_xhr": E("Whether to capture XHR/fetch requests made by the page during rendering.",
                 "是否捕获页面渲染过程中发起的 XHR/fetch 请求。"),
 "enable_browser_rendering": E("Whether to render pages in a real browser instead of a plain HTTP fetch.",
                               "是否在真实浏览器中渲染页面，而非纯 HTTP 抓取。"),
 "disable_cookie_popup": E("Whether to suppress cookie-consent popups before capturing the page.",
                           "捕获页面前是否屏蔽 Cookie 同意弹窗。"),
 "custom_js": E("Custom JavaScript executed on each page after load; its output is returned in custom_js_response.",
                "在每页加载后执行的自定义 JavaScript，其输出返回于 custom_js_response。"),
 "validate_micromarkup": E("Whether to validate structured-data markup on crawled pages.",
                           "是否校验抓取页面上的结构化数据标记。"),
 "allow_subdomains": E("Whether the crawler may follow links into subdomains of the target.",
                       "抓取器是否可跟踪进入 target 子域名的链接。"),
 "allowed_subdomains": E("Explicit list of subdomains the crawler is permitted to enter.",
                         "明确允许抓取器进入的子域名列表。"),
 "disallowed_subdomains": E("List of subdomains the crawler must not enter.",
                            "禁止抓取器进入的子域名列表。"),
 "check_spell": E("Whether to run spell-checking on page text content.",
                  "是否对页面文本内容执行拼写检查。"),
 "check_spell_language": E("Language used for spell-checking, by language code.",
                           "拼写检查使用的语言，以语言代码表示。"),
 "check_spell_exceptions": E("Words to exclude from spell-checking (e.g. brand names).",
                             "拼写检查时需排除的词（如品牌名）。"),
 "calculate_keyword_density": E("Whether to compute keyword-density statistics during the crawl.",
                                "抓取时是否计算关键词密度统计。"),
 "checks_threshold": E("Custom thresholds overriding the defaults used to flag on-page checks.",
                       "覆盖默认值的自定义阈值，用于触发各项页面检查。"),
 "disable_sitewide_checks": E("Site-wide check names to skip for this task.",
                              "本任务需跳过的全站级检查项名称。"),
 "disable_page_checks": E("Per-page check names to skip for this task.",
                          "本任务需跳过的页面级检查项名称。"),
 "switch_pool": E("Whether to retry from a different IP pool if the target blocks the initial request.",
                  "当目标拦截首次请求时，是否切换到其它 IP 池重试。"),
 "return_despite_timeout": E("Whether to return partial results when a page exceeds the load timeout instead of failing it.",
                             "当页面超过加载超时时，是否返回部分结果而非判为失败。"),
 "tag": E("Free-text label you attach to the task to identify it in later listings and callbacks.",
          "为任务附加的自由文本标签，便于在后续列表与回调中识别。"),
 "pingback_url": E("URL the API calls when the task completes, so you can collect results without polling.",
                   "任务完成时 API 回调的 URL，使你无需轮询即可收取结果。"),
 "postback_url": E("URL the API posts the task result to upon completion.",
                   "任务完成时 API 推送结果所到的 URL。"),
 # OnPage data-read endpoints
 "id": E("Task id returned by task_post; identifies which crawl's data to read or act on.",
         "task_post 返回的任务 id，标明要读取或操作哪次抓取的数据。"),
 "url": E("Page URL to act on; for read endpoints it selects a single crawled page, for live endpoints it is the page to fetch now.",
          "要操作的页面 URL；读取端点用它选定单个已抓取页面，实时端点用它指定当前要抓取的页面。"),
 "limit": E("Maximum number of items to return in this response.",
            "本响应最多返回的条目数量。"),
 "offset": E("Number of leading items to skip, for paging through results.",
             "跳过的起始条目数，用于分页浏览结果。"),
 "filters": E("Array of conditions used to narrow the returned items; usable fields are listed by available_filters.",
              "用于筛选返回条目的条件数组；可用字段见 available_filters。"),
 "order_by": E("Sorting rules applied to the returned items, as field/direction pairs.",
               "应用于返回条目的排序规则，以字段/方向成对给出。"),
 "search_after_token": E("Cursor from a previous response used to fetch the next page of items.",
                         "上一响应返回的游标，用于取下一页条目。"),
 "similarity": E("Minimum content-similarity threshold for a page to be reported as duplicate.",
                 "判定页面为重复内容所需的最小相似度阈值。"),
 "type": E("Which tag to compare for duplicates; enum selects title vs. meta description.",
           "用于比较重复的标签类型；枚举可选 title 或 meta description。"),
 "accumulator": E("How duplicate groups are accumulated across pages; enum value controls grouping behavior.",
                  "跨页面累积重复分组的方式；枚举值控制分组行为。"),
 "keyword_length": E("Number of words per phrase to measure (1 for single words, 2+ for n-grams).",
                     "测量的每个短语词数（1 为单词，2 及以上为 n-gram）。"),
 "page_from": E("Filter links by their source page URL.",
                "按来源页面 URL 过滤链接。"),
 "page_to": E("Filter links by their destination page URL.",
              "按目标页面 URL 过滤链接。"),
 "relevant_pages_filters": E("Additional filters applied to the pages a resource appears on.",
                             "对资源所出现页面额外应用的过滤条件。"),
 "markdown_view": E("Whether to also return the parsed page content rendered as Markdown.",
                    "是否同时返回以 Markdown 渲染的解析页面内容。"),
 "ip_pool_for_scan": E("Geographic IP pool to crawl from; enum selects the source region.",
                       "用于抓取的地理 IP 池；枚举选择来源地区。"),
 "disable_cookie_popup_": E("", ""),  # unused
 # Lighthouse params
 "for_mobile": E("Whether to run the Lighthouse audit emulating a mobile device.",
                 "是否以模拟移动设备的方式运行 Lighthouse 审计。"),
 "categories": E("Lighthouse category ids to audit (e.g. performance, accessibility, seo).",
                 "要审计的 Lighthouse 类别 id（如 performance、accessibility、seo）。"),
 "audits": E("Specific Lighthouse audit ids to run instead of full categories; values from lighthouse/audits.",
             "要运行的具体 Lighthouse 单项审计 id，替代整类审计；取值见 lighthouse/audits。"),
 "version": E("Lighthouse engine version to use; values from lighthouse/versions.",
              "要使用的 Lighthouse 引擎版本；取值见 lighthouse/versions。"),
 "language_name": E("Human-readable language for the Lighthouse report; values from lighthouse/languages.",
                    "Lighthouse 报告的可读语言名称；取值见 lighthouse/languages。"),
 "language_code": E("Language code for the Lighthouse report; values from lighthouse/languages.",
                    "Lighthouse 报告的语言代码；取值见 lighthouse/languages。"),
 "full_page_screenshot": E("Whether to capture the entire scrollable page rather than just the viewport.",
                           "是否截取整张可滚动页面，而非仅视口可见区域。"),
}

# ---------------------------------------------------------------------------
# RESPONSE field dictionary (hand-authored).
# Keyed by leaf-name; full-dotpath overrides where context changes meaning.
# RESP_BY_PATH takes priority; otherwise RESP_BY_LEAF (final segment) applies.
# ---------------------------------------------------------------------------
RESP_BY_LEAF = {
 # result-level scalars
 "crawl_progress": E("Crawl lifecycle state of the task; tells whether the crawl is in progress or finished.",
                     "任务的抓取生命周期状态，标明抓取进行中还是已完成。"),
 "items_count": E("Number of items returned in this result page.",
                  "本结果页返回的条目数量。"),
 "total_items_count": E("Total number of items matching the query across all pages.",
                        "跨所有页面匹配查询的条目总数。"),
 "total_count": E("Total number of matching records available.",
                  "可用的匹配记录总数。"),
 "pages_count": E("Total number of crawled pages represented in this result.",
                  "本结果涵盖的已抓取页面总数。"),
 "total_pages_count": E("Total number of pages discovered for the task.",
                        "该任务发现的页面总数。"),
 "items": E("Array of result records for this endpoint; structure depends on the endpoint called.",
            "本端点的结果记录数组，结构因所调用端点而异。"),
 "pages": E("Array of crawled-page records.",
            "已抓取页面记录数组。"),
 "page": E("A single crawled-page record with its checks, meta, timing, and metrics.",
           "单个已抓取页面记录，含其检查项、meta、时序与各项指标。"),
 "language_code": E("Detected or requested content language as a code.",
                    "检测到或请求的内容语言代码。"),
 "language_name": E("Detected or requested content language name.",
                    "检测到或请求的内容语言名称。"),
 "target": E("Domain that was crawled for this task.",
             "本任务所抓取的域名。"),
 "reason": E("Explanation of why the page is non-indexable or why the resource is uncrawlable.",
             "页面不可索引或资源不可抓取的原因说明。"),
 "available_versions": E("List of selectable engine/report versions.",
                         "可选的引擎/报告版本列表。"),
 "default": E("The value applied when the corresponding option is not specified.",
              "未指定对应选项时所采用的默认值。"),
 "date_posted": E("Timestamp when the task was submitted.",
                  "任务提交的时间戳。"),
 "endpoint_json": E("Path of the JSON endpoint to call to fetch this task's result.",
                    "用于取回该任务结果的 JSON 端点路径。"),
 "error_message": E("Error description when the task or page failed.",
                    "任务或页面失败时的错误描述。"),
 # crawl_status block
 "max_crawl_pages": E("Page-count limit configured for this crawl.",
                      "本次抓取所配置的页面数上限。"),
 "pages_crawled": E("Number of pages fetched so far.",
                    "目前已抓取的页面数。"),
 "pages_in_queue": E("Number of pages still waiting to be crawled.",
                     "仍在排队等待抓取的页面数。"),
 # keyword density
 "keyword": E("The word or phrase the density statistic is measured for.",
              "密度统计所针对的词或短语。"),
 "frequency": E("How many times the keyword occurs in the analyzed text.",
                "关键词在被分析文本中出现的次数。"),
 "density": E("Share of the keyword among all words in the text, as a ratio.",
              "关键词在文本全部词中的占比。"),
 # links
 "type": E("Kind of the record (e.g. link, resource, or content type), as classified by the crawler.",
           "记录的类别（如 link、resource 或内容类型），由抓取器分类。"),
 "domain_from": E("Domain of the page the link originates from.",
                  "链接来源页面所属的域名。"),
 "domain_to": E("Domain the link points to.",
                "链接指向的域名。"),
 "page_from": E("URL of the page the link originates from.",
                "链接来源页面的 URL。"),
 "page_to": E("URL the link points to.",
              "链接指向的 URL。"),
 "link_from": E("Source URL of the link.",
                "链接的来源 URL。"),
 "link_to": E("Destination URL of the link.",
              "链接的目标 URL。"),
 "link_attribute": E("rel attribute carried by the link (e.g. nofollow, sponsored).",
                     "链接携带的 rel 属性（如 nofollow、sponsored）。"),
 "dofollow": E("Whether the link passes link equity (true) or is nofollow (false).",
               "链接是否传递权重（true）或为 nofollow（false）。"),
 "direction": E("Whether the link is internal or external relative to the crawled site.",
                "链接相对被抓取站点是内部还是外部。"),
 "is_broken": E("Whether the link or resource target returns an error / is unreachable.",
                "链接或资源目标是否返回错误或无法访问。"),
 "is_link_relation_conflict": E("Whether conflicting rel relations were declared for this link.",
                                "该链接是否声明了相互冲突的 rel 关系。"),
 "page_from_scheme": E("URL scheme (http/https) of the source page.",
                       "来源页面的 URL 协议（http/https）。"),
 "page_to_scheme": E("URL scheme (http/https) of the destination page.",
                     "目标页面的 URL 协议（http/https）。"),
 "page_to_status_code": E("HTTP status code returned by the destination page.",
                          "目标页面返回的 HTTP 状态码。"),
 "image": E("Whether the link is an image link.",
            "该链接是否为图片链接。"),
 "image_alt": E("Alt text of the linked image.",
                "被链接图片的 alt 文本。"),
 "image_src": E("Source URL of the linked image.",
                "被链接图片的源 URL。"),
 "text": E("Text content associated with the record (anchor text, parsed text, or HTML snippet).",
           "与记录关联的文本内容（锚文本、解析文本或 HTML 片段）。"),
 "hreflang": E("hreflang value declared for the link, indicating target language/region.",
               "为该链接声明的 hreflang 值，标明目标语言/地区。"),
 "is_valid_hreflang": E("Whether the declared hreflang value is syntactically valid.",
                        "所声明的 hreflang 值在语法上是否有效。"),
 # resources / waterfall
 "resource_type": E("Type of the resource (e.g. image, script, stylesheet, font).",
                    "资源类型（如 image、script、stylesheet、font）。"),
 "resources": E("Per-resource records loaded by the page, with timing and metadata.",
                "页面加载的逐资源记录，含时序与元数据。"),
 "initiator": E("URL or component that triggered loading of this resource.",
                "触发加载该资源的 URL 或组件。"),
 "is_render_blocking": E("Whether the resource blocks rendering until it finishes loading.",
                         "该资源是否在加载完成前阻塞渲染。"),
 "size": E("Uncompressed size of the resource or page, in bytes.",
           "资源或页面的未压缩大小，单位字节。"),
 "encoded_size": E("Transferred (compressed) size, in bytes.",
                   "传输时的（压缩后）大小，单位字节。"),
 "total_transfer_size": E("Total bytes transferred over the network for the page.",
                          "页面通过网络传输的总字节数。"),
 "total_dom_size": E("Total size of the rendered DOM, in bytes.",
                     "渲染后 DOM 的总大小，单位字节。"),
 "content_encoding": E("Content-Encoding applied to the response (e.g. gzip, br).",
                       "响应所用的 Content-Encoding（如 gzip、br）。"),
 "media_type": E("High-level media category of the resource (e.g. text, image).",
                 "资源的高层媒体类别（如 text、image）。"),
 "status_code_resource": E("", ""),  # unused
 # timing leaf metrics (shared by page_timing / fetch_timing / resource)
 "connection_time": E("Time to establish the network connection, in milliseconds.",
                      "建立网络连接的耗时，单位毫秒。"),
 "request_sent_time": E("Time at which the request was sent, in milliseconds.",
                        "请求发出的时间点，单位毫秒。"),
 "waiting_time": E("Time spent waiting for the server's first byte (TTFB), in milliseconds.",
                   "等待服务器首字节（TTFB）的耗时，单位毫秒。"),
 "download_time": E("Time spent downloading the response body, in milliseconds.",
                    "下载响应体的耗时，单位毫秒。"),
 "duration_time": E("Total time the request took end to end, in milliseconds.",
                    "请求端到端的总耗时，单位毫秒。"),
 "fetch_start": E("Offset at which fetching started, in milliseconds.",
                  "开始抓取的时间偏移，单位毫秒。"),
 "fetch_end": E("Offset at which fetching finished, in milliseconds.",
                "抓取结束的时间偏移，单位毫秒。"),
 "fetch_time": E("Timestamp when the page or resource was fetched.",
                 "页面或资源被抓取的时间戳。"),
 "dom_complete": E("Time at which DOM construction completed, in milliseconds.",
                   "DOM 构建完成的时间，单位毫秒。"),
 "time_to_interactive": E("Time until the page became interactive (TTI), in milliseconds.",
                          "页面变为可交互（TTI）的时间，单位毫秒。"),
 "time_to_secure_connection": E("Time to complete the TLS handshake, in milliseconds.",
                                "完成 TLS 握手的耗时，单位毫秒。"),
 "largest_contentful_paint": E("Largest Contentful Paint metric, in milliseconds.",
                               "最大内容绘制（LCP）指标，单位毫秒。"),
 "first_input_delay": E("First Input Delay metric, in milliseconds.",
                        "首次输入延迟（FID）指标，单位毫秒。"),
 "fetch_timing": E("Timing breakdown of fetching the page.",
                   "抓取该页面的时序细分。"),
 # location object (resources)
 "location": E("Position where the resource is referenced in the source, or the resource location object.",
               "资源在源码中被引用的位置，或资源定位对象。"),
 "line": E("Line number in the source where the reference or error occurs.",
           "源码中引用或错误所在的行号。"),
 "column": E("Column number in the source where the error occurs.",
             "源码中错误所在的列号。"),
 "offset_left": E("Horizontal pixel offset of the element.",
                  "元素的水平像素偏移。"),
 "offset_top": E("Vertical pixel offset of the element.",
                 "元素的垂直像素偏移。"),
}

RESP_BY_LEAF.update({
 # page-level scalars (page / pages / pages.page)
 "url": E("URL of this page or record.",
          "该页面或记录的 URL。"),
 "page_url": E("URL of the page the parsed content belongs to.",
               "解析内容所属页面的 URL。"),
 "status_code": E("HTTP status code returned when the page was fetched.",
                  "抓取该页面时返回的 HTTP 状态码。"),
 "location_page": E("", ""),  # unused
 "click_depth": E("Number of clicks from the home page needed to reach this page.",
                  "从首页到达该页面所需的点击次数。"),
 "is_resource": E("Whether this record is a resource rather than an HTML page.",
                  "该记录是否为资源而非 HTML 页面。"),
 "sitemap": E("Whether the page is listed in the site's sitemap.",
              "该页面是否被列入站点 sitemap。"),
 "last_modified": E("Last-Modified information reported for the page or resource.",
                    "页面或资源报告的 Last-Modified 信息。"),
 "header": E("Last-Modified value taken from the HTTP response header.",
             "取自 HTTP 响应头的 Last-Modified 值。"),
 "meta_tag": E("Last-Modified value taken from an in-page meta tag.",
               "取自页内 meta 标签的 Last-Modified 值。"),
 "server": E("Server software string reported by the page.",
             "页面报告的服务器软件标识。"),
 "onpage_score": E("Aggregate on-page quality score for the page (higher is better).",
                   "页面的综合 on-page 质量得分（越高越好）。"),
 "custom_js_response": E("Output returned by the custom_js script executed on the page.",
                         "在页面上执行 custom_js 脚本所返回的输出。"),
 "custom_js_client_exception": E("Any client-side exception thrown while running custom_js.",
                                 "运行 custom_js 时抛出的客户端异常（如有）。"),
 "duplicate_title": E("Whether the page's title duplicates another page's title.",
                      "该页面的 title 是否与其它页面重复。"),
 "duplicate_description": E("Whether the page's meta description duplicates another page's.",
                           "该页面的 meta description 是否与其它页面重复。"),
 "duplicate_content": E("Whether the page's body content duplicates another page's.",
                        "该页面正文内容是否与其它页面重复。"),
 "broken_links": E("Number of broken links found on the page.",
                   "页面上发现的失效链接数量。"),
 "broken_resources": E("Number of broken resources found on the page.",
                       "页面上发现的失效资源数量。"),
 "similarity": E("Content-similarity ratio between this page and the reference page.",
                 "该页面与参考页之间的内容相似度。"),
 # microdata inspection_info
 "inspection_info": E("Validation results for the structured-data items found on the page.",
                      "页面上结构化数据项的校验结果。"),
 "fields": E("Parsed fields of the structured-data item, with their values and test results.",
             "结构化数据项的解析字段，含取值与检测结果。"),
 "name": E("Name of the field, item, rating, offer, or comment author.",
           "字段、条目、评分、报价或评论作者的名称。"),
 "value": E("Value of the structured-data field.",
            "结构化数据字段的取值。"),
 "types": E("schema.org type(s) declared for the structured-data item.",
            "结构化数据项声明的 schema.org 类型。"),
 "test_results": E("Validation test outcomes for the field.",
                   "该字段的校验检测结果。"),
 "level": E("Severity level of the validation message or content heading level.",
            "校验消息的严重级别或内容标题层级。"),
 "message": E("Validation, error, or warning message text.",
              "校验、错误或警告的消息文本。"),
 # test_summary (microdata)
 "test_summary": E("Counts of validation outcomes by severity for the page.",
                   "页面按严重级别汇总的校验结果计数。"),
 "error": E("Number of validation errors.",
            "校验错误的数量。"),
 "fatal": E("Number of fatal validation problems.",
            "致命校验问题的数量。"),
 "info": E("Number of informational validation notices.",
           "信息级校验提示的数量。"),
 "warning": E("Number of validation warnings.",
              "校验警告的数量。"),
 # cache_control
 "cache_control": E("HTTP cache-control information for the page.",
                    "页面的 HTTP 缓存控制信息。"),
 "cachable": E("Whether the page is cacheable per its cache-control headers.",
               "根据缓存控制头，该页面是否可被缓存。"),
 "ttl": E("Cache time-to-live in seconds.",
          "缓存生存时间，单位秒。"),
})

# checks block: each is a boolean flag raised when the page hits the named condition.
CHECKS = {
 "checks": E("Boolean flags for the on-page issues and properties detected on the page.",
             "页面上检测到的各项 on-page 问题与属性的布尔标记。"),
 "canonical": E("Whether the page declares a canonical URL.",
                "页面是否声明了 canonical URL。"),
 "canonical_chain": E("Whether the page's canonical points through a chain of further canonicals.",
                      "页面 canonical 是否经由一连串再次 canonical 指向。"),
 "canonical_to_broken": E("Whether the canonical URL points to a broken page.",
                          "canonical URL 是否指向失效页面。"),
 "canonical_to_redirect": E("Whether the canonical URL points to a redirecting page.",
                            "canonical URL 是否指向发生重定向的页面。"),
 "recursive_canonical": E("Whether the canonical chain loops back on itself.",
                          "canonical 链是否自我循环。"),
 "deprecated_html_tags": E("Whether the page uses deprecated HTML tags.",
                           "页面是否使用了已废弃的 HTML 标签。"),
 "duplicate_meta_tags": E("Whether the page contains duplicate meta tags.",
                          "页面是否含有重复的 meta 标签。"),
 "duplicate_title_tag": E("Whether the page has more than one title tag.",
                          "页面是否存在多个 title 标签。"),
 "flash": E("Whether the page embeds Flash content.",
            "页面是否嵌入了 Flash 内容。"),
 "frame": E("Whether the page uses frames or iframes.",
            "页面是否使用了 frame 或 iframe。"),
 "has_html_doctype": E("Whether the page declares an HTML doctype.",
                       "页面是否声明了 HTML doctype。"),
 "no_doctype": E("Whether the page is missing a doctype declaration.",
                 "页面是否缺少 doctype 声明。"),
 "has_links_to_redirects": E("Whether the page links to URLs that redirect.",
                             "页面是否存在指向重定向 URL 的链接。"),
 "has_meta_refresh_redirect": E("Whether the page uses a meta-refresh redirect.",
                                "页面是否使用 meta refresh 重定向。"),
 "has_misspelling": E("Whether spell-checking found misspelled words on the page.",
                      "拼写检查是否在页面上发现错拼词。"),
 "has_render_blocking_resources": E("Whether the page loads render-blocking resources.",
                                    "页面是否加载了阻塞渲染的资源。"),
 "high_character_count": E("Whether the page's character count exceeds the high threshold.",
                           "页面字符数是否超过偏高阈值。"),
 "low_character_count": E("Whether the page's character count is below the low threshold.",
                          "页面字符数是否低于偏低阈值。"),
 "high_content_rate": E("Whether the text-to-HTML ratio is above the high threshold.",
                        "文本占 HTML 的比例是否高于偏高阈值。"),
 "low_content_rate": E("Whether the text-to-HTML ratio is below the low threshold.",
                       "文本占 HTML 的比例是否低于偏低阈值。"),
 "high_loading_time": E("Whether the page's load time exceeds the high threshold.",
                        "页面加载时间是否超过偏高阈值。"),
 "high_waiting_time": E("Whether the server waiting time (TTFB) exceeds the high threshold.",
                        "服务器等待时间（TTFB）是否超过偏高阈值。"),
 "low_readability_rate": E("Whether the page's readability score is below the threshold.",
                           "页面可读性得分是否低于阈值。"),
 "https_to_http_links": E("Whether an HTTPS page links to insecure HTTP URLs.",
                          "HTTPS 页面是否存在指向不安全 HTTP URL 的链接。"),
 "irrelevant_description": E("Whether the meta description is irrelevant to the page content.",
                            "meta description 是否与页面内容不相关。"),
 "irrelevant_meta_keywords": E("Whether the meta keywords are irrelevant to the content.",
                               "meta keywords 是否与内容不相关。"),
 "irrelevant_title": E("Whether the title is irrelevant to the page content.",
                       "title 是否与页面内容不相关。"),
 "is_4xx_code": E("Whether the page returned a 4xx HTTP status.",
                  "页面是否返回 4xx HTTP 状态。"),
 "is_5xx_code": E("Whether the page returned a 5xx HTTP status.",
                  "页面是否返回 5xx HTTP 状态。"),
 "is_broken": E("Whether the page is broken / unreachable.",
                "页面是否失效或无法访问。"),
 "is_http": E("Whether the page is served over HTTP.",
              "页面是否通过 HTTP 提供。"),
 "is_https": E("Whether the page is served over HTTPS.",
               "页面是否通过 HTTPS 提供。"),
 "is_redirect": E("Whether the page itself is a redirect.",
                  "页面本身是否为重定向。"),
 "is_www": E("Whether the page URL uses the www host.",
             "页面 URL 是否使用 www 主机。"),
 "is_orphan_page": E("Whether the page has no internal links pointing to it.",
                     "页面是否没有任何内部链接指向（孤儿页）。"),
 "is_link_relation_conflict": E("Whether the page declares conflicting link relations.",
                                "页面是否声明了相互冲突的链接关系。"),
 "large_page_size": E("Whether the page size exceeds the large threshold.",
                      "页面体积是否超过偏大阈值。"),
 "small_page_size": E("Whether the page size is below the small threshold.",
                      "页面体积是否低于偏小阈值。"),
 "size_greater_than_3mb": E("Whether the page exceeds 3 MB.",
                            "页面是否超过 3 MB。"),
 "lorem_ipsum": E("Whether the page contains lorem-ipsum placeholder text.",
                  "页面是否含有 lorem ipsum 占位文本。"),
 "has_misspelling_": E("", ""),  # unused
 "meta_charset_consistency": E("Whether the declared charset is consistent across the page.",
                               "页面声明的字符集是否前后一致。"),
 "no_content_encoding": E("Whether the response lacks content encoding (compression).",
                          "响应是否缺少内容编码（压缩）。"),
 "no_description": E("Whether the page is missing a meta description.",
                     "页面是否缺少 meta description。"),
 "no_encoding_meta_tag": E("Whether the page is missing a charset meta tag.",
                           "页面是否缺少字符集 meta 标签。"),
 "no_favicon": E("Whether the page is missing a favicon.",
                 "页面是否缺少 favicon。"),
 "no_h1_tag": E("Whether the page is missing an H1 heading.",
                "页面是否缺少 H1 标题。"),
 "no_image_alt": E("Whether the page has images without alt text.",
                   "页面是否存在缺少 alt 文本的图片。"),
 "no_image_title": E("Whether the page has images without a title attribute.",
                     "页面是否存在缺少 title 属性的图片。"),
 "no_title": E("Whether the page is missing a title tag.",
               "页面是否缺少 title 标签。"),
 "title_too_long": E("Whether the title exceeds the recommended length.",
                     "title 是否超出推荐长度。"),
 "title_too_short": E("Whether the title is below the recommended length.",
                      "title 是否短于推荐长度。"),
 "redirect_chain": E("Whether the page is reached through a chain of redirects.",
                     "到达该页面是否经过一连串重定向。"),
 "seo_friendly_url": E("Whether the URL is SEO-friendly overall.",
                       "URL 整体是否对 SEO 友好。"),
 "seo_friendly_url_characters_check": E("Whether the URL passes the allowed-characters check.",
                                        "URL 是否通过允许字符检查。"),
 "seo_friendly_url_dynamic_check": E("Whether the URL avoids dynamic query-string patterns.",
                                     "URL 是否避免了动态查询串模式。"),
 "seo_friendly_url_keywords_check": E("Whether the URL contains relevant keywords.",
                                      "URL 是否包含相关关键词。"),
 "seo_friendly_url_relative_length_check": E("Whether the URL length is within the friendly range.",
                                             "URL 长度是否处于友好范围内。"),
 "from_sitemap": E("Whether the resource/page was discovered from the sitemap.",
                   "该资源/页面是否来自 sitemap 发现。"),
 "has_redirect": E("Whether the resource request was redirected.",
                   "该资源请求是否发生重定向。"),
 "has_subrequests": E("Whether loading the resource triggered further subrequests.",
                      "加载该资源是否触发了进一步的子请求。"),
 "is_minified": E("Whether the resource is minified.",
                  "该资源是否经过压缩精简（minify）。"),
 "original_size_displayed": E("Whether the resource is served at its original (un-resized) size.",
                              "该资源是否以原始（未缩放）尺寸提供。"),
}

META = {
 "meta": E("Parsed meta information of the page (title, description, tags, link/image counts, and content metrics).",
           "页面解析出的 meta 信息（title、description、标签、链接/图片计数与内容指标）。"),
 "title": E("Title tag text of the page.",
            "页面 title 标签的文本。"),
 "title_length": E("Character length of the title.",
                   "title 的字符长度。"),
 "description": E("Meta description text of the page.",
                  "页面 meta description 的文本。"),
 "description_length": E("Character length of the meta description.",
                         "meta description 的字符长度。"),
 "charset": E("Character set declared by the page.",
              "页面声明的字符集。"),
 "follow": E("Whether robots directives allow following the page's links.",
             "robots 指令是否允许跟踪页面链接。"),
 "generator": E("Generator meta value (e.g. the CMS that produced the page).",
                "generator meta 值（如生成该页面的 CMS）。"),
 "canonical_meta": E("", ""),  # handled by leaf canonical override below
 "meta_keywords": E("Meta keywords declared by the page.",
                    "页面声明的 meta keywords。"),
 "favicon": E("URL of the page's favicon.",
              "页面 favicon 的 URL。"),
 "htags": E("Headings of the page grouped by level (h1–h6).",
            "页面按层级（h1–h6）分组的标题。"),
 "social_media_tags": E("Open Graph / social-media meta tags found on the page.",
                        "页面上发现的 Open Graph / 社交媒体 meta 标签。"),
 "deprecated_tags": E("Deprecated HTML tags present on the page.",
                      "页面上存在的已废弃 HTML 标签。"),
 "duplicate_meta_tags_list": E("", ""),  # unused
 "cumulative_layout_shift": E("Cumulative Layout Shift (CLS) metric of the page.",
                              "页面的累计布局偏移（CLS）指标。"),
 "images_count": E("Number of images on the page.",
                   "页面上的图片数量。"),
 "images_size": E("Total byte size of the page's images.",
                  "页面图片的总字节大小。"),
 "scripts_count": E("Number of scripts on the page.",
                    "页面上的脚本数量。"),
 "scripts_size": E("Total byte size of the page's scripts.",
                   "页面脚本的总字节大小。"),
 "stylesheets_count": E("Number of stylesheets on the page.",
                        "页面上的样式表数量。"),
 "stylesheets_size": E("Total byte size of the page's stylesheets.",
                       "页面样式表的总字节大小。"),
 "render_blocking_scripts_count": E("Number of render-blocking scripts.",
                                    "阻塞渲染的脚本数量。"),
 "render_blocking_stylesheets_count": E("Number of render-blocking stylesheets.",
                                        "阻塞渲染的样式表数量。"),
 "internal_links_count": E("Number of internal links on the page.",
                           "页面上的内部链接数量。"),
 "external_links_count": E("Number of external links on the page.",
                           "页面上的外部链接数量。"),
 "inbound_links_count": E("Number of internal links pointing to this page.",
                          "指向该页面的内部链接数量。"),
}

# readability / content metrics block (meta.content.*)
CONTENT = {
 "content": E("Text-content metrics computed for the page (readability indices, plain-text size, consistency ratios).",
              "为页面计算的文本内容指标（可读性指数、纯文本规模、一致性比率）。"),
 "plain_text_size": E("Byte size of the page's extracted plain text.",
                      "页面提取的纯文本的字节大小。"),
 "plain_text_rate": E("Ratio of plain text to total page content.",
                      "纯文本占页面总内容的比率。"),
 "plain_text_word_count": E("Number of words in the page's plain text.",
                            "页面纯文本的词数。"),
 "automated_readability_index": E("Automated Readability Index score of the text.",
                                  "文本的 Automated Readability Index 得分。"),
 "coleman_liau_readability_index": E("Coleman-Liau readability index score of the text.",
                                     "文本的 Coleman-Liau 可读性指数得分。"),
 "dale_chall_readability_index": E("Dale-Chall readability index score of the text.",
                                   "文本的 Dale-Chall 可读性指数得分。"),
 "flesch_kincaid_readability_index": E("Flesch-Kincaid readability index score of the text.",
                                       "文本的 Flesch-Kincaid 可读性指数得分。"),
 "smog_readability_index": E("SMOG readability index score of the text.",
                             "文本的 SMOG 可读性指数得分。"),
 "description_to_content_consistency": E("How well the meta description matches the page content, as a ratio.",
                                        "meta description 与页面内容的契合度，以比率表示。"),
 "title_to_content_consistency": E("How well the title matches the page content, as a ratio.",
                                   "title 与页面内容的契合度，以比率表示。"),
 "meta_keywords_to_content_consistency": E("How well the meta keywords match the page content, as a ratio.",
                                           "meta keywords 与页面内容的契合度，以比率表示。"),
}

SPELL = {
 "spell": E("Spell-checking results for the page's text.",
            "页面文本的拼写检查结果。"),
 "hunspell_language_code": E("Hunspell dictionary language code used for spell-checking.",
                             "拼写检查所用 Hunspell 词典的语言代码。"),
 "misspelled": E("List of misspelled words detected on the page.",
                 "页面上检测到的错拼词列表。"),
 "word": E("A single misspelled word.",
           "单个错拼词。"),
}

RESOURCE_ERRORS = {
 "resource_errors": E("Errors and warnings collected while processing the page's resources.",
                      "处理页面资源时收集到的错误与警告。"),
 "errors": E("List of error entries with their source location and message.",
             "错误条目列表，含其源位置与消息。"),
 "warnings": E("List of warning entries with their source location and message.",
              "警告条目列表，含其源位置与消息。"),
 "accept_type": E("Accept type the resource was requested with.",
                  "请求该资源时使用的 Accept 类型。"),
}

PAGE_CONTENT = {
 "page_content": E("Structured parse of the page body into topics, content blocks, tables, ratings, offers, and contacts.",
                   "将页面正文结构化解析为主题、内容块、表格、评分、报价与联系方式。"),
 "page_as_markdown": E("The parsed page content rendered as Markdown.",
                       "解析后的页面内容以 Markdown 渲染的形式。"),
 "html": E("Raw HTML of the parsed block.",
           "解析块的原始 HTML。"),
 # topic blocks (main_topic / secondary_topic)
 "main_topic": E("The page's primary topic block with its heading hierarchy and content.",
                 "页面的主要主题块，含其标题层级与内容。"),
 "secondary_topic": E("Secondary topic blocks of the page.",
                      "页面的次要主题块。"),
 "h_title": E("Heading text of the topic.",
              "主题的标题文本。"),
 "main_title": E("Main title text of the topic.",
                 "主题的主标题文本。"),
 "language": E("Detected language of the topic text.",
               "主题文本检测到的语言。"),
 "author": E("Author attributed to the content (topic, comment, or rating).",
             "归属于内容（主题、评论或评分）的作者。"),
 # content blocks (primary/secondary content)
 "primary_content": E("The primary content block of the topic or page.",
                      "主题或页面的主要内容块。"),
 "secondary_content": E("The secondary content block of the topic or page.",
                        "主题或页面的次要内容块。"),
 "urls": E("URLs found within the content block, with their anchor text.",
           "内容块中发现的 URL，及其锚文本。"),
 "anchor_text": E("Anchor text of the link.",
                  "链接的锚文本。"),
 # tables
 "table_content": E("Tables parsed from the page, split into header, body, and footer rows.",
                    "从页面解析出的表格，分为表头、表体与表尾行。"),
 "body": E("Body rows of the table.",
           "表格的表体行。"),
 "footer": E("Footer rows of the table, or the page footer block.",
             "表格的表尾行，或页面的 footer 块。"),
 "row_cells": E("Cells of the table row.",
                "表格行的单元格。"),
 "is_header": E("Whether the cell is a header cell.",
                "该单元格是否为表头单元格。"),
 # ratings / comments
 "ratings": E("Ratings parsed from the page.",
              "从页面解析出的评分。"),
 "rating": E("Rating block associated with the comment.",
             "与评论关联的评分块。"),
 "rating_value": E("Numeric rating value.",
                   "评分的数值。"),
 "max_rating_value": E("Maximum possible rating value on the scale.",
                       "评分量表上的最大可能值。"),
 "relative_rating": E("Rating normalized relative to its maximum.",
                      "相对于最大值归一化后的评分。"),
 "relative rating": E("Rating normalized relative to its maximum.",
                      "相对于最大值归一化后的评分。"),
 "rating_count": E("Number of ratings aggregated.",
                   "参与聚合的评分数量。"),
 "comments": E("Comments parsed from the page.",
               "从页面解析出的评论。"),
 "publish_date": E("Publication date of the comment.",
                   "评论的发布日期。"),
 # offers
 "offers": E("Product offers parsed from the page.",
             "从页面解析出的商品报价。"),
 "price": E("Price of the offer.",
            "报价的价格。"),
 "price_currency": E("Currency of the offer price.",
                     "报价价格的币种。"),
 "price_valid_until": E("Date until which the offer price is valid.",
                        "报价价格的有效截止日期。"),
 # contacts
 "contacts": E("Contact details parsed from the page.",
               "从页面解析出的联系方式。"),
 "emails": E("Email addresses found on the page.",
             "页面上发现的电子邮箱地址。"),
 "telephones": E("Phone numbers found on the page.",
                 "页面上发现的电话号码。"),
}

# Full-dotpath overrides where the same leaf name means something different by context.
# tasks.result.items.meta.* = resource/image meta (NOT the page-level meta block).
RESP_BY_PATH = {
 "tasks.result.items.meta": E("Metadata of the resource (e.g. image dimensions, content type, title).",
                              "资源的元数据（如图片尺寸、内容类型、标题）。"),
 "tasks.result.items.meta.alternative_text": E("Alt text of the image resource.",
                                               "图片资源的 alt 替代文本。"),
 "tasks.result.items.meta.title": E("Title attribute of the resource.",
                                    "资源的 title 属性。"),
 "tasks.result.items.meta.content_type": E("MIME content type the resource was served with.",
                                           "资源实际提供时的 MIME 内容类型。"),
 "tasks.result.items.meta.expected_content_types": E("Content types expected for the resource based on context.",
                                                     "根据上下文预期的资源内容类型。"),
 "tasks.result.items.meta.width": E("Rendered width of the image, in pixels.",
                                    "图片的渲染宽度，单位像素。"),
 "tasks.result.items.meta.height": E("Rendered height of the image, in pixels.",
                                     "图片的渲染高度，单位像素。"),
 "tasks.result.items.meta.original_width": E("Intrinsic (original) width of the image, in pixels.",
                                             "图片的固有（原始）宽度，单位像素。"),
 "tasks.result.items.meta.original_height": E("Intrinsic (original) height of the image, in pixels.",
                                              "图片的固有（原始）高度，单位像素。"),
 # canonical under meta is a URL string (page meta), keep distinct from checks.canonical bool
 "tasks.result.items.pages.page.meta.canonical": E("Canonical URL declared by the page.",
                                                   "页面声明的 canonical URL。"),
 "tasks.result.pages.meta.canonical": E("Canonical URL declared by the page.",
                                        "页面声明的 canonical URL。"),
 "tasks.result.items.pages.page.meta.content": E("Text-content metrics computed for the page.",
                                                 "为页面计算的文本内容指标。"),
 "tasks.result.pages.meta.content": E("Text-content metrics computed for the page.",
                                      "为页面计算的文本内容指标。"),
 # resource_errors.last_modified is an object here
 "tasks.result.resource_errors.last_modified": E("Last-Modified information for the errored resource.",
                                                 "出错资源的 Last-Modified 信息。"),
 "tasks.result.resource_errors.last_modified.header": E("Last-Modified value from the HTTP header.",
                                                        "取自 HTTP 响应头的 Last-Modified 值。"),
 "tasks.result.resource_errors.last_modified.meta_tag": E("Last-Modified value from an in-page meta tag.",
                                                          "取自页内 meta 标签的 Last-Modified 值。"),
 "tasks.result.resource_errors.last_modified.sitemap": E("Last-Modified value reported by the sitemap.",
                                                         "由 sitemap 报告的 Last-Modified 值。"),
 # status_code inside errors objects = the resource's HTTP status, not the task status
 "tasks.result.resource_errors.errors.status_code": E("HTTP status code returned for the errored resource.",
                                                      "出错资源返回的 HTTP 状态码。"),
 "tasks.result.resource_errors.warnings.status_code": E("HTTP status code returned for the warned resource.",
                                                        "触发警告资源返回的 HTTP 状态码。"),
 # duplicate_meta_tags / deprecated_tags as page-meta lists are arrays of tag info
 "tasks.result.items.pages.page.meta.duplicate_meta_tags": E("Meta tags that are duplicated on the page.",
                                                             "页面上重复出现的 meta 标签。"),
 "tasks.result.pages.meta.duplicate_meta_tags": E("Meta tags that are duplicated on the page.",
                                                  "页面上重复出现的 meta 标签。"),
}

# ---------------------------------------------------------------------------
# Assembler
# ---------------------------------------------------------------------------
# Merge all leaf dictionaries into one lookup (later updates win on key clash;
# order chosen so context-appropriate text wins for shared leaves).
LEAF = {}
for d in (ENVELOPE, RESP_BY_LEAF, CHECKS, META, CONTENT, SPELL, RESOURCE_ERRORS, PAGE_CONTENT):
    LEAF.update(d)

def leaf_of(dotpath):
    return dotpath.split(".")[-1]

def lookup_resp(dotpath):
    if dotpath in RESP_BY_PATH:
        return RESP_BY_PATH[dotpath]
    # envelope / task-wrapper exact paths
    if dotpath in ENVELOPE:
        return ENVELOPE[dotpath]
    leaf = leaf_of(dotpath)
    return LEAF.get(leaf)

def lookup_req(dotpath):
    leaf = leaf_of(dotpath)
    return REQ.get(leaf)

def clean(entry):
    # drop placeholder empties that were used to reserve keys
    return {"desc_en": entry["desc_en"], "title_zh": entry["title_zh"]}

def build():
    missing = []
    content = {"operations": {}, "fields": {}}
    for op, d in INV.items():
        opmeta = OPS.get(op)
        if not opmeta or not opmeta.get("heading_zh"):
            missing.append(("OP", op))
            continue
        content["operations"][op] = {k: opmeta[k] for k in ("heading_zh", "desc_en", "description_zh")}
        fblock = {"request": {}, "response": {}}
        for dp in d["request"]:
            e = lookup_req(dp)
            if not e or not e["desc_en"]:
                missing.append((op, "req", dp)); continue
            fblock["request"][dp] = clean(e)
        for code, paths in d["response"].items():
            cm = {}
            for dp in paths:
                e = lookup_resp(dp)
                if not e or not e["desc_en"]:
                    missing.append((op, "resp", code, dp)); continue
                cm[dp] = clean(e)
            fblock["response"][code] = cm
        content["fields"][op] = fblock

    if missing:
        sys.stderr.write("UNCOVERED DOTPATHS (%d):\n" % len(missing))
        for m in missing[:80]:
            sys.stderr.write("  " + " | ".join(map(str, m)) + "\n")
        sys.exit("ABORT: author missing entries before writing content.json")

    out = "/home/mira/files/aisa-docs-voyager/ws-v2/dataforseo/parts/on_page.content.json"
    json.dump(content, open(out, "w"), ensure_ascii=False, indent=2)
    print("WROTE", out)
    nf = sum(len(b["request"]) + sum(len(c) for c in b["response"].values()) for b in content["fields"].values())
    print("ops=%d fields=%d" % (len(content["operations"]), nf))

# --- additional authored entries for uncovered dotpaths (parent objects/leaves) ---
RESP_BY_PATH.update({
 # crawl_status object itself (children already authored)
 "tasks.result.crawl_status": E("Crawl progress snapshot: page-count limit, pages crawled, and pages still queued.",
                                "抓取进度快照：页面数上限、已抓取页面数与仍排队的页面数。"),
 # page_timing object (children already authored under leaf names)
 "tasks.result.items.pages.page.page_timing": E("Per-stage load-timing breakdown for the page.",
                                                "页面分阶段的加载时序细分。"),
 "tasks.result.pages.page_timing": E("Per-stage load-timing breakdown for the page.",
                                     "页面分阶段的加载时序细分。"),
 "tasks.result.items.fetch_timing": E("Per-stage timing breakdown of fetching the resource.",
                                      "抓取该资源的分阶段时序细分。"),
 # duplicate_tags result-level
 "tasks.result.accumulator": E("Field used to group pages that share the duplicate tag.",
                               "用于将共享重复标签的页面归组的字段。"),
 "tasks.result.audits": E("List of available Lighthouse audit ids.",
                          "可用的 Lighthouse 单项审计 id 列表。"),
 # result-level id / tag in tasks_ready listings
 "tasks.result.id": E("Task id of a completed task ready to be collected.",
                      "已完成、可收取任务的 task id。"),
 "tasks.result.tag": E("User-supplied tag echoed for the completed task.",
                       "为已完成任务回显的用户自定义标签。"),
 # summary / lighthouse task_get minimal response: a lone id = the task id queried
 "id": E("Task id this response corresponds to.",
         "本响应对应的 task id。"),
})

build()
