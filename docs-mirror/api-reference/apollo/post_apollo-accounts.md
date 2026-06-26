> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an Account

> Create a new account.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/accounts
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
  /apollo/accounts:
    post:
      summary: Create an Account
      description: >-
        Create a new account. Duplicate domains are not allowed. Requires a
        master API key.
      operationId: post_apollo_accounts
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: Account name
                domain:
                  type: string
                  description: Account domain
                owner_id:
                  type: string
                  description: Owner ID
                account_stage_id:
                  type: string
                  description: Account stage ID
              required:
                - name
                - domain
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