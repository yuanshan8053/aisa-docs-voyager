> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# View API Usage Stats and Rate Limits

> View API usage stats and rate limits.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/usage_stats/api_usage_stats
openapi: 3.0.3
info:
  title: Apollo API
  version: 1.0.0
  description: Apollo API endpoints exposed through the AIsa unified gateway.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /apollo/usage_stats/api_usage_stats:
    post:
      summary: View API Usage Stats and Rate Limits
      description: View API usage stats and rate limits. Requires a master API key.
      operationId: post_apollo_usage_stats_api_usage_stats
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  api_usage_stats:
                    type: object
                    description: Usage stats and rate limits (when returned).
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