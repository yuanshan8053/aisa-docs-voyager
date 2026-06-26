> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Threads

> List Threads



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/inboxes/{inbox_id}/threads
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
  /agentmail/inboxes/{inbox_id}/threads:
    get:
      tags:
        - subpackage_inboxes.subpackage_inboxes/threads
      summary: List Threads
      description: |-
        **CLI:**
        ```bash
        agentmail inboxes:threads list --inbox-id <inbox_id>
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
                $ref: '#/components/schemas/type_threads_ListThreadsResponse'
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
    type_threads_ListThreadsResponse:
      type: object
      properties:
        count:
          $ref: '#/components/schemas/type__Count'
        limit:
          $ref: '#/components/schemas/type__Limit'
        next_page_token:
          $ref: '#/components/schemas/type__PageToken'
        threads:
          type: array
          items:
            $ref: '#/components/schemas/type_threads_ThreadItem'
          description: Ordered by `timestamp` descending.
      required:
        - count
        - threads
      title: ListThreadsResponse
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
    type_threads_ThreadItem:
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
      title: ThreadItem
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