> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Inbox

> Update Inbox



## OpenAPI

````yaml openapi/agentmail.json PATCH /agentmail/inboxes/{inbox_id}
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
  /agentmail/inboxes/{inbox_id}:
    patch:
      tags:
        - subpackage_inboxes
      summary: Update Inbox
      description: >-
        **CLI:**

        ```bash

        agentmail inboxes update --inbox-id <inbox_id> --display-name "Updated
        Name"

        ```
      operationId: update
      parameters:
        - name: inbox_id
          in: path
          required: true
          schema:
            $ref: '#/components/schemas/type_inboxes_InboxId'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      requestBody:
        description: >-
          Expects an object; provide at least one of `display_name` or
          `metadata`.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/type_inboxes_UpdateInboxRequest'
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_inboxes_Inbox'
        '400':
          description: Error response with status 400
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type__ValidationErrorResponse'
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
    type_inboxes_UpdateInboxRequest:
      type: object
      properties:
        display_name:
          $ref: '#/components/schemas/type_inboxes_DisplayName'
        metadata:
          oneOf:
            - $ref: '#/components/schemas/type_inboxes_UpdateMetadata'
            - type: 'null'
          description: >-
            Metadata to merge into the inbox's existing metadata. Keys you
            include

            are added or overwritten; keys you omit are left unchanged. To
            remove a

            single key, send it with a null value. To clear all metadata, send

            `metadata` as null. Sending an empty object is rejected; use null to

            clear. Each update must include at least one of `display_name` or

            `metadata`.
      title: UpdateInboxRequest
    type_inboxes_Inbox:
      type: object
      properties:
        pod_id:
          $ref: '#/components/schemas/type_pods_PodId'
        inbox_id:
          $ref: '#/components/schemas/type_inboxes_InboxId'
        email:
          $ref: '#/components/schemas/type_inboxes_Email'
        display_name:
          $ref: '#/components/schemas/type_inboxes_DisplayName'
        client_id:
          $ref: '#/components/schemas/type_inboxes_ClientId'
        metadata:
          $ref: '#/components/schemas/type_inboxes_Metadata'
          description: Custom metadata attached to the inbox.
        updated_at:
          type: string
          format: date-time
          description: Time at which inbox was last updated.
        created_at:
          type: string
          format: date-time
          description: Time at which inbox was created.
      required:
        - pod_id
        - inbox_id
        - email
        - updated_at
        - created_at
      title: Inbox
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
    type_inboxes_DisplayName:
      type: string
      description: 'Display name: `Display Name <username@domain.com>`.'
      title: DisplayName
    type_inboxes_UpdateMetadata:
      type: object
      additionalProperties:
        oneOf:
          - $ref: '#/components/schemas/type_inboxes_MetadataValue'
          - type: 'null'
      description: |-
        Custom key-value pairs to merge into the inbox's existing metadata. A
        value may be a string, number, boolean, or null. Setting a key to null
        removes it. Up to 256 keys; keys and string values are each limited to
        256 characters.
      title: UpdateMetadata
    type_pods_PodId:
      type: string
      description: ID of pod.
      title: PodId
    type_inboxes_Email:
      type: string
      description: Email address of the inbox.
      title: Email
    type_inboxes_ClientId:
      type: string
      description: Client ID of inbox.
      title: ClientId
    type_inboxes_Metadata:
      type: object
      additionalProperties:
        $ref: '#/components/schemas/type_inboxes_MetadataValue'
      description: >-
        Custom key-value pairs attached to the inbox. Up to 256 keys. Keys and

        string values are each limited to 256 characters. When updating
        metadata,

        send a key with a null value to remove that key.
      title: Metadata
    type__ErrorName:
      type: string
      description: Name of error.
      title: ErrorName
    type__ErrorMessage:
      type: string
      description: Error message.
      title: ErrorMessage
    type_inboxes_MetadataValue:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
      description: A metadata value. May be a string, number, or boolean.
      title: MetadataValue
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer

````