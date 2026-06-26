> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Gemini LLM Scraper

> Gemini LLM Scraper API provides structured results from Gemini.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/ai_optimization/gemini/llm_scraper/task_post
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
  /dataforseo/ai_optimization/gemini/llm_scraper/task_post:
    post:
      summary: Setting Gemini LLM Scraper
      description: >-
        Gemini LLM Scraper API provides structured results from Gemini. The
        results are specific to the selected location (see [the List of
        Locations](https://docs.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/locations.md))
        and language (see [the List of
        Languages](https://docs.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/languages.md)),
        and keyword.
      operationId: post_dataforseo_ai_optimization_gemini_llm_scraper_task_post
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
                    keyword required field you can specify up to 2000 characters
                    in the keyword field all %## will be decoded (plus character
                    ‘+’ will be decoded to a space character) if you need to use
                    the “%” character for your keyword, please specify it as
                    “%25”; if you need to use the “+” character for your
                    keyword, please specify it as “%2B”learn more about rules
                    and limitations of keyword and keywords fields in DataForSEO
                    APIs in this Help Center article
                priority:
                  type: integer
                  description: >-
                    task priority optional field can take the following values:
                    1 – normal execution priority (set by default) 2 – high
                    execution priorityYou will be additionally charged for the
                    tasks with high execution priority. The cost can be
                    calculated on the Pricing page.
                location_name:
                  type: string
                  description: >-
                    full name of search engine location required field if you
                    don't specify location_code if you use this field, you don't
                    need to specify location_code you can receive the list of
                    available locations of the search engine with their
                    location_name by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/locations
                    example: United States
                location_code:
                  type: integer
                  description: >-
                    search engine location code required field if you don't
                    specify location_name if you use this field, you don't need
                    to specify location_name you can receive the list of
                    available locations of the search engines with their
                    location_code by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/locations
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of search engine language required field if you
                    don't specify language_code; if you use this field, you
                    don't need to specify language_code; you can receive the
                    list of available languages of the search engine with their
                    language_name by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    search engine language code required field if you don't
                    specify language_name; if you use this field, you don't need
                    to specify language_name; you can receive the list of
                    available languages of the search engine with their
                    language_code_by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/languages
                    example: en
                expand_citations:
                  type: boolean
                  description: >-
                    return expanded citation bar in HTML results optional field
                    when enabled, the HTML endpoint will return data from the
                    expanded citation bar; default value: false
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
                    the # character will be encoded into %23learn more on our
                    Help Center
                postback_data:
                  type: string
                  description: >-
                    postback_url datatype required field if you specify
                    postback_url corresponds to the function you used for
                    setting a task possible values: advanced, html
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
                    the # character will be encoded into %23learn more on our
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