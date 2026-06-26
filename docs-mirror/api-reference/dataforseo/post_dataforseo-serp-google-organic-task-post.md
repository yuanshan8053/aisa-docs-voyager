> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Google Organic SERP Tasks

> Setting Google Organic SERP Tasks.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/google/organic/task_post
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
  /dataforseo/serp/google/organic/task_post:
    post:
      summary: Setting Google Organic SERP Tasks
      description: >-
        Setting Google Organic SERP Tasks. Standard task-based endpoint. Your
        account is charged only for setting a task. You can send up to 100 tasks
        per POST call.
      operationId: post_dataforseo_serp_google_organic_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                keyword:
                  type: string
                  description: Keyword to search for
                location_name:
                  type: string
                  description: Full name of search engine location
                location_code:
                  type: integer
                  description: Search engine location code
                location_coordinate:
                  type: string
                  description: GPS coordinates of a location
                language_name:
                  type: string
                  description: Full name of search engine language
                language_code:
                  type: string
                  description: Search engine language code
                depth:
                  type: integer
                  description: Parsing depth, default 100, max 700
                max_crawl_pages:
                  type: integer
                  description: Page crawl limit, max 100
                device:
                  type: string
                  description: 'Device type: desktop or mobile'
                os:
                  type: string
                  description: Device operating system
                group_organic_results:
                  type: boolean
                  description: Display related results as grouped organic results
                calculate_rectangles:
                  type: boolean
                  description: >-
                    Calculate pixel rankings for SERP elements in advanced
                    results
                postback_url:
                  type: string
                  description: Postback URL for completed task results
                pingback_url:
                  type: string
                  description: Pingback URL for task completion notification
                postback_data:
                  type: string
                  description: Postback payload type
                tag:
                  type: string
                  description: User-defined task identifier
              required:
                - keyword
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
                    description: Total tasks cost in USD
                  tasks_count:
                    type: integer
                    description: Number of tasks in the request
                  tasks_error:
                    type: integer
                    description: Number of tasks returned with an error
                  tasks:
                    type: string
                    description: Array of task objects
                  tasks[].id:
                    type: string
                    description: Task identifier in UUID format
                  tasks[].status_code:
                    type: integer
                    description: Task status code
                  tasks[].status_message:
                    type: string
                    description: Task status message
                  tasks[].cost:
                    type: number
                    description: Task cost
                  tasks[].result_count:
                    type: integer
                    description: Number of result elements
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