> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Google Dataset Info Tasks

> Setting Google Dataset Info Tasks.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/google/dataset_info/task_post
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
  /dataforseo/serp/google/dataset_info/task_post:
    post:
      summary: Setting Google Dataset Info Tasks
      description: >-
        Setting Google Dataset Info Tasks. Returns detailed information about
        the dataset specified in the request. Your account is charged only for
        setting a task.
      operationId: post_dataforseo_serp_google_dataset_info_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                dataset_id:
                  type: string
                  description: >-
                    ID of the dataset; you can find it in the dataset URL or in
                    a Google Dataset Search result
                language_name:
                  type: string
                  description: Full name of search engine language
                language_code:
                  type: string
                  description: Search engine language code
                device:
                  type: string
                  description: 'Device type; possible value: desktop'
                priority:
                  type: integer
                  description: Task priority
                postback_url:
                  type: string
                  description: URL for sending task results
                pingback_url:
                  type: string
                  description: Notification URL of a completed task
                postback_data:
                  type: string
                  description: 'Postback datatype; possible value: advanced'
              required:
                - dataset_id
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