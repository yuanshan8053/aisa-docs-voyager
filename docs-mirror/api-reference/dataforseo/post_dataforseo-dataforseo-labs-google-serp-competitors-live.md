> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP Competitors

> This endpoint will provide you with a list of domains ranking for the keywords you specify.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/google/serp_competitors/live
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
  /dataforseo/dataforseo_labs/google/serp_competitors/live:
    post:
      summary: SERP Competitors
      description: >-
        This endpoint will provide you with a list of domains ranking for the
        keywords you specify. You will also get SERP rankings, rating, estimated
        traffic volume, and visibility values the provided domains gain from the
        specified keywords.
      operationId: post_dataforseo_dataforseo_labs_google_serp_competitors_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                keywords:
                  type: array
                  items:
                    type: string
                  description: >-
                    keywords array required field the results will be based on
                    the keywords you specify in this array UTF-8 encoding; the
                    keywords will be converted to lowercase format; you can
                    specify the maximum of 200 keywords learn more about rules
                    and limitations of keyword and keywords fields in DataForSEO
                    APIs in this Help Center article
                location_name:
                  type: string
                  description: >-
                    full name of the location required field if you don’t
                    specify location_code Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with location_name parameters by making
                    a separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: United Kingdom
                location_code:
                  type: integer
                  description: >-
                    unique location identifier required field if you don’t
                    specify location_name Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_code parameters by
                    making a separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language required field if you don’t
                    specify language_code Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available languages with their language_name parameters by
                    making a separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    unique language identifier required field if you don’t
                    specify language_name Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available languages with their language_code parameters by
                    making a separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: en
                include_subdomains:
                  type: boolean
                  description: >-
                    indicates if the subdomains will be included in the search
                    optional field if set to false, the subdomains will be
                    ignored default value: true
                item_types:
                  type: array
                  items:
                    type: string
                  description: >-
                    search results type indicates type of search results
                    included in the response optional field possible values:
                    ["organic", "paid", "featured_snippet", "local_pack"]
                    default value: ["organic", "paid"]
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned domains optional field
                    default value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned domains optional
                    field default value: 0 if you specify the 10 value, the
                    first ten domains in the results array will be omitted and
                    the data will be provided for the successive domains
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: regex, not_regex, , , >,
                    >=, =, , in, not_in, match, not_match, ilike, not_ilike,
                    like, not_like you can use the % operator with like and
                    not_like, as well as ilike and not_ilike to match any string
                    of zero or more characters example:
                    ["median_position","in",[1,10]]
                    [["median_position","in",[1,10]],"and",["domain","not_like","%wikipedia.org%"]]
                    [["domain","not_like","%wikipedia.org%"], "and",
                    [["relevant_serp_items",">",0],"or",["median_position","in",[1,10]]]]
                    for more information about filters, please refer to
                    Dataforseo Labs – Filters or this help center guide
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    results sorting rules optional field you can use the same
                    values as in the filters array to sort the results possible
                    sorting types: asc – results will be sorted in the ascending
                    order desc – results will be sorted in the descending order
                    the comma is used as a separator example:
                    ["avg_position,asc"] default rule: ["rating,desc"] note that
                    you can set no more than three sorting rules in a single
                    request you should use a comma to separate several sorting
                    rules example: ["avg_position,asc","etv,desc"]
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - keywords
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
                  tasks.result.seed_keywords:
                    type: array
                    items:
                      type: string
                    description: >-
                      keywords specified in the request keyword is returned with
                      decoded %## (plus character ‘+’ will be decoded to a space
                      character)
                  tasks.result.location_code:
                    type: integer
                    description: >-
                      location code in a POST array if there is no data, then
                      the value is null
                  tasks.result.language_code:
                    type: string
                    description: >-
                      language code in a POST array if there is no data, then
                      the value is null
                  tasks.result.total_count:
                    type: integer
                    description: >-
                      the total amount of results in our database relevant to
                      your request
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains detected SERP competitors and related data
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.domain:
                    type: string
                    description: domain name of the detected SERP competitor
                  tasks.result.items.avg_position:
                    type: integer
                    description: >-
                      the average position of the domain for the specified
                      keywords the arithmetic mean of values in the
                      keywords_positions array
                  tasks.result.items.median_position:
                    type: integer
                    description: >-
                      the median position of the domain for the specified
                      keywords the median of the values in the
                      keywords_positions array
                  tasks.result.items.rating:
                    type: integer
                    description: >-
                      the margin between the greatest possible and actual
                      keyword positions represents the relative visibility rate
                      of the domain in SERP for the specified keywords
                      calculated as sum(100-keywords_positions)
                  tasks.result.items.etv:
                    type: number
                    description: >-
                      estimated traffic volume represents the estimated monthly
                      traffic that specified keywords are driving to the website
                      calculated as the sum of the products of the specified
                      keywords’ search volume values and CTR
                      (click-through-rate) rates at certain positions in SERP
                      learn more about how the metric is calculated in this help
                      center article
                  tasks.result.items.keywords_count:
                    type: integer
                    description: >-
                      the number of specified keywords the domain has positions
                      for in SERPs
                  tasks.result.items.visibility:
                    type: number
                    description: >-
                      SERP visibility rate represents the website visibility
                      rate based on the SERP positions of the specified keywords
                      Keywords with positions in the range from 1 to 10 are
                      assigned the visibility index from 1 to 0.1, respectively
                      Keywords with positions in the range from 11 to 20 have
                      the fixed visibility index of 0.05 keywords with positions
                      from 20 to 100 have the visibility index equal to 0
                  tasks.result.items.relevant_serp_items:
                    type: integer
                    description: >-
                      the number of SERP elements relevant to the domain
                      represents the number of search results in SERP relevant
                      to the domain for the specified keywords
                  tasks.result.items.keywords_positions:
                    type: object
                    description: >-
                      keyword positions SERP positions the related domain holds
                      in SERP for the specified keywords
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