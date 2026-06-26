> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Thread

> Updates thread labels



## OpenAPI

````yaml openapi/agentmail.json PATCH /agentmail/inboxes/{inbox_id}/threads/{thread_id}
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
  /agentmail/inboxes/{inbox_id}/threads/{thread_id}:
    patch:
      tags:
        - subpackage_inboxes.subpackage_inboxes/threads
      summary: Update Thread
      description: >-
        Updates thread labels. Cannot add or remove system labels (sent,
        received, bounced, etc.). Rejects requests with a `422` for threads with
        100 or more messages.
      operationId: update
      parameters:
        - name: inbox_id
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_inboxes_InboxId'
        - name: thread_id
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_threads_ThreadId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_threads_UpdateThreadRequest'
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_threads_UpdateThreadResponse'
        '400':
          description: Error response with status 400
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type__ValidationErrorResponse'
        '404':
          description: Error response with status 404
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type__ErrorResponse'
        '422':
          description: Error response with status 422
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type__ErrorResponse'
components:
  schemas:
    type_inboxes_InboxId:
      type: string
      description: The ID of the inbox.
      title: InboxId
    type_threads_ThreadId:
      type: string
      description: ID of thread.
      title: ThreadId
    type_threads_UpdateThreadRequest:
      type: object
      properties:
        add_labels:
          type: array
          items:
            type: string
          description: Labels to add to thread. Cannot be system labels.
        remove_labels:
          type: array
          items:
            type: string
          description: >-
            Labels to remove from thread. Cannot be system labels. Takes
            priority over `add_labels` (in the event of duplicate labels passed
            in).
      title: UpdateThreadRequest
    type_threads_UpdateThreadResponse:
      type: object
      properties:
        thread_id:
          $ref: '#/components/schemas/type_threads_ThreadId'
        labels:
          $ref: '#/components/schemas/type_threads_ThreadLabels'
      required:
        - thread_id
        - labels
      title: UpdateThreadResponse
    type__ValidationErrorResponse:
      type: object
      properties:
        name:
          $ref: '#/components/schemas/type__ErrorName'
        errors:
          description: Validation errors.
      required:
        - name
        - errors
      title: ValidationErrorResponse
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
    type_threads_ThreadLabels:
      type: array
      items:
        type: string
      description: Labels of thread.
      title: ThreadLabels
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