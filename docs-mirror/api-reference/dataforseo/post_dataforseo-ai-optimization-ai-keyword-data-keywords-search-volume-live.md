> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Keyword Data Keyword Search Volume

> This endpoint provides search volume data for your target keywords, reflecting their estimated usage in AI tools.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/ai_optimization/ai_keyword_data/keywords_search_volume/live
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
  /dataforseo/ai_optimization/ai_keyword_data/keywords_search_volume/live:
    post:
      summary: AI Keyword Data Keyword Search Volume
      description: >-
        This endpoint provides search volume data for your target keywords,
        reflecting their estimated usage in AI tools.
      operationId: >-
        post_dataforseo_ai_optimization_ai_keyword_data_keywords_search_volume_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                keywords:
                  type: array
                  items:
                    type: string
                  description: >-
                    keywords required field UTF-8 encoding The maximum number of
                    keywords you can specify: 1000; The maximum number of
                    characters in a single keyword: 250; The keywords will be
                    converted to lowercase format;learn more about rules and
                    limitations of keyword and keywords fields in DataForSEO
                    APIs in this Help Center article
                location_name:
                  type: string
                  description: >-
                    full name of the location required field if you don't
                    specify location_code Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languages
                    example: United Kingdom
                location_code:
                  type: integer
                  description: >-
                    unique location identifier required field if you don't
                    specify location_name Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_code by making a
                    separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languages
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language required field if you don't
                    specify language_code if you use this field, you don't need
                    to specify language_code you can receive the list of
                    available languages with their language_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    language code required field if you don't specify
                    language_name if you use this field, you don't need to
                    specify language_name you can receive the list of available
                    languages with their language_code by making a separate
                    request to the
                    https://api.dataforseo.com/v3/ai_optimization/ai_keyword_data/locations_and_languages
                    example: en
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - keywords
                - location_name
                - location_code
                - language_name
                - language_code
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  version:
                    type: string
                    description: the current version of the API
                  status_code:
                    type: integer
                    description: >-
                      general status code you can find the full list of the
                      response codes here Note: we strongly recommend designing
                      a necessary system for handling related exceptional or
                      error conditions
                  status_message:
                    type: string
                    description: >-
                      general informational message you can find the full list
                      of general informational messages here
                  time:
                    type: string
                    description: execution time, seconds
                  cost:
                    type: number
                    description: total tasks cost, USD
                  tasks_count:
                    type: integer
                    description: the number of tasks in the tasks array
                  tasks_error:
                    type: integer
                    description: >-
                      the number of tasks in the tasks array returned with an
                      error
                  tasks:
                    type: array
                    items:
                      type: string
                    description: array of tasks
                  tasks.id:
                    type: string
                    description: >-
                      task identifier unique task identifier in our system in
                      the UUID format
                  tasks.status_code:
                    type: integer
                    description: >-
                      status code of the task generated by DataForSEO; can be
                      within the following range: 10000-60000 you can find the
                      full list of the response codes here
                  tasks.status_message:
                    type: string
                    description: >-
                      informational message of the task you can find the full
                      list of general informational messages here
                  tasks.time:
                    type: string
                    description: execution time, seconds
                  tasks.cost:
                    type: number
                    description: cost of the task, USD
                  tasks.result_count:
                    type: integer
                    description: number of elements in the result array
                  tasks.path:
                    type: array
                    items:
                      type: string
                    description: URL path
                  tasks.data:
                    type: object
                    description: >-
                      contains the same parameters that you specified in the
                      POST request
                  tasks.result:
                    type: array
                    items:
                      type: string
                    description: array of results
                  tasks.result.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.items_count:
                    type: integer
                    description: number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains specified keywords with their AI search volume
                      rates
                  tasks.result.items.keyword:
                    type: string
                    description: specified keyword
                  tasks.result.items.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.items.ai_monthly_searches:
                    type: array
                    items:
                      type: string
                    description: >-
                      monthly AI search volume rates array of objects with AI
                      search volume rates in a certain month of a year
                  tasks.result.items.ai_monthly_searches.year:
                    type: integer
                    description: year
                  tasks.result.items.ai_monthly_searches.month:
                    type: integer
                    description: month
                  tasks.result.items.ai_monthly_searches.ai_search_volume:
                    type: integer
                    description: >-
                      AI search volume rate in a certain month of a year learn
                      more about this metric here
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