> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Google App Listings Search Results

> This endpoint will provide you with a list of apps published on Google Play along with additional information: its ID, icon, reviews count, rating, price, an...



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/app_data/google/app_listings/search/live
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
  /dataforseo/app_data/google/app_listings/search/live:
    post:
      summary: Live Google App Listings Search Results
      description: >-
        This endpoint will provide you with a list of apps published on Google
        Play along with additional information: its ID, icon, reviews count,
        rating, price, and other data. The results are specific to the `title`,
        `description`, and `categories` parameters specified in the API request.
      operationId: post_dataforseo_app_data_google_app_listings_search_live
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                categories:
                  type: array
                  items:
                    type: string
                  description: >-
                    app categories optional field the categories you specify are
                    used to search for app listings; you can get the full list
                    of available app listing categories by this link you can
                    specify up to 10 categories
                description:
                  type: string
                  description: >-
                    keyword in the app’s description optional field keywords
                    that occur in the description of the app; can contain up to
                    200 characters
                title:
                  type: string
                  description: >-
                    keyword in the app’s title optional field keywords that
                    occur in the title of the app; can contain up to 200
                    characters
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: regex, not_regex, , , >,
                    >=, =, , in, not_in, like, not_like you can use the %
                    operator with like and not_like to match any string of zero
                    or more characters example: ["item.rating.value",">",3] you
                    can receive the list of available filters by making a
                    separate request to
                    https://api.dataforseo.com/v3/app_data/google/app_listings/available_filters
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
                    example: ["item.installs_count,asc"] note that you can set
                    no more than three sorting rules in a single request you
                    should use a comma to separate several sorting rules
                    example:
                    ["item.rating.value,desc","item.installs_count,asc"]
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned apps optional field default
                    value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned apps optional field
                    default value: 0 if you specify the 10 value, the first ten
                    entities in the results array will be omitted and the data
                    will be provided for the successive entities Note: we
                    recommend using this parameter only when retrieving up to
                    10,000 results for retrieving over 10,000 results, use the
                    offset_token instead.
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
                      the number of tasks in the tasks array that were returned
                      an error
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
                    description: the total number of relevant results in the database
                  tasks.result.count:
                    type: integer
                    description: the number of items in the results array
                  tasks.result.offset:
                    type: integer
                    description: offset in the results array of returned apps
                  tasks.result.offset_token:
                    type: string
                    description: >-
                      token for subsequent requests you can use this parameter
                      in the POST request to avoid timeouts while trying to
                      obtain over 100,000 results in a single request
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: array of apps and related data
                  tasks.result.items.app_id:
                    type: string
                    description: ID of the returned app
                  tasks.result.items.se_domain:
                    type: string
                    description: search engine domain in a POST array
                  tasks.result.items.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.items.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.items.check_url:
                    type: string
                    description: >-
                      direct URL to search engine results you can use it to make
                      sure that we provided accurate results
                  tasks.result.items.time_update:
                    type: string
                    description: >-
                      date and time when SERP data was last updated in the ISO
                      8601 format: “YYYY-MM-DDThh:mm:ss.sssssssZ” example:
                      2023-05-23 10:16:19 +00:00
                  tasks.result.items.item:
                    type: object
                    description: detailed information about the app
                  tasks.result.items.item.type:
                    type: string
                    description: >-
                      the item’s type possible item types:
                      "google_play_info_organic"
                  tasks.result.items.item.rank_group:
                    type: integer
                    description: >-
                      position within a group of elements with identical type
                      values positions of elements with different type values
                      are omitted from rank_group
                  tasks.result.items.item.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank among all the listed apps absolute position
                      among all apps on the list
                  tasks.result.items.item.position:
                    type: string
                    description: >-
                      the alignment of the element in SERP can take the
                      following values: left
                  tasks.result.items.item.app_id:
                    type: string
                    description: ID of the returned app
                  tasks.result.items.item.title:
                    type: string
                    description: title of the returned app
                  tasks.result.items.item.url:
                    type: string
                    description: URL to the app page on Google Play
                  tasks.result.items.item.icon:
                    type: string
                    description: URL to the app icon
                  tasks.result.items.item.description:
                    type: string
                    description: description of the returned app
                  tasks.result.items.item.reviews_count:
                    type: integer
                    description: the total number of reviews the app has
                  tasks.result.items.item.rating:
                    type: object
                    description: average rating of the app
                  tasks.result.items.item.rating.rating_type:
                    type: string
                    description: 'the type of the rating can take the following values: Max5'
                  tasks.result.items.item.rating.value:
                    type: number
                    description: the value of the rating
                  tasks.result.items.item.rating.votes_count:
                    type: integer
                    description: >-
                      the amount of feedback in this case, the value will be
                      null
                  tasks.result.items.item.rating.rating_max:
                    type: integer
                    description: >-
                      the maximum value for a rating_type the maximum value for
                      Max5 is 5
                  tasks.result.items.item.price:
                    type: object
                    description: price of the app
                  tasks.result.items.item.price.current:
                    type: number
                    description: >-
                      current price refers to the current price indicated in the
                      element
                  tasks.result.items.item.price.regular:
                    type: number
                    description: >-
                      regular price refers to the regular price indicated in the
                      element
                  tasks.result.items.item.price.max_value:
                    type: number
                    description: >-
                      the maximum price refers to the maximum price indicated in
                      the element
                  tasks.result.items.item.price.currency:
                    type: string
                    description: >-
                      currency of the listed price ISO code of the currency
                      applied to the price
                  tasks.result.items.item.price.is_price_range:
                    type: boolean
                    description: >-
                      price is provided as a range indicates whether a price is
                      provided in a range
                  tasks.result.items.item.price.displayed_price:
                    type: string
                    description: >-
                      price string in the result raw price string as provided in
                      the result
                  tasks.result.items.item.is_free:
                    type: boolean
                    description: indicates whether the app is free
                  tasks.result.items.item.main_category:
                    type: string
                    description: app category Google Play category relevant to the app
                  tasks.result.items.item.installs:
                    type: string
                    description: approximate number of app installs
                  tasks.result.items.item.installs_count:
                    type: integer
                    description: accurate number of app installs
                  tasks.result.items.item.developer:
                    type: string
                    description: name of the app developer
                  tasks.result.items.item.developer_id:
                    type: string
                    description: ID of the developer on Google Play
                  tasks.result.items.item.developer_url:
                    type: string
                    description: URL to the developer page on Google Play
                  tasks.result.items.item.developer_email:
                    type: string
                    description: email address of the developer
                  tasks.result.items.item.developer_address:
                    type: string
                    description: physical address of the developer
                  tasks.result.items.item.developer_website:
                    type: string
                    description: official website of the developer
                  tasks.result.items.item.version:
                    type: string
                    description: current version of the app
                  tasks.result.items.item.minimum_os_version:
                    type: string
                    description: minimum OS version required to install the app
                  tasks.result.items.item.size:
                    type: string
                    description: size of the app
                  tasks.result.items.item.released_date:
                    type: string
                    description: >-
                      date and time when the app was released in the UTC format:
                      “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15 12:57:46
                      +00:00
                  tasks.result.items.item.last_update_date:
                    type: string
                    description: >-
                      date and time when the app was last updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.item.update_notes:
                    type: string
                    description: >-
                      update notes contains the latest update notes from the
                      developer
                  tasks.result.items.item.images:
                    type: array
                    items:
                      type: string
                    description: >-
                      app images contains URLs to the images published on the
                      app page on Google Play
                  tasks.result.items.item.videos:
                    type: array
                    items:
                      type: string
                    description: >-
                      app videos contains URLs to the video published on the app
                      page on Google Play
                  tasks.result.items.item.similar_apps:
                    type: array
                    items:
                      type: string
                    description: >-
                      similar apps displays apps similar to the app in a POST
                      request
                  tasks.result.items.item.similar_apps.app_id:
                    type: string
                    description: ID of the app
                  tasks.result.items.item.similar_apps.title:
                    type: string
                    description: title of the app
                  tasks.result.items.item.similar_apps.url:
                    type: string
                    description: URL to the app page on Google Play
                  tasks.result.items.item.more_apps_by_developer:
                    type: array
                    items:
                      type: string
                    description: >-
                      similar apps information about apps built by the same
                      developer
                  tasks.result.items.item.more_apps_by_developer.app_id:
                    type: string
                    description: ID of the app
                  tasks.result.items.item.more_apps_by_developer.title:
                    type: string
                    description: title of the app
                  tasks.result.items.item.more_apps_by_developer.url:
                    type: string
                    description: URL to the app page on Google Play
                  tasks.result.items.item.genres:
                    type: array
                    items:
                      type: string
                    description: app genres contains relevant app categories
                  tasks.result.items.item.tags:
                    type: array
                    items:
                      type: string
                    description: app tags contains relevant app tags
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