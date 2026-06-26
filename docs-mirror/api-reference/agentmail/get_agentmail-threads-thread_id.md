> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Thread

> Get Thread



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/threads/{thread_id}
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
    get:
      tags:
        - subpackage_threads
      summary: Get Thread
      description: |-
        **CLI:**
        ```bash
        agentmail threads get --thread-id <thread_id>
        ```
      operationId: get
      parameters:
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
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_threads_Thread'
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
    type_threads_Thread:
      type: object
      properties:
        inbox_id:
          $ref: '#/components/schemas/type_inboxes_InboxId'
        thread_id:
          $ref: '#/components/schemas/type_threads_ThreadId'
        labels:
          $ref: '#/components/schemas/type_threads_ThreadLabels'
        timestamp:
          $ref: '#/components/schemas/type_threads_ThreadTimestamp'
        received_timestamp:
          $ref: '#/components/schemas/type_threads_ThreadReceivedTimestamp'
        sent_timestamp:
          $ref: '#/components/schemas/type_threads_ThreadSentTimestamp'
        senders:
          $ref: '#/components/schemas/type_threads_ThreadSenders'
        recipients:
          $ref: '#/components/schemas/type_threads_ThreadRecipients'
        subject:
          $ref: '#/components/schemas/type_threads_ThreadSubject'
        preview:
          $ref: '#/components/schemas/type_threads_ThreadPreview'
        attachments:
          $ref: '#/components/schemas/type_threads_ThreadAttachments'
        last_message_id:
          $ref: '#/components/schemas/type_threads_ThreadLastMessageId'
        message_count:
          $ref: '#/components/schemas/type_threads_ThreadMessageCount'
        size:
          $ref: '#/components/schemas/type_threads_ThreadSize'
        updated_at:
          $ref: '#/components/schemas/type_threads_ThreadUpdatedAt'
        created_at:
          $ref: '#/components/schemas/type_threads_ThreadCreatedAt'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/type_messages_Message'
          description: Messages in thread. Ordered by `timestamp` ascending.
      required:
        - inbox_id
        - thread_id
        - labels
        - timestamp
        - senders
        - recipients
        - last_message_id
        - message_count
        - size
        - updated_at
        - created_at
        - messages
      title: Thread
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
    type_inboxes_InboxId:
      type: string
      description: The ID of the inbox.
      title: InboxId
    type_threads_ThreadLabels:
      type: array
      items:
        type: string
      description: Labels of thread.
      title: ThreadLabels
    type_threads_ThreadTimestamp:
      type: string
      format: date-time
      description: Timestamp of last sent or received message.
      title: ThreadTimestamp
    type_threads_ThreadReceivedTimestamp:
      type: string
      format: date-time
      description: Timestamp of last received message.
      title: ThreadReceivedTimestamp
    type_threads_ThreadSentTimestamp:
      type: string
      format: date-time
      description: Timestamp of last sent message.
      title: ThreadSentTimestamp
    type_threads_ThreadSenders:
      type: array
      items:
        type: string
      description: >-
        Senders in thread. In format `username@domain.com` or `Display Name
        <username@domain.com>`.
      title: ThreadSenders
    type_threads_ThreadRecipients:
      type: array
      items:
        type: string
      description: >-
        Recipients in thread. In format `username@domain.com` or `Display Name
        <username@domain.com>`.
      title: ThreadRecipients
    type_threads_ThreadSubject:
      type: string
      description: Subject of thread.
      title: ThreadSubject
    type_threads_ThreadPreview:
      type: string
      description: Text preview of last message in thread.
      title: ThreadPreview
    type_threads_ThreadAttachments:
      type: array
      items:
        $ref: '#/components/schemas/type_attachments_Attachment'
      description: Attachments in thread.
      title: ThreadAttachments
    type_threads_ThreadLastMessageId:
      type: string
      description: ID of last message in thread.
      title: ThreadLastMessageId
    type_threads_ThreadMessageCount:
      type: integer
      description: Number of messages in thread.
      title: ThreadMessageCount
    type_threads_ThreadSize:
      type: integer
      description: Size of thread in bytes.
      title: ThreadSize
    type_threads_ThreadUpdatedAt:
      type: string
      format: date-time
      description: Time at which thread was last updated.
      title: ThreadUpdatedAt
    type_threads_ThreadCreatedAt:
      type: string
      format: date-time
      description: Time at which thread was created.
      title: ThreadCreatedAt
    type_messages_Message:
      type: object
      properties:
        inbox_id:
          $ref: '#/components/schemas/type_inboxes_InboxId'
        thread_id:
          $ref: '#/components/schemas/type_threads_ThreadId'
        message_id:
          $ref: '#/components/schemas/type_messages_MessageId'
        labels:
          $ref: '#/components/schemas/type_messages_MessageLabels'
        timestamp:
          $ref: '#/components/schemas/type_messages_MessageTimestamp'
        from:
          $ref: '#/components/schemas/type_messages_MessageFrom'
        reply_to:
          type: array
          items:
            type: string
          description: >-
            Reply-to addresses. In format `username@domain.com` or `Display Name
            <username@domain.com>`.
        to:
          $ref: '#/components/schemas/type_messages_MessageTo'
        cc:
          $ref: '#/components/schemas/type_messages_MessageCc'
        bcc:
          $ref: '#/components/schemas/type_messages_MessageBcc'
        subject:
          $ref: '#/components/schemas/type_messages_MessageSubject'
        preview:
          $ref: '#/components/schemas/type_messages_MessagePreview'
        text:
          $ref: '#/components/schemas/type_messages_MessageText'
        html:
          $ref: '#/components/schemas/type_messages_MessageHtml'
        extracted_text:
          type: string
          description: Extracted new text content.
        extracted_html:
          type: string
          description: Extracted new HTML content.
        attachments:
          $ref: '#/components/schemas/type_messages_MessageAttachments'
        in_reply_to:
          $ref: '#/components/schemas/type_messages_MessageInReplyTo'
        references:
          $ref: '#/components/schemas/type_messages_MessageReferences'
        headers:
          $ref: '#/components/schemas/type_messages_MessageHeaders'
        size:
          $ref: '#/components/schemas/type_messages_MessageSize'
        updated_at:
          $ref: '#/components/schemas/type_messages_MessageUpdatedAt'
        created_at:
          $ref: '#/components/schemas/type_messages_MessageCreatedAt'
      required:
        - inbox_id
        - thread_id
        - message_id
        - labels
        - timestamp
        - from
        - to
        - size
        - updated_at
        - created_at
      title: Message
    type__ErrorName:
      type: string
      description: Name of error.
      title: ErrorName
    type__ErrorMessage:
      type: string
      description: Error message.
      title: ErrorMessage
    type_attachments_Attachment:
      type: object
      properties:
        attachment_id:
          $ref: '#/components/schemas/type_attachments_AttachmentId'
        filename:
          $ref: '#/components/schemas/type_attachments_AttachmentFilename'
        size:
          $ref: '#/components/schemas/type_attachments_AttachmentSize'
        content_type:
          $ref: '#/components/schemas/type_attachments_AttachmentContentType'
        content_disposition:
          $ref: '#/components/schemas/type_attachments_AttachmentContentDisposition'
        content_id:
          $ref: '#/components/schemas/type_attachments_AttachmentContentId'
      required:
        - attachment_id
        - size
      title: Attachment
    type_messages_MessageId:
      type: string
      description: ID of message.
      title: MessageId
    type_messages_MessageLabels:
      type: array
      items:
        type: string
      description: Labels of message.
      title: MessageLabels
    type_messages_MessageTimestamp:
      type: string
      format: date-time
      description: Time at which message was sent or drafted.
      title: MessageTimestamp
    type_messages_MessageFrom:
      type: string
      description: >-
        Address of sender. In format `username@domain.com` or `Display Name
        <username@domain.com>`.
      title: MessageFrom
    type_messages_MessageTo:
      type: array
      items:
        type: string
      description: >-
        Addresses of recipients. In format `username@domain.com` or `Display
        Name <username@domain.com>`.
      title: MessageTo
    type_messages_MessageCc:
      type: array
      items:
        type: string
      description: >-
        Addresses of CC recipients. In format `username@domain.com` or `Display
        Name <username@domain.com>`.
      title: MessageCc
    type_messages_MessageBcc:
      type: array
      items:
        type: string
      description: >-
        Addresses of BCC recipients. In format `username@domain.com` or `Display
        Name <username@domain.com>`.
      title: MessageBcc
    type_messages_MessageSubject:
      type: string
      description: Subject of message.
      title: MessageSubject
    type_messages_MessagePreview:
      type: string
      description: Text preview of message.
      title: MessagePreview
    type_messages_MessageText:
      type: string
      description: Plain text body of message.
      title: MessageText
    type_messages_MessageHtml:
      type: string
      description: HTML body of message.
      title: MessageHtml
    type_messages_MessageAttachments:
      type: array
      items:
        $ref: '#/components/schemas/type_attachments_Attachment'
      description: Attachments in message.
      title: MessageAttachments
    type_messages_MessageInReplyTo:
      type: string
      description: ID of message being replied to.
      title: MessageInReplyTo
    type_messages_MessageReferences:
      type: array
      items:
        type: string
      description: IDs of previous messages in thread.
      title: MessageReferences
    type_messages_MessageHeaders:
      type: object
      additionalProperties:
        type: string
      description: Headers in message.
      title: MessageHeaders
    type_messages_MessageSize:
      type: integer
      description: Size of message in bytes.
      title: MessageSize
    type_messages_MessageUpdatedAt:
      type: string
      format: date-time
      description: Time at which message was last updated.
      title: MessageUpdatedAt
    type_messages_MessageCreatedAt:
      type: string
      format: date-time
      description: Time at which message was created.
      title: MessageCreatedAt
    type_attachments_AttachmentId:
      type: string
      description: ID of attachment.
      title: AttachmentId
    type_attachments_AttachmentFilename:
      type: string
      description: Filename of attachment.
      title: AttachmentFilename
    type_attachments_AttachmentSize:
      type: integer
      description: Size of attachment in bytes.
      title: AttachmentSize
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