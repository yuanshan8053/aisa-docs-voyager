> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Contact Stages

> List contact stages.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/contact_stages
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
  /apollo/contact_stages:
    get:
      summary: List Contact Stages
      description: List contact stages. Requires a master API key.
      operationId: get_apollo_contact_stages
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  contact_stages:
                    type: string
                    description: Contact stages list
                  contact_stages[].id:
                    type: string
                    description: Stage ID
                  contact_stages[].team_id:
                    type: string
                    description: Team ID
                  contact_stages[].display_name:
                    type: string
                    description: Display name
                  contact_stages[].name:
                    type: string
                    description: Name
                  contact_stages[].display_order:
                    type: integer
                    description: Display order
                  contact_stages[].ignore_trigger_override:
                    type: boolean
                    description: Ignore trigger override
                  contact_stages[].category:
                    type: string
                    description: Category
                  contact_stages[].is_meeting_set:
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