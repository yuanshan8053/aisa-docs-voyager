> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Search By Image SERP Completed Tasks

> Get Search By Image SERP Completed Tasks.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/serp/google/search_by_image/tasks_ready
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
  /dataforseo/serp/google/search_by_image/tasks_ready:
    get:
      summary: Get Search By Image SERP Completed Tasks
      description: >-
        Get Search By Image SERP Completed Tasks. Returns a list of completed
        tasks that have not been collected yet. Up to 1000 tasks completed
        within the previous 3 days can be returned per call.
      operationId: get_dataforseo_serp_google_search_by_image_tasks_ready
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
                  tasks[].result[].se:
                    type: string
                    description: Search engine specified when setting the task
                  tasks[].result[].se_type:
                    type: string
                    description: Type of search engine
                  tasks[].result[].date_posted:
                    type: string
                    description: Date when the task was posted in UTC format
                  tasks[].result[].tag:
                    type: string
                    description: User-defined task identifier
                  tasks[].result[].endpoint_advanced:
                    type: string
                    description: URL for collecting SERP Advanced results
                  tasks[].result[].endpoint_html:
                    type: string
                    description: URL for collecting SERP HTML results
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