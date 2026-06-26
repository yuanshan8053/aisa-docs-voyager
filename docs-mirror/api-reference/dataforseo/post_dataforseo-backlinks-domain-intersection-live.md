> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Domain Intersection

> This endpoint will provide you with the list of domains pointing to the specified websites.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/backlinks/domain_intersection/live
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
  /dataforseo/backlinks/domain_intersection/live:
    post:
      summary: Domain Intersection
      description: >-
        This endpoint will provide you with the list of domains pointing to the
        specified websites. This endpoint is especially useful for creating a
        Link Gap feature that shows what domains link to your competitors but do
        not link out to your website.
      operationId: post_dataforseo_backlinks_domain_intersection_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                targets:
                  type: object
                  description: >-
                    domains, subdomains or webpages to get links for required
                    field you can set up to 20 domains, subdomains or webpages a
                    domain or a subdomain should be specified without https://
                    and www. a page should be specified with absolute URL
                    (including http:// or https://) example: "targets": { "1":
                    "http://planet.postgresql.org/", "2":
                    "http://gborg.postgresql.org/" }
                exclude_targets:
                  type: array
                  items:
                    type: string
                  description: >-
                    domains, subdomains or webpages you want to exclude optional
                    field you can specify up to 10 domains, subdomains or
                    webpages if you use this array, results will contain the
                    referring domains that link to targets but don’t link to
                    exclude_targets example: "exclude_targets": [ "bbc.com",
                    "https://www.apple.com/iphone/*",
                    "https://dataforseo.com/apis/*"]
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
                    ["1.internal_links_count",">","1"]
                    [["2.referring_pages",">","2"], "and",
                    ["1.backlinks",">","10"]] [["1.first_seen",">","2017-10-23
                    11:31:45 +00:00"], "and",
                    [["2.target","like","%dataforseo.com%"],"or",["1.referring_domains",">","10"]]]
                    The full list of possible filters is available here.
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
                    ["backlinks,desc"] note that you can set no more than three
                    sorting rules in a single request you should use a comma to
                    separate several sorting rules example:
                    ["backlinks,desc","rank,asc"]
                offset:
                  type: integer
                  description: >-
                    offset in the array of returned results optional field
                    default value: 0 if you specify the 10 value, the first ten
                    backlinks in the results array will be omitted and the data
                    will be provided for the successive backlinks
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned results optional field
                    default value: 100 maximum value: 1000
                internal_list_limit:
                  type: integer
                  description: >-
                    maximum number of elements within internal arrays optional
                    field you can use this field to limit the number of elements
                    within the following arrays: referring_links_tld
                    referring_links_types referring_links_attributes
                    referring_links_platform_types
                    referring_links_semantic_locations default value: 10 maximum
                    value: 1000
                backlinks_status_type:
                  type: string
                  description: >-
                    set what backlinks to return and count optional field you
                    can use this field to choose what backlinks will be returned
                    and used for aggregated metrics for your targets; possible
                    values: all – all backlinks will be returned and counted;
                    live – backlinks found during the last check will be
                    returned and counted; lost – lost backlinks will be returned
                    and counted; default value: live
                backlinks_filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    filter the backlinks of your target optional field you can
                    use this field to filter the initial backlinks that will be
                    included in the dataset for aggregated metrics for your
                    target you can filter the backlinks by all fields available
                    in the response of this endpoint using this parameter, you
                    can include only dofollow backlinks in the response and
                    create a flexible backlinks dataset to calculate the metrics
                    for example: "backlinks_filters": [["dofollow", "=", true]]
                include_subdomains:
                  type: boolean
                  description: >-
                    indicates if the subdomains of the target will be included
                    in the search optional field if set to false, the subdomains
                    will be ignored default value: true
                include_indirect_links:
                  type: boolean
                  description: >-
                    indicates if indirect links to the targets will be included
                    in the results optional field if set to true, the results
                    will include data on indirect links pointing to a page that
                    either redirects to a target, or points to a canonical page
                    if set to false, indirect links will be ignored default
                    value: true
                exclude_internal_backlinks:
                  type: boolean
                  description: >-
                    indicates whether the backlinks from subdomains of the
                    target are excluded optional field if set to false, the
                    backlinks from subdomains of the target will be omitted and
                    you won’t receive the same domain in the response; default
                    value: true
                intersection_mode:
                  type: string
                  description: >-
                    indicates whether to intersect backlinks optional field use
                    this field to intersect or merge results for the specified
                    domains possible values: all, partial all – results are
                    based on all backlinks; partial – results are based on the
                    intersecting backlinks only; default value: all
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
                - targets
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
                  tasks.result.targets:
                    type: object
                    description: target domains, subdomains or webpages in a POST array
                  tasks.result.total_count:
                    type: integer
                    description: total amount of results relevant to your request
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains domain that link to all targets from the POST
                      array
                  tasks.result.items.domain_intersection:
                    type: object
                    description: >-
                      contains data on domains that link to the corresponding
                      targets specified in the POST array data is provided in
                      separate objects corresponding to domains, subdomains or
                      pages specified in the targets object
                  tasks.result.items.1:
                    type: object
                    description: >-
                      contains data on a domain that links to the corresponding
                      target from the POST array field name varies in the range
                      from 1 to 20 according to the number of domains,
                      subdomains, or pages in the targets object
                  tasks.result.items.1.type:
                    type: string
                    description: type of element = ‘backlinks_domain_intersection’
                  tasks.result.items.1.target:
                    type: string
                    description: >-
                      domain that links to the corresponding target from the
                      POST array
                  tasks.result.items.1.rank:
                    type: integer
                    description: >-
                      rank referred to the target from the POST array indicates
                      the rank that the referring domain (target above) refers
                      to your target from the POST array; rank is calculated
                      based on the method for node ranking in a linked database
                      – a principle used in the original Google PageRank
                      algorithm learn more about the metric and how it is
                      calculated in this help center article
                  tasks.result.items.1.backlinks:
                    type: integer
                    description: indicates the number of backlinks
                  tasks.result.items.1.first_seen:
                    type: string
                    description: >-
                      date and time when our crawler found the backlink from
                      this target for the first time in the UTC format:
                      “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46
                      +00:00
                  tasks.result.items.1.lost_date:
                    type: integer
                    description: >-
                      date and time when the last backlink from this target was
                      lost indicates the date and time when our crawler visited
                      the page and it responded with 4xx or 5xx status code or
                      the last backlink was removed in the UTC format:
                      “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46
                      +00:00
                  tasks.result.items.1.backlinks_spam_score:
                    type: integer
                    description: >-
                      average spam score of the backlinks pointing to the target
                      learn more about how the metric is calculated on this help
                      center page
                  tasks.result.items.1.broken_backlinks:
                    type: integer
                    description: number of broken backlinks
                  tasks.result.items.1.broken_pages:
                    type: integer
                    description: number of broken pages
                  tasks.result.items.1.referring_domains:
                    type: integer
                    description: number of referring domains
                  tasks.result.items.1.referring_domains_nofollow:
                    type: integer
                    description: >-
                      number of domains pointing at least one nofollow link to
                      the corresponding target
                  tasks.result.items.1.referring_main_domains:
                    type: integer
                    description: number of referring main domains
                  tasks.result.items.1.referring_main_domains_nofollow:
                    type: integer
                    description: >-
                      number of main domains pointing at least one nofollow link
                      to the target
                  tasks.result.items.1.referring_ips:
                    type: integer
                    description: number of referring IP addresses
                  tasks.result.items.1.referring_subnets:
                    type: integer
                    description: number of referring subnetworks
                  tasks.result.items.1.referring_pages:
                    type: integer
                    description: indicates the number of pages pointing to the target
                  tasks.result.items.1.referring_links_tld:
                    type: object
                    description: >-
                      top level domains of the referring links contains
                      top-level domains and referring link count per each
                  tasks.result.items.1.referring_links_types:
                    type: object
                    description: >-
                      types of the referring links indicates the types of
                      referring links and link count per each type possible
                      values: anchor, image, link, meta, canonical, alternate,
                      redirect
                  tasks.result.items.1.referring_links_attributes:
                    type: object
                    description: >-
                      link attributes of the referring links indicates link
                      attributes of the referring links and the link count per
                      each attribute
                  tasks.result.items.1.referring_links_platform_types:
                    type: object
                    description: >-
                      types of referring platforms indicates referring platform
                      types and link count per each platform possible values:
                      cms, blogs, ecommerce, message-boards, wikis, news,
                      organization
                  tasks.result.items.1.referring_links_semantic_locations:
                    type: object
                    description: >-
                      semantic locations of the referring links indicates
                      semantic elements in HTML where the referring links are
                      located and the link count per each semantic location you
                      can get the full list of semantic elements here
                  tasks.result.items.1.referring_links_countries:
                    type: object
                    description: >-
                      ISO country codes of the referring links indicates ISO
                      country codes of the domains where the referring links are
                      located and the link count per each country
                  tasks.result.items.1.referring_pages_nofollow:
                    type: integer
                    description: >-
                      number of referring pages pointing at least one nofollow
                      link to the target
                  tasks.result.items.summary:
                    type: object
                    description: contains the domain intersections summary
                  tasks.result.items.intersections_count:
                    type: integer
                    description: total number of intersections
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