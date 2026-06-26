# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 4 个接口，148 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## post_perplexity-sonar

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Cost-effective model for quick web searches with AI-generated answers. Best for simple factual queries. Uses model `sonar`.<br><br>**Pricing:** $0.012 per request | Run a single-turn chat completion against the lightweight `sonar` model, which performs a live web search and returns an AI-written answer with source citations. Optimized for quick, low-cost factual lookups. | 对轻量的 `sonar` 模型发起一次对话补全：模型实时联网检索后，返回带来源引用的 AI 回答。适合快速、低成本的事实型查询。 |
| `req.model` | The Sonar model to use. | Selects which Sonar model handles the request, trading off speed, depth, and cost. Should match the model implied by the endpoint path. | 选择处理本次请求的 Sonar 模型，在速度、深度与成本之间权衡；通常应与所调用端点路径对应的模型一致。 |
| `req.messages` | A list of messages comprising the conversation so far. | Ordered conversation history sent to the model; the last user message is the query to answer, while earlier turns provide context. | 发送给模型的有序对话历史：最后一条 user 消息是待回答的问题，靠前的消息提供上下文。 |
| `req.messages.role` | The role of the message author. | Identifies who authored the message: `system` sets behavior, `user` is the asker, `assistant` is a prior model reply. | 标识消息的发出方：`system` 设定行为，`user` 为提问者，`assistant` 为模型先前的回复。 |
| `req.messages.content` | The content of the message. | The text body of this message turn. | 本条消息的文本内容。 |
| `req.max_tokens` | The maximum number of tokens to generate in the response. | Upper bound on tokens generated in the answer; the model stops once this limit is reached. Leave unset to use the model default. | 回答可生成的 token 数上限，达到上限即停止生成；不设置则使用模型默认值。 |
| `req.temperature` | Sampling temperature between 0 and 2. Lower values make output more focused and deterministic. | Sampling randomness: lower values yield more focused, deterministic answers; higher values increase diversity. | 采样随机度：值越低回答越聚焦、越确定，值越高则越发散多样。 |
| `req.top_p` | Nucleus sampling parameter. The model considers tokens with top_p probability mass. | Nucleus sampling: the model only samples from the smallest set of tokens whose cumulative probability reaches this threshold. Usually tune either this or temperature, not both. | 核采样：模型仅从累积概率达到该阈值的最小 token 集合中采样。通常只调本参数或 temperature 之一，不同时调。 |
| `req.top_k` | The number of tokens to keep for top-k filtering. | Restricts sampling to the K highest-probability tokens at each step; a value of 0 disables this filter. | 将采样限制在每一步概率最高的 K 个 token 内；取 0 表示关闭该过滤。 |
| `req.stream` | Whether to stream the response using server-sent events. | When enabled, the answer is pushed incrementally as server-sent events instead of returned in a single response. | 开启后，回答以 server-sent events 增量推送，而非一次性整体返回。 |
| `req.search_context` | Controls how much search context to use. Affects per-request cost. | How much web search context the model pulls in before answering; more context can improve thoroughness but raises per-request cost. | 模型回答前引入的联网检索上下文量：上下文越多通常越全面，但单次请求成本也越高。 |
| `req.frequency_penalty` | Penalizes new tokens based on their existing frequency in the text so far. Positive values decrease the likelihood of repeating the same line verbatim. | Discourages reusing tokens in proportion to how often they already appeared, reducing verbatim repetition. | 按 token 已出现的频率施加惩罚，抑制逐字重复。 |
| `req.presence_penalty` | Penalizes new tokens based on whether they appear in the text so far. Positive values increase the likelihood of talking about new topics. | Discourages tokens that have appeared at all, nudging the model toward introducing new topics. | 对已出现过的 token 施加惩罚，促使模型转向新的话题。 |
| `req.return_citations` | Whether to return citations and search results in the response. | Whether the response should include the source citations and search results backing the answer. | 响应是否包含支撑回答的来源引用与检索结果。 |
| `req.search_recency_filter` | Filter search results by recency. | Restricts web search to results published within the given recency window (e.g. past hour/day/week/month), useful for time-sensitive queries. | 将联网检索限制在指定的时间新鲜度窗口内（如近 1 小时 / 天 / 周 / 月），适合对时效性敏感的查询。 |
| `req.search_domain_filter` | Limit search to specific domains. | Whitelist of domains the web search is confined to; only sources from these domains are considered. | 联网检索的域名白名单：仅采纳来自这些域名的来源。 |
| `resp.200.id` | Unique identifier for the completion. | Unique identifier of this completion, useful for logging and tracing. | 本次补全的唯一标识，便于日志记录与问题追踪。 |
| `resp.200.model` | The model used for the completion. | The Sonar model that actually produced this completion. | 实际生成本次补全的 Sonar 模型。 |
| `resp.200.object` |  | Type tag of the returned object, marking it as a chat completion result. | 返回对象的类型标记，表明这是一条对话补全结果。 |
| `resp.200.created` | Unix timestamp of when the completion was created. | When the completion was generated, as a Unix timestamp in seconds. | 补全生成的时间，Unix 时间戳（秒）。 |
| `resp.200.choices` |  | The generated answer candidates; typically contains a single entry holding the model's reply. | 生成的回答候选项，通常仅含一条，承载模型的回复。 |
| `resp.200.choices.index` |  | Position of this candidate within the choices list. | 该候选项在 choices 列表中的序号。 |
| `resp.200.choices.message` |  | The reply message produced by the model for this candidate. | 该候选项中模型生成的回复消息。 |
| `resp.200.choices.message.role` |  | Author role of the reply, which is the assistant. | 回复消息的发出方角色，即助手。 |
| `resp.200.choices.message.content` | The AI-generated answer, with inline citation references like [1][2]. | The AI-generated answer text, containing inline citation markers such as [1][2] that map to the citations list. | AI 生成的回答正文，内含 [1][2] 等行内引用标记，与 citations 列表对应。 |
| `resp.200.choices.finish_reason` |  | Why generation stopped: `stop` for a natural end, `length` when the token limit was hit. | 生成结束的原因：`stop` 表示自然结束，`length` 表示触及 token 上限。 |
| `resp.200.citations` | List of source URLs referenced in the answer. | Source URLs cited in the answer, indexed to match the inline [n] markers in the answer text. | 回答中引用的来源 URL，其下标与正文中的行内 [n] 标记对应。 |
| `resp.200.search_results` | Detailed search results with titles, snippets, and URLs. | The web search results the answer was grounded in, each with metadata about the source. | 回答所依据的联网检索结果，每条附带来源的元信息。 |
| `resp.200.search_results.title` |  | Title of the search result page. | 检索结果页面的标题。 |
| `resp.200.search_results.url` |  | Link to the search result source. | 检索结果来源的链接。 |
| `resp.200.search_results.snippet` |  | Excerpt of the source text relevant to the query. | 与查询相关的来源文本摘录。 |
| `resp.200.search_results.date` |  | Publication date of the source.<br>[⚠️Note:源码未声明日期格式，待研发确认。] | 来源的发布日期。<br>[⚠️批注:源码未声明日期格式，待研发确认。] |
| `resp.200.search_results.source` |  | Name of the publisher or site the result came from. | 结果所属的发布方或站点名称。 |
| `resp.200.usage` |  | Token consumption and search usage accounting for this request. | 本次请求的 token 消耗与检索用量统计。 |
| `resp.200.usage.prompt_tokens` |  | Number of tokens in the input messages. | 输入消息所占的 token 数。 |
| `resp.200.usage.completion_tokens` |  | Number of tokens in the generated answer. | 生成回答所占的 token 数。 |
| `resp.200.usage.total_tokens` |  | Sum of prompt and completion tokens for the request. | 本次请求 prompt 与 completion token 之和。 |
| `resp.200.usage.search_context_size` |  | The effective amount of search context applied, reflecting the search_context setting used. | 实际生效的检索上下文量，反映本次采用的 search_context 设置。 |

