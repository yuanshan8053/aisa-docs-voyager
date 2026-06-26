> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Keywords For Categories

> This endpoint will provide you with a list of keywords relevant to the specified product categories.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/google/keywords_for_categories/live
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
  /dataforseo/dataforseo_labs/google/keywords_for_categories/live:
    post:
      summary: Keywords For Categories
      description: >-
        This endpoint will provide you with a list of keywords relevant to the
        specified product categories. You will get the search volume rate for
        the last month, search volume trend for the previous 12 months, as well
        as current cost-per-click and competition values for each keyword.
      operationId: post_dataforseo_dataforseo_labs_google_keywords_for_categories_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                category_codes:
                  type: array
                  items:
                    type: string
                  description: >-
                    product and service categories required field The maximum
                    number of categories you can specify: 20 you can download
                    the full list of possible categories
                location_name:
                  type: string
                  description: >-
                    full name of the location required field if you don’t
                    specify location_code Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: United Kingdom
                location_code:
                  type: integer
                  description: >-
                    unique location identifier required field if you don’t
                    specify location_name Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_code by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language required field if you don’t
                    specify language_code Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available languages with their language_name by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    unique language identifier required field if you don’t
                    specify language_name Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available languages with their language_code by making a
                    separate request to the
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: en
                category_intersection:
                  type: boolean
                  description: >-
                    category intersections optional field if set to true, you
                    will get keywords featured in all specified categories; if
                    set to false, you will keywords that are specified in any of
                    the specified categories; default value: true
                include_serp_info:
                  type: boolean
                  description: >-
                    include data from SERP for each keyword optional field if
                    set to true, we will return a serp_info array containing
                    SERP data (number of search results, relevant URL, and SERP
                    features) for every keyword in the response default value:
                    false
                include_clickstream_data:
                  type: boolean
                  description: >-
                    include or exclude data from clickstream-based metrics in
                    the result optional field if the parameter is set to true,
                    you will receive clickstream_keyword_info,
                    keyword_info_normalized_with_clickstream, and
                    keyword_info_normalized_with_bing fields in the response
                    default value: false with this parameter enabled, you will
                    be charged double the price for the request learn more about
                    how clickstream-based metrics are calculated in this help
                    center article
                ignore_synonyms:
                  type: boolean
                  description: >-
                    ignore highly similar keywords optional field if set to true
                    only core keywords will be returned, all highly similar
                    keywords will be excluded; default value: false
                limit:
                  type: integer
                  description: >-
                    the maximum number of keywords in the results array optional
                    field default value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned keywords optional
                    field default value: 0 if you specify the 10 value, the
                    first ten keywords in the results array will be omitted and
                    the data will be provided for the successive keywords Note:
                    we recommend using this parameter only when retrieving up to
                    10,000 results for retrieving over 10,000 results, use the
                    offset_token instead.
                offset_token:
                  type: string
                  description: >-
                    offset token for subsequent requests optional field provided
                    in the identical filed of the response to each request; use
                    this parameter to avoid timeouts while trying to obtain over
                    10,000 results in a single request; by specifying the unique
                    offset_token value from the response array, you will get the
                    subsequent results of the initial task; offset_token values
                    are unique for each subsequent task Note: if the
                    offset_token is specified in the request, all other
                    parameters except limit will not be taken into account when
                    processing a task. learn more about this parameter on our
                    Help Center
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
                    not_like,as well as ilike, not_ilike to match any string of
                    zero or more characters example:
                    ["keyword_info.search_volume",">",0]
                    [["keyword_info.search_volume","in",[0,1000]], "and",
                    ["keyword_info.competition_level","=","LOW"]]
                    [["keyword_info.search_volume",">",100], "and",
                    [["keyword_info.cpc"," for more information about filters,
                    please refer to Dataforseo Labs – Filters or this help
                    center guide
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    results sorting rules optional field you can use the same
                    values as in the filters array to sort the results possible
                    sorting types: asc – results will be sorted in the ascending
                    order desc – results will be sorted in the descending order
                    you should use a comma to set up a sorting type example:
                    ["keyword_info.competition,desc"] default rule:
                    ["keyword_info.search_volume,desc"] note that you can set no
                    more than three sorting rules in a single request you should
                    use a comma to separate several sorting rules example:
                    ["keyword_info.search_volume,desc","keyword_info.competition,asc"]
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - category_codes
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
                  tasks.result.seed_categories:
                    type: array
                    items:
                      type: string
                    description: categories in a POST array
                  tasks.result.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.total_count:
                    type: integer
                    description: >-
                      the total amount of results in our database relevant to
                      your request
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.offset:
                    type: integer
                    description: current offset value
                  tasks.result.offset_token:
                    type: string
                    description: >-
                      offset token for subsequent requests you can use the
                      string provided in this field to get the subsequent
                      results of the initial task; note: offset_token values are
                      unique for each subsequent task
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains keyword ideas and related data
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword:
                    type: string
                    description: found keyword
                  tasks.result.items.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.items.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.items.keyword_info:
                    type: object
                    description: keyword data for the returned keyword idea
                  tasks.result.items.keyword_info.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword_info.last_updated_time:
                    type: string
                    description: >-
                      date and time when keyword data was updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.keyword_info.competition:
                    type: number
                    description: >-
                      competition represents the relative amount of competition
                      associated with the given keyword; the value is based on
                      Google Ads data and can be between 0 and 1 (inclusive)
                  tasks.result.items.keyword_info.competition_level:
                    type: string
                    description: >-
                      competition level represents the relative level of
                      competition associated with the given keyword in paid SERP
                      only; possible values: LOW, MEDIUM, HIGH if competition
                      level is unknown, the value is null; learn more about the
                      metric in this help center article
                  tasks.result.items.keyword_info.cpc:
                    type: number
                    description: >-
                      cost-per-click represents the average cost per click (USD)
                      historically paid for the keyword
                  tasks.result.items.keyword_info.search_volume:
                    type: integer
                    description: >-
                      average monthly search volume rate represents the
                      (approximate) number of searches for the given keyword
                      idea on google.com
                  tasks.result.items.keyword_info.low_top_of_page_bid:
                    type: number
                    description: >-
                      minimum bid for the ad to be displayed at the top of the
                      first page indicates the value greater than about 20% of
                      the lowest bids for which ads were displayed (based on
                      Google Ads statistics for advertisers) the value may
                      differ depending on the location specified in a POST
                      request
                  tasks.result.items.keyword_info.high_top_of_page_bid:
                    type: number
                    description: >-
                      maximum bid for the ad to be displayed at the top of the
                      first page indicates the value greater than about 80% of
                      the lowest bids for which ads were displayed (based on
                      Google Ads statistics for advertisers) the value may
                      differ depending on the location specified in a POST
                      request
                  tasks.result.items.keyword_info.categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      product and service categories you can download the full
                      list of possible categories
                  tasks.result.items.keyword_info.monthly_searches:
                    type: array
                    items:
                      type: string
                    description: >-
                      monthly searches represents the (approximate) number of
                      searches on this keyword idea (as available for the past
                      twelve months), targeted to the specified geographic
                      locations
                  tasks.result.items.keyword_info.monthly_searches.year:
                    type: integer
                    description: year
                  tasks.result.items.keyword_info.monthly_searches.month:
                    type: integer
                    description: month
                  tasks.result.items.keyword_info.monthly_searches.search_volume:
                    type: integer
                    description: monthly average search volume rate
                  tasks.result.items.keyword_info.search_volume_trend:
                    type: object
                    description: >-
                      search volume trend changes represents search volume
                      change in percent compared to the previous period
                  tasks.result.items.keyword_info.search_volume_trend.monthly:
                    type: integer
                    description: >-
                      search volume change in percent compared to the previous
                      month
                  tasks.result.items.keyword_info.search_volume_trend.quarterly:
                    type: integer
                    description: >-
                      search volume change in percent compared to the previous
                      quarter
                  tasks.result.items.keyword_info.search_volume_trend.yearly:
                    type: integer
                    description: >-
                      search volume change in percent compared to the previous
                      year
                  tasks.result.items.clickstream_keyword_info:
                    type: object
                    description: >-
                      clickstream data for the returned keyword to retrieve
                      results for this field, the parameter
                      include_clickstream_data must be set to true
                  tasks.result.items.clickstream_keyword_info.search_volume:
                    type: integer
                    description: monthly average clickstream search volume rate
                  tasks.result.items.clickstream_keyword_info.last_updated_time:
                    type: string
                    description: >-
                      date and time when the clickstream dataset was updated in
                      the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”
                  tasks.result.items.clickstream_keyword_info.gender_distribution:
                    type: object
                    description: >-
                      distribution of estimated clickstream-based metrics by
                      gender learn more about how the metric is calculated in
                      this help center article
                  tasks.result.items.clickstream_keyword_info.gender_distribution.female:
                    type: integer
                    description: number of female users in the relevant clickstream dataset
                  tasks.result.items.clickstream_keyword_info.gender_distribution.male:
                    type: integer
                    description: number of male users in the relevant clickstream dataset
                  tasks.result.items.clickstream_keyword_info.age_distribution:
                    type: object
                    description: >-
                      distribution of clickstream-based metrics by age learn
                      more about how the metric is calculated in this help
                      center article
                  tasks.result.items.clickstream_keyword_info.age_distribution.18-24:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 18-24 age range
                  tasks.result.items.clickstream_keyword_info.age_distribution.25-34:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 25-34 age range
                  tasks.result.items.clickstream_keyword_info.age_distribution.35-44:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 35-44 age range
                  tasks.result.items.clickstream_keyword_info.age_distribution.45-54:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 45-54 age range
                  tasks.result.items.clickstream_keyword_info.age_distribution.55-64:
                    type: integer
                    description: >-
                      number of users in the relevant clickstream dataset that
                      fall within the 55-64 age range
                  tasks.result.items.clickstream_keyword_info.monthly_searches:
                    type: array
                    items:
                      type: string
                    description: >-
                      monthly clickstream search volume rates array of objects
                      with clickstream search volume rates in a certain month of
                      a year
                  tasks.result.items.clickstream_keyword_info.monthly_searches.year:
                    type: integer
                    description: year
                  tasks.result.items.clickstream_keyword_info.monthly_searches.month:
                    type: integer
                    description: month
                  tasks.result.items.clickstream_keyword_info.monthly_searches.search_volume:
                    type: integer
                    description: >-
                      clickstream-based search volume rate in a certain month of
                      a year
                  tasks.result.items.keyword_properties:
                    type: object
                    description: additional information about the keyword
                  tasks.result.items.keyword_properties.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword_properties.core_keyword:
                    type: string
                    description: >-
                      main keyword in a group contains the main keyword in a
                      group determined by the synonym clustering algorithm if
                      the value is null, our database does not contain any
                      keywords the corresponding algorithm could identify as
                      synonymous with keyword
                  tasks.result.items.keyword_properties.synonym_clustering_algorithm:
                    type: string
                    description: >-
                      the algorithm used to identify synonyms possible values:
                      keyword_metrics – indicates the algorithm based on
                      keyword_info parameters text_processing – indicates the
                      text-based algorithm if the value is null, our database
                      does not contain any keywords the corresponding algorithm
                      could identify as synonymous with keyword
                  tasks.result.items.keyword_properties.keyword_difficulty:
                    type: integer
                    description: >-
                      difficulty of ranking in the first top-10 organic results
                      for a keyword indicates the chance of getting in top-10
                      organic results for a keyword on a logarithmic scale from
                      0 to 100; calculated by analysing, among other parameters,
                      link profiles of the first 10 pages in SERP; learn more
                      about the metric in this help center guide
                  tasks.result.items.keyword_properties.detected_language:
                    type: string
                    description: >-
                      detected language of the keyword indicates the language of
                      the keyword as identified by our system
                  tasks.result.items.keyword_properties.is_another_language:
                    type: boolean
                    description: >-
                      detected language of the keyword is different from the set
                      language if true, the language set in the request does not
                      match the language determined by our system for a given
                      keyword
                  tasks.result.items.keyword_properties.words_count:
                    type: integer
                    description: >-
                      number of words in the keyword indicates how many words
                      the keyword consists of
                  tasks.result.items.serp_info:
                    type: object
                    description: >-
                      SERP data the value will be null if you didn’t set the
                      field include_serp_info to true in the POST array or if
                      there is no SERP data for this keyword in our database
                  tasks.result.items.serp_info.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.serp_info.check_url:
                    type: string
                    description: >-
                      direct URL to search engine results you can use it to make
                      sure that we provided accurate results
                  tasks.result.items.serp_info.serp_item_types:
                    type: array
                    items:
                      type: string
                    description: >-
                      types of search results in SERP contains types of search
                      results (items) found in SERP possible item types:
                      answer_box, app, carousel, multi_carousel,
                      featured_snippet, google_flights, google_reviews,
                      third_party_reviews, google_posts, images, jobs,
                      knowledge_graph, local_pack, hotels_pack, map, organic,
                      paid, people_also_ask, related_searches,
                      people_also_search, shopping, top_stories, twitter, video,
                      events, mention_carousel, recipes, top_sights,
                      scholarly_articles, popular_products, podcasts,
                      questions_and_answers, find_results_on, stocks_box,
                      visual_stories, commercial_units, local_services,
                      google_hotels, math_solver, currency_box,
                      product_considerations, found_on_web, short_videos,
                      refine_products, explore_brands, perspectives,
                      discussions_and_forums, compare_sites, courses,
                      ai_overview; note that the actual results will be returned
                      only for organic, paid, featured_snippet, and local_pack
                      elements
                  tasks.result.items.serp_info.se_results_count:
                    type: string
                    description: number of search results for the returned keyword
                  tasks.result.items.serp_info.last_updated_time:
                    type: string
                    description: >-
                      date and time when SERP data was updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.serp_info.previous_updated_time:
                    type: string
                    description: >-
                      previous to the most recent date and time when SERP data
                      was updated in the UTC format: “yyyy-mm-dd hh-mm-ss
                      +00:00” example: 2019-11-15 12:57:46 +00:00
                  tasks.result.items.avg_backlinks_info:
                    type: object
                    description: >-
                      backlink data for the returned keyword this object
                      provides the average number of backlinks, referring pages
                      and domains, as well as the average rank values among the
                      top-10 webpages ranking organically for the keyword
                  tasks.result.items.avg_backlinks_info.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.avg_backlinks_info.backlinks:
                    type: number
                    description: average number of backlinks
                  tasks.result.items.avg_backlinks_info.dofollow:
                    type: number
                    description: average number of dofollow links
                  tasks.result.items.avg_backlinks_info.referring_pages:
                    type: number
                    description: average number of referring pages
                  tasks.result.items.avg_backlinks_info.referring_domains:
                    type: number
                    description: average number of referring domains
                  tasks.result.items.avg_backlinks_info.referring_main_domains:
                    type: number
                    description: average number of referring main domains
                  tasks.result.items.avg_backlinks_info.rank:
                    type: number
                    description: >-
                      average rank learn more about the metric and its
                      calculation formula in this help center article
                  tasks.result.items.avg_backlinks_info.main_domain_rank:
                    type: number
                    description: >-
                      average main domain rank learn more about the metric and
                      its calculation formula in this help center article
                  tasks.result.items.avg_backlinks_info.last_updated_time:
                    type: string
                    description: >-
                      date and time when backlink data was updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.search_intent_info:
                    type: object
                    description: >-
                      search intent info for the returned keyword learn about
                      search intent in this help center article
                  tasks.result.items.search_intent_info.se_type:
                    type: string
                    description: 'search engine type possible values: google'
                  tasks.result.items.search_intent_info.main_intent:
                    type: string
                    description: >-
                      main search intent possible values: informational,
                      navigational, commercial, transactional
                  tasks.result.items.search_intent_info.foreign_intent:
                    type: array
                    items:
                      type: string
                    description: >-
                      supplementary search intents possible values:
                      informational, navigational, commercial, transactional
                  tasks.result.items.search_intent_info.last_updated_time:
                    type: string
                    description: >-
                      date and time when search intent data was last updated in
                      the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2019-11-15 12:57:46 +00:00
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_bing:
                    type: object
                    description: >-
                      contains keyword search volume normalized with Bing search
                      volume
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_bing.last_updated_time:
                    type: string
                    description: >-
                      date and time when the dataset was updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_bing.search_volume:
                    type: integer
                    description: current search volume rate of a keyword
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_bing.is_normalized:
                    type: boolean
                    description: >-
                      keyword info is normalized if true, values are normalized
                      with Bing data
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_bing.monthly_searches:
                    type: integer
                    description: >-
                      monthly search volume rates array of objects with search
                      volume rates in a certain month of a year
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_bing.monthly_searches.year:
                    type: integer
                    description: year
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_bing.monthly_searches.month:
                    type: integer
                    description: month
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_bing.monthly_searches.search_volume:
                    type: integer
                    description: search volume rate in a certain month of a year
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_clickstream:
                    type: object
                    description: >-
                      contains keyword search volume normalized with clickstream
                      data
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_clickstream.last_updated_time:
                    type: string
                    description: >-
                      date and time when the dataset was updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_clickstream.search_volume:
                    type: integer
                    description: current search volume rate of a keyword
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_clickstream.is_normalized:
                    type: boolean
                    description: >-
                      keyword info is normalized if true, values are normalized
                      with clickstream data
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_clickstream.monthly_searches:
                    type: integer
                    description: >-
                      monthly search volume rates array of objects with search
                      volume rates in a certain month of a year
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_clickstream.monthly_searches.year:
                    type: integer
                    description: year
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_clickstream.monthly_searches.month:
                    type: integer
                    description: month
                  tasks.result.items.search_intent_info.keyword_info_normalized_with_clickstream.monthly_searches.search_volume:
                    type: integer
                    description: search volume rate in a certain month of a year
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