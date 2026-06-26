# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 47 个接口，779 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## post_dataforseo_serp_google_organic_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Organic SERP Tasks. Standard task-based endpoint. Your account is charged only for setting a task. You can send up to 100 tasks per POST call. | Queue a Google Organic SERP task for a keyword/location/language; you are charged only for posting, and up to 100 tasks can be sent per call. The response returns a task id used to collect the SERP later via the matching task_get endpoint or via postback/pingback. | 为给定 keyword/地区/语言提交一个 Google 自然搜索（Organic）SERP 任务；仅按提交计费，单次调用最多 100 个任务。响应返回 task id，稍后通过对应的 task_get 端点或 postback/pingback 收取 SERP。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.depth` | Parsing depth, default 100, max 700 | Number of SERP results to parse; deeper values cost more crawl pages and increase task price. | 要解析的 SERP 结果数量；取值越深消耗的抓取页数越多，任务价格也越高。 |
| `req.max_crawl_pages` | Page crawl limit, max 100 | Upper bound on the number of SERP pages to crawl for this task. | 本任务抓取的 SERP 页面数上限。 |
| `req.device` | Device type: desktop or mobile | Device profile to emulate for the search, such as `desktop` or `mobile`; affects layout and result set. | 搜索时模拟的设备类型，如 `desktop` 或 `mobile`，会影响版式与结果集合。 |
| `req.os` | Device operating system | Operating system to emulate for the chosen device, refining the user-agent presented to Google. | 为所选设备模拟的操作系统，用于细化向 Google 呈现的 user-agent。 |
| `req.group_organic_results` | Display related results as grouped organic results | When enabled, related organic results are merged and reported as grouped organic entries instead of separate items. | 启用后，相关的自然结果会被合并归组为分组自然条目，而非分散的独立条目。 |
| `req.calculate_rectangles` | Calculate pixel rankings for SERP elements in advanced results | When enabled, pixel-coordinate rankings (rectangles) are computed for elements in the advanced SERP, useful for visual position analysis. | 启用后，会为高级 SERP 中的元素计算像素坐标排名（矩形框），便于做可视化位置分析。 |
| `req.postback_url` | Postback URL for completed task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.pingback_url` | Pingback URL for task completion notification | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_data` | Postback payload type | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `req.tag` | User-defined task identifier | Your own identifier echoed back with the task, useful for correlating results with your records. | 随任务回显的你方自定义标识，便于将结果与你方记录关联。 |
| `resp.200.version` | API version | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost in USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | Number of tasks in the request | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | Number of tasks returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Task cost | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of result elements | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_google_organic_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Organic HTML Results by id. Retrieve raw HTML results for a posted task within 30 days at no extra charge. | Retrieve the raw HTML of a previously posted Google Organic SERP task by its id; available within 30 days of posting at no extra charge. | 按 task id 取回此前提交的 Google 自然搜索 SERP 任务的原始 HTML；提交后 30 天内可免费获取。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | API version | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Task cost in USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].result` | Result array containing HTML pages | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].items` | HTML page items | Array of SERP elements parsed for this result. | 本结果解析出的 SERP 元素数组。 |
| `resp.200.tasks[].result[].items[].html` | Raw HTML page content | Raw HTML content of this element. | 该元素的原始 HTML 内容。 |

