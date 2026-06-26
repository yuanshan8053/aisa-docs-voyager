# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 48 个接口，747 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## get_dataforseo_serp_google_organic_task_get_regular_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Organic SERP Results by id. Retrieve regular task results for a posted task within 30 days at no extra charge. | Retrieves the regular (lightweight) result of a previously posted Google Organic SERP task by its task id. Results stay retrievable for 30 days at no extra charge. | 按任务 id 获取此前提交的 Google 自然搜索（Organic）任务的 regular（精简）结果，结果 30 天内可免费重复拉取。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | API version | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Task cost in USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | Number of tasks returned | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | Number of tasks returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].result` | Result array for the task | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_organic_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Organic SERP Advanced Results by id. Retrieve advanced task results for a posted task within 30 days at no extra charge. | Retrieves the advanced (full structured) result of a posted Google Organic SERP task by its task id, including all parsed SERP elements. | 按任务 id 获取已提交的 Google 自然搜索（Organic）任务的 advanced（完整结构化）结果，含全部解析后的 SERP 元素。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | API version | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Task cost in USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | Number of tasks returned | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | Number of tasks returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].result` | Advanced result array for the task | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_organic_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Organic SERP Completed Tasks. Returns a list of completed standard tasks ready for retrieval. | Lists Google Organic SERP tasks that have finished and are ready to collect, returning the endpoints to fetch each one. | 列出已完成、可领取的 Google 自然搜索任务，并给出获取每个任务结果的端点。 |
| `resp.200.version` | API version | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Request cost in USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | Number of tasks returned | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | Number of tasks returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Completed task list | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Completed task identifier | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].endpoint_regular` | Regular results endpoint | Ready-to-call relative URL for fetching this task's regular (lightweight) results. | 可直接调用的相对 URL，用于获取该任务的 regular（精简）结果。 |
| `resp.200.tasks[].result[].endpoint_advanced` | Advanced results endpoint | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |
| `resp.200.tasks[].result[].endpoint_html` | HTML results endpoint | Ready-to-call relative URL for fetching this task's results as a raw HTML SERP page. | 可直接调用的相对 URL，用于获取该任务结果对应的原始 HTML SERP 页面。 |

## post_dataforseo_serp_google_organic_live_html

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Organic SERP HTML. Returns raw HTML immediately. Each Live SERP API call can contain only one task. | Runs a Google Organic SERP query in live mode and returns the rendered search results page as raw HTML in a single synchronous call. | 以实时模式执行 Google 自然搜索查询，单次同步调用直接返回渲染后的搜索结果页面（原始 HTML）。 |
| `req.url` | Direct URL of the search query | Direct Google search URL to parse instead of building the query from keyword/location/language parameters. Use one or the other. | 直接给出要解析的 Google 搜索 URL，替代用 keyword/location/language 拼装查询；两种方式二选一。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates to target, formatted as `latitude,longitude` (optionally with radius). Alternative to `location_name`/`location_code`. | 以 `纬度,经度`（可附半径）格式给出的 GPS 坐标定位，替代 `location_name`/`location_code`。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.device` | Device type: desktop or mobile | Device the SERP is emulated on, typically `desktop` or `mobile`. | 模拟抓取 SERP 所用的设备类型，通常为 `desktop` 或 `mobile`。 |
| `req.os` | Device operating system | Operating system to emulate for the chosen device, e.g. `windows`, `macos`, `android`, `ios`. | 为所选设备模拟的操作系统，如 `windows`、`macos`、`android`、`ios`。 |
| `req.se_domain` | Custom search engine domain | Custom Google domain to query, e.g. `google.co.uk`, overriding the domain inferred from location. | 自定义要查询的 Google 域名，如 `google.co.uk`，覆盖由地区推断出的默认域名。 |
| `req.depth` | Parsing depth, default 100, max 700 | Number of SERP results to parse. Larger depth returns more results and may cost more. | 要解析的 SERP 结果条数。深度越大返回越多，费用也可能更高。 |
| `req.max_crawl_pages` | Page crawl limit, max 100 | Maximum number of SERP pages to crawl for this query. | 本次查询最多抓取的 SERP 页面数。 |
| `req.search_param` | Additional parameters of the search query | Additional raw Google search parameters appended to the query (e.g. URL query-string fragments). | 追加到查询上的额外原生 Google 搜索参数（如 URL 查询串片段）。 |
| `req.load_async_ai_overview` | Load asynchronous AI overview | When true, additionally loads the asynchronously-rendered AI Overview block of the SERP. | 为 true 时，额外加载 SERP 中异步渲染的 AI Overview 区块。 |
| `req.expand_ai_overview` | Expand AI overview item | When true, expands the AI Overview item to capture its full expanded content. | 为 true 时，展开 AI Overview 条目以抓取其完整展开内容。 |
| `req.tag` | User-defined task identifier | User-defined label stored with the task and echoed back in results, for your own correlation. | 随任务保存并在结果中回显的用户自定义标签，供你自行关联对账。 |
| `resp.200.version` | API version | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Request cost in USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | Number of tasks returned | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | Number of tasks returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of live task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].result` | Result array containing HTML pages | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].items` | HTML page items | Array of result items for the page; each item wraps a rendered HTML SERP page. | 页面结果项数组，每个元素封装一份渲染后的 HTML SERP 页面。 |
| `resp.200.tasks[].result[].items[].html` | Raw HTML page content | Raw HTML markup of the rendered Google SERP page. | 渲染后的 Google SERP 页面的原始 HTML 标记。 |

