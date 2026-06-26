> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Organization Enrichment

> Use the Bulk Organization Enrichment endpoint to enrich data for up to 10 companies with a single API call.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/organizations/bulk_enrich
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
  /apollo/organizations/bulk_enrich:
    post:
      summary: Bulk Organization Enrichment
      description: >-
        Use the Bulk Organization Enrichment endpoint to enrich data for up to
        10 companies with a single API call. To enrich data for only 1 company,
        use the Organization Enrichment endpoint instead. Enriched data
        potentially includes industry information, revenue, employee counts,
        funding round details, and corporate phone numbers and locations.
        Calling this endpoint does consume credits as part of your Apollo
        pricing plan . This endpoint's rate limit is throttled to 50% of the
        Organization Enrichment endpoint's per-minute rate limit, and is 100% of
        the hourly and daily rate limits for the same individual endpoint.
      operationId: post_apollo_organizations_bulk_enrich
      parameters:
        - name: domains[]
          in: query
          required: true
          schema:
            type: array
            items:
              type: string
          description: >-
            The domain of each company that you want to enrich. Do not include
            www., the @ symbol, or similar. Example: apollo.io and microsoft.com
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    description: Response field
                  error_code:
                    type: string
                    description: Response field
                  error_message:
                    type: string
                    description: Response field
                  total_requested_domains:
                    type: integer
                    description: Response field
                  unique_domains:
                    type: integer
                    description: Response field
                  unique_enriched_records:
                    type: integer
                    description: Response field
                  missing_records:
                    type: integer
                    description: Response field
                  organizations:
                    type: array
                    items:
                      type: string
                    description: Response array
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