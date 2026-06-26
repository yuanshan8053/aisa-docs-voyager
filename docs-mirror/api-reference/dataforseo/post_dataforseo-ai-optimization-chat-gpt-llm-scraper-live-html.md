> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live ChatGPT LLM Scraper API HTML

> Live ChatGPT LLM Scraper API HTML provides a raw HTML page of the results for the specified keyword, language, and location.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/ai_optimization/chat_gpt/llm_scraper/live/html
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
  /dataforseo/ai_optimization/chat_gpt/llm_scraper/live/html:
    post:
      summary: Live ChatGPT LLM Scraper API HTML
      description: >-
        Live ChatGPT LLM Scraper API HTML provides a raw HTML page of the
        results for the specified keyword, language, and location.
      operationId: post_dataforseo_ai_optimization_chat_gpt_llm_scraper_live_html
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
                location_name:
                  type: string
                  description: >-
                    full name of search engine location required field if you
                    don't specify location_code if you use this field, you don't
                    need to specify location_code you can receive the list of
                    available locations of the search engine with their
                    location_name by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/{{low_se_name}}/locations
                    example: United States
                location_code:
                  type: integer
                  description: >-
                    search engine location code required field if you don't
                    specify location_name if you use this field, you don't need
                    to specify location_name you can receive the list of
                    available locations of the search engines with their
                    location_code by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/{{low_se_name}}/{{low_se_type}}/locations
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of search engine language required field if you
                    don't specify language_code if you use this field, you don't
                    need to specify language_code you can receive the list of
                    available languages of the search engine with their
                    language_name by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/{{low_se_name}}/{{low_se_type}}/languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    search engine language code required field if you don't
                    specify language_name if you use this field, you don't need
                    to specify language_name you can receive the list of
                    available languages of the search engine with their
                    language_code_by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/{{low_se_name}}/{{low_se_type}}/languages
                    example:enn
                force_web_search:
                  type: boolean
                  description: >-
                    force AI agent to use web search optional field when
                    enabled, the AI model is forced to access and cite current
                    web information; default value: false; Note: even if the
                    parameter is set to true, there is no guarantee web sources
                    will be cited in the response
                expand_citations:
                  type: boolean
                  description: >-
                    return expanded citation bar in HTML results optional field
                    to enable this parameter, force_web_search must also be
                    enabled; when enabled, the endpoint will return HTML data
                    from the expanded citation bar; default value: false
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - keyword
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
                  tasks.result.keyword:
                    type: string
                    description: >-
                      keyword received in a POST array keyword is returned with
                      decoded %## (plus character '+' will be decoded to a space
                      character)
                  tasks.result.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.language_code:
                    type: string
                    description: language code in a POST array
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
                    description: elements of search results found
                  tasks.result.items.page:
                    type: integer
                    description: serial number of the returned HTML page
                  tasks.result.items.date:
                    type: string
                    description: >-
                      date and time when the HTML page was scanned in the
                      format:
                      “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”
                      example: 2019-11-15 12:57:46 +00:00
                  tasks.result.items.html:
                    type: string
                    description: HTML page
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