## get_dataforseo_serp_google_ai_mode_languages

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | You will receive the list of languages by calling this API. Your account will not be charged for using this API. | Returns the list of languages supported by the Google AI Mode SERP endpoints. | 返回 Google AI Mode SERP 接口支持的语言列表。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of available languages | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].language_name` | Language name | Full human-readable language name, e.g. `English`. | 完整可读的语言名称，如 `English`。 |
| `resp.200.tasks[].result[].language_code` | Language code | Language code, e.g. `en`; use it as the `language_code` parameter when posting tasks. | 语言码，如 `en`；提交任务时作为 `language_code` 参数使用。 |

## get_dataforseo_serp_google_ai_mode_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Returns the list of completed tasks that have not been collected yet. If postback_url was specified, tasks appear here only when delivery to your server failed. You can make up to 20 API calls per minute and get up to 1000 tasks completed within the previous three days per call. | Lists completed Google AI Mode SERP tasks that are ready to collect. | 列出已完成、可领取的 Google AI Mode SERP 任务。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].time` | Execution time, seconds | Processing time for this individual task, as a duration string (seconds). | 处理该单个任务的耗时（秒，时长字符串）。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].path` | URL path | API path segments identifying the endpoint this task was routed to; useful when debugging. | 标识该任务所走接口的 API 路径片段，排错时有用。 |
| `resp.200.tasks[].data` | Contains the parameters passed in the request URL | Echo of the parameters this task was created with, making the response self-describing about its inputs. | 任务创建时所用参数的回显，使响应自带输入信息、便于核对。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].se` | Search engine specified when setting the task | Search engine the task targeted, e.g. `google`. | 任务所针对的搜索引擎，如 `google`。 |
| `resp.200.tasks[].result[].se_type` | Type of search engine | Result-set sub-type, e.g. `organic`, `maps`, `news`, `local_finder`. | 结果集子类型，如 `organic`、`maps`、`news`、`local_finder`。 |
| `resp.200.tasks[].result[].date_posted` | Date when the task was posted in UTC format | UTC timestamp of when the task was submitted, indicating result freshness. | 任务提交时刻的 UTC 时间戳，用于判断结果时效。 |
| `resp.200.tasks[].result[].tag` | User-defined task identifier | User-defined label attached at task creation, echoed back for client-side correlation. | 创建任务时设置的用户自定义标签，原样回显以便对账关联。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting SERP Advanced results | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting SERP HTML results | Ready-to-call relative URL for fetching this task's results as a raw HTML SERP page. | 可直接调用的相对 URL，用于获取该任务结果对应的原始 HTML SERP 页面。 |

## get_dataforseo_serp_google_ai_mode_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Retrieve Google AI Mode HTML results by task id. The task-get HTML endpoint is referenced from the AI Mode catalog and completed-task endpoint list; path placeholder normalized from $id to {id}. | Retrieves the HTML result of a posted Google AI Mode SERP task by its task id. | 按任务 id 获取已提交的 Google AI Mode SERP 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].time` | Execution time, seconds | Processing time for this individual task, as a duration string (seconds). | 处理该单个任务的耗时（秒，时长字符串）。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].path` | URL path | API path segments identifying the endpoint this task was routed to; useful when debugging. | 标识该任务所走接口的 API 路径片段，排错时有用。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the parameters this task was created with, making the response self-describing about its inputs. | 任务创建时所用参数的回显，使响应自带输入信息、便于核对。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## post_dataforseo_serp_google_ai_mode_live_html

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Returns raw HTML of Google AI Mode SERP results in real time. Each Live SERP API call can contain only one task. | Runs a Google AI Mode SERP query in live mode and returns the rendered page as raw HTML in one synchronous call. | 以实时模式执行 Google AI Mode 查询，单次同步调用返回渲染后的页面（原始 HTML）。 |
| `req.keyword` | Keyword; you can specify up to 700 characters | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_name` | Full name of search engine location; required if location_code or location_coordinate is not specified | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code; required if location_name or location_coordinate is not specified | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.location_coordinate` | GPS coordinates of a location; required if location_name or location_code is not specified | GPS coordinates to target, formatted as `latitude,longitude` (optionally with radius). Alternative to `location_name`/`location_code`. | 以 `纬度,经度`（可附半径）格式给出的 GPS 坐标定位，替代 `location_name`/`location_code`。 |
| `req.language_name` | Full name of search engine language; required if language_code is not specified | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.language_code` | Search engine language code; required if language_name is not specified | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.device` | Device type: desktop or mobile | Device the SERP is emulated on, typically `desktop` or `mobile`. | 模拟抓取 SERP 所用的设备类型，通常为 `desktop` 或 `mobile`。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].time` | Execution time, seconds | Processing time for this individual task, as a duration string (seconds). | 处理该单个任务的耗时（秒，时长字符串）。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].path` | URL path | API path segments identifying the endpoint this task was routed to; useful when debugging. | 标识该任务所走接口的 API 路径片段，排错时有用。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the parameters this task was created with, making the response self-describing about its inputs. | 任务创建时所用参数的回显，使响应自带输入信息、便于核对。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].keyword` | Keyword received in the POST array | Search keyword echoed from the POST request that produced this result. | 产生该结果的 POST 请求中回显的查询关键词。 |
| `resp.200.tasks[].result[].type` | Search engine type in the POST array | Search type echoed from the POST request, e.g. `ai_mode`. | POST 请求中回显的搜索类型，如 `ai_mode`。 |
| `resp.200.tasks[].result[].se_domain` | Search engine domain in the POST array | Search engine domain echoed from the POST request, e.g. `google.com`. | POST 请求中回显的搜索引擎域名，如 `google.com`。 |
| `resp.200.tasks[].result[].location_code` | Location code in the POST array | Location code echoed from the POST request used for this result. | 产生该结果时 POST 请求中回显的位置码。 |
| `resp.200.tasks[].result[].language_code` | Language code in the POST array | Language code echoed from the POST request used for this result. | 产生该结果时 POST 请求中回显的语言码。 |

## get_dataforseo_serp_google_maps_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Maps SERP Completed Tasks. Returns a list of completed tasks that have not been collected yet. Up to 1000 tasks completed within the previous 3 days can be returned per call. | Lists completed Google Maps SERP tasks that are ready to collect. | 列出已完成、可领取的 Google Maps SERP 任务。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].se` | Search engine specified when setting the task | Search engine the task targeted, e.g. `google`. | 任务所针对的搜索引擎，如 `google`。 |
| `resp.200.tasks[].result[].se_type` | Type of search engine | Result-set sub-type, e.g. `organic`, `maps`, `news`, `local_finder`. | 结果集子类型，如 `organic`、`maps`、`news`、`local_finder`。 |
| `resp.200.tasks[].result[].date_posted` | Date when the task was posted in UTC format | UTC timestamp of when the task was submitted, indicating result freshness. | 任务提交时刻的 UTC 时间戳，用于判断结果时效。 |
| `resp.200.tasks[].result[].tag` | User-defined task identifier | User-defined label attached at task creation, echoed back for client-side correlation. | 创建任务时设置的用户自定义标签，原样回显以便对账关联。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting SERP Advanced results | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |

