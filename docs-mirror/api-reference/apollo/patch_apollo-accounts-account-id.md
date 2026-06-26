> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an Account

> Update fields on an existing account.



## OpenAPI

````yaml openapi/apollo.json PATCH /apollo/accounts/{account_id}
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
  /apollo/accounts/{account_id}:
    patch:
      summary: Update an Account
      description: Update fields on an existing account. Requires a master API key.
      operationId: patch_apollo_accounts_account_id
      parameters:
        - name: account_id
          in: path
          required: true
          schema:
            type: string
          description: Account ID
      requestBody:
        required: false
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
                raw_address:
                  type: string
                  description: Raw address
                phone:
                  type: string
                  description: Phone number
                typed_custom_fields:
                  type: object
                  description: Typed custom fields object
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