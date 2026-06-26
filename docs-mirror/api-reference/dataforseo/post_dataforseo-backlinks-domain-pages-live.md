> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Domain Pages

> This endpoint will provide you with a detailed overview of domain pages with backlink data for each page.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/backlinks/domain_pages/live
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
  /dataforseo/backlinks/domain_pages/live:
    post:
      summary: Domain Pages
      description: >-
        This endpoint will provide you with a detailed overview of domain pages
        with backlink data for each page.
      operationId: post_dataforseo_backlinks_domain_pages_live
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
                    domain or subdomain required field a domain or a subdomain
                    should be specified without https:// and www. example:
                    forbes.com
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned pages optional field default
                    value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned pages optional field
                    default value: 0 if you specify the 10 value, the first ten
                    pages in the results array will be omitted and the data will
                    be provided for the successive pages
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
                    and used for aggregated metrics; possible values: all – all
                    backlinks will be returned and counted; live – backlinks
                    found during the last check will be returned and counted;
                    lost – lost backlinks will be returned and counted; default
                    value: live
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
                    ["meta.internal_links_count",">","1"]
                    [["meta.external_links_count",">","2"], "and",
                    ["backlinks",">","10"]] [["first_visited",">","2017-10-23
                    11:31:45 +00:00"], "and",
                    [["title","like","%seo%"],"or",["referring_domains",">","10"]]]
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
                    ["page_summary.backlinks,desc"] note that you can set no
                    more than three sorting rules in a single request you should
                    use a comma to separate several sorting rules example:
                    ["page_summary.backlinks,desc","page_summary.rank,asc"]
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
                    for example: "backlinks_filters": ["dofollow", "=", true]
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
                    description: target in a POST array
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
                    description: type of element = ‘backlinks_domain_page’
                  tasks.result.items.main_domain:
                    type: string
                    description: >-
                      main website domain main website domain does not include
                      subdomains
                  tasks.result.items.domain:
                    type: string
                    description: domain domain where the page was found
                  tasks.result.items.tld:
                    type: string
                    description: top-level domain top-level domain in the DNS root zone
                  tasks.result.items.page:
                    type: string
                    description: page URL relevant page URL
                  tasks.result.items.ip:
                    type: string
                    description: Internet Protocol address
                  tasks.result.items.first_visited:
                    type: string
                    description: >-
                      date and time of the first page visit date and time when
                      our crawler visited this page for the first time in the
                      UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2017-01-24 13:20:59 +00:00
                  tasks.result.items.prev_visited:
                    type: string
                    description: >-
                      previous to the most recent date when our crawler visited
                      the page in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”
                      example: 2017-01-24 13:20:59 +00:00
                  tasks.result.items.fetch_time:
                    type: string
                    description: >-
                      most recent date and time when our crawler visited the
                      page in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”
                      example: 2017-01-24 13:20:59 +00:00
                  tasks.result.items.status code:
                    type: integer
                    description: HTTP status code of the page
                  tasks.result.items.location:
                    type: string
                    description: >-
                      location header indicates the URL to redirect a page to if
                      exists
                  tasks.result.items.size:
                    type: integer
                    description: indicates the page size, in bytes
                  tasks.result.items.encoded_size:
                    type: integer
                    description: >-
                      page size after encoding indicates the size of the encoded
                      page, in bytes
                  tasks.result.items.content_encoding:
                    type: string
                    description: type of encoding
                  tasks.result.items.media_type:
                    type: string
                    description: types of media used to display a page
                  tasks.result.items.server:
                    type: string
                    description: server version
                  tasks.result.items.meta:
                    type: object
                    description: page meta data
                  tasks.result.items.meta.title:
                    type: string
                    description: page title
                  tasks.result.items.meta.canonical:
                    type: string
                    description: canonical page
                  tasks.result.items.meta.internal_links_count:
                    type: integer
                    description: number of internal links on the page
                  tasks.result.items.meta.external_links_count:
                    type: integer
                    description: number of external links on the page
                  tasks.result.items.meta.images_count:
                    type: integer
                    description: number of images on the page
                  tasks.result.items.meta.words_count:
                    type: integer
                    description: number of words on the page
                  tasks.result.items.meta.page_spam_score:
                    type: integer
                    description: >-
                      spam score of the page learn more about how the metric is
                      calculated on this help center page
                  tasks.result.items.meta.social_media_tags:
                    type: object
                    description: >-
                      array of social media tags found on the page contains
                      social media tags and their content supported tags include
                      but are not limited to Open Graph and Twitter card
                  tasks.result.items.meta.h1:
                    type: array
                    items:
                      type: string
                    description: h1 tag content of h1 tags
                  tasks.result.items.meta.h2:
                    type: array
                    items:
                      type: string
                    description: h2 tag content of h2 tags
                  tasks.result.items.meta.h3:
                    type: array
                    items:
                      type: string
                    description: h3 tag content of h3 tags
                  tasks.result.items.meta.images_alt:
                    type: array
                    items:
                      type: string
                    description: content of alt tags
                  tasks.result.items.meta.powered_by:
                    type: array
                    items:
                      type: string
                    description: CMS details
                  tasks.result.items.meta.language:
                    type: string
                    description: 'page content language example: en'
                  tasks.result.items.meta.charset:
                    type: string
                    description: 'character encoding examples: utf-8'
                  tasks.result.items.meta.platform_type:
                    type: array
                    items:
                      type: string
                    description: type of a platform
                  tasks.result.items.meta.technologies:
                    type: object
                    description: website technologies
                  tasks.result.items.meta.technologies.cms:
                    type: string
                    description: content management system
                  tasks.result.items.meta.technologies.blogs:
                    type: string
                    description: blog management system
                  tasks.result.items.meta.technologies.cdn:
                    type: string
                    description: content delivery network
                  tasks.result.items.page_summary:
                    type: object
                    description: contains backlink data for this page
                  tasks.result.items.page_summary.first_seen:
                    type: string
                    description: >-
                      date and time when our crawler found the backlink for the
                      first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”
                      example: 2019-11-15 12:57:46 +00:00
                  tasks.result.items.page_summary.lost_date:
                    type: string
                    description: >-
                      date and time when the last backlink for this page was
                      lost indicates the date and time when our crawler visited
                      the page and it responded with 4xx or 5xx status code or
                      the last backlink was removed in the UTC format:
                      “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59
                      +00:00
                  tasks.result.items.page_summary.rank:
                    type: integer
                    description: >-
                      page rank rank of the page rank is calculated based on the
                      method for node ranking in a linked database – a principle
                      used in the original Google PageRank algorithm learn more
                      about the metric and how it is calculated in this help
                      center article
                  tasks.result.items.page_summary.backlinks:
                    type: integer
                    description: indicates the number of backlinks
                  tasks.result.items.page_summary.backlinks_spam_score:
                    type: integer
                    description: >-
                      average spam score of the backlinks pointing to the page
                      learn more about how the metric is calculated on this help
                      center page
                  tasks.result.items.page_summary.broken_backlinks:
                    type: integer
                    description: >-
                      number of broken backlinks number of broken backlinks
                      pointing to the page
                  tasks.result.items.page_summary.broken_pages:
                    type: integer
                    description: >-
                      number of broken pages number of pages that respond with
                      4xx or 5xx status codes where backlinks are pointing to
                  tasks.result.items.page_summary.referring_domains:
                    type: integer
                    description: indicates the number of referring domains
                  tasks.result.items.page_summary.referring_domains_nofollow:
                    type: integer
                    description: >-
                      number of domains pointing at least one nofollow link to
                      the page
                  tasks.result.items.page_summary.referring_main_domains:
                    type: integer
                    description: indicates the number of referring main domains
                  tasks.result.items.page_summary.referring_main_domains_nofollow:
                    type: integer
                    description: >-
                      number of main domains pointing at least one nofollow link
                      to the page
                  tasks.result.items.page_summary.referring ips:
                    type: integer
                    description: >-
                      number of referring IP addresses number of IP addresses
                      pointing to this page
                  tasks.result.items.page_summary.referring subnets:
                    type: integer
                    description: number of referring subnetworks
                  tasks.result.items.page_summary.referring_pages:
                    type: integer
                    description: indicates the number of pages pointing to the page
                  tasks.result.items.page_summary.referring_links_tld:
                    type: object
                    description: >-
                      top-level domains of the referring links contains top
                      level domains and referring link count per each
                  tasks.result.items.page_summary.referring_links_types:
                    type: object
                    description: >-
                      types of referring links indicates the types of the
                      referring links and link count per each type possible
                      values: anchor, image, link, meta, canonical, alternate,
                      redirect
                  tasks.result.items.page_summary.referring_links_attributes:
                    type: object
                    description: >-
                      link attributes of the referring links indicates link
                      attributes of the referring links and link count per each
                      attribute
                  tasks.result.items.page_summary.referring_links_platform_types:
                    type: object
                    description: >-
                      types of referring platforms indicates referring platform
                      types and and link count per each platform possible
                      values: cms, blogs, ecommerce, message-boards, wikis,
                      news, organization
                  tasks.result.items.page_summary.referring_links_semantic_locations:
                    type: object
                    description: >-
                      semantic locations of the referring links indicates
                      semantic elements in HTML where the referring links are
                      located and link count per each semantic location you can
                      get the full list of semantic elements here examples:
                      article, section, summary
                  tasks.result.items.page_summary.referring_links_countries:
                    type: object
                    description: >-
                      ISO country codes of the referring links indicates ISO
                      country codes of the domains where the referring links are
                      located and the link count per each country
                  tasks.result.items.page_summary.referring_pages_nofollow:
                    type: integer
                    description: >-
                      number of referring pages pointing at least one nofollow
                      link to the page
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