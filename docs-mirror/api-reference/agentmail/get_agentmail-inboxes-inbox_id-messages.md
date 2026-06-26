> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Messages

> List Messages



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/inboxes/{inbox_id}/messages
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
  /agentmail/inboxes/{inbox_id}/messages:
    get:
      tags:
        - subpackage_inboxes.subpackage_inboxes/messages
      summary: List Messages
      description: |-
        **CLI:**
        ```bash
        agentmail inboxes:messages list --inbox-id <inbox_id>
        ```
      operationId: list
      parameters:
        - name: inbox_id
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_inboxes_InboxId'
        - name: limit
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type__Limit'
        - name: page_token
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type__PageToken'
        - name: labels
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type__Labels'
        - name: before
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type__Before'
        - name: after
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type__After'
        - name: ascending
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type__Ascending'
        - name: include_spam
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type__IncludeSpam'
        - name: include_blocked
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type__IncludeBlocked'
        - name: include_unauthenticated
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type__IncludeUnauthenticated'
        - name: include_trash
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type__IncludeTrash'
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
                $ref: '#/components/schemas/type_messages_ListMessagesResponse'
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
    type__Limit:
      type: integer
      description: Limit of number of items returned.
      title: Limit
    type__PageToken:
      type: string
      description: Page token for pagination.
      title: PageToken
    type__Labels:
      type: array
      items:
        type: string
      description: Labels to filter by.
      title: Labels
    type__Before:
      type: string
      format: date-time
      description: Timestamp before which to filter by.
      title: Before
    type__After:
      type: string
      format: date-time
      description: Timestamp after which to filter by.
      title: After
    type__Ascending:
      type: boolean
      description: Sort in ascending temporal order.
      title: Ascending
    type__IncludeSpam:
      type: boolean
      description: Include spam in results.
      title: IncludeSpam
    type__IncludeBlocked:
      type: boolean
      description: Include blocked in results.
      title: IncludeBlocked
    type__IncludeUnauthenticated:
      type: boolean
      description: Include unauthenticated in results.
      title: IncludeUnauthenticated
    type__IncludeTrash:
      type: boolean
      description: Include trash in results.
      title: IncludeTrash
    type_messages_ListMessagesResponse:
      type: object
      properties:
        count:
          $ref: '#/components/schemas/type__Count'
        limit:
          $ref: '#/components/schemas/type__Limit'
        next_page_token:
          $ref: '#/components/schemas/type__PageToken'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/type_messages_MessageItem'
          description: Ordered by `timestamp` descending.
      required:
        - count
        - messages
      title: ListMessagesResponse
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
    type__Count:
      type: integer
      description: Number of items returned.
      title: Count
    type_messages_MessageItem:
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
      title: MessageItem
    type__ErrorName:
      type: string
      description: Name of error.
      title: ErrorName
    type__ErrorMessage:
      type: string
      description: Error message.
      title: ErrorMessage
    type_threads_ThreadId:
      type: string
      description: ID of thread.
      title: ThreadId
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