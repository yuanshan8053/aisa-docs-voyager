> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon Bulk Search Volume

> This endpoint will provide you with search volume values for a maximum of 1,000 keywords in one API request.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/amazon/bulk_search_volume/live
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
  /dataforseo/dataforseo_labs/amazon/bulk_search_volume/live:
    post:
      summary: Amazon Bulk Search Volume
      description: >-
        This endpoint will provide you with search volume values for a maximum
        of 1,000 keywords in one API request. Here search volume represents the
        approximate number of monthly searches for a keyword on Amazon. The
        returned results are specific to the `keywords`, `location`, and
        `language` parameters specified in a POST request.
      operationId: post_dataforseo_dataforseo_labs_amazon_bulk_search_volume_live
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
                    target keywords required field UTF-8 encoding maximum number
                    of keywords you can specify in this array: 1000; the
                    keywords will be converted to lowercase format learn more
                    about rules and limitations of keyword and keywords fields
                    in DataForSEO APIs in this Help Center article
                location_name:
                  type: string
                  description: >-
                    full name of the location required field if don’t specify
                    location_code you can receive the list of available
                    locations with their location_name by making a separate
                    request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;
                    Note: this endpoint currently supports the following
                    locations and languages only: Australia – 2036, en Austria –
                    2040, de Canada – 2124, en Egypt – 2818, ar France – 2250,
                    fr Germany – 2276, de India – 2356, en Italy – 2380, it
                    Mexico – 2484, es Netherlands – 2528, nl Saudi Arabia –
                    2682, ar Singapore – 2702, en Spain – 2724, es United Arab
                    Emirates – 2784, ar United Kingdom – 2826, en United States
                    – 2840, en example: United States
                location_code:
                  type: integer
                  description: >-
                    location code required field if don’t specify location_name
                    you can receive the list of available locations with their
                    location_code by making a separate request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;
                    Note: this endpoint currently supports these locations and
                    languages only; example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language required field if don’t specify
                    language_code you can receive the list of available
                    languages with their language_name by making a separate
                    request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    Note: this endpoint currently supports these locations and
                    languages only; example: English
                language_code:
                  type: string
                  description: >-
                    language code required field if don’t specify language_name
                    you can receive the list of available languages with their
                    language_code by making a separate request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    Note: this endpoint currently supports these locations and
                    languages only; example: en
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
                  tasks.result.se_type:
                    type: string
                    description: search engine type
                  tasks.result.location_code:
                    type: integer
                    description: >-
                      location code in a POST array if there is no data, then
                      the value is null
                  tasks.result.language_code:
                    type: string
                    description: >-
                      language code in a POST array if there is no data, then
                      the value is null
                  tasks.result.total_count:
                    type: integer
                    description: >-
                      total amount of results in our database relevant to your
                      request
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains keyword search volume data data
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword:
                    type: string
                    description: keyword in a POST array
                  tasks.result.items.search_volume:
                    type: integer
                    description: >-
                      average monthly search volume rate represents the
                      (approximate) number of searches for the returned keyword
                      on Amazon
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