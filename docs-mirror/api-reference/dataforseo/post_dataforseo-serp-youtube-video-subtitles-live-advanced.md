> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live YouTube Subtitles Advanced

> Live YouTube Subtitles Advanced.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/youtube/video_subtitles/live/advanced
openapi: 3.0.3
info:
  title: DataForSEO API
  version: 1.0.0
  description: DataForSEO API endpoints exposed through the AIsa unified gateway.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /dataforseo/serp/youtube/video_subtitles/live/advanced:
    post:
      summary: Live YouTube Subtitles Advanced
      description: >-
        Live YouTube Subtitles Advanced. Returns YouTube subtitle data in real
        time. Each Live SERP API call can contain only one task.
      operationId: post_dataforseo_serp_youtube_video_subtitles_live_advanced
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                video_id:
                  type: string
                  description: ID of the video
                language_code:
                  type: string
                  description: Subtitle language code
              required:
                - video_id
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  version:
                    type: string
                    description: The current version of the API
                  status_code:
                    type: integer
                    description: General status code
                  status_message:
                    type: string
                    description: General informational message
                  time:
                    type: string
                    description: Execution time, seconds
                  cost:
                    type: number
                    description: Total tasks cost, USD
                  tasks:
                    type: array
                    items:
                      type: string
                    description: Array of tasks
                  tasks[].result:
                    type: array
                    items:
                      type: string
                    description: Array of live SERP results
        '400':
          description: Bad request
        '401':
          description: Unauthorized
        '429':
          description: Rate limit exceeded
        '500':
          description: Internal server error
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````