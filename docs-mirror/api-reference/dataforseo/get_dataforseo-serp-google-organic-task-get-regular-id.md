> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Google Organic SERP Results by id

> Get Google Organic SERP Results by id.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/serp/google/organic/task_get/regular/{id}
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
  /dataforseo/serp/google/organic/task_get/regular/{id}:
    get:
      summary: Get Google Organic SERP Results by id
      description: >-
        Get Google Organic SERP Results by id. Retrieve regular task results for
        a posted task within 30 days at no extra charge.
      operationId: get_dataforseo_serp_google_organic_task_get_regular_id
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
                    description: API version
                  status_code:
                    type: integer
                    description: General status code
                  status_message:
                    type: string
                    description: General informational message
                  time:
                    type: string
                    description: Execution time
                  cost:
                    type: number
                    description: Task cost in USD
                  tasks_count:
                    type: integer
                    description: Number of tasks returned
                  tasks_error:
                    type: integer
                    description: Number of tasks returned with an error
                  tasks:
                    type: string
                    description: Array of task objects
                  tasks[].id:
                    type: string
                    description: Task identifier
                  tasks[].result:
                    type: string
                    description: Result array for the task
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