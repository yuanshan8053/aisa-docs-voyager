> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Google Dataset Search Advanced

> Live Google Dataset Search Advanced.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/google/dataset_search/live/advanced
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
  /dataforseo/serp/google/dataset_search/live/advanced:
    post:
      summary: Live Google Dataset Search Advanced
      description: >-
        Live Google Dataset Search Advanced. Returns Google Dataset Search
        results in real time. Each Live SERP API call can contain only one task.
      operationId: post_dataforseo_serp_google_dataset_search_live_advanced
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                keyword:
                  type: string
                  description: Keyword to search datasets for
                language_name:
                  type: string
                  description: Full name of search engine language
                language_code:
                  type: string
                  description: Search engine language code
                os:
                  type: string
                  description: Device operating system
                last_updated:
                  type: string
                  description: Last updated filter
                file_formats:
                  type: array
                  items:
                    type: string
                  description: Dataset file formats
                usage_rights:
                  type: string
                  description: Usage rights filter
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