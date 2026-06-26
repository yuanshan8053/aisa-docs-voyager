> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search for Outreach Emails

> Search for outreach emails.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/emailer_messages/search
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
  /apollo/emailer_messages/search:
    get:
      summary: Search for Outreach Emails
      description: Search for outreach emails. Requires a master API key.
      operationId: get_apollo_emailer_messages_search
      parameters:
        - name: emailer_message_stats[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Filter by message stats (e.g., open, click).
        - name: emailer_message_reply_classes[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Filter by reply classes.
        - name: user_ids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Filter by user IDs.
        - name: email_account_id_and_aliases
          in: query
          required: false
          schema:
            type: string
          description: Filter by email account and aliases.
        - name: emailer_campaign_ids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Only include these sequence IDs.
        - name: not_emailer_campaign_ids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Exclude these sequence IDs.
        - name: page
          in: query
          required: false
          schema:
            type: integer
          description: Page number.
        - name: per_page
          in: query
          required: false
          schema:
            type: integer
          description: Results per page.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  emailer_messages:
                    type: array
                    items:
                      type: string
                    description: Outreach emails (when returned).
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