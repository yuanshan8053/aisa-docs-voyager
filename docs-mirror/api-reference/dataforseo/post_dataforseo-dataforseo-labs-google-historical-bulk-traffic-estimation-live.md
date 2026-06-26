> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Historical Bulk Traffic Estimation

> This endpoint will provide you with historical monthly traffic volumes for up to 1,000 domains collected within the specified time range through October 2020.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/google/historical_bulk_traffic_estimation/live
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
  /dataforseo/dataforseo_labs/google/historical_bulk_traffic_estimation/live:
    post:
      summary: Historical Bulk Traffic Estimation
      description: >-
        This endpoint will provide you with historical monthly traffic volumes
        for up to 1,000 domains collected within the specified time range
        through October 2020. If you do not specify the range, data will be
        returned for the previous 12 months. Along with organic search traffic
        estimations, you will also get separate values for paid search, featured
        snippet, and local pack results.
      operationId: >-
        post_dataforseo_dataforseo_labs_google_historical_bulk_traffic_estimation_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                targets:
                  type: array
                  items:
                    type: string
                  description: >-
                    target domains and subdomains required field you can specify
                    domains and subdomains in this field; domains and subdomains
                    should be specified without https:// and www.; you can set
                    up to 1000 domains or subdomains
                location_name:
                  type: string
                  description: >-
                    full name of the location if you use this field, you don’t
                    have to specify location_code you can receive the list of
                    available locations with their location_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    ignore this field to get the results for all available
                    locations example: United Kingdom
                location_code:
                  type: integer
                  description: >-
                    location code if you use this field, you don’t have to
                    specify location_name you can receive the list of available
                    locations with their location_code by making a separate
                    request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    ignore this field to get the results for all available
                    locations example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language if you use this field, you don’t
                    need to specify language_code you can receive the list of
                    available languages with their language_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    ignore this field to get the results for all available
                    languages example: English
                language_code:
                  type: string
                  description: >-
                    language code if you use this field, you don’t need to
                    specify language_name you can receive the list of available
                    languages with their language_code by making a separate
                    request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    ignore this field to get the results for all available
                    languages example: en
                date_from:
                  type: string
                  description: >-
                    starting date of the time range optional field if you don’t
                    specify this field, the data will be provided for the
                    previous 12 months minimal possible value: 2020-10-01 date
                    format: "yyyy-mm-dd"
                date_to:
                  type: string
                  description: >-
                    ending date of the time range optional field if you don’t
                    specify this field, the today’s date will be used by
                    default; date format: "yyyy-mm-dd" example: "2021-04-01"
                ignore_synonyms:
                  type: boolean
                  description: >-
                    ignore highly similar keywords optional field if set to
                    true, only core keywords will be returned, all highly
                    similar keywords will be excluded; default value: false
                item_types:
                  type: array
                  items:
                    type: string
                  description: >-
                    display results by item type optional field indicates the
                    type of search results included in the response; Note: if
                    the item_types array contains item types that are different
                    from organic, the results will be ordered by the first item
                    type in the array; possible values: ["organic", "paid",
                    "featured_snippet", "local_pack"] default value: ["organic",
                    "paid"]
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
                  tasks.result.se_type:
                    type: string
                    description: search engine type
                  tasks.result.location_code:
                    type: integer
                    description: >-
                      location code in a POST array if there is no data, then
                      the value is null
                  tasks.result.language_code:
                    type: string
                    description: >-
                      language code in a POST array if there is no data, then
                      the value is null
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
                    description: array of items with relevant traffic estimation data
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.target:
                    type: string
                    description: target domain in a POST array
                  tasks.result.items.metrics:
                    type: object
                    description: traffic data relevant to the specified domain
                  tasks.result.items.metrics.organic:
                    type: array
                    items:
                      type: string
                    description: traffic data from organic search
                  tasks.result.items.metrics.organic.year:
                    type: integer
                    description: year for which the data is provided
                  tasks.result.items.metrics.organic.month:
                    type: integer
                    description: month for which the data is provided
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
                  tasks.result.items.metrics.paid:
                    type: array
                    items:
                      type: string
                    description: traffic data from paid search
                  tasks.result.items.metrics.paid.year:
                    type: integer
                    description: year for which the data is provided
                  tasks.result.items.metrics.paid.month:
                    type: integer
                    description: month for which the data is provided
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
                  tasks.result.items.metrics.featured_snippet:
                    type: array
                    items:
                      type: string
                    description: >-
                      traffic data from the featured snippet results in Google
                      SERP
                  tasks.result.items.metrics.featured_snippet.year:
                    type: integer
                    description: year for which the data is provided
                  tasks.result.items.metrics.featured_snippet.month:
                    type: integer
                    description: month for which the data is provided
                  tasks.result.items.metrics.featured_snippet.etv:
                    type: number
                    description: >-
                      estimated traffic volume estimated paid monthly traffic to
                      the domain calculated as the product of CTR
                      (click-through-rate) and search volume values of all
                      keywords in the category that the domain ranks for learn
                      more about how the metric is calculated in this help
                      center article
                  tasks.result.items.metrics.featured_snippet.count:
                    type: integer
                    description: >-
                      total count of featured snippet items that contain the
                      domain
                  tasks.result.items.metrics.local_pack:
                    type: array
                    items:
                      type: string
                    description: traffic data from the local pack results in SERP
                  tasks.result.items.metrics.local_pack.year:
                    type: integer
                    description: year for which the data is provided
                  tasks.result.items.metrics.local_pack.month:
                    type: integer
                    description: month for which the data is provided
                  tasks.result.items.metrics.local_pack.etv:
                    type: number
                    description: >-
                      estimated traffic volume estimated paid monthly traffic to
                      the domain calculated as the product of CTR
                      (click-through-rate) and search volume values of all
                      keywords in the category that the domain ranks for learn
                      more about how the metric is calculated in this help
                      center article
                  tasks.result.items.metrics.local_pack.count:
                    type: integer
                    description: total count of local pack items that contain the domain
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