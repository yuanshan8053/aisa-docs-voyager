> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Thread

> Moves the thread to trash by adding a trash label to all messages



## OpenAPI

````yaml openapi/agentmail.json DELETE /agentmail/threads/{thread_id}
openapi: 3.1.0
info:
  title: AgentMail API
  version: 1.0.0
  description: >-
    AgentMail email API endpoints exposed through the AIsa unified gateway.
    Adapted from the upstream docs.agentmail.to OpenAPI spec.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - Bearer: []
paths:
  /agentmail/threads/{thread_id}:
    delete:
      tags:
        - subpackage_threads
      summary: Delete Thread
      description: >-
        Moves the thread to trash by adding a trash label to all messages. If
        the thread is already in trash, it will be permanently deleted. Use
        `permanent=true` to force permanent deletion.


        **CLI:**

        ```bash

        agentmail threads delete --thread-id <thread_id>

        ```
      operationId: delete
      parameters:
        - name: thread_id
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_threads_ThreadId'
        - name: permanent
          in: query
          description: If true, permanently delete the thread instead of moving to trash.
          required: false
          schema:
            type: boolean
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
        '404':
          description: Error response with status 404
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type__ErrorResponse'
components:
  schemas:
    type_threads_ThreadId:
      type: string
      description: ID of thread.
      title: ThreadId
    type__ErrorResponse:
      type: object
      properties:
        name:
          $ref: '#/components/schemas/type__ErrorName'
        message:
          $ref: '#/components/schemas/type__ErrorMessage'
      required:
        - name
        - message
      title: ErrorResponse
    type__ErrorName:
      type: string
      description: Name of error.
      title: ErrorName
    type__ErrorMessage:
      type: string
      description: Error message.
      title: ErrorMessage
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer

````