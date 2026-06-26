> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP API Page Screenshot

> Using the Live Page Screenshot endpoint, you can capture a screenshot of any SERP page.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/screenshot
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
  /dataforseo/serp/screenshot:
    post:
      summary: SERP API Page Screenshot
      description: >-
        Using the Live Page Screenshot endpoint, you can capture a screenshot of
        any SERP page. The screenshot is made by visualizing the HTML of the
        search engine page. Your account is charged for each request.
      operationId: post_dataforseo_serp_screenshot
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                task_id:
                  type: string
                  description: >-
                    Unique identifier of the associated task in UUID format; can
                    be used within 7 days
                browser_preset:
                  type: string
                  description: 'Browser resolution preset: desktop, tablet, or mobile'
                browser_screen_width:
                  type: integer
                  description: Browser resolution width; range 240-9999
                browser_screen_height:
                  type: integer
                  description: Browser resolution height; range 240-9999
                browser_screen_scale_factor:
                  type: number
                  description: Browser scale factor; range 0.5-3
                page:
                  type: integer
                  description: SERP page number to screenshot; default 1
              required:
                - task_id
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
                    description: Total task cost, USD
                  tasks:
                    type: array
                    items:
                      type: string
                    description: Array of tasks
                  tasks[].id:
                    type: string
                    description: Task identifier in UUID format
                  tasks[].status_code:
                    type: integer
                    description: Task status code
                  tasks[].status_message:
                    type: string
                    description: Task status message
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
                    description: Array of results
                  tasks[].result[].items_count:
                    type: integer
                    description: Number of items in the results array
                  tasks[].result[].items:
                    type: array
                    items:
                      type: string
                    description: Items array
                  tasks[].result[].items[].image:
                    type: string
                    description: URL of the page screenshot on DataForSEO storage
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