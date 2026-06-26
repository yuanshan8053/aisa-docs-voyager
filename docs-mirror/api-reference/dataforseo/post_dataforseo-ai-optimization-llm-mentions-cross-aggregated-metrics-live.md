> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live LLM Mentions Cross Aggregated Metrics

> Live LLM Mentions endpoint provides aggregated metrics grouped by custom keys for mentions of the keywords or domains specified in the `target` array of the ...



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/ai_optimization/llm_mentions/cross_aggregated_metrics/live
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
  /dataforseo/ai_optimization/llm_mentions/cross_aggregated_metrics/live:
    post:
      summary: Live LLM Mentions Cross Aggregated Metrics
      description: >-
        Live LLM Mentions endpoint provides aggregated metrics grouped by custom
        keys for mentions of the keywords or domains specified in the `target`
        array of the request. Each item in the results array corresponds to the
        specified target. The results are specific to the selected platform
        (`google` for Google’s AI Overview or `chat_gpt` for ChatGPT), location
        and language parameters (see [the List of Locations &
        Languages](https://docs.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages.md)).
      operationId: >-
        post_dataforseo_ai_optimization_llm_mentions_cross_aggregated_metrics_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                targets:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of objects containing target entities with aggregation
                    keys required field you can specify up to 10, but not less
                    than 2 target sets of parameters, each with its
                    aggregation_key;example of a targets array with multiple
                    entities:
                    [{"aggregation_key":"bmw","target":[{"domain":"en.wikipedia.org","search_filter":"exclude"},{"keyword":"m5","match_type":"partial_match","search_scope":["answer"]}]},{"aggregation_key":"mercedes","target":[{"domain":"www.mercedes-benz.com","search_filter":"exclude"},{"keyword":"GLC","match_type":"word_match"}]}]
                aggregation_key:
                  type: string
                  description: >-
                    aggregation key for grouping the results required field
                    groups results for comparison and serves as a label for the
                    group; you can specify up to 250 characters in the
                    aggregation_key field
                target:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of objects containing target entities required field a
                    single target can contain up to 10 domain and/or keyword
                    entities
                domain_entity:
                  type: object
                  description: >-
                    domain entity in the target array example: {"domain":
                    "en.wikipedia.org", "search_filter": "exclude",
                    "search_scope": ["sources"]}
                domain:
                  type: string
                  description: >-
                    target domain required field if you don't specify a keyword
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
                    target keyword required field if you don't specify a domain
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
                initial_dataset_filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of filter expressions applied before aggregation
                    optional field you can use this array to filter expressions
                    applied to the raw mentions database before aggregation to
                    limit the rows contributing to the result;you can add
                    several filters at once (8 filters maximum) you should set a
                    logical operator and, or between the conditions the
                    following operators are supported: =, , in, not_in, like,
                    not_like, ilike, not_ilike, match, not_match you can use the
                    % operator with like and not_like to match any string of
                    zero or more characters example:
                    ["ai_search_volume",">","1000"]the full list of possible
                    filters is available here. learn more about the initial
                    dataset filters in this help center article.
                internal_list_limit:
                  type: integer
                  description: >-
                    maximum number of elements within internal arrays optional
                    field you can use this field to limit the number of elements
                    within the following arrays: sources_domain
                    search_results_domain minimum value: 1 maximum value: 10
                    default value: 5
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - targets
                - aggregation_key
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
                  tasks.result.total:
                    type: object
                    description: >-
                      aggregated mentions metrics summary contains overall
                      aggregated LLM mention metrics across all found domains,
                      grouped by various dimensions
                  tasks.result.total.location:
                    type: array
                    items:
                      type: string
                    description: >-
                      location-based grouping array of objects containing
                      mention metrics segmented by geographical location
                  tasks.result.total.location.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.total.location.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension
                  tasks.result.total.location.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to this
                      specific grouping key
                  tasks.result.total.location.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.total.location.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.total.language:
                    type: array
                    items:
                      type: string
                    description: >-
                      language-based grouping array of objects containing
                      mention metrics segmented by content language
                  tasks.result.total.language.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.total.language.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension
                  tasks.result.total.language.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to this
                      specific grouping key
                  tasks.result.total.language.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.total.language.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.total.platform:
                    type: array
                    items:
                      type: string
                    description: >-
                      platform-based grouping array of group elements containing
                      mention metrics segmented by AI platform
                  tasks.result.total.platform.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.total.platform.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension
                  tasks.result.total.platform.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to this
                      specific grouping key
                  tasks.result.total.platform.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.total.platform.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.total.sources_domain:
                    type: array
                    items:
                      type: string
                    description: >-
                      found top source domains relevant to the target array of
                      objects containing data on top domains that are cited as
                      sources in LLM responses
                  tasks.result.total.sources_domain.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.total.sources_domain.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension in this case the field displays a found
                      domain name
                  tasks.result.total.sources_domain.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to the
                      specific domain
                  tasks.result.total.sources_domain.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.total.sources_domain.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.total.search_results_domain:
                    type: array
                    items:
                      type: string
                    description: >-
                      found top search results domains relevant to the target
                      array of objects containing data on top domains that
                      appear in search results related to LLM queries
                  tasks.result.total.search_results_domain.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.total.search_results_domain.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension in this case the field displays a found
                      domain name
                  tasks.result.total.search_results_domain.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to the
                      specific domain
                  tasks.result.total.search_results_domain.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.total.search_results_domain.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.total.brand_entities_title:
                    type: array
                    items:
                      type: string
                    description: >-
                      data on brand entities relevant to the target array of
                      objects containing data on brand entity titles that appear
                      in search results related to LLM queries
                  tasks.result.total.brand_entities_title.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.total.brand_entities_title.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension in this case the field displays a found
                      brand entity title
                  tasks.result.total.brand_entities_title.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to the
                      specific domain
                  tasks.result.total.brand_entities_title.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.total.brand_entities_title.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.total.brand_entities_category:
                    type: array
                    items:
                      type: string
                    description: >-
                      data on brand entities relevant to the target array of
                      objects containing data on brand entity categories that
                      appear in search results related to LLM queries
                  tasks.result.total.brand_entities_category.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.total.brand_entities_category.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension in this case the field displays a found
                      brand entity category
                  tasks.result.total.brand_entities_category.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to the
                      specific domain
                  tasks.result.total.brand_entities_category.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.total.brand_entities_category.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains relevant mentions data
                  tasks.result.items.key:
                    type: string
                    description: aggregation key received in a POST array
                  tasks.result.items.location:
                    type: array
                    items:
                      type: string
                    description: >-
                      location-based grouping array of objects containing
                      mention metrics segmented by geographical location
                  tasks.result.items.location.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.items.location.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension
                  tasks.result.items.location.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to this
                      specific grouping key
                  tasks.result.items.location.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.items.location.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.items.language:
                    type: array
                    items:
                      type: string
                    description: >-
                      language-based grouping array of objects containing
                      mention metrics segmented by content language
                  tasks.result.items.language.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.items.language.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension
                  tasks.result.items.language.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to this
                      specific grouping key
                  tasks.result.items.language.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.items.language.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.items.platform:
                    type: array
                    items:
                      type: string
                    description: >-
                      platform-based grouping array of group elements containing
                      mention metrics segmented by AI platform
                  tasks.result.items.platform.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.items.platform.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension
                  tasks.result.items.platform.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to this
                      specific grouping key
                  tasks.result.items.platform.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.items.platform.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.items.sources_domain:
                    type: array
                    items:
                      type: string
                    description: >-
                      found top source domains relevant to the target array of
                      objects containing data on top domains that are cited as
                      sources in LLM responses
                  tasks.result.items.sources_domain.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.items.sources_domain.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension in this case the field displays a found
                      domain name
                  tasks.result.items.sources_domain.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to the
                      specific domain
                  tasks.result.items.sources_domain.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.items.sources_domain.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.items.search_results_domain:
                    type: array
                    items:
                      type: string
                    description: >-
                      found top search results domains relevant to the target
                      array of objects containing data on top domains that
                      appear in search results related to LLM queries
                  tasks.result.items.search_results_domain.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.items.search_results_domain.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension in this case the field displays a found
                      domain name
                  tasks.result.items.search_results_domain.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to the
                      specific domain
                  tasks.result.items.search_results_domain.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.items.search_results_domain.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.items.brand_entities_title:
                    type: array
                    items:
                      type: string
                    description: >-
                      data on brand entities relevant to the target array of
                      objects containing data on brand entity titles that appear
                      in search results related to LLM queries
                  tasks.result.items.brand_entities_title.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.items.brand_entities_title.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension in this case the field displays a found
                      brand entity title
                  tasks.result.items.brand_entities_title.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to the
                      specific domain
                  tasks.result.items.brand_entities_title.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.items.brand_entities_title.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
                  tasks.result.items.brand_entities_category:
                    type: array
                    items:
                      type: string
                    description: >-
                      data on brand entities relevant to the target array of
                      objects containing data on brand entity categories that
                      appear in search results related to LLM queries
                  tasks.result.items.brand_entities_category.type:
                    type: string
                    description: type of the element = 'group_element'
                  tasks.result.items.brand_entities_category.key:
                    type: string
                    description: >-
                      grouping identifier the specific identifier for the
                      grouping dimension in this case the field displays a found
                      brand entity category
                  tasks.result.items.brand_entities_category.mentions:
                    type: integer
                    description: >-
                      total LLM mentions count the number of times the target
                      keyword or domain were mentioned in relation to the
                      specific domain
                  tasks.result.items.brand_entities_category.ai_search_volume:
                    type: integer
                    description: >-
                      current AI search volume rate of a keyword learn more
                      about this metric here
                  tasks.result.items.brand_entities_category.impressions:
                    type: integer
                    description: current AI impressions rate of a keyword
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