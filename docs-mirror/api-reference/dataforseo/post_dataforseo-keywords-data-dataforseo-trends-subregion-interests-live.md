> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Live ‘DataForSEO Trends Subregion Interests’ Tasks

> This endpoint will provide you with location-specific keyword popularity data from DataForSEO Trends.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/keywords_data/dataforseo_trends/subregion_interests/live
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
  /dataforseo/keywords_data/dataforseo_trends/subregion_interests/live:
    post:
      summary: Setting Live ‘DataForSEO Trends Subregion Interests’ Tasks
      description: >-
        This endpoint will provide you with location-specific keyword popularity
        data from DataForSEO Trends. You can check keyword trends for Google
        Search, Google News, and Google Shopping.
      operationId: post_dataforseo_keywords_data_dataforseo_trends_subregion_interests_live
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
                    keywords required field the maximum number of keywords you
                    can specify: 5 avoid symbols and special characters (e.g.,
                    UTF symbols, emojis); specifying non-Latin characters,
                    you’ll get data for the countries where they are used learn
                    more about rules and limitations of keyword and keywords
                    fields in DataForSEO APIs in this Help Center article
                location_name:
                  type: string
                  description: >-
                    full name of search engine location optional field if you
                    don’t use this field, you will recieve global results if you
                    use this field, you don’t need to specify location_code you
                    can receive the list of available locations of the search
                    engine with their location_name by making a separate request
                    to
                    https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations
                    note that the data will be provided for the country the
                    specified location_name belongs to; example: United Kingdom
                location_code:
                  type: integer
                  description: >-
                    search engine location code optional field if you don’t use
                    this field, you will recieve global results if you use this
                    field, you don’t need to specify location_name you can
                    receive the list of available locations of the search
                    engines with their location_code by making a separate
                    request to
                    https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations
                    note that the data will be provided for the country the
                    specified location_code belongs to; example: 2840
                type:
                  type: string
                  description: >-
                    dataforseo trends type optional field if you don’t specify
                    this field, the web type will be used by default possible
                    values: web, news, ecommerce
                date_from:
                  type: string
                  description: >-
                    starting date of the time range optional field if you don’t
                    specify this field, the current day and month of the
                    preceding year will be used by default minimal value for the
                    web type: 2004-01-01 minimal value for other types:
                    2008-01-01 date format: "yyyy-mm-dd" example: "2019-01-15"
                date_to:
                  type: string
                  description: >-
                    ending date of the time range optional field if you don’t
                    specify this field, the today’s date will be used by default
                    date format: "yyyy-mm-dd" example: "2019-01-15"
                time_range:
                  type: string
                  description: >-
                    preset time ranges optional field if you specify date_from
                    or date_to parameters, this field will be ignored when
                    setting a task possible values for all type parameters:
                    past_4_hours, past_day, past_7_days, past_30_days,
                    past_90_days, past_12_months, past_5_years
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - keywords
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
                      full list of response codes here
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
                  tasks.result.keywords:
                    type: array
                    items:
                      type: string
                    description: keywords in a POST array
                  tasks.result.type:
                    type: array
                    items:
                      type: string
                    description: search engine type in a POST array
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
                  tasks.result.datetime:
                    type: string
                    description: >-
                      date and time when the result was received in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains keyword popularity and related data
                  tasks.result.items.position:
                    type: integer
                    description: >-
                      the alignment of the element can take the following
                      values: 1, 2, 3, 4, etc.
                  tasks.result.items.type:
                    type: string
                    description: type of element = ‘subregion_interests’
                  tasks.result.items.keywords:
                    type: array
                    items:
                      type: string
                    description: >-
                      relevant keywords the data included in the interests and
                      interests_comparison is based on the keywords listed in
                      this array
                  tasks.result.items.interests:
                    type: array
                    items:
                      type: string
                    description: subregional keyword popuarity data for each specified term
                  tasks.result.items.interests.keyword:
                    type: string
                    description: >-
                      relevant keyword the data included in the values element
                      is based on this keyword
                  tasks.result.items.interests.values:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains data on relative keyword popularity by country or
                      region
                  tasks.result.items.interests.values.geo_id:
                    type: string
                    description: >-
                      location identifier you can use this field for matching
                      obtained results with location parameters specified in the
                      request see the full list of available locations with
                      their geo_id here or by making a separate request to
                      https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations
                      example: US-NY
                  tasks.result.items.interests.values.geo_name:
                    type: string
                    description: >-
                      location name you can use this field for matching obtained
                      results with location parameters specified in the request
                      see the full list of available locations with their
                      geo_name here or by making a separate request to
                      https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations
                      example: Andorra
                  tasks.result.items.interests.values.value:
                    type: integer
                    description: >-
                      relative keyword popularity rate in a given location
                      represents location-specific keyword popularity rate over
                      the specified time range; using this value you can
                      understand how popular a keyword is in one location
                      compared to another location; calculation: we determine
                      the highest popularity value for the relevant keyword
                      across all locations, and then express all other values as
                      a percentage of that highest value (100); a value of 100
                      is the highest popularity for the term a value of 50 means
                      that the term is half as popular a value of 0 means there
                      was not enough data for this term
                  tasks.result.items.interests_comparison:
                    type: object
                    description: >-
                      comparison of data on subregional keyword popularity for
                      the specified parameters if you specified a single
                      keyword, the value will be null
                  tasks.result.items.interests_comparison.items:
                    type: array
                    items:
                      type: string
                    description: >-
                      keyword popularity values per location values in this
                      array represent percentages relative to the maximum value
                      within each region
                  tasks.result.items.interests_comparison.items.geo_id:
                    type: string
                    description: >-
                      location identifier you can use this field for matching
                      obtained results with location parameters specified in the
                      request see the full list of available locations with
                      their geo_id here or by making a separate request to
                      https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations
                      example: US-NY
                  tasks.result.items.interests_comparison.items.geo_name:
                    type: string
                    description: >-
                      location name you can use this field for matching obtained
                      results with location parameters specified in the request
                      see the full list of available locations with their
                      geo_name here or by making a separate request to
                      https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations
                      example: Andorra
                  tasks.result.items.interests_comparison.items.values:
                    type: array
                    items:
                      type: string
                    description: >-
                      keyword popularity rates within a given location
                      represents location-specific keyword popularity rate over
                      the specified time range; using these values, you can
                      understand which of the specified keywords is more popular
                      in the related location; the first value in the array is
                      provided for the first term from the keywords array, the
                      second value is provided for the second keyword, and so
                      on; calculation: we determine the highest popularity value
                      across all specified keywords within a given location, and
                      then express the popularity values of each keyword as a
                      percentage of the highest value (100); a value of 100 is
                      the peak popularity for the term a value of 50 means that
                      the term is half as popular a value of 0 means there was
                      not enough data for this term
                  tasks.result.items.interests_comparison.absolute_items:
                    type: array
                    items:
                      type: string
                    description: >-
                      keyword popularity rates across all locations values in
                      this array represent percentages relative to the maximum
                      value across all locations
                  tasks.result.items.interests_comparison.absolute_items.geo_id:
                    type: string
                    description: >-
                      location identifier you can use this field for matching
                      obtained results with location parameters specified in the
                      request see the full list of available locations with
                      their geo_id here or by making a separate request to
                      https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations
                      example: US-NY
                  tasks.result.items.interests_comparison.absolute_items.geo_name:
                    type: string
                    description: >-
                      location name you can use this field for matching obtained
                      results with location parameters specified in the request
                      see the full list of available locations with their
                      geo_name here or by making a separate request to
                      https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations
                      example: Andorra
                  tasks.result.items.interests_comparison.absolute_items.values:
                    type: array
                    items:
                      type: string
                    description: >-
                      keyword popularity rates relative to all locations
                      represents location-specific keyword popularity rate over
                      the specified time range; using these values, you can
                      understand how popular each keyword is compared to all
                      other keywords across all locations; the first value in
                      the array is provided for the first term from the keywords
                      array, the second value is provided for the second
                      keyword, and so on; calculation: we determine the highest
                      popularity value across all keywords across all locations,
                      and then express all other values as a percentage of that
                      highest value (100); a value of 100 is the peak popularity
                      for the term a value of 50 means that the term is half as
                      popular a value of 0 means there was not enough data for
                      this term
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