## post_perplexity-sonar-pro

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Advanced search model supporting complex queries and multi-step follow-ups. Better for nuanced research questions. Uses model `sonar-pro`.<br><br>**Pricing:** $0.012 per request | Run a chat completion against the `sonar-pro` model, which handles more complex, multi-step queries and follow-up reasoning while grounding the answer in live web search and citations. | 对 `sonar-pro` 模型发起对话补全：在实时联网检索并附带引用的基础上，处理更复杂、需要多步推进与追问的查询。 |
| `req.model` | The Sonar model to use. | Selects which Sonar model handles the request, trading off speed, depth, and cost. Should match the model implied by the endpoint path. | 选择处理本次请求的 Sonar 模型，在速度、深度与成本之间权衡；通常应与所调用端点路径对应的模型一致。 |
| `req.messages` | A list of messages comprising the conversation so far. | Ordered conversation history sent to the model; the last user message is the query to answer, while earlier turns provide context. | 发送给模型的有序对话历史：最后一条 user 消息是待回答的问题，靠前的消息提供上下文。 |
| `req.messages.role` | The role of the message author. | Identifies who authored the message: `system` sets behavior, `user` is the asker, `assistant` is a prior model reply. | 标识消息的发出方：`system` 设定行为，`user` 为提问者，`assistant` 为模型先前的回复。 |
| `req.messages.content` | The content of the message. | The text body of this message turn. | 本条消息的文本内容。 |
| `req.max_tokens` | The maximum number of tokens to generate in the response. | Upper bound on tokens generated in the answer; the model stops once this limit is reached. Leave unset to use the model default. | 回答可生成的 token 数上限，达到上限即停止生成；不设置则使用模型默认值。 |
| `req.temperature` | Sampling temperature between 0 and 2. Lower values make output more focused and deterministic. | Sampling randomness: lower values yield more focused, deterministic answers; higher values increase diversity. | 采样随机度：值越低回答越聚焦、越确定，值越高则越发散多样。 |
| `req.top_p` | Nucleus sampling parameter. The model considers tokens with top_p probability mass. | Nucleus sampling: the model only samples from the smallest set of tokens whose cumulative probability reaches this threshold. Usually tune either this or temperature, not both. | 核采样：模型仅从累积概率达到该阈值的最小 token 集合中采样。通常只调本参数或 temperature 之一，不同时调。 |
| `req.top_k` | The number of tokens to keep for top-k filtering. | Restricts sampling to the K highest-probability tokens at each step; a value of 0 disables this filter. | 将采样限制在每一步概率最高的 K 个 token 内；取 0 表示关闭该过滤。 |
| `req.stream` | Whether to stream the response using server-sent events. | When enabled, the answer is pushed incrementally as server-sent events instead of returned in a single response. | 开启后，回答以 server-sent events 增量推送，而非一次性整体返回。 |
| `req.search_context` | Controls how much search context to use. Affects per-request cost. | How much web search context the model pulls in before answering; more context can improve thoroughness but raises per-request cost. | 模型回答前引入的联网检索上下文量：上下文越多通常越全面，但单次请求成本也越高。 |
| `req.frequency_penalty` | Penalizes new tokens based on their existing frequency in the text so far. Positive values decrease the likelihood of repeating the same line verbatim. | Discourages reusing tokens in proportion to how often they already appeared, reducing verbatim repetition. | 按 token 已出现的频率施加惩罚，抑制逐字重复。 |
| `req.presence_penalty` | Penalizes new tokens based on whether they appear in the text so far. Positive values increase the likelihood of talking about new topics. | Discourages tokens that have appeared at all, nudging the model toward introducing new topics. | 对已出现过的 token 施加惩罚，促使模型转向新的话题。 |
| `req.return_citations` | Whether to return citations and search results in the response. | Whether the response should include the source citations and search results backing the answer. | 响应是否包含支撑回答的来源引用与检索结果。 |
| `req.search_recency_filter` | Filter search results by recency. | Restricts web search to results published within the given recency window (e.g. past hour/day/week/month), useful for time-sensitive queries. | 将联网检索限制在指定的时间新鲜度窗口内（如近 1 小时 / 天 / 周 / 月），适合对时效性敏感的查询。 |
| `req.search_domain_filter` | Limit search to specific domains. | Whitelist of domains the web search is confined to; only sources from these domains are considered. | 联网检索的域名白名单：仅采纳来自这些域名的来源。 |
| `resp.200.id` | Unique identifier for the completion. | Unique identifier of this completion, useful for logging and tracing. | 本次补全的唯一标识，便于日志记录与问题追踪。 |
| `resp.200.model` | The model used for the completion. | The Sonar model that actually produced this completion. | 实际生成本次补全的 Sonar 模型。 |
| `resp.200.object` |  | Type tag of the returned object, marking it as a chat completion result. | 返回对象的类型标记，表明这是一条对话补全结果。 |
| `resp.200.created` | Unix timestamp of when the completion was created. | When the completion was generated, as a Unix timestamp in seconds. | 补全生成的时间，Unix 时间戳（秒）。 |
| `resp.200.choices` |  | The generated answer candidates; typically contains a single entry holding the model's reply. | 生成的回答候选项，通常仅含一条，承载模型的回复。 |
| `resp.200.choices.index` |  | Position of this candidate within the choices list. | 该候选项在 choices 列表中的序号。 |
| `resp.200.choices.message` |  | The reply message produced by the model for this candidate. | 该候选项中模型生成的回复消息。 |
| `resp.200.choices.message.role` |  | Author role of the reply, which is the assistant. | 回复消息的发出方角色，即助手。 |
| `resp.200.choices.message.content` | The AI-generated answer, with inline citation references like [1][2]. | The AI-generated answer text, containing inline citation markers such as [1][2] that map to the citations list. | AI 生成的回答正文，内含 [1][2] 等行内引用标记，与 citations 列表对应。 |
| `resp.200.choices.finish_reason` |  | Why generation stopped: `stop` for a natural end, `length` when the token limit was hit. | 生成结束的原因：`stop` 表示自然结束，`length` 表示触及 token 上限。 |
| `resp.200.citations` | List of source URLs referenced in the answer. | Source URLs cited in the answer, indexed to match the inline [n] markers in the answer text. | 回答中引用的来源 URL，其下标与正文中的行内 [n] 标记对应。 |
| `resp.200.search_results` | Detailed search results with titles, snippets, and URLs. | The web search results the answer was grounded in, each with metadata about the source. | 回答所依据的联网检索结果，每条附带来源的元信息。 |
| `resp.200.search_results.title` |  | Title of the search result page. | 检索结果页面的标题。 |
| `resp.200.search_results.url` |  | Link to the search result source. | 检索结果来源的链接。 |
| `resp.200.search_results.snippet` |  | Excerpt of the source text relevant to the query. | 与查询相关的来源文本摘录。 |
| `resp.200.search_results.date` |  | Publication date of the source.<br>[⚠️Note:源码未声明日期格式，待研发确认。] | 来源的发布日期。<br>[⚠️批注:源码未声明日期格式，待研发确认。] |
| `resp.200.search_results.source` |  | Name of the publisher or site the result came from. | 结果所属的发布方或站点名称。 |
| `resp.200.usage` |  | Token consumption and search usage accounting for this request. | 本次请求的 token 消耗与检索用量统计。 |
| `resp.200.usage.prompt_tokens` |  | Number of tokens in the input messages. | 输入消息所占的 token 数。 |
| `resp.200.usage.completion_tokens` |  | Number of tokens in the generated answer. | 生成回答所占的 token 数。 |
| `resp.200.usage.total_tokens` |  | Sum of prompt and completion tokens for the request. | 本次请求 prompt 与 completion token 之和。 |
| `resp.200.usage.search_context_size` |  | The effective amount of search context applied, reflecting the search_context setting used. | 实际生效的检索上下文量，反映本次采用的 search_context 设置。 |

