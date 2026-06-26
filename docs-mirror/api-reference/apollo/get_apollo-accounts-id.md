> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# View an Account

> View an account by ID.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/accounts/{id}
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
  /apollo/accounts/{id}:
    get:
      summary: View an Account
      description: View an account by ID. Requires a master API key.
      operationId: get_apollo_accounts_id
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: Account ID
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