> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a List of Fields + Create a Custom Field

> Create a custom field.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/fields
openapi: 3.0.3
info:
  title: Apollo API
  version: 1.0.0
  description: Apollo API endpoints exposed through the AIsa unified gateway.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /apollo/fields:
    post:
      summary: Get a List of Fields + Create a Custom Field
      description: Create a custom field. Requires a master API key.
      operationId: post_apollo_fields
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                label:
                  type: string
                  description: Field label.
                modality:
                  type: string
                  description: Entity modality (e.g., contact).
                type:
                  type: string
                  description: Field type (e.g., textarea).
                meta:
                  type: object
                  description: Additional field config.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  typed_custom_fields:
                    type: array
                    items:
                      type: string
                    description: Created field(s) (when returned).
        '400':
          description: Bad request
        '401':
          description: Unauthorized
        '429':
          description: Rate limit exceeded
        '500':
          description: Internal server error
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````