> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Deal

> Create a deal (opportunity).



## OpenAPI

````yaml openapi/apollo.json POST /apollo/opportunities
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
  /apollo/opportunities:
    post:
      summary: Create Deal
      description: Create a deal (opportunity). Requires a master API key.
      operationId: post_apollo_opportunities
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: Deal name
                owner_id:
                  type: string
                  description: Owner ID
                account_id:
                  type: string
                  description: Account ID
                amount:
                  type: number
                  description: Deal amount
                opportunity_stage_id:
                  type: string
                  description: Deal stage ID
                closed_date:
                  type: string
                  description: Closed date (date string)
                typed_custom_fields:
                  type: object
                  description: Typed custom fields object
              required:
                - name
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
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