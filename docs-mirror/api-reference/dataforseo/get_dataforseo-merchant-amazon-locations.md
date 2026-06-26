> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List of Amazon Locations for Merchant API

> Pricing.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/merchant/amazon/locations
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
  /dataforseo/merchant/amazon/locations:
    get:
      summary: List of Amazon Locations for Merchant API
      description: Pricing
      operationId: get_dataforseo_merchant_amazon_locations
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