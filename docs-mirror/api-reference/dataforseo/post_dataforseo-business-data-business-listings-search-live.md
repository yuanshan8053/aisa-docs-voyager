> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Business Listings Search Tasks

> Business Listings Search API provides results containing information about business entities listed on Google Maps in the specified categories.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/business_data/business_listings/search/live
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
  /dataforseo/business_data/business_listings/search/live:
    post:
      summary: Live Business Listings Search Tasks
      description: >-
        Business Listings Search API provides results containing information
        about business entities listed on Google Maps in the specified
        categories. You will receive the address, contacts, rating, working
        hours, and other relevant data. The provided results are specific to the
        selected location (see [the List of
        Locations](https://docs.dataforseo.com/v3/business_data/business_listings/locations.md))
        settings.
      operationId: post_dataforseo_business_data_business_listings_search_live
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
                    *business categories* optional field the categories you
                    specify are used to search for business listings; if you
                    don’t use this field, we will return business listings found
                    in the specified location; you can specify **up to 10
                    categories**
                description:
                  type: string
                  description: >-
                    *description of the element in SERP* optional field the
                    description of the business entity for which the results are
                    collected; can contain up to 200 characters
                title:
                  type: string
                  description: >-
                    *title of the element in SERP* optional field the name of
                    the business entity for which the results are collected; can
                    contain up to 200 characters
                is_claimed:
                  type: boolean
                  description: >-
                    *indicates whether the business is verified by its owner on
                    Google Maps* optional field
                location_coordinate:
                  type: string
                  description: >-
                    *GPS coordinates of a location* optional field
                    `location_coordinate` parameter should be specified in the
                    *“latitude,longitude,radius”* format the maximum number of
                    decimal digits for *“latitude”* and *“longitude”*: 7 the
                    value of *“radius”* is specified in kilometres (km) the
                    minimum value for *“radius”*: `1` the maximum value for
                    *“radius”*: `100000` example: `53.476225,-2.243572,200`
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    *array of results filtering parameters* optional field **you
                    can add several filters at once (8 filters maximum)** you
                    should set a logical operator `and`, `or` between the
                    conditions the following operators are supported: `regex`,
                    `not_regex`, ``, `>=`, `=`, ``, `in`, `not_in`, `like`,
                    `not_like`, `ilike`, `not_ilike`, `match`, `not_match` you
                    can use the `%` operator with `like` and `not_like` to match
                    any string of zero or more characters example:
                    `["rating.value",">",3]` you can receive the list of
                    available filters by making a separate request to
                    `https://api.dataforseo.com/v3/business_data/business_listings/available_filters`
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    *results sorting rules* optional field you can use the same
                    values as in the `filters` array to sort the results
                    possible sorting types: `asc` – results will be sorted in
                    the ascending order `desc` – results will be sorted in the
                    descending order you should use a comma to set up a sorting
                    parameter example: `["rating.value,desc"]`**note that you
                    can set no more than three sorting rules in a single
                    request** you should use a comma to separate several sorting
                    rules example:
                    `["rating.value,desc","rating.votes_count,desc"]`
                limit:
                  type: integer
                  description: >-
                    *the maximum number of returned businesses* optional field
                    default value: `100` maximum value: `1000`
                offset:
                  type: integer
                  description: >-
                    *offset in the results array of returned businesses*
                    optional field default value: `0` if you specify the `10`
                    value, the first ten entities in the results array will be
                    omitted and the data will be provided for the successive
                    entities
                offset_token:
                  type: string
                  description: >-
                    *token for subsequent requests* optional field provided in
                    the identical filed of the response to each request; use
                    this parameter to avoid timeouts while trying to obtain over
                    100,000 results in a single request; by specifying the
                    unique `offset_token` value from the response array, you
                    will get the subsequent results of the initial task;
                    `offset_token` values are unique for each subsequent task
                    **Note:** if the `offset_token` is specified in the request,
                    all other parameters should be identical to the previous
                    request
                tag:
                  type: string
                  description: >-
                    *user-defined task identifier* optional field *the character
                    limit is 255* you can use this parameter to identify the
                    task and match it with the result you will find the
                    specified `tag` value in the `data` object of the response
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
                    description: '*the current version of the API*'
                  version.status_code:
                    type: integer
                    description: >-
                      *general status code* you can find the full list of the
                      response codes
                      [here](https://docs.dataforseo.com/v3/appendix/errors.md)
                      **Note:** we strongly recommend designing a necessary
                      system for handling related exceptional or error
                      conditions
                  version.status_message:
                    type: string
                    description: >-
                      *general informational message* you can find the full list
                      of general informational messages
                      [here](https://docs.dataforseo.com/v3/appendix/errors.md)
                  version.time:
                    type: string
                    description: '*execution time, seconds*'
                  version.cost:
                    type: number
                    description: '*total tasks cost, USD*'
                  version.tasks_count:
                    type: integer
                    description: '*the number of tasks in the **`tasks`**array*'
                  version.tasks_error:
                    type: integer
                    description: >-
                      *the number of tasks in the **`tasks`** array returned
                      with an error*
                  tasks:
                    type: array
                    items:
                      type: string
                    description: '*array of tasks*'
                  tasks.id:
                    type: string
                    description: >-
                      *unique task identifier in our system* in the [Universally
                      unique identifier
                      (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier)
                      format
                  tasks.status_code:
                    type: integer
                    description: >-
                      *status code of the task* generated by DataForSEO; can be
                      within the following range: 10000-60000
                  tasks.status_message:
                    type: string
                    description: '*informational message of the task*'
                  tasks.time:
                    type: string
                    description: '*execution time, seconds*'
                  tasks.cost:
                    type: number
                    description: '*cost of the task, USD*'
                  tasks.result_count:
                    type: integer
                    description: '*number of elements in the `result` array*'
                  tasks.path:
                    type: array
                    items:
                      type: string
                    description: '*URL path*'
                  tasks.data:
                    type: object
                    description: >-
                      *contains the same parameters that you specified in the
                      POST request*
                  result:
                    type: array
                    items:
                      type: string
                    description: '*array of results*'
                  result.total_count:
                    type: integer
                    description: >-
                      *total number of results in our database relevant to your
                      request*
                  result.count:
                    type: integer
                    description: '*item types* the number of items in the `items` array'
                  result.offset:
                    type: integer
                    description: '*offset in the results array of returned businesses*'
                  result.offset_token:
                    type: string
                    description: >-
                      *token for subsequent requests* by specifying the unique
                      `offset_token` when setting a new task, you will get the
                      subsequent results of the initial task; `offset_token`
                      values are unique for each subsequent task
                  items:
                    type: array
                    items:
                      type: string
                    description: >-
                      *encountered item types* types of search engine results
                      encountered in the `items` array; possible item types:
                      `business_listing`
                  items.type:
                    type: string
                    description: '*type of element = **‘business\_listing’***'
                  items.title:
                    type: string
                    description: >-
                      *title of the element in SERP* the name of the business
                      entity for which the results are collected
                  items.original_title:
                    type: string
                    description: >-
                      *original title of the element* original title not
                      translated by Google
                  items.description:
                    type: string
                    description: >-
                      *description of the element in SERP* the description of
                      the business entity for which the results are collected
                  items.category:
                    type: string
                    description: >-
                      *business category* Google My Business general category
                      that best describes the services provided by the business
                      entity
                  items.category_ids:
                    type: array
                    items:
                      type: string
                    description: >-
                      *global category IDs* universal category IDs that do not
                      change based on the selected country
                  items.additional_categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      *additional business categories* additional Google My
                      Business categories that describe the services provided by
                      the business entity in more detail
                  items.cid:
                    type: string
                    description: >-
                      *google-defined client id* unique id of a local
                      establishment learn more about the identifier in [this
                      help center
                      article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)
                  items.feature_id:
                    type: string
                    description: >-
                      *the unique identifier of the element in SERP* learn more
                      about the identifier in [this help center
                      article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)
                  items.address:
                    type: string
                    description: '*street address of the business entity*'
                  items.address_info:
                    type: object
                    description: >-
                      *object containing address components of the business
                      entity*
                  items.borough:
                    type: string
                    description: >-
                      *administrative unit or district the business entity
                      location belongs to*
                  items.city:
                    type: string
                    description: '*name of the city where the business entity is located*'
                  items.zip:
                    type: string
                    description: '*ZIP code of the business entity*'
                  items.region:
                    type: string
                    description: '*DMA region of the business entity location*'
                  items.country_code:
                    type: string
                    description: '*ISO country code of the business entity location*'
                  items.place_id:
                    type: string
                    description: >-
                      *unique place identifier* [place
                      id](https://developers.google.com/places/place-id) of the
                      local establishment featured in the element learn more
                      about the identifier in [this help center
                      article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)
                  items.phone:
                    type: string
                    description: '*phone number of the business entity*'
                  items.url:
                    type: string
                    description: '*absolute url of the business entity*'
                  items.domain:
                    type: string
                    description: '*domain of the business entity*'
                  items.logo:
                    type: string
                    description: '*URL of the logo featured in Google My Business profile*'
                  items.main_image:
                    type: string
                    description: >-
                      *URL of the main image featured in Google My Business
                      profile*
                  items.total_photos:
                    type: integer
                    description: >-
                      *total count of images featured in Google My Business
                      profile*
                  items.snippet:
                    type: string
                    description: '*additional information on the business entity*'
                  items.latitude:
                    type: number
                    description: >-
                      *latitude coordinate of the local establishments in google
                      maps* example: `"latitude": 51.584091`
                  items.longitude:
                    type: number
                    description: >-
                      *longitude coordinate of the local establishment in google
                      maps* example: `"longitude": -0.31365919999999997`
                  items.is_claimed:
                    type: boolean
                    description: >-
                      *shows whether the entity is verified by its owner on
                      Google Maps*
                  items.attributes:
                    type: object
                    description: >-
                      *service details in a form of user-reviewed checks;*
                      service details of a business entity displayed in a form
                      of checks and based on user feedback and business
                      `category`
                  items.available_attributes:
                    type: object
                    description: >-
                      *available attributes* indicates attributes a business
                      entity can offer
                  items.unavailable_attributes:
                    type: object
                    description: >-
                      *unavailable attributes* indicates attributes a business
                      entity cannot offer
                  items.place_topics:
                    type: object
                    description: >-
                      *keywords mentioned in customer reviews* contains most
                      popular keywords related to products/services mentioned in
                      customer reviews of a business entity and the number of
                      reviews mentioning each keyword example: `"place_topics":
                      {"egg roll": 48,"birthday": 33}`
                  items.rating:
                    type: object
                    description: >-
                      *the element’s rating* the popularity rate based on
                      reviews and displayed in SERP
                  items.rating_type:
                    type: string
                    description: >-
                      *the type of rating* here you can find the following
                      elements: `Max5`, `Percents`, `CustomMax`
                  items.value:
                    type: integer
                    description: '*the value of the rating*'
                  items.votes_count:
                    type: integer
                    description: '*the amount of feedback*'
                  items.rating_max:
                    type: integer
                    description: '*the maximum value for a `rating_type`*'
                  items.hotel_rating:
                    type: integer
                    description: >-
                      *hotel class rating* class ratings range between 1-5
                      stars, [learn
                      more](https://support.google.com/business/answer/7660515?hl=en)
                      if there is no hotel class rating information, the value
                      will be `null`
                  items.price_level:
                    type: string
                    description: >-
                      *property price level* can take values: `inexpensive`,
                      `moderate`, `expensive`, `very_expensive` if there is no
                      price level information, the value will be `null`
                  items.rating_distribution:
                    type: object
                    description: >-
                      *the distribution of ratings of the business entity* the
                      object displays the number of 1-star to 5-star ratings, as
                      reviewed by users
                  items.1:
                    type: integer
                    description: '*the number of 1-star ratings*'
                  items.2:
                    type: integer
                    description: '*the number of 2-star ratings*'
                  items.3:
                    type: integer
                    description: '*the number of 3-star ratings*'
                  items.4:
                    type: integer
                    description: '*the number of 4-star ratings*'
                  items.5:
                    type: integer
                    description: '*the number of 5-star ratings*'
                  items.people_also_search:
                    type: array
                    items:
                      type: string
                    description: '*related business entities*'
                  items.work_time:
                    type: object
                    description: >-
                      *work time details* information related to operational
                      hours of the business entity
                  items.work_hours:
                    type: object
                    description: >-
                      *open hours* information about work hours of the local
                      establishment
                  items.timetable:
                    type: object
                    description: '*work hours timetable*'
                  items.sunday:
                    type: array
                    items:
                      type: string
                    description: >-
                      *work hours on Sunday* **can take values of the
                      corresponding days of the week**
                  items.open:
                    type: object
                    description: '*opening time*'
                  items.hour:
                    type: integer
                    description: '*hours in the 24-hour format*'
                  items.minute:
                    type: integer
                    description: '*minutes*'
                  items.close:
                    type: object
                    description: '*closing time*'
                  items.current_status:
                    type: string
                    description: >-
                      *current status of the establishment* possible values:
                      `open`, `close`, `temporarily_closed`, `closed_forever`
                  popular_times:
                    type: object
                    description: >-
                      *popular times* information related to busy hours of the
                      business entity
                  popular_times.popular_times_by_days:
                    type: object
                    description: >-
                      *popular hours* information about busy hours of the local
                      establishment on each day of the week
                  popular_times.sunday:
                    type: array
                    items:
                      type: string
                    description: >-
                      *busy hours on Sunday* **can take values of the
                      corresponding days of the week**
                  popular_times.time:
                    type: object
                    description: '*busy hours*'
                  popular_times.hour:
                    type: integer
                    description: '*hours in a 24-hour format*'
                  popular_times.minute:
                    type: integer
                    description: '*minutes*'
                  popular_times.popular_index:
                    type: integer
                    description: >-
                      *popularity index* relative time-bound popularity index
                      measured from `0` to `100`; higher value corresponds to a
                      busier time of a day
                  local_business_links:
                    type: array
                    items:
                      type: string
                    description: >-
                      *available interactions with the business* list of options
                      to interact with the business directly from search results
                  local_business_links.type:
                    type: string
                    description: >-
                      *type of element* possible values:
                      `"reservation""order""delivery_services_element""menu"`
                  local_business_links.title:
                    type: string
                    description: '*title of the element* domain of the reservation software'
                  local_business_links.url:
                    type: string
                    description: '*URL to the services*'
                  contact_info:
                    type: array
                    items:
                      type: string
                    description: >-
                      *available contacts of the business* list of contacts to
                      interact with the business
                  contact_info.type:
                    type: string
                    description: '*type of contact element*'
                  contact_info.value:
                    type: string
                    description: '*contact displayed in SERP* example: `"+119797979736"`'
                  contact_info.source:
                    type: string
                    description: '*data source*'
                  contact_info.check_url:
                    type: string
                    description: >-
                      *direct URL to search engine results* you can use it to
                      make sure that we provided accurate results
                  contact_info.last_updated_time:
                    type: string
                    description: >-
                      *date and time when the data was last updated* in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: `2023-01-26
                      09:03:15 +00:00`
                  contact_info.first_seen:
                    type: string
                    description: >-
                      *date and time when our crawler found the business listing
                      element for the first time* in the UTC format: “yyyy-mm-dd
                      hh-mm-ss +00:00” example: `2023-03-11 10:04:11 +00:00`
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