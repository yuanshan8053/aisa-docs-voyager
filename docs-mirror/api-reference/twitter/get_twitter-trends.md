> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Trends

> Get Trends



## OpenAPI

````yaml openapi/twitter-trend.json GET /twitter/trends
openapi: 3.0.3
info:
  title: TwitterAPI Unified API
  version: 1.0.0
  description: Unified OpenAPI 3.0 specification for TwitterAPI endpoints.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /twitter/trends:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_trends
      summary: Get Trends
      description: Get trends by WOEID.
      parameters:
        - name: woeid
          in: query
          required: true
          schema:
            type: integer
            format: int64
          description: 'The WOEID of the location. Example: 2418046.'
        - name: count
          in: query
          required: false
          schema:
            type: integer
            format: int64
            default: 30
            minimum: 30
          description: The number of trends to return. Default is 30.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TrendsResponse'
components:
  schemas:
    TrendsResponse:
      type: object
      properties:
        trends:
          type: array
          items:
            $ref: '#/components/schemas/Trend'
        status:
          type: string
          enum:
            - success
            - error
        msg:
          type: string
    Trend:
      type: object
      properties:
        name:
          type: string
        target:
          type: object
          properties:
            query:
              type: string
        rank:
          type: integer
          format: int64
        meta_description:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````