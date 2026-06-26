> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Google App Searches Results by id

> This endpoint will provide you with a list of apps ranking on Google Play for the `keyword` specified in a POST request.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/app_data/google/app_searches/task_get/advanced/{id}
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
  /dataforseo/app_data/google/app_searches/task_get/advanced/{id}:
    get:
      summary: Get Google App Searches Results by id
      description: >-
        This endpoint will provide you with a list of apps ranking on Google
        Play for the `keyword` specified in a POST request. You will also
        receive additional information about each application: its ID, icon,
        reviews count, rating, price, and other data. The results are specific
        to the `keyword` as well as location and language parameters specified
        in the POST request.
      operationId: get_dataforseo_app_data_google_app_searches_task_get_advanced_id
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
                      task identifier unique task identifier in our system in
                      the UUID format you will be able to use it within 30 days
                      to request the results of the task at any time
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