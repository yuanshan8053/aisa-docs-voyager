> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Live Google My Business Questions and Answers Tasks

> This endpoint will provide you with a detailed overview of questions and answers associated with a specific business entity listed on Google My Business.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/business_data/google/questions_and_answers/live
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
  /dataforseo/business_data/google/questions_and_answers/live:
    post:
      summary: Setting Live Google My Business Questions and Answers Tasks
      description: >-
        This endpoint will provide you with a detailed overview of questions and
        answers associated with a specific business entity listed on Google My
        Business. By submitting a request to this endpoint, you can access
        comprehensive data on the inquiries and responses related to a
        particular business, including the full text of the questions and
        answers, as well as metadata such as timestamps, user information.
      operationId: post_dataforseo_business_data_google_questions_and_answers_live
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
                depth:
                  type: integer
                  description: >-
                    *parsing depth* optional field number of results in SERP
                    default value: `20` max value: `100` **Your account will be
                    billed per each SERP containing up to 20 results;** Setting
                    depth above 20 may result in additional charges if the
                    search engine returns more than 20 results; If the specified
                    depth is higher than the number of questions in the
                    response, the difference will be refunded automatically to
                    your account balance; The cost can be calculated on the
                    [Pricing](https://dataforseo.com/pricing/business-data/google-questions-and-answers-api-pricing
                    "Pricing") page.
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
                  result.cid:
                    type: string
                    description: >-
                      *google-defined client id* unique id of a local
                      establishment; learn more about the identifier in [this
                      help center
                      article](https://dataforseo.com/help-center/what-is-cid-place-id-feature-id)
                  result.feature_id:
                    type: string
                    description: '*unique identifier of the SERP feature*'
                  result.item_types:
                    type: array
                    items:
                      type: string
                    description: >-
                      *item types* types of search engine results encountered in
                      the `items` array; possible item types:
                      `google_business_question_item`
                  items_without_answers:
                    type: array
                    items:
                      type: string
                    description: '*array of google business question items without answers*'
                  items_without_answers.type:
                    type: string
                    description: '*type of element = **‘google\_business\_question\_item’***'
                  items_without_answers.rank_group:
                    type: integer
                    description: >-
                      *position within a group of elements with identical `type`
                      values* positions of elements with different `type` values
                      are omitted from `rank_group`
                  items_without_answers.rank_absolute:
                    type: integer
                    description: '*absolute rank among all the elements*'
                  items_without_answers.question_id:
                    type: string
                    description: '*ID of the question*'
                  items_without_answers.url:
                    type: string
                    description: '*URL of the question*'
                  items_without_answers.profile_image_url:
                    type: string
                    description: '*URL of the user’s profile image*'
                  items_without_answers.profile_url:
                    type: string
                    description: '*URL of the user’s profile*'
                  items_without_answers.profile_name:
                    type: string
                    description: '*displayed name of the user*'
                  items_without_answers.question_text:
                    type: string
                    description: '*current text of the question*'
                  items_without_answers.original_question_text:
                    type: string
                    description: '*original text of the question*'
                  items_without_answers.time_ago:
                    type: string
                    description: '*estimated time when the question was posted*'
                  items_without_answers.timestamp:
                    type: string
                    description: '*exact time when the question was posted*'
                  items_without_answers.items:
                    type: array
                    items:
                      type: string
                    description: >-
                      *array of items* items within
                      `google_business_question_item`
                  items_without_answers.items_count:
                    type: integer
                    description: '*the number of items in the `items` array*'
                  items:
                    type: array
                    items:
                      type: string
                    description: >-
                      *array of google business question items with answers*
                      possible item types: `google_business_question_item`
                  items.type:
                    type: string
                    description: >-
                      *type of the element =
                      **‘google\_business\_answer\_element’***
                  items.rank_group:
                    type: integer
                    description: >-
                      *position within a group of elements with identical `type`
                      values* positions of elements with different `type` values
                      are omitted from `rank_group`
                  items.rank_absolute:
                    type: integer
                    description: '*absolute rank among all the elements*'
                  items.question_id:
                    type: string
                    description: '*ID of the question*'
                  items.url:
                    type: string
                    description: '*URL of the question*'
                  items.profile_image_url:
                    type: string
                    description: '*URL of the user’s profile image*'
                  items.profile_url:
                    type: string
                    description: '*URL of the user’s profile*'
                  items.profile_name:
                    type: string
                    description: '*displayed name of the user*'
                  items.question_text:
                    type: string
                    description: '*current text of the question*'
                  items.original_question_text:
                    type: string
                    description: '*original text of the question*'
                  items.time_ago:
                    type: string
                    description: '*estimated time when the answer was posted*'
                  items.timestamp:
                    type: string
                    description: '*exact time when the answer was posted*'
                  items.items:
                    type: array
                    items:
                      type: string
                    description: >-
                      *array of items within `google_business_question_item`*
                      contains answers to the google business questions;
                      possible item types `google_business_answer_element`
                  items.answer_id:
                    type: string
                    description: '*ID of the answer*'
                  items.answer_text:
                    type: string
                    description: '*current text of the answer*'
                  items.original_answer_text:
                    type: string
                    description: '*original text of the answer*'
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