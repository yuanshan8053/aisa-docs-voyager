> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Google Shopping Reviews Results by id

> This endpoint provides review data on products listed on the Google Shopping marketplace, including top mentioned keywords, review titles, images, ratings, r...



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/merchant/google/reviews/task_get/advanced/{id}
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
  /dataforseo/merchant/google/reviews/task_get/advanced/{id}:
    get:
      summary: Get Google Shopping Reviews Results by id
      description: >-
        This endpoint provides review data on products listed on the Google
        Shopping marketplace, including top mentioned keywords, review titles,
        images, ratings, review content, reviewer info, review publication
        dates, and more. The results are specific to the `product_id` indicated
        in the POST request.
      operationId: get_dataforseo_merchant_google_reviews_task_get_advanced_id
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