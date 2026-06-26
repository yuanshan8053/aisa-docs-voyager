> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Reply To Message

> Reply To Message



## OpenAPI

````yaml openapi/agentmail.json POST /agentmail/inboxes/{inbox_id}/messages/{message_id}/reply
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
  /agentmail/inboxes/{inbox_id}/messages/{message_id}/reply:
    post:
      tags:
        - subpackage_inboxes.subpackage_inboxes/messages
      summary: Reply To Message
      description: >-
        **CLI:**

        ```bash

        agentmail inboxes:messages reply --inbox-id <inbox_id> --message-id
        <message_id> --text "Reply text"

        ```
      operationId: reply
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
              $ref: '#/components/schemas/type_messages_ReplyToMessageRequest'
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
    type_messages_MessageId:
      type: string
      description: ID of message.
      title: MessageId
    type_messages_ReplyToMessageRequest:
      type: object
      properties:
        labels:
          $ref: '#/components/schemas/type_messages_MessageLabels'
        reply_to:
          $ref: '#/components/schemas/type_messages_SendMessageReplyTo'
        to:
          $ref: '#/components/schemas/type_messages_SendMessageTo'
        cc:
          $ref: '#/components/schemas/type_messages_SendMessageCc'
        bcc:
          $ref: '#/components/schemas/type_messages_SendMessageBcc'
        reply_all:
          $ref: '#/components/schemas/type_messages_ReplyAll'
        text:
          $ref: '#/components/schemas/type_messages_MessageText'
        html:
          $ref: '#/components/schemas/type_messages_MessageHtml'
        attachments:
          $ref: '#/components/schemas/type_messages_SendMessageAttachments'
        headers:
          $ref: '#/components/schemas/type_messages_SendMessageHeaders'
      title: ReplyToMessageRequest
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
    type_messages_MessageLabels:
      type: array
      items:
        type: string
      description: Labels of message.
      title: MessageLabels
    type_messages_SendMessageReplyTo:
      $ref: '#/components/schemas/type_messages_Addresses'
      description: Reply-to address or addresses.
      title: SendMessageReplyTo
    type_messages_SendMessageTo:
      $ref: '#/components/schemas/type_messages_Addresses'
      description: Recipient address or addresses.
      title: SendMessageTo
    type_messages_SendMessageCc:
      $ref: '#/components/schemas/type_messages_Addresses'
      description: CC recipient address or addresses.
      title: SendMessageCc
    type_messages_SendMessageBcc:
      $ref: '#/components/schemas/type_messages_Addresses'
      description: BCC recipient address or addresses.
      title: SendMessageBcc
    type_messages_ReplyAll:
      type: boolean
      description: Reply to all recipients of the original message.
      title: ReplyAll
    type_messages_MessageText:
      type: string
      description: Plain text body of message.
      title: MessageText
    type_messages_MessageHtml:
      type: string
      description: HTML body of message.
      title: MessageHtml
    type_messages_SendMessageAttachments:
      type: array
      items:
        $ref: '#/components/schemas/type_attachments_SendAttachment'
      description: Attachments to include in message.
      title: SendMessageAttachments
    type_messages_SendMessageHeaders:
      type: object
      additionalProperties:
        type: string
      description: Headers to include in message.
      title: SendMessageHeaders
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
    type_messages_Addresses:
      oneOf:
        - type: string
        - type: array
          items:
            type: string
      title: Addresses
    type_attachments_SendAttachment:
      type: object
      properties:
        filename:
          $ref: '#/components/schemas/type_attachments_AttachmentFilename'
        content_type:
          $ref: '#/components/schemas/type_attachments_AttachmentContentType'
        content_disposition:
          $ref: '#/components/schemas/type_attachments_AttachmentContentDisposition'
        content_id:
          $ref: '#/components/schemas/type_attachments_AttachmentContentId'
        content:
          type: string
          description: Base64 encoded content of attachment.
        url:
          type: string
          description: URL to the attachment.
      title: SendAttachment
    type_attachments_AttachmentFilename:
      type: string
      description: Filename of attachment.
      title: AttachmentFilename
    type_attachments_AttachmentContentType:
      type: string
      description: Content type of attachment.
      title: AttachmentContentType
    type_attachments_AttachmentContentDisposition:
      type: string
      enum:
        - inline
        - attachment
      description: Content disposition of attachment.
      title: AttachmentContentDisposition
    type_attachments_AttachmentContentId:
      type: string
      description: Content ID of attachment.
      title: AttachmentContentId
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer

````