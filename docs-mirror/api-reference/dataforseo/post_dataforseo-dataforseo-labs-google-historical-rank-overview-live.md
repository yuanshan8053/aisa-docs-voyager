> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Historical Rank Overview

> This endpoint will provide you with historical data on rankings and traffic of the specified domain, such as domain ranking distribution in SERPs and estimat...



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/google/historical_rank_overview/live
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
  /dataforseo/dataforseo_labs/google/historical_rank_overview/live:
    post:
      summary: Historical Rank Overview
      description: >-
        This endpoint will provide you with historical data on rankings and
        traffic of the specified domain, such as domain ranking distribution in
        SERPs and estimated monthly traffic volume for both organic and paid
        results.
      operationId: post_dataforseo_dataforseo_labs_google_historical_rank_overview_live
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
                    full name of the location required field if you don’t
                    specify location_code Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: United Kingdom
                location_code:
                  type: integer
                  description: >-
                    location code required field if you don’t specify
                    location_name Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_code by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language required field if you don’t
                    specify language_code Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available locations with their language_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    language code required field if you don’t specify
                    language_name Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available locations with their language_code by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: en
                date_from:
                  type: string
                  description: >-
                    starting date of the time range optional field if you don’t
                    specify this field, the data will be provided for the
                    previous 6 months minimal possible value: 2020-10-01 date
                    format: "yyyy-mm-dd"
                date_to:
                  type: string
                  description: >-
                    ending date of the time range optional field if you don’t
                    specify this field, the today’s date will be used by default
                    date format: "yyyy-mm-dd" example: "2021-04-01"
                correlate:
                  type: boolean
                  description: >-
                    correlate data with previously obtained datasets optional
                    field default value: true if you use this parameter, our
                    system will correlate data you obtain now with previously
                    obtained datasets this parameter is intended to mitigate any
                    inconsistencies that may result from changes to our database
                    we recommend always setting correlate to true
                ignore_synonyms:
                  type: boolean
                  description: >-
                    ignore highly similar keywords optional field if set to
                    true, only data based on core keywords will be returned,
                    data for all highly similar keywords will be excluded;
                    default value: false
                include_clickstream_data:
                  type: boolean
                  description: >-
                    include or exclude data from clickstream-based metrics in
                    the result optional field if the parameter is set to true,
                    you will receive clickstream_etv,
                    clickstream_gender_distribution, and
                    clickstream_age_distribution fields with clickstream data in
                    the response; default value: false; Note: historical
                    clickstream data is available from 2024/05 (May, 2024); with
                    this parameter enabled, you will be charged double the price
                    for the request; learn more about how clickstream-based
                    metrics are calculated in this help center article
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - target
                - location_name
                - location_code
                - language_name
                - language_code
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
                    description: contains historical ranking and traffic data
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.year:
                    type: integer
                    description: year for which the data is provided
                  tasks.result.items.month:
                    type: integer
                    description: month for which the data is provided
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
                      ranked elements were found for the indicated target
                  tasks.result.items.metrics.organic.is_up:
                    type: integer
                    description: >-
                      rank went up indicates how many ranked elements of the
                      indicated target went up
                  tasks.result.items.metrics.organic.is_down:
                    type: integer
                    description: >-
                      rank went down indicates how many ranked elements of the
                      indicated target went down
                  tasks.result.items.metrics.organic.is_lost:
                    type: integer
                    description: >-
                      lost ranked elements indicates how many ranked elements of
                      the indicated target were previously presented in SERPs,
                      but weren’t found during the last check
                  tasks.result.items.metrics.organic.clickstream_etv:
                    type: integer
                    description: >-
                      estimated traffic volume based on clickstream data
                      calculated as the product of click-through-rate and
                      clickstream search volume values of all keywords the
                      domain ranks for to retrieve results for this field, the
                      parameter include_clickstream_data must be set to true
                      learn more about how the metric is calculated in this help
                      center article
                  tasks.result.items.metrics.organic.clickstream_gender_distribution:
                    type: object
                    description: >-
                      distribution of estimated clickstream-based metrics by
                      gender to retrieve results for this field, the parameter
                      include_clickstream_data must be set to true learn more
                      about how the metric is calculated in this help center
                      article
                  tasks.result.items.metrics.organic.female:
                    type: integer
                    description: number of female users in the relevant clickstream dataset
                  tasks.result.items.metrics.organic.male:
                    type: integer
                    description: number of male users in the relevant clickstream dataset
                  tasks.result.items.metrics.organic.clickstream_age_distribution:
                    type: object
                    description: >-
                      distribution of clickstream-based metrics by age to
                      retrieve results for this field, the parameter
                      include_clickstream_data must be set to true learn more
                      about how the metric is calculated in this help center
                      article
                  tasks.result.items.metrics.organic.18-24:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 18-24 age range
                  tasks.result.items.metrics.organic.25-34:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 25-34 age range
                  tasks.result.items.metrics.organic.35-44:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 35-44 age range
                  tasks.result.items.metrics.organic.45-54:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 45-54 age range
                  tasks.result.items.metrics.organic.55-64:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 55-64 age range
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
                      ranked elements were found for the indicated target
                  tasks.result.items.metrics.paid.is_up:
                    type: integer
                    description: >-
                      rank went up indicates how many ranked elements of the
                      indicated target went up
                  tasks.result.items.metrics.paid.is_down:
                    type: integer
                    description: >-
                      rank went down indicates how many ranked elements of the
                      indicated target went down
                  tasks.result.items.metrics.paid.is_lost:
                    type: integer
                    description: >-
                      lost ranked elements indicates how many ranked elements of
                      the indicated target were previously presented in SERPs,
                      but weren’t found during the last check
                  tasks.result.items.metrics.paid.clickstream_etv:
                    type: integer
                    description: >-
                      estimated traffic volume based on clickstream data
                      calculated as the product of click-through-rate and
                      clickstream search volume values of all keywords the
                      domain ranks for to retrieve results for this field, the
                      parameter include_clickstream_data must be set to true
                      learn more about how the metric is calculated in this help
                      center article
                  tasks.result.items.metrics.paid.clickstream_gender_distribution:
                    type: object
                    description: >-
                      distribution of estimated clickstream-based metrics by
                      gender to retrieve results for this field, the parameter
                      include_clickstream_data must be set to true learn more
                      about how the metric is calculated in this help center
                      article
                  tasks.result.items.metrics.paid.female:
                    type: integer
                    description: number of female users in the relevant clickstream dataset
                  tasks.result.items.metrics.paid.male:
                    type: integer
                    description: number of male users in the relevant clickstream dataset
                  tasks.result.items.metrics.paid.clickstream_age_distribution:
                    type: object
                    description: >-
                      distribution of clickstream-based metrics by age to
                      retrieve results for this field, the parameter
                      include_clickstream_data must be set to true learn more
                      about how the metric is calculated in this help center
                      article
                  tasks.result.items.metrics.paid.18-24:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 18-24 age range
                  tasks.result.items.metrics.paid.25-34:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 25-34 age range
                  tasks.result.items.metrics.paid.35-44:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 35-44 age range
                  tasks.result.items.metrics.paid.45-54:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 45-54 age range
                  tasks.result.items.metrics.paid.55-64:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 55-64 age range
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