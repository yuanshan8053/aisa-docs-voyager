> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Business Data Google Extended Reviews Tasks

> This endpoint provides results from the “Reviews” element of Google SERPs, including not only Google user reviews but also reviews from other reputable sourc...



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/business_data/google/extended_reviews/task_post
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
  /dataforseo/business_data/google/extended_reviews/task_post:
    post:
      summary: Setting Business Data Google Extended Reviews Tasks
      description: >-
        This endpoint provides results from the “Reviews” element of Google
        SERPs, including not only Google user reviews but also reviews from
        other reputable sources (e.g., TripAdvisor, Yelp, Trustpilot). The
        results are specific to the selected location (see [the List of
        Locations](https://docs.dataforseo.com/v3/business_data-google-locations.md))
        and language (see [the List of
        Languages](https://docs.dataforseo.com/v3/business_data-google-languages.md))
        parameters.
      operationId: post_dataforseo_business_data_google_extended_reviews_task_post
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
                    *keyword* **required field if you don’t specify `cid` or
                    `place_id`** the keyword you specify should indicate the
                    name of the local establishment; you can specify **up to 700
                    characters** in the `keyword` filed; all %## will be decoded
                    (plus character ‘+’ will be decoded to a space character) if
                    you need to use the “%” character for your `keyword`, please
                    specify it as “%25”; if this field contains such parameters
                    as ‘allinanchor:’, ‘allintext:’, ‘allintitle:’, ‘allinurl:’,
                    ‘define:’, ‘filetype:’, ‘id:’, ‘inanchor:’, ‘info:’,
                    ‘intext:’, ‘intitle:’, ‘inurl:’, ‘link:’, ‘related:’,
                    ‘site:’, **the charge per task will be multiplied by 5**
                    Note: queries containing the ‘cache:’ parameter are not
                    supported and will return a validation error learn more
                    about rules and limitations of `keyword` and `keywords`
                    fields in DataForSEO APIs in this [Help Center
                    article](https://dataforseo.com/help-center/rules-and-limitations-of-keyword-and-keywords-fields-in-dataforseo-apis)
                    **Note:** if you use this field, your account will be
                    charged **three times the standard rate** for tasks
                    involving the [Google Reviews
                    API](https://dataforseo.com/pricing/business-data/google-reviews-api)
                cid:
                  type: string
                  description: >-
                    *unique, google-defined id of the business entity*
                    **required field if you don’t specify `keyword` or
                    `place_id`** example: `194604053573767737` learn more about
                    the identifier in [this help center
                    article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)**Note:**
                    if you use this field, your account will be charged **two
                    times the standard rate** for tasks involving the [Google
                    Reviews
                    API](https://dataforseo.com/pricing/business-data/google-reviews-api)
                place_id:
                  type: string
                  description: >-
                    *identifier of the business entity in Google Maps*
                    **required field if you don’t specify `keyword` or `cid`**
                    example: `GhIJQWDl0CIeQUARxks3icF8U8A` learn more about the
                    identifier in [this help center
                    article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)**Note:**
                    if you use this field, your account will be charged **two
                    times the standard rate** for tasks involving the [Google
                    Reviews
                    API](https://dataforseo.com/pricing/business-data/google-reviews-api)
                priority:
                  type: integer
                  description: >-
                    *task priority* optional field can take the following
                    values: 1 – normal execution priority (set by default) 2 –
                    high execution priority You will be additionally charged for
                    the tasks with high execution priority. The cost can be
                    calculated on the
                    [Pricing](https://dataforseo.com/pricing/business-data/google-reviews-api
                    "Pricing") page.
                location_name:
                  type: string
                  description: >-
                    *full name of search engine location* **required field if
                    you don’t specify** `location_code` or `location_coordinate`
                    **if you use this field, you don’t need to specify
                    `location_code` or `location_coordinate`** you can receive
                    the list of available locations with `location_name` by
                    making a separate request to the
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
                    example: `53.476225,-2.243572,200`
                language_name:
                  type: string
                  description: >-
                    *full name of search engine language* **required field if
                    you don’t specify** `language_code` **if you use this field,
                    you don’t need to specify `language_code`** you can receive
                    the list of available languages with `language_name` by
                    making a separate request to the
                    `https://api.dataforseo.com/v3/business_data/google/languages`
                    example: `English`
                language_code:
                  type: string
                  description: >-
                    *search engine language code* **required field if you don’t
                    specify** `language_name` **if you use this field, you don’t
                    need to specify `language_name`** you can receive the list
                    of available languages with their `language_code` by making
                    a separate request to the
                    `https://api.dataforseo.com/v3/business_data/google/languages`
                    example: `en`
                depth:
                  type: integer
                  description: >-
                    *parsing depth* optional field number of reviews in SERP we
                    strongly recommend setting the parsing depth in the
                    multiples of twenty, because our systems processes twenty
                    reviews in a row default value: `20` maximum value: `1000`
                    **Your account will be billed per each SERP containing up to
                    20 results;** Setting depth above 20 may result in
                    additional charges if the search engine returns more than 20
                    results; The cost can be calculated on the
                    [Pricing](https://dataforseo.com/pricing/business-data/google-reviews-api
                    "Pricing") page.
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
                - keyword
                - cid
                - place_id
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