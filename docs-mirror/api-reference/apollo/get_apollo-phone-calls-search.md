> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search for Calls

> Search calls.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/phone_calls/search
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
  /apollo/phone_calls/search:
    get:
      summary: Search for Calls
      description: Search calls. Requires a master API key.
      operationId: get_apollo_phone_calls_search
      parameters:
        - name: date_range[max]
          in: query
          required: false
          schema:
            type: string
          description: Upper bound for call date range (YYYY-MM-DD).
        - name: date_range[min]
          in: query
          required: false
          schema:
            type: string
          description: Lower bound for call date range (YYYY-MM-DD).
        - name: duration[max]
          in: query
          required: false
          schema:
            type: integer
          description: Upper bound for duration (seconds).
        - name: duration[min]
          in: query
          required: false
          schema:
            type: integer
          description: Lower bound for duration (seconds).
        - name: inbound
          in: query
          required: false
          schema:
            type: string
          description: Inbound or outbound.
        - name: user_ids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: User IDs.
        - name: contact_label_ids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Contact label IDs.
        - name: phone_call_purpose_ids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Purpose IDs.
        - name: phone_call_outcome_ids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Outcome IDs.
        - name: q_keywords
          in: query
          required: false
          schema:
            type: string
          description: Keyword filter.
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
                  phone_calls:
                    type: array
                    items:
                      type: string
                    description: Calls (when returned).
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