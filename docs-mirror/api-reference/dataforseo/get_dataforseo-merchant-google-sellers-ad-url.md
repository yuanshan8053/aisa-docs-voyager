> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Google Shopping Sellers Ad URL

> Google Shopping Sellers Ad URL is designed to provide you with a full URL of the advertisement containing all additional parameters set by the seller.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/merchant/google/sellers/ad_url
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
  /dataforseo/merchant/google/sellers/ad_url:
    get:
      summary: Get Google Shopping Sellers Ad URL
      description: >-
        Google Shopping Sellers Ad URL is designed to provide you with a full
        URL of the advertisement containing all additional parameters set by the
        seller.
      operationId: get_dataforseo_merchant_google_sellers_ad_url
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  shop_ad_aclk:
                    type: string
                    description: >-
                      unique ad click referral parameter you can obtain this
                      parameter with Google Shopping Products or Google Shopping
                      Sellers
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