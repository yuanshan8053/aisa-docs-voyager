> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Video Comments SERP Completed Tasks

> Get Video Comments SERP Completed Tasks.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/serp/youtube/video_comments/tasks_ready
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
  /dataforseo/serp/youtube/video_comments/tasks_ready:
    get:
      summary: Get Video Comments SERP Completed Tasks
      description: >-
        Get Video Comments SERP Completed Tasks. Returns completed YouTube
        Comments tasks that have not been collected yet.
      operationId: get_dataforseo_serp_youtube_video_comments_tasks_ready
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
                  tasks_count:
                    type: integer
                    description: The number of tasks in the tasks array
                  tasks_error:
                    type: integer
                    description: >-
                      The number of tasks in the tasks array returned with an
                      error
                  tasks:
                    type: array
                    items:
                      type: string
                    description: Array of tasks
                  tasks[].result:
                    type: array
                    items:
                      type: string
                    description: Array of completed task references
                  tasks[].result[].id:
                    type: string
                    description: Task identifier of the completed task
                  tasks[].result[].endpoint_advanced:
                    type: string
                    description: URL for collecting advanced results
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