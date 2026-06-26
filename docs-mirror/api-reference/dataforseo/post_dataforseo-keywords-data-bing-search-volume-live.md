> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Live ‘Search Volume’ Tasks

> This endpoint will provide you with search volume data for the last month, search volume trend for up to 24 past months (that will let you estimate search vo...



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/keywords_data/bing/search_volume/live
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
  /dataforseo/keywords_data/bing/search_volume/live:
    post:
      summary: Setting Live ‘Search Volume’ Tasks
      description: >-
        This endpoint will provide you with search volume data for the last
        month, search volume trend for up to 24 past months (that will let you
        estimate search volume dynamics), current cost-per-click and competition
        values for paid search.
      operationId: post_dataforseo_keywords_data_bing_search_volume_live
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
                    can specify: 1000 The maximum number of characters for each
                    keyword: 100 the specified keywords will be converted to
                    lowercase, data will be provided in a separate array learn
                    more about rules and limitations of keyword and keywords
                    fields in DataForSEO APIs in this Help Center article
                location_name:
                  type: string
                  description: >-
                    full name of search engine location required field if you
                    don’t specify location_code or location_coordinate if you
                    use this field, you don’t need to specify location_code or
                    location_coordinate you can receive the list of available
                    locations of the search engine with their location_name by
                    making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/bing/locations
                    example: London,England,United Kingdom
                location_code:
                  type: integer
                  description: >-
                    search engine location code required field if you don’t
                    specify location_name or location_coordinate if you use this
                    field, you don’t need to specify location_name or
                    location_coordinate you can receive the list of available
                    locations of the search engines with their location_code by
                    making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/bing/locations
                    example: 2840
                location_coordinate:
                  type: string
                  description: >-
                    GPS coordinates of a location required field if you don’t
                    specify location_name or location_code if you use this
                    field, you don’t need to specify location_name or
                    location_code location_coordinate parameter should be
                    specified in the “latitude,longitude” format the data will
                    be provided for the country the specified coordinates belong
                    to example: 52.6178549,-155.352142
                language_name:
                  type: string
                  description: >-
                    full name of search engine language required field if you
                    don’t specify language_code if you use this field, you don’t
                    need to specify language_code supported languages: English,
                    French, German
                language_code:
                  type: string
                  description: >-
                    search engine language code required field if you don’t
                    specify language_name if you use this field, you don’t need
                    to specify language_name supported languages: en, fr, de
                device:
                  type: string
                  description: >-
                    device type optional field specify this field if you want to
                    get the data for a particular device type; possible values:
                    all, mobile, desktop, tablet default value: all
                sort_by:
                  type: string
                  description: >-
                    results sorting parameters optional field Use these
                    parameters to sort the results by search_volume, cpc,
                    competition or relevance in the descending order default
                    value: relevance
                date_from:
                  type: string
                  description: >-
                    starting date of the time range optional field minimal
                    value: 24 months from today’s date if you don’t specify this
                    field, data will be provided for the last 12 months minimum
                    value: two years back from today’s date date format:
                    "yyyy-mm-dd" example: "2020-01-01" Note: we do not recommend
                    using a custom time range for the past year’s dates
                date_to:
                  type: string
                  description: >-
                    ending date of the time range optional field if you don’t
                    specify this field, data will be provided for the last 12
                    months; minimum value: two years back from today’s date;
                    maximum value: one month from today’s date; note: we do not
                    recommend using a custom time range for the past year’s
                    dates; date format: "yyyy-mm-dd" example: "2020-03-15" Note:
                    we do not recommend using a custom time range for the past
                    year’s dates
                search_partners:
                  type: boolean
                  description: >-
                    Bing search partners type optional field if you specify
                    true, the results will be delivered for owned, operated, and
                    syndicated networks across Bing, Yahoo, AOL and partner
                    sites that host Bing, AOL, and Yahoo search. default value:
                    false – results are returned for Bing, AOL, and Yahoo search
                    networks
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
                - location_coordinate
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
                  tasks.result.keyword:
                    type: string
                    description: keyword in a POST array
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
                  tasks.result.search_partners:
                    type: boolean
                    description: >-
                      indicates whether data from partner networks included in
                      the response
                  tasks.result.device:
                    type: string
                    description: >-
                      device type in a POST array if there is no data, then the
                      value is null
                  tasks.result.competition:
                    type: number
                    description: >-
                      competition represents the relative amount of competition
                      associated with the given keyword in paid SERP only. This
                      value is based on Bing Ads data. Possible values: 0.1,
                      0.5,0.90.1 – low competition, 0.5 – medium competition,
                      0.9 – high competition; if there is no data the value is
                      null
                  tasks.result.cpc:
                    type: number
                    description: >-
                      cost-per-click represents the average cost per click (USD)
                      historically paid for the keyword. if there is no data
                      then the value is null
                  tasks.result.search_volume:
                    type: integer
                    description: >-
                      monthly average search volume rate represents either the
                      (approximate) number of searches for the given keyword
                      idea on bing search engine depending on the user’s
                      targeting; search volume is rounded to the nearest tens;
                      if there is no data, the value is null
                  tasks.result.categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      product and service categories our API doesn’t return
                      categories for this endpoint: the parameter will always
                      equal null
                  tasks.result.monthly_searches:
                    type: array
                    items:
                      type: string
                    description: >-
                      monthly searches represents the (approximate) number of
                      searches on this keyword idea (as available for the past
                      twelve months), targeted to the specified geographic
                      locations if there is no data then the value is null
                  tasks.result.monthly_searches.year:
                    type: integer
                    description: year
                  tasks.result.monthly_searches.month:
                    type: integer
                    description: month
                  tasks.result.monthly_searches.search_volume:
                    type: integer
                    description: >-
                      monthly average search volume rate search volume is
                      rounded to the nearest tens
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