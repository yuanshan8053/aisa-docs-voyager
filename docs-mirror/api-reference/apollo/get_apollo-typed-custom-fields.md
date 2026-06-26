> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a List of All Custom Fields

> Get a list of all custom fields.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/typed_custom_fields
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
  /apollo/typed_custom_fields:
    get:
      summary: Get a List of All Custom Fields
      description: Get a list of all custom fields. Requires a master API key.
      operationId: get_apollo_typed_custom_fields
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
                    description: Custom field definitions (when returned).
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