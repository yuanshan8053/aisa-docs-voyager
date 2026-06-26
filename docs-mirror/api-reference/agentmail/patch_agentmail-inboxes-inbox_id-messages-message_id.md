> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Message

> Update Message



## OpenAPI

````yaml openapi/agentmail.json PATCH /agentmail/inboxes/{inbox_id}/messages/{message_id}
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
  /agentmail/inboxes/{inbox_id}/messages/{message_id}:
    patch:
      tags:
        - subpackage_inboxes.subpackage_inboxes/messages
      summary: Update Message
      description: >-
        **CLI:**

        ```bash

        agentmail inboxes:messages update --inbox-id <inbox_id> --message-id
        <message_id> --add-label read --remove-label unread

        ```
      operationId: update
      parameters:
        - name: inbox_id
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_inboxes_InboxId'
        - name: message_id
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_messages_MessageId'
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
                $ref: '#/components/schemas/type_messages_UpdateMessageResponse'
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
components:
  schemas:
    type_inboxes_InboxId:
      type: string
      description: The ID of the inbox.
      title: InboxId
    type_messages_MessageId:
      type: string
      description: ID of message.
      title: MessageId
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
    type_messages_UpdateMessageResponse:
      type: object
      properties:
        message_id:
          $ref: '#/components/schemas/type_messages_MessageId'
        labels:
          $ref: '#/components/schemas/type_messages_MessageLabels'
      required:
        - message_id
        - labels
      title: UpdateMessageResponse
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
    type_messages_MessageLabels:
      type: array
      items:
        type: string
      description: Labels of message.
      title: MessageLabels
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