> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Google AI Mode SERP

> Returns Google AI Mode SERP results in real time.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/google/ai_mode/live/advanced
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
  /dataforseo/serp/google/ai_mode/live/advanced:
    post:
      summary: Live Google AI Mode SERP
      description: >-
        Returns Google AI Mode SERP results in real time. Each Live SERP call
        can contain only one task.
      operationId: post_dataforseo_serp_google_ai_mode_live_advanced
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
                device:
                  type: string
                  description: 'Device type: desktop or mobile'
                calculate_rectangles:
                  type: boolean
                  description: Enable pixel ranking calculations for elements in SERP
                browser_screen_width:
                  type: integer
                  description: Custom browser screen width
                browser_screen_height:
                  type: integer
                  description: Custom browser screen height
                browser_screen_resolution_ratio:
                  type: number
                  description: Screen resolution ratio for rectangle calculations
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
                    description: Array of tasks
                  tasks[].result:
                    type: array
                    items:
                      type: string
                    description: Array of live SERP results
                  tasks[].result[].keyword:
                    type: string
                    description: Keyword received in the POST array
                  tasks[].result[].type:
                    type: string
                    description: Search engine type in the POST array
                  tasks[].result[].se_domain:
                    type: string
                    description: Search engine domain in the POST array
                  tasks[].result[].location_code:
                    type: integer
                    description: Location code in the POST array
                  tasks[].result[].language_code:
                    type: string
                    description: Language code in the POST array
                  tasks[].result[].check_url:
                    type: string
                    description: Search URL with refinement parameters
                  tasks[].result[].item_types:
                    type: array
                    items:
                      type: string
                    description: Types of search results found in SERP
                  tasks[].result[].items_count:
                    type: integer
                    description: Number of results returned in the items array
                  tasks[].result[].items:
                    type: array
                    items:
                      type: string
                    description: Elements of search results found in SERP
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