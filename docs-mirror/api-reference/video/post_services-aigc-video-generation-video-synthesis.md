> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create video generation task

> Submit an async text-to-video or image-to-video task with any of 4 Wan models (wan2.6-t2v, wan2.6-i2v, wan2.7-t2v, wan2.7-i2v). Returns a task_id to poll.

Submit an asynchronous video generation task. Returns a `task_id` to poll via [`GET /apis/v1/services/aigc/tasks/{task_id}`](/api-reference/video/get_services-aigc-tasks).

## Supported models

Four Wan variants share this endpoint:

| Model        | Kind           | Image input field    | Output SR |
| ------------ | -------------- | -------------------- | --------- |
| `wan2.6-t2v` | text-to-video  | *n/a*                | 1080      |
| `wan2.6-i2v` | image-to-video | `input.img_url`      | 720       |
| `wan2.7-t2v` | text-to-video  | *n/a*                | 720       |
| `wan2.7-i2v` | image-to-video | **`input.media`** ⚠️ | 720       |

<Warning>
  **Schema trap on `wan2.7-i2v`.** It takes the reference image in `input.media` (an **array** of URL strings), not `input.img_url` like `wan2.6-i2v`. Submissions without `media` succeed at HTTP 200 with a `task_id`, then fail downstream with `code: "InvalidParameter"` / `message: "Field required: input.media"`. The task is **not billed** — but you wasted a round trip.
</Warning>

## Minimal bodies

<CodeGroup>
  ```json wan2.6-t2v theme={null}
  {
    "model": "wan2.6-t2v",
    "input": {
      "prompt": "cinematic close-up, slow push-in, shallow depth of field"
    },
    "parameters": { "resolution": "720P", "duration": 5 }
  }
  ```

  ```json wan2.6-i2v theme={null}
  {
    "model": "wan2.6-i2v",
    "input": {
      "prompt": "gentle camera orbit, golden hour lighting",
      "img_url": "https://example.com/reference.jpg"
    },
    "parameters": { "resolution": "1080P", "duration": 10 }
  }
  ```

  ```json wan2.7-t2v theme={null}
  {
    "model": "wan2.7-t2v",
    "input": {
      "prompt": "wide sweeping shot of a neon cyberpunk skyline at dusk"
    },
    "parameters": { "resolution": "720P", "duration": 5 }
  }
  ```

  ```json wan2.7-i2v theme={null}
  {
    "model": "wan2.7-i2v",
    "input": {
      "prompt": "gentle zoom with parallax, cinematic color grading",
      "media": ["https://example.com/reference.jpg"]
    },
    "parameters": { "resolution": "720P", "duration": 5 }
  }
  ```
</CodeGroup>

## Required pieces

* **Header**: `X-DashScope-Async: enable`
* **Body**: `model` + `input.prompt` always. Image field only for `-i2v` models (see table).

## What the response looks like

```json theme={null}
{
  "output": {
    "task_id": "b3be072e-cc82-4033-8fb7-0b089846544f",
    "task_status": "PENDING"
  },
  "request_id": "8a931b13-c44f-9230-a76b-83487d840060"
}
```

Save the `task_id` and poll [`/services/aigc/tasks/{task_id}`](/api-reference/video/get_services-aigc-tasks) every 3–5 s. See [Async Operations](/api-reference/async-operations) for the full polling pattern (including failure handling).


## OpenAPI

