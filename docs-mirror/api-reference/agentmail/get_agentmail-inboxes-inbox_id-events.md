> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Inbox Events

> List label change events for an inbox



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/inboxes/{inbox_id}/events
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
  /agentmail/inboxes/{inbox_id}/events:
    get:
      tags:
        - subpackage_inboxes.subpackage_inboxes/events
      summary: List Inbox Events
      description: >-
        List label change events for an inbox. Returns events in reverse
        chronological order by default. Use for IMAP UID projection or audit
        logging.


        **CLI:**

        ```bash

        agentmail inboxes:events list --inbox-id <inbox_id>

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
                $ref: '#/components/schemas/type_inbox-events_ListInboxEventsResponse'
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
    type__Ascending:
      type: boolean
      description: Sort in ascending temporal order.
      title: Ascending
    type_inbox-events_ListInboxEventsResponse:
      type: object
      properties:
        count:
          $ref: '#/components/schemas/type__Count'
        limit:
          $ref: '#/components/schemas/type__Limit'
        next_page_token:
          $ref: '#/components/schemas/type__PageToken'
        events:
          type: array
          items:
            $ref: '#/components/schemas/type_inbox-events_InboxEvent'
          description: Ordered by `event_id` descending.
      required:
        - count
        - events
      title: ListInboxEventsResponse
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
    type_inbox-events_InboxEvent:
      type: object
      properties:
        organization_id:
          $ref: '#/components/schemas/type__OrganizationId'
        pod_id:
          type: string
          description: ID of pod.
        inbox_id:
          $ref: '#/components/schemas/type_inboxes_InboxId'
        event_id:
          $ref: '#/components/schemas/type_inbox-events_InboxEventId'
        event_type:
          $ref: '#/components/schemas/type_inbox-events_InboxEventType'
        message_id:
          type: string
          description: ID of message.
        label:
          type: string
          description: Label added or removed.
        event_at:
          type: string
          format: date-time
          description: Time at which the event occurred.
        created_at:
          type: string
          format: date-time
          description: Time at which the event was recorded.
      required:
        - organization_id
        - pod_id
        - inbox_id
        - event_id
        - event_type
        - message_id
        - label
        - event_at
        - created_at
      title: InboxEvent
    type__ErrorName:
      type: string
      description: Name of error.
      title: ErrorName
    type__ErrorMessage:
      type: string
      description: Error message.
      title: ErrorMessage
    type__OrganizationId:
      type: string
      description: ID of organization.
      title: OrganizationId
    type_inbox-events_InboxEventId:
      type: string
      description: ID of event.
      title: InboxEventId
    type_inbox-events_InboxEventType:
      type: string
      enum:
        - label.added
        - label.removed
      description: |-
        Type of inbox event. Wire format is dot.case to match the
        convention used by webhook events (`message.received`,
        `domain.verified`, etc. in events.yml). Pre-2026-04 these were
        `label_added`/`label_removed` (snake_case). The Fern enum's `name`
        field stays uppercase-snake (Fern convention); only the wire
        `value` changed.
      title: InboxEventType
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer

````