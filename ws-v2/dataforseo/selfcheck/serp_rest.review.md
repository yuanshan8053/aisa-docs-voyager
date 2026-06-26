# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 59 个接口，795 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## get_dataforseo_serp_bing_locations

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Bing Locations for SERP. Returns the list of supported locations for Bing SERP. Your account is not charged for using this endpoint. | List the locations supported for Bing SERP requests; use a returned code or name to geo-target tasks. This endpoint is free. | 列出 Bing SERP 请求支持的地区；用返回的代码或名称对任务做地域定位。该接口免费。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of available locations | List of locations supported for this search engine's SERP. Use a returned `location_code` (or `location_name`) when posting tasks to target that locale. | 该搜索引擎 SERP 支持的地区列表。提交任务时用其中的 `location_code`（或 `location_name`）来锁定目标地区。 |
| `resp.200.tasks[].result[].location_code` | Location code | Numeric code identifying the location; pass it as the `location_code` request field to geo-target a task. | 标识地区的数字代码；作为请求字段 `location_code` 传入以对任务做地域定位。 |
| `resp.200.tasks[].result[].location_name` | Location name | Human-readable full name of the location; corresponds to the `location_name` request field. | 地区的可读全名；对应请求字段 `location_name`。 |
| `resp.200.tasks[].result[].location_code_parent` | Parent location code | Code of the enclosing (parent) location, e.g. the country a city belongs to; helps build a location hierarchy. | 上级（父）地区的代码，例如城市所属的国家，可用于构建地区层级。 |
| `resp.200.tasks[].result[].country_iso_code` | Country ISO code | ISO 3166-1 country code of the location, e.g. `US`. | 该地区所属国家的 ISO 3166-1 代码，如 `US`。 |

## get_dataforseo_serp_bing_languages

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Bing Languages for SERP. Returns the list of supported languages for Bing SERP. Your account is not charged for using this endpoint. | List the languages supported for Bing SERP requests; use a returned code or name when posting tasks. This endpoint is free. | 列出 Bing SERP 请求支持的语言；提交任务时使用返回的代码或名称。该接口免费。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of available languages | List of languages supported for this search engine's SERP. Use a returned `language_code` (or `language_name`) when posting tasks. | 该搜索引擎 SERP 支持的语言列表。提交任务时使用其中的 `language_code`（或 `language_name`）。 |
| `resp.200.tasks[].result[].language_name` | Language name | Human-readable full name of the language; corresponds to the `language_name` request field. | 语言的可读全名；对应请求字段 `language_name`。 |
| `resp.200.tasks[].result[].language_code` | Language code | Code identifying the language; pass it as the `language_code` request field. | 标识语言的代码；作为请求字段 `language_code` 传入。 |

## post_dataforseo_serp_bing_organic_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Bing Organic SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Queue an organic SERP task for Bing; you are charged only for posting, can send up to 100 tasks per call, and collect results later by task id or via postback/pingback. | 提交 Bing 自然搜索 SERP 任务；仅在提交时计费，每次调用最多 100 个任务，稍后按任务 id 或通过 postback/pingback 领取结果。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `req.depth` | Parsing depth | How many SERP results to parse; higher values return more results and may affect task cost. | 解析的 SERP 结果条数；值越大返回结果越多，并可能影响任务费用。 |
| `req.priority` | Task priority | Execution priority of the queued task; a higher priority makes the task run sooner and may cost more. | 排队任务的执行优先级；优先级越高任务越早执行，费用可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the task result once it is ready, so you do not have to poll. | 任务完成后由 DataForSEO 主动回推结果的你方接收地址，从而无需轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify that the task is complete (without the payload); you then collect results via `task_get`. | 任务完成时由 DataForSEO 回调通知（不含结果数据）的你方地址；收到通知后再用 `task_get` 领取结果。 |
| `req.postback_data` | Postback datatype; possible values: regular, advanced, html | Result format to deliver to `postback_url`; choose the result type that matches how you will consume the data. | 回推到 `postback_url` 的结果格式；选择与你消费方式相匹配的结果类型。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of task objects | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单任务的扣费金额，单位为美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_bing_organic_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Organic SERP Completed Tasks. Returns completed Bing Organic SERP tasks that have not been collected yet. | List Bing tasks that have finished but have not yet been collected, with the URLs to fetch each result. | 列出 Bing 已完成但尚未领取的任务，并给出领取各结果的 URL。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | List of completed-but-uncollected tasks. Each entry exposes the URLs to fetch its results. | 已完成但尚未领取的任务列表；每个条目给出领取结果的 URL。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | UUID of a completed task ready for collection; feed it to the matching `task_get` endpoint. | 可领取的已完成任务的 UUID；传给对应的 `task_get` 接口。 |
| `resp.200.tasks[].result[].endpoint_regular` | URL for collecting regular results | Relative API path for collecting this task's regular results. | 领取该任务 regular 结果的相对 API 路径。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative API path for collecting this task's advanced results. | 领取该任务 advanced 结果的相对 API 路径。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting HTML results | Relative API path for collecting this task's HTML results. | 领取该任务 HTML 结果的相对 API 路径。 |

## get_dataforseo_serp_bing_organic_task_get_regular_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Bing Organic SERP Results by id (regular). Returns regular SERP results for a previously posted Bing Organic task. | Collect the regular results of a previously posted Bing task by its id. | 按任务 id 领取此前提交的 Bing 任务的 regular 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of regular SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_bing_organic_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Bing Organic SERP Results by id (advanced). Returns advanced SERP results for a previously posted Bing Organic task. | Collect the advanced results of a previously posted Bing task by its id. | 按任务 id 领取此前提交的 Bing 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_bing_organic_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Bing Organic HTML Results by id. Returns HTML results for a previously posted Bing Organic task. | Collect the HTML results of a previously posted Bing task by its id. | 按任务 id 领取此前提交的 Bing 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## post_dataforseo_serp_bing_organic_live_html

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Bing Organic SERP HTML. Returns raw HTML of Bing Organic SERP results in real time. Each Live SERP API call can contain only one task. | Return raw HTML of Bing organic SERP results synchronously in one call; each Live call carries exactly one task. | 在一次调用中同步返回 Bing 自然搜索 SERP 的原始 HTML；每个 Live 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | The SERP payload generated in real time for this Live request. Its inner shape depends on the result type and search engine, so it is returned as an open array. | 本次 Live 请求实时生成的 SERP 结果数据。其内部结构取决于结果类型与搜索引擎，故以开放数组返回。 |

## post_dataforseo_serp_bing_organic_live_regular

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Bing Organic SERP Regular. Returns regular Bing Organic SERP results in real time. Each Live SERP API call can contain only one task. | Return regular Bing organic SERP results synchronously in one call; each Live call carries exactly one task. | 在一次调用中同步返回 Bing 自然搜索 SERP 的 regular 结果；每个 Live 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of regular SERP results | The SERP payload generated in real time for this Live request. Its inner shape depends on the result type and search engine, so it is returned as an open array. | 本次 Live 请求实时生成的 SERP 结果数据。其内部结构取决于结果类型与搜索引擎，故以开放数组返回。 |

