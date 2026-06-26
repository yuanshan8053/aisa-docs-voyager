# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 1 个接口，39 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## createMessage

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Send a structured conversation to a Claude model and receive a response. Compatible with the Anthropic Messages API. | Send a structured, multi-turn conversation to a Claude model and get its response. Compatible with the Anthropic Messages API; supports tool use, extended thinking, streaming, and fine-grained sampling controls. | 向 Claude 模型发送结构化的多轮对话并获取应答。兼容 Anthropic Messages API,支持工具调用、扩展思考、流式输出与细粒度采样控制。 |
| `req.model` | Claude model identifier. Examples: claude-opus-4-7, claude-sonnet-4-6, claude-haiku-4-5-20251001. | Which Claude model to run. | 本次调用使用的 Claude 模型。 |
| `req.max_tokens` | Maximum number of tokens to generate before stopping. | Upper bound on how many tokens the model may generate before it is forced to stop. The model can stop earlier on its own. | 模型在被强制停止前最多可生成的 token 数。模型也可能提前自行停止。 |
| `req.messages` | Conversation turns. | The ordered conversation turns. Alternate user and assistant turns to supply prior context; the model continues from the last turn. | 有序的对话轮次。以用户与助手轮次交替提供既往上下文,模型从最后一轮接续生成。 |
| `req.messages.role` |  | Who authored the turn, distinguishing user input from prior assistant output. | 该轮的作者身份,用于区分用户输入与助手既往输出。 |
| `req.messages.content` | String or array of content blocks. | The turn's content, given either as plain text or as an array of structured content blocks (for example text plus images or tool results). | 该轮的内容,可以是纯文本,也可以是一组结构化内容块(例如文本搭配图像或工具结果)。 |
| `req.system` | System prompt. String or array of text blocks. | A top-level system prompt that frames the model's behavior across the whole conversation, given as text or as an array of text blocks. | 顶层系统提示,用于框定模型在整段对话中的行为,可为文本或一组文本块。 |
| `req.temperature` | Randomness. 0 = deterministic, 1 = creative. | Controls output randomness; lower values make replies more focused and deterministic, higher values make them more varied. Tune either this or `top_p`, not both. | 控制输出的随机性;取值越低应答越聚焦、越确定,越高则越多样。请在本参数与 `top_p` 之间二选一调节,不要同时调。 |
| `req.top_p` | Nucleus sampling. Use instead of temperature. | Nucleus sampling: the model samples only from the most probable tokens whose cumulative probability reaches this threshold. Use as an alternative to `temperature`. | 核采样:模型仅从累计概率达到该阈值的最高概率 token 中采样。作为 `temperature` 的替代方案使用。 |
| `req.top_k` | Only sample from the top K options for each token. | Limits sampling to the K most likely tokens at each step, removing long-tail low-probability options. | 将每一步的采样限制在概率最高的 K 个 token 内,剔除长尾低概率选项。 |
| `req.stop_sequences` | Custom sequences that stop generation. | Custom text sequences that, once produced, immediately halt generation. | 自定义文本序列,一旦被生成即立刻停止本次生成。 |
| `req.stream` | Enable SSE streaming. | Whether to stream the response incrementally over server-sent events instead of returning it all at once. | 是否以服务器发送事件(SSE)增量流式返回应答,而非一次性返回全部内容。 |
| `req.tools` | Tools the model may use. | The set of tools the model is allowed to call during the turn. | 本轮允许模型调用的工具集合。 |
| `req.tools.name` |  | The tool's name, by which the model refers to it when calling. | 工具名称,模型调用时以此引用该工具。 |
| `req.tools.description` |  | Explanation of what the tool does, which the model reads to decide when and how to call it. | 对工具用途的说明,模型据此判断何时、如何调用。 |
| `req.tools.input_schema` |  | JSON Schema describing the arguments the tool accepts, used to validate and shape the model's tool calls. | 描述工具入参的 JSON Schema,用于校验并规范模型的工具调用。 |
| `req.tools.type` |  | The kind of tool, distinguishing a custom-defined tool from other supported tool types. | 工具类别,用于区分自定义工具与其他受支持的工具类型。 |
| `req.tool_choice` | How the model uses tools. | Governs whether and how the model is allowed to invoke the supplied tools on this turn. | 约束本轮模型是否以及如何调用所提供的工具。 |
| `req.tool_choice.type` |  | The tool-use strategy: let the model decide, require it to use some tool, force a specific named tool, or forbid tool use entirely. | 工具使用策略:让模型自行决定、要求其必须使用某个工具、强制使用某个指定工具,或完全禁止使用工具。 |
| `req.tool_choice.name` | Required when type is tool. | The specific tool to force, used when the strategy targets a single named tool. | 要强制使用的具体工具,在策略指向单个指定工具时使用。 |
| `req.tool_choice.disable_parallel_tool_use` |  | When set, restricts the model to one tool call at a time instead of issuing several in parallel. | 开启后,限制模型每次只发起一个工具调用,而非并行发起多个。 |
| `req.thinking` | Enable extended thinking for complex reasoning. | Enables extended thinking, giving the model room to reason internally before answering complex problems. | 启用扩展思考,让模型在应答复杂问题前进行更充分的内部推理。 |
| `req.thinking.type` |  | Switch that turns extended thinking on. | 用于开启扩展思考的开关。 |
| `req.thinking.budget_tokens` |  | Token allowance set aside for the model's internal reasoning. | 为模型内部推理预留的 token 额度。 |
| `req.thinking.display` |  | How the thinking trace is surfaced in the response: returned as a summary, or omitted from the output. | 思考过程在响应中的呈现方式:以摘要形式返回,或从输出中略去。 |
| `req.metadata` |  | Optional request metadata used for tracking and analytics. | 可选的请求元数据,用于追踪与分析。 |
| `req.metadata.user_id` | External user ID (no PII). | An opaque identifier for the end user driving the request; must not contain personally identifiable information. | 标识发起请求的终端用户的不透明 ID,不得包含个人可识别信息。 |
| `req.service_tier` |  | Selects the service tier for the request, trading off automatic capacity selection against pinning to standard capacity only. | 为请求选择服务层级,在自动选择容量与仅锁定标准容量之间权衡。 |
| `resp.200.id` |  | Unique identifier of the generated message. | 生成消息的唯一标识。 |
| `resp.200.type` |  | Object type of the payload. | 载荷的对象类型。 |
| `resp.200.role` |  | Author role of the response, the assistant. | 应答的作者角色,即助手。 |
| `resp.200.content` | Response content blocks (text, tool_use, thinking, etc.). | The response body as a sequence of content blocks, which may include text, tool-use requests, or thinking output. | 以一系列内容块组成的应答正文,可能包含文本、工具调用请求或思考输出。 |
| `resp.200.model` |  | The model that produced the response. | 产生该应答的模型。 |
| `resp.200.stop_reason` |  | Why generation ended: a natural end of turn, hitting a stop sequence, reaching the token cap, or pausing to call a tool. | 生成结束的原因:自然结束本轮、命中停止序列、达到 token 上限,或为调用工具而暂停。 |
| `resp.200.stop_sequence` |  | The specific stop sequence that triggered the stop, when generation ended for that reason. | 当因停止序列而结束时,触发停止的那个具体序列。 |
| `resp.200.usage` |  | Token accounting for the request, including prompt-cache reads and writes. | 本次请求的 token 计量,含提示缓存的读取与写入。 |
| `resp.200.usage.input_tokens` |  | Tokens consumed by the input. | 输入消耗的 token 数。 |
| `resp.200.usage.output_tokens` |  | Tokens produced in the output. | 输出生成的 token 数。 |
| `resp.200.usage.cache_creation_input_tokens` |  | Input tokens used to write new entries into the prompt cache. | 用于向提示缓存写入新条目的输入 token 数。 |
| `resp.200.usage.cache_read_input_tokens` |  | Input tokens served from the prompt cache rather than recomputed. | 从提示缓存命中读取、而非重新计算的输入 token 数。 |

