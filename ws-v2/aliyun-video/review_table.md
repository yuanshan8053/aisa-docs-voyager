# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 2 个接口，38 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## createVideoSynthesisTask

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Submit an asynchronous video generation task. Returns a `task_id` you then poll via `GET /apis/v1/services/aigc/tasks/{task_id}`.<br><br>**Models.** Four Wan variants are accepted on this single endpoint:<br><br>\| Model \| Kind \| Image input field \|<br>\| --- \| --- \| --- \|<br>\| `wan2.6-t2v` \| text-to-video \| _n/a_ \|<br>\| `wan2.6-i2v` \| image-to-video \| `input.img_url` \|<br>\| `wan2.7-t2v` \| text-to-video \| _n/a_ \|<br>\| `wan2.7-i2v` \| image-to-video \| `input.media` ⚠️ *not* `input.img_url` \|<br><br>**Header.** `X-DashScope-Async: enable` is required.<br><br>**Body.** `model` and `input.prompt` are always required. For i2v, provide a reference image using the field indicated in the table above — `wan2.6-i2v` uses `input.img_url` (string URL), while `wan2.7-i2v` uses `input.media` (array of URLs).<br><br>Failed tasks (e.g., invalid prompt, missing required field) are **not billed** — the task-status response returns `task_status: "FAILED"` with a `code` and `message`. | Submit an asynchronous text-to-video or image-to-video generation job on one of the Wan models and get back a `task_id` to poll with `getVideoSynthesisTask`. The async header must be enabled, and image-to-video models differ in how the reference image is supplied (`input.img_url` vs `input.media`). | 在某个 Wan 模型上提交异步的文生视频或图生视频任务，返回可交给 getVideoSynthesisTask 轮询的 task_id。需开启异步请求头，且不同图生视频模型传参考图的字段不同（input.img_url 与 input.media）。 |
| `param:X-DashScope-Async` | Must be `enable` to run asynchronously (the only mode currently supported). | Switches the request into asynchronous task mode, which is the only mode this endpoint runs in. | 将请求切换为异步任务模式，也是该接口唯一支持的模式。 |
| `req.model` | Video generation model. Use `-t2v` suffix for text-to-video, `-i2v` for image-to-video. **Note the i2v schema difference:** `wan2.6-i2v` takes a reference image via `input.img_url` (string), while `wan2.7-i2v` takes it via `input.media` (array). | Selects which Wan generation model handles the job; the suffix distinguishes text-to-video from image-to-video, and the two image-to-video variants take the reference image through different fields. | 选择由哪个 Wan 模型来处理任务；后缀区分文生视频与图生视频，两个图生视频变体通过不同字段传入参考图。 |
| `req.input` | Required body container. `prompt` is always required; image inputs depend on the model (see field descriptions). | Container for the generation inputs (prompt and optional reference image/audio). | 生成输入的容器（提示词及可选的参考图、参考音频）。 |
| `req.input.prompt` | Text prompt describing the video. Must contain words — empty or whitespace-only prompts fail upstream with `prompt must contain words`. | Text describing the video to generate; must contain actual words, as empty or whitespace-only prompts are rejected upstream. | 描述要生成视频的文本提示词；必须包含实际词语，纯空白会被上游拒绝。 |
| `req.input.negative_prompt` | Optional negative prompt. | Text describing what to keep out of the generated video. | 描述希望在生成视频中避免出现的内容。 |
| `req.input.img_url` | Reference image URL. **Required** for `wan2.6-i2v`. Ignored by t2v models. **Do NOT use for `wan2.7-i2v`** — that model uses `media` instead. | URL of the reference image for the `wan2.6-i2v` image-to-video model; text-to-video models ignore it, and `wan2.7-i2v` uses `input.media` instead. | wan2.6-i2v 图生视频模型的参考图链接；文生视频模型会忽略它，wan2.7-i2v 改用 input.media。 |
| `req.input.media` | Reference image URLs as an array. **Required** for `wan2.7-i2v`. Do NOT use `img_url` with `wan2.7-i2v` — the upstream validator rejects submissions without `input.media`. | Reference image URLs supplied as an array, used by the `wan2.7-i2v` image-to-video model; do not use `input.img_url` with that model. | 以数组形式传入的参考图链接，供 wan2.7-i2v 图生视频模型使用；该模型不要改用 input.img_url。 |
| `req.input.audio_url` | Optional reference audio URL. | URL of an optional reference audio track. | 可选的参考音频链接。 |
| `req.parameters` |  | Container for generation tuning options such as resolution, duration, and seed. | 生成调节项的容器，如分辨率、时长、随机种子等。 |
| `req.parameters.resolution` |  | Output resolution of the generated video. | 生成视频的输出分辨率。 |
| `req.parameters.duration` | Video length in seconds. | Length of the generated clip, in seconds. | 生成片段的时长，单位为秒。 |
| `req.parameters.shot_type` |  | Whether the output is a single continuous shot or stitched from multiple shots. | 输出为单一连续镜头还是由多个镜头拼接。 |
| `req.parameters.watermark` |  | Whether to overlay a watermark on the generated video. | 是否在生成视频上叠加水印。 |
| `req.parameters.seed` |  | Random seed controlling generation; reusing the same seed with identical inputs reproduces the same output. | 控制生成的随机种子；在相同输入下复用同一种子可复现相同结果。 |
| `resp.200.output` |  | Container for the newly created task's identifier and initial status. | 新建任务的标识与初始状态的容器。 |
| `resp.200.output.task_id` | Pass this to `GET /services/aigc/tasks/{task_id}`. | Identifier of the created task; pass it to `getVideoSynthesisTask` to poll for the result. | 所创建任务的标识，传给 getVideoSynthesisTask 轮询结果。 |
| `resp.200.output.task_status` |  | Lifecycle status of the task right after creation, before processing begins. | 任务创建之后、开始处理之前的生命周期状态。 |
| `resp.200.request_id` |  | Identifier of this API call, useful for tracing and support. | 本次接口调用的标识，便于追踪与排障。 |

