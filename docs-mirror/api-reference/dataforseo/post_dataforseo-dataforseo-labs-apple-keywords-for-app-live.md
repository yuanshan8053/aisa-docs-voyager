> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# App Store Keywords For App Live

> This endpoint will provide you with a list of keywords for which the target app ranks on App Store.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/apple/keywords_for_app/live
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
  /dataforseo/dataforseo_labs/apple/keywords_for_app/live:
    post:
      summary: App Store Keywords For App Live
      description: >-
        This endpoint will provide you with a list of keywords for which the
        target app ranks on App Store. You will obtain keyword data and discover
        the app’s ranking position for each returned keyword.
      operationId: post_dataforseo_dataforseo_labs_apple_keywords_for_app_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                app_id:
                  type: string
                  description: >-
                    id of the app required field ID of the mobile application on
                    App Store; you can find the ID in the URL of every app
                    listed on App Store; example: in the URL
                    https://apps.apple.com/us/app/id835599320 the id is
                    835599320
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
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: , , >, >=, =, , in,
                    not_in example:
                    ["keyword_data.keyword_info.search_volume",">",500]
                    [["keyword_data.keyword_info.search_volume","",500],"and",["ranked_serp_element.serp_item.rank_group",">=","10"]]
                    for more information about filters, please refer to
                    Dataforseo Labs – Filters or this help center guide
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    results sorting rules optional field you can use the same
                    values as in the filters array to sort the results; possible
                    sorting types: asc – results will be sorted in the ascending
                    order; desc – results will be sorted in the descending
                    order; you should use a comma to specify a sorting type;
                    example: ["ranked_serp_element.serp_item.rank_group,asc"]
                    Note: you can set no more than three sorting rules in a
                    single request; you should use a comma to separate several
                    sorting rules; example:
                    ["ranked_serp_element.serp_item.rank_group,desc","keyword_data.keyword_info.search_volume,asc"]
                    default rule:
                    ["keyword_data.keyword_info.search_volume,desc"] Note: if
                    the item_types array contains item types that are different
                    from organic, the results will be ordered by the first item
                    type in the array
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned keywords optional field
                    default value: 100 maximum value: 1000
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
                - app_id
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
                      contains data related to the ranking keywords for the app
                      specified in the app_id field
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
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
                    description: location code in a POST array
                  tasks.result.items.keyword_data.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.items.keyword_data.keyword_info:
                    type: object
                    description: keyword info for the returned keyword
                  tasks.result.items.keyword_data.keyword_info.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword_data.keyword_info.last_updated_time:
                    type: string
                    description: >-
                      date and time when keyword data was updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.keyword_data.keyword_info.competition:
                    type: number
                    description: >-
                      competition represents the relative amount of competition
                      associated with the given keyword; the value is based on
                      Google Ads data and can be between 0 and 1 (inclusive); in
                      this case, will equal null
                  tasks.result.items.keyword_data.keyword_info.competition_level:
                    type: string
                    description: >-
                      competition level represents the relative level of
                      competition associated with the given keyword in paid SERP
                      only; possible values: LOW, MEDIUM, HIGH if competition
                      level is unknown, the value is null; learn more about the
                      metric in this help center article; in this case, will
                      equal null
                  tasks.result.items.keyword_data.keyword_info.cpc:
                    type: number
                    description: >-
                      cost-per-click represents the average cost per click (USD)
                      historically paid for the keyword; in this case, will
                      equal null
                  tasks.result.items.keyword_data.keyword_info.search_volume:
                    type: integer
                    description: >-
                      average monthly search volume rate represents the
                      (approximate) number of searches for the given keyword on
                      App Store
                  tasks.result.items.keyword_data.keyword_info.low_top_of_page_bid:
                    type: number
                    description: >-
                      minimum bid for the ad to be displayed at the top of the
                      first page indicates the value greater than about 20% of
                      the lowest bids for which ads were displayed (based on
                      Google Ads statistics for advertisers) the value may
                      differ depending on the location specified in a POST
                      request; in this case, will equal null
                  tasks.result.items.keyword_data.keyword_info.high_top_of_page_bid:
                    type: number
                    description: >-
                      maximum bid for the ad to be displayed at the top of the
                      first page indicates the value greater than about 80% of
                      the lowest bids for which ads were displayed (based on
                      Google Ads statistics for advertisers) the value may
                      differ depending on the location specified in a POST
                      request; in this case, will equal null
                  tasks.result.items.keyword_data.keyword_info.categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      product and service categories you can download the full
                      list of possible categories; in this case, will equal null
                  tasks.result.items.keyword_data.keyword_info.monthly_searches:
                    type: array
                    items:
                      type: string
                    description: >-
                      monthly searches represents the (approximate) number of
                      searches for this keyword (as available for the past
                      twelve months), targeted to the specified geographic
                      locations; in this case, will equal null
                  tasks.result.items.ranked_serp_element:
                    type: object
                    description: >-
                      contains data on the domain’s SERP element found for the
                      returned keyword
                  tasks.result.items.ranked_serp_element.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.ranked_serp_element.serp_item:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains data on the SERP element the list of supported
                      SERP elements can be found below
                  tasks.result.items.ranked_serp_element.serp_item.type:
                    type: string
                    description: >-
                      type of the SERP element possible values:
                      app_store_search_organic
                  tasks.result.items.ranked_serp_element.serp_item.rank_group:
                    type: integer
                    description: >-
                      position within a group of elements with identical type
                      values positions of elements with different type values
                      are omitted from rank_group
                  tasks.result.items.ranked_serp_element.serp_item.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in SERP absolute position among all the
                      elements in SERP
                  tasks.result.items.ranked_serp_element.serp_item.position:
                    type: string
                    description: >-
                      the alignment of the element in SERP can take the
                      following values: left, right
                  tasks.result.items.ranked_serp_element.serp_item.app_id:
                    type: string
                    description: id of the app
                  tasks.result.items.ranked_serp_element.serp_item.title:
                    type: string
                    description: title of the app
                  tasks.result.items.ranked_serp_element.serp_item.url:
                    type: string
                    description: URL to the app page on App Store
                  tasks.result.items.ranked_serp_element.serp_item.icon:
                    type: string
                    description: URL to the app icon
                  tasks.result.items.ranked_serp_element.serp_item.reviews_count:
                    type: integer
                    description: the total number of reviews of the app
                  tasks.result.items.ranked_serp_element.serp_item.rating:
                    type: object
                    description: average rating of the app
                  tasks.result.items.ranked_serp_element.serp_item.rating.rating_type:
                    type: string
                    description: 'the type of the rating can take the following values: Max5'
                  tasks.result.items.ranked_serp_element.serp_item.rating.value:
                    type: number
                    description: the value of the rating
                  tasks.result.items.ranked_serp_element.serp_item.rating.votes_count:
                    type: integer
                    description: >-
                      the amount of feedback in this case, the value will be
                      null
                  tasks.result.items.ranked_serp_element.serp_item.rating.rating_max:
                    type: integer
                    description: >-
                      the maximum value for a rating_type the maximum value for
                      Max5 is 5
                  tasks.result.items.ranked_serp_element.serp_item.is_free:
                    type: boolean
                    description: indicates whether the app is free
                  tasks.result.items.ranked_serp_element.serp_item.is_free.current:
                    type: number
                    description: >-
                      current price refers to the current price indicated in the
                      element
                  tasks.result.items.ranked_serp_element.serp_item.is_free.regular:
                    type: number
                    description: >-
                      regular price refers to the regular price indicated in the
                      element
                  tasks.result.items.ranked_serp_element.serp_item.is_free.max_value:
                    type: number
                    description: >-
                      the maximum price refers to the maximum price indicated in
                      the element
                  tasks.result.items.ranked_serp_element.serp_item.is_free.currency:
                    type: string
                    description: >-
                      currency of the listed price ISO code of the currency
                      applied to the price
                  tasks.result.items.ranked_serp_element.serp_item.is_free.is_price_range:
                    type: boolean
                    description: >-
                      price is provided as a range indicates whether a price is
                      provided in a range
                  tasks.result.items.ranked_serp_element.serp_item.is_free.displayed_price:
                    type: string
                    description: >-
                      price string in the result raw price string as provided in
                      the result
                  tasks.result.items.ranked_serp_element.check_url:
                    type: string
                    description: >-
                      direct URL to search engine results you can use it to make
                      sure that we provided accurate results
                  tasks.result.items.ranked_serp_element.se_results_count:
                    type: string
                    description: number of search results for the returned keyword
                  tasks.result.items.ranked_serp_element.last_updated_time:
                    type: string
                    description: >-
                      date and time when SERP data was updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.ranked_serp_element.previous_updated_time:
                    type: string
                    description: >-
                      previous to the most recent date and time when SERP data
                      was updated in the UTC format: “yyyy-mm-dd hh-mm-ss
                      +00:00” example: 2019-10-15 12:57:46 +00:00; in this case,
                      will equal null
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