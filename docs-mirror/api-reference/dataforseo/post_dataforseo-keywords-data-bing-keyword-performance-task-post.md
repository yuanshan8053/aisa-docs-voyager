> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting ‘Bing Keyword Performance’ Tasks

> You can receive a set of keyword performance stats for a group of keywords depending on the specified match type, location and language parameters.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/keywords_data/bing/keyword_performance/task_post
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
  /dataforseo/keywords_data/bing/keyword_performance/task_post:
    post:
      summary: Setting ‘Bing Keyword Performance’ Tasks
      description: >-
        You can receive a set of keyword performance stats for a group of
        keywords depending on the specified match type, location and language
        parameters. Ad position, clicks, impressions, and other keyword metrics
        are aggregated for the last month for one or all of the following device
        types: mobile, desktop, tablet.
      operationId: post_dataforseo_keywords_data_bing_keyword_performance_task_post
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
                    phrase: 10 the specified keywords will be converted to
                    lowercase, data will be provided in a separate array learn
                    more about rules and limitations of keyword and keywords
                    fields in DataForSEO APIs in this Help Center article
                device:
                  type: string
                  description: >-
                    device type optional field specify this field if you want to
                    get the data for a particular device typepossible values:
                    desktop, mobile, tablet, all default value: all
                match:
                  type: string
                  description: >-
                    keywords match type optional field can take the following
                    values: aggregate returns data across all match types; broad
                    returns data for all user queries containing the specified
                    keyword with varying word order; phrase returns data for all
                    user queries containing the specified keyword with identical
                    word order; exact returns data for user query that matches
                    the specified keyword;Note: the aggregate match type is
                    applied by default
                location_name:
                  type: string
                  description: >-
                    full name of search engine location required field if you
                    don’t specify location_code or location_coordinate if you
                    use this field, you don’t need to specify location_code or
                    location_coordinate you can receive the list of available
                    locations and languages by making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/bing/keyword_performance/locations_and_languages
                    example: "United States"
                location_code:
                  type: integer
                  description: >-
                    search engine location code required field if you don’t
                    specify location_name or location_coordinate if you use this
                    field, you don’t need to specify location_name or
                    location_coordinate you can receive the list of available
                    locations and languages by making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/bing/keyword_performance/locations_and_languages
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
                    need to specify language_code you can receive the list of
                    available locations and languages by making a separate
                    request to
                    https://api.dataforseo.com/v3/keywords_data/bing/keyword_performance/locations_and_languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    search engine language code required field if you don’t
                    specify language_name you can receive the list of available
                    locations and languages by making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/bing/keyword_performance/locations_and_languages
                    example: "en"
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