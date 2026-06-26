> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Draft

> Send Draft



## OpenAPI

````yaml openapi/agentmail.json POST /agentmail/inboxes/{inbox_id}/drafts/{draft_id}/send
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
  /agentmail/inboxes/{inbox_id}/drafts/{draft_id}/send:
    post:
      tags:
        - subpackage_inboxes.subpackage_inboxes/drafts
      summary: Send Draft
      description: >-
        **CLI:**

        ```bash

        agentmail inboxes:drafts send --inbox-id <inbox_id> --draft-id
        <draft_id>

        ```
      operationId: send
      parameters:
        - name: inbox_id
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_inboxes_InboxId'
        - name: draft_id
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_drafts_DraftId'
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
              $ref: '#/components/schemas/type_messages_UpdateMessageRequest'
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_messages_SendMessageResponse'
        '400':
          description: Error response with status 400
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type__ValidationErrorResponse'
        '403':
          description: Error response with status 403
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type__ErrorResponse'
        '404':
          description: Error response with status 404
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
    type_drafts_DraftId:
      type: string
      description: ID of draft.
      title: DraftId
    type_messages_UpdateMessageRequest:
      type: object
      properties:
        add_labels:
          $ref: '#/components/schemas/type_messages_UpdateMessageLabels'
          description: Label or labels to add to message.
        remove_labels:
          $ref: '#/components/schemas/type_messages_UpdateMessageLabels'
          description: Label or labels to remove from message.
      title: UpdateMessageRequest
    type_messages_SendMessageResponse:
      type: object
      properties:
        message_id:
          $ref: '#/components/schemas/type_messages_MessageId'
        thread_id:
          $ref: '#/components/schemas/type_threads_ThreadId'
      required:
        - message_id
        - thread_id
      title: SendMessageResponse
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
    type_messages_UpdateMessageLabels:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      description: Label or list of labels.
      title: UpdateMessageLabels
    type_messages_MessageId:
      type: string
      description: ID of message.
      title: MessageId
    type_threads_ThreadId:
      type: string
      description: ID of thread.
      title: ThreadId
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