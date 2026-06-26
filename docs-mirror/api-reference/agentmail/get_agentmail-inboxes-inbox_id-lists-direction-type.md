> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Entries

> List Entries



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/inboxes/{inbox_id}/lists/{direction}/{type}
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
  /agentmail/inboxes/{inbox_id}/lists/{direction}/{type}:
    get:
      tags:
        - subpackage_inboxes.subpackage_inboxes/lists
      summary: List Entries
      description: >-
        **CLI:**

        ```bash

        agentmail inboxes:lists list --inbox-id <inbox_id> --direction
        <direction> --type <type>

        ```
      operationId: list
      parameters:
        - name: inbox_id
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_inboxes_InboxId'
        - name: direction
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_lists_Direction'
        - name: type
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_lists_ListType'
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
                $ref: '#/components/schemas/type_lists_PodListListEntriesResponse'
components:
  schemas:
    type_inboxes_InboxId:
      type: string
      description: The ID of the inbox.
      title: InboxId
    type_lists_Direction:
      type: string
      enum:
        - send
        - receive
        - reply
      description: Direction of list entry.
      title: Direction
    type_lists_ListType:
      type: string
      enum:
        - allow
        - block
      description: Type of list entry.
      title: ListType
    type__Limit:
      type: integer
      description: Limit of number of items returned.
      title: Limit
    type__PageToken:
      type: string
      description: Page token for pagination.
      title: PageToken
    type_lists_PodListListEntriesResponse:
      type: object
      properties:
        count:
          $ref: '#/components/schemas/type__Count'
        limit:
          $ref: '#/components/schemas/type__Limit'
        next_page_token:
          $ref: '#/components/schemas/type__PageToken'
        entries:
          type: array
          items:
            $ref: '#/components/schemas/type_lists_PodListEntry'
          description: Ordered by entry ascending.
      required:
        - count
        - entries
      title: PodListListEntriesResponse
    type__Count:
      type: integer
      description: Number of items returned.
      title: Count
    type_lists_PodListEntry:
      type: object
      properties:
        entry:
          type: string
          description: Email address or domain of list entry.
        organization_id:
          $ref: '#/components/schemas/type__OrganizationId'
        reason:
          type: string
          description: Reason for adding the entry.
        direction:
          $ref: '#/components/schemas/type_lists_Direction'
        list_type:
          $ref: '#/components/schemas/type_lists_ListType'
        entry_type:
          $ref: '#/components/schemas/type_lists_EntryType'
        created_at:
          type: string
          format: date-time
          description: Time at which entry was created.
        read_only:
          type: boolean
          description: Whether the entry is read-only and cannot be deleted via the API.
        pod_id:
          type: string
          description: ID of pod.
        inbox_id:
          type: string
          description: ID of inbox, if entry is inbox-scoped.
      required:
        - entry
        - organization_id
        - direction
        - list_type
        - entry_type
        - created_at
        - pod_id
      title: PodListEntry
    type__OrganizationId:
      type: string
      description: ID of organization.
      title: OrganizationId
    type_lists_EntryType:
      type: string
      enum:
        - email
        - domain
      description: Whether the entry is an email address or domain.
      title: EntryType
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer

````