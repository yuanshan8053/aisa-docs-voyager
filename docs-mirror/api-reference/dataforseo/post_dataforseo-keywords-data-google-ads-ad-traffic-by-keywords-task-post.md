> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting ‘Ad Traffic By Keywords’ Tasks

> Note that Google Ads Keywords Data API is based on the latest version of the [Google Ads API](https://developers.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/keywords_data/google_ads/ad_traffic_by_keywords/task_post
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
  /dataforseo/keywords_data/google_ads/ad_traffic_by_keywords/task_post:
    post:
      summary: Setting ‘Ad Traffic By Keywords’ Tasks
      description: >-
        Note that Google Ads Keywords Data API is based on the latest version of
        the [Google Ads
        API](https://developers.google.com/google-ads/api/docs/start) that has
        replaced legacy Google AdWords API. If you’re using [DataForSEO Google
        AdWords
        API](https://docs.dataforseo.com/v3/keywords_data/google/overview.md),
        you need to upgrade to [DataForSEO Google Ads
        API](https://docs.dataforseo.com/v3/keywords_data/google_ads/overview.md).
      operationId: >-
        post_dataforseo_keywords_data_google_ads_ad_traffic_by_keywords_task_post
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
                    keyword: 80 The maximum number of words for each keyword
                    phrase: 10 the keywords you specify will be converted to a
                    lowercase format Note #1: Google Ads may return no data for
                    certain groups of keywords; Note #2: Google Ads provides
                    combined search volume values for groups of similar keywords
                    to obtain search volume for similar keywords, we recommend
                    submitting such keywords in separate requests; Note #3:
                    Google Ads doesn’t allow using certain symbols and
                    characters (e.g., UTF symbols, emojis), so you can’t use
                    them when setting a task; to learn more about which symbols
                    and characters can be used, please refer to this article
                    learn more about rules and limitations of keyword and
                    keywords fields in DataForSEO APIs in this Help Center
                    article
                bid:
                  type: number
                  description: >-
                    the maximum custom bid required field the collected data
                    will be based on this value it stands for the price you are
                    willing to pay for an ad; the higher value you specify here,
                    the higher values you will get in the returned metrics learn
                    more in this help center article
                match:
                  type: string
                  description: >-
                    keywords match-type required field can take the following
                    values: exact, broad, phrase
                search_partners:
                  type: boolean
                  description: >-
                    include Google search partners optional field if you specify
                    true, the results will be delivered for owned, operated, and
                    syndicated networks across Google and partner sites that
                    host Google search; default value: false – results are
                    returned for Google search sites
                location_name:
                  type: string
                  description: >-
                    full name of search engine location optional field if you do
                    not indicate the location, you will receive worldwide
                    results, i.e., for all available locations; if you use this
                    field, you don’t need to specify location_code or
                    location_coordinate you can receive the list of available
                    locations of the search engine with their location_name by
                    making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/google_ads/locations
                    example: London,England,United Kingdom
                location_code:
                  type: integer
                  description: >-
                    search engine location code optional field if you do not
                    indicate the location, you will receive worldwide results,
                    i.e., for all available locations; if you use this field,
                    you don’t need to specify location_name or
                    location_coordinate; you can receive the list of available
                    locations of the search engines with their location_code by
                    making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/google_ads/locations
                    example: 2840
                location_coordinate:
                  type: string
                  description: >-
                    GPS coordinates of a location optional field if you do not
                    indicate the location, you will receive worldwide results,
                    i.e., for all available locations; if you use this field,
                    you don’t need to specify location_name or location_code;
                    location_coordinate parameter should be specified in the
                    “latitude,longitude” format; the data will be provided for
                    the country the specified coordinates belong to; example:
                    52.6178549,-155.352142
                language_name:
                  type: string
                  description: >-
                    full name of search engine language optional field you can
                    receive the list of available languages of the search engine
                    with their language_name by making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/google_ads/languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    search engine language code optional field you can receive
                    the list of available languages of the search engine with
                    their language_code by making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/google_ads/languages
                    example: en
                date_from:
                  type: string
                  description: >-
                    starting date of the forecasting time range required field
                    if you specify date_to if you indicate date_from and
                    date_to, you don’t need to specify date_interval minimum
                    value is tomorrow’s date the value you specify in date_from
                    shouldn’t be further than date_to date format: "yyyy-mm-dd"
                    example: "2021-10-30"if Status endpoint returns false in the
                    actual_data field, date_from can be set to the month before
                    last and prior; if Status endpoint returns true in the
                    actual_data field, date_from can be set to the last month
                    and prior
                date_to:
                  type: string
                  description: >-
                    ending date of the forecasting time range required field if
                    you specify date_from if you indicate date_from and date_to,
                    you don’t need to specify date_interval minimum value is
                    date_from +1 day maximum value is current day and month of
                    the next year date format: "yyyy-mm-dd" example:
                    "2022-10-30"
                date_interval:
                  type: string
                  description: >-
                    forecasting date interval optional field if you specify
                    date_interval, you don’t need to indicate date_from and
                    date_to possible values: next_week, next_month, next_quarter
                    default value: next_month
                sort_by:
                  type: string
                  description: >-
                    results sorting parameters optional field Use these
                    parameters to sort the results by relevance, impressions,
                    ctr, average_cpc, cost, or clicks in the descending order
                    default value: relevance
                postback_url:
                  type: string
                  description: >-
                    URL for sending task results optional field once the task is
                    completed, we will send a POST request with its results
                    compressed in the gzip format to the postback_url you
                    specified you can use the ‘$id’ string as a $id variable and
                    ‘$tag’ as urlencoded $tag variable. We will set the
                    necessary values before sending the request. example:
                    http://your-server.com/postbackscript?id=$id
                    http://your-server.com/postbackscript?id=$id&tag=$tag Note:
                    special characters in postback_url will be urlencoded; i.a.,
                    the # character will be encoded into %23 learn more on our
                    Help Center
                pingback_url:
                  type: string
                  description: >-
                    notification URL of a completed task optional field when a
                    task is completed we will notify you by GET request sent to
                    the URL you have specified you can use the ‘$id’ string as a
                    $id variable and ‘$tag’ as urlencoded $tag variable. We will
                    set the necessary values before sending the request.
                    example: http://your-server.com/pingscript?id=$id
                    http://your-server.com/pingscript?id=$id&tag=$tag Note:
                    special characters in pingback_url will be urlencoded; i.a.,
                    the # character will be encoded into %23 learn more on our
                    Help Center
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - keywords
                - bid
                - match
                - date_from
                - date_to
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
                    description: the number of tasks in the tasksarray
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
                      unique task identifier in our system in the Universally
                      unique identifier (UUID) format
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
                    description: array of results in this case, the value will be null
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