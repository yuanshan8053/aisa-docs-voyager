# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 1 个接口，13 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## createImageGeneration

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Generate images with the OpenAI-compatible images-generations endpoint. Currently routed to **ByteDance Seedream** — the Wan 2.7 family does not use this path.<br><br>**Size constraint.** Seedream's upstream requires a minimum of **3,686,400 pixels** per image. Requests below that return `400 InvalidParameter: image size must be at least 3686400 pixels`. A 1024×1024 image (1,048,576 px) is rejected; 1920×1920 (3,686,400 px) and 2048×2048 (4,194,304 px) are accepted. Other aspect ratios are fine as long as `width × height ≥ 3,686,400`. | Generate images from a text prompt via the OpenAI-compatible images endpoint. On AIsa this path routes to the ByteDance Seedream family only; Wan 2.7 image models go through `/v1/chat/completions` and Gemini image previews through `/v1/models/{model}:generateContent`. Mind the upstream minimum-pixel requirement on the requested size, or the request is rejected. | 通过 OpenAI 兼容的图像接口,从文本提示词生成图像。在 AIsa 上,该路径仅路由到 ByteDance Seedream 系列;Wan 2.7 图像模型走 `/v1/chat/completions`,Gemini 图像预览走 `/v1/models/{model}:generateContent`。注意上游对请求尺寸有最小像素要求,否则请求会被拒绝。 |
| `req.model` | Image generation model. Currently only `seedream-4-5-251128` is routed through this endpoint. Wan 2.7 models use `/v1/chat/completions`. | Which image model to run. On this endpoint it pins the call to the Seedream family; Wan 2.7 models must instead be called through `/v1/chat/completions`. | 本次调用使用的图像模型。在本接口上它将调用锁定到 Seedream 系列;Wan 2.7 模型须改走 `/v1/chat/completions`。 |
| `req.prompt` | Text description of the image to generate. | Natural-language description of the image you want. It is the main driver of the result — be specific about subject, style, and lighting for better output. | 你想要的图像的自然语言描述。它是结果的主要驱动信号 —— 对主体、风格、光照描述得越具体,产出越好。 |
| `req.n` | Number of images to generate. Each image is billed separately at the per-image rate. | How many images to generate in one call. Each generated image is billed separately at the per-image rate, so a higher count multiplies cost. | 单次调用生成的图像数量。每张图按单图费率分别计费,数量越多成本成倍增加。 |
| `req.size` | Image dimensions as `WIDTHxHEIGHT`. Must satisfy `width × height ≥ 3,686,400`. Common valid values: `1920x1920`, `2048x2048`, `2304x1600`, `2560x1920`. | Output dimensions in `WIDTHxHEIGHT` form. Seedream's upstream enforces a minimum of 3,686,400 pixels (`width × height`), so e.g. `1024x1024` is rejected while `1920x1920` and larger pass; any aspect ratio is fine as long as the pixel total clears the floor. | 输出尺寸,形如 `WIDTHxHEIGHT`。Seedream 上游要求像素总数(`宽 × 高`)不低于 3,686,400,因此 `1024x1024` 会被拒,`1920x1920` 及更大可通过;只要像素总数过线,任意宽高比都可以。 |
| `resp.200.model` |  | The model that actually produced these images, echoing the requested model. | 实际生成这些图像的模型,回显请求中指定的模型。 |
| `resp.200.created` |  | When the images were generated, as a Unix timestamp in seconds. | 图像生成的时间,Unix 时间戳(秒)。 |
| `resp.200.data` | One entry per generated image. | The generated images, one entry per image — its count matches the requested `n`. | 生成的图像,每张一个条目 —— 数量与请求的 `n` 一致。 |
| `resp.200.data.url` | Short-lived URL to the generated image. Download and persist it; the URL expires. | Short-lived URL to a generated image. It expires, so download and persist the image promptly rather than relying on the link long-term. | 指向某张生成图的临时 URL。该链接会过期,应尽快下载并持久化图像,不要长期依赖此链接。 |
| `resp.200.data.size` | Actual dimensions of the returned image. | The actual dimensions of the returned image, which may differ from the requested size after upstream adjustment. | 返回图像的实际尺寸,经上游调整后可能与请求尺寸不同。 |
| `resp.200.usage` |  | Resource-usage breakdown for this call, used for billing and quota tracking. | 本次调用的资源用量明细,用于计费与配额核算。 |
| `resp.200.usage.generated_images` |  | Number of images actually generated and billed in this call. | 本次实际生成并计费的图像数量。 |
| `resp.200.usage.output_tokens` |  | Tokens attributed to producing the output for this call, used in cost calculation. | 本次产出所计的输出 token 数,参与成本计算。 |
| `resp.200.usage.total_tokens` |  | Total tokens charged for this call. | 本次调用计费的总 token 数。 |

