> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Backlinks

> This endpoint will provide you with a list of backlinks and relevant data for the specified domain, subdomain, or webpage.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/backlinks/backlinks/live
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
  /dataforseo/backlinks/backlinks/live:
    post:
      summary: Backlinks
      description: >-
        This endpoint will provide you with a list of backlinks and relevant
        data for the specified domain, subdomain, or webpage.
      operationId: post_dataforseo_backlinks_backlinks_live
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
                    domain, subdomain or webpage to get backlinks for required
                    field a domain or a subdomain should be specified without
                    https:// and www. a page should be specified with absolute
                    URL (including http:// or https://)
                mode:
                  type: string
                  description: >-
                    results grouping type optional field possible grouping
                    types: as_is – returns all backlinks one_per_domain –
                    returns one backlink per domain one_per_anchor – returns one
                    backlink per anchor default value: as_is
                custom_mode:
                  type: object
                  description: >-
                    detailed results grouping type optional field use this
                    object to get a specific number of backlinks per field if
                    you use custom_mode, then mode will be ignored example:
                    "custom_mode": {"field": "domain", "value": 100}
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: =, , in, not_in, like,
                    not_like, ilike, not_ilike, regex, not_regex, match,
                    not_match you can use the % operator with like and not_like
                    to match any string of zero or more characters example:
                    ["rank",">","80"] [["page_from_rank",">","55"], "and",
                    ["dofollow","=",true]] [["first_seen",">","2017-10-23
                    11:31:45 +00:00"], "and",
                    [["anchor","like","%seo%"],"or",["text_pre","like","%seo%"]]]
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
                    ["rank,desc"] note that you can set no more than three
                    sorting rules in a single request you should use a comma to
                    separate several sorting rules example:
                    ["domain_from_rank,desc","page_from_rank,asc"]
                offset:
                  type: integer
                  description: >-
                    offset in the results array of the returned backlinks
                    optional field default value: 0 if you specify the 10 value,
                    the first ten backlinks in the results array will be omitted
                    and the data will be provided for the successive backlinks;
                    Note: the maximum value is 20,000, use the
                    search_after_token if you would like to offset more results
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
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned backlinks optional field
                    default value: 100 maximum value: 1000
                backlinks_status_type:
                  type: string
                  description: >-
                    set what backlinks to return and count optional field you
                    can use this field to choose what backlinks will be returned
                    and used for aggregated metrics for your target; possible
                    values: all – all backlinks will be returned and counted;
                    live – backlinks found during the last check will be
                    returned and counted; lost – lost backlinks will be returned
                    and counted; default value: live
                include_subdomains:
                  type: boolean
                  description: >-
                    indicates if the subdomains of the target will be included
                    in the search optional field if set to false, the subdomains
                    will be ignored default value: true
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
                  tasks.result.target:
                    type: string
                    description: target domain in a POST array
                  tasks.result.mode:
                    type: string
                    description: mode specified in a POST array
                  tasks.result.custom_mode:
                    type: object
                    description: custom mode specified in a POST array
                  tasks.result.total_count:
                    type: integer
                    description: total amount of results relevant the request
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains relevant backlinks and referring domains data
                  tasks.result.items.type:
                    type: string
                    description: type of element = ‘backlink’
                  tasks.result.items.domain_from:
                    type: string
                    description: domain referring to the target domain or webpage
                  tasks.result.items.url_from:
                    type: string
                    description: URL of the page where the backlink is found
                  tasks.result.items.url_from_https:
                    type: boolean
                    description: >-
                      indicates whether the referring URL is secured with HTTPS
                      if true, the referring URL is secured with HTTPS
                  tasks.result.items.domain_to:
                    type: string
                    description: domain the backlink is pointing to
                  tasks.result.items.url_to:
                    type: string
                    description: URL the backlink is pointing to
                  tasks.result.items.url_to_https:
                    type: boolean
                    description: >-
                      indicates if the URL the backlink is pointing to is
                      secured with HTTPS if true, the URL is secured with HTTPS
                  tasks.result.items.tld_from:
                    type: string
                    description: top-level domain of the referring URL
                  tasks.result.items.is_new:
                    type: boolean
                    description: >-
                      indicates whether the backlink is new if true, the
                      backlink was found on the page last time our crawler
                      visited it
                  tasks.result.items.is_lost:
                    type: boolean
                    description: >-
                      indicates whether the backlink was removed if true, the
                      backlink or the entire page was removed
                  tasks.result.items.backlink_spam_score:
                    type: integer
                    description: >-
                      spam score of the backlink learn more about how the metric
                      is calculated on this help center page
                  tasks.result.items.rank:
                    type: integer
                    description: >-
                      backlink rank rank that the given backlink passes to the
                      target rank is calculated based on the method for node
                      ranking in a linked database – a principle used in the
                      original Google PageRank algorithm learn more about the
                      metric and how it is calculated in this help center
                      article
                  tasks.result.items.page_from_rank:
                    type: integer
                    description: >-
                      page rank of the referring page page_from_rank is
                      calculated based on the method for node ranking in a
                      linked database – a principle used in the original Google
                      PageRank algorithm learn more about the metric and how it
                      is calculated in this help center article
                  tasks.result.items.domain_from_rank:
                    type: integer
                    description: >-
                      domain rank of the referring domain domain_from_rank is
                      calculated based on the method for node ranking in a
                      linked database – a principle used in the original Google
                      PageRank algorithm learn more about the metric and how it
                      is calculated in this help center article
                  tasks.result.items.domain_from_platform_type:
                    type: array
                    items:
                      type: string
                    description: >-
                      platform types of the referring domain possible values:
                      cms, blogs, ecommerce, message-boards, wikis, news,
                      organization
                  tasks.result.items.domain_from_is_ip:
                    type: boolean
                    description: >-
                      indicates if the domain is IP if true, the domain
                      functions as an IP address and does not have a domain name
                  tasks.result.items.domain_from_ip:
                    type: string
                    description: IP address of the referring domain
                  tasks.result.items.domain_from_country:
                    type: string
                    description: ISO country code of the referring domain
                  tasks.result.items.page_from_external_links:
                    type: integer
                    description: number of external links found on the referring page
                  tasks.result.items.page_from_internal_links:
                    type: integer
                    description: number of internal links found on the referring page
                  tasks.result.items.page_from_size:
                    type: integer
                    description: 'size of the referring page, in bytes example: 63357'
                  tasks.result.items.page_from_encoding:
                    type: string
                    description: 'character encoding of the referring page example: utf-8'
                  tasks.result.items.page_from_language:
                    type: string
                    description: >-
                      language of the referring page in ISO 639-1 format
                      example: en
                  tasks.result.items.page_from_title:
                    type: string
                    description: title of the referring page
                  tasks.result.items.page_from_status_code:
                    type: integer
                    description: >-
                      HTTP status code returned by the referring page example:
                      200
                  tasks.result.items.first_seen:
                    type: string
                    description: >-
                      date and time when our crawler found the backlink for the
                      first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”
                      example: 2019-11-15 12:57:46 +00:00
                  tasks.result.items.prev_seen:
                    type: string
                    description: >-
                      previous to the most recent date when our crawler visited
                      the backlink in the UTC format: “yyyy-mm-dd hh-mm-ss
                      +00:00” example: 2019-11-15 12:57:46 +00:00
                  tasks.result.items.last_seen:
                    type: string
                    description: >-
                      most recent date when our crawler visited the backlink in
                      the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2019-11-15 12:57:46 +00:00
                  tasks.result.items.item_type:
                    type: string
                    description: >-
                      link type possible values: anchor, image, meta, canonical,
                      alternate, redirect
                  tasks.result.items.attributes:
                    type: array
                    items:
                      type: string
                    description: 'link attributes of the referring links example: nofollow'
                  tasks.result.items.dofollow:
                    type: boolean
                    description: >-
                      indicates whether the backlink is dofollow if false, the
                      backlink is nofollow
                  tasks.result.items.original:
                    type: boolean
                    description: >-
                      indicates whether the backlink was present on the
                      referring page when our crawler first visited it
                  tasks.result.items.alt:
                    type: string
                    description: >-
                      alternative text of the image this field will be null if
                      backlink type is not image
                  tasks.result.items.image_url:
                    type: string
                    description: >-
                      URL of the image the URL leading to the image on the
                      original resource or DataForSEO storage (in case the
                      original source is not available)
                  tasks.result.items.anchor:
                    type: string
                    description: anchor text of the backlink
                  tasks.result.items.text_pre:
                    type: string
                    description: snippet before the anchor text
                  tasks.result.items.text_post:
                    type: string
                    description: snippet after the anchor text
                  tasks.result.items.semantic_location:
                    type: string
                    description: >-
                      indicates semantic element in HTML where the backlink is
                      found you can get the full list of semantic elements here
                      examples: article, section, summary
                  tasks.result.items.links_count:
                    type: integer
                    description: number of identical backlinks found on the referring page
                  tasks.result.items.group_count:
                    type: integer
                    description: >-
                      indicates total number of backlinks from this domain for
                      example, if mode is set to one_per_domain, this field will
                      indicate the total number of backlinks coming from this
                      domain
                  tasks.result.items.is_broken:
                    type: boolean
                    description: >-
                      indicates whether the backlink is broken if true, the
                      backlink is pointing to a page responding with a 4xx or
                      5xx status code
                  tasks.result.items.url_to_status_code:
                    type: integer
                    description: >-
                      status code of the referenced page if the value is null,
                      our crawler hasn’t yet visited the webpage the link is
                      pointing to example: 200
                  tasks.result.items.url_to_spam_score:
                    type: integer
                    description: >-
                      spam score of the referenced page if the value is null,
                      our crawler hasn’t yet visited the webpage the link is
                      pointing to; learn more about how the metric is calculated
                      on this help center page
                  tasks.result.items.url_to_redirect_target:
                    type: string
                    description: >-
                      target url of the redirect target page the redirect is
                      pointing to
                  tasks.result.items.is_indirect_link:
                    type: boolean
                    description: >-
                      indicates whether the backlink is an indirect link if
                      true, the backlink is an indirect link pointing to a page
                      that either redirects to url_to, or points to a canonical
                      page
                  tasks.result.items.indirect_link_path:
                    type: array
                    items:
                      type: string
                    description: >-
                      indirect link path indicates a URL or a sequence of URLs
                      that lead to url_to
                  tasks.result.items.indirect_link_path.type:
                    type: string
                    description: 'indirect link type possible values: redirect, canonical'
                  tasks.result.items.indirect_link_path.status_code:
                    type: integer
                    description: HTTP status code of the URL
                  tasks.result.items.indirect_link_path.url:
                    type: string
                    description: indirect link URL
                  tasks.result.search_after_token:
                    type: string
                    description: >-
                      token for subsequent requests by specifying the unique
                      search_after_token when setting a new task, you will get
                      the subsequent results of the initial task;
                      search_after_token values are unique for each subsequent
                      task
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