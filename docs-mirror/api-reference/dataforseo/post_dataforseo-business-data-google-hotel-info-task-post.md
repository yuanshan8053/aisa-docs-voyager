> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Google Hotel Info Tasks

> Google Hotel Info will provide you with structured data available for a specific hotel entity on the [Google Hotels](http://www.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/business_data/google/hotel_info/task_post
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
  /dataforseo/business_data/google/hotel_info/task_post:
    post:
      summary: Setting Google Hotel Info Tasks
      description: >-
        Google Hotel Info will provide you with structured data available for a
        specific hotel entity on the [Google
        Hotels](http://www.google.com/travel/hotels) platform: such as service
        description, location details, rating, amenities, reviews, images,
        prices, and more.
      operationId: post_dataforseo_business_data_google_hotel_info_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                hotel_identifier:
                  type: string
                  description: >-
                    *unique hotel identifier* **required field if you don’t
                    specify `keyword`** **if you use this field, you don’t need
                    to specify `keyword`** unique identifier of a hotel entity
                    in Google search; you can obtain the value by making a
                    request to Advanced [Google SERP
                    API](https://docs.dataforseo.com/v3/serp/google/organic/overview.md)
                    (enclosed in the `hotels_pack` element of the response), or
                    the [Hotel Searches
                    endpoint](https://docs.dataforseo.com/v3/business_data/google/hotel_searches/task_post.md)
                    of Business Data API example:
                    `ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE`
                keyword:
                  type: string
                  description: >-
                    *keyword* **required field if you don’t specify
                    `hotel_identifier`** **if you use this field, you don’t need
                    to specify `hotel_identifier`** the keyword you specify
                    should indicate the name of the hotel entity you can specify
                    **up to 700 characters** in the `keyword` filed **all %##
                    will be decoded (plus character ‘+’ will be decoded to a
                    space character)** if you need to use the “%” character for
                    your `keyword`, please specify it as “%25”
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
                    example: `London,England,United Kingdom`
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
                check_in:
                  type: string
                  description: >-
                    *check-in date* optional field if you don’t specify this
                    field, tomorrow’s date will be used by default; the value
                    must not be earlier than today’s date date format:
                    `"yyyy-mm-dd"` example: `"2019-01-15"`
                check_out:
                  type: string
                  description: >-
                    *check-out date* optional field if you don’t specify this
                    field, our system will apply the date of two days from now
                    by default; **Note:** the value cannot be less than or equal
                    to `check_in`; the range between `check_in` and `check_out`
                    values cannot exceed 30 days date format: `"yyyy-mm-dd"`
                    example: `"2019-01-15"`
                currency:
                  type: string
                  description: '*currency* optional field example: `"USD"`'
                adults:
                  type: integer
                  description: >-
                    *number of adults* optional field if you don’t specify this
                    field, two adults will be used by default example: `1`
                children:
                  type: array
                  items:
                    type: string
                  description: >-
                    *number and age of children* optional field if you don’t
                    specify this field, no children will be included in the
                    search; set the following value if you want to include one
                    14-years-old child: `[14]` set the following value if you
                    want to include one 13-years-old child and one 8-years-old
                    child: `[13,8]`
                load_prices_by_dates:
                  type: boolean
                  description: >-
                    *load hotel stay prices by dates* optional field if you
                    specify this parameter with `true`, the response will
                    include the `prices_by_dates` array with hotel stay prices
                    divided by dates if you use this parameter, you will be
                    charged **double the base price for a request**
                prices_start_date:
                  type: string
                  description: >-
                    *start date to load prices by dates* optional field to use
                    this parameter, you must specify `load_prices_by_dates` with
                    `true` if this parameter is not specified, the start date is
                    set to `check_in` date date format: `yyyy-mm-dd` example:
                    `2025-05-20`
                prices_end_date:
                  type: string
                  description: >-
                    *end date to load prices by dates* optional field to use
                    this parameter, you must specify `load_prices_by_dates` with
                    `true` if this parameter is not specified, you will get
                    prices by date for the month date format: `yyyy-mm-dd`
                    example: `2025-05-21`
                prices_date_range:
                  type: string
                  description: >-
                    *predefined period for retrieving daily price data* optional
                    field to use this parameter, you must specify
                    `load_prices_by_dates` with `true` if the `prices_start_date
                    `is not specified, the start date is set to `check_in` date
                    possible values: `month`, `three_months`, `six_months`,
                    `year` default value: `month`
                tag:
                  type: string
                  description: >-
                    *user-defined task identifier* optional field *the character
                    limit is 255;* you can use this parameter to identify the
                    task and match it with the result; you will find the
                    specified `tag` value in the `data` object of the response
                postback_url:
                  type: string
                  description: >-
                    *return URL for sending task results* optional field once
                    the task is completed, we will send a POST request with its
                    results compressed in the `gzip` format to the
                    `postback_url` you specified; you can use the ‘$id’ string
                    as a `$id` variable and ‘$tag’ as urlencoded `$tag`
                    variable. We will set the necessary values before sending
                    the request; example:
                    `http://your-server.com/postbackscript?id=$id`
                    `http://your-server.com/postbackscript?id=$id&tag=$tag`
                    **Note:** special characters in `postback_url` will be
                    urlencoded; i.a., the `#` character will be encoded into
                    `%23`learn more on our [Help
                    Center](https://dataforseo.com/help-center/pingbacks-postbacks-with-dataforseo-api)
                postback_data:
                  type: string
                  description: >-
                    *postback\_url datatype* **required field if you specify
                    `postback_url`** corresponds to the datatype that will be
                    sent to your server possible values: `advanced`, `html`
                pingback_url:
                  type: string
                  description: >-
                    *notification URL of a completed task* optional field when a
                    task is completed we will notify you by GET request sent to
                    the URL you have specified; you can use the ‘$id’ string as
                    a `$id` variable and ‘$tag’ as urlencoded `$tag` variable;
                    we will set the necessary values before sending the request;
                    example: `http://your-server.com/pingscript?id=$id`
                    `http://your-server.com/pingscript?id=$id&tag=$tag`
                    **Note:** special characters in `pingback_url` will be
                    urlencoded; i.a., the `#` character will be encoded into
                    `%23`learn more on our [Help
                    Center](https://dataforseo.com/help-center/pingbacks-postbacks-with-dataforseo-api)
              required:
                - hotel_identifier
                - keyword
                - location_name
                - location_code
                - location_coordinate
                - language_name
                - language_code
                - postback_data
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