> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search for Contacts

> Search for contacts.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/contacts/search
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
  /apollo/contacts/search:
    post:
      summary: Search for Contacts
      description: Search for contacts. Requires a master API key.
      operationId: post_apollo_contacts_search
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                q_keywords:
                  type: string
                  description: Keyword query
                contact_stage_ids:
                  type: string
                  description: Filter by contact stage IDs
                contact_label_ids:
                  type: string
                  description: Filter by contact label IDs
                sort_by_field:
                  type: string
                  description: >-
                    Sort field (e.g. contact_last_activity_date,
                    contact_created_at, contact_updated_at)
                sort_ascending:
                  type: boolean
                  description: Sort ascending. Default false.
                per_page:
                  type: integer
                  description: Items per page
                page:
                  type: integer
                  description: Page number
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