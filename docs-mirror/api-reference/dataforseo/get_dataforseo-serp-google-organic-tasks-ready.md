> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Organic SERP Completed Tasks

> Get Organic SERP Completed Tasks.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/serp/google/organic/tasks_ready
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
  /dataforseo/serp/google/organic/tasks_ready:
    get:
      summary: Get Organic SERP Completed Tasks
      description: >-
        Get Organic SERP Completed Tasks. Returns a list of completed standard
        tasks ready for retrieval.
      operationId: get_dataforseo_serp_google_organic_tasks_ready
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
                    description: Request cost in USD
                  tasks_count:
                    type: integer
                    description: Number of tasks returned
                  tasks_error:
                    type: integer
                    description: Number of tasks returned with an error
                  tasks:
                    type: string
                    description: Array of task objects
                  tasks[].result:
                    type: string
                    description: Completed task list
                  tasks[].result[].id:
                    type: string
                    description: Completed task identifier
                  tasks[].result[].endpoint_regular:
                    type: string
                    description: Regular results endpoint
                  tasks[].result[].endpoint_advanced:
                    type: string
                    description: Advanced results endpoint
                  tasks[].result[].endpoint_html:
                    type: string
                    description: HTML results endpoint
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