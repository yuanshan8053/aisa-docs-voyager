> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search for Sequences

> Search for sequences (emailer campaigns) in your Apollo account.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/emailer_campaigns/search
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
  /apollo/emailer_campaigns/search:
    post:
      summary: Search for Sequences
      description: >-
        Search for sequences (emailer campaigns) in your Apollo account.
        Requires a master API key.
      operationId: post_apollo_emailer_campaigns_search
      parameters:
        - name: q_name
          in: query
          required: false
          schema:
            type: string
          description: Keywords to match sequence names.
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
                  emailer_campaigns:
                    type: array
                    items:
                      type: string
                    description: Sequence records (when returned).
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