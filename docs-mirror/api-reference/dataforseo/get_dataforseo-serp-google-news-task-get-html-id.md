> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Google News HTML Results by id

> Get Google News HTML Results by id.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/serp/google/news/task_get/html/{id}
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
  /dataforseo/serp/google/news/task_get/html/{id}:
    get:
      summary: Get Google News HTML Results by id
      description: >-
        Get Google News HTML Results by id. Returns HTML results for a
        previously posted task.
      operationId: get_dataforseo_serp_google_news_task_get_html_id
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: Task identifier in UUID format
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
                  tasks[].id:
                    type: string
                    description: Task identifier
                  tasks[].status_code:
                    type: integer
                    description: Task status code
                  tasks[].status_message:
                    type: string
                    description: Task status message
                  tasks[].result:
                    type: array
                    items:
                      type: string
                    description: Array of HTML results
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