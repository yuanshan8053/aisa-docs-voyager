> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Historical Keyword Data

> This endpoint provides Google historical keyword data for specified keywords, including search volume, cost-per-click, competition values for paid search, mo...



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/google/historical_keyword_data/live
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
  /dataforseo/dataforseo_labs/google/historical_keyword_data/live:
    post:
      summary: Historical Keyword Data
      description: >-
        This endpoint provides Google historical keyword data for specified
        keywords, including search volume, cost-per-click, competition values
        for paid search, monthly searches, and search volume trends. You can get
        historical keyword data since **August, 2021**, depending on keywords
        along with location and language combination. You can find the list of
        supported locations and languages
        [here.](https://docs.dataforseo.com/v3/dataforseo_labs/locations_and_languages.md)
      operationId: post_dataforseo_dataforseo_labs_google_historical_keyword_data_live
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
                    keywords required field The maximum number of keywords you
                    can specify: 700 The maximum number of characters for each
                    keyword: 80 The maximum number of words for each keyword
                    phrase: 10 the specified keywords will be converted to
                    lowercase format, data will be provided in a separate array
                    note that if some of the keywords specified in this array
                    are omitted in the results you receive, then our database
                    doesn’t contain such keywords and cannot return data on them
                    you will not be charged for the keywords omitted in the
                    results learn more about rules and limitations of keyword
                    and keywords fields in DataForSEO APIs in this Help Center
                    article
                location_name:
                  type: string
                  description: >-
                    full name of the location required field if you don’t
                    specify location_code Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: United Kingdom
                location_code:
                  type: integer
                  description: >-
                    location code required field if you don’t specify
                    location_name Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_code by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language required field if you don’t
                    specify language_code Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available locations with their language_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    language code required field if you don’t specify
                    language_name Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available locations with their language_code by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
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
                  tasks.result.se_type:
                    type: string
                    description: search engine type
                  tasks.result.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains keywords and related data
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword:
                    type: string
                    description: >-
                      keyword keyword is returned with decoded %## (plus
                      character ‘+’ will be decoded to a space character)
                  tasks.result.items.location_code:
                    type: integer
                    description: >-
                      location code in a POST array if there is no data, then
                      the value is null
                  tasks.result.items.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.items.history:
                    type: array
                    items:
                      type: string
                    description: array of objects with historical data for the keyword
                  tasks.result.items.history.year:
                    type: integer
                    description: year
                  tasks.result.items.history.month:
                    type: integer
                    description: month
                  tasks.result.items.history.keyword_info:
                    type: object
                    description: historical data for the keyword
                  tasks.result.items.history.keyword_info.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.history.keyword_info.last_updated_time:
                    type: string
                    description: >-
                      date and time when keyword data was updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.history.keyword_info.competition:
                    type: number
                    description: >-
                      competition represents the relative amount of competition
                      associated with the given keyword; the value is based on
                      Google Ads data and can be between 0 and 1 (inclusive)
                  tasks.result.items.history.keyword_info.competition_level:
                    type: string
                    description: >-
                      competition level represents the relative level of
                      competition associated with the given keyword in paid SERP
                      only; possible values: LOW, MEDIUM, HIGH if competition
                      level is unknown, the value is null; learn more about the
                      metric in this help center article
                  tasks.result.items.history.keyword_info.cpc:
                    type: number
                    description: >-
                      cost-per-click represents the average cost per click (USD)
                      historically paid for the keyword
                  tasks.result.items.history.keyword_info.search_volume:
                    type: integer
                    description: >-
                      average monthly search volume rate represents the
                      (approximate) number of searches for the given keyword
                      idea on google.com
                  tasks.result.items.history.keyword_info.low_top_of_page_bid:
                    type: number
                    description: >-
                      minimum bid for the ad to be displayed at the top of the
                      first page indicates the value greater than about 20% of
                      the lowest bids for which ads were displayed (based on
                      Google Ads statistics for advertisers) the value may
                      differ depending on the location specified in a POST
                      request
                  tasks.result.items.history.keyword_info.high_top_of_page_bid:
                    type: number
                    description: >-
                      maximum bid for the ad to be displayed at the top of the
                      first page indicates the value greater than about 80% of
                      the lowest bids for which ads were displayed (based on
                      Google Ads statistics for advertisers) the value may
                      differ depending on the location specified in a POST
                      request
                  tasks.result.items.history.keyword_info.categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      product and service categories you can download the full
                      list of possible categories
                  tasks.result.items.history.keyword_info.monthly_searches:
                    type: array
                    items:
                      type: string
                    description: >-
                      monthly searches represents the (approximate) number of
                      searches on this keyword idea (as available for the past
                      twelve months), targeted to the specified geographic
                      locations
                  tasks.result.items.history.keyword_info.monthly_searches.year:
                    type: integer
                    description: year
                  tasks.result.items.history.keyword_info.monthly_searches.month:
                    type: integer
                    description: month
                  tasks.result.items.history.keyword_info.monthly_searches.search_volume:
                    type: integer
                    description: monthly average search volume rate
                  tasks.result.items.history.keyword_info.search_volume_trend:
                    type: object
                    description: >-
                      search volume trend changes represents search volume
                      change in percent compared to the previous period
                  tasks.result.items.history.keyword_info.search_volume_trend.monthly:
                    type: integer
                    description: >-
                      search volume change in percent compared to the previous
                      month
                  tasks.result.items.history.keyword_info.search_volume_trend.quarterly:
                    type: integer
                    description: >-
                      search volume change in percent compared to the previous
                      quarter
                  tasks.result.items.history.keyword_info.search_volume_trend.yearly:
                    type: integer
                    description: >-
                      search volume change in percent compared to the previous
                      year
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