> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Check Email Stats

> Check email stats for a specific outreach email.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/emailer_messages/{id}/activities
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
  /apollo/emailer_messages/{id}/activities:
    get:
      summary: Check Email Stats
      description: >-
        Check email stats for a specific outreach email. Requires a master API
        key.
      operationId: get_apollo_emailer_messages_id_activities
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: Emailer message ID.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  emailer_message:
                    type: object
                    description: Email object (when returned).
                  activities:
                    type: array
                    items:
                      type: string
                    description: Activity events (when returned).
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