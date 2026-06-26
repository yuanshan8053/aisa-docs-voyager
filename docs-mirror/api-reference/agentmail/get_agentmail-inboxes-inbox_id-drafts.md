> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Drafts

> List Drafts



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/inboxes/{inbox_id}/drafts
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
  /agentmail/inboxes/{inbox_id}/drafts:
    get:
      tags:
        - subpackage_inboxes.subpackage_inboxes/drafts
      summary: List Drafts
      description: |-
        **CLI:**
        ```bash
        agentmail inboxes:drafts list --inbox-id <inbox_id>
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
                $ref: '#/components/schemas/type_drafts_ListDraftsResponse'
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
    type_drafts_ListDraftsResponse:
      type: object
      properties:
        count:
          $ref: '#/components/schemas/type__Count'
        limit:
          $ref: '#/components/schemas/type__Limit'
        next_page_token:
          $ref: '#/components/schemas/type__PageToken'
        drafts:
          type: array
          items:
            $ref: '#/components/schemas/type_drafts_DraftItem'
          description: Ordered by `updated_at` descending.
      required:
        - count
        - drafts
      title: ListDraftsResponse
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
    type_drafts_DraftItem:
      type: object
      properties:
        inbox_id:
          $ref: '#/components/schemas/type_inboxes_InboxId'
        draft_id:
          $ref: '#/components/schemas/type_drafts_DraftId'
        labels:
          $ref: '#/components/schemas/type_drafts_DraftLabels'
        to:
          $ref: '#/components/schemas/type_drafts_DraftTo'
        cc:
          $ref: '#/components/schemas/type_drafts_DraftCc'
        bcc:
          $ref: '#/components/schemas/type_drafts_DraftBcc'
        subject:
          $ref: '#/components/schemas/type_drafts_DraftSubject'
        preview:
          $ref: '#/components/schemas/type_drafts_DraftPreview'
        attachments:
          $ref: '#/components/schemas/type_drafts_DraftAttachments'
        in_reply_to:
          $ref: '#/components/schemas/type_drafts_DraftInReplyTo'
        send_status:
          $ref: '#/components/schemas/type_drafts_DraftSendStatus'
        send_at:
          $ref: '#/components/schemas/type_drafts_DraftSendAt'
        updated_at:
          $ref: '#/components/schemas/type_drafts_DraftUpdatedAt'
      required:
        - inbox_id
        - draft_id
        - labels
        - updated_at
      title: DraftItem
    type__ErrorName:
      type: string
      description: Name of error.
      title: ErrorName
    type__ErrorMessage:
      type: string
      description: Error message.
      title: ErrorMessage
    type_drafts_DraftId:
      type: string
      description: ID of draft.
      title: DraftId
    type_drafts_DraftLabels:
      type: array
      items:
        type: string
      description: Labels of draft.
      title: DraftLabels
    type_drafts_DraftTo:
      type: array
      items:
        type: string
      description: >-
        Addresses of recipients. In format `username@domain.com` or `Display
        Name <username@domain.com>`.
      title: DraftTo
    type_drafts_DraftCc:
      type: array
      items:
        type: string
      description: >-
        Addresses of CC recipients. In format `username@domain.com` or `Display
        Name <username@domain.com>`.
      title: DraftCc
    type_drafts_DraftBcc:
      type: array
      items:
        type: string
      description: >-
        Addresses of BCC recipients. In format `username@domain.com` or `Display
        Name <username@domain.com>`.
      title: DraftBcc
    type_drafts_DraftSubject:
      type: string
      description: Subject of draft.
      title: DraftSubject
    type_drafts_DraftPreview:
      type: string
      description: Text preview of draft.
      title: DraftPreview
    type_drafts_DraftAttachments:
      type: array
      items:
        $ref: '#/components/schemas/type_attachments_Attachment'
      description: Attachments in draft.
      title: DraftAttachments
    type_drafts_DraftInReplyTo:
      type: string
      description: ID of message being replied to.
      title: DraftInReplyTo
    type_drafts_DraftSendStatus:
      type: string
      enum:
        - scheduled
        - sending
        - failed
      description: Schedule send status of draft.
      title: DraftSendStatus
    type_drafts_DraftSendAt:
      type: string
      format: date-time
      description: Time at which to schedule send draft.
      title: DraftSendAt
    type_drafts_DraftUpdatedAt:
      type: string
      format: date-time
      description: Time at which draft was last updated.
      title: DraftUpdatedAt
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