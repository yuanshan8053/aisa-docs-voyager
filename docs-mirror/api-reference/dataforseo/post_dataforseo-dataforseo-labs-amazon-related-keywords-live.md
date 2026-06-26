> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Related Keywords

> The Related Keywords endpoint provides keywords appearing in the [ 'Related Searches' section on Amazon.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/dataforseo_labs/amazon/related_keywords/live
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
  /dataforseo/dataforseo_labs/amazon/related_keywords/live:
    post:
      summary: Related Keywords
      description: >-
        The Related Keywords endpoint provides keywords appearing in the [
        "Related Searches" section on
        Amazon.![](https://dataforseo.com/wp-content/uploads/2022/02/Screenshot_10.jpg)](#)
      operationId: post_dataforseo_dataforseo_labs_amazon_related_keywords_live
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
                    keyword required field UTF-8 encoding the keywords should be
                    specified in the lowercase format learn more about rules and
                    limitations of keyword and keywords fields in DataForSEO
                    APIs in this Help Center article
                location_name:
                  type: string
                  description: >-
                    full name of the location required field if you don’t
                    specify location_code Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_name by making a
                    separate request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;
                    Note: this endpoint currently supports the US, Egypt, Saudi
                    Arabia, and the United Arab Emirates locations only;
                    example: United States
                location_code:
                  type: integer
                  description: >-
                    location code required field if you don’t specify
                    location_name Note: it is required to specify either
                    location_name or location_code you can receive the list of
                    available locations with their location_code by making a
                    separate request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;
                    Note: this endpoint currently supports the US, Egypt, Saudi
                    Arabia, and the United Arab Emirates locations only;
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of the language required field if you don’t
                    specify language_code Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available locations with their language_name by making a
                    separate request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    language code required field if you don’t specify
                    language_name Note: it is required to specify either
                    language_name or language_code you can receive the list of
                    available locations with their language_code by making a
                    separate request to
                    https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages
                    example: en
                depth:
                  type: integer
                  description: >-
                    keyword search depth optional field default value: 1; number
                    of the returned results depends on the value you set in this
                    field; you can specify a level from 0 to 4; estimated number
                    of keywords for each level (maximum): 0 – the keyword set in
                    the keyword field 1 – 6 keywords 2 – 42 keywords 3 – 258
                    keywords 4 – 1554 keywords
                include_seed_keyword:
                  type: boolean
                  description: >-
                    include data for the seed keyword optional field if set to
                    true, data for the seed keyword specified in the keyword
                    field will be provided in the seed_keyword_data array of the
                    response default value: false
                ignore_synonyms:
                  type: boolean
                  description: >-
                    ignore highly similar keywords optional field if set to true
                    only core keywords will be returned, all highly similar
                    keywords will be excluded; default value: false
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned keywords optional field
                    default value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned keywords optional
                    field default value: 0 if you specify the 10 value, the
                    first ten keywords in the results array will be omitted and
                    the data will be provided for the successive keywords
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - keyword
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
                  tasks.result.seed_keyword:
                    type: string
                    description: keyword in a POST array
                  tasks.result.seed_keyword_data:
                    type: object
                    description: >-
                      keyword data for the seed keyword fields in the object are
                      identical to that of keyword_data
                  tasks.result.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.language_code:
                    type: string
                    description: language code in a POST array
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
                    description: contains objects with keywords and related data
                  tasks.result.items.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword_data:
                    type: object
                    description: keyword data for the returned keyword
                  tasks.result.items.keyword_data.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword_data.keyword:
                    type: string
                    description: related keyword
                  tasks.result.items.keyword_data.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.items.keyword_data.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.items.keyword_data.keyword_info:
                    type: object
                    description: keyword info for the returned keyword
                  tasks.result.items.keyword_data.keyword_info.se_type:
                    type: string
                    description: search engine type
                  tasks.result.items.keyword_data.keyword_info.last_updated_time:
                    type: string
                    description: >-
                      date and time when keyword data was updated in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.keyword_data.keyword_info.search_volume:
                    type: integer
                    description: >-
                      average monthly search volume rate represents the
                      (approximate) number of searches for the provided keyword
                      idea on Amazon
                  tasks.result.items.depth:
                    type: integer
                    description: keyword search depth
                  tasks.result.items.related_keywords:
                    type: array
                    items:
                      type: string
                    description: >-
                      list of related keywords represents the list of search
                      queries which are related to the keyword returned in the
                      array above
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