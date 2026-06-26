> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Google AI Mode SERP Tasks

> Google AI Mode SERP API provides search results from the AI Mode feature of Google Search.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/google/ai_mode/task_post
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
  /dataforseo/serp/google/ai_mode/task_post:
    post:
      summary: Setting Google AI Mode SERP Tasks
      description: >-
        Google AI Mode SERP API provides search results from the AI Mode feature
        of Google Search. Send JSON task arrays; up to 100 tasks per POST call.
        Completed tasks can be retrieved later by id, postback_url, or
        pingback_url.
      operationId: post_dataforseo_serp_google_ai_mode_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                keyword:
                  type: string
                  description: Keyword; you can specify up to 700 characters
                location_code:
                  type: integer
                  description: >-
                    Search engine location code; required if location_name or
                    location_coordinate is not specified
                location_name:
                  type: string
                  description: >-
                    Full name of search engine location; required if
                    location_code or location_coordinate is not specified
                location_coordinate:
                  type: string
                  description: >-
                    GPS coordinates of a location; required if location_name or
                    location_code is not specified
                language_name:
                  type: string
                  description: >-
                    Full name of search engine language; required if
                    language_code is not specified
                language_code:
                  type: string
                  description: >-
                    Search engine language code; required if language_name is
                    not specified
                priority:
                  type: integer
                  description: 'Task priority: 1 normal (default), 2 high'
                device:
                  type: string
                  description: 'Device type: desktop or mobile'
                pingback_url:
                  type: string
                  description: Notification URL of a completed task
                postback_url:
                  type: string
                  description: URL for sending task results
                postback_data:
                  type: string
                  description: >-
                    Postback URL datatype; required if postback_url is
                    specified; possible values: advanced, html
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
                    description: Cost of the task, USD
                  tasks[].result_count:
                    type: integer
                    description: Number of elements in the result array
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