## post_dataforseo_serp_bing_organic_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Bing Organic SERP Advanced. Returns advanced Bing Organic SERP results in real time. Each Live SERP API call can contain only one task. | Return advanced Bing organic SERP results synchronously in one call; each Live call carries exactly one task. | 在一次调用中同步返回 Bing 自然搜索 SERP 的 advanced 结果；每个 Live 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The SERP payload generated in real time for this Live request. Its inner shape depends on the result type and search engine, so it is returned as an open array. | 本次 Live 请求实时生成的 SERP 结果数据。其内部结构取决于结果类型与搜索引擎，故以开放数组返回。 |

## get_dataforseo_serp_youtube_locations

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of YouTube Locations for SERP. Returns the list of supported locations for YouTube SERP. Your account is not charged for using this endpoint. | List the locations supported for YouTube SERP requests; use a returned code or name to geo-target tasks. This endpoint is free. | 列出 YouTube SERP 请求支持的地区；用返回的代码或名称对任务做地域定位。该接口免费。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of available locations | List of locations supported for this search engine's SERP. Use a returned `location_code` (or `location_name`) when posting tasks to target that locale. | 该搜索引擎 SERP 支持的地区列表。提交任务时用其中的 `location_code`（或 `location_name`）来锁定目标地区。 |
| `resp.200.tasks[].result[].location_code` | Location code | Numeric code identifying the location; pass it as the `location_code` request field to geo-target a task. | 标识地区的数字代码；作为请求字段 `location_code` 传入以对任务做地域定位。 |
| `resp.200.tasks[].result[].location_name` | Location name | Human-readable full name of the location; corresponds to the `location_name` request field. | 地区的可读全名；对应请求字段 `location_name`。 |
| `resp.200.tasks[].result[].location_code_parent` | Parent location code | Code of the enclosing (parent) location, e.g. the country a city belongs to; helps build a location hierarchy. | 上级（父）地区的代码，例如城市所属的国家，可用于构建地区层级。 |
| `resp.200.tasks[].result[].country_iso_code` | Country ISO code | ISO 3166-1 country code of the location, e.g. `US`. | 该地区所属国家的 ISO 3166-1 代码，如 `US`。 |

## get_dataforseo_serp_youtube_languages

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of YouTube Languages for SERP. Returns the list of supported languages for YouTube SERP. Your account is not charged for using this endpoint. | List the languages supported for YouTube SERP requests; use a returned code or name when posting tasks. This endpoint is free. | 列出 YouTube SERP 请求支持的语言；提交任务时使用返回的代码或名称。该接口免费。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of available languages | List of languages supported for this search engine's SERP. Use a returned `language_code` (or `language_name`) when posting tasks. | 该搜索引擎 SERP 支持的语言列表。提交任务时使用其中的 `language_code`（或 `language_name`）。 |
| `resp.200.tasks[].result[].language_name` | Language name | Human-readable full name of the language; corresponds to the `language_name` request field. | 语言的可读全名；对应请求字段 `language_name`。 |
| `resp.200.tasks[].result[].language_code` | Language code | Code identifying the language; pass it as the `language_code` request field. | 标识语言的代码；作为请求字段 `language_code` 传入。 |

## post_dataforseo_serp_youtube_video_info_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting YouTube Video Info Tasks. Provides detailed information about the specified YouTube video. Your account is charged only for setting a task. | Queue a task to fetch detailed metadata for a YouTube video; you are charged only for posting and collect results later by task id. | 提交任务以获取某 YouTube 视频的详细元数据；仅在提交时计费，稍后按任务 id 领取结果。 |
| `req.video_id` | ID of the video | Identifier of the target YouTube video (the `v` value in a watch URL). Required to fetch info, organic, subtitle, or comment data for that video. | 目标 YouTube 视频的标识（观看链接中的 `v` 值）。获取该视频的信息、自然结果、字幕或评论时必填。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type; only desktop is supported | Device profile to emulate. Only desktop is supported for this endpoint. | 搜索时模拟的设备类型；本接口仅支持 desktop。 |
| `req.priority` | Task priority | Execution priority of the queued task; a higher priority makes the task run sooner and may cost more. | 排队任务的执行优先级；优先级越高任务越早执行，费用可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the task result once it is ready, so you do not have to poll. | 任务完成后由 DataForSEO 主动回推结果的你方接收地址，从而无需轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify that the task is complete (without the payload); you then collect results via `task_get`. | 任务完成时由 DataForSEO 回调通知（不含结果数据）的你方地址；收到通知后再用 `task_get` 领取结果。 |
| `req.postback_data` | Postback datatype; possible value: advanced | Result format to deliver to `postback_url`. Only the advanced result type is available for this endpoint. | 回推到 `postback_url` 的结果格式；本接口仅提供 advanced 结果类型。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of task objects | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单任务的扣费金额，单位为美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_youtube_video_info_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Video Info SERP Completed Tasks. Returns completed YouTube Video Info tasks that have not been collected yet. | List YouTube tasks that have finished but have not yet been collected, with the URLs to fetch each result. | 列出 YouTube 已完成但尚未领取的任务，并给出领取各结果的 URL。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | List of completed-but-uncollected tasks. Each entry exposes the URLs to fetch its results. | 已完成但尚未领取的任务列表；每个条目给出领取结果的 URL。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | UUID of a completed task ready for collection; feed it to the matching `task_get` endpoint. | 可领取的已完成任务的 UUID；传给对应的 `task_get` 接口。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative API path for collecting this task's advanced results. | 领取该任务 advanced 结果的相对 API 路径。 |

## get_dataforseo_serp_youtube_video_info_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get YouTube Video Info Results by id. Returns advanced video info results for a previously posted task. | Collect the advanced results of a previously posted YouTube task by its id. | 按任务 id 领取此前提交的 YouTube 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## post_dataforseo_serp_youtube_video_info_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live YouTube Video Info Advanced. Returns detailed information about a YouTube video in real time. Each Live SERP API call can contain only one task. | Return detailed YouTube video metadata synchronously in one call; each Live call carries exactly one task. | 在一次调用中同步返回 YouTube 视频的详细元数据；每个 Live 调用仅含一个任务。 |
| `req.video_id` | ID of the video | Identifier of the target YouTube video (the `v` value in a watch URL). Required to fetch info, organic, subtitle, or comment data for that video. | 目标 YouTube 视频的标识（观看链接中的 `v` 值）。获取该视频的信息、自然结果、字幕或评论时必填。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type; only desktop is supported | Device profile to emulate. Only desktop is supported for this endpoint. | 搜索时模拟的设备类型；本接口仅支持 desktop。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | The SERP payload generated in real time for this Live request. Its inner shape depends on the result type and search engine, so it is returned as an open array. | 本次 Live 请求实时生成的 SERP 结果数据。其内部结构取决于结果类型与搜索引擎，故以开放数组返回。 |

