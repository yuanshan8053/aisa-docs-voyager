> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Entries

> List Entries



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/lists/{direction}/{type}
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
  /agentmail/lists/{direction}/{type}:
    get:
      tags:
        - subpackage_lists
      summary: List Entries
      description: |-
        **CLI:**
        ```bash
        agentmail lists list --direction <direction> --type <type>
        ```
      operationId: list
      parameters:
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
                $ref: '#/components/schemas/type_lists_ListListEntriesResponse'
components:
  schemas:
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
    type_lists_ListListEntriesResponse:
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
            $ref: '#/components/schemas/type_lists_ListEntry'
          description: Ordered by entry ascending.
      required:
        - count
        - entries
      title: ListListEntriesResponse
    type__Count:
      type: integer
      description: Number of items returned.
      title: Count
    type_lists_ListEntry:
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
      required:
        - entry
        - organization_id
        - direction
        - list_type
        - entry_type
        - created_at
      title: ListEntry
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