## post_dataforseo_serp_google_organic_live_regular

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Organic SERP Regular. Returns regular SERP results immediately. Each Live SERP API call can contain only one task. | Return Google Organic SERP results in the regular (lightweight) format immediately in the same response; each Live SERP call carries exactly one task. | 以常规（轻量）格式即时返回 Google 自然搜索 SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.device` | Device type: desktop or mobile | Device profile to emulate for the search, such as `desktop` or `mobile`; affects layout and result set. | 搜索时模拟的设备类型，如 `desktop` 或 `mobile`，会影响版式与结果集合。 |
| `req.os` | Device operating system | Operating system to emulate for the chosen device, refining the user-agent presented to Google. | 为所选设备模拟的操作系统，用于细化向 Google 呈现的 user-agent。 |
| `req.depth` | Parsing depth, default 100, max 700 | Number of SERP results to parse; deeper values cost more crawl pages and increase task price. | 要解析的 SERP 结果数量；取值越深消耗的抓取页数越多，任务价格也越高。 |
| `req.max_crawl_pages` | Page crawl limit, max 100 | Upper bound on the number of SERP pages to crawl for this task. | 本任务抓取的 SERP 页面数上限。 |
| `req.tag` | User-defined task identifier | Your own identifier echoed back with the task, useful for correlating results with your records. | 随任务回显的你方自定义标识，便于将结果与你方记录关联。 |
| `resp.200.version` | API version | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Request cost in USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | Number of tasks returned | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | Number of tasks returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of live task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].result` | Live SERP regular results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_organic_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Organic SERP Advanced. Returns advanced SERP results immediately. Each Live SERP API call can contain only one task. | Return Google Organic SERP results in the advanced (full element-level) format immediately in the same response; each Live SERP call carries exactly one task. | 以高级（完整元素级）格式即时返回 Google 自然搜索 SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.device` | Device type: desktop or mobile | Device profile to emulate for the search, such as `desktop` or `mobile`; affects layout and result set. | 搜索时模拟的设备类型，如 `desktop` 或 `mobile`，会影响版式与结果集合。 |
| `req.os` | Device operating system | Operating system to emulate for the chosen device, refining the user-agent presented to Google. | 为所选设备模拟的操作系统，用于细化向 Google 呈现的 user-agent。 |
| `req.depth` | Parsing depth, default 100, max 700 | Number of SERP results to parse; deeper values cost more crawl pages and increase task price. | 要解析的 SERP 结果数量；取值越深消耗的抓取页数越多，任务价格也越高。 |
| `req.max_crawl_pages` | Page crawl limit, max 100 | Upper bound on the number of SERP pages to crawl for this task. | 本任务抓取的 SERP 页面数上限。 |
| `req.calculate_rectangles` | Calculate pixel rankings for SERP elements | When enabled, pixel-coordinate rankings (rectangles) are computed for elements in the advanced SERP, useful for visual position analysis. | 启用后，会为高级 SERP 中的元素计算像素坐标排名（矩形框），便于做可视化位置分析。 |
| `req.tag` | User-defined task identifier | Your own identifier echoed back with the task, useful for correlating results with your records. | 随任务回显的你方自定义标识，便于将结果与你方记录关联。 |
| `resp.200.version` | API version | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Request cost in USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | Number of tasks returned | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | Number of tasks returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of live task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].result` | Live SERP advanced results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_ai_mode_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Google AI Mode SERP API provides search results from the AI Mode feature of Google Search. Send JSON task arrays; up to 100 tasks per POST call. Completed tasks can be retrieved later by id, postback_url, or pingback_url. | Queue a Google AI Mode SERP task, returning search results from Google Search's AI Mode feature; up to 100 tasks per call. Collect the completed task later by id or via postback/pingback. | 提交一个 Google AI Mode SERP 任务，返回 Google 搜索 AI Mode 功能的搜索结果；单次最多 100 个任务。稍后按 id 或通过 postback/pingback 收取已完成任务。 |
| `req.keyword` | Keyword; you can specify up to 700 characters | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code; required if location_name or location_coordinate is not specified | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location; required if location_code or location_coordinate is not specified | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location; required if location_name or location_code is not specified | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_name` | Full name of search engine language; required if language_code is not specified | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code; required if language_name is not specified | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.priority` | Task priority: 1 normal (default), 2 high | Execution priority of the task; higher priority is processed sooner at a higher price. | 任务的执行优先级；更高优先级处理更快、价格更高。 |
| `req.device` | Device type: desktop or mobile | Device profile to emulate for the search, such as `desktop` or `mobile`; affects layout and result set. | 搜索时模拟的设备类型，如 `desktop` 或 `mobile`，会影响版式与结果集合。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.postback_data` | Postback URL datatype; required if postback_url is specified; possible values: advanced, html | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_google_ai_mode_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Retrieve Google AI Mode SERP advanced results by task id. Results can be requested within 30 days after task creation at no extra charge beyond posting the task. | Retrieve advanced Google AI Mode SERP results by task id; available within 30 days of posting at no extra charge beyond the task fee. | 按 task id 取回 Google AI Mode SERP 的高级结果；提交后 30 天内除任务费外不再额外收费。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].time` | Execution time, seconds | Server-side execution time spent on this task, in seconds. | 该任务的服务端执行耗时，单位秒。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |
| `resp.200.tasks[].path` | URL path | Endpoint path segments called to create this task; echoes the request routing. | 创建该任务时调用的端点路径分段，回显请求路由。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the request parameters used to create this task, for traceability. | 回显创建该任务所用的请求参数，便于追溯。 |
| `resp.200.tasks[].result` | Array of SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].keyword` | Keyword received in the POST array | Keyword echoed from the POST request that this result corresponds to. | 对应本结果、回显自 POST 请求的关键词。 |
| `resp.200.tasks[].result[].type` | Search engine type in the POST array | Search type of this result block, echoed from the request. | 本结果块的搜索类型，回显自请求。 |
| `resp.200.tasks[].result[].check_url` | Search URL with refinement parameters | Direct Google URL reproducing this SERP with the same refinement parameters; open it to verify the result. | 可复现本 SERP 且带相同细化参数的 Google 直达 URL；打开可核对结果。 |
| `resp.200.tasks[].result[].item_types` | Types of search results found in SERP | List of element types present in this SERP (e.g. organic, ai_overview), useful to know what `items` contains. | 本 SERP 中出现的元素类型列表（如 organic、ai_overview），可据此了解 `items` 的内容。 |
| `resp.200.tasks[].result[].se_results_count` | Total number of results in SERP | Total number of results Google reports for the query. | Google 为该查询报告的结果总数。 |
| `resp.200.tasks[].result[].items_count` | Number of results returned in the items array | Number of elements returned in this result's `items` array. | 本结果 `items` 数组中返回的元素数量。 |
| `resp.200.tasks[].result[].items` | Elements of search results found in SERP | Array of SERP elements parsed for this result. | 本结果解析出的 SERP 元素数组。 |
| `resp.200.tasks[].result[].items[].type` | Type of element, such as ai_overview | Type of this SERP element (e.g. `ai_overview`), determining its other fields. | 该 SERP 元素的类型（如 `ai_overview`），决定其其余字段。 |
| `resp.200.tasks[].result[].items[].markdown` | Content of the element in markdown format | Content of this element rendered as Markdown. | 该元素以 Markdown 渲染的内容。 |

## post_dataforseo_serp_google_ai_mode_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Returns Google AI Mode SERP results in real time. Each Live SERP call can contain only one task. | Return advanced Google AI Mode SERP results in real time in the same response; each Live SERP call carries exactly one task. | 以高级格式即时返回 Google AI Mode SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Keyword; you can specify up to 700 characters | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code; required if location_name or location_coordinate is not specified | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location; required if location_code or location_coordinate is not specified | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location; required if location_name or location_code is not specified | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_name` | Full name of search engine language; required if language_code is not specified | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code; required if language_name is not specified | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.device` | Device type: desktop or mobile | Device profile to emulate for the search, such as `desktop` or `mobile`; affects layout and result set. | 搜索时模拟的设备类型，如 `desktop` 或 `mobile`，会影响版式与结果集合。 |
| `req.calculate_rectangles` | Enable pixel ranking calculations for elements in SERP | When enabled, pixel-coordinate rankings (rectangles) are computed for elements in the advanced SERP, useful for visual position analysis. | 启用后，会为高级 SERP 中的元素计算像素坐标排名（矩形框），便于做可视化位置分析。 |
| `req.browser_screen_width` | Custom browser screen width | Custom browser viewport width, in pixels, used when rendering the SERP for rectangle calculations. | 渲染 SERP 以计算矩形框时使用的自定义浏览器视口宽度，单位像素。 |
| `req.browser_screen_height` | Custom browser screen height | Custom browser viewport height, in pixels, used when rendering the SERP for rectangle calculations. | 渲染 SERP 以计算矩形框时使用的自定义浏览器视口高度，单位像素。 |
| `req.browser_screen_resolution_ratio` | Screen resolution ratio for rectangle calculations | Device pixel ratio applied to the rendering viewport when computing rectangles. | 计算矩形框时应用于渲染视口的设备像素比。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].keyword` | Keyword received in the POST array | Keyword echoed from the POST request that this result corresponds to. | 对应本结果、回显自 POST 请求的关键词。 |
| `resp.200.tasks[].result[].type` | Search engine type in the POST array | Search type of this result block, echoed from the request. | 本结果块的搜索类型，回显自请求。 |
| `resp.200.tasks[].result[].se_domain` | Search engine domain in the POST array | Search-engine domain used for this result (e.g. `google.com`). | 本结果使用的搜索引擎域名（如 `google.com`）。 |
| `resp.200.tasks[].result[].location_code` | Location code in the POST array | Location code applied to this result, echoed from the request. | 应用于本结果的地区代码，回显自请求。 |
| `resp.200.tasks[].result[].language_code` | Language code in the POST array | Language code applied to this result, echoed from the request. | 应用于本结果的语言代码，回显自请求。 |
| `resp.200.tasks[].result[].check_url` | Search URL with refinement parameters | Direct Google URL reproducing this SERP with the same refinement parameters; open it to verify the result. | 可复现本 SERP 且带相同细化参数的 Google 直达 URL；打开可核对结果。 |
| `resp.200.tasks[].result[].item_types` | Types of search results found in SERP | List of element types present in this SERP (e.g. organic, ai_overview), useful to know what `items` contains. | 本 SERP 中出现的元素类型列表（如 organic、ai_overview），可据此了解 `items` 的内容。 |
| `resp.200.tasks[].result[].items_count` | Number of results returned in the items array | Number of elements returned in this result's `items` array. | 本结果 `items` 数组中返回的元素数量。 |
| `resp.200.tasks[].result[].items` | Elements of search results found in SERP | Array of SERP elements parsed for this result. | 本结果解析出的 SERP 元素数组。 |