## post_dataforseo_serp_youtube_organic_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting YouTube Organic Tasks. Returns organic YouTube search results for the specified keyword. Your account is charged only for setting a task. | Queue a task to fetch YouTube organic search results for a keyword; you are charged only for posting and collect results later by task id. | 提交任务以按关键词获取 YouTube 自然搜索结果；仅在提交时计费，稍后按任务 id 领取结果。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.priority` | Task priority | Execution priority of the queued task; a higher priority makes the task run sooner and may cost more. | 排队任务的执行优先级；优先级越高任务越早执行，费用可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the task result once it is ready, so you do not have to poll. | 任务完成后由 DataForSEO 主动回推结果的你方接收地址，从而无需轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify that the task is complete (without the payload); you then collect results via `task_get`. | 任务完成时由 DataForSEO 回调通知（不含结果数据）的你方地址；收到通知后再用 `task_get` 领取结果。 |
| `req.postback_data` | Postback datatype; possible value: advanced | Result format to deliver to `postback_url`. Only the advanced result type is available for this endpoint. | 回推到 `postback_url` 的结果格式；本接口仅提供 advanced 结果类型。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of task objects | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单任务的扣费金额，单位为美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_youtube_organic_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Organic SERP Completed Tasks. Returns completed YouTube Organic tasks that have not been collected yet. | List YouTube tasks that have finished but have not yet been collected, with the URLs to fetch each result. | 列出 YouTube 已完成但尚未领取的任务，并给出领取各结果的 URL。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | List of completed-but-uncollected tasks. Each entry exposes the URLs to fetch its results. | 已完成但尚未领取的任务列表；每个条目给出领取结果的 URL。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | UUID of a completed task ready for collection; feed it to the matching `task_get` endpoint. | 可领取的已完成任务的 UUID；传给对应的 `task_get` 接口。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative API path for collecting this task's advanced results. | 领取该任务 advanced 结果的相对 API 路径。 |

## get_dataforseo_serp_youtube_organic_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get YouTube Organic Results by id. Returns advanced YouTube Organic results for a previously posted task. | Collect the advanced results of a previously posted YouTube task by its id. | 按任务 id 领取此前提交的 YouTube 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## post_dataforseo_serp_youtube_organic_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live YouTube Organic Advanced. Returns YouTube Organic search results in real time. Each Live SERP API call can contain only one task. | Return YouTube organic search results synchronously in one call; each Live call carries exactly one task. | 在一次调用中同步返回 YouTube 自然搜索结果；每个 Live 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | The SERP payload generated in real time for this Live request. Its inner shape depends on the result type and search engine, so it is returned as an open array. | 本次 Live 请求实时生成的 SERP 结果数据。其内部结构取决于结果类型与搜索引擎，故以开放数组返回。 |

## post_dataforseo_serp_youtube_video_subtitles_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting YouTube Subtitles Tasks. Returns subtitles for a specified YouTube video. Your account is charged only for setting a task. | Queue a task to retrieve subtitles for a YouTube video; you are charged only for posting and collect results later by task id. | 提交任务以获取某 YouTube 视频的字幕；仅在提交时计费，稍后按任务 id 领取结果。 |
| `req.video_id` | ID of the video | Identifier of the target YouTube video (the `v` value in a watch URL). Required to fetch info, organic, subtitle, or comment data for that video. | 目标 YouTube 视频的标识（观看链接中的 `v` 值）。获取该视频的信息、自然结果、字幕或评论时必填。 |
| `req.language_code` | Subtitle language code | Language code of the subtitle track to retrieve for the video. | 要获取的视频字幕轨道的语言代码。 |
| `req.priority` | Task priority | Execution priority of the queued task; a higher priority makes the task run sooner and may cost more. | 排队任务的执行优先级；优先级越高任务越早执行，费用可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the task result once it is ready, so you do not have to poll. | 任务完成后由 DataForSEO 主动回推结果的你方接收地址，从而无需轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify that the task is complete (without the payload); you then collect results via `task_get`. | 任务完成时由 DataForSEO 回调通知（不含结果数据）的你方地址；收到通知后再用 `task_get` 领取结果。 |
| `req.postback_data` | Postback datatype; possible value: advanced | Result format to deliver to `postback_url`. Only the advanced result type is available for this endpoint. | 回推到 `postback_url` 的结果格式；本接口仅提供 advanced 结果类型。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of task objects | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单任务的扣费金额，单位为美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_youtube_video_subtitles_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Video Subtitles SERP Completed Tasks. Returns completed YouTube Subtitles tasks that have not been collected yet. | List YouTube tasks that have finished but have not yet been collected, with the URLs to fetch each result. | 列出 YouTube 已完成但尚未领取的任务，并给出领取各结果的 URL。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | List of completed-but-uncollected tasks. Each entry exposes the URLs to fetch its results. | 已完成但尚未领取的任务列表；每个条目给出领取结果的 URL。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | UUID of a completed task ready for collection; feed it to the matching `task_get` endpoint. | 可领取的已完成任务的 UUID；传给对应的 `task_get` 接口。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative API path for collecting this task's advanced results. | 领取该任务 advanced 结果的相对 API 路径。 |

## get_dataforseo_serp_youtube_video_subtitles_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get YouTube Subtitles Results by id. Returns subtitle results for a previously posted task. | Collect the advanced results of a previously posted YouTube task by its id. | 按任务 id 领取此前提交的 YouTube 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## post_dataforseo_serp_youtube_video_subtitles_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live YouTube Subtitles Advanced. Returns YouTube subtitle data in real time. Each Live SERP API call can contain only one task. | Return YouTube video subtitles synchronously in one call; each Live call carries exactly one task. | 在一次调用中同步返回 YouTube 视频字幕；每个 Live 调用仅含一个任务。 |
| `req.video_id` | ID of the video | Identifier of the target YouTube video (the `v` value in a watch URL). Required to fetch info, organic, subtitle, or comment data for that video. | 目标 YouTube 视频的标识（观看链接中的 `v` 值）。获取该视频的信息、自然结果、字幕或评论时必填。 |
| `req.language_code` | Subtitle language code | Language code of the subtitle track to retrieve for the video. | 要获取的视频字幕轨道的语言代码。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | The SERP payload generated in real time for this Live request. Its inner shape depends on the result type and search engine, so it is returned as an open array. | 本次 Live 请求实时生成的 SERP 结果数据。其内部结构取决于结果类型与搜索引擎，故以开放数组返回。 |

## post_dataforseo_serp_youtube_video_comments_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting YouTube Comments Tasks. Returns comments for a specified YouTube video. Your account is charged only for setting a task. | Queue a task to retrieve comments for a YouTube video; you are charged only for posting and collect results later by task id. | 提交任务以获取某 YouTube 视频的评论；仅在提交时计费，稍后按任务 id 领取结果。 |
| `req.video_id` | ID of the video | Identifier of the target YouTube video (the `v` value in a watch URL). Required to fetch info, organic, subtitle, or comment data for that video. | 目标 YouTube 视频的标识（观看链接中的 `v` 值）。获取该视频的信息、自然结果、字幕或评论时必填。 |
| `req.priority` | Task priority | Execution priority of the queued task; a higher priority makes the task run sooner and may cost more. | 排队任务的执行优先级；优先级越高任务越早执行，费用可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the task result once it is ready, so you do not have to poll. | 任务完成后由 DataForSEO 主动回推结果的你方接收地址，从而无需轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify that the task is complete (without the payload); you then collect results via `task_get`. | 任务完成时由 DataForSEO 回调通知（不含结果数据）的你方地址；收到通知后再用 `task_get` 领取结果。 |
| `req.postback_data` | Postback datatype; possible value: advanced | Result format to deliver to `postback_url`. Only the advanced result type is available for this endpoint. | 回推到 `postback_url` 的结果格式；本接口仅提供 advanced 结果类型。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of task objects | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单任务的扣费金额，单位为美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_youtube_video_comments_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Video Comments SERP Completed Tasks. Returns completed YouTube Comments tasks that have not been collected yet. | List YouTube tasks that have finished but have not yet been collected, with the URLs to fetch each result. | 列出 YouTube 已完成但尚未领取的任务，并给出领取各结果的 URL。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | List of completed-but-uncollected tasks. Each entry exposes the URLs to fetch its results. | 已完成但尚未领取的任务列表；每个条目给出领取结果的 URL。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | UUID of a completed task ready for collection; feed it to the matching `task_get` endpoint. | 可领取的已完成任务的 UUID；传给对应的 `task_get` 接口。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative API path for collecting this task's advanced results. | 领取该任务 advanced 结果的相对 API 路径。 |

