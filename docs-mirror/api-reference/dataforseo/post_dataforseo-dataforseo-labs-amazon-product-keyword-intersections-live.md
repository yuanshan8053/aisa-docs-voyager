> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Keyword Intersections

> This endpoint will provide you with a list of keywords for which the target products intersect in Amazon SERP.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/amazon/product_keyword_intersections/live
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
  /dataforseo/dataforseo_labs/amazon/product_keyword_intersections/live:
    post:
      summary: Keyword Intersections
      description: >-
        This endpoint will provide you with a list of keywords for which the
        target products intersect in Amazon SERP. The returned results are
        specific to the `asins` specified in a POST request. Learn more about
        ASIN in [this help center
        article.](https://dataforseo.com/help-center/asin-in-amazon-api)
      operationId: >-
        post_dataforseo_dataforseo_labs_amazon_product_keyword_intersections_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                asins:
                  type: object
                  description: >-
                    asins of target products required field product IDs of the
                    products for which you need to find keyword intersections;
                    specify the ASINs as in the following example: "asins": {
                    "1": "019005476X", "2": "0190074442" } the maximum number of
                    ASINs you can specify in this object is 20; learn more about
                    the parameter on this help center page
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
                    example: United Kingdom
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
                limit:
                  type: integer
                  description: >-
                    the maximum number of products in the results array optional
                    field default value: 100; maximum value: 1000
                intersection_mode:
                  type: string
                  description: >-
                    mode for finding asin intersections optional field possible
                    values: union, intersect; default value: intersect; learn
                    more about the parameter in this help center guide
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: regex, not_regex, , , >,
                    >=, =, , in, not_in, ilike, not_ilike, like, not_like,
                    match, not_match you can use the % operator with like and
                    not_like, as well as ilike and not_ilike to match any string
                    of zero or more characters example: ["avg_position"," for
                    more information about filters, please refer to Dataforseo
                    Labs – Filters or this help center guide
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    results sorting rules optional field you can use the same
                    values as in the filters array to sort the results possible
                    sorting types: asc – results will be sorted in the ascending
                    order desc – results will be sorted in the descending order
                    you should use a comma to set up a sorting parameter
                    example: ["sum_position,desc"] note that you can set no more
                    than three sorting rules in a single request you should use
                    a comma to separate several sorting rules example:
                    ["intersections,desc","avg_position,asc"] default rule:
                    ["intersections,desc"]
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned keywords optional
                    field default value: 0 if you specify the 10 value, the
                    first ten keywords in the results array will be omitted and
                    the data will be provided for the successive keywords
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
                  tasks.result.asins:
                    type: object
                    description: ASINs in a POST array
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
                  tasks.result.items.keyword_data:
                    type: object
                    description: keyword data for the returned keyword
                  tasks.result.items.keyword_data.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword_data.keyword:
                    type: string
                    description: returned keyword
                  tasks.result.items.keyword_data.location_code:
                    type: integer
                    description: location in a POST array
                  tasks.result.items.keyword_data.language_code:
                    type: string
                    description: language in a POST array
                  tasks.result.items.keyword_data.keyword_info:
                    type: object
                    description: keyword data for the returned keyword
                  tasks.result.items.keyword_data.keyword_info.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword_data.keyword_info.last_updated_time:
                    type: string
                    description: >-
                      date and time when keyword data was updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.keyword_data.keyword_info.search_volume:
                    type: integer
                    description: >-
                      average monthly search volume rate represents the
                      (approximate) number of searches for the returned keyword
                      on Amazon
                  tasks.result.items.intersection_result:
                    type: object
                    description: data on the intersection
                  tasks.result.items.intersection_result.$asin_number:
                    type: object
                    description: intersection data for one of the ASINs in a POST request
                  tasks.result.items.intersection_result.$asin_number.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.intersection_result.$asin_number.type:
                    type: string
                    description: type of element = ‘amazon_serp’
                  tasks.result.items.intersection_result.$asin_number.rank_group:
                    type: integer
                    description: >-
                      position within a group of elements with identical type
                      values positions of elements with different type values
                      are omitted from rank_group
                  tasks.result.items.intersection_result.$asin_number.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in Amazon SERP absolute position among all
                      the elements in SERP
                  tasks.result.items.intersection_result.$asin_number.position:
                    type: string
                    description: >-
                      the alignment of the element in Amazon SERP can take the
                      following values: left, right
                  tasks.result.items.intersection_result.$asin_number.xpath:
                    type: string
                    description: the XPath of the element
                  tasks.result.items.intersection_result.$asin_number.domain:
                    type: string
                    description: Amazon domain
                  tasks.result.items.intersection_result.$asin_number.title:
                    type: string
                    description: product title
                  tasks.result.items.intersection_result.$asin_number.url:
                    type: string
                    description: URL of the product page
                  tasks.result.items.intersection_result.$asin_number.description:
                    type: string
                    description: description of the product
                  tasks.result.items.intersection_result.$asin_number.asin:
                    type: string
                    description: >-
                      ASIN of the product learn more about ASIN in this help
                      center guide
                  tasks.result.items.intersection_result.$asin_number.image_url:
                    type: string
                    description: URL of the product image featured in the results
                  tasks.result.items.intersection_result.$asin_number.price_from:
                    type: number
                    description: 'the regular price of a product example: 49.98'
                  tasks.result.items.intersection_result.$asin_number.price_to:
                    type: number
                    description: 'the upper limit of the product price range example: 384.99'
                  tasks.result.items.intersection_result.$asin_number.currency:
                    type: string
                    description: 'currency in the ISO format example: USD'
                  tasks.result.items.intersection_result.$asin_number.special_offers:
                    type: array
                    items:
                      type: string
                    description: >-
                      special offer details contains special offer details,
                      including coupon and Subscribe & Save discounts
                  tasks.result.items.intersection_result.$asin_number.is_best_seller:
                    type: boolean
                    description: >-
                      “Best Seller” label if the value is true, the product is
                      marked with the “Best Seller” label
                  tasks.result.items.intersection_result.$asin_number.is_amazon_choice:
                    type: boolean
                    description: >-
                      “Amazon’s choice” label if the value is true, the product
                      is marked with the “Amazon’s choice” label
                  tasks.result.items.intersection_result.$asin_number.rating:
                    type: object
                    description: >-
                      the item’s rating the popularity rate based on reviews and
                      displayed in SERP
                  tasks.result.items.intersection_result.$asin_number.rating.rating_type:
                    type: string
                    description: >-
                      the type of rating here you can find the following
                      elements: Max5, Percents, CustomMax
                  tasks.result.items.intersection_result.$asin_number.rating.value:
                    type: integer
                    description: the value of the rating
                  tasks.result.items.intersection_result.$asin_number.rating.votes_count:
                    type: integer
                    description: the amount of feedback
                  tasks.result.items.intersection_result.$asin_number.rating.rating_max:
                    type: integer
                    description: the maximum value for a rating_type
                  tasks.result.items.intersection_result.$asin_number.delivery_info:
                    type: object
                    description: >-
                      delivery information delivery information including free
                      and fast delivery date ranges
                  tasks.result.items.intersection_result.$asin_number.delivery_info.delivery_message:
                    type: string
                    description: >-
                      delivery information message accompanying the delivery
                      information as posted by the seller
                  tasks.result.items.intersection_result.$asin_number.delivery_info.delivery_price:
                    type: object
                    description: >-
                      price for the delivery price of the delivery based on the
                      location you specified in the POST request; if free
                      delivery is available, the value is null
                  tasks.result.items.intersection_result.$asin_number.delivery_info.delivery_price.current:
                    type: number
                    description: current delivery price
                  tasks.result.items.intersection_result.$asin_number.delivery_info.delivery_price.regular:
                    type: number
                    description: regular undiscounted delivery price
                  tasks.result.items.intersection_result.$asin_number.delivery_info.delivery_price.max_value:
                    type: number
                    description: maximum undiscounted delivery price
                  tasks.result.items.intersection_result.$asin_number.delivery_info.delivery_price.currency:
                    type: string
                    description: currency in the ISO format
                  tasks.result.items.intersection_result.$asin_number.delivery_info.delivery_price.is_price_range:
                    type: boolean
                    description: indicates whether the delivery price is a range
                  tasks.result.items.intersection_result.$asin_number.delivery_info.delivery_price.displayed_price:
                    type: string
                    description: price line provided as displayed in Amazon listing
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