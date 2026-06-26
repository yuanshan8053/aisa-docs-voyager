> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Google Hotel Info HTML

> Google Hotel Info will provide you with unstructured HTML data available for a specific hotel entity on the [Google Hotels](http://www.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/business_data/google/hotel_info/live/html
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
  /dataforseo/business_data/google/hotel_info/live/html:
    post:
      summary: Live Google Hotel Info HTML
      description: >-
        Google Hotel Info will provide you with unstructured HTML data available
        for a specific hotel entity on the [Google
        Hotels](http://www.google.com/travel/hotels) platform: such as service
        description, location details, rating, amenities, reviews, images,
        prices, and more.
      operationId: post_dataforseo_business_data_google_hotel_info_live_html
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
                    *unique hotel identifier* **required field** unique
                    identifier of a hotel entity in Google search; you can
                    obtain the value by making a request to Advanced [Google
                    SERP
                    API](https://docs.dataforseo.com/v3/serp/google/organic/overview.md)
                    (enclosed in the `hotels` element of the response), or the
                    [Hotel Searches
                    endpoint](https://docs.dataforseo.com/v3/business_data/google/hotel_searches/task_post.md)
                    of Business Data API example:
                    `ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE`
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
                    field, tomorrow’s date will be used by default; date format:
                    `"yyyy-mm-dd"` example: `"2019-01-15"`
                check_out:
                  type: string
                  description: >-
                    *check-out date* optional field if you don’t specify this
                    field, our system will apply the date of two days from now
                    by default; date format: `"yyyy-mm-dd"` example:
                    `"2019-01-15"`
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
                tag:
                  type: string
                  description: >-
                    *user-defined task identifier* optional field *the character
                    limit is 255* you can use this parameter to identify the
                    task and match it with the result you will find the
                    specified `tag` value in the `data` array of the response
              required:
                - hotel_identifier
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
                    type: array
                    items:
                      type: string
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
                    description: '*unique hotel identifier specified as `"hotel_id:$"`*'
                  result.type:
                    type: string
                    description: '*type of search results* in this case, `"hotel_info"`'
                  result.se_domain:
                    type: string
                    description: '*search engine domain in a POST array*'
                  result.location_code:
                    type: integer
                    description: '*location code in a POST array*'
                  result.language_code:
                    type: string
                    description: '*language code in a POST array*'
                  result.datetime:
                    type: string
                    description: >-
                      *date and time when the result was received* in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: `2019-11-15
                      12:57:46 +00:00`
                  result.items_count:
                    type: integer
                    description: '*the number of results returned in the **`items`** array*'
                  items:
                    type: array
                    items:
                      type: string
                    description: '*HTML pages*'
                  items.page:
                    type: integer
                    description: '*serial number of the returned HTML page*'
                  items.date:
                    type: string
                    description: >-
                      *date and time when the HTML page was scanned* in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: `2019-11-15
                      12:57:46 +00:00`
                  items.html:
                    type: string
                    description: '*HTML page*'
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