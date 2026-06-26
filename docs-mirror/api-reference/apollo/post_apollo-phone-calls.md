> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Call Records

> Create call records.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/phone_calls
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
  /apollo/phone_calls:
    post:
      summary: Create Call Records
      description: Create call records. Requires a master API key.
      operationId: post_apollo_phone_calls
      parameters:
        - name: logged
          in: query
          required: false
          schema:
            type: boolean
          description: Whether to create an individual record.
        - name: user_id[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Caller user IDs.
        - name: contact_id
          in: query
          required: false
          schema:
            type: string
          description: Contact ID.
        - name: account_id
          in: query
          required: false
          schema:
            type: string
          description: Account ID.
        - name: to_number
          in: query
          required: false
          schema:
            type: string
          description: Dialed phone number.
        - name: from_number
          in: query
          required: false
          schema:
            type: string
          description: Caller phone number.
        - name: status
          in: query
          required: false
          schema:
            type: string
          description: Call status.
        - name: start_time
          in: query
          required: false
          schema:
            type: string
          description: ISO 8601 start time.
        - name: end_time
          in: query
          required: false
          schema:
            type: string
          description: ISO 8601 end time.
        - name: duration
          in: query
          required: false
          schema:
            type: integer
          description: Duration in seconds.
        - name: phone_call_purpose_id
          in: query
          required: false
          schema:
            type: string
          description: Purpose ID.
        - name: phone_call_outcome_id
          in: query
          required: false
          schema:
            type: string
          description: Outcome ID.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  phone_call:
                    type: object
                    description: Call record (when returned).
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