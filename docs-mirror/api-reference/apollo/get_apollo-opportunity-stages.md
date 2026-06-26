> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Deal Stages

> List deal stages (opportunity stages).



## OpenAPI

````yaml openapi/apollo.json GET /apollo/opportunity_stages
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
  /apollo/opportunity_stages:
    get:
      summary: List Deal Stages
      description: List deal stages (opportunity stages). Requires a master API key.
      operationId: get_apollo_opportunity_stages
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  opportunity_stages:
                    type: string
                    description: Opportunity stages list
                  opportunity_stages[].id:
                    type: string
                    description: Stage ID
                  opportunity_stages[].team_id:
                    type: string
                    description: Team ID
                  opportunity_stages[].name:
                    type: string
                    description: Name
                  opportunity_stages[].display_order:
                    type: integer
                    description: Display order
                  opportunity_stages[].forecast_category_cd:
                    type: string
                    description: Forecast category code
                  opportunity_stages[].is_won:
                    type: boolean
                    description: Is won
                  opportunity_stages[].is_closed:
                    type: boolean
                    description: Is closed
                  opportunity_stages[].probability:
                    type: number
                    description: Probability
                  opportunity_stages[].description:
                    type: string
                    description: Description
                  opportunity_stages[].opportunity_pipeline_id:
                    type: string
                    description: Opportunity pipeline ID
                  opportunity_stages[].type:
                    type: string
                    description: Type
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