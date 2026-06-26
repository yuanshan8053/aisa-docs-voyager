> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Live ‘DataForSEO Search Volume’ Tasks

> This endpoint will provide you with search volume normalized with Bing search volume data or clickstream data for up to 1000 keywords in a single request.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/keywords_data/clickstream_data/dataforseo_search_volume/live
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
  /dataforseo/keywords_data/clickstream_data/dataforseo_search_volume/live:
    post:
      summary: Setting Live ‘DataForSEO Search Volume’ Tasks
      description: >-
        This endpoint will provide you with search volume normalized with Bing
        search volume data or clickstream data for up to 1000 keywords in a
        single request.
      operationId: >-
        post_dataforseo_keywords_data_clickstream_data_dataforseo_search_volume_live
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
                    of keywords you can specify in this array: 1000 the keywords
                    will be converted to lowercase format Note: certain symbols
                    and characters (e.g., UTF symbols, emojis) are not allowed
                    to learn more about which symbols and characters can be
                    used, please refer to this article learn more about rules
                    and limitations of keyword and keywords fields in DataForSEO
                    APIs in this Help Center article
                location_name:
                  type: string
                  description: >-
                    full name of search engine location required field if you
                    don’t specify location_code you can receive the list of
                    available locations with location_name by making a separate
                    request to
                    https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages
                    example: United Kingdom
                location_code:
                  type: integer
                  description: >-
                    search engine location code required field if you don’t
                    specify location_name if you use this field, you can receive
                    the list of available locations with location_code by making
                    a separate request to the
                    https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages
                    example: 2826
                language_name:
                  type: string
                  description: >-
                    full name of search engine language required field if don’t
                    specify language_code you can receive the list of available
                    languages with their language_name by making a separate
                    request to the
                    https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    search engine language code required field if don’t specify
                    language_name you can receive the list of available
                    languages with their language_code by making a separate
                    request to the
                    https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages
                    example: en
                use_clickstream:
                  type: boolean
                  description: >-
                    use clickstream data to provide results optional field if
                    set to true, you will get DataForSEO search volume values
                    based on clickstream data; if set to false, Bing search
                    volume data will be used to calculate DataForSEO search
                    volume; default value: true; Note: Bing search volume is
                    available for locations provided in Bing Search Volume
                    History Locations and Bing Ads Locations endpoints; search
                    volume values for any other location are calculated based on
                    clickstream data even if you set this parameter to false
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
                    type: array
                    items:
                      type: string
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
                    description: >-
                      location code in a POST array if there is no data, then
                      the value is null
                  tasks.result.language_code:
                    type: string
                    description: >-
                      language code in a POST array if there is no data, then
                      the value is null
                  tasks.result.items_count:
                    type: string
                    description: ithe number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of keywords contains keywords and their search
                      volume rates
                  tasks.result.items.keyword:
                    type: string
                    description: keyword provided in the POST array
                  tasks.result.items.use_clickstream:
                    type: boolean
                    description: >-
                      indicates if the use_clickstream parameter is active
                      possible values: true, false
                  tasks.result.items.search_volume:
                    type: integer
                    description: current search volume rate of a keyword
                  tasks.result.items.monthly_searches:
                    type: array
                    items:
                      type: string
                    description: >-
                      monthly search volume rates array of objects with search
                      volume rates in a certain month of a year
                  tasks.result.items.monthly_searches.year:
                    type: integer
                    description: year
                  tasks.result.items.monthly_searches.month:
                    type: integer
                    description: month
                  tasks.result.items.monthly_searches.search_volume:
                    type: integer
                    description: search volume rate in a certain month of a year
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