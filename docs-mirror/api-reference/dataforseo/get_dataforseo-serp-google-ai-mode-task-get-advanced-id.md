> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Google AI Mode SERP Advanced Results by id

> Retrieve Google AI Mode SERP advanced results by task id.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/serp/google/ai_mode/task_get/advanced/{id}
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
  /dataforseo/serp/google/ai_mode/task_get/advanced/{id}:
    get:
      summary: Get Google AI Mode SERP Advanced Results by id
      description: >-
        Retrieve Google AI Mode SERP advanced results by task id. Results can be
        requested within 30 days after task creation at no extra charge beyond
        posting the task.
      operationId: get_dataforseo_serp_google_ai_mode_task_get_advanced_id
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
                  tasks[].time:
                    type: string
                    description: Execution time, seconds
                  tasks[].cost:
                    type: number
                    description: Cost of the task, USD
                  tasks[].result_count:
                    type: integer
                    description: Number of elements in the result array
                  tasks[].path:
                    type: array
                    items:
                      type: string
                    description: URL path
                  tasks[].data:
                    type: object
                    description: Contains the same parameters specified in the POST request
                  tasks[].result:
                    type: array
                    items:
                      type: string
                    description: Array of SERP results
                  tasks[].result[].keyword:
                    type: string
                    description: Keyword received in the POST array
                  tasks[].result[].type:
                    type: string
                    description: Search engine type in the POST array
                  tasks[].result[].check_url:
                    type: string
                    description: Search URL with refinement parameters
                  tasks[].result[].item_types:
                    type: array
                    items:
                      type: string
                    description: Types of search results found in SERP
                  tasks[].result[].se_results_count:
                    type: integer
                    description: Total number of results in SERP
                  tasks[].result[].items_count:
                    type: integer
                    description: Number of results returned in the items array
                  tasks[].result[].items:
                    type: array
                    items:
                      type: string
                    description: Elements of search results found in SERP
                  tasks[].result[].items[].type:
                    type: string
                    description: Type of element, such as ai_overview
                  tasks[].result[].items[].markdown:
                    type: string
                    description: Content of the element in markdown format
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