## getVideoSynthesisTask

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Poll the status and result of a task created by `POST /apis/v1/services/aigc/video-generation/video-synthesis`. The `task_id` is a **path parameter**, not a query string.<br><br>Suggested polling: every 3–5 seconds, with a hard timeout around 5 minutes. | Poll the status and result of a job created by `createVideoSynthesisTask`. Read `output.task_status` to tell lifecycle states apart; on success the playable video URL appears in `output.video_url`. | 轮询由 createVideoSynthesisTask 创建的任务的状态与结果。通过 output.task_status 区分各生命周期状态，成功后可在 output.video_url 取到视频地址。 |
| `param:task_id` | Task ID returned by the video-synthesis create call. Unknown IDs return `task_status: "UNKNOWN"` (HTTP 200). | Identifier of the task to query, as returned by `createVideoSynthesisTask`; unrecognized IDs come back with an unknown status rather than an error. | 要查询的任务标识，由 createVideoSynthesisTask 返回；无法识别的 ID 会返回未知状态而非报错。 |
| `resp.200.output` |  | Container for the task's current status and, once finished, its result or failure details. | 任务当前状态的容器，任务结束后还含结果或失败详情。 |
| `resp.200.output.task_id` |  | Identifier of the queried task. | 所查询任务的标识。 |
| `resp.200.output.task_status` |  | Current lifecycle status of the task; drives whether you keep polling, read the result, or inspect the failure fields. | 任务当前的生命周期状态；据此决定继续轮询、读取结果还是查看失败字段。 |
| `resp.200.output.video_url` | Present on `SUCCEEDED`. Short-lived URL — download and persist the video before it expires. | Link to the generated video, present once the task succeeds; it is short-lived, so download and persist the video promptly. | 生成视频的链接，任务成功后才出现；该链接有效期短，请尽快下载并自行保存。 |
| `resp.200.output.orig_prompt` | The original prompt as stored by the upstream provider. | The original prompt as stored by the upstream provider. | 上游服务保存的原始提示词。 |
| `resp.200.output.submit_time` | When the task was accepted. | When the task was accepted. | 任务被受理的时间。 |
| `resp.200.output.scheduled_time` | When the task was scheduled for execution. | When the task was scheduled for execution. | 任务被调度执行的时间。 |
| `resp.200.output.end_time` | When the task reached a terminal state. | When the task reached a terminal state. | 任务到达终态的时间。 |
| `resp.200.output.code` | Present on `FAILED`. Example: `InvalidParameter`. | Machine-readable error code, present when the task failed. | 机器可读的错误码，任务失败时出现。 |
| `resp.200.output.message` | Present on `FAILED`. Human-readable failure reason. | Human-readable failure reason, present when the task failed. | 可读的失败原因，任务失败时出现。 |
| `resp.200.usage` | Present on `SUCCEEDED`. | Container for resource-usage figures, present once the task succeeds. | 资源用量数据的容器，任务成功后出现。 |
| `resp.200.usage.input_video_duration` | Duration of any input video reference (0 when none). | Duration of any input video reference, in seconds; zero when no input video was provided. | 输入视频参考的时长（秒），未提供输入视频时为 0。 |
| `resp.200.usage.output_video_duration` | Duration of the generated video in seconds. | Duration of the generated video, in seconds. | 生成视频的时长，单位为秒。 |
| `resp.200.usage.duration` | Total duration used for billing. | The duration figure used as the basis for billing. | 用作计费依据的时长数值。 |
| `resp.200.usage.video_count` | Number of videos produced (always 1 today). | Number of videos produced by the task. | 任务生成的视频数量。 |
| `resp.200.usage.size` | Actual dimensions of the generated video, formatted as `WIDTH*HEIGHT` (e.g., `1920*1080`). Note the `*` separator. Present on `wan2.6-*` outputs. | Actual pixel dimensions of the generated video, given as width by height. | 生成视频的实际像素尺寸，以宽乘高的形式给出。 |
| `resp.200.usage.ratio` | Aspect ratio of the output (e.g., `16:9`). Present on `wan2.7-t2v` outputs. | Aspect ratio of the generated video. | 生成视频的宽高比。 |
| `resp.200.usage.SR` | Super-resolution output height. `wan2.6-t2v` upscales 720P input to 1080. `wan2.6-i2v`, `wan2.7-t2v`, `wan2.7-i2v` return 720. | Super-resolution output height the video was upscaled to. | 视频经超分辨率放大后的输出高度。 |
| `resp.200.request_id` |  | Identifier of this API call, useful for tracing and support. | 本次接口调用的标识，便于追踪与排障。 |

