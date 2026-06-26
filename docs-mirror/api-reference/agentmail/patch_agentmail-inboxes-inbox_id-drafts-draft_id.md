> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Draft

> Update Draft



## OpenAPI

````yaml openapi/agentmail.json PATCH /agentmail/inboxes/{inbox_id}/drafts/{draft_id}
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
  /agentmail/inboxes/{inbox_id}/drafts/{draft_id}:
    patch:
      tags:
        - subpackage_inboxes.subpackage_inboxes/drafts
      summary: Update Draft
      description: >-
        **CLI:**

        ```bash

        agentmail inboxes:drafts update --inbox-id <inbox_id> --draft-id
        <draft_id> --subject "Updated subject"

        ```
      operationId: update
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
              $ref: '#/components/schemas/type_drafts_UpdateDraftRequest'
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_drafts_Draft'
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
    type_drafts_UpdateDraftRequest:
      type: object
      properties:
        reply_to:
          $ref: '#/components/schemas/type_drafts_DraftReplyTo'
        to:
          $ref: '#/components/schemas/type_drafts_DraftTo'
        cc:
          $ref: '#/components/schemas/type_drafts_DraftCc'
        bcc:
          $ref: '#/components/schemas/type_drafts_DraftBcc'
        subject:
          $ref: '#/components/schemas/type_drafts_DraftSubject'
        text:
          $ref: '#/components/schemas/type_drafts_DraftText'
        html:
          $ref: '#/components/schemas/type_drafts_DraftHtml'
        send_at:
          $ref: '#/components/schemas/type_drafts_DraftSendAt'
      title: UpdateDraftRequest
    type_drafts_Draft:
      type: object
      properties:
        inbox_id:
          $ref: '#/components/schemas/type_inboxes_InboxId'
        draft_id:
          $ref: '#/components/schemas/type_drafts_DraftId'
        client_id:
          $ref: '#/components/schemas/type_drafts_DraftClientId'
        labels:
          $ref: '#/components/schemas/type_drafts_DraftLabels'
        reply_to:
          $ref: '#/components/schemas/type_drafts_DraftReplyTo'
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
        text:
          $ref: '#/components/schemas/type_drafts_DraftText'
        html:
          $ref: '#/components/schemas/type_drafts_DraftHtml'
        attachments:
          $ref: '#/components/schemas/type_drafts_DraftAttachments'
        in_reply_to:
          $ref: '#/components/schemas/type_drafts_DraftInReplyTo'
        references:
          type: array
          items:
            type: string
          description: IDs of previous messages in thread.
        send_status:
          $ref: '#/components/schemas/type_drafts_DraftSendStatus'
        send_at:
          $ref: '#/components/schemas/type_drafts_DraftSendAt'
        updated_at:
          $ref: '#/components/schemas/type_drafts_DraftUpdatedAt'
        created_at:
          type: string
          format: date-time
          description: Time at which draft was created.
      required:
        - inbox_id
        - draft_id
        - labels
        - updated_at
        - created_at
      title: Draft
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
    type_drafts_DraftReplyTo:
      type: array
      items:
        type: string
      description: >-
        Reply-to addresses. In format `username@domain.com` or `Display Name
        <username@domain.com>`.
      title: DraftReplyTo
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
    type_drafts_DraftText:
      type: string
      description: Plain text body of draft.
      title: DraftText
    type_drafts_DraftHtml:
      type: string
      description: HTML body of draft.
      title: DraftHtml
    type_drafts_DraftSendAt:
      type: string
      format: date-time
      description: Time at which to schedule send draft.
      title: DraftSendAt
    type_drafts_DraftClientId:
      type: string
      description: Client ID of draft.
      title: DraftClientId
    type_drafts_DraftLabels:
      type: array
      items:
        type: string
      description: Labels of draft.
      title: DraftLabels
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
    type_drafts_DraftUpdatedAt:
      type: string
      format: date-time
      description: Time at which draft was last updated.
      title: DraftUpdatedAt
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