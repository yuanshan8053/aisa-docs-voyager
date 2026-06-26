> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List of Youtube Locations for SERP

> List of YouTube Locations for SERP.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/serp/youtube/locations
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
  /dataforseo/serp/youtube/locations:
    get:
      summary: List of Youtube Locations for SERP
      description: >-
        List of YouTube Locations for SERP. Returns the list of supported
        locations for YouTube SERP. Your account is not charged for using this
        endpoint.
      operationId: get_dataforseo_serp_youtube_locations
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
                    description: Array of available locations
                  tasks[].result[].location_code:
                    type: integer
                    description: Location code
                  tasks[].result[].location_name:
                    type: string
                    description: Location name
                  tasks[].result[].location_code_parent:
                    type: integer
                    description: Parent location code
                  tasks[].result[].country_iso_code:
                    type: string
                    description: Country ISO code
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