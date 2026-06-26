> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List All Deals

> List all deals (opportunities).



## OpenAPI

````yaml openapi/apollo.json GET /apollo/opportunities/search
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
  /apollo/opportunities/search:
    get:
      summary: List All Deals
      description: List all deals (opportunities). Requires a master API key.
      operationId: get_apollo_opportunities_search
      parameters:
        - name: sort_by_field
          in: query
          required: false
          schema:
            type: string
          description: Sort field
        - name: page
          in: query
          required: false
          schema:
            type: integer
          description: Page number
        - name: per_page
          in: query
          required: false
          schema:
            type: integer
          description: Items per page
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  opportunities:
                    type: string
                    description: Opportunities list
                  opportunities[].id:
                    type: string
                    description: Opportunity ID
                  opportunities[].owner_id:
                    type: string
                    description: Owner ID
                  opportunities[].account_id:
                    type: string
                    description: Account ID
                  opportunities[].amount:
                    type: number
                    description: Amount
                  opportunities[].name:
                    type: string
                    description: Name
                  opportunities[].opportunity_stage_id:
                    type: string
                    description: Stage ID
                  opportunities[].is_closed:
                    type: boolean
                    description: Is closed
                  opportunities[].is_won:
                    type: boolean
                    description: Is won
                  opportunities[].created_at:
                    type: string
                    description: Created timestamp
                  pagination:
                    type: object
                    description: Pagination object
                  pagination.page:
                    type: integer
                    description: Page number
                  pagination.per_page:
                    type: integer
                    description: Items per page
                  pagination.total_entries:
                    type: integer
                    description: Total entries
                  pagination.total_pages:
                    type: integer
                    description: Total pages
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