## get_dataforseo_serp_youtube_video_comments_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get YouTube Comments Results by id. Returns comment results for a previously posted task. | Collect the advanced results of a previously posted YouTube task by its id. | 按任务 id 领取此前提交的 YouTube 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## post_dataforseo_serp_youtube_video_comments_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live YouTube Comments Advanced. Returns YouTube comment data in real time. Each Live SERP API call can contain only one task. | Return YouTube video comments synchronously in one call; each Live call carries exactly one task. | 在一次调用中同步返回 YouTube 视频评论；每个 Live 调用仅含一个任务。 |
| `req.video_id` | ID of the video | Identifier of the target YouTube video (the `v` value in a watch URL). Required to fetch info, organic, subtitle, or comment data for that video. | 目标 YouTube 视频的标识（观看链接中的 `v` 值）。获取该视频的信息、自然结果、字幕或评论时必填。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of live SERP results | The SERP payload generated in real time for this Live request. Its inner shape depends on the result type and search engine, so it is returned as an open array. | 本次 Live 请求实时生成的 SERP 结果数据。其内部结构取决于结果类型与搜索引擎，故以开放数组返回。 |

## get_dataforseo_serp_baidu_locations

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Baidu Locations for SERP. Returns the list of supported locations for Baidu SERP. Your account is not charged for using this endpoint. | List the locations supported for Baidu SERP requests; use a returned code or name to geo-target tasks. This endpoint is free. | 列出 百度 SERP 请求支持的地区；用返回的代码或名称对任务做地域定位。该接口免费。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of available locations | List of locations supported for this search engine's SERP. Use a returned `location_code` (or `location_name`) when posting tasks to target that locale. | 该搜索引擎 SERP 支持的地区列表。提交任务时用其中的 `location_code`（或 `location_name`）来锁定目标地区。 |
| `resp.200.tasks[].result[].location_code` | Location code | Numeric code identifying the location; pass it as the `location_code` request field to geo-target a task. | 标识地区的数字代码；作为请求字段 `location_code` 传入以对任务做地域定位。 |
| `resp.200.tasks[].result[].location_name` | Location name | Human-readable full name of the location; corresponds to the `location_name` request field. | 地区的可读全名；对应请求字段 `location_name`。 |
| `resp.200.tasks[].result[].location_code_parent` | Parent location code | Code of the enclosing (parent) location, e.g. the country a city belongs to; helps build a location hierarchy. | 上级（父）地区的代码，例如城市所属的国家，可用于构建地区层级。 |
| `resp.200.tasks[].result[].country_iso_code` | Country ISO code | ISO 3166-1 country code of the location, e.g. `US`. | 该地区所属国家的 ISO 3166-1 代码，如 `US`。 |

## get_dataforseo_serp_baidu_languages

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Baidu Languages for SERP. Returns the list of supported languages for Baidu SERP. Your account is not charged for using this endpoint. | List the languages supported for Baidu SERP requests; use a returned code or name when posting tasks. This endpoint is free. | 列出 百度 SERP 请求支持的语言；提交任务时使用返回的代码或名称。该接口免费。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of available languages | List of languages supported for this search engine's SERP. Use a returned `language_code` (or `language_name`) when posting tasks. | 该搜索引擎 SERP 支持的语言列表。提交任务时使用其中的 `language_code`（或 `language_name`）。 |
| `resp.200.tasks[].result[].language_name` | Language name | Human-readable full name of the language; corresponds to the `language_name` request field. | 语言的可读全名；对应请求字段 `language_name`。 |
| `resp.200.tasks[].result[].language_code` | Language code | Code identifying the language; pass it as the `language_code` request field. | 标识语言的代码；作为请求字段 `language_code` 传入。 |

## post_dataforseo_serp_baidu_organic_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Baidu Organic SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Queue an organic SERP task for Baidu; you are charged only for posting, can send up to 100 tasks per call, and collect results later by task id or via postback/pingback. | 提交 百度 自然搜索 SERP 任务；仅在提交时计费，每次调用最多 100 个任务，稍后按任务 id 或通过 postback/pingback 领取结果。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `req.depth` | Parsing depth | How many SERP results to parse; higher values return more results and may affect task cost. | 解析的 SERP 结果条数；值越大返回结果越多，并可能影响任务费用。 |
| `req.priority` | Task priority | Execution priority of the queued task; a higher priority makes the task run sooner and may cost more. | 排队任务的执行优先级；优先级越高任务越早执行，费用可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the task result once it is ready, so you do not have to poll. | 任务完成后由 DataForSEO 主动回推结果的你方接收地址，从而无需轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify that the task is complete (without the payload); you then collect results via `task_get`. | 任务完成时由 DataForSEO 回调通知（不含结果数据）的你方地址；收到通知后再用 `task_get` 领取结果。 |
| `req.postback_data` | Postback datatype; possible values: regular, advanced, html | Result format to deliver to `postback_url`; choose the result type that matches how you will consume the data. | 回推到 `postback_url` 的结果格式；选择与你消费方式相匹配的结果类型。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of task objects | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单任务的扣费金额，单位为美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_baidu_organic_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Organic SERP Completed Tasks. Returns completed Baidu Organic SERP tasks that have not been collected yet. | List Baidu tasks that have finished but have not yet been collected, with the URLs to fetch each result. | 列出 百度 已完成但尚未领取的任务，并给出领取各结果的 URL。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | List of completed-but-uncollected tasks. Each entry exposes the URLs to fetch its results. | 已完成但尚未领取的任务列表；每个条目给出领取结果的 URL。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | UUID of a completed task ready for collection; feed it to the matching `task_get` endpoint. | 可领取的已完成任务的 UUID；传给对应的 `task_get` 接口。 |
| `resp.200.tasks[].result[].endpoint_regular` | URL for collecting regular results | Relative API path for collecting this task's regular results. | 领取该任务 regular 结果的相对 API 路径。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative API path for collecting this task's advanced results. | 领取该任务 advanced 结果的相对 API 路径。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting HTML results | Relative API path for collecting this task's HTML results. | 领取该任务 HTML 结果的相对 API 路径。 |