## get_dataforseo_serp_google_maps_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Maps SERP Advanced Results by id. Results can be retrieved by task id within the retention window after posting the task. | Retrieves the advanced result of a posted Google Maps SERP task by its task id. | 按任务 id 获取已提交的 Google Maps SERP 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the parameters this task was created with, making the response self-describing about its inputs. | 任务创建时所用参数的回显，使响应自带输入信息、便于核对。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_local_finder_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Local Finder SERP Completed Tasks. Returns a list of completed tasks that have not been collected yet. Up to 1000 tasks completed within the previous 3 days can be returned per call. | Lists completed Google Local Finder SERP tasks that are ready to collect. | 列出已完成、可领取的 Google Local Finder SERP 任务。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].se` | Search engine specified when setting the task | Search engine the task targeted, e.g. `google`. | 任务所针对的搜索引擎，如 `google`。 |
| `resp.200.tasks[].result[].se_type` | Type of search engine | Result-set sub-type, e.g. `organic`, `maps`, `news`, `local_finder`. | 结果集子类型，如 `organic`、`maps`、`news`、`local_finder`。 |
| `resp.200.tasks[].result[].date_posted` | Date when the task was posted in UTC format | UTC timestamp of when the task was submitted, indicating result freshness. | 任务提交时刻的 UTC 时间戳，用于判断结果时效。 |
| `resp.200.tasks[].result[].tag` | User-defined task identifier | User-defined label attached at task creation, echoed back for client-side correlation. | 创建任务时设置的用户自定义标签，原样回显以便对账关联。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting SERP Advanced results | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting SERP HTML results | Ready-to-call relative URL for fetching this task's results as a raw HTML SERP page. | 可直接调用的相对 URL，用于获取该任务结果对应的原始 HTML SERP 页面。 |

## get_dataforseo_serp_google_local_finder_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Local Finder HTML Results by id. Returns HTML results for a previously posted task. | Retrieves the HTML result of a posted Google Local Finder SERP task by its task id. | 按任务 id 获取已提交的 Google Local Finder SERP 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## post_dataforseo_serp_google_local_finder_live_html

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Local Finder SERP HTML. Returns raw HTML of Google Local Finder SERP results in real time. Each Live SERP API call can contain only one task. | Runs a Google Local Finder query in live mode and returns the rendered page as raw HTML in one synchronous call. | 以实时模式执行 Google Local Finder 查询，单次同步调用返回渲染后的页面（原始 HTML）。 |
| `req.keyword` | Keyword to search for | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates to target, formatted as `latitude,longitude` (optionally with radius). Alternative to `location_name`/`location_code`. | 以 `纬度,经度`（可附半径）格式给出的 GPS 坐标定位，替代 `location_name`/`location_code`。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_news_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get News SERP Completed Tasks. Returns a list of completed tasks that have not been collected yet. Up to 1000 tasks completed within the previous 3 days can be returned per call. | Lists completed Google News SERP tasks that are ready to collect. | 列出已完成、可领取的 Google News SERP 任务。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].se` | Search engine specified when setting the task | Search engine the task targeted, e.g. `google`. | 任务所针对的搜索引擎，如 `google`。 |
| `resp.200.tasks[].result[].se_type` | Type of search engine | Result-set sub-type, e.g. `organic`, `maps`, `news`, `local_finder`. | 结果集子类型，如 `organic`、`maps`、`news`、`local_finder`。 |
| `resp.200.tasks[].result[].date_posted` | Date when the task was posted in UTC format | UTC timestamp of when the task was submitted, indicating result freshness. | 任务提交时刻的 UTC 时间戳，用于判断结果时效。 |
| `resp.200.tasks[].result[].tag` | User-defined task identifier | User-defined label attached at task creation, echoed back for client-side correlation. | 创建任务时设置的用户自定义标签，原样回显以便对账关联。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting SERP Advanced results | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting SERP HTML results | Ready-to-call relative URL for fetching this task's results as a raw HTML SERP page. | 可直接调用的相对 URL，用于获取该任务结果对应的原始 HTML SERP 页面。 |

## get_dataforseo_serp_google_news_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google News HTML Results by id. Returns HTML results for a previously posted task. | Retrieves the HTML result of a posted Google News SERP task by its task id. | 按任务 id 获取已提交的 Google News SERP 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## post_dataforseo_serp_google_news_live_html

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google News SERP HTML. Returns raw HTML of Google News SERP results in real time. Each Live SERP API call can contain only one task. | Runs a Google News SERP query in live mode and returns the rendered page as raw HTML in one synchronous call. | 以实时模式执行 Google News 查询，单次同步调用返回渲染后的页面（原始 HTML）。 |
| `req.keyword` | Keyword to search for | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates to target, formatted as `latitude,longitude` (optionally with radius). Alternative to `location_name`/`location_code`. | 以 `纬度,经度`（可附半径）格式给出的 GPS 坐标定位，替代 `location_name`/`location_code`。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_events_locations

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Google Events Locations for SERP API. Returns the list of supported locations for Google Events SERP. Your account is not charged for using this endpoint. | Returns the list of locations supported by the Google Events SERP endpoints, with their location codes. | 返回 Google Events SERP 接口支持的地区列表及其位置码。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of available locations | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].location_code` | Location code | Numeric location code; pass it as the `location_code` parameter to target this region in a task. | 数字位置码；提交任务时作为 `location_code` 参数传入即可定位该地区。 |
| `resp.200.tasks[].result[].location_name` | Location name | Full human-readable location name, e.g. `London,England,United Kingdom`. | 完整可读的位置名称，如 `London,England,United Kingdom`。 |
| `resp.200.tasks[].result[].location_code_parent` | Parent location code | Location code of the parent region in the geo hierarchy (e.g. country code for a city), or null at the top level. | 地理层级中上级地区的位置码（如城市对应的国家码），顶层时为 null。 |
| `resp.200.tasks[].result[].country_iso_code` | Country ISO code | ISO country code of the location, e.g. `GB`, `US`. | 该位置所属国家的 ISO 代码，如 `GB`、`US`。 |

