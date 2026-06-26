> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Google Hotel Searches Tasks

> Hotel Searches API provides results containing information about different hotels listed on Google.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/business_data/google/hotel_searches/task_post
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
  /dataforseo/business_data/google/hotel_searches/task_post:
    post:
      summary: Setting Google Hotel Searches Tasks
      description: >-
        Hotel Searches API provides results containing information about
        different hotels listed on Google. The provided results are specific to
        the keyword, selected location (see [the List of
        Locations](https://docs.dataforseo.com/v3/business_data/google/locations.md))
        and language (see [the List of
        Languages](https://docs.dataforseo.com/v3/business_data/google/languages.md))
        settings.
      operationId: post_dataforseo_business_data_google_hotel_searches_task_post
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
                    *keyword* optional field the keyword you specify is used to
                    search for the list of hotels; if you don’t use this field,
                    we will return the list of hotels found in a specified
                    location; you can specify **up to 700 characters** in the
                    `keyword` filed **all %## will be decoded (plus character
                    ‘+’ will be decoded to a space character)** if you need to
                    use the “%” character for your `keyword`, please specify it
                    as “%25”; **Note:** in order to obtain accurate search
                    results, the location name is appended to the keyword
                    automatically learn more about rules and limitations of
                    `keyword` and `keywords` fields in DataForSEO APIs in this
                    [Help Center
                    article](https://dataforseo.com/help-center/rules-and-limitations-of-keyword-and-keywords-fields-in-dataforseo-apis)
                priority:
                  type: integer
                  description: >-
                    *task priority* optional field can take the following
                    values: 1 – normal execution priority (set by default) 2 –
                    high execution priority You will be additionally charged for
                    the tasks with high execution priority. The cost can be
                    calculated on the
                    [Pricing](https://dataforseo.com/pricing/business-data/google-hotels-api
                    "Pricing") page.
                location_name:
                  type: string
                  description: >-
                    *full name of search engine location* **required field if
                    you don’t specify `location_code` or `location_coordinate`**
                    **if you use this field, you don’t need to specify
                    `location_code` or `location_coordinate`** you can receive
                    the list of available locations with `location_name` by
                    making a separate request to
                    `https://api.dataforseo.com/v3/business_data/google/locations`
                    example: `London,England,United Kingdom` **Note:** in order
                    to obtain accurate search results, the `location_name` you
                    specify will be automatically appended to the keyword
                location_code:
                  type: integer
                  description: >-
                    *search engine location code* **required field if you don’t
                    specify `location_name` or `location_coordinate`** **if you
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
                    don’t specify `location_name` or `location_code`** **if you
                    use this field, you don’t need to specify `location_name` or
                    `location_code`** `location_coordinate` parameter should be
                    specified in the *“latitude,longitude”* format the maximum
                    number of decimal digits for *“latitude”* and *“longitude”*:
                    7 **Note**: if the coordinates are used to set a location,
                    the search will occur in the nearest settlement; example:
                    `53.476225,-2.243572`
                language_name:
                  type: string
                  description: >-
                    *full name of search engine language* **required field if
                    you don’t specify `language_code`** **if you use this field,
                    you don’t need to specify `language_code`** you can receive
                    the list of available languages with `language_name` by
                    making a separate request to
                    `https://api.dataforseo.com/v3/business_data/google/languages`
                    example: `English`
                language_code:
                  type: string
                  description: >-
                    *search engine language code* **required field if you don’t
                    specify `language_name`** **if you use this field, you don’t
                    need to specify `language_name`** you can receive the list
                    of available languages with their `language_code` by making
                    a separate request to
                    `https://api.dataforseo.com/v3/business_data/google/languages`
                    example: `en`
                depth:
                  type: integer
                  description: >-
                    *parsing depth* optional field number of results in Google
                    Hotels default value: `20` organic results max value: `140`
                    **Note:** your account will be billed per each 20 organic
                    results regardless of paid listings in the response; thus,
                    setting a depth above `20` may result in additional charges
                    if Google Hotels return more than 20 results; if the
                    specified depth is higher than the number of results in the
                    response, the difference will be refunded automatically to
                    your account balance
                check_in:
                  type: string
                  description: >-
                    *check-in date* optional field if you don’t specify this
                    field, tomorrow’s date will be used by default; date format:
                    `"yyyy-mm-dd"` example: `"2019-01-15"` **Note:** the value
                    cannot precede the today’s date
                check_out:
                  type: string
                  description: >-
                    *check-out date* optional field if you don’t specify this
                    field, our system will apply the date of two days from now
                    by default; date format: `"yyyy-mm-dd"` example:
                    `"2019-01-15"` **Note:** the value cannot be less than or
                    equal to `check_in`; the range between `check_in` and
                    `check_out` values cannot exceed 30 days
                currency:
                  type: string
                  description: '*currency* optional field example: `"USD"`'
                adults:
                  type: integer
                  description: >-
                    *number of adults* optional field if you don’t specify this
                    field, the default value of `2` will be applied; **note**
                    that you can specify up to 6 persons including both adults
                    and children example: `1`
                children:
                  type: array
                  items:
                    type: string
                  description: >-
                    *number and age of children* optional field if you don’t
                    specify this field, no children will be included in the
                    search; age of child can be from `0` to `17`; **note** that
                    you can specify up to 6 persons including both adults and
                    children set the following value if you want to include one
                    14-year-old child: `[14]` set the following value if you
                    want to include one 13-year-old child and one 8-year-old
                    child: `[13,8]`
                stars:
                  type: array
                  items:
                    type: string
                  description: >-
                    *hotel stars* optional field set this field to `[5]` if you
                    want to get the list of 5-star hotels only example:
                    `[3,4,5]`
                min_rating:
                  type: number
                  description: >-
                    *minimum rating* optional field you can use this field to
                    specify guest rating higher than a certain value example:
                    `2.5`
                sort_by:
                  type: string
                  description: >-
                    *results sorting parameters* optional field you can use this
                    field to sort the results possible types of sorting:
                    `relevance` – sort by most relevant `lowest_price` – sort by
                    the lowest price `highest_rating` – sort by highest rating
                    `most_reviewed` – sort by most reviewed default value:
                    `relevance`
                min_price:
                  type: integer
                  description: >-
                    *minimum price per night* optional field the currency of
                    this value depends on the `currency` field example: `100`
                max_price:
                  type: integer
                  description: >-
                    *maximum price per night* optional field the currency of
                    this value depends on the `currency` field example: `600`
                free_cancellation:
                  type: boolean
                  description: >-
                    *hotels with a free cancellation* optional field set this
                    field to `true` if you want to get the list of hotels with
                    free cancellation of reservations default value: `false`
                is_vacation_rentals:
                  type: boolean
                  description: >-
                    *search for vacation rentals* optional field set this field
                    to `true` if you want to get the list of vacation rentals
                    instead of hotels default value: `false`
                amenities:
                  type: array
                  items:
                    type: string
                  description: >-
                    *hotel amenities* optional field you can use this field to
                    specify different hotel amenities example: ` [
                    "free_parking", "pets_allowed" ]` possible values:
                    `"air_conditioning","all_inclusive_available","bar","free_breakfast","fitness_center","kid_friendly","free_parking","pets_allowed","pool","restaurant","room_service","spa","free_wifi","parking","indoor_pool","outdoor_pool","wheelchair_accessible","beach_access"`
                tag:
                  type: string
                  description: >-
                    *user-defined task identifier* optional field *the character
                    limit is 255* you can use this parameter to identify the
                    task and match it with the result you will find the
                    specified `tag` value in the `data` object of the response
                postback_url:
                  type: string
                  description: >-
                    *return URL for sending task results* optional field once
                    the task is completed, we will send a POST request with its
                    results compressed in the `gzip` format to the
                    `postback_url` you specified you can use the ‘$id’ string as
                    a `$id` variable and ‘$tag’ as urlencoded `$tag` variable.
                    We will set the necessary values before sending the request.
                    example: `http://your-server.com/postbackscript?id=$id`
                    `http://your-server.com/postbackscript?id=$id&tag=$tag`
                    **Note:** special characters in `postback_url` will be
                    urlencoded; i.a., the `#` character will be encoded into
                    `%23`learn more on our [Help
                    Center](https://dataforseo.com/help-center/pingbacks-postbacks-with-dataforseo-api)
                pingback_url:
                  type: string
                  description: >-
                    *notification URL of a completed task* optional field when a
                    task is completed we will notify you by GET request sent to
                    the URL you have specified you can use the ‘$id’ string as a
                    `$id` variable and ‘$tag’ as urlencoded `$tag` variable. We
                    will set the necessary values before sending the request.
                    example: `http://your-server.com/pingscript?id=$id`
                    `http://your-server.com/pingscript?id=$id&tag=$tag`
                    **Note:** special characters in `pingback_url` will be
                    urlencoded; i.a., the `#` character will be encoded into
                    `%23`learn more on our [Help
                    Center](https://dataforseo.com/help-center/pingbacks-postbacks-with-dataforseo-api)
              required:
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
                    description: '*array of results* in this case, the value will be `null`'
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