## post_perplexity-sonar-reasoning-pro

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Reasoning model with Chain of Thought (CoT) for precise, step-by-step analysis backed by web search. Best for analytical and complex reasoning tasks. Uses model `sonar-reasoning-pro`.<br><br>**Pricing:** $0.012 per request | Run a chat completion against the `sonar-reasoning-pro` model, which applies chain-of-thought reasoning over live web search results for step-by-step analytical answers. | 对 `sonar-reasoning-pro` 模型发起对话补全：在实时联网检索结果之上运用思维链推理，给出逐步推导的分析型回答。 |
| `req.model` | The Sonar model to use. | Selects which Sonar model handles the request, trading off speed, depth, and cost. Should match the model implied by the endpoint path. | 选择处理本次请求的 Sonar 模型，在速度、深度与成本之间权衡；通常应与所调用端点路径对应的模型一致。 |
| `req.messages` | A list of messages comprising the conversation so far. | Ordered conversation history sent to the model; the last user message is the query to answer, while earlier turns provide context. | 发送给模型的有序对话历史：最后一条 user 消息是待回答的问题，靠前的消息提供上下文。 |
| `req.messages.role` | The role of the message author. | Identifies who authored the message: `system` sets behavior, `user` is the asker, `assistant` is a prior model reply. | 标识消息的发出方：`system` 设定行为，`user` 为提问者，`assistant` 为模型先前的回复。 |
| `req.messages.content` | The content of the message. | The text body of this message turn. | 本条消息的文本内容。 |
| `req.max_tokens` | The maximum number of tokens to generate in the response. | Upper bound on tokens generated in the answer; the model stops once this limit is reached. Leave unset to use the model default. | 回答可生成的 token 数上限，达到上限即停止生成；不设置则使用模型默认值。 |
| `req.temperature` | Sampling temperature between 0 and 2. Lower values make output more focused and deterministic. | Sampling randomness: lower values yield more focused, deterministic answers; higher values increase diversity. | 采样随机度：值越低回答越聚焦、越确定，值越高则越发散多样。 |
| `req.top_p` | Nucleus sampling parameter. The model considers tokens with top_p probability mass. | Nucleus sampling: the model only samples from the smallest set of tokens whose cumulative probability reaches this threshold. Usually tune either this or temperature, not both. | 核采样：模型仅从累积概率达到该阈值的最小 token 集合中采样。通常只调本参数或 temperature 之一，不同时调。 |
| `req.top_k` | The number of tokens to keep for top-k filtering. | Restricts sampling to the K highest-probability tokens at each step; a value of 0 disables this filter. | 将采样限制在每一步概率最高的 K 个 token 内；取 0 表示关闭该过滤。 |
| `req.stream` | Whether to stream the response using server-sent events. | When enabled, the answer is pushed incrementally as server-sent events instead of returned in a single response. | 开启后，回答以 server-sent events 增量推送，而非一次性整体返回。 |
| `req.search_context` | Controls how much search context to use. Affects per-request cost. | How much web search context the model pulls in before answering; more context can improve thoroughness but raises per-request cost. | 模型回答前引入的联网检索上下文量：上下文越多通常越全面，但单次请求成本也越高。 |
| `req.frequency_penalty` | Penalizes new tokens based on their existing frequency in the text so far. Positive values decrease the likelihood of repeating the same line verbatim. | Discourages reusing tokens in proportion to how often they already appeared, reducing verbatim repetition. | 按 token 已出现的频率施加惩罚，抑制逐字重复。 |
| `req.presence_penalty` | Penalizes new tokens based on whether they appear in the text so far. Positive values increase the likelihood of talking about new topics. | Discourages tokens that have appeared at all, nudging the model toward introducing new topics. | 对已出现过的 token 施加惩罚，促使模型转向新的话题。 |
| `req.return_citations` | Whether to return citations and search results in the response. | Whether the response should include the source citations and search results backing the answer. | 响应是否包含支撑回答的来源引用与检索结果。 |
| `req.search_recency_filter` | Filter search results by recency. | Restricts web search to results published within the given recency window (e.g. past hour/day/week/month), useful for time-sensitive queries. | 将联网检索限制在指定的时间新鲜度窗口内（如近 1 小时 / 天 / 周 / 月），适合对时效性敏感的查询。 |
| `req.search_domain_filter` | Limit search to specific domains. | Whitelist of domains the web search is confined to; only sources from these domains are considered. | 联网检索的域名白名单：仅采纳来自这些域名的来源。 |
| `resp.200.id` | Unique identifier for the completion. | Unique identifier of this completion, useful for logging and tracing. | 本次补全的唯一标识，便于日志记录与问题追踪。 |
| `resp.200.model` | The model used for the completion. | The Sonar model that actually produced this completion. | 实际生成本次补全的 Sonar 模型。 |
| `resp.200.object` |  | Type tag of the returned object, marking it as a chat completion result. | 返回对象的类型标记，表明这是一条对话补全结果。 |
| `resp.200.created` | Unix timestamp of when the completion was created. | When the completion was generated, as a Unix timestamp in seconds. | 补全生成的时间，Unix 时间戳（秒）。 |
| `resp.200.choices` |  | The generated answer candidates; typically contains a single entry holding the model's reply. | 生成的回答候选项，通常仅含一条，承载模型的回复。 |
| `resp.200.choices.index` |  | Position of this candidate within the choices list. | 该候选项在 choices 列表中的序号。 |
| `resp.200.choices.message` |  | The reply message produced by the model for this candidate. | 该候选项中模型生成的回复消息。 |
| `resp.200.choices.message.role` |  | Author role of the reply, which is the assistant. | 回复消息的发出方角色，即助手。 |
| `resp.200.choices.message.content` | The AI-generated answer, with inline citation references like [1][2]. | The AI-generated answer text, containing inline citation markers such as [1][2] that map to the citations list. | AI 生成的回答正文，内含 [1][2] 等行内引用标记，与 citations 列表对应。 |
| `resp.200.choices.finish_reason` |  | Why generation stopped: `stop` for a natural end, `length` when the token limit was hit. | 生成结束的原因：`stop` 表示自然结束，`length` 表示触及 token 上限。 |
| `resp.200.citations` | List of source URLs referenced in the answer. | Source URLs cited in the answer, indexed to match the inline [n] markers in the answer text. | 回答中引用的来源 URL，其下标与正文中的行内 [n] 标记对应。 |
| `resp.200.search_results` | Detailed search results with titles, snippets, and URLs. | The web search results the answer was grounded in, each with metadata about the source. | 回答所依据的联网检索结果，每条附带来源的元信息。 |
| `resp.200.search_results.title` |  | Title of the search result page. | 检索结果页面的标题。 |
| `resp.200.search_results.url` |  | Link to the search result source. | 检索结果来源的链接。 |
| `resp.200.search_results.snippet` |  | Excerpt of the source text relevant to the query. | 与查询相关的来源文本摘录。 |
| `resp.200.search_results.date` |  | Publication date of the source.<br>[⚠️Note:源码未声明日期格式，待研发确认。] | 来源的发布日期。<br>[⚠️批注:源码未声明日期格式，待研发确认。] |
| `resp.200.search_results.source` |  | Name of the publisher or site the result came from. | 结果所属的发布方或站点名称。 |
| `resp.200.usage` |  | Token consumption and search usage accounting for this request. | 本次请求的 token 消耗与检索用量统计。 |
| `resp.200.usage.prompt_tokens` |  | Number of tokens in the input messages. | 输入消息所占的 token 数。 |
| `resp.200.usage.completion_tokens` |  | Number of tokens in the generated answer. | 生成回答所占的 token 数。 |
| `resp.200.usage.total_tokens` |  | Sum of prompt and completion tokens for the request. | 本次请求 prompt 与 completion token 之和。 |
| `resp.200.usage.search_context_size` |  | The effective amount of search context applied, reflecting the search_context setting used. | 实际生效的检索上下文量，反映本次采用的 search_context 设置。 |