## post_dataforseo_serp_google_events_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Events SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Creates a Google Events SERP task for asynchronous processing; poll `tasks_ready` and collect with `task_get`, or receive results via postback/pingback. | 创建 Google Events SERP 异步任务；可轮询 `tasks_ready` 后用 `task_get` 领取，或通过 postback/pingback 接收结果。 |
| `req.keyword` | Keyword to search for | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates to target, formatted as `latitude,longitude` (optionally with radius). Alternative to `location_name`/`location_code`. | 以 `纬度,经度`（可附半径）格式给出的 GPS 坐标定位，替代 `location_name`/`location_code`。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.priority` | Task priority | Task execution priority that controls how quickly the task is picked up for processing; higher priority is handled sooner and may cost more. | 任务执行优先级，决定任务被调度处理的快慢；优先级越高越早处理，费用也可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO POSTs the completed task results to, removing the need to poll. | DataForSEO 在任务完成后将结果 POST 到的你方端点，可免去主动轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO notifies (pings) when the task completes, so you can then fetch results. | 任务完成时 DataForSEO 通知（ping）的你方端点，收到后再去拉取结果。 |
| `req.postback_data` | Postback datatype | Result format delivered to `postback_url`, selecting which payload variant (e.g. `regular`, `advanced`, `html`) is sent. | 投递到 `postback_url` 的结果格式，用于选择发送的结果变体（如 `regular`、`advanced`、`html`）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |

## post_dataforseo_serp_google_images_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Images SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Creates a Google Images SERP task for asynchronous processing; collect via `tasks_ready` + `task_get` or postback/pingback. | 创建 Google Images SERP 异步任务；通过 `tasks_ready` + `task_get` 或 postback/pingback 领取结果。 |
| `req.keyword` | Keyword to search for | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates to target, formatted as `latitude,longitude` (optionally with radius). Alternative to `location_name`/`location_code`. | 以 `纬度,经度`（可附半径）格式给出的 GPS 坐标定位，替代 `location_name`/`location_code`。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.device` | Device type: desktop or mobile | Device the SERP is emulated on, typically `desktop` or `mobile`. | 模拟抓取 SERP 所用的设备类型，通常为 `desktop` 或 `mobile`。 |
| `req.priority` | Task priority | Task execution priority that controls how quickly the task is picked up for processing; higher priority is handled sooner and may cost more. | 任务执行优先级，决定任务被调度处理的快慢；优先级越高越早处理，费用也可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO POSTs the completed task results to, removing the need to poll. | DataForSEO 在任务完成后将结果 POST 到的你方端点，可免去主动轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO notifies (pings) when the task completes, so you can then fetch results. | 任务完成时 DataForSEO 通知（ping）的你方端点，收到后再去拉取结果。 |
| `req.postback_data` | Postback datatype; possible values include regular, advanced, html | Result format delivered to `postback_url`, selecting which payload variant (e.g. `regular`, `advanced`, `html`) is sent. | 投递到 `postback_url` 的结果格式，用于选择发送的结果变体（如 `regular`、`advanced`、`html`）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |

## get_dataforseo_serp_google_images_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Images HTML Results by id. Returns HTML results for a previously posted task. | Retrieves the HTML result of a posted Google Images SERP task by its task id. | 按任务 id 获取已提交的 Google Images SERP 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## post_dataforseo_serp_google_images_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Images SERP. Returns Google Images SERP results in real time. Each Live SERP API call can contain only one task. | Runs a Google Images SERP query in live mode and returns advanced structured results in one synchronous call. | 以实时模式执行 Google Images 查询，单次同步调用返回 advanced 结构化结果。 |
| `req.keyword` | Keyword to search for | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates to target, formatted as `latitude,longitude` (optionally with radius). Alternative to `location_name`/`location_code`. | 以 `纬度,经度`（可附半径）格式给出的 GPS 坐标定位，替代 `location_name`/`location_code`。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.device` | Device type: desktop or mobile | Device the SERP is emulated on, typically `desktop` or `mobile`. | 模拟抓取 SERP 所用的设备类型，通常为 `desktop` 或 `mobile`。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_search_by_image_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Search By Image SERP Completed Tasks. Returns a list of completed tasks that have not been collected yet. Up to 1000 tasks completed within the previous 3 days can be returned per call. | Lists completed Google Search-by-Image SERP tasks that are ready to collect. | 列出已完成、可领取的 Google 以图搜图（Search by Image）SERP 任务。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].se` | Search engine specified when setting the task | Search engine the task targeted, e.g. `google`. | 任务所针对的搜索引擎，如 `google`。 |
| `resp.200.tasks[].result[].se_type` | Type of search engine | Result-set sub-type, e.g. `organic`, `maps`, `news`, `local_finder`. | 结果集子类型，如 `organic`、`maps`、`news`、`local_finder`。 |
| `resp.200.tasks[].result[].date_posted` | Date when the task was posted in UTC format | UTC timestamp of when the task was submitted, indicating result freshness. | 任务提交时刻的 UTC 时间戳，用于判断结果时效。 |
| `resp.200.tasks[].result[].tag` | User-defined task identifier | User-defined label attached at task creation, echoed back for client-side correlation. | 创建任务时设置的用户自定义标签，原样回显以便对账关联。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting SERP Advanced results | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting SERP HTML results | Ready-to-call relative URL for fetching this task's results as a raw HTML SERP page. | 可直接调用的相对 URL，用于获取该任务结果对应的原始 HTML SERP 页面。 |

