> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Raw Message

> Get Raw Message



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/inboxes/{inbox_id}/messages/{message_id}/raw
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
  /agentmail/inboxes/{inbox_id}/messages/{message_id}/raw:
    get:
      tags:
        - subpackage_inboxes.subpackage_inboxes/messages
      summary: Get Raw Message
      description: >-
        **CLI:**

        ```bash

        agentmail inboxes:messages get-raw --inbox-id <inbox_id> --message-id
        <message_id>

        ```
      operationId: get-raw
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
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_messages_RawMessageResponse'
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
    type_messages_RawMessageResponse:
      type: object
      properties:
        message_id:
          $ref: '#/components/schemas/type_messages_MessageId'
          description: ID of the message.
        size:
          $ref: '#/components/schemas/type_messages_MessageSize'
          description: Size of the raw message in bytes.
        download_url:
          type: string
          description: S3 presigned URL to download the raw message. Expires at expires_at.
        expires_at:
          type: string
          format: date-time
          description: Time at which the download URL expires.
      required:
        - message_id
        - size
        - download_url
        - expires_at
      description: S3 presigned URL to download the raw .eml file.
      title: RawMessageResponse
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
    type_messages_MessageSize:
      type: integer
      description: Size of message in bytes.
      title: MessageSize
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