## post_dataforseo_serp_google_maps_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Maps SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Queue a Google Maps SERP task for a keyword/location; charged only for posting, up to 100 tasks per call, with results collected later by id or via postback/pingback. | 为给定 keyword/地区提交一个 Google 地图 SERP 任务；仅按提交计费，单次最多 100 个任务，结果稍后按 id 或通过 postback/pingback 收取。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.depth` | Parsing depth | Number of SERP results to parse; deeper values cost more crawl pages and increase task price. | 要解析的 SERP 结果数量；取值越深消耗的抓取页数越多，任务价格也越高。 |
| `req.priority` | Task priority | Execution priority of the task; higher priority is processed sooner at a higher price. | 任务的执行优先级；更高优先级处理更快、价格更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_data` | Postback datatype | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## post_dataforseo_serp_google_maps_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Maps SERP. Returns Google Maps SERP results in real time. Each Live SERP API call can contain only one task. | Return Google Maps SERP results in real time in the same response; each Live SERP call carries exactly one task. | 即时返回 Google 地图 SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.depth` | Parsing depth | Number of SERP results to parse; deeper values cost more crawl pages and increase task price. | 要解析的 SERP 结果数量；取值越深消耗的抓取页数越多，任务价格也越高。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_local_finder_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Local Finder SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Queue a Google Local Finder SERP task for a keyword/location; charged only for posting, up to 100 tasks per call, with results collected later by id or via postback/pingback. | 为给定 keyword/地区提交一个 Google Local Finder SERP 任务；仅按提交计费，单次最多 100 个任务，结果稍后按 id 或通过 postback/pingback 收取。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.depth` | Parsing depth | Number of SERP results to parse; deeper values cost more crawl pages and increase task price. | 要解析的 SERP 结果数量；取值越深消耗的抓取页数越多，任务价格也越高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_data` | Postback datatype; possible values include advanced and html | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_google_local_finder_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Local Finder SERP Advanced Results by id. Results can be retrieved by task id within the retention window after posting the task. | Retrieve advanced Google Local Finder SERP results by task id within the retention window after the task was posted. | 在任务提交后的留存期内，按 task id 取回 Google Local Finder SERP 的高级结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the request parameters used to create this task, for traceability. | 回显创建该任务所用的请求参数，便于追溯。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_local_finder_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Local Finder SERP. Returns Google Local Finder SERP results in real time. Each Live SERP API call can contain only one task. | Return Google Local Finder SERP results in real time in the same response; each Live SERP call carries exactly one task. | 即时返回 Google Local Finder SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.min_rating` | Minimum rating filter | Lower bound on the place rating; results with a rating below this value are filtered out. | 地点评分的下限；评分低于该值的结果会被过滤掉。 |
| `req.time_filter` | Time filter | Restricts results to a time window (e.g. open-now / specific hours); narrows the local results returned. | 将结果限定在某时间窗口（如当前营业/特定时段），收窄返回的本地结果。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_news_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google News SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Queue a Google News SERP task for a keyword/location; charged only for posting, up to 100 tasks per call, with results collected later by id or via postback/pingback. | 为给定 keyword/地区提交一个 Google 新闻 SERP 任务；仅按提交计费，单次最多 100 个任务，结果稍后按 id 或通过 postback/pingback 收取。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.depth` | Parsing depth | Number of SERP results to parse; deeper values cost more crawl pages and increase task price. | 要解析的 SERP 结果数量；取值越深消耗的抓取页数越多，任务价格也越高。 |
| `req.priority` | Task priority | Execution priority of the task; higher priority is processed sooner at a higher price. | 任务的执行优先级；更高优先级处理更快、价格更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_data` | Postback datatype; possible values include advanced and html | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_google_news_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google News SERP Advanced Results by id. Results can be retrieved by task id within the retention window after posting the task. | Retrieve advanced Google News SERP results by task id within the retention window after the task was posted. | 在任务提交后的留存期内，按 task id 取回 Google 新闻 SERP 的高级结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the request parameters used to create this task, for traceability. | 回显创建该任务所用的请求参数，便于追溯。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_news_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google News SERP. Returns Google News SERP results in real time. Each Live SERP API call can contain only one task. | Return Google News SERP results in real time in the same response; each Live SERP call carries exactly one task. | 即时返回 Google 新闻 SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.depth` | Parsing depth | Number of SERP results to parse; deeper values cost more crawl pages and increase task price. | 要解析的 SERP 结果数量；取值越深消耗的抓取页数越多，任务价格也越高。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## get_dataforseo_serp_google_events_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Events SERP Completed Tasks. Returns a list of completed tasks that have not been collected yet. Up to 1000 tasks completed within the previous 3 days can be returned per call. | List completed Google Events SERP tasks that have not yet been collected; up to 1000 tasks completed within the previous 3 days are returned per call, each with the endpoint to fetch its results. | 列出已完成但尚未收取的 Google 活动（Events）SERP 任务；单次最多返回近 3 天内完成的 1000 个任务，每项附带取结果的端点。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Task id of the completed task, ready to be collected. | 已完成、可收取任务的 task id。 |
| `resp.200.tasks[].result[].se` | Search engine specified when setting the task | Search engine specified when the task was posted. | 提交任务时指定的搜索引擎。 |
| `resp.200.tasks[].result[].se_type` | Type of search engine | Type of search-engine SERP the task targets (e.g. organic, news). | 任务所针对的搜索引擎 SERP 类型（如 organic、news）。 |
| `resp.200.tasks[].result[].date_posted` | Date when the task was posted in UTC format | Timestamp when the task was posted, in UTC. | 任务提交的时间戳，UTC 格式。 |
| `resp.200.tasks[].result[].tag` | User-defined task identifier | User-defined tag echoed for the completed task. | 为已完成任务回显的用户自定义标签。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting SERP Advanced results | Relative URL to call to collect this task's advanced results. | 用于收取该任务高级结果的相对 URL。 |

