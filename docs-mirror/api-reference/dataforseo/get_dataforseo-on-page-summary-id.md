> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OnPage API Summary

> Using this function, you can get the overall information on a website as well as drill down into exact on-page issues of a website that has been scanned.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/on_page/summary/{id}
openapi: 3.0.3
info:
  title: DataForSEO API
  version: 1.0.0
  description: DataForSEO API endpoints exposed through the AIsa unified gateway.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /dataforseo/on_page/summary/{id}:
    get:
      summary: OnPage API Summary
      description: >-
        Using this function, you can get the overall information on a website as
        well as drill down into exact on-page issues of a website that has been
        scanned. As a result, you will know what functions to use for receiving
        detailed data for each of the found issues.
      operationId: get_dataforseo_on_page_summary_id
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: >-
                      task identifier required field you can get this ID in the
                      response of the Task POST endpoint example:
                      “07131248-1535-0216-1000-17384017ad04”
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