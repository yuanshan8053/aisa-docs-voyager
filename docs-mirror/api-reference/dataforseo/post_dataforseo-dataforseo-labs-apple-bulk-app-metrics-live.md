> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# App Store Bulk App Metrics Live

> This endpoint will provide you with ranking metrics for up to 1000 App Store applications.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/apple/bulk_app_metrics/live
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
  /dataforseo/dataforseo_labs/apple/bulk_app_metrics/live:
    post:
      summary: App Store Bulk App Metrics Live
      description: >-
        This endpoint will provide you with ranking metrics for up to 1000 App
        Store applications.
      operationId: post_dataforseo_dataforseo_labs_apple_bulk_app_metrics_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                app_ids:
                  type: array
                  items:
                    type: string
                  description: >-
                    ids of the apps required field IDs of mobile applications on
                    App Store; you can find the ID in the URL of every app
                    listed on App Store; example: in the URL
                    https://apps.apple.com/us/app/id835599320 the id is
                    835599320; the maximum number of IDs you can specify in this
                    field is 1000
                location_name:
                  type: string
                  description: >-
                    full name of the location required field if you don’t
                    specify location_code Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_name by making a
                    separate request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;
                    Note: this endpoint currently supports the US location only;
                    example: United States
                location_code:
                  type: integer
                  description: >-
                    location code required field if you don’t specify
                    location_name Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_code by making a
                    separate request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;
                    Note: this endpoint currently supports the US location only;
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language required field if you don’t
                    specify language_code Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available languages with their language_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;
                    Note: this endpoint currently supports the English language
                    only; example: English
                language_code:
                  type: string
                  description: >-
                    language code required field if you don’t specify
                    language_name Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available languages with their language_code by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;
                    Note: this endpoint currently supports the English language
                    only example: en
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - app_ids
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
                  tasks.result.app_id:
                    type: string
                    description: id of the app in a POST array
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
                    description: >-
                      contains data related to the ranking app metrics of the
                      specified application
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.app_id:
                    type: string
                    description: id of the app in a POST array
                  tasks.result.items.metrics:
                    type: object
                    description: >-
                      metrics for the ranking keywords of the app ranking data
                      relevant to the keywords that the provided application
                      ranks for on App Store
                  tasks.result.items.metrics.app_store_search_organic:
                    type: object
                    description: ranking data from App Store organic search
                  tasks.result.items.metrics.app_store_search_organic.pos_1:
                    type: integer
                    description: 'number of SERPs where the app ranks #1 in organic results'
                  tasks.result.items.metrics.app_store_search_organic.pos_2_3:
                    type: integer
                    description: >-
                      number of SERPs where the app ranks #2-3 in organic
                      results
                  tasks.result.items.metrics.app_store_search_organic.pos_4_10:
                    type: integer
                    description: >-
                      number of SERPs where the app ranks #4-10 in organic
                      results
                  tasks.result.items.metrics.app_store_search_organic.pos_11_100:
                    type: integer
                    description: >-
                      number of SERPs where the app ranks #11-100 in organic
                      results
                  tasks.result.items.metrics.app_store_search_organic.count:
                    type: integer
                    description: total count of organic SERPs that contain the app
                  tasks.result.items.metrics.app_store_search_organic.search_volume:
                    type: integer
                    description: >-
                      total search volume of the app’s ranking keywords in App
                      Store organic SERP
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