## post_perplexity-sonar-deep-research

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Expert-level research model that conducts exhaustive multi-step web searches and generates comprehensive reports. Best for deep-dive research tasks. Uses model `sonar-deep-research`.<br><br>**Pricing:** $0.012 per request<br><br>> **Note:** Deep research requests may take significantly longer to complete due to the exhaustive search process. | Run a chat completion against the `sonar-deep-research` model, which performs exhaustive multi-step web research and produces a comprehensive report. Requests can take noticeably longer than other Sonar models. | 对 `sonar-deep-research` 模型发起对话补全：执行穷尽式的多步联网研究并生成综合报告。相比其他 Sonar 模型，此类请求耗时明显更长。 |
| `req.model` | The Sonar model to use. | Selects which Sonar model handles the request, trading off speed, depth, and cost. Should match the model implied by the endpoint path. | 选择处理本次请求的 Sonar 模型，在速度、深度与成本之间权衡；通常应与所调用端点路径对应的模型一致。 |
| `req.messages` | A list of messages comprising the conversation so far. | Ordered conversation history sent to the model; the last user message is the query to answer, while earlier turns provide context. | 发送给模型的有序对话历史：最后一条 user 消息是待回答的问题，靠前的消息提供上下文。 |
| `req.messages.role` | The role of the message author. | Identifies who authored the message: `system` sets behavior, `user` is the asker, `assistant` is a prior model reply. | 标识消息的发出方：`system` 设定行为，`user` 为提问者，`assistant` 为模型先前的回复。 |
| `req.messages.content` | The content of the message. | The text body of this message turn. | 本条消息的文本内容。 |
| `req.max_tokens` | The maximum number of tokens to generate in the response. | Upper bound on tokens generated in the answer; the model stops once this limit is reached. Leave unset to use the model default. | 回答可生成的 token 数上限，达到上限即停止生成；不设置则使用模型默认值。 |
| `req.temperature` | Sampling temperature between 0 and 2. Lower values make output more focused and deterministic. | Sampling randomness: lower values yield more focused, deterministic answers; higher values increase diversity. | 采样随机度：值越低回答越聚焦、越确定，值越高则越发散多样。 |
| `req.top_p` | Nucleus sampling parameter. The model considers tokens with top_p probability mass. | Nucleus sampling: the model only samples from the smallest set of tokens whose cumulative probability reaches this threshold. Usually tune either this or temperature, not both. | 核采样：模型仅从累积概率达到该阈值的最小 token 集合中采样。通常只调本参数或 temperature 之一，不同时调。 |
| `req.top_k` | The number of tokens to keep for top-k filtering. | Restricts sampling to the K highest-probability tokens at each step; a value of 0 disables this filter. | 将采样限制在每一步概率最高的 K 个 token 内；取 0 表示关闭该过滤。 |
| `req.stream` | Whether to stream the response using server-sent events. | When enabled, the answer is pushed incrementally as server-sent events instead of returned in a single response. | 开启后，回答以 server-sent events 增量推送，而非一次性整体返回。 |
| `req.search_context` | Controls how much search context to use. Affects per-request cost. | How much web search context the model pulls in before answering; more context can improve thoroughness but raises per-request cost. | 模型回答前引入的联网检索上下文量：上下文越多通常越全面，但单次请求成本也越高。 |
| `req.frequency_penalty` | Penalizes new tokens based on their existing frequency in the text so far. Positive values decrease the likelihood of repeating the same line verbatim. | Discourages reusing tokens in proportion to how often they already appeared, reducing verbatim repetition. | 按 token 已出现的频率施加惩罚，抑制逐字重复。 |
| `req.presence_penalty` | Penalizes new tokens based on whether they appear in the text so far. Positive values increase the likelihood of talking about new topics. | Discourages tokens that have appeared at all, nudging the model toward introducing new topics. | 对已出现过的 token 施加惩罚，促使模型转向新的话题。 |
| `req.return_citations` | Whether to return citations and search results in the response. | Whether the response should include the source citations and search results backing the answer. | 响应是否包含支撑回答的来源引用与检索结果。 |
| `req.search_recency_filter` | Filter search results by recency. | Restricts web search to results published within the given recency window (e.g. past hour/day/week/month), useful for time-sensitive queries. | 将联网检索限制在指定的时间新鲜度窗口内（如近 1 小时 / 天 / 周 / 月），适合对时效性敏感的查询。 |
| `req.search_domain_filter` | Limit search to specific domains. | Whitelist of domains the web search is confined to; only sources from these domains are considered. | 联网检索的域名白名单：仅采纳来自这些域名的来源。 |
| `resp.200.id` | Unique identifier for the completion. | Unique identifier of this completion, useful for logging and tracing. | 本次补全的唯一标识，便于日志记录与问题追踪。 |
| `resp.200.model` | The model used for the completion. | The Sonar model that actually produced this completion. | 实际生成本次补全的 Sonar 模型。 |
| `resp.200.object` |  | Type tag of the returned object, marking it as a chat completion result. | 返回对象的类型标记，表明这是一条对话补全结果。 |
| `resp.200.created` | Unix timestamp of when the completion was created. | When the completion was generated, as a Unix timestamp in seconds. | 补全生成的时间，Unix 时间戳（秒）。 |
| `resp.200.choices` |  | The generated answer candidates; typically contains a single entry holding the model's reply. | 生成的回答候选项，通常仅含一条，承载模型的回复。 |
| `resp.200.choices.index` |  | Position of this candidate within the choices list. | 该候选项在 choices 列表中的序号。 |
| `resp.200.choices.message` |  | The reply message produced by the model for this candidate. | 该候选项中模型生成的回复消息。 |
| `resp.200.choices.message.role` |  | Author role of the reply, which is the assistant. | 回复消息的发出方角色，即助手。 |
| `resp.200.choices.message.content` | The AI-generated answer, with inline citation references like [1][2]. | The AI-generated answer text, containing inline citation markers such as [1][2] that map to the citations list. | AI 生成的回答正文，内含 [1][2] 等行内引用标记，与 citations 列表对应。 |
| `resp.200.choices.finish_reason` |  | Why generation stopped: `stop` for a natural end, `length` when the token limit was hit. | 生成结束的原因：`stop` 表示自然结束，`length` 表示触及 token 上限。 |
| `resp.200.citations` | List of source URLs referenced in the answer. | Source URLs cited in the answer, indexed to match the inline [n] markers in the answer text. | 回答中引用的来源 URL，其下标与正文中的行内 [n] 标记对应。 |
| `resp.200.search_results` | Detailed search results with titles, snippets, and URLs. | The web search results the answer was grounded in, each with metadata about the source. | 回答所依据的联网检索结果，每条附带来源的元信息。 |
| `resp.200.search_results.title` |  | Title of the search result page. | 检索结果页面的标题。 |
| `resp.200.search_results.url` |  | Link to the search result source. | 检索结果来源的链接。 |
| `resp.200.search_results.snippet` |  | Excerpt of the source text relevant to the query. | 与查询相关的来源文本摘录。 |
| `resp.200.search_results.date` |  | Publication date of the source.<br>[⚠️Note:源码未声明日期格式，待研发确认。] | 来源的发布日期。<br>[⚠️批注:源码未声明日期格式，待研发确认。] |
| `resp.200.search_results.source` |  | Name of the publisher or site the result came from. | 结果所属的发布方或站点名称。 |
| `resp.200.usage` |  | Token consumption and search usage accounting for this request. | 本次请求的 token 消耗与检索用量统计。 |
| `resp.200.usage.prompt_tokens` |  | Number of tokens in the input messages. | 输入消息所占的 token 数。 |
| `resp.200.usage.completion_tokens` |  | Number of tokens in the generated answer. | 生成回答所占的 token 数。 |
| `resp.200.usage.total_tokens` |  | Sum of prompt and completion tokens for the request. | 本次请求 prompt 与 completion token 之和。 |
| `resp.200.usage.search_context_size` |  | The effective amount of search context applied, reflecting the search_context setting used. | 实际生效的检索上下文量，反映本次采用的 search_context 设置。 |

