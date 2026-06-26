> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Inbox

> Delete Inbox



## OpenAPI

````yaml openapi/agentmail.json DELETE /agentmail/inboxes/{inbox_id}
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
    delete:
      tags:
        - subpackage_inboxes
      summary: Delete Inbox
      description: |-
        **CLI:**
        ```bash
        agentmail inboxes delete --inbox-id <inbox_id>
        ```
      operationId: delete
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
      responses:
        '200':
          description: Successful response
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