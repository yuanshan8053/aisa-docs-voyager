> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Content Analysis – Phrase Trends API

> This endpoint will provide you with data on all citations of the target keyword for the indicated date range.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/content_analysis/phrase_trends/live
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
  /dataforseo/content_analysis/phrase_trends/live:
    post:
      summary: Content Analysis – Phrase Trends API
      description: >-
        This endpoint will provide you with data on all citations of the target
        keyword for the indicated date range.
      operationId: post_dataforseo_content_analysis_phrase_trends_live
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
                    types: as_is – returns data on all citations for the target
                    keyword one_per_domain – returns data on one citation of the
                    keyword per domain default value: as_is
                internal_list_limit:
                  type: integer
                  description: >-
                    maximum number of elements within internal arrays optional
                    field you can use this field to limit the number of elements
                    within the following arrays: top_domains text_categories
                    page_categories countries languages default value: 1 maximum
                    value: 20
                date_from:
                  type: string
                  description: >-
                    starting date of the time range required field date format:
                    "yyyy-mm-dd" example: "2019-01-15"
                date_to:
                  type: string
                  description: >-
                    ending date of the time range optional field if you don’t
                    specify this field, today’s date will be used by default
                    date format: "yyyy-mm-dd" example: "2019-01-15"
                date_group:
                  type: string
                  description: >-
                    time range which will be used to group the results optional
                    field default value: month possible values: day, week, month
                initial_dataset_filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    initial dataset filtering parameters optional field initial
                    filtering parameters that apply to fields in the Search
                    endpoint; you can add several filters at once (8 filters
                    maximum); you should set a logical operator and, or between
                    the conditions; the following operators are supported:
                    regex, not_regex, , , >, >=, =, , in, not_in, like,not_like,
                    has, has_not, match, not_match you can use the % operator
                    with like and not_like to match any string of zero or more
                    characters; example: ["domain","", "logitech.com"]
                    [["domain","","logitech.com"],"and",["content_info.connotation_types.negative",">",1000]]
                    [["domain","","logitech.com"]], "and",
                    [["content_info.connotation_types.negative",">",1000], "or",
                    ["content_info.text_category","has",10994]]] for more
                    information about filters, please refer to Content Analysis
                    API – Filters learn more about the initial dataset filters
                    in this help center article.
                rank_scale:
                  type: string
                  description: >-
                    defines the scale used for calculating and displaying the
                    rank values optional field you can use this parameter to
                    choose whether rank values are presented on a 0–100 or
                    0–1000 scale possible values: one_hundred — rank values are
                    displayed on a 0–100 scale one_thousand — rank values are
                    displayed on a 0–1000 scale default value: one_thousand
                    learn more about how this parameter works in this Help
                    Center article
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - keyword
                - date_from
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
                  tasks.result.type:
                    type: string
                    description: type of element = ‘content_analysis_trends’
                  tasks.result.date:
                    type: string
                    description: date for which the data is provided
                  tasks.result.total_count:
                    type: integer
                    description: >-
                      total number of results in our database relevant to your
                      request
                  tasks.result.rank:
                    type: integer
                    description: >-
                      rank of all URLs citing the keyword normalized sum of
                      ranks of all URLs citing the target keyword for the given
                      date
                  tasks.result.top_domains:
                    type: array
                    items:
                      type: string
                    description: >-
                      top domains citing the target keyword contains objects
                      with top domains citing the target keyword and citation
                      count per each domain
                  tasks.result.sentiment_connotations:
                    type: object
                    description: >-
                      sentiment connotations contains sentiments (emotional
                      reactions) related to the target keyword citation and the
                      number of citations per each sentiment possible
                      connotations: "anger", "happiness", "love", "sadness",
                      "share", "fun"
                  tasks.result.connotation_types:
                    type: object
                    description: >-
                      connotation types contains types of sentiments (sentiment
                      polarity) related to the keyword citation and citation
                      count per each sentiment type possible connotation types:
                      "positive", "negative", "neutral"
                  tasks.result.text_categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      text categories contains objects with text categories and
                      citation count in each text category to obtain a full list
                      of available categories, refer to the Categories endpoint
                  tasks.result.page_categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      page categories contains objects with page categories and
                      citation count in each page category to obtain a full list
                      of available categories, refer to the Categories endpoint
                  tasks.result.page_types:
                    type: object
                    description: >-
                      page types contains page types and citation count per each
                      page type
                  tasks.result.countries:
                    type: object
                    description: >-
                      countries contains countries and citation count in each
                      country to obtain a full list of available countries,
                      refer to the Locations endpoint
                  tasks.result.languages:
                    type: object
                    description: >-
                      languages contains languages and citation count in each
                      language to obtain a full list of available languages,
                      refer to the Languages endpoint
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