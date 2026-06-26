> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Content Analysis – Sentiment Analysis API

> This endpoint will provide you with sentiment analysis data for the citations available for the target keyword.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/content_analysis/sentiment_analysis/live
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
  /dataforseo/content_analysis/sentiment_analysis/live:
    post:
      summary: Content Analysis – Sentiment Analysis API
      description: >-
        This endpoint will provide you with sentiment analysis data for the
        citations available for the target keyword.
      operationId: post_dataforseo_content_analysis_sentiment_analysis_live
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
                internal_list_limit:
                  type: integer
                  description: >-
                    maximum number of elements within internal arrays optional
                    field you can use this field to limit the number of elements
                    within the following arrays: top_domains text_categories
                    page_categories countries languages default value: 1 maximum
                    value: 20
                positive_connotation_threshold:
                  type: number
                  description: >-
                    positive connotation threshold optional field specified as
                    the probability index threshold for positive sentiment
                    related to the citation content if you specify this field,
                    connotation_types object in the response will only contain
                    data on citations with positive sentiment probability more
                    than or equal to the specified value possible values: from 0
                    to 1 default value: 0.4
                sentiments_connotation_threshold:
                  type: number
                  description: >-
                    sentiment connotation threshold optional field specified as
                    the probability index threshold for sentiment connotations
                    related to the citation content if you specify this field,
                    sentiment_connotations object in the response will only
                    contain data on citations where the probability per each
                    sentiment is more than or equal to the specified value
                    possible values: from 0 to 1 default value: 0.4
                initial_dataset_filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    initial dataset filtering parameters optional field initial
                    filtering parameters that apply to fields in the Search
                    endpoint you can add several filters at once (8 filters
                    maximum) you should set a logical operator and, or between
                    the conditions the following operators are supported: regex,
                    not_regex, , , >, >=, =, , in, not_in, like,not_like, has,
                    has_not, match, not_match you can use the % operator with
                    like and not_like to match any string of zero or more
                    characters example: ["domain","", "logitech.com"]
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
                    description: type of element = ‘content_analysis_sentiment_analysis’
                  tasks.result.positive_connotation_distribution:
                    type: object
                    description: >-
                      citation distribution by sentiment connotation types
                      contains objects with citation counts and relevant data
                      distributed by types of sentiments (sentiment polarity);
                      possible sentiment connotation types: positive, negative,
                      neutral
                  tasks.result.positive_connotation_distribution.$positive:
                    type: object
                    description: >-
                      positive, negative, or neutral connotations variable can
                      take the following values: positive, negative, neutral
                  tasks.result.positive_connotation_distribution.$positive.type:
                    type: string
                    description: type of element = ‘content_analysis_summary’
                  tasks.result.positive_connotation_distribution.$positive.total_count:
                    type: integer
                    description: total number of relevant results
                  tasks.result.positive_connotation_distribution.$positive.rank:
                    type: integer
                    description: rank of all relevant URLs
                  tasks.result.positive_connotation_distribution.$positive.top_domains:
                    type: array
                    items:
                      type: string
                    description: >-
                      top relevant domains contains objects with top relevant
                      domains and the number of citations per each domain
                  tasks.result.positive_connotation_distribution.$positive.sentiment_connotations:
                    type: object
                    description: >-
                      sentiment connotations contains relevant sentiments
                      (emotional reactions) and the number of citations per each
                      sentiment; possible connotations: "anger", "happiness",
                      "love", "sadness", "share", "fun"
                  tasks.result.positive_connotation_distribution.$positive.connotation_types:
                    type: object
                    description: >-
                      connotation types contains types of sentiments (sentiment
                      polarity) related to the keyword citation and citation
                      count per each sentiment type; possible connotation types:
                      "positive", "negative", "neutral"
                  tasks.result.positive_connotation_distribution.$positive.text_categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      text categories contains text categories and citation
                      count in each text category to obtain a full list of
                      available categories, refer to the Categories endpoint
                  tasks.result.positive_connotation_distribution.$positive.page_categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      page categories contains objects with page categories and
                      citation count in each page category to obtain a full list
                      of available categories, refer to the Categories endpoint
                  tasks.result.positive_connotation_distribution.$positive.page_types:
                    type: object
                    description: >-
                      page types contains page types and citation count per each
                      page type
                  tasks.result.positive_connotation_distribution.$positive.countries:
                    type: object
                    description: >-
                      countries contains countries and citation count in each
                      country to obtain a full list of available countries,
                      refer to the Locations endpoint
                  tasks.result.positive_connotation_distribution.$positive.languages:
                    type: object
                    description: >-
                      languages to obtain a full list of available languages,
                      refer to the Languages endpoint
                  tasks.result.sentiment_connotation_distribution:
                    type: object
                    description: >-
                      citation distribution by sentiment connotations contains
                      objects with citation counts and relevant data distributed
                      by sentiments (emotional reactions); possible sentiment
                      connotation types: anger, happiness, love, sadness, share,
                      fun
                  tasks.result.sentiment_connotation_distribution.$anger:
                    type: object
                    description: >-
                      sentiment name variable can take the following values:
                      anger, happiness, love, sadness, share, fun
                  tasks.result.sentiment_connotation_distribution.$anger.type:
                    type: string
                    description: type of element = ‘content_analysis_summary’
                  tasks.result.sentiment_connotation_distribution.$anger.total_count:
                    type: integer
                    description: total number of relevant results
                  tasks.result.sentiment_connotation_distribution.$anger.rank:
                    type: integer
                    description: rank of all relevant URLs
                  tasks.result.sentiment_connotation_distribution.$anger.top_domains:
                    type: array
                    items:
                      type: string
                    description: >-
                      top relevant domains contains objects with top relevant
                      domains and the number of citations per each domain
                  tasks.result.sentiment_connotation_distribution.$anger.sentiment_connotations:
                    type: object
                    description: >-
                      sentiment connotations contains relevant sentiments
                      (emotional reactions) and the number of citations per each
                      sentiment; possible connotations: "anger", "happiness",
                      "love", "sadness", "share", "fun"
                  tasks.result.sentiment_connotation_distribution.$anger.connotation_types:
                    type: object
                    description: >-
                      connotation types contains types of sentiments (sentiment
                      polarity) related to the keyword citation and citation
                      count per each sentiment type; possible connotation types:
                      "positive", "negative", "neutral"
                  tasks.result.sentiment_connotation_distribution.$anger.text_categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      text categories contains text categories and citation
                      count in each text category to obtain a full list of
                      available categories, refer to the Categories endpoint
                  tasks.result.sentiment_connotation_distribution.$anger.page_categories:
                    type: array
                    items:
                      type: string
                    description: >-
                      page categories contains objects with page categories and
                      citation count in each page category to obtain a full list
                      of available categories, refer to the Categories endpoint
                  tasks.result.sentiment_connotation_distribution.$anger.page_types:
                    type: object
                    description: >-
                      page types contains page types and citation count per each
                      page type
                  tasks.result.sentiment_connotation_distribution.$anger.countries:
                    type: object
                    description: >-
                      countries contains countries and citation count in each
                      country to obtain a full list of available countries,
                      refer to the Locations endpoint
                  tasks.result.sentiment_connotation_distribution.$anger.languages:
                    type: object
                    description: >-
                      languages to obtain a full list of available countries,
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