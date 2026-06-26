> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organization Enrichment

> Use the Oganization Enrichment endpoint to enrich data for 1 company.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/organizations/enrich
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
  /apollo/organizations/enrich:
    get:
      summary: Organization Enrichment
      description: >-
        Use the Oganization Enrichment endpoint to enrich data for 1 company. To
        enrich data for up to 10 companies with a single API call, use the Bulk
        Organization Enrichment endpoint instead. Calling this endpoint does
        consume credits as part of your Apollo pricing plan . Enriched data
        potentially includes industry information, revenue, employee counts,
        funding round details, and corporate phone numbers and locations.
        Calling this endpoint does consume credits as part of your Apollo
        pricing plan .
      operationId: get_apollo_organizations_enrich
      parameters:
        - name: domain
          in: query
          required: true
          schema:
            type: string
          description: >-
            The domain of the company that you want to enrich. Do not include
            www., the @ symbol, or similar. Example: apollo.io or microsoft.com
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