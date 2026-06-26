> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organization Job Postings

> Use the Organization Job Postings endpoint to retrieve the current job postings for companies.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/organizations/{organization_id}/job_postings
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
  /apollo/organizations/{organization_id}/job_postings:
    get:
      summary: Organization Job Postings
      description: >-
        Use the Organization Job Postings endpoint to retrieve the current job
        postings for companies. This can help you identify companies that are
        growing headcount in areas that are strategically important for you.
        Calling this endpoint does consume credits as part of your Apollo
        pricing plan . To protect Apollo's performance for all users, this
        endpoint has a display limit of 10,000 records. This limitation does not
        restrict your access to Apollo's database; you just need to access the
        data in batches.
      operationId: get_apollo_organizations_organization_id_job_postings
      parameters:
        - name: organization_id
          in: path
          required: true
          schema:
            type: string
          description: >-
            The organization ID of the company for which you want to find job
            postings. Each company in the Apollo database is assigned a unique
            ID. To find IDs, call the Organization Search endpoint and identify
            the values for organization_id. Example: 5e66b6381e05b4008c8331b8
        - name: page
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The page number of the Apollo data that you want to retrieve. Use
            this parameter in combination with the per_page parameter to make
            search results for navigable and improve the performance of the
            endpoint. Example: 4
        - name: per_page
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The number of search results that should be returned for each page.
            Limiting the number of results per page improves the endpoint's
            performance. Use the page parameter to search the different pages of
            data. Example: 10
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  organization_job_postings:
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