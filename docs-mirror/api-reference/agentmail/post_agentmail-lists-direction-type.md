> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create List Entry

> Create List Entry



## OpenAPI

````yaml openapi/agentmail.json POST /agentmail/lists/{direction}/{type}
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
    post:
      tags:
        - subpackage_lists
      summary: Create List Entry
      description: >-
        **CLI:**

        ```bash

        agentmail lists create --direction <direction> --type <type> --entry
        user@example.com

        ```
      operationId: create
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
              $ref: '#/components/schemas/type_lists_CreateListEntryRequest'
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_lists_ListEntry'
        '400':
          description: Error response with status 400
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type__ValidationErrorResponse'
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
    type_lists_CreateListEntryRequest:
      type: object
      properties:
        entry:
          type: string
          description: Email address or domain to add.
        reason:
          type: string
          description: Reason for adding the entry.
      required:
        - entry
      title: CreateListEntryRequest
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
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer

````