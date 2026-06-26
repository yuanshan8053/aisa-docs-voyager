> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Live Google My Business Info Tasks

> Business Data API provides results containing information about specific business entity from Google.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/business_data/google/my_business_info/live
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
  /dataforseo/business_data/google/my_business_info/live:
    post:
      summary: Setting Live Google My Business Info Tasks
      description: >-
        Business Data API provides results containing information about specific
        business entity from Google. The provided results are specific to the
        selected location (see [the List of
        Locations](https://docs.dataforseo.com/v3/business_data/google/locations.md))
        and language (see [the List of
        Languages](https://docs.dataforseo.com/v3/business_data/google/languages.md))
        settings.
      operationId: post_dataforseo_business_data_google_my_business_info_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                keyword:
                  type: string
                  description: >-
                    *keyword* **required field** the keyword you specify should
                    indicate the name of the local establishment you can specify
                    **up to 700 characters** in the `keyword` filed **all %##
                    will be decoded (plus character ‘+’ will be decoded to a
                    space character)** if you need to use the “%” character for
                    your `keyword`, please specify it as “%25”; this field can
                    also be used to pass the following parameters: `cid` – a
                    unique, google-defined id of the business entity; `place_id`
                    – an identifier of the business entity in Google Maps; `spp`
                    – a unique identifier of local services featured in the
                    `local_pack` element of Google SERP example:
                    `cid:194604053573767737`
                    `place_id:GhIJQWDl0CIeQUARxks3icF8U8A`
                    `spp:CgsvZy8xdGN4cWRraBoUChIJPZDrEzLsZIgRoNrpodC5P30` learn
                    more about the `cid` and `place_id` identifiers in [this
                    help center
                    article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)
                    learn more about rules and limitations of `keyword` and
                    `keywords` fields in DataForSEO APIs in this [Help Center
                    article](https://dataforseo.com/help-center/rules-and-limitations-of-keyword-and-keywords-fields-in-dataforseo-apis)
                location_name:
                  type: string
                  description: >-
                    *full name of search engine location* **required field if
                    you don’t specify** `location_code` or `location_coordinate`
                    **if you use this field, you don’t need to specify
                    `location_code` or `location_coordinate`** you can receive
                    the list of available locations with `location_name` by
                    making a separate request to
                    `https://api.dataforseo.com/v3/business_data/google/locations`
                    example: `London,England,United Kingdom`
                location_code:
                  type: integer
                  description: >-
                    *search engine location code* **required field if you don’t
                    specify** `location_name` or `location_coordinate` **if you
                    use this field, you don’t need to specify `location_name` or
                    `location_coordinate`** you can receive the list of
                    available locations with `location_code` by making a
                    separate request to the
                    `https://api.dataforseo.com/v3/business_data/google/locations`
                    example: `2840`
                location_coordinate:
                  type: string
                  description: >-
                    *GPS coordinates of a location* **required field if you
                    don’t specify** `location_name` or `location_code` **if you
                    use this field, you don’t need to specify `location_name` or
                    `location_code`** `location_coordinate` parameter should be
                    specified in the *“latitude,longitude,radius”* format the
                    maximum number of decimal digits for *“latitude”* and
                    *“longitude”*: 7 the minimum value for *“radius”*: 199.9
                    (mm) the maximum value for *“radius”*: 199999 (mm) example:
                    `53.476225,-2.243572,200`
                language_name:
                  type: string
                  description: >-
                    *full name of search engine language* **required field if
                    you don’t specify** `language_code` **if you use this field,
                    you don’t need to specify `language_code`** you can receive
                    the list of available languages with `language_name` by
                    making a separate request to
                    `https://api.dataforseo.com/v3/business_data/google/languages`
                    example: `English`
                language_code:
                  type: string
                  description: >-
                    *search engine language code* **required field if you don’t
                    specify** `language_name` **if you use this field, you don’t
                    need to specify `language_name`** you can receive the list
                    of available languages with their `language_code` by making
                    a separate request to
                    `https://api.dataforseo.com/v3/business_data/google/languages`
                    example: `en`
                tag:
                  type: string
                  description: >-
                    *user-defined task identifier* optional field *the character
                    limit is 255* you can use this parameter to identify the
                    task and match it with the result you will find the
                    specified `tag` value in the `data` object of the response
              required:
                - keyword
                - location_name
                - location_code
                - location_coordinate
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
                    description: '*total *tasks* cost, USD*'
                  version.tasks_count:
                    type: integer
                    description: '*the number of tasks in the **`tasks`** array*'
                  version.tasks_error:
                    type: integer
                    description: >-
                      *the number of tasks in the **`tasks`** array that were
                      returned an error*
                  tasks:
                    type: array
                    items:
                      type: string
                    description: '*array of tasks*'
                  tasks.id:
                    type: string
                    description: >-
                      *task identifier* **unique task identifier in our system
                      in the
                      [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)
                      format**
                  tasks.status_code:
                    type: integer
                    description: >-
                      *status code of the task* generated by DataForSEO; can be
                      within the following range: 10000-60000 you can find the
                      full list of the response codes
                      [here](https://docs.dataforseo.com/v3/appendix/errors.md)
                  tasks.status_message:
                    type: string
                    description: >-
                      *informational message of the task* you can find the full
                      list of general informational messages
                      [here](https://docs.dataforseo.com/v3/appendix/errors.md)
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
                  result.keyword:
                    type: string
                    description: >-
                      *keyword received in a POST array* **keyword is returned
                      with decoded %## (plus character ‘+’ will be decoded to a
                      space character)** this field will contain the `cid`
                      parameter if you specified it in the `keyword` field when
                      setting a task; example: `cid:2946633002421908862` learn
                      more about the parameter in [this help center
                      article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)
                  result.se_domain:
                    type: string
                    description: '*search engine domain as specified in a POST array*'
                  result.location_code:
                    type: integer
                    description: '*location code in a POST array*'
                  result.language_code:
                    type: string
                    description: '*language code in a POST array*'
                  result.check_url:
                    type: string
                    description: >-
                      *direct URL to search engine results* you can use it to
                      make sure that we provided accurate results
                  result.datetime:
                    type: string
                    description: >-
                      *date and time when the result was received* in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: `2019-11-15
                      12:57:46 +00:00`
                  result.item_types:
                    type: array
                    items:
                      type: string
                    description: >-
                      *item types* types of search engine results encountered in
                      the `items` array; possible item types:
                      `google_business_info`
                  result.items_count:
                    type: integer
                    description: '*item types* the number of items in the `items` array'
                  items:
                    type: array
                    items:
                      type: string
                    description: >-
                      *encountered item types* types of search engine results
                      encountered in the `items` array; possible item types:
                      `google_business_info`
                  items.type:
                    type: string
                    description: '*type of element = **‘google\_business\_info’***'
                  items.rank_group:
                    type: integer
                    description: >-
                      *position within a group of elements with identical `type`
                      values* positions of elements with different `type` values
                      are omitted from `rank_group`
                  items.rank_absolute:
                    type: integer
                    description: '*absolute rank among all the elements*'
                  items.position:
                    type: string
                    description: '*the alignment in SERP*'
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
                  items.contact_url:
                    type: string
                    description: '*URL of the preferred contact page*'
                  items.contributor_url:
                    type: string
                    description: >-
                      *URL of the user’s or entity’s Local Guides profile, if
                      available*
                  items.book_online_url:
                    type: string
                    description: >-
                      *URL in the ‘book online’ button of the element* URL
                      directing users to the online booking or order page of the
                      business entity
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
                    description: '*work hours on Sundays*'
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
                  items.monday:
                    type: array
                    items:
                      type: string
                    description: '*work hours on Mondays*'
                  items.tuesday:
                    type: array
                    items:
                      type: string
                    description: '*work hours on Tuesdays*'
                  items.wednesday:
                    type: array
                    items:
                      type: string
                    description: '*work hours on Wednesdays*'
                  items.thursday:
                    type: array
                    items:
                      type: string
                    description: '*work hours on Thursdays*'
                  items.friday:
                    type: array
                    items:
                      type: string
                    description: '*work hours on Fridays*'
                  items.saturday:
                    type: array
                    items:
                      type: string
                    description: '*work hours on Saturday*'
                  items.current_status:
                    type: string
                    description: >-
                      *current status of the establishment* possible values:
                      `opened`, `closed`, `temporarily_closed`, `closed_forever`
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
                      *busy hours on sunday* **can take values of the
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
                    description: '*type of element = **‘menu’***'
                  local_business_links.title:
                    type: string
                    description: '*title of the element* domain of the online menu system'
                  local_business_links.url:
                    type: string
                    description: '*URL to view the menu*'
                  local_business_links.delivery_services:
                    type: array
                    items:
                      type: string
                    description: '*lists available delivery services*'
                  local_business_links.is_directory_item:
                    type: boolean
                    description: >-
                      *business establishment is a part of the directory*
                      indicates whether the business establishment is a part of
                      the directory; if `true`, the item is a part of the larger
                      directory of businesses with the same address (e.g., a
                      mall or a business centre); **note:** if the business
                      establishment is a parent item in the directory, the value
                      will be `null`
                  directory:
                    type: array
                    items:
                      type: string
                    description: >-
                      *items of the directory* includes information about
                      businesses that are located within the target business
                      establishment and have the same address
                  directory.title:
                    type: string
                    description: >-
                      *title of the element in SERP* the name of the business
                      entity
                  directory.items:
                    type: array
                    items:
                      type: string
                    description: '***array of directory items***'
                  directory.type:
                    type: string
                    description: '*type of element = **‘maps\_search’***'
                  directory.rank_group:
                    type: integer
                    description: >-
                      *position within a group of elements with identical `type`
                      values* positions of elements with different `type` values
                      are omitted from the `rank_group`
                  directory.rank_absolute:
                    type: integer
                    description: '*absolute rank among all the elements*'
                  directory.domain:
                    type: string
                    description: '*domain of the business entity*'
                  directory.url:
                    type: string
                    description: '*absolute url of the business entity*'
                  directory.rating:
                    type: object
                    description: >-
                      *the element’s rating* the popularity rate based on
                      reviews and displayed in SERP
                  directory.rating_type:
                    type: string
                    description: >-
                      *the type of rating* here you can find the following
                      elements: `Max5`, `Percents`, `CustomMax`
                  directory.value:
                    type: integer
                    description: '*the value of the rating*'
                  directory.votes_count:
                    type: integer
                    description: '*the amount of feedback*'
                  directory.rating_max:
                    type: integer
                    description: '*the maximum value for a `rating_type`*'
                  directory.rating_distribution:
                    type: object
                    description: >-
                      *the distribution of ratings of the business entity* the
                      object displays the number of 1-star to 5-star ratings, as
                      reviewed by users
                  directory.1:
                    type: integer
                    description: '*the number of 1-star ratings*'
                  directory.2:
                    type: integer
                    description: '*the number of 2-star ratings*'
                  directory.3:
                    type: integer
                    description: '*the number of 3-star ratings*'
                  directory.4:
                    type: integer
                    description: '*the number of 4-star ratings*'
                  directory.5:
                    type: integer
                    description: '*the number of 5-star ratings*'
                  directory.snippet:
                    type: string
                    description: '*additional information about the business entity*'
                  directory.address:
                    type: string
                    description: '*street address of the business entity*'
                  directory.address_info:
                    type: object
                    description: >-
                      *object containing address components of the business
                      entity*
                  directory.borough:
                    type: string
                    description: >-
                      *administrative unit or district the business entity
                      location belongs to*
                  directory.city:
                    type: string
                    description: '*name of the city where the business entity is located*'
                  directory.zip:
                    type: string
                    description: '*ZIP code of the business entity*'
                  directory.region:
                    type: string
                    description: '*DMA region of the business entity location*'
                  directory.country_code:
                    type: string
                    description: '*ISO country code of the business entity location*'
                  directory.place_id:
                    type: string
                    description: >-
                      *unique place identifier* [place
                      id](https://developers.google.com/places/place-id) of the
                      local establishment featured in the element learn more
                      about the identifier in [this help center
                      article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)
                  directory.phone:
                    type: string
                    description: '*phone number of the business entity*'
                  directory.main_image:
                    type: string
                    description: >-
                      *URL of the main image featured in Google My Business
                      profile*
                  directory.total_photos:
                    type: integer
                    description: >-
                      *total count of images featured in Google My Business
                      profile*
                  directory.category:
                    type: string
                    description: >-
                      *business category* Google My Business general category
                      that best describes the services provided by the business
                      entity
                  directory.category_ids:
                    type: array
                    items:
                      type: string
                    description: >-
                      *global category IDs* universal category IDs that do not
                      change based on the selected country
                  directory.work_hours:
                    type: object
                    description: >-
                      *work hours* information about work hours of the local
                      establishment
                  directory.feature_id:
                    type: string
                    description: >-
                      *the unique identifier of the element in SERP* learn more
                      about the identifier in [this help center
                      article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)
                  directory.cid:
                    type: string
                    description: >-
                      *google-defined client id* unique id of a local
                      establishment; can be used with [Google Reviews
                      API](https://docs.dataforseo.com/v3/reviews/google/overview.md)
                      to get a full list of reviews learn more about the
                      identifier in [this help center
                      article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)
                  directory.latitude:
                    type: number
                    description: >-
                      *latitude coordinate of the local establishments in google
                      maps* example: `"latitude": 51.584091`
                  directory.longitude:
                    type: number
                    description: >-
                      *longitude coordinate of the local establishment in google
                      maps* example: `"longitude": -0.31365919999999997`
                  directory.is_claimed:
                    type: boolean
                    description: >-
                      *shows whether the entity is verified by its owner on
                      Google Maps*
                  directory.local_justifications:
                    type: array
                    items:
                      type: string
                    description: >-
                      *Google local justifications* snippets of text that
                      “justify” why the business is showing up for search query
                  directory.is_directory_item:
                    type: boolean
                    description: >-
                      *business establishment is a part of the directory*
                      indicates whether the business establishment is a part of
                      the directory; if `true`, the item is a part of the larger
                      directory of businesses with the same address (e.g., a
                      mall or a business centre); **note:** if the business
                      establishment is a parent item in the directory, the value
                      will be `null`
                  directory.price_level:
                    type: string
                    description: >-
                      *property price level* can take values: `inexpensive`,
                      `moderate`, `expensive`, `very_expensive` if there is no
                      price level information, the value will be `null`
                  directory.hotel_rating:
                    type: integer
                    description: >-
                      *hotel class rating* class ratings range between 1-5
                      stars, [learn
                      more](https://support.google.com/business/answer/7660515?hl=en)
                      if there is no hotel class rating information, the value
                      will be `null`
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