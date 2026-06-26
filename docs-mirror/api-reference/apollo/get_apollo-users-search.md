> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a List of Users

> Get a list of users.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/users/search
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
  /apollo/users/search:
    get:
      summary: Get a List of Users
      description: Get a list of users. Requires a master API key.
      operationId: get_apollo_users_search
      parameters:
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
                  users:
                    type: array
                    items:
                      type: string
                    description: Users (when returned).
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