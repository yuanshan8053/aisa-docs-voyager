> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Content Analysis – Search API

> This endpoint will provide you with detailed citation data available for the target keyword.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/content_analysis/search/live
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
  /dataforseo/content_analysis/search/live:
    post:
      summary: Content Analysis – Search API
      description: >-
        This endpoint will provide you with detailed citation data available for
        the target keyword.
      operationId: post_dataforseo_content_analysis_search_live
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
                    target keyword required field UTF-8 encoding the keywords
                    will be converted to a lowercase format; Note: to match an
                    exact phrase instead of a stand-alone keyword, use double
                    quotes and backslashes; example: "keyword": "\"tesla palo
                    alto\"" learn more about rules and limitations of keyword
                    and keywords fields in DataForSEO APIs in this Help Center
                    article
                keyword_fields:
                  type: object
                  description: >-
                    target keyword fields and target keywords optional field use
                    this parameter to filter the dataset by keywords that
                    certain fields should contain; fields you can specify:
                    title, main_title, previous_title, snippet you can indicate
                    several fields; Note: to match an exact phrase instead of a
                    stand-alone keyword, use double quotes and backslashes;
                    example: "keyword_fields": { "snippet": "\"logitech
                    mouse\"", "main_title": "sale" }
                page_type:
                  type: array
                  items:
                    type: string
                  description: >-
                    target page types optional field use this parameter to
                    filter the dataset by page types possible values:
                    "ecommerce", "news", "blogs", "message-boards",
                    "organization"
                search_mode:
                  type: string
                  description: >-
                    results grouping type optional field possible grouping
                    types: as_is – returns all citations for the target keyword
                    one_per_domain – returns one citation of the keyword per
                    domain default value: as_is
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned citations optional field
                    default value: 100 maximum value: 1000
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: regex, not_regex, , , >,
                    >=, =, , in, not_in, like,not_like, match, not_match you can
                    use the % operator with like and not_like to match any
                    string of zero or more characters example: ["country","=",
                    "US"]
                    [["domain_rank",">",800],"and",["content_info.connotation_types.negative",">",0.9]]
                    [["domain_rank",">",800], "and",
                    [["page_types","has","ecommerce"], "or",
                    ["content_info.text_category","has",10994]]] for more
                    information about filters, please refer to Content Analysis
                    API – Filters
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
                    ["content_info.sentiment_connotations.anger,desc"] default
                    rule: ["content_info.sentiment_connotations.anger,desc"]
                    note that you can set no more than three sorting rules in a
                    single request you should use a comma to separate several
                    sorting rules example:
                    ["content_info.sentiment_connotations.anger,desc","keyword_data.keyword_info.cpc,desc"]
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned citations optional
                    field default value: 0 if you specify the 10 value, the
                    first ten citations in the results array will be omitted and
                    the data will be provided for the successive citations Note:
                    we recommend using this parameter only when retrieving up to
                    10,000 results for retrieving over 10,000 results, use the
                    offset_token instead.
                offset_token:
                  type: string
                  description: >-
                    offset token for subsequent requests optional field provided
                    in the identical field of the response to each request; use
                    this parameter to avoid timeouts while trying to obtain over
                    10,000 results in a single request; by specifying the unique
                    offset_token value from the response array, you will get the
                    subsequent results of the initial task; offset_token values
                    are unique for each subsequent task Note: if the
                    offset_token is specified in the request, all other
                    parameters except limit will not be taken into account when
                    processing a task learn more about this parameter on our
                    Help Center
                rank_scale:
                  type: string
                  description: >-
                    defines the scale used for calculating and displaying the
                    domain_rank, and url_rank values optional field you can use
                    this parameter to choose whether rank values are presented
                    on a 0–100 or 0–1000 scale possible values: one_hundred —
                    rank values are displayed on a 0–100 scale one_thousand —
                    rank values are displayed on a 0–1000 scale default value:
                    one_thousand learn more about how this parameter works in
                    this Help Center article
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
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
                  tasks.result.offset_token:
                    type: string
                    description: >-
                      offset token for subsequent requests you can use the
                      string provided in this field to get the subsequent
                      results of the initial task; note: offset_token values are
                      unique for each subsequent task
                  tasks.result.total_count:
                    type: integer
                    description: >-
                      total amount of results in our database relevant to your
                      request
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains citations and related data
                  tasks.result.items.type:
                    type: string
                    description: type of element = ‘content_analysis_search’
                  tasks.result.items.url:
                    type: string
                    description: URL where the citation was found
                  tasks.result.items.domain:
                    type: string
                    description: domain name
                  tasks.result.items.main_domain:
                    type: string
                    description: main domain
                  tasks.result.items.url_rank:
                    type: integer
                    description: >-
                      rank of the url this value is based on backlink data for
                      the given URL from DataForSEO Backlink Index; url_rank is
                      calculated based on the method for node ranking in a
                      linked database – a principle used in the original Google
                      PageRank algorithm learn more about the metric and how it
                      is calculated in this help center article
                  tasks.result.items.spam_score:
                    type: string
                    description: >-
                      backlink spam score of the url this value is based on
                      backlink data for the given URL from DataForSEO Backlink
                      Index; learn more about how the metric is calculated on
                      this help center page
                  tasks.result.items.domain_rank:
                    type: string
                    description: >-
                      rank of the domain this value is based on backlink data
                      for the given domain from DataForSEO Backlink Index;
                      domain_rank is calculated based on the method for node
                      ranking in a linked database – a principle used in the
                      original Google PageRank algorithm learn more about the
                      metric and how it is calculated in this help center
                      article
                  tasks.result.items.fetch_time:
                    type: string
                    description: >-
                      date and time when our crawler visited the page in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24
                      13:20:59 +00:00
                  tasks.result.items.country:
                    type: string
                    description: >-
                      country code of the domain registration to obtain a full
                      list of available countries, refer to the Locations
                      endpoint
                  tasks.result.items.language:
                    type: string
                    description: >-
                      main language of the domain to obtain a full list of
                      available languages, refer to the Languages endpoint
                  tasks.result.items.score:
                    type: string
                    description: >-
                      citation prominence score this value is based on url_rank,
                      domain_rank, keyword presence in title, main_title, url,
                      snippet the higher the score, the more value the related
                      citation has
                  tasks.result.items.page_category:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains all relevant page categories product and service
                      categories relevant for the page to obtain a full list of
                      available categories, refer to the Categories endpoint
                  tasks.result.items.page_types:
                    type: array
                    items:
                      type: string
                    description: page types
                  tasks.result.items.ratings:
                    type: array
                    items:
                      type: string
                    description: >-
                      ratings found on the page all ratings found on the page
                      based on microdata
                  tasks.result.items.social_metrics:
                    type: array
                    items:
                      type: string
                    description: >-
                      social media engagement metrics data on social media
                      interactions associated with the content based on website
                      embeds developed and supported by social media platforms
                  tasks.result.items.content_info:
                    type: object
                    description: contains data on citations from the given url
                  tasks.result.items.content_info.content_type:
                    type: string
                    description: 'type of content example: page_content, comment'
                  tasks.result.items.content_info.title:
                    type: string
                    description: title of the result
                  tasks.result.items.content_info.main_title:
                    type: string
                    description: page title
                  tasks.result.items.content_info.previous_title:
                    type: string
                    description: title of the previous content block
                  tasks.result.items.content_info.level:
                    type: integer
                    description: >-
                      title heading level indicates h-tag level from 1 (top) to
                      6 (bottom)
                  tasks.result.items.content_info.author:
                    type: string
                    description: author of the content
                  tasks.result.items.content_info.snippet:
                    type: string
                    description: content snippet
                  tasks.result.items.content_info.snippet_length:
                    type: integer
                    description: character length of the snippet
                  tasks.result.items.content_info.social_metrics:
                    type: array
                    items:
                      type: string
                    description: >-
                      social media engagement metrics data on social media
                      interactions associated with the content based on website
                      embeds developed and supported by social media platforms
                  tasks.result.items.content_info.highlighted_text:
                    type: string
                    description: highlighted text from the snippet
                  tasks.result.items.content_info.language:
                    type: string
                    description: >-
                      content language to obtain a full list of available
                      languages, refer to the Languages endpoint
                  tasks.result.items.content_info.sentiment_connotations:
                    type: object
                    description: >-
                      sentiment connotations contains sentiments (emotional
                      reactions) related to the given citation and probability
                      index per each sentiment possible sentiment connotations:
                      anger, happiness, love, sadness, share, fun
                  tasks.result.items.content_info.connotation_types:
                    type: object
                    description: >-
                      connotation types contains types of sentiments (sentiment
                      polarity) related to the given citation and probability
                      index per each sentiment type possible sentiment
                      connotation types: positive, negative, neutral
                  tasks.result.items.content_info.text_category:
                    type: array
                    items:
                      type: string
                    description: >-
                      text category to obtain a full list of available
                      categories, refer to the Categories endpoint
                  tasks.result.items.content_info.date_published:
                    type: string
                    description: >-
                      date and time when the content was published in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24
                      13:20:59 +00:00
                  tasks.result.items.content_info.content_quality_score:
                    type: integer
                    description: >-
                      content quality score this value is calculated based on
                      the number of words, sentences and characters the content
                      contains
                  tasks.result.items.content_info.semantic_location:
                    type: string
                    description: >-
                      semantic location indicates semantic element in HTML where
                      the target keyword citation is located example: article,
                      header
                  tasks.result.items.content_info.rating:
                    type: object
                    description: content rating rating related to content_info
                  tasks.result.items.content_info.rating.name:
                    type: string
                    description: >-
                      rating name here you can find the following elements:
                      Max5, Percents, CustomMax
                  tasks.result.items.content_info.rating.rating_value:
                    type: integer
                    description: the value of the rating
                  tasks.result.items.content_info.rating.max_rating_value:
                    type: integer
                    description: maximum value for the rating name
                  tasks.result.items.content_info.rating.rating_count:
                    type: integer
                    description: number of votes
                  tasks.result.items.content_info.rating.relative_rating:
                    type: number
                    description: relative rating
                  tasks.result.items.content_info.group_date:
                    type: string
                    description: >-
                      citation group date and time indicates content publication
                      date or date and time when our crawler visited the page
                      for the first time; this field can be used to group
                      citations by date and display citation trends; date and
                      time are provided in the UTC format: “yyyy-mm-dd hh-mm-ss
                      +00:00” example: 2017-01-24 13:20:59 +00:00
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