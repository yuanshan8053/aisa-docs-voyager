> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List of Google Shopping Locations for Merchant API

> You can find the list of available Google Shopping countries on [this page](https://support.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/merchant/google/locations
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
  /dataforseo/merchant/google/locations:
    get:
      summary: List of Google Shopping Locations for Merchant API
      description: >-
        You can find the list of available Google Shopping countries on [this
        page](https://support.google.com/merchants/answer/160637?hl=en&ref_topic=7286989).
      operationId: get_dataforseo_merchant_google_locations
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