## get_dataforseo_serp_google_events_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Events SERP Advanced Results by id. Results can be retrieved by task id within the retention window after posting the task. | Retrieve advanced Google Events SERP results by task id within the retention window after the task was posted. | 在任务提交后的留存期内，按 task id 取回 Google 活动 SERP 的高级结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the request parameters used to create this task, for traceability. | 回显创建该任务所用的请求参数，便于追溯。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_events_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Events SERP Advanced. Returns Google Events SERP results in real time. Each Live SERP API call can contain only one task. | Return Google Events SERP results in real time in the same response; each Live SERP call carries exactly one task. | 即时返回 Google 活动 SERP 结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## get_dataforseo_serp_google_images_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Images SERP Completed Tasks. Returns a list of completed tasks that have not been collected yet. Up to 1000 tasks completed within the previous 3 days can be returned per call. | List completed Google Images SERP tasks that have not yet been collected; up to 1000 tasks completed within the previous 3 days are returned per call, each with the endpoints to fetch its regular and HTML results. | 列出已完成但尚未收取的 Google 图片 SERP 任务；单次最多返回近 3 天内完成的 1000 个任务，每项附带取常规结果与 HTML 结果的端点。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Task id of the completed task, ready to be collected. | 已完成、可收取任务的 task id。 |
| `resp.200.tasks[].result[].se` | Search engine specified when setting the task | Search engine specified when the task was posted. | 提交任务时指定的搜索引擎。 |
| `resp.200.tasks[].result[].se_type` | Type of search engine | Type of search-engine SERP the task targets (e.g. organic, news). | 任务所针对的搜索引擎 SERP 类型（如 organic、news）。 |
| `resp.200.tasks[].result[].date_posted` | Date when the task was posted in UTC format | Timestamp when the task was posted, in UTC. | 任务提交的时间戳，UTC 格式。 |
| `resp.200.tasks[].result[].tag` | User-defined task identifier | User-defined tag echoed for the completed task. | 为已完成任务回显的用户自定义标签。 |
| `resp.200.tasks[].result[].endpoint_regular` | URL for collecting SERP results | Relative URL to call to collect this task's regular results. | 用于收取该任务常规结果的相对 URL。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting SERP HTML results | Relative URL to call to collect this task's HTML results. | 用于收取该任务 HTML 结果的相对 URL。 |

