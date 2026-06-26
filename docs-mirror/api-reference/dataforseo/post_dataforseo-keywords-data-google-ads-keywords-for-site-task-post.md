> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting ‘Keywords For Site’ Tasks

> Note that Google Ads Keywords Data API is based on the latest version of the [Google Ads API](https://developers.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/keywords_data/google_ads/keywords_for_site/task_post
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
  /dataforseo/keywords_data/google_ads/keywords_for_site/task_post:
    post:
      summary: Setting ‘Keywords For Site’ Tasks
      description: >-
        Note that Google Ads Keywords Data API is based on the latest version of
        the [Google Ads
        API](https://developers.google.com/google-ads/api/docs/start) that has
        replaced legacy Google AdWords API. If you’re using [DataForSEO Google
        AdWords
        API](https://docs.dataforseo.com/v3/keywords_data/google/overview.md),
        you need to upgrade to [DataForSEO Google Ads
        API](https://docs.dataforseo.com/v3/keywords_data/google_ads/overview.md).
      operationId: post_dataforseo_keywords_data_google_ads_keywords_for_site_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                target:
                  type: string
                  description: >-
                    domain or page required field the domain name of the target
                    website or the url of the target page; note: to obtain
                    keywords for the target website, use the target_type
                    parameter
                target_type:
                  type: string
                  description: >-
                    search keywords for site or url optional field possible
                    values: site, page; default value: page if set to site,
                    keywords will be provided for the entire site; if set to
                    page, keywords will be provided for the specified webpage
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
                search_partners:
                  type: boolean
                  description: >-
                    include Google search partners optional field if you specify
                    true, the results will be delivered for owned, operated, and
                    syndicated networks across Google and partner sites that
                    host Google search; default value: false – results are
                    returned for Google search sites
                date_from:
                  type: string
                  description: >-
                    starting date of the time range optional field date format:
                    "yyyy-mm-dd" minimal value: 4 years from the current date by
                    default, data is returned for the past 12 months; Note: the
                    indicated date cannot be greater than that specified in
                    date_to and/or yesterday’s date;if Status endpoint returns
                    false in the actual_data field, date_from can be set to the
                    month before last and prior; if Status endpoint returns true
                    in the actual_data field, date_from can be set to the last
                    month and prior
                date_to:
                  type: string
                  description: >-
                    ending date of the time range optional field Note: the
                    indicated date cannot be greater than yesterday’s date; if
                    you don’t specify this field, yesterday’s date will be used
                    by default date format: "yyyy-mm-dd" example: "2022-11-30"
                include_adult_keywords:
                  type: boolean
                  description: >-
                    include keywords associated with adult content optional
                    field if set to true, adult keywords will be included in the
                    response default value: false note that the API may return
                    no data for such keywords due to Google Ads restrictions
                sort_by:
                  type: string
                  description: >-
                    results sorting parameters optional field Use these
                    parameters to sort the results by relevance, search_volume,
                    competition_index, low_top_of_page_bid, or
                    high_top_of_page_bid in descending order default value:
                    relevance
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
                    set the necessary values before sending the request example:
                    http://your-server.com/pingscript?id=$id
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
                - target
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
                    description: general informational message
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