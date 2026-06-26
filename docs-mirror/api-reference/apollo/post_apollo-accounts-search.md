> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search for Accounts

> Search for accounts.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/accounts/search
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
  /apollo/accounts/search:
    post:
      summary: Search for Accounts
      description: Search for accounts. Requires a master API key.
      operationId: post_apollo_accounts_search
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                q_organization_name:
                  type: string
                  description: Organization name query
                account_stage_ids:
                  type: string
                  description: Filter by account stage IDs
                account_label_ids:
                  type: string
                  description: Filter by account label IDs
                sort_by_field:
                  type: string
                  description: >-
                    Sort field (e.g. account_last_activity_date,
                    account_created_at, account_updated_at)
                sort_ascending:
                  type: boolean
                  description: Sort ascending
                page:
                  type: integer
                  description: Page number
                per_page:
                  type: integer
                  description: Items per page
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