## get_dataforseo_serp_baidu_organic_task_get_regular_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Baidu Organic SERP Results by id (regular). Returns regular SERP results for a previously posted Baidu Organic task. | Collect the regular results of a previously posted Baidu task by its id. | 按任务 id 领取此前提交的 百度 任务的 regular 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of regular SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_baidu_organic_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Baidu Organic SERP Advanced Results by id. Returns advanced SERP results for a previously posted Baidu Organic task. | Collect the advanced results of a previously posted Baidu task by its id. | 按任务 id 领取此前提交的 百度 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_baidu_organic_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Baidu Organic HTML Results by id. Returns HTML results for a previously posted Baidu Organic task. | Collect the HTML results of a previously posted Baidu task by its id. | 按任务 id 领取此前提交的 百度 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_yahoo_locations

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Yahoo Locations for SERP. Returns the list of supported locations for Yahoo SERP. Your account is not charged for using this endpoint. | List the locations supported for Yahoo SERP requests; use a returned code or name to geo-target tasks. This endpoint is free. | 列出 Yahoo SERP 请求支持的地区；用返回的代码或名称对任务做地域定位。该接口免费。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of available locations | List of locations supported for this search engine's SERP. Use a returned `location_code` (or `location_name`) when posting tasks to target that locale. | 该搜索引擎 SERP 支持的地区列表。提交任务时用其中的 `location_code`（或 `location_name`）来锁定目标地区。 |
| `resp.200.tasks[].result[].location_code` | Location code | Numeric code identifying the location; pass it as the `location_code` request field to geo-target a task. | 标识地区的数字代码；作为请求字段 `location_code` 传入以对任务做地域定位。 |
| `resp.200.tasks[].result[].location_name` | Location name | Human-readable full name of the location; corresponds to the `location_name` request field. | 地区的可读全名；对应请求字段 `location_name`。 |
| `resp.200.tasks[].result[].location_code_parent` | Parent location code | Code of the enclosing (parent) location, e.g. the country a city belongs to; helps build a location hierarchy. | 上级（父）地区的代码，例如城市所属的国家，可用于构建地区层级。 |
| `resp.200.tasks[].result[].country_iso_code` | Country ISO code | ISO 3166-1 country code of the location, e.g. `US`. | 该地区所属国家的 ISO 3166-1 代码，如 `US`。 |

## get_dataforseo_serp_yahoo_languages

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Yahoo Languages for SERP. Returns the list of supported languages for Yahoo SERP. Your account is not charged for using this endpoint. | List the languages supported for Yahoo SERP requests; use a returned code or name when posting tasks. This endpoint is free. | 列出 Yahoo SERP 请求支持的语言；提交任务时使用返回的代码或名称。该接口免费。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of available languages | List of languages supported for this search engine's SERP. Use a returned `language_code` (or `language_name`) when posting tasks. | 该搜索引擎 SERP 支持的语言列表。提交任务时使用其中的 `language_code`（或 `language_name`）。 |
| `resp.200.tasks[].result[].language_name` | Language name | Human-readable full name of the language; corresponds to the `language_name` request field. | 语言的可读全名；对应请求字段 `language_name`。 |
| `resp.200.tasks[].result[].language_code` | Language code | Code identifying the language; pass it as the `language_code` request field. | 标识语言的代码；作为请求字段 `language_code` 传入。 |

## post_dataforseo_serp_yahoo_organic_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Yahoo Organic SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Queue an organic SERP task for Yahoo; you are charged only for posting, can send up to 100 tasks per call, and collect results later by task id or via postback/pingback. | 提交 Yahoo 自然搜索 SERP 任务；仅在提交时计费，每次调用最多 100 个任务，稍后按任务 id 或通过 postback/pingback 领取结果。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `req.depth` | Parsing depth | How many SERP results to parse; higher values return more results and may affect task cost. | 解析的 SERP 结果条数；值越大返回结果越多，并可能影响任务费用。 |
| `req.priority` | Task priority | Execution priority of the queued task; a higher priority makes the task run sooner and may cost more. | 排队任务的执行优先级；优先级越高任务越早执行，费用可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the task result once it is ready, so you do not have to poll. | 任务完成后由 DataForSEO 主动回推结果的你方接收地址，从而无需轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify that the task is complete (without the payload); you then collect results via `task_get`. | 任务完成时由 DataForSEO 回调通知（不含结果数据）的你方地址；收到通知后再用 `task_get` 领取结果。 |
| `req.postback_data` | Postback datatype; possible values: regular, advanced, html | Result format to deliver to `postback_url`; choose the result type that matches how you will consume the data. | 回推到 `postback_url` 的结果格式；选择与你消费方式相匹配的结果类型。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of task objects | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单任务的扣费金额，单位为美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_yahoo_organic_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Organic SERP Completed Tasks. Returns completed Yahoo Organic SERP tasks that have not been collected yet. | List Yahoo tasks that have finished but have not yet been collected, with the URLs to fetch each result. | 列出 Yahoo 已完成但尚未领取的任务，并给出领取各结果的 URL。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | List of completed-but-uncollected tasks. Each entry exposes the URLs to fetch its results. | 已完成但尚未领取的任务列表；每个条目给出领取结果的 URL。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | UUID of a completed task ready for collection; feed it to the matching `task_get` endpoint. | 可领取的已完成任务的 UUID；传给对应的 `task_get` 接口。 |
| `resp.200.tasks[].result[].endpoint_regular` | URL for collecting regular results | Relative API path for collecting this task's regular results. | 领取该任务 regular 结果的相对 API 路径。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative API path for collecting this task's advanced results. | 领取该任务 advanced 结果的相对 API 路径。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting HTML results | Relative API path for collecting this task's HTML results. | 领取该任务 HTML 结果的相对 API 路径。 |

## get_dataforseo_serp_yahoo_organic_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Yahoo Organic SERP Advanced Results by id. Returns advanced SERP results for a previously posted Yahoo Organic task. | Collect the advanced results of a previously posted Yahoo task by its id. | 按任务 id 领取此前提交的 Yahoo 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_yahoo_organic_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Yahoo Organic HTML Results by id. Returns HTML results for a previously posted Yahoo Organic task. | Collect the HTML results of a previously posted Yahoo task by its id. | 按任务 id 领取此前提交的 Yahoo 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_yahoo_organic_task_get_regular_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Yahoo Organic SERP Results by id (regular). Returns regular SERP results for a previously posted Yahoo Organic task. | Collect the regular results of a previously posted Yahoo task by its id. | 按任务 id 领取此前提交的 Yahoo 任务的 regular 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of regular SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## post_dataforseo_serp_yahoo_organic_live_regular

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Yahoo Organic SERP Regular. Returns regular Yahoo Organic SERP results in real time. Each Live SERP API call can contain only one task. | Return regular Yahoo organic SERP results synchronously in one call; each Live call carries exactly one task. | 在一次调用中同步返回 Yahoo 自然搜索 SERP 的 regular 结果；每个 Live 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of regular SERP results | The SERP payload generated in real time for this Live request. Its inner shape depends on the result type and search engine, so it is returned as an open array. | 本次 Live 请求实时生成的 SERP 结果数据。其内部结构取决于结果类型与搜索引擎，故以开放数组返回。 |

