> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Rank Overview

> This endpoint will provide you with ranking data from organic and paid Amazon SERPs for the target products.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/amazon/product_rank_overview/live
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
  /dataforseo/dataforseo_labs/amazon/product_rank_overview/live:
    post:
      summary: Product Rank Overview
      description: >-
        This endpoint will provide you with ranking data from organic and paid
        Amazon SERPs for the target products. The returned results are specific
        to the `asins` specified in a POST request. Learn more about ASIN in
        [this help center
        article.](https://dataforseo.com/help-center/asin-in-amazon-api)
      operationId: post_dataforseo_dataforseo_labs_amazon_product_rank_overview_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                asins:
                  type: array
                  items:
                    type: string
                  description: >-
                    product IDs to compare required field product IDs to receive
                    ranking data for; the maximum number of ASINs you can
                    specify in this array is 1000; you can receive the asin
                    parameter by making a separate request to the Amazon
                    Products endpoint Note: all letters in ASIN code must be
                    specified in uppercase format; example: B01LW2SL7R
                location_name:
                  type: string
                  description: >-
                    full name of the location required field if don’t specify
                    location_code you can receive the list of available
                    locations with their location_name by making a separate
                    request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;
                    Note: this endpoint currently supports the US, Egypt, Saudi
                    Arabia, and the United Arab Emirates locations only;
                    example: United States
                location_code:
                  type: integer
                  description: >-
                    location code required field if don’t specify location_name
                    you can receive the list of available locations with their
                    location_code by making a separate request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;
                    Note: this endpoint currently supports the US, Egypt, Saudi
                    Arabia, and the United Arab Emirates locations only;
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language required field if don’t specify
                    language_code you can receive the list of available
                    languages with their language_name by making a separate
                    request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    language code required field if don’t specify language_name
                    you can receive the list of available languages with their
                    language_code by making a separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: en
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - asins
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
                    description: >-
                      contains detected Amazon product competitors and related
                      data
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.asin:
                    type: string
                    description: >-
                      ASIN of the product unique product identifier on Amazon;
                      for more information, refer to this help center guide
                  tasks.result.items.metrics:
                    type: object
                    description: average keyword position of the product
                  tasks.result.items.metrics.amazon_serp:
                    type: object
                    description: ranking data from Amazon organic SERP
                  tasks.result.items.metrics.amazon_serp.pos_1:
                    type: integer
                    description: 'number of organic SERPs where the product ranks #1'
                  tasks.result.items.metrics.amazon_serp.pos_2_3:
                    type: integer
                    description: 'number of organic SERPs where the product ranks #2-3'
                  tasks.result.items.metrics.amazon_serp.pos_4_10:
                    type: integer
                    description: 'number of organic SERPs where the product ranks #4-10'
                  tasks.result.items.metrics.amazon_serp.pos_11_100:
                    type: integer
                    description: 'number of organic SERPs where the product ranks #11-100'
                  tasks.result.items.metrics.amazon_serp.count:
                    type: integer
                    description: >-
                      total count of Amazon organic SERPs that contain the
                      product
                  tasks.result.items.metrics.amazon_serp.search_volume:
                    type: integer
                    description: >-
                      total search volume of the product’s ranking keywords in
                      organic SERP
                  tasks.result.items.metrics.amazon_paid:
                    type: object
                    description: ranking data from Amazon paid SERP
                  tasks.result.items.metrics.amazon_paid.pos_1:
                    type: integer
                    description: 'number of paid SERPs where the product ranks #1'
                  tasks.result.items.metrics.amazon_paid.pos_2_3:
                    type: integer
                    description: 'number of paid SERPs where the product ranks #2-3'
                  tasks.result.items.metrics.amazon_paid.pos_4_10:
                    type: integer
                    description: 'number of paid SERPs where the product ranks #4-10'
                  tasks.result.items.metrics.amazon_paid.pos_11_100:
                    type: integer
                    description: 'number of paid SERPs where the product ranks #11-100'
                  tasks.result.items.metrics.amazon_paid.count:
                    type: integer
                    description: total count of Amazon paid SERPs that contain the product
                  tasks.result.items.metrics.amazon_paid.search_volume:
                    type: integer
                    description: >-
                      total search volume of the product’s ranking keywords in
                      paid SERP
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