> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Uncrawlable Resources

> This endpoint returns a list of resources detected on the target website that could not be crawled due to a content type inconsistency.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/on_page/uncrawlable_resources
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
  /dataforseo/on_page/uncrawlable_resources:
    post:
      summary: Uncrawlable Resources
      description: >-
        This endpoint returns a list of resources detected on the target website
        that could not be crawled due to a content type inconsistency. A
        resource is considered uncrawlable when the content type returned in the
        server response does not match the content type expected based on how
        the resource is referenced in the page HTML.
      operationId: post_dataforseo_on_page_uncrawlable_resources
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
                    "07131248-1535-0216-1000-17384017ad04"
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned uncrawlable resources
                    optional field default value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned uncrawlable
                    resources optional field default value: 0 if you specify the
                    10 value, the first ten invalid resources in the results
                    array will be omitted and the data will be provided for the
                    successive invalid resources
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    results sorting rules optional field you can use the same
                    values as in the filters array to sort the results possible
                    sorting types: asc - results will be sorted in the ascending
                    order desc - results will be sorted in the descending order
                    you should use a comma to set up a sorting type example:
                    ["meta.content_type,desc"] note that you can set no more
                    than three sorting rules in a single request you should use
                    a comma to separate several sorting rules example:
                    ["meta.content_type,asc","fetch_time,desc"]
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: regex, not_regex, , , >,
                    >=, =, , in, not_in, like, not_like you can use the %
                    operator with like and not_like to match any string of zero
                    or more characters example:
                    [["meta.content_type","=","image/jpeg"], "and",
                    ["url","not_like","%/help-center/%"]]The full list of
                    possible filters is available by this link.
              required:
                - id
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
                      total number of uncrawlable resources found total number
                      of uncrawlable resources found during the crawl of the
                      target domain
                  tasks.result.items_count:
                    type: integer
                    description: number of uncrawlable resources in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: array of uncrawlable resources
                  tasks.result.items.url:
                    type: string
                    description: URL of the uncrawlable resource
                  tasks.result.items.reason:
                    type: string
                    description: >-
                      reason the resource is uncrawlable can take the following
                      values: content_type_inconsistency
                  tasks.result.items.status_code:
                    type: integer
                    description: >-
                      HTTP response code returned by the uncrawlable resource
                      possible values: 200
                  tasks.result.items.fetch_time:
                    type: string
                    description: >-
                      date and time when the resource was fetched in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2026-03-09
                      18:20:32 +00:00
                  tasks.result.items.meta:
                    type: object
                    description: metadata of the uncrawlable resource
                  tasks.result.items.meta.content_type:
                    type: string
                    description: actual content type of the resource
                  tasks.result.items.meta.expected_content_types:
                    type: array
                    items:
                      type: string
                    description: >-
                      expected content types for the resource list of content
                      types that were expected by the crawler based on how the
                      resource is referenced on the page
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