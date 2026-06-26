> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List of DataForSEO Trends Locations

> ![checked](https://docs.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/keywords_data/dataforseo_trends/locations
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
  /dataforseo/keywords_data/dataforseo_trends/locations:
    get:
      summary: List of DataForSEO Trends Locations
      description: >-
        ![checked](https://docs.dataforseo.com/v3/wp-content/themes/dataforseo/assets/img/icons/checked-circle.svg)
        GET
        https://api.dataforseo.com/v3/keywords\_data/dataforseo\_trends/locations
      operationId: get_dataforseo_keywords_data_dataforseo_trends_locations
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  country:
                    type: string
                    description: >-
                      country ISO code optional field specify the ISO code if
                      you want to filter the list of locations by country
                      example: us
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