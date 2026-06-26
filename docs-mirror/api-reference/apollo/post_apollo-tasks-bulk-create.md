> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Create Tasks

> Bulk create tasks.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/tasks/bulk_create
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
  /apollo/tasks/bulk_create:
    post:
      summary: Bulk Create Tasks
      description: Bulk create tasks. Requires a master API key.
      operationId: post_apollo_tasks_bulk_create
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
                contact_ids:
                  type: array
                  items:
                    type: string
                  description: Contact IDs.
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
                - contact_ids
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
                  tasks:
                    type: array
                    items:
                      type: string
                    description: Created tasks (when returned).
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