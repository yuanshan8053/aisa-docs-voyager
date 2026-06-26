> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Account Owner for Multiple Accounts

> Update account owner for multiple accounts.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/accounts/update_owners
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
  /apollo/accounts/update_owners:
    post:
      summary: Update Account Owner for Multiple Accounts
      description: Update account owner for multiple accounts. Requires a master API key.
      operationId: post_apollo_accounts_update_owners
      parameters:
        - name: account_ids[]
          in: query
          required: true
          schema:
            type: string
          description: Account IDs
        - name: owner_id
          in: query
          required: true
          schema:
            type: string
          description: New owner ID
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
                  accounts[].owner_id:
                    type: string
                    description: Owner ID
                  accounts[].crm_owner_id:
                    type: string
                    description: CRM owner ID
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