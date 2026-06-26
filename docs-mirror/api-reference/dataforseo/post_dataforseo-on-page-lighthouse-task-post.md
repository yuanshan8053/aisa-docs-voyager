> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Lighthouse Tasks

> The OnPage Lighthouse API is based on Google’s open-source Lighthouse project for measuring the quality of web pages and web apps.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/on_page/lighthouse/task_post
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
  /dataforseo/on_page/lighthouse/task_post:
    post:
      summary: Setting Lighthouse Tasks
      description: >-
        The OnPage Lighthouse API is based on Google’s open-source Lighthouse
        project for measuring the quality of web pages and web apps.
      operationId: post_dataforseo_on_page_lighthouse_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  description: >-
                    target URL required field target page should be specified
                    with its absolute URL (including http:// or https://)
                    example: https://dataforseo.com/
                for_mobile:
                  type: boolean
                  description: >-
                    applies mobile emulation optional field if set to true,
                    Lighthouse will use mobile device and screen emulation to
                    test the page against mobile environment if set to false,
                    the results will be provided for desktop default value:
                    false
                categories:
                  type: array
                  items:
                    type: string
                  description: >-
                    categories of Lighthouse audits optional field each category
                    is a collection of audits and audit groups that applies
                    weighting and scoring to the section (see official
                    definition)if you ignore this field, we will return data for
                    all categories unless you specify audits use this field to
                    get data for specific categories you indicate herepossible
                    values: seo, performance, best_practices, accessibility
                audits:
                  type: array
                  items:
                    type: string
                  description: >-
                    Lighthouse audits optional field audits are individual tests
                    Lighthouse runs for each specific
                    feature/optimization/metric to produce a numeric score (see
                    official definition)if you ignore this field, we will return
                    data for all audits use this field to get data for specific
                    audits you indicate herenote that some audits do not belong
                    to a specific category and are stand-alone page quality
                    measurementsin general, there can be several use cases:1. if
                    you ignore categories, you can use this field to get data
                    for the specified audits only for example, if you ignore
                    "categories" and specify "audits":
                    ["metrics/cumulative-layout-shift","metrics/largest-contentful-paint","metrics/total-blocking-time"],
                    you will get data only for these audits2. if you specify a
                    category, you can use this field to additionally receive
                    audits that do not belong to the category(-ies) you
                    specified for example, if you specify "categories": ["seo"]
                    and "audits":
                    ["metrics/cumulative-layout-shift","metrics/largest-contentful-paint","metrics/total-blocking-time"],
                    you will get only these audits under "performance" and all
                    audits under "seo"you can get the full list of possible
                    audits here
                version:
                  type: string
                  description: >-
                    lighthouse version optional field you can obtain the results
                    specific to a certain Lighthouse version by specifying its
                    number the list of available versions is available through
                    the Lighthouse Versions endpoint
                language_name:
                  type: string
                  description: >-
                    lighthouse language name optional field you can receive the
                    list of available languages of the search engine with their
                    language_name by making a separate request to
                    https://api.dataforseo.com/v3/on_page/lighthouse/languages
                    default value: English
                language_code:
                  type: string
                  description: >-
                    lighthouse language code optional field you can receive the
                    list of available languages of the search engine with their
                    language_code by making a separate request to
                    https://api.dataforseo.com/v3/on_page/lighthouse/languages
                    default value: en
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
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
                - url
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