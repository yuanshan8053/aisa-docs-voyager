> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Links

> This endpoint will provide you with a list of internal and external links detected on a target website.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/on_page/links
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
  /dataforseo/on_page/links:
    post:
      summary: Links
      description: >-
        This endpoint will provide you with a list of internal and external
        links detected on a target website.
      operationId: post_dataforseo_on_page_links
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
                page_from:
                  type: string
                  description: >-
                    relative page URL optional field if you use this field, the
                    API response will contain only links from the specified page
                    note that in this field you can specify relative URLs only
                page_to:
                  type: string
                  description: >-
                    relative page URL optional field if you use this field, the
                    API response will contain only internal links pointing to
                    the specified page note that in this field you can specify
                    relative URLs only
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned links optional field default
                    value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned links optional field
                    default value: 0 if you specify the 10 value, the first ten
                    links in the results array will be omitted and the data will
                    be provided for the successive links
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
                    characters example: ["direction","=","external"]
                    [["domain_to","","example.com"], "and",
                    ["link_from","not_like","%example.com/blog%"]]
                    [["direction","=","external"], "and",
                    [["link_from","like","%example.com/blog%"],"or",["link_from","like","%example.com/help%"]]]
                    The full list of possible filters is available by this link.
                search_after_token:
                  type: string
                  description: >-
                    token for subsequent requests optional field provided in the
                    identical filed of the response to each request; use this
                    parameter to avoid timeouts while trying to obtain over
                    20,000 results in a single request; by specifying the unique
                    search_after_token value from the response array, you will
                    get the subsequent results of the initial task;
                    search_after_token values are unique for each subsequent
                    task ; Note: if the search_after_token is specified in the
                    request, all other parameters should be identical to the
                    previous request
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
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
                    description: total number of relevant items in the database
                  tasks.result.items_count:
                    type: integer
                    description: number of items in the results array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: items array
                  tasks.result.items.type:
                    type: string
                    description: >-
                      type of the link = ‘redirect’ HTTP redirect with 3xx
                      status code
                  tasks.result.items.domain_from:
                    type: string
                    description: referring domain the link was found on this domain
                  tasks.result.items.domain_to:
                    type: string
                    description: referenced domain the link is pointing to this domain
                  tasks.result.items.page_from:
                    type: string
                    description: >-
                      referring page relative URL of the page on which the link
                      was found
                  tasks.result.items.page_to:
                    type: string
                    description: >-
                      referenced page relative URL of the page to which the link
                      is pointing
                  tasks.result.items.link_from:
                    type: string
                    description: >-
                      referring page absolute URL of the page on which the link
                      was found
                  tasks.result.items.link_to:
                    type: string
                    description: >-
                      referenced page absolute URL of the page to which the link
                      is pointing
                  tasks.result.items.link_attribute:
                    type: array
                    items:
                      type: string
                    description: >-
                      link attribute added to external link indicates link
                      attributes added to the link_to on the page_from
                      ["ugc","noopener"]
                  tasks.result.items.dofollow:
                    type: boolean
                    description: >-
                      indicates whether the link is dofollow if the value is
                      true, the link doesn’t have a rel="nofollow" attribute
                  tasks.result.items.page_from_scheme:
                    type: string
                    description: url scheme of the referring page
                  tasks.result.items.page_to_scheme:
                    type: string
                    description: url scheme of the referenced page
                  tasks.result.items.direction:
                    type: string
                    description: 'direction of the link possible values: internal, external'
                  tasks.result.items.is_broken:
                    type: boolean
                    description: >-
                      link is broken indicates whether a link is directing to a
                      broken page or resource
                  tasks.result.items.text:
                    type: string
                    description: image text
                  tasks.result.items.is_link_relation_conflict:
                    type: boolean
                    description: >-
                      indicates that the link may have a conflict with another
                      link if true, at least one link pointing to link_to has a
                      rel="nofollow" attribute and at least one is dofollow
                  tasks.result.items.page_to_status_code:
                    type: integer
                    description: >-
                      status code of the referenced page status code of the page
                      to which the link is pointing
                  tasks.result.items.image_alt:
                    type: string
                    description: alternative text for the image
                  tasks.result.items.image_src:
                    type: string
                    description: url of the image
                  tasks.result.items.is_valid_hreflang:
                    type: boolean
                    description: >-
                      hreflang validity status indicates whether the hreflang
                      attribute is correctly implemented
                  tasks.result.items.hreflang:
                    type: string
                    description: >-
                      hreflang attribute value language and optional country
                      code specified in the hreflang attribute example: "en-US",
                      "fr"
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