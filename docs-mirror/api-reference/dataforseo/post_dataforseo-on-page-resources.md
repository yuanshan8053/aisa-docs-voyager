> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OnPage API Resources

> This endpoint will provide you with a list of resources, including images, scripts, stylesheets, and broken elements.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/on_page/resources
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
  /dataforseo/on_page/resources:
    post:
      summary: OnPage API Resources
      description: >-
        This endpoint will provide you with a list of resources, including
        images, scripts, stylesheets, and broken elements.
      operationId: post_dataforseo_on_page_resources
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
                url:
                  type: string
                  description: >-
                    page URL optional field specify this field if you want to
                    get the resources for a specific page note that to obtain
                    resource’s meta from a particular URL, you should specify
                    the URL in this field; if you do not indicate a url when
                    setting a task, resource’s meta in the results will be
                    returned based on the data from the page where our crawler
                    first saw the resource
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned resources optional field
                    default value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned resources optional
                    field default value: 0 if you specify the 10 value, the
                    first ten resources in the results array will be omitted and
                    the data will be provided for the successive resources
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
                    ["resource_type","=","stylesheet"]
                    [["resource_type","=","image"],
                    "and",["checks.is_https","=",false]]
                    [["fetch_timing.duration_time",">",1],"and",[["total_transfer_size",">",100],"or",["checks.high_loading_time","=",true]]]
                    The full list of possible filters is available by this link.
                relevant_pages_filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    filter the resources by relevant pages optional field you
                    can use this field to obtain resources from pages matching
                    to the defined parameters you can apply the same filters
                    here as available for the pages endpoint you can add several
                    filters at once (8 filters maximum) you should set a logical
                    operator and, or between the conditions the following
                    operators are supported: regex, not_regex, , , >, >=, =, ,
                    in, not_in, like, not_like you can use the % operator with
                    like and not_like to match any string of zero or more
                    characters example: ["checks.no_image_title","=",true]
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
                    ["size,desc"] note that you can set no more than three
                    sorting rules in a single request you should use a comma to
                    separate several sorting rules example:
                    ["size,desc","fetch_timing.fetch_end,desc"]
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
                    description: total number of relevant items crawled
                  tasks.result.items_count:
                    type: integer
                    description: number of items in the results array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: items array
                  tasks.result.items.resource_type:
                    type: string
                    description: >-
                      type of the returned resource possible types: script,
                      image, stylesheet, broken
                  tasks.result.items.meta:
                    type: object
                    description: >-
                      resource properties the value depends on the resource_type
                      note that if you do not indicate a url when setting a
                      task, resource’s meta is returned based on the data from
                      the page where our crawler first saw the resource; to
                      obtain resource’s meta from a particular url, specify that
                      URL when setting a task
                  tasks.result.items.meta.alternative_text:
                    type: string
                    description: >-
                      content of the image alt attribute the value depends on
                      the resource_type
                  tasks.result.items.meta.title:
                    type: string
                    description: title
                  tasks.result.items.meta.original_width:
                    type: integer
                    description: original image width in px
                  tasks.result.items.meta.original_height:
                    type: integer
                    description: original image height in px
                  tasks.result.items.meta.width:
                    type: integer
                    description: image width in px
                  tasks.result.items.meta.height:
                    type: integer
                    description: image height in px
                  tasks.result.items.status_code:
                    type: integer
                    description: status code of the page where a given resource is located
                  tasks.result.items.location:
                    type: string
                    description: location header indicates the URL to redirect a page to
                  tasks.result.items.url:
                    type: string
                    description: resource URL
                  tasks.result.items.size:
                    type: integer
                    description: >-
                      resource size indicates the size of a given resource
                      measured in bytes
                  tasks.result.items.encoded_size:
                    type: integer
                    description: >-
                      resource size after encoding indicates the size of the
                      encoded resource measured in bytes
                  tasks.result.items.total_transfer_size:
                    type: integer
                    description: >-
                      compressed resource size indicates the compressed size of
                      a given resource in bytes
                  tasks.result.items.fetch_time:
                    type: string
                    description: >-
                      date and time when a resource was fetched in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2021-02-17
                      13:54:15 +00:00
                  tasks.result.items.fetch_timing:
                    type: object
                    description: resource fething time range
                  tasks.result.items.fetch_timing.duration_time:
                    type: integer
                    description: >-
                      indicates how many milliseconds it took to fetch a
                      resource
                  tasks.result.items.fetch_timing.fetch_start:
                    type: integer
                    description: >-
                      time to start downloading the resource the amount of time
                      a browser needs to start downloading a resource
                  tasks.result.items.fetch_timing.fetch_end:
                    type: integer
                    description: >-
                      time to complete downloading the resource the amount of
                      time a browser needs to complete downloading a resource
                  tasks.result.items.cache_control:
                    type: object
                    description: instructions for caching
                  tasks.result.items.cache_control.cachable:
                    type: boolean
                    description: indicates whether the resource is cacheable
                  tasks.result.items.cache_control.ttl:
                    type: integer
                    description: >-
                      time to live the amount of time it takes for the browser
                      to cache a resource; measured in milliseconds
                  tasks.result.items.checks:
                    type: object
                    description: >-
                      resource check-ups contents of the array depend on the
                      resource_type
                  tasks.result.items.checks.no_content_encoding:
                    type: boolean
                    description: >-
                      resource with no content encoding indicates whether a page
                      has no compression algorithm of the content; available for
                      items with the following resource_type: script, image,
                      stylesheet, broken
                  tasks.result.items.checks.high_loading_time:
                    type: boolean
                    description: >-
                      resource with high loading time indicates whether a
                      resource loading time exceeds 3 seconds; available for
                      items with the following resource_type: script, image,
                      stylesheet, broken
                  tasks.result.items.checks.is_redirect:
                    type: boolean
                    description: >-
                      resource with redirects indicates whether a page with this
                      resource has 3XX redirects to other pages; available for
                      items with the following resource_type: script, image,
                      stylesheet, broken
                  tasks.result.items.checks.is_4xx_code:
                    type: boolean
                    description: >-
                      resource with with 4xx status code indicates whether a
                      page with this resource has 4XX response code
                  tasks.result.items.checks.is_5xx_code:
                    type: boolean
                    description: >-
                      resource with 5xx status code indicates whethera page with
                      this resource has 5XX response code
                  tasks.result.items.checks.is_broken:
                    type: boolean
                    description: >-
                      broken resource indicates whether a page with this
                      resource returns 4xx, 5xx response codes or has broken
                      elements inside the resource; available for items with the
                      following resource_type: script, image, stylesheet, broken
                  tasks.result.items.checks.is_www:
                    type: boolean
                    description: >-
                      page with www indicates whether a page with this resource
                      is on a www subdomain; available for items with the
                      following resource_type: script, image, stylesheet, broken
                  tasks.result.items.checks.is_https:
                    type: boolean
                    description: >-
                      page with the https protocol available for items with the
                      following resource_type: script, image, stylesheet, broken
                  tasks.result.items.checks.is_http:
                    type: boolean
                    description: >-
                      page with the http protocol available for items with the
                      following resource_type: script, image, stylesheet, broken
                  tasks.result.items.checks.original_size_displayed:
                    type: boolean
                    description: >-
                      image desplayes in its original size indicates whether the
                      image is displayed in its original size; available for
                      items with the following resource_type: image
                  tasks.result.items.checks.is_minified:
                    type: boolean
                    description: >-
                      resource is minified indicates whether the content of a
                      stylesheet or script is minified; available for items with
                      the following resource_type: stylesheet, script
                  tasks.result.items.checks.has_redirect:
                    type: boolean
                    description: >-
                      resource has a redirect available for items with the
                      following resource_type: script, image; if the
                      resource_type is image, this field will indicate whether
                      other pages and/or resources have redirects pointing at
                      the image; if the resource_type is script, this field will
                      indicate whether the script contains a redirect
                  tasks.result.items.checks.has_subrequests:
                    type: boolean
                    description: >-
                      resource contains subrequests indicates whether the
                      content of a stylesheet or script contain additional
                      requests; available for items with the following
                      resource_type: stylesheet, script
                  tasks.result.items.checks.from_sitemap:
                    type: boolean
                    description: >-
                      resource was found on website’s sitemap if true, the
                      resource was found on the sitemap of the website
                  tasks.result.resource_errors:
                    type: object
                    description: resource errors and warnings
                  tasks.result.resource_errors.errors:
                    type: array
                    items:
                      type: string
                    description: resource errors
                  tasks.result.resource_errors.errors.line:
                    type: integer
                    description: line where the error was found
                  tasks.result.resource_errors.errors.column:
                    type: integer
                    description: column where the error was found
                  tasks.result.resource_errors.errors.message:
                    type: string
                    description: >-
                      text message of the error the full list of possible HTML
                      errors can be found here
                  tasks.result.resource_errors.errors.status_code:
                    type: integer
                    description: >-
                      status code of the error possible values: 0 — Unidentified
                      Error; 501 — Html Parse Error; 1501 — JS Parse Error; 2501
                      — CSS Parse Error; 3501 — Image Parse Error; 3502 — Image
                      Scale Is Zero; 3503 — Image Size Is Zero; 3504 — Image
                      Format Invalid
                  tasks.result.resource_errors.warnings:
                    type: array
                    items:
                      type: string
                    description: resource warnings
                  tasks.result.resource_errors.warnings.line:
                    type: integer
                    description: >-
                      line the warning relates to note that if "line": 0, the
                      warning relates to the whole page
                  tasks.result.resource_errors.warnings.column:
                    type: integer
                    description: >-
                      column the warning relates to note that if "column": 0,
                      the warning relates to the whole page
                  tasks.result.resource_errors.warnings.message:
                    type: string
                    description: >-
                      text message of the warning possible messages: "Has node
                      with more than 60 childs." – HTML page has at least 1 tag
                      nesting over 60 tags of the same level "Has more that 1500
                      nodes." – DOM tree contains over 1,500 elements "HTML
                      depth more than 32 tags." – DOM depth exceeds 32 nodes
                  tasks.result.resource_errors.warnings.status_code:
                    type: integer
                    description: >-
                      status code of the warning possible values: 0 —
                      Unidentified Warning; 1 — Has node with more than 60
                      childs; 2 — Has more that 1500 nodes; 3 — HTML depth more
                      than 32 tags
                  tasks.result.resource_errors.content_encoding:
                    type: string
                    description: type of encoding
                  tasks.result.resource_errors.media_type:
                    type: string
                    description: types of media used to display a resource
                  tasks.result.resource_errors.accept_type:
                    type: string
                    description: >-
                      indicates the expected type of resource for example, if
                      "resource_type": "broken", accept_type will indicate the
                      type of the broken resource possible values: any, none,
                      image, sitemap, robots, script, stylesheet, redirect,
                      html, text, other, font
                  tasks.result.resource_errors.server:
                    type: string
                    description: server version
                  tasks.result.resource_errors.last_modified:
                    type: object
                    description: >-
                      contains data on changes related to the resource if there
                      is no data, the value will be null
                  tasks.result.resource_errors.last_modified.header:
                    type: string
                    description: >-
                      date and time when the header was last modified in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00 if there is no data, the value will be
                      null
                  tasks.result.resource_errors.last_modified.sitemap:
                    type: string
                    description: >-
                      date and time when the sitemap was last modified in the
                      UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2019-11-15 12:57:46 +00:00 if there is no data, the value
                      will be null
                  tasks.result.resource_errors.last_modified.meta_tag:
                    type: string
                    description: >-
                      date and time when the meta tag was last modified in the
                      UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2019-11-15 12:57:46 +00:00 if there is no data, the value
                      will be null
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