> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Gemini LLM Scraper Advanced

> Live Gemini LLM Scraper endpoint provides structured results from Gemini.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/ai_optimization/gemini/llm_scraper/live/advanced
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
  /dataforseo/ai_optimization/gemini/llm_scraper/live/advanced:
    post:
      summary: Live Gemini LLM Scraper Advanced
      description: >-
        Live Gemini LLM Scraper endpoint provides structured results from
        Gemini. The results are specific to the selected location (see [the List
        of
        Locations](https://docs.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/locations.md)),
        language (see [the List of
        Languages](https://docs.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/languages.md)),
        and keyword.
      operationId: post_dataforseo_ai_optimization_gemini_llm_scraper_live_advanced
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
                    keyword required field you can specify up to 2000 characters
                    in the keyword field all %## will be decoded (plus character
                    ‘+’ will be decoded to a space character) if you need to use
                    the “%” character for your keyword, please specify it as
                    “%25”; if you need to use the “+” character for your
                    keyword, please specify it as “%2B”learn more about rules
                    and limitations of keyword and keywords fields in DataForSEO
                    APIs in this Help Center article
                location_name:
                  type: string
                  description: >-
                    full name of search engine location required field if you
                    don't specify location_code if you use this field, you don't
                    need to specify location_code you can receive the list of
                    available locations of the search engine with their
                    location_name by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/locations
                    example: United States
                location_code:
                  type: integer
                  description: >-
                    search engine location code required field if you don't
                    specify location_name if you use this field, you don't need
                    to specify location_name you can receive the list of
                    available locations of the search engines with their
                    location_code by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/locations
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of search engine language required field if you
                    don't specify language_code; if you use this field, you
                    don't need to specify language_code; you can receive the
                    list of available languages of the search engine with their
                    language_name by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    search engine language code required field if you don't
                    specify language_name; if you use this field, you don't need
                    to specify language_name; you can receive the list of
                    available languages of the search engine with their
                    language_code_by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/languages
                    example: enn
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
                  tasks.result.keyword:
                    type: string
                    description: >-
                      keyword received in a POST array the keyword is returned
                      with decoded %## (plus symbol '+' will be decoded to a
                      space character)
                  tasks.result.location_code:
                    type: integer
                    description: location code in a POST array
                  tasks.result.language_code:
                    type: string
                    description: language code in a POST array
                  tasks.result.model:
                    type: string
                    description: indicates the model version
                  tasks.result.datetime:
                    type: string
                    description: >-
                      date and time when the result was received in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.sources:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of sources the sources the model actually cited or
                      relied on in its final answer
                  tasks.result.sources.type:
                    type: string
                    description: type of element='gemini_source'
                  tasks.result.sources.title:
                    type: string
                    description: source title
                  tasks.result.sources.snippet:
                    type: string
                    description: source description
                  tasks.result.sources.domain:
                    type: string
                    description: source domain
                  tasks.result.sources.url:
                    type: string
                    description: source URL
                  tasks.result.sources.thumbnail:
                    type: string
                    description: source thumbnail
                  tasks.result.sources.source_name:
                    type: string
                    description: source name
                  tasks.result.sources.publication_date:
                    type: string
                    description: >-
                      date and time when the result was published in the format:
                      “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”
                      example: 2019-11-15 12:57:46 +00:00
                  tasks.result.sources.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.se_results_count:
                    type: integer
                    description: total number of results
                  tasks.result.item_types:
                    type: array
                    items:
                      type: string
                    description: >-
                      types of search results contains types of search results
                      (items) found in SERP. possible item types: gemini_text,
                      gemini_table, gemini_images
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: elements of Gemini results
                  tasks.result.items.gemini_text:
                    type: object
                    description: element in the response
                  tasks.result.items.gemini_text.type:
                    type: string
                    description: type of element='gemini_text'
                  tasks.result.items.gemini_text.rank_group:
                    type: integer
                    description: >-
                      group rank in SERP position within a group of elements
                      with identical type values positions of elements with
                      different type values are omitted from rank_group
                  tasks.result.items.gemini_text.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in SERP absolute position among all the
                      elements in SERP
                  tasks.result.items.gemini_text.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.gemini_text.original_text:
                    type: string
                    description: unformatted text content of the element
                  tasks.result.items.gemini_text.sources:
                    type: array
                    items:
                      type: string
                    description: array of sources
                  tasks.result.items.gemini_text.sources.type:
                    type: string
                    description: type of element='gemini_source'
                  tasks.result.items.gemini_text.sources.title:
                    type: string
                    description: source title
                  tasks.result.items.gemini_text.sources.snippet:
                    type: string
                    description: source description
                  tasks.result.items.gemini_text.sources.domain:
                    type: string
                    description: source domain in SERP
                  tasks.result.items.gemini_text.sources.url:
                    type: string
                    description: source URL
                  tasks.result.items.gemini_text.sources.thumbnail:
                    type: string
                    description: source thumbnail
                  tasks.result.items.gemini_text.sources.source_name:
                    type: string
                    description: source name
                  tasks.result.items.gemini_text.sources.publication_date:
                    type: string
                    description: >-
                      date and time when the result was published in the format:
                      “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”
                      example: 2019-11-15 12:57:46 +00:00
                  tasks.result.items.gemini_text.sources.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.gemini_table:
                    type: object
                    description: element in the response
                  tasks.result.items.gemini_table.type:
                    type: string
                    description: type of element='gemini_table'
                  tasks.result.items.gemini_table.rank_group:
                    type: integer
                    description: >-
                      group rank in SERP position within a group of elements
                      with identical type values positions of elements with
                      different type values are omitted from rank_group
                  tasks.result.items.gemini_table.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in SERP absolute position among all the
                      elements in SERP
                  tasks.result.items.gemini_table.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.gemini_table.original_text:
                    type: string
                    description: unformatted text content of the element
                  tasks.result.items.gemini_table.table:
                    type: object
                    description: >-
                      table present in the element the header and content of the
                      table present in the element
                  tasks.result.items.gemini_table.table.table_header:
                    type: array
                    items:
                      type: string
                    description: content in the header of the table
                  tasks.result.items.gemini_table.table.table_content:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of contents of the table present in the element each
                      array represents the table row
                  tasks.result.items.gemini_images:
                    type: object
                    description: element in the response
                  tasks.result.items.gemini_images.type:
                    type: string
                    description: type of element='gemini_images'
                  tasks.result.items.gemini_images.rank_group:
                    type: integer
                    description: >-
                      group rank in SERP position within a group of elements
                      with identical type values positions of elements with
                      different type values are omitted from rank_group
                  tasks.result.items.gemini_images.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in SERP absolute position among all the
                      elements in SERP
                  tasks.result.items.gemini_images.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.gemini_images.items:
                    type: array
                    items:
                      type: string
                    description: items present in the element
                  tasks.result.items.gemini_images.items.type:
                    type: string
                    description: type of element = 'gemini_images_element'
                  tasks.result.items.gemini_images.items.url:
                    type: string
                    description: relevant URL
                  tasks.result.items.gemini_images.items.alt:
                    type: string
                    description: alt tag of the image
                  tasks.result.items.gemini_images.items.image_url:
                    type: string
                    description: >-
                      URL of the image the URL leading to the image on the
                      original resource or DataForSEO storage (in case the
                      original source is not available)
                  tasks.result.items.gemini_images.items.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
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