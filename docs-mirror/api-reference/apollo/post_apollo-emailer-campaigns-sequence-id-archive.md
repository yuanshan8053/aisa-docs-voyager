> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Archive a Sequence

> Archive a sequence (marks it inactive and finishes contacts).



## OpenAPI

````yaml openapi/apollo.json POST /apollo/emailer_campaigns/{sequence_id}/archive
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
  /apollo/emailer_campaigns/{sequence_id}/archive:
    post:
      summary: Archive a Sequence
      description: >-
        Archive a sequence (marks it inactive and finishes contacts). Requires a
        master API key.
      operationId: post_apollo_emailer_campaigns_sequence_id_archive
      parameters:
        - name: sequence_id
          in: path
          required: true
          schema:
            type: string
          description: Sequence ID.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  emailer_campaign:
                    type: object
                    description: Archived sequence object (when returned).
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