> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live LLM Mentions

> Live LLM Mentions Search endpoint provides mention data and related metrics from AI searches.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/ai_optimization/llm_mentions/search/live
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
  /dataforseo/ai_optimization/llm_mentions/search/live:
    post:
      summary: Live LLM Mentions
      description: >-
        Live LLM Mentions Search endpoint provides mention data and related
        metrics from AI searches. The results are specific to the selected
        platform (`google` for Google’s AI Overview or `chat_gpt` for ChatGPT),
        as well as location and language parameters (see [the List of Locations
        &
        Languages](https://docs.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages.md)).
      operationId: post_dataforseo_ai_optimization_llm_mentions_search_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                target:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of objects containing target entities required field
                    you can specify up to 10 entities (objects) in the target
                    field one target entity can contain either one domain or one
                    keyword and related parametersexamples: target array with a
                    domain entity [{"domain": "en.wikipedia.org",
                    "search_filter": "exclude"}] target array with a keyword
                    entity [{"keyword": "bmw", "search_scope": ["question"],
                    "match_type ": "partial_match"}] target array with multiple
                    entities [{"domain": "en.wikipedia.org", "search_filter":
                    "exclude"}, {"keyword": "bmw", "match_type ":
                    "partial_match", "search_scope": ["answer"]}]
                domain_entity:
                  type: object
                  description: >-
                    domain entity in the target array example: {"domain":
                    "en.wikipedia.org", "search_filter": "exclude",
                    "search_scope": ["sources"]}
                domain:
                  type: string
                  description: >-
                    target domain required field if you don't specify keyword
                    you can specify up to 63 characters in the domain field; a
                    domain should be specified without https:// and www.
                search_filter:
                  type: string
                  description: >-
                    target keyword search filter optional field possible values:
                    include, exclude default value: include
                search_scope:
                  type: array
                  items:
                    type: string
                  description: >-
                    target keyword search scope optional field possible values:
                    any, question, answer, brand_entities, fan_out_queries
                    default value: any
                include_subdomains:
                  type: boolean
                  description: >-
                    indicates if the subdomains of the target domain will be
                    included in the search optional field if set to true, the
                    subdomains will be included in the search default value:
                    false
                keyword_entity:
                  type: object
                  description: >-
                    keyword entity in the target array example: {"keyword":
                    "bmw", "search_filter": "include", "search_scope":
                    ["question"], "match_type ": "partial_match"}
                keyword:
                  type: string
                  description: >-
                    target keyword required field if you don't specify domain
                    you can specify up to 250 characters in the keyword field
                    all %## will be decoded (plus character ‘+’ will be decoded
                    to a space character) if you need to use the “%” character
                    for your keyword, please specify it as “%25”; if you need to
                    use the “+” character for your keyword, please specify it as
                    “%2B”learn more about rules and limitations of keyword and
                    keywords fields in DataForSEO APIs in this Help Center
                    article
                match_type:
                  type: string
                  description: >-
                    target keyword match type defines how the specified keyword
                    is matched optional field possible values: word_match -
                    full-text search for terms that match the specified seed
                    keyword with additional words included before, after, or
                    within the key phrase (e.g., search for "light" will return
                    results with "light bulb", "light switch"); partial_match -
                    substring search that finds all instances containing the
                    specified sequence of characters, even if it appears inside
                    a longer word (e.g., search for "light" will return results
                    with "lighting", "highlight"); default value: word_match
                location_name:
                  type: string
                  description: >-
                    full name of search location optional field if you use this
                    field, you don't need to specify location_code if you don't
                    specify this field, the location_code with 2840 value will
                    be used by default; you can receive the list of available
                    locations of the search engine with their location_name by
                    making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages
                    Note: chat_gpt data is available for United States only
                location_code:
                  type: integer
                  description: >-
                    search location code optional field if you use this field,
                    you don't need to specify location_name you can receive the
                    list of available locations of the search engine with their
                    location_code by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages
                    default value: 2840 Note: chat_gpt data is available for
                    2840 only
                language_name:
                  type: string
                  description: >-
                    full name of search language optional field if you use this
                    field, you don't need to specify language_code; if you don't
                    specify this field, the language_code with en value will be
                    used by default; you can receive the list of available
                    languages of the search engine with their language_name by
                    making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages
                    Note: chat_gpt data is available for English only
                language_code:
                  type: string
                  description: >-
                    search language code optional field if you use this field,
                    you don't need to specify language_name; you can receive the
                    list of available languages of the search engine with their
                    language_code_by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages
                    default value: en Note: chat_gpt data is available for en
                    onlyn
                platform:
                  type: string
                  description: >-
                    target platform optional field possible values: chat_gpt,
                    google default value: google Note: the data returned depends
                    on the selected platform Note #2:chat_gpt data is available
                    for the United States and English only
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: =, , in, not_in, like,
                    not_like, ilike, not_ilike, match, not_match you can use the
                    % operator with like and not_like to match any string of
                    zero or more characters example:
                    ["ai_search_volume",">","1000"]The full list of possible
                    filters is available here.
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    results sorting rules optional field you can use the same
                    values as in the filters array to sort the results possible
                    sorting types: asc - results will be sorted in the ascending
                    order desc - results will be sorted in the descending order
                    you should use a comma to set up a sorting type example:
                    ["ai_search_volume,desc"] note that you can set no more than
                    three sorting rules in a single request you should use a
                    comma to separate several sorting rules
                offset:
                  type: integer
                  description: >-
                    offset in the results array of the returned mentions data
                    optional fielddefault value: 0 example: if you specify the
                    10 value, the first ten mentions objects in the results
                    array will be omitted and the data will be provided for the
                    successive objects; Note: the maximum value is 9,000, use
                    the search_after_token if you would like to offset more
                    results
                search_after_token:
                  type: string
                  description: >-
                    token for subsequent requests optional field provided in the
                    identical filed of the response to each request; use this
                    parameter to avoid timeouts while trying to obtain over
                    20,000 results in a single request; by specifying the unique
                    search_after_token value from the response array, you will
                    get the subsequent results of the initial task;
                    search_after_token values are unique for each subsequent
                    task ; Note: if the search_after_token is specified in the
                    request, all other parameters should be identical to the
                    previous request
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned objects optional fielddefault
                    value: 100 maximum value: 1000
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - target
                - domain
                - keyword
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
                  tasks.result.total_count:
                    type: integer
                    description: total amount of results relevant the request
                  tasks.result.current_offset:
                    type: integer
                    description: >-
                      the number of mentions objects that are omitted in the
                      items array
                  tasks.result.search_after_token:
                    type: string
                    description: >-
                      token for subsequent requests by specifying the unique
                      search_after_token when setting a new task, you will get
                      the subsequent results of the initial task;
                      search_after_token values are unique for each subsequent
                      task
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains relevant mentions data
                  tasks.result.items.platform:
                    type: string
                    description: platform received in a POST array
                  tasks.result.items.model_name:
                    type: string
                    description: >-
                      name of the AI model from which the data was retrieved
                      Note: for the google platform type, the value is always
                      google_ai_overview
                  tasks.result.items.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.items.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.items.question:
                    type: string
                    description: relevant question
                  tasks.result.items.answer:
                    type: string
                    description: >-
                      relevant answer in markdown format content of the result
                      formatted in the markdown markup language
                  tasks.result.items.sources:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of sources the sources the model cited or relied on
                      in its final answer
                  tasks.result.items.sources.snippet:
                    type: string
                    description: source description
                  tasks.result.items.sources.source_name:
                    type: string
                    description: source name
                  tasks.result.items.sources.thumbnail:
                    type: string
                    description: source thumbnail
                  tasks.result.items.sources.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.sources.position:
                    type: integer
                    description: position in the results
                  tasks.result.items.sources.title:
                    type: string
                    description: source title
                  tasks.result.items.sources.domain:
                    type: string
                    description: source domain
                  tasks.result.items.sources.url:
                    type: string
                    description: source URL
                  tasks.result.items.sources.publication_date:
                    type: string
                    description: >-
                      date and time when the result was published in the format:
                      “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”
                      example: 2019-11-15 12:57:46 +00:00
                  tasks.result.items.search_results:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of search results all web search outputs the model
                      retrieved when looking up information, including
                      duplicates and unused entries
                  tasks.result.items.search_results.description:
                    type: string
                    description: result description
                  tasks.result.items.search_results.breadcrumb:
                    type: string
                    description: breadcrumb
                  tasks.result.items.search_results.position:
                    type: integer
                    description: position in the results
                  tasks.result.items.search_results.title:
                    type: string
                    description: result title
                  tasks.result.items.search_results.domain:
                    type: string
                    description: result domain
                  tasks.result.items.search_results.url:
                    type: string
                    description: result URL
                  tasks.result.items.search_results.publication_date:
                    type: string
                    description: >-
                      date and time when the result was published in the format:
                      “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”
                      example: 2019-11-15 12:57:46 +00:00
                  tasks.result.items.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.items.monthly_searches:
                    type: array
                    items:
                      type: string
                    description: >-
                      monthly AI search volume rates array of objects with AI
                      search volume rates in a certain month of a year
                  tasks.result.items.monthly_searches.year:
                    type: integer
                    description: year
                  tasks.result.items.monthly_searches.month:
                    type: integer
                    description: month
                  tasks.result.items.monthly_searches.search_volume:
                    type: integer
                    description: >-
                      AI search volume rate in a certain month of a year learn
                      more about this metric here
                  tasks.result.items.first_response_at:
                    type: string
                    description: >-
                      date and time when the response data was first recorded in
                      the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2025-10-21 06:25:30 +00:00
                  tasks.result.items.last_response_at:
                    type: string
                    description: >-
                      date and time when the response data was last updated in
                      the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2025-10-21 06:25:30 +00:00
                  tasks.result.items.brand_entities:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of brand entities contains information on brands
                      mentioned in the response
                  tasks.result.items.brand_entities.position:
                    type: integer
                    description: position in the results
                  tasks.result.items.brand_entities.title:
                    type: string
                    description: name of the brand
                  tasks.result.items.brand_entities.category:
                    type: string
                    description: category of the brand
                  tasks.result.items.fan_out_queries:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of fan-out queries contains related search queries
                      derived from the main query to provide a more
                      comprehensive response
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