## post_dataforseo_serp_yahoo_organic_live_advanced

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Yahoo Organic SERP Advanced. Returns advanced Yahoo Organic SERP results in real time. Each Live SERP API call can contain only one task. | Return advanced Yahoo organic SERP results synchronously in one call; each Live call carries exactly one task. | 在一次调用中同步返回 Yahoo 自然搜索 SERP 的 advanced 结果；每个 Live 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The SERP payload generated in real time for this Live request. Its inner shape depends on the result type and search engine, so it is returned as an open array. | 本次 Live 请求实时生成的 SERP 结果数据。其内部结构取决于结果类型与搜索引擎，故以开放数组返回。 |

## post_dataforseo_serp_yahoo_organic_live_html

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Live Yahoo Organic SERP HTML. Returns raw HTML of Yahoo Organic SERP results in real time. Each Live SERP API call can contain only one task. | Return raw HTML of Yahoo organic SERP results synchronously in one call; each Live call carries exactly one task. | 在一次调用中同步返回 Yahoo 自然搜索 SERP 的原始 HTML；每个 Live 调用仅含一个任务。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | The SERP payload generated in real time for this Live request. Its inner shape depends on the result type and search engine, so it is returned as an open array. | 本次 Live 请求实时生成的 SERP 结果数据。其内部结构取决于结果类型与搜索引擎，故以开放数组返回。 |

## get_dataforseo_serp_seznam_locations

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Seznam Locations for SERP. Returns the list of supported locations for Seznam SERP. Your account is not charged for using this endpoint. | List the locations supported for Seznam SERP requests; use a returned code or name to geo-target tasks. This endpoint is free. | 列出 Seznam SERP 请求支持的地区；用返回的代码或名称对任务做地域定位。该接口免费。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of available locations | List of locations supported for this search engine's SERP. Use a returned `location_code` (or `location_name`) when posting tasks to target that locale. | 该搜索引擎 SERP 支持的地区列表。提交任务时用其中的 `location_code`（或 `location_name`）来锁定目标地区。 |
| `resp.200.tasks[].result[].location_code` | Location code | Numeric code identifying the location; pass it as the `location_code` request field to geo-target a task. | 标识地区的数字代码；作为请求字段 `location_code` 传入以对任务做地域定位。 |
| `resp.200.tasks[].result[].location_name` | Location name | Human-readable full name of the location; corresponds to the `location_name` request field. | 地区的可读全名；对应请求字段 `location_name`。 |
| `resp.200.tasks[].result[].location_code_parent` | Parent location code | Code of the enclosing (parent) location, e.g. the country a city belongs to; helps build a location hierarchy. | 上级（父）地区的代码，例如城市所属的国家，可用于构建地区层级。 |
| `resp.200.tasks[].result[].country_iso_code` | Country ISO code | ISO 3166-1 country code of the location, e.g. `US`. | 该地区所属国家的 ISO 3166-1 代码，如 `US`。 |

## get_dataforseo_serp_seznam_languages

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of Seznam Languages for SERP. Returns the list of supported languages for Seznam SERP. Your account is not charged for using this endpoint. | List the languages supported for Seznam SERP requests; use a returned code or name when posting tasks. This endpoint is free. | 列出 Seznam SERP 请求支持的语言；提交任务时使用返回的代码或名称。该接口免费。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of available languages | List of languages supported for this search engine's SERP. Use a returned `language_code` (or `language_name`) when posting tasks. | 该搜索引擎 SERP 支持的语言列表。提交任务时使用其中的 `language_code`（或 `language_name`）。 |
| `resp.200.tasks[].result[].language_name` | Language name | Human-readable full name of the language; corresponds to the `language_name` request field. | 语言的可读全名；对应请求字段 `language_name`。 |
| `resp.200.tasks[].result[].language_code` | Language code | Code identifying the language; pass it as the `language_code` request field. | 标识语言的代码；作为请求字段 `language_code` 传入。 |

## post_dataforseo_serp_seznam_organic_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Seznam Organic SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Queue an organic SERP task for Seznam; you are charged only for posting, can send up to 100 tasks per call, and collect results later by task id or via postback/pingback. | 提交 Seznam 自然搜索 SERP 任务；仅在提交时计费，每次调用最多 100 个任务，稍后按任务 id 或通过 postback/pingback 领取结果。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `req.depth` | Parsing depth | How many SERP results to parse; higher values return more results and may affect task cost. | 解析的 SERP 结果条数；值越大返回结果越多，并可能影响任务费用。 |
| `req.priority` | Task priority | Execution priority of the queued task; a higher priority makes the task run sooner and may cost more. | 排队任务的执行优先级；优先级越高任务越早执行，费用可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the task result once it is ready, so you do not have to poll. | 任务完成后由 DataForSEO 主动回推结果的你方接收地址，从而无需轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify that the task is complete (without the payload); you then collect results via `task_get`. | 任务完成时由 DataForSEO 回调通知（不含结果数据）的你方地址；收到通知后再用 `task_get` 领取结果。 |
| `req.postback_data` | Postback datatype; possible values: regular, advanced, html | Result format to deliver to `postback_url`; choose the result type that matches how you will consume the data. | 回推到 `postback_url` 的结果格式；选择与你消费方式相匹配的结果类型。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of task objects | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单任务的扣费金额，单位为美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_seznam_organic_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Organic SERP Completed Tasks. Returns completed Seznam Organic SERP tasks that have not been collected yet. | List Seznam tasks that have finished but have not yet been collected, with the URLs to fetch each result. | 列出 Seznam 已完成但尚未领取的任务，并给出领取各结果的 URL。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | List of completed-but-uncollected tasks. Each entry exposes the URLs to fetch its results. | 已完成但尚未领取的任务列表；每个条目给出领取结果的 URL。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | UUID of a completed task ready for collection; feed it to the matching `task_get` endpoint. | 可领取的已完成任务的 UUID；传给对应的 `task_get` 接口。 |
| `resp.200.tasks[].result[].endpoint_regular` | URL for collecting regular results | Relative API path for collecting this task's regular results. | 领取该任务 regular 结果的相对 API 路径。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative API path for collecting this task's advanced results. | 领取该任务 advanced 结果的相对 API 路径。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting HTML results | Relative API path for collecting this task's HTML results. | 领取该任务 HTML 结果的相对 API 路径。 |

