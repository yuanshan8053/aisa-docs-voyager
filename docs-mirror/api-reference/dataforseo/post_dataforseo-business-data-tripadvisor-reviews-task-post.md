> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Business Data Tripadvisor Reviews Tasks

> This endpoint provides results from the “Reviews” element on the [Tripadvisor](https://www.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/business_data/tripadvisor/reviews/task_post
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
  /dataforseo/business_data/tripadvisor/reviews/task_post:
    post:
      summary: Setting Business Data Tripadvisor Reviews Tasks
      description: >-
        This endpoint provides results from the “Reviews” element on the
        [Tripadvisor](https://www.tripadvisor.com/) platform. The results are
        specific to the URL path or keyword you indicate, and and the selected
        location (see [the List of
        Locations](https://docs.dataforseo.com/v3/business_data/tripadvisor/locations.md)).
      operationId: post_dataforseo_business_data_tripadvisor_reviews_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                url_path:
                  type: string
                  description: >-
                    *URL path of the business entity* **required field if you do
                    not specify `keyword`** URL path to the Tripadvisor page of
                    the business entity; examples:
                    `Hotel_Review-g60763-d23462501-Reviews-Margaritaville_Times_Square-New_York_City_New_York.html`
                    `https://www.tripadvisor.com/Hotel_Review-g60763-d23462501-Reviews-Margaritaville_Times_Square-New_York_City_New_York.html`
                keyword:
                  type: string
                  description: >-
                    *keyword* **required field if you do not specify
                    `url_path`** the keyword you specify should indicate a name
                    of an existing business or prominent place on Tripadvisor;
                    you can specify up to 700 characters in the `keyword` filed;
                    all %## will be decoded (plus character ‘+’ will be decoded
                    to a space character); if you need to use the “%” character
                    for your `keyword`, please specify it as “%25”
                location_name:
                  type: string
                  description: >-
                    *full name of search engine location* **required field if
                    you don’t specify `location_code` or `url_path`** you can
                    receive the list of available locations with `location_name`
                    by making a separate request to the
                    `https://api.dataforseo.com/v3/business_data/tripadvisor/locations`
                    example: `London,England,United Kingdom`
                location_code:
                  type: integer
                  description: >-
                    *search engine location code* **required field if you don’t
                    specify `location_name` or `url_path`** you can receive the
                    list of available locations with `location_code` by making a
                    separate request to the
                    `https://api.dataforseo.com/v3/business_data/tripadvisor/locations`
                    example: `1003854`
                priority:
                  type: integer
                  description: >-
                    *task priority* optional field can take the following
                    values: 1 – normal execution priority (set by default) 2 –
                    high execution priority You will be additionally charged for
                    the tasks with high execution priority. The cost can be
                    calculated on the
                    [Pricing](https://dataforseo.com/pricing/business-data/business-data-api-tripadvisor-pricing
                    "Pricing") page.
                language_name:
                  type: string
                  description: >-
                    *full name of search engine language* optional field **if
                    you use this field, your account will be charged for one
                    extra request** you can receive the list of available
                    languages with `language_name` by making a separate request
                    to the
                    `https://api.dataforseo.com/v3/business_data/tripadvisor/languages`
                    example: `English` You will be additionally charged for
                    setting a language parameter in this endpoint. The cost can
                    be calculated on the
                    [Pricing](https://dataforseo.com/pricing/business-data/business-data-api-tripadvisor-pricing
                    "Pricing") page.
                language_code:
                  type: string
                  description: >-
                    *search engine language code* optional field **if you use
                    this field, your account will be charged for one extra
                    request** you can receive the list of available languages
                    with `language_code` by making a separate request to the
                    `https://api.dataforseo.com/v3/business_data/tripadvisor/languages`
                    example: `en` You will be additionally charged for setting a
                    language parameter in this endpoint. The cost can be
                    calculated on the
                    [Pricing](https://dataforseo.com/pricing/business-data/business-data-api-tripadvisor-pricing
                    "Pricing") page.
                depth:
                  type: integer
                  description: >-
                    *parsing depth* optional field number of reviews in SERP; we
                    strongly recommend setting the parsing depth in the
                    multiples of ten, because our systems processes ten reviews
                    in a row; default value: `10`; max value: `4490` **Your
                    account will be billed per each SERP containing up to 10
                    results;** Setting depth above 10 may result in additional
                    charges if the search engine returns more than 10 results;
                    The cost can be calculated on the
                    [Pricing](https://dataforseo.com/pricing/business-data/business-data-api-tripadvisor-pricing
                    "Pricing") page.
                ratings:
                  type: array
                  items:
                    type: string
                  description: >-
                    *Tripadvisor traveler rating for a place of interest*
                    optional field rating based on the written reviews by a
                    traveler after they visited a place. possible values:
                    `excellent`, `very_good`, `average`, `poor`, `terrible` you
                    can specify several values at once
                visit_type:
                  type: array
                  items:
                    type: string
                  description: >-
                    *filter by type of travelers who left a review* optional
                    field possible values: `families`, `couples`, `solo`,
                    `business`, `friends` you can specify several values at once
                months:
                  type: array
                  items:
                    type: string
                  description: >-
                    *filter by months when a traveler made a visit* optional
                    field possible values: `january`, `february`, `march`,
                    `april`, `may`, `april`, `june`, `july`, `august`,
                    `september`, `october`, `november`, `december` you can
                    specify several values at once
                search_reviews_keyword:
                  type: string
                  description: >-
                    *search reviews containing a specified keyword* example:
                    `dessert`
                sort_by:
                  type: string
                  description: >-
                    *results sorting parameters* optional field you can use this
                    field to sort the results; possible types of sorting:
                    `most_recent` `detailed_reviews`
                translate_reviews:
                  type: boolean
                  description: >-
                    *translate reviews according to the URL path* optional field
                    if set to `true`, returned reviews will be translated to the
                    language matching the specified `url_path`; for example, if
                    `url_path` contains `tripadvisor.it` and `translate_reviews`
                    is `true`, reviews will be translated to the Italian
                    language; default value: `true` you can learn more about how
                    reviews are translated in [this Help Center
                    article](https://dataforseo.com/help-center/how-to-translate-reviews-in-tripadvisor-business-data-api)
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
                - url_path
                - keyword
                - location_name
                - location_code
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