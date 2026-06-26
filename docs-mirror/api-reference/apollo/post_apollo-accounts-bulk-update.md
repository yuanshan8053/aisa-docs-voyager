> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Update Accounts

> Bulk update accounts.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/accounts/bulk_update
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
  /apollo/accounts/bulk_update:
    post:
      summary: Bulk Update Accounts
      description: Bulk update accounts. Requires a master API key.
      operationId: post_apollo_accounts_bulk_update
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                account_ids:
                  type: string
                  description: IDs of accounts to update
                account_attributes:
                  type: string
                  description: List of account attribute update objects
                account_attributes[].name:
                  type: string
                  description: Account name
                account_attributes[].owner_id:
                  type: string
                  description: Owner ID
                account_attributes[].account_stage_id:
                  type: string
                  description: Account stage ID
                async:
                  type: boolean
                  description: Run asynchronously. Default false.
              required:
                - account_ids
                - account_attributes
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  accounts:
                    type: string
                    description: Updated accounts
                  accounts[].id:
                    type: string
                    description: Account ID
                  accounts[].account_stage_id:
                    type: string
                    description: Account stage ID
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