## get_dataforseo_serp_seznam_organic_task_get_regular_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Seznam Organic SERP Results by id (regular). Returns regular SERP results for a previously posted Seznam Organic task. | Collect the regular results of a previously posted Seznam task by its id. | 按任务 id 领取此前提交的 Seznam 任务的 regular 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of regular SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_seznam_organic_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Seznam Organic SERP Advanced Results by id. Returns advanced SERP results for a previously posted Seznam Organic task. | Collect the advanced results of a previously posted Seznam task by its id. | 按任务 id 领取此前提交的 Seznam 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_seznam_organic_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Seznam Organic HTML Results by id. Returns HTML results for a previously posted Seznam Organic task. | Collect the HTML results of a previously posted Seznam task by its id. | 按任务 id 领取此前提交的 Seznam 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## post_dataforseo_serp_naver_organic_task_post

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Setting Naver Organic SERP Tasks. Your account is charged only for setting a task. You can send up to 100 tasks per POST call and retrieve completed results later by task id or via postback/pingback. | Queue an organic SERP task for Naver; you are charged only for posting, can send up to 100 tasks per call, and collect results later by task id or via postback/pingback. | 提交 Naver 自然搜索 SERP 任务；仅在提交时计费，每次调用最多 100 个任务，稍后按任务 id 或通过 postback/pingback 领取结果。 |
| `req.keyword` | Keyword to search for | Search query to run on the search engine, exactly as a user would type it. This is the only required field for keyword-based endpoints. | 要在搜索引擎上执行的查询词，按用户实际输入的样子填写；关键词类接口中这是唯一必填字段。 |
| `req.location_name` | Full name of search engine location | Full location name to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_code`. | 用于地域定位搜索的地区全名；有效取值见对应引擎的 locations 接口。与 `location_code` 二选一提供。 |
| `req.location_code` | Search engine location code | Numeric location code to geo-target the search; obtain valid values from the engine's locations endpoint. Provide either this or `location_name`. | 用于地域定位搜索的数字地区代码；有效取值见对应引擎的 locations 接口。与 `location_name` 二选一提供。 |
| `req.language_name` | Full name of search engine language | Full language name for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_code`. | 搜索使用的语言全名；有效取值见对应引擎的 languages 接口。与 `language_code` 二选一提供。 |
| `req.language_code` | Search engine language code | Language code for the search; obtain valid values from the engine's languages endpoint. Provide either this or `language_name`. | 搜索使用的语言代码；有效取值见对应引擎的 languages 接口。与 `language_name` 二选一提供。 |
| `req.device` | Device type | Device profile to emulate for the search, which can change how results are ranked and rendered. | 搜索时模拟的设备类型，会影响结果的排序与呈现方式。 |
| `req.os` | Device operating system | Operating system to emulate together with `device`. | 与 `device` 搭配模拟的操作系统。 |
| `req.depth` | Parsing depth | How many SERP results to parse; higher values return more results and may affect task cost. | 解析的 SERP 结果条数；值越大返回结果越多，并可能影响任务费用。 |
| `req.priority` | Task priority | Execution priority of the queued task; a higher priority makes the task run sooner and may cost more. | 排队任务的执行优先级；优先级越高任务越早执行，费用可能更高。 |
| `req.postback_url` | URL for sending task results | Your endpoint that DataForSEO calls with the task result once it is ready, so you do not have to poll. | 任务完成后由 DataForSEO 主动回推结果的你方接收地址，从而无需轮询。 |
| `req.pingback_url` | Notification URL of a completed task | Your endpoint that DataForSEO pings to notify that the task is complete (without the payload); you then collect results via `task_get`. | 任务完成时由 DataForSEO 回调通知（不含结果数据）的你方地址；收到通知后再用 `task_get` 领取结果。 |
| `req.postback_data` | Postback datatype; possible values: regular, advanced, html | Result format to deliver to `postback_url`; choose the result type that matches how you will consume the data. | 回推到 `postback_url` 的结果格式；选择与你消费方式相匹配的结果类型。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of task objects | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].cost` | Cost of the task, USD | Amount charged for this individual task, in USD. | 该单任务的扣费金额，单位为美元。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |

## get_dataforseo_serp_naver_organic_tasks_ready

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Organic SERP Completed Tasks. Returns completed Naver Organic SERP tasks that have not been collected yet. | List Naver tasks that have finished but have not yet been collected, with the URLs to fetch each result. | 列出 Naver 已完成但尚未领取的任务，并给出领取各结果的 URL。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of completed task references | List of completed-but-uncollected tasks. Each entry exposes the URLs to fetch its results. | 已完成但尚未领取的任务列表；每个条目给出领取结果的 URL。 |
| `resp.200.tasks[].result[].id` | Task identifier of the completed task | UUID of a completed task ready for collection; feed it to the matching `task_get` endpoint. | 可领取的已完成任务的 UUID；传给对应的 `task_get` 接口。 |
| `resp.200.tasks[].result[].endpoint_regular` | URL for collecting regular results | Relative API path for collecting this task's regular results. | 领取该任务 regular 结果的相对 API 路径。 |
| `resp.200.tasks[].result[].endpoint_advanced` | URL for collecting advanced results | Relative API path for collecting this task's advanced results. | 领取该任务 advanced 结果的相对 API 路径。 |
| `resp.200.tasks[].result[].endpoint_html` | URL for collecting HTML results | Relative API path for collecting this task's HTML results. | 领取该任务 HTML 结果的相对 API 路径。 |

## get_dataforseo_serp_naver_organic_task_get_regular_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Naver Organic SERP Results by id (regular). Returns regular SERP results for a previously posted Naver Organic task. | Collect the regular results of a previously posted Naver task by its id. | 按任务 id 领取此前提交的 Naver 任务的 regular 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of regular SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_naver_organic_task_get_advanced_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Naver Organic SERP Advanced Results by id. Returns advanced SERP results for a previously posted Naver Organic task. | Collect the advanced results of a previously posted Naver task by its id. | 按任务 id 领取此前提交的 Naver 任务的 advanced 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of advanced SERP results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## get_dataforseo_serp_naver_organic_task_get_html_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Naver Organic HTML Results by id. Returns HTML results for a previously posted Naver Organic task. | Collect the HTML results of a previously posted Naver task by its id. | 按任务 id 领取此前提交的 Naver 任务的 HTML 结果。 |
| `param:id` | Task identifier in UUID format | UUID of the task to collect, as returned in `tasks[].id` when the task was posted or listed by the matching tasks_ready endpoint. | 要领取的任务的 UUID；提交任务时由 `tasks[].id` 返回，或可从对应 tasks_ready 接口列出。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total tasks cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks_count` | The number of tasks in the tasks array | Number of entries in the `tasks` array. | `tasks` 数组中的条目数量。 |
| `resp.200.tasks_error` | The number of tasks in the tasks array returned with an error | How many of the entries in `tasks` finished with an error; if non-zero, inspect each task's own `status_code`. | `tasks` 中以错误结束的条目数量；若非 0，需逐个检查任务自身的 `status_code`。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].result` | Array of HTML results | The collected SERP payload for the requested task. Its inner shape depends on the result type (regular / advanced / html) and the search engine, so it is returned as an open array; parse according to the endpoint you called. | 所请求任务领取到的 SERP 结果数据。其内部结构取决于结果类型（regular / advanced / html）与搜索引擎，故以开放数组返回；请按调用的接口类型解析。 |

