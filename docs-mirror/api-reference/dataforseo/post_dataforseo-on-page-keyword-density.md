> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Keyword Density

> This endpoint will provide you with keyword density and keyword frequency data for terms appearing on the specified website or web page.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/on_page/keyword_density
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
  /dataforseo/on_page/keyword_density:
    post:
      summary: Keyword Density
      description: >-
        This endpoint will provide you with keyword density and keyword
        frequency data for terms appearing on the specified website or web page.
        You can filter and sort the data that will be retrieved with this API
        call.
      operationId: post_dataforseo_on_page_keyword_density
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: >-
                    ID of the task required field you can get this ID in the
                    response of the Task POST endpoint example:
                    “07131248-1535-0216-1000-17384017ad04”
                keyword_length:
                  type: integer
                  description: >-
                    number of words for a keyword required field possible
                    values: 1, 2, 3, 4, 5
                url:
                  type: string
                  description: >-
                    page URL optional field if you do not specify a page here,
                    the results will be provided for the whole website if you
                    use this field, the API response will contain only keywords
                    from the specified page a page should be specified with
                    absolute URL (including http:// or https://)
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned keywords optional field
                    default value: 100 maximum value: 1000
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: regex, not_regex, =, ,
                    in, not_in, like, not_like you can use the % operator with
                    like and not_like to match any string of zero or more
                    characters example: ["keyword","=","%seo%"]
                    [["keyword","=","%seo%"], "and", ["frequency","
                    [["keyword","not_like","%seo%"], "and",
                    [["frequency",">","6"],"or",["density",">","0.02"]]] The
                    full list of possible filters is available by this link.
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    results sorting rules optional field you can use the same
                    values as in the filters array to sort the results possible
                    sorting types: asc – results will be sorted in the ascending
                    order desc – results will be sorted in the descending order
                    you should use a comma to set up a sorting type example:
                    ["frequency,desc"] note that you can set no more than three
                    sorting rules in a single request you should use a comma to
                    separate several sorting rules example:
                    ["keyword,asc","frequency,desc"]
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - id
                - keyword_length
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
                  tasks.result.crawl_progress:
                    type: string
                    description: >-
                      status of the crawling session possible values:
                      in_progress, finished
                  tasks.result.crawl_status:
                    type: object
                    description: details of the crawling session
                  tasks.result.crawl_status.max_crawl_pages:
                    type: integer
                    description: >-
                      maximum number of pages to crawl indicates the
                      max_crawl_pages limit you specified when setting a task
                  tasks.result.crawl_status.pages_in_queue:
                    type: integer
                    description: number of pages that are currently in the crawling queue
                  tasks.result.crawl_status.pages_crawled:
                    type: integer
                    description: number of crawled pages
                  tasks.result.total_items_count:
                    type: integer
                    description: >-
                      total number of relevant items total number of keywords on
                      the specified website or web page matching the set
                      keyword_length and filters
                  tasks.result.items_count:
                    type: integer
                    description: number of items in the results array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: items array
                  tasks.result.items.keyword:
                    type: string
                    description: returned keyword
                  tasks.result.items.frequency:
                    type: integer
                    description: >-
                      keyword frequency number of times the keyword appears on
                      the website (or webpage if you specified a url)
                  tasks.result.items.density:
                    type: integer
                    description: >-
                      keyword density calculated as a ratio of frequency to the
                      total count of keywords with the set keyword_length on the
                      web page or website
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