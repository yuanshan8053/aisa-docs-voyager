> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a List of Notes

> Get a list of notes.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/notes
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
  /apollo/notes:
    get:
      summary: Get a List of Notes
      description: Get a list of notes. Requires a master API key.
      operationId: get_apollo_notes
      parameters:
        - name: contact_id
          in: query
          required: false
          schema:
            type: string
          description: Filter by a contact ID.
        - name: account_id
          in: query
          required: false
          schema:
            type: string
          description: Filter by an account ID.
        - name: opportunity_id
          in: query
          required: false
          schema:
            type: string
          description: Filter by an opportunity ID.
        - name: calendar_event_id
          in: query
          required: false
          schema:
            type: string
          description: Filter by a calendar event ID.
        - name: conversation_id
          in: query
          required: false
          schema:
            type: string
          description: Filter by a conversation ID.
        - name: conversation_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Filter by conversation IDs.
        - name: contact_ids
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Filter by contact IDs.
        - name: start_date
          in: query
          required: false
          schema:
            type: string
          description: Only include notes created on/after this date (when supported).
        - name: page
          in: query
          required: false
          schema:
            type: integer
          description: Page number (when supported).
        - name: per_page
          in: query
          required: false
          schema:
            type: integer
          description: Results per page (when supported).
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  notes:
                    type: array
                    items:
                      type: string
                    description: Notes (when returned).
                  pagination:
                    type: object
                    description: Pagination metadata (when returned).
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