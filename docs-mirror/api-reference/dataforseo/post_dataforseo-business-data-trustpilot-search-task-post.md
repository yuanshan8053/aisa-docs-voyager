> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Business Data Trustpilot Search Tasks

> This endpoint provides a list of business profiles listed on the [Trustpilot](https://www.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/business_data/trustpilot/search/task_post
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
  /dataforseo/business_data/trustpilot/search/task_post:
    post:
      summary: Setting Business Data Trustpilot Search Tasks
      description: >-
        This endpoint provides a list of business profiles listed on the
        [Trustpilot](https://www.trustpilot.com) platform. The returned results
        are relevant to the specified `keyword`.
      operationId: post_dataforseo_business_data_trustpilot_search_task_post
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
                    *keyword* **required field** the keyword you specify should
                    indicate a business category or company name; you can
                    specify up to 700 characters in the `keyword` filed; all %##
                    will be decoded (plus character ‘+’ will be decoded to a
                    space character); if you need to use the “%” character for
                    your `keyword`, please specify it as “%25” learn more about
                    rules and limitations of `keyword` and `keywords` fields in
                    DataForSEO APIs in this [Help Center
                    article](https://dataforseo.com/help-center/rules-and-limitations-of-keyword-and-keywords-fields-in-dataforseo-apis)
                priority:
                  type: integer
                  description: >-
                    *task priority* optional field can take the following
                    values: 1 – normal execution priority (set by default) 2 –
                    high execution priority You will be additionally charged for
                    the tasks with high execution priority. The cost can be
                    calculated on the
                    [Pricing](https://dataforseo.com/pricing/business-data/business-data-api-trustpilot-search-pricing
                    "Pricing") page.
                depth:
                  type: integer
                  description: >-
                    *parsing depth* optional field number of search results to
                    be returned from the API response we strongly recommend
                    setting the parsing depth in the multiples of twenty because
                    our systems processes twenty search results in a row;
                    default value: `10`; maximum value: `140` **Your account
                    will be billed per each SERP containing up to 10 results;**
                    Setting depth above 10 may result in additional charges if
                    the search engine returns more than 10 results; The cost can
                    be calculated on the
                    [Pricing](https://dataforseo.com/pricing/business-data/business-data-api-trustpilot-search-pricing
                    "Pricing") page.
                tag:
                  type: string
                  description: >-
                    *user-defined task identifier* optional field *the character
                    limit is 255* you can use this parameter to identify the
                    task and match it with the result you will find the
                    specified `tag` value in the `data` object of the response
                postback_url:
                  type: string
                  description: >-
                    *return URL for sending task results* optional field once
                    the task is completed, we will send a POST request with its
                    results compressed in the `gzip` format to the
                    `postback_url` you specified you can use the ‘$id’ string as
                    a `$id` variable and ‘$tag’ as urlencoded `$tag` variable.
                    We will set the necessary values before sending the request.
                    example: `http://your-server.com/postbackscript?id=$id`
                    `http://your-server.com/postbackscript?id=$id&tag=$tag`
                    **Note:** special characters in `postback_url` will be
                    urlencoded; i.a., the `#` character will be encoded into
                    `%23`learn more on our [Help
                    Center](https://dataforseo.com/help-center/pingbacks-postbacks-with-dataforseo-api)
                pingback_url:
                  type: string
                  description: >-
                    *notification URL of a completed task* optional field when a
                    task is completed we will notify you by GET request sent to
                    the URL you have specified you can use the ‘$id’ string as a
                    `$id` variable and ‘$tag’ as urlencoded `$tag` variable. We
                    will set the necessary values before sending the request.
                    example: `http://your-server.com/pingscript?id=$id`
                    `http://your-server.com/pingscript?id=$id&tag=$tag`
                    **Note:** special characters in `pingback_url` will be
                    urlencoded; i.a., the `#` character will be encoded into
                    `%23`learn more on our [Help
                    Center](https://dataforseo.com/help-center/pingbacks-postbacks-with-dataforseo-api)
              required:
                - keyword
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
                    description: '*the current version of the API*'
                  version.status_code:
                    type: integer
                    description: >-
                      *general status code* you can find the full list of the
                      response codes
                      [here](https://docs.dataforseo.com/v3/appendix/errors.md)
                      **Note:** we strongly recommend designing a necessary
                      system for handling related exceptional or error
                      conditions
                  version.status_message:
                    type: string
                    description: >-
                      *general informational message* you can find the full list
                      of general informational messages
                      [here](https://docs.dataforseo.com/v3/appendix/errors.md)
                  version.time:
                    type: string
                    description: '*execution time, seconds*'
                  version.cost:
                    type: number
                    description: '*total tasks cost, USD*'
                  version.tasks_count:
                    type: integer
                    description: '*the number of tasks in the **`tasks`**array*'
                  version.tasks_error:
                    type: integer
                    description: >-
                      *the number of tasks in the **`tasks`** array returned
                      with an error*
                  tasks:
                    type: array
                    items:
                      type: string
                    description: '*array of tasks*'
                  tasks.id:
                    type: string
                    description: >-
                      *unique task identifier in our system* in the [Universally
                      unique identifier
                      (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier)
                      format
                  tasks.status_code:
                    type: integer
                    description: >-
                      *status code of the task* generated by DataForSEO; can be
                      within the following range: 10000-60000
                  tasks.status_message:
                    type: string
                    description: '*informational message of the task*'
                  tasks.time:
                    type: string
                    description: '*execution time, seconds*'
                  tasks.cost:
                    type: number
                    description: '*cost of the task, USD*'
                  tasks.result_count:
                    type: integer
                    description: '*number of elements in the `result` array*'
                  tasks.path:
                    type: array
                    items:
                      type: string
                    description: '*URL path*'
                  tasks.data:
                    type: object
                    description: >-
                      *contains the same parameters that you specified in the
                      POST request*
                  result:
                    type: array
                    items:
                      type: string
                    description: '*array of results* in this case, the value will be `null`'
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