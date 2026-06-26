> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Backlinks History

> This endpoint will provide you with historical backlinks data back to the beginning of 2019.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/backlinks/history/live
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
  /dataforseo/backlinks/history/live:
    post:
      summary: Backlinks History
      description: >-
        This endpoint will provide you with historical backlinks data back to
        the beginning of 2019. You can receive the number of backlinks a given
        domain had in a specific time period, the number of new & lost
        backlinks, referring domains, and more.
      operationId: post_dataforseo_backlinks_history_live
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
                    domain required field a domain should be specified without
                    https:// and www.
                date_from:
                  type: string
                  description: >-
                    starting date of the time range optional field minimum value
                    2019-01-01 if you don’t specify this field, the minimum
                    value will be used by default date format: "yyyy-mm-dd"
                    example: "2019-01-15"
                date_to:
                  type: string
                  description: >-
                    ending date of the time range optional field if you don’t
                    specify this field, the today’s date will be used by default
                    date format: "yyyy-mm-dd" example: "2019-01-15"
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
                    description: target from the POST array
                  tasks.result.date_from:
                    type: string
                    description: >-
                      starting date of the time range in the UTC format:
                      “yyyy-mm-dd” example: 2019-01-01
                  tasks.result.date_to:
                    type: string
                    description: >-
                      ending date of the time range in the UTC format:
                      "yyyy-mm-dd" example: "2019-01-15"
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains historical backlink data for the specified domain
                      the data is provided month-by-month; the metrics are
                      aggregated according to the backlinks the specified domain
                      had on the first day of each given month
                  tasks.result.items.type:
                    type: string
                    description: type of element = ‘backlinks_history’
                  tasks.result.items.date:
                    type: string
                    description: >-
                      date and time when the data for the target was stored in
                      the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2019-11-15 12:57:46 +00:00
                  tasks.result.items.rank:
                    type: integer
                    description: >-
                      domain rank on the given date learn more about the metric
                      and how it is calculated in this help center article
                  tasks.result.items.backlinks:
                    type: integer
                    description: number of backlinks
                  tasks.result.items.new_backlinks:
                    type: integer
                    description: >-
                      number of new backlinks for the target data is provided
                      based in a comparison with the previous period Note: this
                      data is available from May 2021; if the date range
                      specified in the POST request precedes May 2021, the field
                      will equal 0
                  tasks.result.items.lost_backlinks:
                    type: integer
                    description: >-
                      number of lost backlinks for the target data is provided
                      based in a comparison with the previous period Note: this
                      data is available from May 2021; if the date range
                      specified in the POST request precedes May 2021, the field
                      will equal 0
                  tasks.result.items.new_referring_domains:
                    type: integer
                    description: >-
                      number of new referring domains for the target data is
                      provided based in a comparison with the previous period
                      Note: this data is available from May 2021; if the date
                      range specified in the POST request precedes May 2021, the
                      field will equal 0
                  tasks.result.items.lost_referring_domains:
                    type: integer
                    description: >-
                      number of lost referring domains for the target data is
                      provided based in a comparison with the previous period
                      Note: this data is available from May 2021; if the date
                      range specified in the POST request precedes May 2021, the
                      field will equal 0
                  tasks.result.items.crawled_pages:
                    type: integer
                    description: number of crawled pages for the target
                  tasks.result.items.info:
                    type: object
                    description: information about the target
                  tasks.result.items.info.server:
                    type: string
                    description: server
                  tasks.result.items.info.cms:
                    type: string
                    description: content management system
                  tasks.result.items.info.platform_type:
                    type: array
                    items:
                      type: string
                    description: platform type
                  tasks.result.items.info.ip_address:
                    type: string
                    description: IP address of the target
                  tasks.result.items.info.country:
                    type: string
                    description: >-
                      country code that the target domain is determined to
                      belong to
                  tasks.result.items.info.is_ip:
                    type: boolean
                    description: >-
                      indicates if the target is IP if true, the domain,
                      subdomain or webpage functions as an IP address and does
                      not have a domain name
                  tasks.result.items.info.target_spam_score:
                    type: integer
                    description: >-
                      spam score of the target if the target is a
                      domain/subdomain, this fields indicates the average spam
                      score of all pages of that domain/subdomain; learn more
                      about how the metric is calculated on this help center
                      page
                  tasks.result.items.internal_links_count:
                    type: integer
                    description: >-
                      number of internal links calculated as the sum of internal
                      links on the pages of the specified target
                  tasks.result.items.external_links_count:
                    type: integer
                    description: >-
                      number of external links on the page calculated as the sum
                      of external links on the pages of the specified target
                  tasks.result.items.broken_backlinks:
                    type: integer
                    description: >-
                      number of broken backlinks number of broken backlinks
                      pointing to the target
                  tasks.result.items.broken_pages:
                    type: integer
                    description: >-
                      number of broken pages number of pages that receive
                      backlinks but respond with 4xx or 5xx status codes
                  tasks.result.items.referring_domains:
                    type: integer
                    description: >-
                      number of referring domains referring domains include
                      subdomains that are counted as separate domains for this
                      metric
                  tasks.result.items.referring_domains_nofollow:
                    type: integer
                    description: >-
                      number of domains pointing at least one nofollow link to
                      the target
                  tasks.result.items.referring_main_domains:
                    type: integer
                    description: number of referring main domains
                  tasks.result.items.referring_main_domains_nofollow:
                    type: integer
                    description: >-
                      number of main domains pointing at least one nofollow link
                      to the target
                  tasks.result.items.referring_ips:
                    type: integer
                    description: >-
                      number of referring IP addresses number of IP addresses
                      pointing to this page
                  tasks.result.items.referring_subnets:
                    type: integer
                    description: number of referring subnetworks
                  tasks.result.items.referring_pages:
                    type: integer
                    description: number of pages pointing to the target
                  tasks.result.items.referring_links_tld:
                    type: object
                    description: >-
                      top-level domains of the referring links contains
                      top-level domains and referring link count per each
                  tasks.result.items.referring_links_types:
                    type: object
                    description: >-
                      types of referring links indicates the types of the
                      referring links and link count per each type possible
                      values: anchor, image, link, meta, canonical, alternate,
                      redirect
                  tasks.result.items.referring_links_attributes:
                    type: object
                    description: >-
                      link attributes of the referring links indicates link
                      attributes of the referring links and link count per each
                      attribute
                  tasks.result.items.referring_links_platform_types:
                    type: object
                    description: >-
                      types of referring platforms indicates referring platform
                      types and and link count per each platform possible
                      values: cms, blogs, ecommerce, message-boards, wikis,
                      news, organization
                  tasks.result.items.referring_links_semantic_locations:
                    type: object
                    description: >-
                      semantic locations of the referring links indicates
                      semantic elements in HTML where the referring links are
                      located and link count per each semantic location you can
                      get the full list of semantic elements here examples:
                      article, section, summary
                  tasks.result.items.referring_links_countries:
                    type: object
                    description: >-
                      ISO country codes of the referring links indicates ISO
                      country codes of the domains where the referring links are
                      located and the link count per each country
                  tasks.result.items.referring_pages_nofollow:
                    type: integer
                    description: >-
                      number of referring pages pointing at least one nofollow
                      link to the target
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