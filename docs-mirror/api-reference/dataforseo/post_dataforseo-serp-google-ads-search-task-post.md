> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Google Ads Search SERP Tasks

> Setting Google Ads Search SERP Tasks.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/google/ads_search/task_post
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
  /dataforseo/serp/google/ads_search/task_post:
    post:
      summary: Setting Google Ads Search SERP Tasks
      description: >-
        Setting Google Ads Search SERP Tasks. Returns ads run by advertisers on
        Google Ads. Historical data is available from 2018-05-31. Your account
        is charged only for setting a task.
      operationId: post_dataforseo_serp_google_ads_search_task_post
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                advertiser_ids:
                  type: array
                  items:
                    type: string
                  description: Advertiser identifiers; required if target is not specified
                target:
                  type: string
                  description: >-
                    Domain name associated with an advertiser account; required
                    if advertiser_ids is not specified
                location_name:
                  type: string
                  description: Full name of search engine location
                location_code:
                  type: integer
                  description: Search engine location code
                location_coordinate:
                  type: string
                  description: GPS coordinates of a location
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
                  description: Postback datatype; only advanced is supported
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