## get_dataforseo_serp_google_search_by_image_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Search By Image HTML Results by id. Returns HTML results for a previously posted task. | Retrieves the HTML result of a posted Google Search-by-Image SERP task by its task id. | 按任务 id 获取已提交的 Google 以图搜图 SERP 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_jobs_locations

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Google Jobs Locations for SERP API. Returns the list of supported locations for Google Jobs SERP. Your account is not charged for using this endpoint. | Returns the list of locations supported by the Google Jobs SERP endpoints, with their location codes. | 返回 Google Jobs SERP 接口支持的地区列表及其位置码。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of available locations | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].location_code` | Location code | Numeric location code; pass it as the `location_code` parameter to target this region in a task. | 数字位置码；提交任务时作为 `location_code` 参数传入即可定位该地区。 |
| `resp.200.tasks[].result[].location_name` | Location name | Full human-readable location name, e.g. `London,England,United Kingdom`. | 完整可读的位置名称，如 `London,England,United Kingdom`。 |
| `resp.200.tasks[].result[].location_code_parent` | Parent location code | Location code of the parent region in the geo hierarchy (e.g. country code for a city), or null at the top level. | 地理层级中上级地区的位置码（如城市对应的国家码），顶层时为 null。 |
| `resp.200.tasks[].result[].country_iso_code` | Country ISO code | ISO country code of the location, e.g. `GB`, `US`. | 该位置所属国家的 ISO 代码，如 `GB`、`US`。 |

## get_dataforseo_serp_google_jobs_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Jobs SERP Completed Tasks. Returns a list of completed tasks that have not been collected yet. Up to 1000 tasks completed within the previous 3 days can be returned per call. | Lists completed Google Jobs SERP tasks that are ready to collect. | 列出已完成、可领取的 Google Jobs SERP 任务。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].se` | Search engine specified when setting the task | Search engine the task targeted, e.g. `google`. | 任务所针对的搜索引擎，如 `google`。 |
| `resp.200.tasks[].result[].se_type` | Type of search engine | Result-set sub-type, e.g. `organic`, `maps`, `news`, `local_finder`. | 结果集子类型，如 `organic`、`maps`、`news`、`local_finder`。 |
| `resp.200.tasks[].result[].date_posted` | Date when the task was posted in UTC format | UTC timestamp of when the task was submitted, indicating result freshness. | 任务提交时刻的 UTC 时间戳，用于判断结果时效。 |
| `resp.200.tasks[].result[].tag` | User-defined task identifier | User-defined label attached at task creation, echoed back for client-side correlation. | 创建任务时设置的用户自定义标签，原样回显以便对账关联。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting SERP Advanced results | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting SERP HTML results | Ready-to-call relative URL for fetching this task's results as a raw HTML SERP page. | 可直接调用的相对 URL，用于获取该任务结果对应的原始 HTML SERP 页面。 |

## get_dataforseo_serp_google_jobs_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Jobs HTML Results by id. Returns HTML results for a previously posted task. | Retrieves the HTML result of a posted Google Jobs SERP task by its task id. | 按任务 id 获取已提交的 Google Jobs SERP 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result` | Array of HTML results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_autocomplete_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Autocomplete SERP Completed Tasks. Returns completed Google Autocomplete tasks that have not been collected yet. | Lists completed Google Autocomplete SERP tasks that are ready to collect. | 列出已完成、可领取的 Google Autocomplete SERP 任务。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |

## get_dataforseo_serp_google_autocomplete_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Autocomplete Advanced Results by id. You can retrieve completed task results by task id within the retention period. | Retrieves the advanced result of a posted Google Autocomplete SERP task by its task id. | 按任务 id 获取已提交的 Google Autocomplete SERP 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the parameters this task was created with, making the response self-describing about its inputs. | 任务创建时所用参数的回显，使响应自带输入信息、便于核对。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_dataset_search_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Dataset Search SERP Completed Tasks. Returns completed Google Dataset Search tasks that have not been collected yet. | Lists completed Google Dataset Search SERP tasks that are ready to collect. | 列出已完成、可领取的 Google Dataset Search SERP 任务。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |

## get_dataforseo_serp_google_dataset_search_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Dataset Search Advanced Results by id. You can retrieve completed task results by task id within the retention period. | Retrieves the advanced result of a posted Google Dataset Search SERP task by its task id. | 按任务 id 获取已提交的 Google Dataset Search SERP 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the parameters this task was created with, making the response self-describing about its inputs. | 任务创建时所用参数的回显，使响应自带输入信息、便于核对。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_dataset_info_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Dataset Info SERP Completed Tasks. Returns completed Google Dataset Info tasks that have not been collected yet. | Lists completed Google Dataset Info SERP tasks that are ready to collect. | 列出已完成、可领取的 Google Dataset Info SERP 任务。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |

## get_dataforseo_serp_google_dataset_info_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Dataset Info Advanced Results by id. You can retrieve completed task results by task id within the retention period. | Retrieves the advanced result of a posted Google Dataset Info SERP task by its task id. | 按任务 id 获取已提交的 Google Dataset Info SERP 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the parameters this task was created with, making the response self-describing about its inputs. | 任务创建时所用参数的回显，使响应自带输入信息、便于核对。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_ads_advertisers_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Ads Advertisers SERP Completed Tasks. Returns completed Google Ads Advertisers tasks that have not been collected yet. | Lists completed Google Ads Advertisers SERP tasks that are ready to collect. | 列出已完成、可领取的 Google Ads Advertisers SERP 任务。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of completed task references | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | Identifier of a completed task; feed it to the corresponding `task_get` endpoint to download its full payload. | 已完成任务的标识；传给对应的 `task_get` 接口即可下载完整结果。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Ready-to-call relative URL for fetching this task's advanced (full structured) results. | 可直接调用的相对 URL，用于获取该任务的 advanced（完整结构化）结果。 |

