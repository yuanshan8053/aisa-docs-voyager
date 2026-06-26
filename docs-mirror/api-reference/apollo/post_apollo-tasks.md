> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Task

> Create a task.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/tasks
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
  /apollo/tasks:
    post:
      summary: Create a Task
      description: Create a task. Requires a master API key.
      operationId: post_apollo_tasks
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                user_id:
                  type: string
                  description: Task owner user ID.
                contact_id:
                  type: string
                  description: Contact ID.
                type:
                  type: string
                  description: Task type.
                priority:
                  type: string
                  description: 'Task priority (default: medium).'
                status:
                  type: string
                  description: Task status.
                due_at:
                  type: string
                  description: ISO 8601 due datetime.
                title:
                  type: string
                  description: Optional title.
              required:
                - user_id
                - contact_id
                - type
                - status
                - due_at
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  task:
                    type: object
                    description: Created task (when returned).
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