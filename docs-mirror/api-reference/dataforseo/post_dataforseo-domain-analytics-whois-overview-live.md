> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Domain Whois Overview

> This endpoint will provide you with Whois data enriched with backlink stats, and ranking and traffic info from organic and paid search results.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/domain_analytics/whois/overview/live
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
  /dataforseo/domain_analytics/whois/overview/live:
    post:
      summary: Domain Whois Overview
      description: >-
        This endpoint will provide you with Whois data enriched with backlink
        stats, and ranking and traffic info from organic and paid search
        results. Using this endpoint you will be able to get all these data for
        the domains matching the parameters you specify in the request.
      operationId: post_dataforseo_domain_analytics_whois_overview_live
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned domains optional field
                    default value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned items optional field
                    default value: 0 if you specify the 10 value, the first ten
                    items in the results array will be omitted and the data will
                    be provided for the successive items; Note: we recommend
                    using this parameter only when retrieving up to 10,000
                    results for retrieving over 10,000 results, use the
                    offset_token instead
                offset_token:
                  type: string
                  description: >-
                    token for subsequent requests optional field provided in the
                    identical filed of the response to each request; use this
                    parameter to avoid timeouts while trying to obtain over
                    100,000 results in a single request; by specifying the
                    unique offset_token value from the response array, you will
                    get the subsequent results of the initial task; offset_token
                    values are unique for each subsequent task Note: if the
                    offset_token is specified in the request, all other
                    parameters should be identical to the previous request learn
                    more about this parameter on our Help Center
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: regex, , , >, >=, =, ,
                    in, not_in, like, not_like you can use the % operator with
                    like and not_like to match any string of zero or more
                    characters
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    results sorting rules optional field you can use the same
                    values as in the filters array to sort the results possible
                    sorting types: asc - results will be sorted in the ascending
                    order desc - results will be sorted in the descending order
                    the comma is used as a separator example:
                    ["metrics.organic.pos_1,desc"] default rule:
                    ["metrics.organic.count,desc"] note that you can set no more
                    than three sorting rules in a single request you should use
                    a comma to separate several sorting rules example:
                    ["expiration_datetime,asc","metrics.organic.etv,desc","metrics.organic.pos_1,desc"]
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
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
                    description: >-
                      total amount of results in our database relevant to your
                      request
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.offset:
                    type: integer
                    description: results offset value specified in POST request
                  tasks.result.offset_token:
                    type: object
                    description: >-
                      token for subsequent requests by specifying the unique
                      offset_token when setting a new task, you will get the
                      subsequent results of the initial task; offset_token
                      values are unique for each subsequent task
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains ranking and traffic data
                  tasks.result.items.domain:
                    type: string
                    description: domain name
                  tasks.result.items.created_datetime:
                    type: string
                    description: >-
                      date and time of registration date and time (in the ISO
                      8601 format) when the domain was first registered example:
                      "1997-03-29 03:00:00 +00:00"
                  tasks.result.items.changed_datetime:
                    type: string
                    description: >-
                      date and time when the domain entry was changed date and
                      time (in the ISO 8601 format) when the domain entry was
                      last modified example: "2021-01-14 08:36:28 +00:00"
                  tasks.result.items.expiration_datetime:
                    type: string
                    description: >-
                      date and time when the domain will expire date and time
                      (in the ISO 8601 format) when the domain is due to expire
                      example: "2022-11-26 17:21:23 +00:00"
                  tasks.result.items.updated_datetime:
                    type: string
                    description: >-
                      date and time when the domain was updated date and time
                      (in the ISO 8601 format) when the domain was last updated
                      example: "2021-01-29 13:59:38 +00:00"
                  tasks.result.items.first_seen:
                    type: string
                    description: >-
                      date and time when our crawler found the domain for the
                      first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”
                      example: "2019-11-15 12:57:46 +00:00"
                  tasks.result.items.epp_status_codes:
                    type: array
                    items:
                      type: string
                    description: >-
                      extensive provisioning protocol status codes the status of
                      a domain name registration as defined by ICANN
                  tasks.result.items.tld:
                    type: string
                    description: top-level domain top-level domain in the DNS root zone
                  tasks.result.items.registered:
                    type: boolean
                    description: >-
                      domain registration status if false, the domain name
                      registration has expired Note: expired domains will remain
                      in the database for only a short period of time
                  tasks.result.items.registrar:
                    type: string
                    description: >-
                      domain registrar if null, the domain registrar is unknown
                      example: NameCheap, Inc.
                  tasks.result.items.metrics:
                    type: object
                    description: ranking data relevant to the specified domain
                  tasks.result.items.metrics.organic:
                    type: object
                    description: ranking and traffic data from organic search
                  tasks.result.items.metrics.organic.pos_1:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #1'
                  tasks.result.items.metrics.organic.pos_2_3:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #2-3'
                  tasks.result.items.metrics.organic.pos_4_10:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #4-10'
                  tasks.result.items.metrics.organic.pos_11_20:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #11-20'
                  tasks.result.items.metrics.organic.pos_21_30:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #21-30'
                  tasks.result.items.metrics.organic.pos_31_40:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #31-40'
                  tasks.result.items.metrics.organic.pos_41_50:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #41-50'
                  tasks.result.items.metrics.organic.pos_51_60:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #51-60'
                  tasks.result.items.metrics.organic.pos_61_70:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #61-70'
                  tasks.result.items.metrics.organic.pos_71_80:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #71-80'
                  tasks.result.items.metrics.organic.pos_81_90:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #81-90'
                  tasks.result.items.metrics.organic.pos_91_100:
                    type: integer
                    description: 'number of organic SERPs where the domain ranks #91-100'
                  tasks.result.items.metrics.organic.etv:
                    type: number
                    description: >-
                      estimated traffic volume estimated organic monthly traffic
                      to the domain calculated as the product of CTR
                      (click-through-rate) and search volume values of all
                      keywords the domain ranks for learn more about how the
                      metric is calculated in this help center article
                  tasks.result.items.metrics.organic.count:
                    type: integer
                    description: total count of organic SERPs that contain the domain
                  tasks.result.items.metrics.organic.estimated_paid_traffic_cost:
                    type: number
                    description: >-
                      estimated cost of converting organic search traffic into
                      paid represents the estimated monthly cost of running ads
                      (USD) for all keywords a domain ranks for the metric is
                      calculated as the product of organic etv and paid cpc
                      values and indicates the cost of driving the estimated
                      volume of monthly organic traffic through PPC advertising
                      in Google Search learn more about how the metric is
                      calculated in this help center article
                  tasks.result.items.metrics.paid:
                    type: object
                    description: ranking and traffic data from paid search
                  tasks.result.items.metrics.paid.pos_1:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #1'
                  tasks.result.items.metrics.paid.pos_2_3:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #2-3'
                  tasks.result.items.metrics.paid.pos_4_10:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #4-10'
                  tasks.result.items.metrics.paid.pos_11_20:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #11-20'
                  tasks.result.items.metrics.paid.pos_21_30:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #21-30'
                  tasks.result.items.metrics.paid.pos_31_40:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #31-40'
                  tasks.result.items.metrics.paid.pos_41_50:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #41-50'
                  tasks.result.items.metrics.paid.pos_51_60:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #51-60'
                  tasks.result.items.metrics.paid.pos_61_70:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #61-70'
                  tasks.result.items.metrics.paid.pos_71_80:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #71-80'
                  tasks.result.items.metrics.paid.pos_81_90:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #81-90'
                  tasks.result.items.metrics.paid.pos_91_100:
                    type: integer
                    description: 'number of paid SERPs where the domain ranks #91-100'
                  tasks.result.items.metrics.paid.etv:
                    type: number
                    description: >-
                      estimated traffic volume estimated paid monthly traffic to
                      the domain calculated as the product of CTR
                      (click-through-rate) and search volume values of all
                      keywords the domain ranks for learn more about how the
                      metric is calculated in this help center article
                  tasks.result.items.metrics.paid.count:
                    type: integer
                    description: total count of paid SERPs that contain the domain
                  tasks.result.items.metrics.paid.estimated_paid_traffic_cost:
                    type: number
                    description: >-
                      estimated cost of monthly search traffic represents the
                      estimated cost of paid monthly traffic (USD) based on etv
                      and cpc values learn more about how the metric is
                      calculated in this help center article
                  tasks.result.items.backlinks_info:
                    type: object
                    description: backlink data for the returned domain
                  tasks.result.items.backlinks_info.referring_domains:
                    type: integer
                    description: number of referring domains
                  tasks.result.items.backlinks_info.referring_main_domains:
                    type: integer
                    description: number of referring main domains
                  tasks.result.items.backlinks_info.referring_pages:
                    type: integer
                    description: number of referring pages
                  tasks.result.items.backlinks_info.dofollow:
                    type: integer
                    description: number of dofollow links
                  tasks.result.items.backlinks_info.backlinks:
                    type: integer
                    description: >-
                      total number of backlinks the total number of backlinks,
                      including dofollow and nofollow links
                  tasks.result.items.backlinks_info.time_update:
                    type: string
                    description: >-
                      date and time when backlink data was updated in the UTC
                      format: "yyyy-mm-dd hh-mm-ss +00:00" example: 2019-11-15
                      12:57:46 +00:00
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