## get_dataforseo_serp_google_ads_advertisers_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Ads Advertisers Advanced Results by id. You can retrieve completed task results by task id within the retention period. | Retrieves the advanced result of a posted Google Ads Advertisers SERP task by its task id. | 按任务 id 获取已提交的 Google Ads Advertisers SERP 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].items` | Array of advertisers or domains returned in SERP | Array of advertiser or domain records returned in the SERP for the queried advertiser. | 针对所查广告主，在 SERP 中返回的广告主或域名记录数组。 |

## post_dataforseo_serp_google_ads_advertisers_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Ads Advertisers Advanced. Returns advertiser information from Google Ads in real time. Each Live SERP API call can contain only one task. | Runs a Google Ads Advertisers lookup in live mode and returns advanced structured results in one synchronous call. | 以实时模式执行 Google Ads Advertisers 查询，单次同步调用返回 advanced 结构化结果。 |
| `req.keyword` | Keyword to search advertisers for | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## get_dataforseo_serp_google_ads_search_locations

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Google Ads Search Locations for SERP API. Returns supported locations. Your account is not charged for using this API. | Returns the list of locations supported by the Google Ads Search endpoints, with their location codes. | 返回 Google Ads Search 接口支持的地区列表及其位置码。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of available locations | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |
| `resp.200.tasks[].result[].location_code` | Location code | Numeric location code; pass it as the `location_code` parameter to target this region in a task. | 数字位置码；提交任务时作为 `location_code` 参数传入即可定位该地区。 |
| `resp.200.tasks[].result[].location_name` | Location name | Full human-readable location name, e.g. `London,England,United Kingdom`. | 完整可读的位置名称，如 `London,England,United Kingdom`。 |
| `resp.200.tasks[].result[].country_iso_code` | Country ISO code | ISO country code of the location, e.g. `GB`, `US`. | 该位置所属国家的 ISO 代码，如 `GB`、`US`。 |

## post_dataforseo_serp_google_ads_search_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Ads Search SERP Tasks. Returns ads run by advertisers on Google Ads. Historical data is available from 2018-05-31. Your account is charged only for setting a task. | Creates a Google Ads Search task for asynchronous processing; collect via `tasks_ready` + `task_get` or postback/pingback. Target by advertiser ids or domain. | 创建 Google Ads Search 异步任务；通过 `tasks_ready` + `task_get` 或 postback/pingback 领取结果。可按广告主 ID 或域名定位。 |
| `req.advertiser_ids` | Advertiser identifiers; required if target is not specified | List of advertiser identifiers to search ads for. Provide either `advertiser_ids` or `target`. | 要检索其广告的广告主标识列表。与 `target` 二选一。 |
| `req.target` | Domain name associated with an advertiser account; required if advertiser_ids is not specified | Domain name associated with an advertiser account to search ads for. Provide either `target` or `advertiser_ids`. | 与广告主账号关联、用于检索广告的域名。与 `advertiser_ids` 二选一。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.location_coordinate` | GPS coordinates of a location | GPS coordinates to target, formatted as `latitude,longitude` (optionally with radius). Alternative to `location_name`/`location_code`. | 以 `纬度,经度`（可附半径）格式给出的 GPS 坐标定位，替代 `location_name`/`location_code`。 |
| `req.priority` | Task priority | Task execution priority that controls how quickly the task is picked up for processing; higher priority is handled sooner and may cost more. | 任务执行优先级，决定任务被调度处理的快慢；优先级越高越早处理，费用也可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO POSTs the completed task results to, removing the need to poll. | DataForSEO 在任务完成后将结果 POST 到的你方端点，可免去主动轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO notifies (pings) when the task completes, so you can then fetch results. | 任务完成时 DataForSEO 通知（ping）的你方端点，收到后再去拉取结果。 |
| `req.postback_data` | Postback datatype; only advanced is supported | Result format delivered to `postback_url`, selecting which payload variant (e.g. `regular`, `advanced`, `html`) is sent. | 投递到 `postback_url` 的结果格式，用于选择发送的结果变体（如 `regular`、`advanced`、`html`）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |

## post_dataforseo_serp_google_finance_explore_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Finance Explore SERP Tasks. Provides real-time data from the Explore tab of Google Finance for the specified location and language. | Creates a Google Finance Explore task for asynchronous processing; collect via `tasks_ready` + `task_get` or postback/pingback. | 创建 Google Finance Explore 异步任务；通过 `tasks_ready` + `task_get` 或 postback/pingback 领取结果。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.device` | Device type; possible value: desktop | Device the SERP is emulated on, typically `desktop` or `mobile`. | 模拟抓取 SERP 所用的设备类型，通常为 `desktop` 或 `mobile`。 |
| `req.priority` | Task priority | Task execution priority that controls how quickly the task is picked up for processing; higher priority is handled sooner and may cost more. | 任务执行优先级，决定任务被调度处理的快慢；优先级越高越早处理，费用也可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO POSTs the completed task results to, removing the need to poll. | DataForSEO 在任务完成后将结果 POST 到的你方端点，可免去主动轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO notifies (pings) when the task completes, so you can then fetch results. | 任务完成时 DataForSEO 通知（ping）的你方端点，收到后再去拉取结果。 |
| `req.postback_data` | Postback datatype; possible values: advanced, html | Result format delivered to `postback_url`, selecting which payload variant (e.g. `regular`, `advanced`, `html`) is sent. | 投递到 `postback_url` 的结果格式，用于选择发送的结果变体（如 `regular`、`advanced`、`html`）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |

