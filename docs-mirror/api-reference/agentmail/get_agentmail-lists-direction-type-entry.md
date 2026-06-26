> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get List Entry

> Get List Entry



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/lists/{direction}/{type}/{entry}
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
  /agentmail/lists/{direction}/{type}/{entry}:
    get:
      tags:
        - subpackage_lists
      summary: Get List Entry
      description: >-
        **CLI:**

        ```bash

        agentmail lists get --direction <direction> --type <type> --entry
        <entry>

        ```
      operationId: get
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
        - name: entry
          in: path
          description: Email address or domain.
          required: true
          schema:
            type: string
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
                $ref: '#/components/schemas/type_lists_ListEntry'
        '404':
          description: Error response with status 404
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type__ErrorResponse'
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