> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Google Ads Search Advanced

> Live Google Ads Search Advanced.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/google/ads_search/live/advanced
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
  /dataforseo/serp/google/ads_search/live/advanced:
    post:
      summary: Live Google Ads Search Advanced
      description: >-
        Live Google Ads Search Advanced. Returns ads search data from Google Ads
        in real time. Each Live SERP API call can contain only one task.
      operationId: post_dataforseo_serp_google_ads_search_live_advanced
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