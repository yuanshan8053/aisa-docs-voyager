> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Bing Ads Keyword Suggestions For URL Results by id

> This endpoint provides keyword suggestions based on the content of a given webpage URL.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/keywords_data/bing/keyword_suggestions_for_url/task_get/{id}
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
  /dataforseo/keywords_data/bing/keyword_suggestions_for_url/task_get/{id}:
    get:
      summary: Get Bing Ads Keyword Suggestions For URL Results by id
      description: >-
        This endpoint provides keyword suggestions based on the content of a
        given webpage URL. It analyzes the page and returns a list of relevant
        keywords, along with a confidence score that indicates the probability
        that the keyword would match a user’s search query.
      operationId: >-
        get_dataforseo_keywords_data_bing_keyword_suggestions_for_url_task_get_id
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