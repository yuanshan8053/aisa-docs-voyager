> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# View or Update Deal

> Update fields on an existing deal (opportunity).



## OpenAPI

````yaml openapi/apollo.json PATCH /apollo/opportunities/{opportunity_id}
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
    patch:
      summary: View or Update Deal
      description: >-
        Update fields on an existing deal (opportunity). Requires a master API
        key.
      operationId: patch_apollo_opportunities_opportunity_id
      parameters:
        - name: opportunity_id
          in: path
          required: true
          schema:
            type: string
          description: Opportunity ID
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                owner_id:
                  type: string
                  description: Owner ID
                name:
                  type: string
                  description: Opportunity name
                amount:
                  type: number
                  description: Amount
                opportunity_stage_id:
                  type: string
                  description: Stage ID
                closed_date:
                  type: string
                  description: Closed date (date string)
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