> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search for Tasks

> Search tasks.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/tasks/search
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
  /apollo/tasks/search:
    post:
      summary: Search for Tasks
      description: Search tasks. Requires a master API key.
      operationId: post_apollo_tasks_search
      parameters:
        - name: sort_by_field
          in: query
          required: false
          schema:
            type: string
          description: Sort field.
        - name: open_factor_names[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: Optional open factors.
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
                  tasks:
                    type: array
                    items:
                      type: string
                    description: Tasks (when returned).
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