## get_dataforseo_serp_google_finance_explore_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Finance Explore Advanced Results by id. You can retrieve completed task results by task id within the retention period. | Retrieves the advanced result of a posted Google Finance Explore task by its task id. | 按任务 id 获取已提交的 Google Finance Explore 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## post_dataforseo_serp_google_finance_explore_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Finance Explore Advanced. Returns Google Finance Explore results in real time. Each Live SERP API call can contain only one task. | Runs a Google Finance Explore query in live mode and returns advanced structured results in one synchronous call. | 以实时模式执行 Google Finance Explore 查询，单次同步调用返回 advanced 结构化结果。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.device` | Device type; possible value: desktop | Device the SERP is emulated on, typically `desktop` or `mobile`. | 模拟抓取 SERP 所用的设备类型，通常为 `desktop` 或 `mobile`。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## post_dataforseo_serp_google_finance_markets_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Finance Markets SERP Tasks. Provides real-time data from the Markets tab of Google Finance for the specified location, language, and market type. | Creates a Google Finance Markets task for asynchronous processing; collect via `tasks_ready` + `task_get` or postback/pingback. | 创建 Google Finance Markets 异步任务；通过 `tasks_ready` + `task_get` 或 postback/pingback 领取结果。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.market_type` | Market type for the Markets tab | Which Markets tab to fetch in Google Finance (e.g. indexes, most active, gainers, losers).<br>[⚠️Note:源码未声明 market_type 的可选枚举值，具体取值待研发确认。] | 要抓取的 Google Finance Markets 标签页类别（如指数、最活跃、涨幅榜、跌幅榜等）。<br>[⚠️批注:源码未声明 market_type 的可选枚举值，具体取值待研发确认。] |
| `req.priority` | Task priority | Task execution priority that controls how quickly the task is picked up for processing; higher priority is handled sooner and may cost more. | 任务执行优先级，决定任务被调度处理的快慢；优先级越高越早处理，费用也可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO POSTs the completed task results to, removing the need to poll. | DataForSEO 在任务完成后将结果 POST 到的你方端点，可免去主动轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO notifies (pings) when the task completes, so you can then fetch results. | 任务完成时 DataForSEO 通知（ping）的你方端点，收到后再去拉取结果。 |
| `req.postback_data` | Postback datatype; possible values: advanced, html | Result format delivered to `postback_url`, selecting which payload variant (e.g. `regular`, `advanced`, `html`) is sent. | 投递到 `postback_url` 的结果格式，用于选择发送的结果变体（如 `regular`、`advanced`、`html`）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |

## get_dataforseo_serp_google_finance_markets_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Finance Markets Advanced Results by id. You can retrieve completed task results by task id within the retention period. | Retrieves the advanced result of a posted Google Finance Markets task by its task id. | 按任务 id 获取已提交的 Google Finance Markets 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## post_dataforseo_serp_google_finance_markets_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Finance Markets Advanced. Returns Google Finance Markets results in real time. Each Live SERP API call can contain only one task. | Runs a Google Finance Markets query in live mode and returns advanced structured results in one synchronous call. | 以实时模式执行 Google Finance Markets 查询，单次同步调用返回 advanced 结构化结果。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.market_type` | Market type for the Markets tab | Which Markets tab to fetch in Google Finance (e.g. indexes, most active, gainers, losers).<br>[⚠️Note:源码未声明 market_type 的可选枚举值，具体取值待研发确认。] | 要抓取的 Google Finance Markets 标签页类别（如指数、最活跃、涨幅榜、跌幅榜等）。<br>[⚠️批注:源码未声明 market_type 的可选枚举值，具体取值待研发确认。] |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## post_dataforseo_serp_google_finance_quote_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Finance Quote SERP Tasks. Provides real-time data from the Quote tab of Google Finance for the specified ticker, location, and language. | Creates a Google Finance Quote task for a ticker/stock symbol for asynchronous processing; collect via `tasks_ready` + `task_get` or postback/pingback. | 针对某个股票代码创建 Google Finance Quote 异步任务；通过 `tasks_ready` + `task_get` 或 postback/pingback 领取结果。 |
| `req.keyword` | Ticker or stock symbol | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.os` | Device operating system | Operating system to emulate for the chosen device, e.g. `windows`, `macos`, `android`, `ios`. | 为所选设备模拟的操作系统，如 `windows`、`macos`、`android`、`ios`。 |
| `req.window` | Time window for the quote graph, such as 1D, 5D, 1M, 6M, YTD, 1Y, 5Y, or MAX | Time window for the quote price graph, such as `1D`, `5D`, `1M`, `6M`, `YTD`, `1Y`, `5Y` or `MAX`. | 报价走势图的时间窗口，如 `1D`、`5D`、`1M`、`6M`、`YTD`、`1Y`、`5Y` 或 `MAX`。 |
| `req.priority` | Task priority | Task execution priority that controls how quickly the task is picked up for processing; higher priority is handled sooner and may cost more. | 任务执行优先级，决定任务被调度处理的快慢；优先级越高越早处理，费用也可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO POSTs the completed task results to, removing the need to poll. | DataForSEO 在任务完成后将结果 POST 到的你方端点，可免去主动轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO notifies (pings) when the task completes, so you can then fetch results. | 任务完成时 DataForSEO 通知（ping）的你方端点，收到后再去拉取结果。 |
| `req.postback_data` | Postback datatype; possible values: advanced, html | Result format delivered to `postback_url`, selecting which payload variant (e.g. `regular`, `advanced`, `html`) is sent. | 投递到 `postback_url` 的结果格式，用于选择发送的结果变体（如 `regular`、`advanced`、`html`）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |

## get_dataforseo_serp_google_finance_quote_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Google Finance Quote Advanced Results by id. You can retrieve completed task results by task id within the retention period. | Retrieves the advanced result of a posted Google Finance Quote task by its task id. | 按任务 id 获取已提交的 Google Finance Quote 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | Identifier (UUID) of the previously posted task whose results you want to retrieve. | 此前提交、要获取其结果的任务的标识（UUID）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## post_dataforseo_serp_google_finance_quote_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Finance Quote Advanced. Returns Google Finance Quote results in real time. Each Live SERP API call can contain only one task. | Runs a Google Finance Quote lookup for a ticker in live mode and returns advanced structured results in one synchronous call. | 以实时模式查询某股票代码的 Google Finance Quote，单次同步调用返回 advanced 结构化结果。 |
| `req.keyword` | Ticker or stock symbol | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.os` | Device operating system | Operating system to emulate for the chosen device, e.g. `windows`, `macos`, `android`, `ios`. | 为所选设备模拟的操作系统，如 `windows`、`macos`、`android`、`ios`。 |
| `req.window` | Time window for the quote graph | Time window for the quote price graph, such as `1D`, `5D`, `1M`, `6M`, `YTD`, `1Y`, `5Y` or `MAX`. | 报价走势图的时间窗口，如 `1D`、`5D`、`1M`、`6M`、`YTD`、`1Y`、`5Y` 或 `MAX`。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