## get_dataforseo_serp_google_images_task_get_regular_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Images SERP Results by id. Returns regular image SERP results for a previously posted task. | Retrieve regular-format Google Images SERP results for a previously posted task by its id. | 按 task id 取回此前提交任务的 Google 图片 SERP 常规格式结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].result` | Array of regular SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_images_live_html

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Images SERP HTML. Returns raw HTML of Google Images SERP results in real time. Each Live SERP API call can contain only one task. | Return the raw HTML of Google Images SERP results in real time in the same response; each Live SERP call carries exactly one task. | 即时返回 Google 图片 SERP 结果的原始 HTML，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.device` | Device type: desktop or mobile | Device profile to emulate for the search, such as `desktop` or `mobile`; affects layout and result set. | 搜索时模拟的设备类型，如 `desktop` 或 `mobile`，会影响版式与结果集合。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_search_by_image_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Search By Image SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Queue a Google Search-by-Image SERP task using a publicly accessible image URL as the query; charged only for posting, up to 100 tasks per call, with results collected later by id or via postback/pingback. | 以一个可公开访问的图片 URL 作为查询，提交一个 Google 以图搜图（Search by Image）SERP 任务；仅按提交计费，单次最多 100 个任务，结果稍后按 id 或通过 postback/pingback 收取。 |
| `req.image_url` | Publicly accessible image URL used as the search input | Publicly accessible URL of the image to search with; Google returns results based on this image. | 用于搜索的可公开访问图片 URL；Google 基于该图片返回结果。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.priority` | Task priority | Execution priority of the task; higher priority is processed sooner at a higher price. | 任务的执行优先级；更高优先级处理更快、价格更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_data` | Postback datatype; possible values include advanced and html | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_google_search_by_image_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Search By Image SERP Advanced Results by id. Results can be retrieved by task id within the retention window after posting the task. | Retrieve advanced Google Search-by-Image SERP results by task id within the retention window after the task was posted. | 在任务提交后的留存期内，按 task id 取回 Google 以图搜图 SERP 的高级结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the request parameters used to create this task, for traceability. | 回显创建该任务所用的请求参数，便于追溯。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_jobs_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Jobs Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Queue a Google Jobs SERP task for a keyword/location; charged only for posting, up to 100 tasks per call, with results collected later by id or via postback/pingback. | 为给定 keyword/地区提交一个 Google 招聘（Jobs）SERP 任务；仅按提交计费，单次最多 100 个任务，结果稍后按 id 或通过 postback/pingback 收取。 |
| `req.keyword` | Keyword to search for | Search term to query. URL-encode it; the SERP is built around this query. | 要查询的搜索词。需做 URL 编码；SERP 围绕该查询词构建。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.priority` | Task priority | Execution priority of the task; higher priority is processed sooner at a higher price. | 任务的执行优先级；更高优先级处理更快、价格更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_data` | Postback datatype; possible values include advanced and html | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_google_jobs_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Jobs Advanced Results by id. Results can be retrieved by task id within the retention window after posting the task. | Retrieve advanced Google Jobs SERP results by task id within the retention window after the task was posted. | 在任务提交后的留存期内，按 task id 取回 Google 招聘 SERP 的高级结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the request parameters used to create this task, for traceability. | 回显创建该任务所用的请求参数，便于追溯。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_autocomplete_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Autocomplete Tasks. DataForSEO returns Google Autocomplete suggestions for a keyword, cursor position, and selected client. Your account is charged only for setting a task. | Queue a Google Autocomplete task that returns search suggestions for a keyword, cursor position, and search client; charged only for posting. | 提交一个 Google 自动补全（Autocomplete）任务，返回给定 keyword、光标位置与搜索客户端下的搜索建议；仅按提交计费。 |
| `req.keyword` | Keyword to get autocomplete suggestions for | Seed term to fetch autocomplete suggestions for. | 用于获取自动补全建议的种子词。 |
| `req.client` | Search client for autocomplete, such as chrome, chrome-omni, gws-wiz, safari, firefox, img, or youtube | Autocomplete source client to emulate, such as `chrome`, `chrome-omni`, `gws-wiz`, `safari`, `firefox`, `img`, or `youtube`; each client returns a different suggestion set. | 要模拟的自动补全来源客户端，如 `chrome`、`chrome-omni`、`gws-wiz`、`safari`、`firefox`、`img` 或 `youtube`；不同客户端返回的建议集合不同。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.priority` | Task priority | Execution priority of the task; higher priority is processed sooner at a higher price. | 任务的执行优先级；更高优先级处理更快、价格更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_data` | Postback datatype; possible value: advanced | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## post_dataforseo_serp_google_autocomplete_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Autocomplete Advanced. Returns Google Autocomplete suggestions in real time. Each Live SERP API call can contain only one task. | Return Google Autocomplete suggestions in real time in the same response; each Live SERP call carries exactly one task. | 即时返回 Google 自动补全建议，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Keyword to get autocomplete suggestions for | Seed term to fetch autocomplete suggestions for. | 用于获取自动补全建议的种子词。 |
| `req.client` | Search client for autocomplete | Autocomplete source client to emulate, such as `chrome`, `chrome-omni`, `gws-wiz`, `safari`, `firefox`, `img`, or `youtube`; each client returns a different suggestion set. | 要模拟的自动补全来源客户端，如 `chrome`、`chrome-omni`、`gws-wiz`、`safari`、`firefox`、`img` 或 `youtube`；不同客户端返回的建议集合不同。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_dataset_search_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Dataset Search Tasks. Returns Google Dataset Search results for the specified keyword. Your account is charged only for setting a task. | Queue a Google Dataset Search task that returns datasets matching the keyword; charged only for posting. | 提交一个 Google 数据集搜索（Dataset Search）任务，返回与 keyword 匹配的数据集；仅按提交计费。 |
| `req.keyword` | Keyword to search datasets for | Search term used to find matching datasets. | 用于查找匹配数据集的搜索词。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.os` | Device operating system, such as windows or macos | Operating system to emulate for the chosen device, refining the user-agent presented to Google. | 为所选设备模拟的操作系统，用于细化向 Google 呈现的 user-agent。 |
| `req.last_updated` | Last time the dataset was updated, such as 1m, 1y, or 3y | Filter datasets by how recently they were updated, expressed as a relative window such as `1m`, `1y`, or `3y`. | 按数据集的最近更新时间筛选，使用相对时间窗口表示，如 `1m`、`1y`、`3y`。 |
| `req.file_formats` | Dataset file formats, such as other, archive, text, image, document, or tabular | Filter datasets by file format, such as `other`, `archive`, `text`, `image`, `document`, or `tabular`. | 按文件格式筛选数据集，如 `other`、`archive`、`text`、`image`、`document` 或 `tabular`。 |
| `req.usage_rights` | Usage rights, such as commercial or noncommercial | Filter datasets by usage rights, such as `commercial` or `noncommercial`. | 按使用权限筛选数据集，如 `commercial` 或 `noncommercial`。 |
| `req.priority` | Task priority | Execution priority of the task; higher priority is processed sooner at a higher price. | 任务的执行优先级；更高优先级处理更快、价格更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_data` | Postback datatype; possible value: advanced | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## post_dataforseo_serp_google_dataset_search_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Dataset Search Advanced. Returns Google Dataset Search results in real time. Each Live SERP API call can contain only one task. | Return Google Dataset Search results in real time in the same response; each Live SERP call carries exactly one task. | 即时返回 Google 数据集搜索结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Keyword to search datasets for | Search term used to find matching datasets. | 用于查找匹配数据集的搜索词。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.os` | Device operating system | Operating system to emulate for the chosen device, refining the user-agent presented to Google. | 为所选设备模拟的操作系统，用于细化向 Google 呈现的 user-agent。 |
| `req.last_updated` | Last updated filter | Filter datasets by how recently they were updated, expressed as a relative window such as `1m`, `1y`, or `3y`. | 按数据集的最近更新时间筛选，使用相对时间窗口表示，如 `1m`、`1y`、`3y`。 |
| `req.file_formats` | Dataset file formats | Filter datasets by file format, such as `other`, `archive`, `text`, `image`, `document`, or `tabular`. | 按文件格式筛选数据集，如 `other`、`archive`、`text`、`image`、`document` 或 `tabular`。 |
| `req.usage_rights` | Usage rights filter | Filter datasets by usage rights, such as `commercial` or `noncommercial`. | 按使用权限筛选数据集，如 `commercial` 或 `noncommercial`。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_dataset_info_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Dataset Info Tasks. Returns detailed information about the dataset specified in the request. Your account is charged only for setting a task. | Queue a Google Dataset Info task that returns detailed metadata about a specific dataset; charged only for posting. | 提交一个 Google 数据集信息（Dataset Info）任务，返回某个数据集的详细元数据；仅按提交计费。 |
| `req.dataset_id` | ID of the dataset; you can find it in the dataset URL or in a Google Dataset Search result | Identifier of the dataset to look up; find it in the dataset URL or in a Google Dataset Search result. | 要查询的数据集标识；可在数据集 URL 或 Google 数据集搜索结果中找到。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.device` | Device type; possible value: desktop | Device profile to emulate for the search, such as `desktop` or `mobile`; affects layout and result set. | 搜索时模拟的设备类型，如 `desktop` 或 `mobile`，会影响版式与结果集合。 |
| `req.priority` | Task priority | Execution priority of the task; higher priority is processed sooner at a higher price. | 任务的执行优先级；更高优先级处理更快、价格更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_data` | Postback datatype; possible value: advanced | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## post_dataforseo_serp_google_dataset_info_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Dataset Info Advanced. Returns Google Dataset Info results in real time. Each Live SERP API call can contain only one task. | Return Google Dataset Info results in real time in the same response; each Live SERP call carries exactly one task. | 即时返回 Google 数据集信息结果，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.dataset_id` | ID of the dataset | Identifier of the dataset to look up; find it in the dataset URL or in a Google Dataset Search result. | 要查询的数据集标识；可在数据集 URL 或 Google 数据集搜索结果中找到。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.device` | Device type; possible value: desktop | Device profile to emulate for the search, such as `desktop` or `mobile`; affects layout and result set. | 搜索时模拟的设备类型，如 `desktop` 或 `mobile`，会影响版式与结果集合。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## get_dataforseo_serp_google_ads_advertisers_locations

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Google Ads Advertisers Locations for SERP API. Returns supported locations. Your account is not charged for using this API. | Return the list of locations supported by the Google Ads Advertisers SERP API; this endpoint is free to call. | 返回 Google Ads Advertisers SERP API 支持的地区列表；该端点免费调用。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of available locations | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].location_code` | Location code | Location code applied to this result, echoed from the request. | 应用于本结果的地区代码，回显自请求。 |
| `resp.200.tasks[].result[].location_name` | Location name | Human-readable name of the supported location. | 受支持地区的可读名称。 |
| `resp.200.tasks[].result[].country_iso_code` | Country ISO code | ISO country code of the location. | 该地区的 ISO 国家代码。 |
| `resp.200.tasks[].result[].location_type` | Location type | Type/level of the location (e.g. country, region, city). | 地区的类型/层级（如国家、地区、城市）。 |

## post_dataforseo_serp_google_ads_advertisers_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Ads Advertisers SERP Tasks. Returns advertiser information from the Ads Transparency platform for the specified keyword and location. Your account is charged only for setting a task. | Queue a Google Ads Advertisers task that returns advertiser information from the Ads Transparency platform for a keyword and location; charged only for posting. | 提交一个 Google Ads Advertisers 任务，返回 Ads Transparency 平台上某 keyword 与地区下的广告主信息；仅按提交计费。 |
| `req.keyword` | Keyword to search advertisers for | Search term used to find matching advertisers. | 用于查找匹配广告主的搜索词。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.priority` | Task priority | Execution priority of the task; higher priority is processed sooner at a higher price. | 任务的执行优先级；更高优先级处理更快、价格更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the completed task results once the task finishes. | 任务完成后 DataForSEO 回调推送结果的你方接收端点。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify you that the task is complete, without sending the payload. | 任务完成时 DataForSEO 通知你方的 ping 端点，仅通知不发送结果数据。 |
| `req.postback_data` | Postback datatype; only advanced is supported | Result format delivered to `postback_url`; choose the variant (such as advanced or html) matching how you want results pushed. | 推送到 `postback_url` 的结果格式；按你期望的推送方式选择对应变体（如 advanced 或 html）。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of task objects | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Billed cost attributed to this task, in USD. | 归属于该任务的计费金额，单位美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_google_ads_search_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Ads Search SERP Completed Tasks. Returns completed Google Ads Search tasks that have not been collected yet. | List completed Google Ads Search tasks that have not yet been collected, each with the endpoint to fetch its advanced results. | 列出已完成但尚未收取的 Google Ads Search 任务，每项附带取高级结果的端点。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Task id of the completed task, ready to be collected. | 已完成、可收取任务的 task id。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative URL to call to collect this task's advanced results. | 用于收取该任务高级结果的相对 URL。 |

