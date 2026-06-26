> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Domain Rank Overview

> This endpoint will provide you with ranking and traffic data from organic and paid search for the specified domain.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/google/domain_rank_overview/live
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
  /dataforseo/dataforseo_labs/google/domain_rank_overview/live:
    post:
      summary: Domain Rank Overview
      description: >-
        This endpoint will provide you with ranking and traffic data from
        organic and paid search for the specified domain. You will be able to
        review the domain ranking distribution in SERPs as well as estimated
        monthly traffic volume for both organic and paid results.
      operationId: post_dataforseo_dataforseo_labs_google_domain_rank_overview_live
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
                    domain required field the domain name of the target website
                    the domain should be specified without https:// and www.
                location_name:
                  type: string
                  description: >-
                    full name of the location optional field if you use this
                    field, you don’t need to specify location_code you can
                    receive the list of available locations with their
                    location_name by making a separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    ignore this field to get the results for all available
                    locations example: United Kingdom
                location_code:
                  type: integer
                  description: >-
                    location code optional field if you use this field, you
                    don’t need to specify location_name you can receive the list
                    of available locations with their location_code by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    ignore this field to get the results for all available
                    locations example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language optional field if you use this
                    field, you don’t need to specify language_code you can
                    receive the list of available languages with their
                    language_name by making a separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    ignore this field to get the results for all available
                    languages example: English
                language_code:
                  type: string
                  description: >-
                    language code optional field if you use this field, you
                    don’t need to specify language_name you can receive the list
                    of available languages with their language_code by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    ignore this field to get the results for all available
                    languages example: en
                ignore_synonyms:
                  type: boolean
                  description: >-
                    ignore highly similar keywords optional field if set to
                    true, all highly similar keywords will be excluded from the
                    ranking and traffic calculations, the results will be based
                    on data for main keywords from groups of synonyms default
                    value: false
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned results for domain optional
                    field default value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned items optional field
                    default value: 0 if you specify the 10 value, the first ten
                    items in the results array will be omitted and the data will
                    be provided for the successive items
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
                  tasks.result.se_type:
                    type: string
                    description: search engine type
                  tasks.result.target:
                    type: string
                    description: target domain in a POST array
                  tasks.result.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.total_count:
                    type: integer
                    description: >-
                      total amount of results in our database relevant to your
                      request
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains ranking and traffic data
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.items.language_code:
                    type: string
                    description: language code in a POST array
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
                      (USD) for all keywords that a domain ranks for the metric
                      is calculated as the product of organic etv and paid cpc
                      values and indicates the cost of driving the estimated
                      volume of monthly organic traffic through PPC advertising
                      in Google Search learn more about how the metric is
                      calculated in this help center article
                  tasks.result.items.metrics.organic.is_new:
                    type: integer
                    description: >-
                      number of new ranked elements indicates how many new
                      ranked elements were found for this domain
                  tasks.result.items.metrics.organic.is_up:
                    type: integer
                    description: >-
                      rank went up indicates how many ranked elements of this
                      domain went up in Google Search
                  tasks.result.items.metrics.organic.is_down:
                    type: integer
                    description: >-
                      rank went down indicates how many ranked elements of this
                      domain went down in Google Search
                  tasks.result.items.metrics.organic.is_lost:
                    type: integer
                    description: >-
                      lost ranked elements indicates how many ranked elements of
                      this domain were previously presented in SERPs, but
                      weren’t found during the last check
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
                  tasks.result.items.metrics.paid.is_new:
                    type: integer
                    description: >-
                      number of new ranked elements indicates how many new
                      ranked elements were found for this domain
                  tasks.result.items.metrics.paid.is_up:
                    type: integer
                    description: >-
                      rank went up indicates how many ranked elements of this
                      domain went up in Google Search
                  tasks.result.items.metrics.paid.is_down:
                    type: integer
                    description: >-
                      rank went down indicates how many ranked elements of this
                      domain went down in Google Search
                  tasks.result.items.metrics.paid.is_lost:
                    type: integer
                    description: >-
                      lost ranked elements indicates how many ranked elements of
                      this domain were previously presented in SERPs, but
                      weren’t found during the last check
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