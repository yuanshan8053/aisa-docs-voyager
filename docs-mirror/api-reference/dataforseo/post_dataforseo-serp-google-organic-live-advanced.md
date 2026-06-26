> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Google Organic SERP Advanced

> Live Google Organic SERP Advanced.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/google/organic/live/advanced
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
  /dataforseo/serp/google/organic/live/advanced:
    post:
      summary: Live Google Organic SERP Advanced
      description: >-
        Live Google Organic SERP Advanced. Returns advanced SERP results
        immediately. Each Live SERP API call can contain only one task.
      operationId: post_dataforseo_serp_google_organic_live_advanced
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
                device:
                  type: string
                  description: 'Device type: desktop or mobile'
                os:
                  type: string
                  description: Device operating system
                depth:
                  type: integer
                  description: Parsing depth, default 100, max 700
                max_crawl_pages:
                  type: integer
                  description: Page crawl limit, max 100
                calculate_rectangles:
                  type: boolean
                  description: Calculate pixel rankings for SERP elements
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
                    description: Request cost in USD
                  tasks_count:
                    type: integer
                    description: Number of tasks returned
                  tasks_error:
                    type: integer
                    description: Number of tasks returned with an error
                  tasks:
                    type: string
                    description: Array of live task objects
                  tasks[].id:
                    type: string
                    description: Task identifier
                  tasks[].result:
                    type: string
                    description: Live SERP advanced results
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