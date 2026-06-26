> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Backlinks Summary

> This endpoint will provide you with an overview of backlinks data available for a given domain, subdomain, or webpage.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/backlinks/summary/live
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
  /dataforseo/backlinks/summary/live:
    post:
      summary: Backlinks Summary
      description: >-
        This endpoint will provide you with an overview of backlinks data
        available for a given domain, subdomain, or webpage.
      operationId: post_dataforseo_backlinks_summary_live
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
                    domain, subdomain or webpage to get data for required field
                    a domain or a subdomain should be specified without https://
                    and www. a page should be specified with absolute URL
                    (including http:// or https://)
                include_subdomains:
                  type: boolean
                  description: >-
                    indicates if the subdomains of the target will be included
                    in the search optional field if set to false, the subdomains
                    will be ignored default value: true
                include_indirect_links:
                  type: boolean
                  description: >-
                    indicates if indirect links to the target will be included
                    in the results optional field if set to true, the results
                    will include data on indirect links pointing to a page that
                    either redirects to the target, or points to a canonical
                    page if set to false, indirect links will be ignored default
                    value: true
                exclude_internal_backlinks:
                  type: boolean
                  description: >-
                    indicates if internal backlinks from subdomains to the
                    target will be excluded from the results optional field if
                    set to true, the results will not include data on internal
                    backlinks from subdomains of the same domain as target if
                    set to false, internal links will be included in the results
                    default value: true
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
                    and used for aggregated metrics for your target; possible
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
                    for example: "backlinks_filters": ["dofollow", "=", true]
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
                  tasks.result.first_seen:
                    type: string
                    description: >-
                      date and time when our crawler found the backlink for the
                      target for the first time in the UTC format: “yyyy-mm-dd
                      hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00
                  tasks.result.lost_date:
                    type: string
                    description: >-
                      date and time when the backlink was lost indicates the
                      date and time when our crawler visited the target and it
                      responded with a 4xx or 5xx status code or when its last
                      backlink was removed in the UTC format: “yyyy-mm-dd
                      hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00
                  tasks.result.rank:
                    type: integer
                    description: >-
                      target rank learn more about the metric and how it is
                      calculated in this help center article
                  tasks.result.backlinks:
                    type: integer
                    description: indicates the number of backlinks
                  tasks.result.backlinks_spam_score:
                    type: integer
                    description: >-
                      spam score of the backlinks displays the total spam score
                      of all backlinks pointing to the target domain, subdomain,
                      or webpage; to learn more about how the metric is
                      calculated, refer to this Help Center page
                  tasks.result.crawled_pages:
                    type: integer
                    description: number of crawled pages for the target
                  tasks.result.info:
                    type: object
                    description: information about the target
                  tasks.result.info.server:
                    type: string
                    description: server
                  tasks.result.info.cms:
                    type: string
                    description: content management system
                  tasks.result.info.platform_type:
                    type: array
                    items:
                      type: string
                    description: platform type
                  tasks.result.info.ip_address:
                    type: string
                    description: IP address of the target
                  tasks.result.info.country:
                    type: string
                    description: >-
                      country code that the target domain is determined to
                      belong to
                  tasks.result.info.is_ip:
                    type: boolean
                    description: >-
                      indicates if the target is IP if true, the domain,
                      subdomain or webpage functions as an IP address and does
                      not have a domain name
                  tasks.result.info.target_spam_score:
                    type: integer
                    description: >-
                      spam score of the target if the target is a
                      domain/subdomain, this fields indicates the average spam
                      score of all pages of that domain/subdomain; learn more
                      about how the metric is calculated on this help center
                      page
                  tasks.result.internal_links_count:
                    type: integer
                    description: >-
                      number of internal links calculated as the sum of internal
                      links on the pages of the specified target
                  tasks.result.external_links_count:
                    type: integer
                    description: >-
                      number of external links on the page calculated as the sum
                      of external links on the pages of the specified target
                  tasks.result.broken_backlinks:
                    type: integer
                    description: >-
                      number of broken backlinks number of broken backlinks
                      pointing to the target
                  tasks.result.broken_pages:
                    type: integer
                    description: >-
                      number of broken pages number of pages on the target that
                      respond with 4xx or 5xx status codes note that the number
                      of broken pages includes pages on the target discovered by
                      following external links, but it may also include pages
                      discovered by following the target’s sitemap
                  tasks.result.referring_domains:
                    type: integer
                    description: >-
                      indicates the number of referring domains referring
                      domains include subdomains that are counted as separate
                      domains for this metric
                  tasks.result.referring_domains_nofollow:
                    type: integer
                    description: >-
                      number of domains pointing at least one nofollow link to
                      the target
                  tasks.result.referring_main_domains:
                    type: integer
                    description: indicates the number of referring main domains
                  tasks.result.referring_main_domains_nofollow:
                    type: integer
                    description: >-
                      number of main domains pointing at least one nofollow link
                      to the target
                  tasks.result.referring_ips:
                    type: integer
                    description: >-
                      number of referring IP addresses number of IP addresses
                      pointing to this page
                  tasks.result.referring_subnets:
                    type: integer
                    description: number of referring subnetworks
                  tasks.result.referring_pages:
                    type: integer
                    description: indicates the number of pages pointing to the target
                  tasks.result.referring_links_tld:
                    type: object
                    description: >-
                      top-level domains of the referring links contains top
                      level domains and referring link count per each
                  tasks.result.referring_links_types:
                    type: object
                    description: >-
                      types of referring links indicates the types of the
                      referring links and link count per each type possible
                      values: anchor, image, link, meta, canonical, alternate,
                      redirect
                  tasks.result.referring_links_attributes:
                    type: object
                    description: >-
                      link attributes of the referring links indicates link
                      attributes of the referring links and link count per each
                      attribute example values: nofollow, noopener, noreferrer,
                      external, ugc, sponsored
                  tasks.result.referring_links_platform_types:
                    type: object
                    description: >-
                      types of referring platforms indicates referring platform
                      types and and link count per each platform possible
                      values: cms, blogs, ecommerce, message-boards, wikis,
                      news, organization
                  tasks.result.referring_links_semantic_locations:
                    type: object
                    description: >-
                      semantic locations of the referring links indicates
                      semantic elements in HTML where the referring links are
                      located and link count per each semantic location you can
                      get the full list of semantic elements here example
                      values: article, section, summary, ""
                  tasks.result.referring_links_countries:
                    type: object
                    description: >-
                      ISO country codes of the referring links indicates ISO
                      country codes of the domains where the referring links are
                      located and the link count per each country
                  tasks.result.referring_pages_nofollow:
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