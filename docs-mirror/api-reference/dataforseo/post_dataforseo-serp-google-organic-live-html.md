> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Google Organic SERP HTML

> Live Google Organic SERP HTML.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/google/organic/live/html
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
  /dataforseo/serp/google/organic/live/html:
    post:
      summary: Live Google Organic SERP HTML
      description: >-
        Live Google Organic SERP HTML. Returns raw HTML immediately. Each Live
        SERP API call can contain only one task.
      operationId: post_dataforseo_serp_google_organic_live_html
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  description: Direct URL of the search query
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
                se_domain:
                  type: string
                  description: Custom search engine domain
                depth:
                  type: integer
                  description: Parsing depth, default 100, max 700
                max_crawl_pages:
                  type: integer
                  description: Page crawl limit, max 100
                search_param:
                  type: string
                  description: Additional parameters of the search query
                load_async_ai_overview:
                  type: boolean
                  description: Load asynchronous AI overview
                expand_ai_overview:
                  type: boolean
                  description: Expand AI overview item
                tag:
                  type: string
                  description: User-defined task identifier
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
                    description: Result array containing HTML pages
                  tasks[].result[].items:
                    type: string
                    description: HTML page items
                  tasks[].result[].items[].html:
                    type: string
                    description: Raw HTML page content
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