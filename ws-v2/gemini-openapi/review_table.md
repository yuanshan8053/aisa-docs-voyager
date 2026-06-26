# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 1 个接口，22 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## generateContent

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Generate content using the specified Gemini model | Invoke a Gemini model to generate content from a multi-turn conversation. Drive the output with tools, safety settings, a system instruction, and generation parameters, and optionally reuse previously cached context. | 调用指定 Gemini 模型,基于多轮对话生成内容。可通过工具、安全设置、系统指令与生成参数控制输出,并可选择复用此前缓存的上下文。 |
| `param:model` | The name of the model to use, format: models/{model} | Which Gemini model to run, given in the path as `models/{model}`. | 本次调用使用的 Gemini 模型,在路径中以 `models/{model}` 形式给出。 |
| `req.contents` | Content of the conversation, required | The ordered conversation turns sent to the model; each turn carries its content parts and the role that produced them. This is the primary input the model responds to. | 发送给模型的有序对话轮次,每一轮携带其内容片段以及产生它的角色。这是模型据以应答的主要输入。 |
| `req.contents.parts` |  | The pieces that make up one conversation turn. A part is either a text segment or inline binary data (such as an image), letting a single turn mix modalities. | 构成一个对话轮次的若干片段。每个片段要么是一段文本,要么是内联的二进制数据(如图像),从而让单轮内容可以混合多种模态。 |
| `req.contents.parts.text` |  | The text payload of a part, used when the part carries written content. | 片段的文本内容,当该片段承载文字时使用。 |
| `req.contents.role` |  | Who authored this turn, distinguishing system guidance, end-user input, and prior model output so the model reads the dialogue in the right voice. | 该轮内容的作者身份,用于区分系统引导、终端用户输入与模型既往输出,使模型以正确的视角解读对话。 |
| `req.tools` | Optional tools the model can use | Tools the model is allowed to call during generation, enabling capabilities such as function calling. | 允许模型在生成过程中调用的工具,用于开启函数调用等能力。 |
| `req.toolConfig` | Optional tool configuration | Configuration that governs how the model selects and invokes the provided tools. | 约束模型如何选择并调用上述工具的配置。 |
| `req.safetySettings` |  | Per-request safety controls that adjust how generated content is filtered against harm categories. | 本次请求的安全控制项,用于调整生成内容针对各类风险类别的过滤策略。 |
| `req.systemInstruction` |  | A top-level instruction that sets the model's persona, rules, or task framing, applied across the whole conversation. | 顶层系统指令,用于设定模型的人设、规则或任务框架,对整段对话统一生效。 |
| `req.systemInstruction.parts` |  | The pieces that make up one conversation turn. A part is either a text segment or inline binary data (such as an image), letting a single turn mix modalities. | 构成一个对话轮次的若干片段。每个片段要么是一段文本,要么是内联的二进制数据(如图像),从而让单轮内容可以混合多种模态。 |
| `req.systemInstruction.parts.text` |  | The text payload of a part, used when the part carries written content. | 片段的文本内容,当该片段承载文字时使用。 |
| `req.systemInstruction.role` |  | Who authored this turn, distinguishing system guidance, end-user input, and prior model output so the model reads the dialogue in the right voice. | 该轮内容的作者身份,用于区分系统引导、终端用户输入与模型既往输出,使模型以正确的视角解读对话。 |
| `req.generationConfig` |  | Parameters that shape the generation itself, such as sampling and output-length controls. | 塑造本次生成过程的参数,例如采样与输出长度等控制项。 |
| `req.cachedContent` | Optional cached content ID | Reference to previously cached context to reuse, avoiding resending large shared content on each call.<br>[⚠️Note:源码未声明该缓存 ID 的获取接口与生效条件,待研发确认。] | 指向此前已缓存上下文的引用,可复用以避免每次调用都重传大体量的共享内容。<br>[⚠️批注:源码未声明该缓存 ID 的获取接口与生效条件,待研发确认。] |
| `resp.200.candidates` |  | The content the model generated; each candidate is one self-contained response made up of content parts and its role. | 模型生成的内容;每个候选是一份自包含的应答,由内容片段及其角色组成。 |
| `resp.200.candidates.parts` |  | The pieces that make up one conversation turn. A part is either a text segment or inline binary data (such as an image), letting a single turn mix modalities. | 构成一个对话轮次的若干片段。每个片段要么是一段文本,要么是内联的二进制数据(如图像),从而让单轮内容可以混合多种模态。 |
| `resp.200.candidates.parts.text` |  | The text payload of a part, used when the part carries written content. | 片段的文本内容,当该片段承载文字时使用。 |
| `resp.200.candidates.role` |  | Who authored this turn, distinguishing system guidance, end-user input, and prior model output so the model reads the dialogue in the right voice. | 该轮内容的作者身份,用于区分系统引导、终端用户输入与模型既往输出,使模型以正确的视角解读对话。 |
| `resp.default.error` |  | The error payload returned when generation fails, carrying a code, a human-readable message, and a symbolic status. | 生成失败时返回的错误载荷,携带错误码、可读消息与符号化状态。 |
| `resp.default.error.code` |  | Numeric error code identifying the failure category. | 标识失败类别的数字错误码。 |
| `resp.default.error.message` |  | Human-readable explanation of what went wrong. | 对出错原因的可读说明。 |
| `resp.default.error.status` |  | Symbolic status string for the error, suitable for programmatic branching. | 错误的符号化状态字符串,便于程序按状态分支处理。 |

