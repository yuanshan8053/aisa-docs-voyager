> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Account Stages

> List account stages.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/account_stages
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
  /apollo/account_stages:
    get:
      summary: List Account Stages
      description: List account stages. Requires a master API key.
      operationId: get_apollo_account_stages
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  account_stages:
                    type: string
                    description: Account stages list
                  account_stages[].id:
                    type: string
                    description: Stage ID
                  account_stages[].team_id:
                    type: string
                    description: Team ID
                  account_stages[].display_name:
                    type: string
                    description: Display name
                  account_stages[].name:
                    type: string
                    description: Name
                  account_stages[].display_order:
                    type: integer
                    description: Display order
                  account_stages[].default_exclude_for_leadgen:
                    type: boolean
                    description: Default exclude for leadgen
                  account_stages[].category:
                    type: string
                    description: Category
                  account_stages[].is_meeting_set:
                    type: boolean
                    description: Is meeting set
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