## get_dataforseo_serp_google_ads_search_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Ads Search Advanced Results by id. You can retrieve completed task results by task id within the retention period. | Retrieve advanced Google Ads Search results by task id within the retention period after the task was posted. | 在任务提交后的留存期内，按 task id 取回 Google Ads Search 的高级结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_ads_search_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Ads Search Advanced. Returns ads search data from Google Ads in real time. Each Live SERP API call can contain only one task. | Return Google Ads Search data in real time in the same response; identify the advertiser by advertiser_ids or by target domain. Each Live SERP call carries exactly one task. | 即时返回 Google Ads Search 数据，结果在同一响应中给出；通过 advertiser_ids 或 target 域名指定广告主。每次 Live SERP 调用仅含一个任务。 |
| `req.advertiser_ids` | Advertiser identifiers; required if target is not specified | Advertiser identifiers whose ads to retrieve; required when `target` is not provided. | 要检索其广告的广告主标识；未提供 `target` 时必填。 |
| `req.target` | Domain name associated with an advertiser account; required if advertiser_ids is not specified | Domain name associated with an advertiser account whose ads to retrieve; required when `advertiser_ids` is not provided. | 与某广告主账户关联的域名，用于检索其广告；未提供 `advertiser_ids` 时必填。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates of the target location, as `latitude,longitude`; used for fine-grained geo-targeting. | 目标地点的 GPS 坐标，格式为 `纬度,经度`，用于更精细的地理定向。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## get_dataforseo_serp_google_finance_explore_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Finance Explore SERP Completed Tasks. Returns completed Google Finance Explore tasks that have not been collected yet. | List completed Google Finance Explore tasks that have not yet been collected, each with the endpoints to fetch its advanced and HTML results. | 列出已完成但尚未收取的 Google Finance Explore 任务，每项附带取高级结果与 HTML 结果的端点。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Task id of the completed task, ready to be collected. | 已完成、可收取任务的 task id。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative URL to call to collect this task's advanced results. | 用于收取该任务高级结果的相对 URL。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting HTML results | Relative URL to call to collect this task's HTML results. | 用于收取该任务 HTML 结果的相对 URL。 |