````yaml openapi/aliyun-video.json POST /services/aigc/video-generation/video-synthesis
openapi: 3.0.3
info:
  title: AIsa Video Generation API (async)
  version: 1.0.0
  description: >-
    Asynchronous video generation. Submit a task via `POST
    /apis/v1/services/aigc/video-generation/video-synthesis`, then poll `GET
    /apis/v1/services/aigc/tasks/{task_id}` until the status is `SUCCEEDED` or
    `FAILED`.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /services/aigc/video-generation/video-synthesis:
    post:
      tags:
        - Video Generation
      summary: Create a video generation task
      description: >-
        Submit an asynchronous video generation task. Returns a `task_id` you
        then poll via `GET /apis/v1/services/aigc/tasks/{task_id}`.


        **Models.** Four Wan variants are accepted on this single endpoint:


        | Model | Kind | Image input field |

        | --- | --- | --- |

        | `wan2.6-t2v` | text-to-video | _n/a_ |

        | `wan2.6-i2v` | image-to-video | `input.img_url` |

        | `wan2.7-t2v` | text-to-video | _n/a_ |

        | `wan2.7-i2v` | image-to-video | `input.media` ⚠️ *not* `input.img_url`
        |


        **Header.** `X-DashScope-Async: enable` is required.


        **Body.** `model` and `input.prompt` are always required. For i2v,
        provide a reference image using the field indicated in the table above —
        `wan2.6-i2v` uses `input.img_url` (string URL), while `wan2.7-i2v` uses
        `input.media` (array of URLs).


        Failed tasks (e.g., invalid prompt, missing required field) are **not
        billed** — the task-status response returns `task_status: "FAILED"` with
        a `code` and `message`.
      operationId: createVideoSynthesisTask
      parameters:
        - name: X-DashScope-Async
          in: header
          required: true
          schema:
            type: string
            enum:
              - enable
          description: >-
            Must be `enable` to run asynchronously (the only mode currently
            supported).
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - model
                - input
              properties:
                model:
                  type: string
                  enum:
                    - wan2.6-t2v
                    - wan2.6-i2v
                    - wan2.7-t2v
                    - wan2.7-i2v
                  description: >-
                    Video generation model. Use `-t2v` suffix for text-to-video,
                    `-i2v` for image-to-video. **Note the i2v schema
                    difference:** `wan2.6-i2v` takes a reference image via
                    `input.img_url` (string), while `wan2.7-i2v` takes it via
                    `input.media` (array).
                  example: wan2.6-t2v
                input:
                  type: object
                  required:
                    - prompt
                  description: >-
                    Required body container. `prompt` is always required; image
                    inputs depend on the model (see field descriptions).
                  properties:
                    prompt:
                      type: string
                      description: >-
                        Text prompt describing the video. Must contain words —
                        empty or whitespace-only prompts fail upstream with
                        `prompt must contain words`.
                    negative_prompt:
                      type: string
                      description: Optional negative prompt.
                    img_url:
                      type: string
                      format: uri
                      description: >-
                        Reference image URL. **Required** for `wan2.6-i2v`.
                        Ignored by t2v models. **Do NOT use for `wan2.7-i2v`** —
                        that model uses `media` instead.
                    media:
                      type: array
                      items:
                        type: string
                        format: uri
                      description: >-
                        Reference image URLs as an array. **Required** for
                        `wan2.7-i2v`. Do NOT use `img_url` with `wan2.7-i2v` —
                        the upstream validator rejects submissions without
                        `input.media`.
                    audio_url:
                      type: string
                      format: uri
                      description: Optional reference audio URL.
                parameters:
                  type: object
                  properties:
                    resolution:
                      type: string
                      enum:
                        - 720P
                        - 1080P
                      default: 720P
                    duration:
                      type: integer
                      enum:
                        - 5
                        - 10
                      default: 5
                      description: Video length in seconds.
                    shot_type:
                      type: string
                      enum:
                        - single
                        - multi
                      default: single
                    watermark:
                      type: boolean
                      default: false
                    seed:
                      type: integer
                      minimum: 0
                      maximum: 2147483647
            examples:
              wan26_t2v:
                summary: wan2.6-t2v — text-to-video, 5 s, 720P
                value:
                  model: wan2.6-t2v
                  input:
                    prompt: cinematic close-up, slow push-in, shallow depth of field
                  parameters:
                    resolution: 720P
                    duration: 5
              wan26_i2v:
                summary: wan2.6-i2v — image-to-video (uses img_url)
                value:
                  model: wan2.6-i2v
                  input:
                    prompt: gentle camera orbit, golden hour lighting
                    img_url: https://example.com/reference.jpg
                  parameters:
                    resolution: 1080P
                    duration: 10
              wan27_t2v:
                summary: wan2.7-t2v — text-to-video, newer model
                value:
                  model: wan2.7-t2v
                  input:
                    prompt: wide sweeping shot of a neon cyberpunk skyline at dusk
                  parameters:
                    resolution: 720P
                    duration: 5
              wan27_i2v:
                summary: wan2.7-i2v — image-to-video (uses media ARRAY, not img_url)
                value:
                  model: wan2.7-i2v
                  input:
                    prompt: gentle zoom with parallax, cinematic color grading
                    media:
                      - https://example.com/reference.jpg
                  parameters:
                    resolution: 720P
                    duration: 5
      responses:
        '200':
          description: Task created — poll `/services/aigc/tasks/{task_id}` for progress.
          content:
            application/json:
              schema:
                type: object
                properties:
                  output:
                    type: object
                    properties:
                      task_id:
                        type: string
                        description: Pass this to `GET /services/aigc/tasks/{task_id}`.
                      task_status:
                        type: string
                        enum:
                          - PENDING
                  request_id:
                    type: string
              example:
                output:
                  task_id: b3be072e-cc82-4033-8fb7-0b089846544f
                  task_status: PENDING
                request_id: 8a931b13-c44f-9230-a76b-83487d840060
        '400':
          description: Invalid request body.
        '401':
          description: Missing or invalid AIsa API key.
        '429':
          description: Rate limit hit.
        '500':
          description: >-
            `model not supported` (the model isn't routed through this endpoint)
            or `input param is required` (body missing `input`).


            Note: for `wan2.7-i2v`, submission **succeeds with HTTP 200** even
            without the image input — the task later lands in `FAILED` status
            with `code: "InvalidParameter"` and `message: "Field required:
            input.media"`.
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````