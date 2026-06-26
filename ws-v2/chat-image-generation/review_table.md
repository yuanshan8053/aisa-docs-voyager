# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 1 个接口，25 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## generateImageViaChat

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Generate images with the Wan 2.7 image models. Request shape matches OpenAI Chat Completions with multimodal content; the response contains `choices[].message.content[]` where each item is `{type: "image", image: "<url or base64>"}`.<br><br>**Important:** `messages[].content` must be an **array of typed parts**, not a plain string. Passing a string returns `400 invalid_parameter_error` with `Input should be a valid list: messages[*].content`.<br><br>By default `wan2.7-image` returns **4 candidate images** (billed per image). Set `n` to request a different count. | Generate images with the Wan 2.7 image models through the standard chat-completions endpoint. Send the prompt as typed parts inside the last user message, optionally with a reference image for image-to-image; generated images come back as image parts in the assistant message. | 借助标准的对话补全端点,用 Wan 2.7 系列图像模型生成图像。将提示词以带类型的片段放入最后一条用户消息中,可选附参考图以做图生图;生成结果以图像片段形式回填在助手消息里。 |
| `req.model` | Image-generation model. `wan2.7-image` ($0.030/image) for standard quality, `wan2.7-image-pro` ($0.075/image) for higher fidelity. | Which image model to run. The two variants trade off quality against price, with the pro variant offering higher fidelity at a higher per-image cost. | 本次使用的图像模型。两个变体在画质与价格之间权衡,pro 变体以更高的单图成本换取更高的保真度。 |
| `req.messages` | Conversation messages. Image prompts go in the last user message's `content` array as `{type: "text"}` parts. | The conversation sent to the model. Put the image prompt in the last user message; each message carries a role and a content array of typed parts. | 发送给模型的对话。把图像提示词放进最后一条用户消息;每条消息带有角色,以及一个由带类型片段组成的 content 数组。 |
| `req.messages.role` |  | Who authored the message, distinguishing system guidance, user input, and prior assistant output. | 该消息的作者身份,用于区分系统引导、用户输入与助手既往输出。 |
| `req.messages.content` | Multimodal parts. For image generation, include at least one `{type: "text"}` part with the prompt. | The typed parts making up one message. It must be an array of parts, not a plain string; for image generation include at least one text part holding the prompt, and add an image part for image-to-image. | 构成一条消息的带类型片段。它必须是片段数组而非纯字符串;做图像生成时至少包含一个携带提示词的文本片段,做图生图时再加入图像片段。 |
| `req.messages.content.type` |  | What kind of part this is: a text segment carrying the prompt, or an image-URL part supplying a reference image for image-to-image. | 该片段的类别:承载提示词的文本片段,或为图生图提供参考图的图像 URL 片段。 |
| `req.messages.content.text` | Used when `type: "text"`. | The prompt text, used for a text-type part. | 提示词文本,用于文本类型的片段。 |
| `req.messages.content.image_url` | Used when `type: "image_url"` (image-to-image use cases). | A reference image for image-to-image generation, supplied for an image-URL part. | 用于图生图的参考图,在图像 URL 类型片段中提供。 |
| `req.messages.content.image_url.url` |  | Location of the reference image. | 参考图的地址。 |
| `req.n` | Number of images to generate. `wan2.7-image` returns 4 by default; pass `1` to save cost. | How many candidate images to generate in one call. Each image is billed separately, so request fewer to save cost. | 单次调用生成的候选图像数量。每张图单独计费,需要省成本时请减少数量。 |
| `resp.200.id` |  | Unique identifier of this generation response. | 本次生成响应的唯一标识。 |
| `resp.200.object` |  | Object type of the payload, mirroring the chat-completions response shape. | 载荷的对象类型,沿用对话补全的响应结构。 |
| `resp.200.created` |  | When the response was produced. | 该响应的生成时间。 |
| `resp.200.model` |  | The image model that actually served the request. | 实际处理本次请求的图像模型。 |
| `resp.200.choices` | One entry per generated image. | The generated results, one entry per image. | 生成结果,每张图像对应一个条目。 |
| `resp.200.choices.index` |  | Position of this result within the choices list. | 该结果在 choices 列表中的位置。 |
| `resp.200.choices.finish_reason` |  | Why generation for this result stopped. | 该结果停止生成的原因。 |
| `resp.200.choices.message` |  | The assistant message that holds the generated image. | 承载生成图像的助手消息。 |
| `resp.200.choices.message.role` |  | Author role of the generated message, always the assistant. | 生成消息的作者角色,固定为助手。 |
| `resp.200.choices.message.content` |  | The message's parts; for this endpoint each part wraps one generated image. | 该消息的片段;在本接口中每个片段包裹一张生成图像。 |
| `resp.200.choices.message.content.type` |  | Part kind, marking the part as a generated image. | 片段类别,标记该片段为生成图像。 |
| `resp.200.choices.message.content.image` | Short-lived URL to the generated image (or base64-encoded data, depending on your account configuration). | The generated image itself, delivered either as a short-lived URL or as base64 data depending on account configuration. | 生成的图像本身,依据账号配置以短时有效的 URL 或 base64 数据形式给出。 |
| `resp.200.usage` |  | Token accounting for the request. | 本次请求的 token 计量。 |
| `resp.200.usage.prompt_tokens` |  | Tokens consumed by the input prompt. | 输入提示词消耗的 token 数。 |
| `resp.200.usage.completion_tokens` |  | Tokens attributed to the generated output. | 归于生成输出的 token 数。 |
| `resp.200.usage.total_tokens` |  | Combined input and output token count. | 输入与输出合计的 token 数。 |

