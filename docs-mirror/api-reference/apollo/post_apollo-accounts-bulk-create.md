> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Create Accounts

> Bulk create accounts.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/accounts/bulk_create
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
  /apollo/accounts/bulk_create:
    post:
      summary: Bulk Create Accounts
      description: Bulk create accounts. Requires a master API key.
      operationId: post_apollo_accounts_bulk_create
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                accounts:
                  type: string
                  description: Array of accounts to create
                append_label_names:
                  type: string
                  description: Label names to append to each created account
                run_dedupe:
                  type: boolean
                  description: Enable deduplication. Default false.
              required:
                - accounts
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  created_accounts:
                    type: string
                    description: Accounts created in this request
                  created_accounts[].id:
                    type: string
                    description: Account ID
                  created_accounts[].name:
                    type: string
                    description: Account name
                  created_accounts[].domain:
                    type: string
                    description: Account domain
                  created_accounts[].team_id:
                    type: string
                    description: Team ID
                  created_accounts[].owner_id:
                    type: string
                    description: Owner ID
                  created_accounts[].account_stage_id:
                    type: string
                    description: Account stage ID
                  created_accounts[].phone:
                    type: string
                    description: Phone number
                  created_accounts[].created_at:
                    type: string
                    description: Created timestamp
                  created_accounts[].updated_at:
                    type: string
                    description: Updated timestamp
                  existing_accounts:
                    type: string
                    description: Accounts that already existed (dedupe matches)
                  existing_accounts[].id:
                    type: string
                    description: Account ID
                  existing_accounts[].name:
                    type: string
                    description: Account name
                  existing_accounts[].domain:
                    type: string
                    description: Account domain
                  existing_accounts[].team_id:
                    type: string
                    description: Team ID
                  existing_accounts[].owner_id:
                    type: string
                    description: Owner ID
                  existing_accounts[].account_stage_id:
                    type: string
                    description: Account stage ID
                  existing_accounts[].phone:
                    type: string
                    description: Phone number
                  existing_accounts[].created_at:
                    type: string
                    description: Created timestamp
                  existing_accounts[].updated_at:
                    type: string
                    description: Updated timestamp
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