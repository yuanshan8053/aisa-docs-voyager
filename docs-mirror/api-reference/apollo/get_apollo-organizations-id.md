> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Complete Organization Info

> Use the Get Complete Organization Info endpoint to retrieve complete details about an organization in the Apollo database.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/organizations/{id}
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
  /apollo/organizations/{id}:
    get:
      summary: Get Complete Organization Info
      description: >-
        Use the Get Complete Organization Info endpoint to retrieve complete
        details about an organization in the Apollo database. This endpoint
        requires a master API key. If you attempt to call the endpoint without a
        master key, you will receive a 403 response. Refer to Create API Keys to
        learn how to create a master API key. u003e ? Credits u003e u003e Using
        this endpoint potentially consumes your account’s credits. Refer to
        Apollo’s for more details.
      operationId: get_apollo_organizations_id
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: >-
            The Apollo ID for the organization that you want to research. To
            find organization IDs, call the Organization Search endpoint and
            identify the organizaton_id value for the organization. Example:
            5e66b6381e05b4008c8331b8
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  organization:
                    type: object
                    description: Response object
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