> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get ‘Bing Keyword Performance’ Results by id

> You can receive a set of keyword performance stats for a group of keywords depending on the specified match type, location and language parameters.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/keywords_data/bing/keyword_performance/task_get/{id}
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
  /dataforseo/keywords_data/bing/keyword_performance/task_get/{id}:
    get:
      summary: Get ‘Bing Keyword Performance’ Results by id
      description: >-
        You can receive a set of keyword performance stats for a group of
        keywords depending on the specified match type, location and language
        parameters. Ad position, clicks, impressions, and other keyword metrics
        are aggregated for the last month for one or all of the following device
        types: mobile, desktop, tablet.
      operationId: get_dataforseo_keywords_data_bing_keyword_performance_task_get_id
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