## post_dataforseo_serp_google_finance_ticker_search_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Google Finance Ticker Search Tasks. Allows searching for financial instruments available on Google Finance by company or instrument name. | Creates a Google Finance Ticker Search task (find tickers by company/instrument name) for asynchronous processing. | 创建 Google Finance Ticker Search 异步任务（按公司/金融工具名称查找代码）。 |
| `req.keyword` | Company or financial instrument name | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `req.priority` | Task priority | Task execution priority that controls how quickly the task is picked up for processing; higher priority is handled sooner and may cost more. | 任务执行优先级，决定任务被调度处理的快慢；优先级越高越早处理，费用也可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO POSTs the completed task results to, removing the need to poll. | DataForSEO 在任务完成后将结果 POST 到的你方端点，可免去主动轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO notifies (pings) when the task completes, so you can then fetch results. | 任务完成时 DataForSEO 通知（ping）的你方端点，收到后再去拉取结果。 |
| `req.postback_data` | Postback datatype; possible value: advanced | Result format delivered to `postback_url`, selecting which payload variant (e.g. `regular`, `advanced`, `html`) is sent. | 投递到 `postback_url` 的结果格式，用于选择发送的结果变体（如 `regular`、`advanced`、`html`）。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of task objects in the `tasks` array. | `tasks` 数组中的任务对象数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | Number of tasks that finished with an error; `0` means all tasks succeeded. | 以错误结束的任务数量，`0` 表示全部任务成功。 |
| `resp.200.tasks` | Array of task objects | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | Unique task identifier (UUID). Pass it to the matching `task_get` endpoint to download the completed result. | 任务唯一标识（UUID）。传给对应的 `task_get` 接口即可下载已完成的结果。 |
| `resp.200.tasks[].status_code` | Task status code | Status code of this individual task; `20000` means the task itself succeeded. | 单个任务的状态码，`20000` 表示该任务自身成功。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable status text for this individual task. | 该单个任务状态码对应的可读文本。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单个任务按美元计的费用。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of elements in this task's `result` array. | 该任务 `result` 数组中的元素数量。 |

## post_dataforseo_serp_google_finance_ticker_search_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Google Finance Ticker Search Advanced. Returns Google Finance Ticker Search results in real time. Each Live SERP API call can contain only one task. | Runs a Google Finance Ticker Search in live mode and returns advanced structured results in one synchronous call. | 以实时模式执行 Google Finance Ticker Search 查询，单次同步调用返回 advanced 结构化结果。 |
| `req.keyword` | Company or financial instrument name | Search query string to run against Google. | 要在 Google 上执行的查询关键词。 |
| `req.location_name` | Full name of search engine location | Full location name to target, e.g. `London,England,United Kingdom`. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的完整地区名称，如 `London,England,United Kingdom`。`location_name`、`location_code`、`location_coordinate` 三者择一。 |
| `req.location_code` | Search engine location code | Numeric location code to target; obtainable from the matching `.../locations` endpoint. Provide either `location_name`, `location_code` or `location_coordinate`. | 要定位的数字位置码，可从对应的 `.../locations` 接口获取。与 `location_name`、`location_coordinate` 三者择一。 |
| `req.language_name` | Full name of search engine language | Full language name to use, e.g. `English`. Provide either `language_name` or `language_code`. | 要使用的完整语言名称，如 `English`。与 `language_code` 二选一。 |
| `req.language_code` | Search engine language code | Language code to use, e.g. `en`; obtainable from the matching `.../languages` endpoint. Provide either `language_name` or `language_code`. | 要使用的语言码，如 `en`，可从对应的 `.../languages` 接口获取。与 `language_name` 二选一。 |
| `resp.200.version` | The current version of the API | Version of the DataForSEO API that produced this response, e.g. `0.1.20240101`. Handy for reproducibility and support tickets. | 生成本次响应的 DataForSEO API 版本号，如 `0.1.20240101`，便于复现与提交工单。 |
| `resp.200.status_code` | General status code | Overall status code for the whole response. `20000` means the call succeeded; any other value signals a request-level failure (auth, quota, malformed payload) — see `status_message`. | 整个响应的总体状态码。`20000` 表示调用成功；其它值表示请求级失败（鉴权、配额、报文格式等），详情见 `status_message`。 |
| `resp.200.status_message` | General informational message | Human-readable text for `status_code`: `Ok.` on success, or the failure reason otherwise. | 与 `status_code` 配套的可读文本，成功为 `Ok.`，否则为失败原因。 |
| `resp.200.time` | Execution time, seconds | Total server-side processing time for the response, as a duration string such as `0.1234 sec`. | 服务端处理本次响应的总耗时，形如 `0.1234 sec` 的时长字符串。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this request in USD, aggregated over all tasks in the response. | 本次请求按美元计的总费用，为响应内全部任务费用之和。 |
| `resp.200.tasks` | Array of tasks | Container array holding one object per task, each carrying its own status and `result` payload. | 任务容器数组，每个元素对应一个任务，内含各自的状态与 `result` 数据。 |
| `resp.200.tasks[].result` | Array of live SERP results | Result payload array for this task; element shape depends on the endpoint (SERP items, task references, locations, languages, etc.). | 该任务的结果数组，元素结构随接口而异（SERP 条目、任务引用、地区、语言等）。 |

