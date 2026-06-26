> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Contact Status in a Sequence

> Update contact status in a sequence.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/emailer_campaigns/remove_or_stop_contact_ids
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
  /apollo/emailer_campaigns/remove_or_stop_contact_ids:
    post:
      summary: Update Contact Status in a Sequence
      description: Update contact status in a sequence. Requires a master API key.
      operationId: post_apollo_emailer_campaigns_remove_or_stop_contact_ids
      parameters:
        - name: emailer_campaign_ids[]
          in: query
          required: true
          schema:
            type: array
            items:
              type: string
          description: Sequence IDs.
        - name: contact_ids[]
          in: query
          required: true
          schema:
            type: array
            items:
              type: string
          description: Contact IDs.
        - name: mode
          in: query
          required: true
          schema:
            type: string
          description: 'One of: mark_as_finished, remove, stop.'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    description: Whether the update succeeded (when returned).
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