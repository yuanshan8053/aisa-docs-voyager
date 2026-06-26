> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Competitors

> This endpoint will provide you with a list of competitors that share some part of the backlink profile with a target website, along with a number of backlink...



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/backlinks/competitors/live
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
  /dataforseo/backlinks/competitors/live:
    post:
      summary: Competitors
      description: >-
        This endpoint will provide you with a list of competitors that share
        some part of the backlink profile with a target website, along with a
        number of backlink intersections and the rank of every competing
        website.
      operationId: post_dataforseo_backlinks_competitors_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                target:
                  type: string
                  description: >-
                    domain, subdomain or webpage to get competitor domains for
                    required field a domain or a subdomain should be specified
                    without https:// and www. a page should be specified with
                    absolute URL (including http:// or https://)
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned domains optional field
                    default value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned domains optional
                    field default value: 0 if you specify the 10 value, the
                    first ten domains in the results array will be omitted and
                    the data will be provided for the successive pages
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: regex, not_regex, =, ,
                    in, not_in, like, not_like, ilike, not_ilike, match,
                    not_match you can use the % operator with like and not_like
                    to match any string of zero or more characters example:
                    ["rank",">","100"] [["target","like","%forbes%"], "and",
                    [["rank",">","100"],"or",["intersections",">","5"]]] The
                    full list of possible filters is available here.
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
                    ["rank,desc"] note that you can set no more than three
                    sorting rules in a single request you should use a comma to
                    separate several sorting rules example:
                    ["intersections,desc","rank,asc"]
                main_domain:
                  type: boolean
                  description: >-
                    indicates if only main domain of the target will be included
                    in the search optional field if set to true, only the main
                    domain will be included in search; default value: true
                exclude_large_domains:
                  type: boolean
                  description: >-
                    indicates whether large domain will appear in results
                    optional field if set to true, the results from the large
                    domain (google.com, amazon.com, etc.) will be omitted;
                    default value: true
                exclude_internal_backlinks:
                  type: boolean
                  description: >-
                    indicates if internal backlinks from subdomains to the
                    target will be excluded from the results optional field if
                    set to true, the results will not include data on internal
                    backlinks from subdomains of the same domain as target if
                    set to false, internal links will be included in the results
                    default value: true
                rank_scale:
                  type: string
                  description: >-
                    defines the scale used for calculating and displaying the
                    rank, domain_from_rank, and page_from_rank values optional
                    field you can use this parameter to choose whether rank
                    values are presented on a 0–100 or 0–1000 scale possible
                    values: one_hundred — rank values are displayed on a 0–100
                    scale one_thousand — rank values are displayed on a 0–1000
                    scale default value: one_thousand learn more about how this
                    parameter works and how ranking metrics are calculated in
                    this Help Center article
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - target
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
                  tasks.result.total_count:
                    type: integer
                    description: total number of relevant items in the database
                  tasks.result.items_count:
                    type: integer
                    description: number of items in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: items array
                  tasks.result.items.type:
                    type: string
                    description: type of element = ‘backlinks_competitors’
                  tasks.result.items.target:
                    type: string
                    description: competitor domain
                  tasks.result.items.rank:
                    type: integer
                    description: >-
                      domain rank domain rank across all domains in the database
                      rank is calculated based on the method for node ranking in
                      a linked database – a principle used in the original
                      Google PageRank algorithm learn more about the metric and
                      how it is calculated in this help center article
                  tasks.result.items.intersections:
                    type: integer
                    description: >-
                      indicates the number of backlink intersections with the
                      target specified in the POST array
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