## get_dataforseo_serp_google_finance_explore_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Finance Explore HTML Results by id. Returns HTML results for a previously posted task. | Retrieve the HTML results of a previously posted Google Finance Explore task by its id. | 按 task id 取回此前提交的 Google Finance Explore 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_finance_explore_live_html

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Finance Explore SERP HTML. Returns raw HTML from the Explore tab of Google Finance in real time. Each Live SERP API call can contain only one task. | Return the raw HTML of the Google Finance Explore tab in real time in the same response; each Live SERP call carries exactly one task. | 即时返回 Google Finance Explore 标签页的原始 HTML，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.device` | Device type; possible value: desktop | Device profile to emulate for the search, such as `desktop` or `mobile`; affects layout and result set. | 搜索时模拟的设备类型，如 `desktop` 或 `mobile`，会影响版式与结果集合。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## get_dataforseo_serp_google_finance_markets_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Finance Markets SERP Completed Tasks. Returns completed Google Finance Markets tasks that have not been collected yet. | List completed Google Finance Markets tasks that have not yet been collected, each with the endpoints to fetch its advanced and HTML results. | 列出已完成但尚未收取的 Google Finance Markets 任务，每项附带取高级结果与 HTML 结果的端点。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Task id of the completed task, ready to be collected. | 已完成、可收取任务的 task id。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative URL to call to collect this task's advanced results. | 用于收取该任务高级结果的相对 URL。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting HTML results | Relative URL to call to collect this task's HTML results. | 用于收取该任务 HTML 结果的相对 URL。 |

## get_dataforseo_serp_google_finance_markets_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Finance Markets HTML Results by id. Returns HTML results for a previously posted task. | Retrieve the HTML results of a previously posted Google Finance Markets task by its id. | 按 task id 取回此前提交的 Google Finance Markets 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_finance_markets_live_html

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Finance Markets SERP HTML. Returns raw HTML from the Markets tab of Google Finance in real time. Each Live SERP API call can contain only one task. | Return the raw HTML of the Google Finance Markets tab in real time in the same response; each Live SERP call carries exactly one task. | 即时返回 Google Finance Markets 标签页的原始 HTML，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.market_type` | Market type for the Markets tab | Which Google Finance Markets section to load (e.g. indexes, most-active, gainers/losers), selecting the market view to scrape. | 要加载的 Google Finance Markets 板块（如指数、最活跃、涨跌幅榜），用于选择要抓取的行情视图。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## get_dataforseo_serp_google_finance_quote_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Finance Quote SERP Completed Tasks. Returns completed Google Finance Quote tasks that have not been collected yet. | List completed Google Finance Quote tasks that have not yet been collected, each with the endpoints to fetch its advanced and HTML results. | 列出已完成但尚未收取的 Google Finance Quote 任务，每项附带取高级结果与 HTML 结果的端点。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Task id of the completed task, ready to be collected. | 已完成、可收取任务的 task id。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative URL to call to collect this task's advanced results. | 用于收取该任务高级结果的相对 URL。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting HTML results | Relative URL to call to collect this task's HTML results. | 用于收取该任务 HTML 结果的相对 URL。 |

