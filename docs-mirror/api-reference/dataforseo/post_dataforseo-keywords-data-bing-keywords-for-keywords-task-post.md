> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting ‘Keywords For Keywords’ Tasks

> This endpoint will select relevant keywords for the specified terms.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/keywords_data/bing/keywords_for_keywords/task_post
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
  /dataforseo/keywords_data/bing/keywords_for_keywords/task_post:
    post:
      summary: Setting ‘Keywords For Keywords’ Tasks
      description: >-
        This endpoint will select relevant keywords for the specified terms. Set
        up to 200 keywords and get the results, which are suggested by Bing Ads
        for your query. You can get up to 3000 keyword suggestions using this
        function.
      operationId: post_dataforseo_keywords_data_bing_keywords_for_keywords_task_post
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
                    keywords required field you can specify the maximum of 200
                    keywords with each keyword containing no more than 100
                    characters; the specified keywords will be converted to
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
                sort_by:
                  type: string
                  description: >-
                    results sorting parameters optional field Use these
                    parameters to sort the results by search_volume, cpc,
                    competition or relevance in the descending order default
                    value: relevance
                keywords_negative:
                  type: array
                  items:
                    type: string
                  description: >-
                    keywords negative array optional field These keywords will
                    be ignored in the results array; You can specify a maximum
                    of 200 terms that you want to exclude from the results; the
                    specified keywords will be converted to lowercase format
                device:
                  type: string
                  description: >-
                    device type optional field specify this field if you want to
                    get the data for a particular device type; possible values:
                    all, mobile, desktop, tablet default value: all
                date_from:
                  type: string
                  description: >-
                    starting date of the time range optional field minimal
                    value: 24 months from today’s date; if you don’t specify
                    this field, data will be provided for the last 12 months
                    date format: "yyyy-mm-dd" example: "2020-01-01" Note: we do
                    not recommend using a custom time range for the past year’s
                    dates
                date_to:
                  type: string
                  description: >-
                    ending date of the time range optional field if you don’t
                    specify this field, data will be provided for the last 12
                    months; minimum value: two years back from today’s date;
                    maximum value: one month from today’s date; date format:
                    "yyyy-mm-dd" example: "2020-03-15" Note: we do not recommend
                    using a custom time range for the past year’s dates
                search_partners:
                  type: boolean
                  description: >-
                    Bing search partners type optional field if you specify
                    true, the results will be delivered for owned, operated, and
                    syndicated networks across Bing, Yahoo, AOL and partner
                    sites that host Bing, AOL, and Yahoo search. default value:
                    false – results are returned for Bing, AOL, and Yahoo search
                    networks
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