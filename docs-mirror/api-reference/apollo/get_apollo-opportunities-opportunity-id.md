> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# View or Update Deal

> View a deal (opportunity) by ID.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/opportunities/{opportunity_id}
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
  /apollo/opportunities/{opportunity_id}:
    get:
      summary: View or Update Deal
      description: View a deal (opportunity) by ID. Requires a master API key.
      operationId: get_apollo_opportunities_opportunity_id
      parameters:
        - name: opportunity_id
          in: path
          required: true
          schema:
            type: string
          description: Opportunity ID
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  opportunity:
                    type: object
                    description: Opportunity object
                  opportunity.id:
                    type: string
                    description: Opportunity ID
                  opportunity.owner_id:
                    type: string
                    description: Owner ID
                  opportunity.account_id:
                    type: string
                    description: Account ID
                  opportunity.amount:
                    type: number
                    description: Amount
                  opportunity.name:
                    type: string
                    description: Name
                  opportunity.opportunity_stage_id:
                    type: string
                    description: Stage ID
                  opportunity.is_closed:
                    type: boolean
                    description: Is closed
                  opportunity.is_won:
                    type: boolean
                    description: Is won
                  opportunity.created_at:
                    type: string
                    description: Created timestamp
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