## get_dataforseo_serp_google_finance_quote_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Finance Quote HTML Results by id. Returns HTML results for a previously posted task. | Retrieve the HTML results of a previously posted Google Finance Quote task by its id. | 按 task id 取回此前提交的 Google Finance Quote 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## post_dataforseo_serp_google_finance_quote_live_html

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Finance Quote SERP HTML. Returns raw HTML from the Quote tab of Google Finance in real time. Each Live SERP API call can contain only one task. | Return the raw HTML of the Google Finance Quote tab for a ticker symbol in real time in the same response; each Live SERP call carries exactly one task. | 即时返回某股票代码在 Google Finance Quote 标签页的原始 HTML，结果在同一响应中给出；每次 Live SERP 调用仅含一个任务。 |
| `req.keyword` | Ticker or stock symbol | Ticker or stock symbol to quote (e.g. `AAPL`); the SERP is built around this symbol. | 要查询行情的股票代码（如 `AAPL`）；SERP 围绕该代码构建。 |
| `req.location_name` | Full name of search engine location | Full text name of the search-engine location (e.g. `London,England,United Kingdom`); used to localize the SERP. | 搜索引擎地区的完整名称（如 `London,England,United Kingdom`），用于本地化 SERP。 |
| `req.location_code` | Search engine location code | Numeric code of the search-engine location; the code-based alternative to `location_name`, obtainable from the locations reference endpoint. | 搜索引擎地区的数字代码，是 `location_name` 的代码型替代写法，可从地区参考端点获取。 |
| `req.language_name` | Full name of search engine language | Full text name of the search-engine language (e.g. `English`); the SERP is returned in this language. | 搜索引擎语言的完整名称（如 `English`），SERP 以该语言返回。 |
| `req.language_code` | Search engine language code | Two-letter language code (e.g. `en`); the code-based alternative to `language_name`. | 两位语言代码（如 `en`），是 `language_name` 的代码型替代写法。 |
| `req.os` | Device operating system | Operating system to emulate for the chosen device, refining the user-agent presented to Google. | 为所选设备模拟的操作系统，用于细化向 Google 呈现的 user-agent。 |
| `req.window` | Time window for the quote graph | Time window of the price graph for the quote, controlling the historical range shown. | 报价价格走势图的时间窗口，控制展示的历史区间。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

## get_dataforseo_serp_google_finance_ticker_search_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Finance Ticker Search SERP Completed Tasks. Returns completed Google Finance Ticker Search tasks that have not been collected yet. | List completed Google Finance Ticker Search tasks that have not yet been collected, each with the endpoint to fetch its advanced results. | 列出已完成但尚未收取的 Google Finance Ticker Search 任务，每项附带取高级结果的端点。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Task id of the completed task, ready to be collected. | 已完成、可收取任务的 task id。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative URL to call to collect this task's advanced results. | 用于收取该任务高级结果的相对 URL。 |

## get_dataforseo_serp_google_finance_ticker_search_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Finance Ticker Search Results by id. Returns advanced ticker search results for a previously posted task. | Retrieve advanced Google Finance Ticker Search results for a previously posted task by its id. | 按 task id 取回此前提交任务的 Google Finance Ticker Search 高级结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task whose results you want to fetch, as returned in `tasks[].id` when the task was posted. | 要取结果的任务 UUID，即提交任务时 `tasks[].id` 返回的值。 |
| `resp.200.version` | The current version of the API | API version string that produced this response. | 生成本响应的 API 版本号。 |
| `resp.200.status_code` | General status code | Overall response status code; check it before reading the payload. | 本次响应的总体状态码；读取数据前应先检查。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying the overall status code. | 与总体状态码对应的可读说明文字。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time of the request, in seconds. | 本次请求的服务端执行耗时，单位秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total billed cost of this response across all tasks, in USD. | 本响应所有任务的合计计费金额，单位美元。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task entries contained in the `tasks` array. | `tasks` 数组中包含的任务条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many tasks finished with an error; if non-zero, inspect each task's own status fields. | 以错误结束的任务数量；若不为 0，需逐个检查任务自身的状态字段。 |
| `resp.200.tasks` | Array of tasks | List of task objects; one entry per task in the request. | 任务对象列表，请求中的每个任务对应一个条目。 |
| `resp.200.tasks[].id` | Task identifier | UUID of this task; reuse it to fetch the task's results from the matching task_get endpoint. | 该任务的 UUID；在对应 task_get 端点取该任务结果时复用。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code; check it to tell whether this individual task succeeded. | 单个任务的状态码，用于判断该任务是否成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status code. | 该任务状态码对应的可读说明文字。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload for this task; the actual SERP data is nested inside. | 该任务的结果载荷，实际的 SERP 数据嵌套于内。 |

