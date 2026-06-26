> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get video generation task result

> Poll the status of an async video generation task. `task_id` is a path parameter, not a query string.

Poll the status and result of a task created by [`POST /apis/v1/services/aigc/video-generation/video-synthesis`](/api-reference/video/post_services-aigc-video-generation-video-synthesis). The `task_id` goes in the **path**, not the query string.

```bash theme={null}
curl "https://api.aisa.one/apis/v1/services/aigc/tasks/$TASK_ID" \
  -H "Authorization: Bearer $AISA_API_KEY"
```

The endpoint returns HTTP 200 for every known task — inspect `output.task_status` to tell states apart:

| `task_status` | Meaning                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------- |
| `PENDING`     | Accepted, queued                                                                          |
| `RUNNING`     | Actively generating                                                                       |
| `SUCCEEDED`   | Done — `output.video_url` is populated (short-lived, download ASAP)                       |
| `FAILED`      | Failed — `output.code` and `output.message` explain why. **Failed tasks are not billed.** |
| `CANCELED`    | Cancelled                                                                                 |
| `UNKNOWN`     | The provided `task_id` isn't recognised (or expired)                                      |

See [Async Operations](/api-reference/async-operations) for the full polling pattern.


## OpenAPI

````yaml openapi/aliyun-video.json GET /services/aigc/tasks/{task_id}
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
  /services/aigc/tasks/{task_id}:
    get:
      tags:
        - Video Generation
      summary: Get video generation task result
      description: >-
        Poll the status and result of a task created by `POST
        /apis/v1/services/aigc/video-generation/video-synthesis`. The `task_id`
        is a **path parameter**, not a query string.


        Suggested polling: every 3–5 seconds, with a hard timeout around 5
        minutes.
      operationId: getVideoSynthesisTask
      parameters:
        - name: task_id
          in: path
          required: true
          schema:
            type: string
          description: >-
            Task ID returned by the video-synthesis create call. Unknown IDs
            return `task_status: "UNKNOWN"` (HTTP 200).
      responses:
        '200':
          description: >-
            Task status response. Always HTTP 200 — inspect `output.task_status`
            to tell lifecycle states apart.
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
                      task_status:
                        type: string
                        enum:
                          - PENDING
                          - RUNNING
                          - SUCCEEDED
                          - FAILED
                          - CANCELED
                          - UNKNOWN
                      video_url:
                        type: string
                        format: uri
                        description: >-
                          Present on `SUCCEEDED`. Short-lived URL — download and
                          persist the video before it expires.
                      orig_prompt:
                        type: string
                        description: >-
                          The original prompt as stored by the upstream
                          provider.
                      submit_time:
                        type: string
                        description: When the task was accepted.
                      scheduled_time:
                        type: string
                        description: When the task was scheduled for execution.
                      end_time:
                        type: string
                        description: When the task reached a terminal state.
                      code:
                        type: string
                        description: 'Present on `FAILED`. Example: `InvalidParameter`.'
                      message:
                        type: string
                        description: Present on `FAILED`. Human-readable failure reason.
                  usage:
                    type: object
                    description: Present on `SUCCEEDED`.
                    properties:
                      input_video_duration:
                        type: integer
                        description: Duration of any input video reference (0 when none).
                      output_video_duration:
                        type: integer
                        description: Duration of the generated video in seconds.
                      duration:
                        type: number
                        description: Total duration used for billing.
                      video_count:
                        type: integer
                        description: Number of videos produced (always 1 today).
                      size:
                        type: string
                        description: >-
                          Actual dimensions of the generated video, formatted as
                          `WIDTH*HEIGHT` (e.g., `1920*1080`). Note the `*`
                          separator. Present on `wan2.6-*` outputs.
                        example: 1920*1080
                      ratio:
                        type: string
                        description: >-
                          Aspect ratio of the output (e.g., `16:9`). Present on
                          `wan2.7-t2v` outputs.
                        example: '16:9'
                      SR:
                        type: integer
                        description: >-
                          Super-resolution output height. `wan2.6-t2v` upscales
                          720P input to 1080. `wan2.6-i2v`, `wan2.7-t2v`,
                          `wan2.7-i2v` return 720.
                        example: 1080
                  request_id:
                    type: string
              examples:
                succeeded:
                  summary: SUCCEEDED — video_url is populated
                  value:
                    output:
                      task_id: b3be072e-cc82-4033-8fb7-0b089846544f
                      task_status: SUCCEEDED
                      video_url: https://cdn.aisa.one/videos/wan2.6/20260418-abc.mp4
                      orig_prompt: cinematic close-up, slow push-in, shallow depth of field
                      submit_time: '2026-04-18 15:16:01.841'
                      scheduled_time: '2026-04-18 15:16:01.867'
                      end_time: '2026-04-18 15:16:42.512'
                    usage:
                      output_video_duration: 5
                      video_count: 1
                      SR: 720
                    request_id: 8a931b13-c44f-9230-a76b-83487d840060
                failed:
                  summary: FAILED (invalid prompt — not billed)
                  value:
                    output:
                      task_id: b3be072e-cc82-4033-8fb7-0b089846544f
                      task_status: FAILED
                      code: InvalidParameter
                      message: prompt must contain words
                      submit_time: '2026-04-18 15:16:01.841'
                      scheduled_time: '2026-04-18 15:16:01.867'
                      end_time: '2026-04-18 15:16:01.941'
                    request_id: 8a931b13-c44f-9230-a76b-83487d840060
                running:
                  summary: RUNNING (still processing)
                  value:
                    output:
                      task_id: b3be072e-cc82-4033-8fb7-0b089846544f
                      task_status: RUNNING
                    request_id: 8a931b13-c44f-9230-a76b-83487d840060
                unknown:
                  summary: UNKNOWN task_id (still returns HTTP 200)
                  value:
                    output:
                      task_id: bogus-task-id
                      task_status: UNKNOWN
                    request_id: 71b2b0ad-cb6f-9de4-a8bc-a88e4fb72f0e
        '401':
          description: Missing or invalid AIsa API key.
        '500':
          description: >-
            `unsupported uri` — check the path. The correct pattern is
            `/services/aigc/tasks/{task_id}`, not
            `/services/aigc/tasks?task_id=`.
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````