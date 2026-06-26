> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Inboxes

> List Inboxes



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/inboxes
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
  /agentmail/inboxes:
    get:
      tags:
        - subpackage_inboxes
      summary: List Inboxes
      description: |-
        **CLI:**
        ```bash
        agentmail inboxes list
        ```
      operationId: list
      parameters:
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
                $ref: '#/components/schemas/type_inboxes_ListInboxesResponse'
components:
  schemas:
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
    type_inboxes_ListInboxesResponse:
      type: object
      properties:
        count:
          $ref: '#/components/schemas/type__Count'
        limit:
          $ref: '#/components/schemas/type__Limit'
        next_page_token:
          $ref: '#/components/schemas/type__PageToken'
        inboxes:
          type: array
          items:
            $ref: '#/components/schemas/type_inboxes_Inbox'
          description: Ordered by `created_at` descending.
      required:
        - count
        - inboxes
      title: ListInboxesResponse
    type__Count:
      type: integer
      description: Number of items returned.
      title: Count
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
    type_pods_PodId:
      type: string
      description: ID of pod.
      title: PodId
    type_inboxes_InboxId:
      type: string
      description: The ID of the inbox.
      title: InboxId
    type_inboxes_Email:
      type: string
      description: Email address of the inbox.
      title: Email
    type_inboxes_DisplayName:
      type: string
      description: 'Display name: `Display Name <username@domain.com>`.'
      title: DisplayName
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