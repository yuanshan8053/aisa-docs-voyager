> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Apple App Searches Tasks

> This endpoint will provide you with a list of apps ranking on the App Store for the specified `keyword`.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/app_data/apple/app_searches/task_post
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
  /dataforseo/app_data/apple/app_searches/task_post:
    post:
      summary: Setting Apple App Searches Tasks
      description: >-
        This endpoint will provide you with a list of apps ranking on the App
        Store for the specified `keyword`. The returned results are specific to
        the indicated keyword, as well as the location and language parameters.
      operationId: post_dataforseo_app_data_apple_app_searches_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                keyword:
                  type: string
                  description: >-
                    keyword required field you can specify up to 700 characters
                    in the keyword field; all %## will be decoded (plus
                    character ‘+’ will be decoded to a space character); if you
                    need to use the “%” character for your keyword, please
                    specify it as “%25”; if you need to use the “+” character
                    for your keyword, please specify it as “%2B” learn more
                    about rules and limitations of keyword and keywords fields
                    in DataForSEO APIs in this Help Center article
                location_name:
                  type: string
                  description: >-
                    full name of search engine location required field if you
                    don’t specify location_code if you use this field, you don’t
                    need to specify location_code you can receive the list of
                    available locations of the search engine with their
                    location_name by making a separate request to
                    https://api.dataforseo.com/v3/app_data/apple/locations
                    example: West Los Angeles,California,United States
                location_code:
                  type: integer
                  description: >-
                    search engine location code required field if you don’t
                    specify location_name if you use this field, you don’t need
                    to specify location_name you can receive the list of
                    available locations of the search engine with their
                    location_code by making a separate request to
                    https://api.dataforseo.com/v3/app_data/apple/locations
                    example: 9061121
                language_name:
                  type: string
                  description: >-
                    full name of search engine language required field if
                    language_code is not specified if you use this field, you
                    don’t need to specify language_code you can receive the list
                    of available languages with language_name by making a
                    separate request to
                    https://api.dataforseo.com/v3/app_data/apple/languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    search engine language code required field if language_name
                    is not specified if you use this field, you don’t need to
                    specify language_name you can receive the list of available
                    languages with their language_code by making a separate
                    request to
                    https://api.dataforseo.com/v3/app_data/apple/languages
                    example: en
                priority:
                  type: integer
                  description: >-
                    task priority optional field can take the following values:
                    1 – normal execution priority (set by default) 2 – high
                    execution priority You will be additionally charged for the
                    tasks with high execution priority. The cost can be
                    calculated on the Pricing page.
                depth:
                  type: integer
                  description: >-
                    parsing depth optional field number of results to be
                    returned from the App Store SERP; we strongly recommend
                    setting the parsing depth in the multiples of 100, because
                    our system processes 100 results in a row; default value:
                    100 maximum value: 700 Your account will be billed per each
                    SERP containing up to 100 results; Setting depth above 100
                    may result in additional charges if the search engine
                    returns more than 100 results; The cost can be calculated on
                    the Pricing page.
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
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
                postback_data:
                  type: string
                  description: >-
                    postback_url datatype required field if you specify
                    postback_url corresponds to the datatype that will be sent
                    to your server possible values: advanced
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
              required:
                - keyword
                - location_name
                - location_code
                - language_name
                - language_code
                - postback_data
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
                      within the following range: 10000-60000
                  tasks.status_message:
                    type: string
                    description: informational message of the task
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