## post_dataforseo_serp_ai_summary

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | The Live SERP API AI Summary endpoint provides a summary of the content found on any SERP and generates a response based on the user prompt. Your account is charged for each request. | Generate an AI summary of the content found on a previously fetched SERP, answering an optional prompt. Charged per request. | 对此前抓取的某个 SERP 内容生成 AI 摘要，并可按可选 prompt 作答。按次计费。 |
| `req.task_id` | Unique identifier of the associated task in UUID format; can be used within 30 days | UUID of an existing SERP task whose content the summary is built from; returned as `tasks[].id` when you posted the task and valid for 30 days. | 用于生成摘要的已有 SERP 任务的 UUID；提交任务时由 `tasks[].id` 返回，有效期 30 天。 |
| `req.prompt` | Additional AI prompt; maximum 2000 characters | Extra instruction steering how the AI summarizes the SERP content. | 用于引导 AI 如何总结 SERP 内容的附加指令。 |
| `req.support_extra` | Whether to consider extra SERP features such as answer_box, knowledge_graph, and featured_snippet; default true | When enabled, the summary also takes extra SERP features (such as `answer_box`, `knowledge_graph`, and `featured_snippet`) into account. | 开启后，摘要会同时纳入额外的 SERP 特性（如 `answer_box`、`knowledge_graph`、`featured_snippet`）。 |
| `req.fetch_content` | Whether to fetch content from pages in SERPs; default false | When enabled, the page content behind the SERP results is fetched and fed into the summary for richer answers. | 开启后，会抓取 SERP 结果背后的页面内容并纳入摘要，以获得更充实的回答。 |
| `req.include_links` | Whether to include source links in the summary; default false | When enabled, the summary cites the source links it drew from. | 开启后，摘要会附带其引用的来源链接。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total task cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |
| `resp.200.tasks[].path` | URL path | API path segments that were called, echoing how the request was routed. | 本次调用的 API 路径分段，回显请求的路由方式。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the parameters supplied in the POST request, useful for correlating the response with its input. | 回显 POST 请求中提交的参数，便于将响应与其输入对应。 |
| `resp.200.tasks[].result` | Array of results | Array holding the AI summary output for the request. | 承载本次请求 AI 摘要输出的数组。 |
| `resp.200.tasks[].result[].items_count` | Number of items in the result array | Number of entries in the `items` array. | `items` 数组中的条目数量。 |
| `resp.200.tasks[].result[].items` | Items array | Array of generated summary items. | 生成的摘要条目数组。 |
| `resp.200.tasks[].result[].items[].summary` | Generated summary | The AI-generated summary text answering the prompt against the SERP content. | 针对 SERP 内容并结合 prompt 生成的 AI 摘要文本。 |

## post_dataforseo_serp_screenshot

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Using the Live Page Screenshot endpoint, you can capture a screenshot of any SERP page. The screenshot is made by visualizing the HTML of the search engine page. Your account is charged for each request. | Capture a screenshot of a previously fetched SERP page by rendering its HTML. Charged per request. | 通过渲染此前抓取的某个 SERP 页面的 HTML 来截取页面截图。按次计费。 |
| `req.task_id` | Unique identifier of the associated task in UUID format; can be used within 7 days | UUID of an existing SERP task whose page is screenshotted; returned as `tasks[].id` when you posted the task and valid for 7 days. | 用于截图的已有 SERP 任务的 UUID；提交任务时由 `tasks[].id` 返回，有效期 7 天。 |
| `req.browser_preset` | Browser resolution preset: desktop, tablet, or mobile | Predefined viewport profile (desktop, tablet, or mobile) controlling the rendered screen size. | 预设视口配置（desktop、tablet 或 mobile），决定渲染的屏幕尺寸。 |
| `req.browser_screen_width` | Browser resolution width; range 240-9999 | Custom viewport width in pixels, overriding the preset; valid range 240-9999. | 自定义视口宽度（像素），覆盖预设；有效范围 240-9999。 |
| `req.browser_screen_height` | Browser resolution height; range 240-9999 | Custom viewport height in pixels, overriding the preset; valid range 240-9999. | 自定义视口高度（像素），覆盖预设；有效范围 240-9999。 |
| `req.browser_screen_scale_factor` | Browser scale factor; range 0.5-3 | Device pixel ratio applied when rendering, controlling screenshot sharpness; valid range 0.5-3. | 渲染时应用的设备像素比，控制截图清晰度；有效范围 0.5-3。 |
| `req.page` | SERP page number to screenshot; default 1 | Which SERP page to capture (1 is the first results page). | 要截取的 SERP 页码（1 为第一页结果）。 |
| `resp.200.version` | The current version of the API | API version that produced this response, useful when reporting issues or pinning behavior across releases. | 生成该响应的 API 版本，便于上报问题或在版本迭代中锁定行为。 |
| `resp.200.status_code` | General status code | Top-level status code for the whole API call. `20000` indicates the call was accepted and processed; non-20xxx values signal a request-level failure that applies before any per-task processing. | 整次 API 调用的总状态码。`20000` 表示调用被受理并处理成功；非 20xxx 值代表在进入单任务处理之前就发生的请求级失败。 |
| `resp.200.status_message` | General informational message | Human-readable message accompanying `status_code`; read it when `status_code` is not a success value to learn the cause. | 与 `status_code` 配套的可读说明；当 `status_code` 非成功值时，读取此字段定位原因。 |
| `resp.200.time` | Execution time, seconds | Server-side execution time for the whole call, in seconds. | 整次调用的服务端执行耗时，单位为秒。 |
| `resp.200.cost` | Total task cost, USD | Total amount charged for this call across all tasks, in USD. Reads-only listing endpoints (locations/languages) return 0. | 本次调用所有任务合计扣费，单位为美元；locations/languages 等只读列表接口返回 0。 |
| `resp.200.tasks` | Array of tasks | Container for the individual task results of this call. Because the gateway sends one task per call, expect a single entry. | 本次调用各任务结果的容器；由于网关每次仅提交一个任务，通常只含一个条目。 |
| `resp.200.tasks[].id` | Task identifier in UUID format | UUID of this task. Pass it to the matching `task_get` endpoint to collect results later, and reuse it as `task_id` for the AI Summary and Screenshot endpoints. | 该任务的 UUID。稍后用它调用对应的 `task_get` 接口取回结果，也可作为 `task_id` 复用于 AI Summary 与 Screenshot 接口。 |
| `resp.200.tasks[].status_code` | Task status code | Per-task status code. `20000` means done; `20100` typically means the task was accepted and is still being processed. | 单任务状态码。`20000` 表示已完成；`20100` 通常表示任务已受理、仍在处理中。 |
| `resp.200.tasks[].status_message` | Task status message | Human-readable message for this task's status; consult it when the task code is not a success value. | 该任务状态的可读说明；当任务状态码非成功值时据此排查。 |
| `resp.200.tasks[].result_count` | Number of elements in the result array | Number of entries in this task's `result` array. | 该任务 `result` 数组中的条目数量。 |
| `resp.200.tasks[].path` | URL path | API path segments that were called, echoing how the request was routed. | 本次调用的 API 路径分段，回显请求的路由方式。 |
| `resp.200.tasks[].data` | Contains the same parameters specified in the POST request | Echo of the parameters supplied in the POST request, useful for correlating the response with its input. | 回显 POST 请求中提交的参数，便于将响应与其输入对应。 |
| `resp.200.tasks[].result` | Array of results | Array holding the screenshot output for the request. | 承载本次请求截图输出的数组。 |
| `resp.200.tasks[].result[].items_count` | Number of items in the results array | Number of entries in the `items` array. | `items` 数组中的条目数量。 |
| `resp.200.tasks[].result[].items` | Items array | Array of screenshot items. | 截图条目数组。 |
| `resp.200.tasks[].result[].items[].image` | URL of the page screenshot on DataForSEO storage | URL of the captured SERP page screenshot hosted on DataForSEO storage. | 截取的 SERP 页面截图地址，托管于 DataForSEO 存储。 |

