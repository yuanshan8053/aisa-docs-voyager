> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live ChatGPT LLM Scraper

> Live ChatGPT LLM Scraper endpoint provides results from ChatGPT searches.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/ai_optimization/chat_gpt/llm_scraper/live/advanced
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
  /dataforseo/ai_optimization/chat_gpt/llm_scraper/live/advanced:
    post:
      summary: Live ChatGPT LLM Scraper
      description: >-
        Live ChatGPT LLM Scraper endpoint provides results from ChatGPT
        searches. The results are specific to the selected location (see [the
        List of
        Locations](https://docs.dataforseo.com/v3/ai_optimization/chatgpt/llm_scraper/locations.md))
        and language (see [the List of
        Languages](https://docs.dataforseo.com/v3/ai_optimization/chatgpt/llm_scraper/languages.md))
        parameters.
      operationId: post_dataforseo_ai_optimization_chat_gpt_llm_scraper_live_advanced
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
                    https://api.dataforseo.com/v3/ai_optimization/chat_gpt/llm_scraper/locations
                    example: United States
                location_code:
                  type: integer
                  description: >-
                    search engine location code required field if you don't
                    specify location_name if you use this field, you don't need
                    to specify location_name you can receive the list of
                    available locations of the search engines with their
                    location_code by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/chat_gpt/llm_scraper/locations
                    example: 2840
                language_name:
                  type: string
                  description: >-
                    full name of search engine language required field if you
                    don't specify language_code; if you use this field, you
                    don't need to specify language_code; you can receive the
                    list of available languages of the search engine with their
                    language_name by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/chat_gpt/llm_scraper/languages
                language_code:
                  type: string
                  description: >-
                    search engine language code required field if you don't
                    specify language_name; if you use this field, you don't need
                    to specify language_name; you can receive the list of
                    available languages of the search engine with their
                    language_code by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/chat_gpt/llm_scraper/languages
                force_web_search:
                  type: boolean
                  description: >-
                    force AI agent to use web search optional field when
                    enabled, the AI model is forced to access and cite current
                    web information; default value: false; Note: even if the
                    parameter is set to true, there is no guarantee web sources
                    will be cited in the response
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
                  tasks.result.check_url:
                    type: string
                    description: >-
                      direct URL to search engine results you can use it to make
                      sure that we provided exact results
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
                  tasks.result.search_results:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of search results all web search outputs the model
                      retrieved when looking up information, including
                      duplicates and unused entries
                  tasks.result.search_results.type:
                    type: string
                    description: type of element='chatgpt_search_result'n
                  tasks.result.search_results.url:
                    type: string
                    description: result URL
                  tasks.result.search_results.domain:
                    type: string
                    description: result domain
                  tasks.result.search_results.title:
                    type: string
                    description: result title
                  tasks.result.search_results.description:
                    type: string
                    description: result description
                  tasks.result.search_results.breadcrumb:
                    type: string
                    description: breadcrumb
                  tasks.result.sources:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of sources the sources the model actually cited or
                      relied on in its final answer
                  tasks.result.sources.type:
                    type: string
                    description: type of element='chat_gpt_source'
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
                  tasks.result.fan_out_queries:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of fan-out queries contains related search queries
                      derived from the main query to provide a more
                      comprehensive response
                  tasks.result.brand_entities:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of brand entities contains information on brands
                      mentioned in the response
                  tasks.result.brand_entities.type:
                    type: string
                    description: type of the element = 'chat_gpt_brand_entity'
                  tasks.result.brand_entities.title:
                    type: string
                    description: name of the brand
                  tasks.result.brand_entities.category:
                    type: string
                    description: category of the brand
                  tasks.result.brand_entities.markdown:
                    type: string
                    description: >-
                      brand name in markdown format contains brand name
                      formatted in the markdown markup language
                  tasks.result.brand_entities.urls:
                    type: array
                    items:
                      type: string
                    description: array of URLs and domains relevant to the brand
                  tasks.result.brand_entities.urls.url:
                    type: string
                    description: URL
                  tasks.result.brand_entities.urls.domain:
                    type: string
                    description: domain
                  tasks.result.se_results_count:
                    type: integer
                    description: total number of results
                  tasks.result.item_types:
                    type: array
                    items:
                      type: string
                    description: >-
                      types of search results contains types of search results
                      (items) found in SERP. possible item types: chat_gpt_text,
                      chat_gpt_table, chat_gpt_navigation_list, chat_gpt_images,
                      chat_gpt_local_businesses, chat_gpt_products
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: elements of ChatGPT results
                  tasks.result.items.chat_gpt_text:
                    type: object
                    description: element in the response
                  tasks.result.items.chat_gpt_text.type:
                    type: string
                    description: type of element='chat_gpt_text'
                  tasks.result.items.chat_gpt_text.rank_group:
                    type: integer
                    description: >-
                      group rank in SERP position within a group of elements
                      with identical type values positions of elements with
                      different type values are omitted from rank_group
                  tasks.result.items.chat_gpt_text.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in SERP absolute position among all the
                      elements in SERP
                  tasks.result.items.chat_gpt_text.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.chat_gpt_text.sources:
                    type: array
                    items:
                      type: string
                    description: array of sources
                  tasks.result.items.chat_gpt_text.sources.type:
                    type: string
                    description: type of element='chat_gpt_source'n
                  tasks.result.items.chat_gpt_text.sources.title:
                    type: string
                    description: source title
                  tasks.result.items.chat_gpt_text.sources.snippet:
                    type: string
                    description: source description
                  tasks.result.items.chat_gpt_text.sources.domain:
                    type: string
                    description: source domain in SERP
                  tasks.result.items.chat_gpt_text.sources.url:
                    type: string
                    description: source URL
                  tasks.result.items.chat_gpt_text.sources.thumbnail:
                    type: string
                    description: source thumbnail
                  tasks.result.items.chat_gpt_text.sources.source_name:
                    type: string
                    description: source name
                  tasks.result.items.chat_gpt_text.sources.publication_date:
                    type: string
                    description: >-
                      date and time when the result was published in the format:
                      “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”
                      example: 2019-11-15 12:57:46 +00:00
                  tasks.result.items.chat_gpt_text.sources.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.chat_gpt_text.brand_entities:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of brand entities contains information on brands
                      mentioned in the text
                  tasks.result.items.chat_gpt_text.brand_entities.type:
                    type: string
                    description: type of the element = 'chat_gpt_brand_entity'
                  tasks.result.items.chat_gpt_text.brand_entities.title:
                    type: string
                    description: name of the brand
                  tasks.result.items.chat_gpt_text.brand_entities.category:
                    type: string
                    description: category of the brand
                  tasks.result.items.chat_gpt_text.brand_entities.markdown:
                    type: string
                    description: >-
                      brand name in markdown format contains brand name
                      formatted in the markdown markup language
                  tasks.result.items.chat_gpt_text.brand_entities.urls:
                    type: array
                    items:
                      type: string
                    description: array of URLs and domains relevant to the brand
                  tasks.result.items.chat_gpt_text.brand_entities.urls.url:
                    type: string
                    description: URL
                  tasks.result.items.chat_gpt_text.brand_entities.urls.domain:
                    type: string
                    description: domain
                  tasks.result.items.chat_gpt_table:
                    type: object
                    description: element in the response
                  tasks.result.items.chat_gpt_table.type:
                    type: string
                    description: type of element='chat_gpt_table'
                  tasks.result.items.chat_gpt_table.rank_group:
                    type: integer
                    description: >-
                      group rank in SERP position within a group of elements
                      with identical type values positions of elements with
                      different type values are omitted from rank_group
                  tasks.result.items.chat_gpt_table.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in SERP absolute position among all the
                      elements in SERP
                  tasks.result.items.chat_gpt_table.text:
                    type: string
                    description: text of the element
                  tasks.result.items.chat_gpt_table.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.chat_gpt_table.table:
                    type: object
                    description: >-
                      table present in the element the header and content of the
                      table present in the element
                  tasks.result.items.chat_gpt_table.table.table_header:
                    type: array
                    items:
                      type: string
                    description: content in the header of the table
                  tasks.result.items.chat_gpt_table.table.table_content:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of contents of the table present in the element each
                      array represents the table row
                  tasks.result.items.chat_gpt_table.brand_entities:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of brand entities contains information on brands
                      mentioned in the table
                  tasks.result.items.chat_gpt_table.brand_entities.type:
                    type: string
                    description: type of the element = 'chat_gpt_brand_entity'
                  tasks.result.items.chat_gpt_table.brand_entities.title:
                    type: string
                    description: name of the brand
                  tasks.result.items.chat_gpt_table.brand_entities.category:
                    type: string
                    description: category of the brand
                  tasks.result.items.chat_gpt_table.brand_entities.markdown:
                    type: string
                    description: >-
                      brand name in markdown format contains brand name
                      formatted in the markdown markup language
                  tasks.result.items.chat_gpt_table.brand_entities.urls:
                    type: array
                    items:
                      type: string
                    description: array of URLs and domains relevant to the brand
                  tasks.result.items.chat_gpt_table.brand_entities.urls.url:
                    type: string
                    description: URL
                  tasks.result.items.chat_gpt_table.brand_entities.urls.domain:
                    type: string
                    description: domain
                  tasks.result.items.chat_gpt_navigation_list:
                    type: object
                    description: element in the response
                  tasks.result.items.chat_gpt_navigation_list.type:
                    type: string
                    description: type of element='chat_gpt_navigation_list'
                  tasks.result.items.chat_gpt_navigation_list.rank_group:
                    type: integer
                    description: >-
                      group rank in SERP position within a group of elements
                      with identical type values positions of elements with
                      different type values are omitted from rank_group
                  tasks.result.items.chat_gpt_navigation_list.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in SERP absolute position among all the
                      elements in SERP
                  tasks.result.items.chat_gpt_navigation_list.title:
                    type: string
                    description: title of the element
                  tasks.result.items.chat_gpt_navigation_list.sources:
                    type: array
                    items:
                      type: string
                    description: array of sources
                  tasks.result.items.chat_gpt_navigation_list.sources.type:
                    type: string
                    description: type of element='chat_gpt_source'
                  tasks.result.items.chat_gpt_navigation_list.sources.title:
                    type: string
                    description: source title
                  tasks.result.items.chat_gpt_navigation_list.sources.snippet:
                    type: string
                    description: source description
                  tasks.result.items.chat_gpt_navigation_list.sources.domain:
                    type: string
                    description: source domain in SERP
                  tasks.result.items.chat_gpt_navigation_list.sources.url:
                    type: string
                    description: source URL
                  tasks.result.items.chat_gpt_navigation_list.sources.thumbnail:
                    type: string
                    description: source thumbnail
                  tasks.result.items.chat_gpt_navigation_list.sources.source_name:
                    type: string
                    description: source name
                  tasks.result.items.chat_gpt_navigation_list.sources.publication_date:
                    type: string
                    description: >-
                      date and time when the result was published in the format:
                      “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”
                      example: 2019-11-15 12:57:46 +00:00
                  tasks.result.items.chat_gpt_navigation_list.sources.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.chat_gpt_images:
                    type: object
                    description: element in the response
                  tasks.result.items.chat_gpt_images.type:
                    type: string
                    description: type of element='chat_gpt_images'
                  tasks.result.items.chat_gpt_images.rank_group:
                    type: integer
                    description: >-
                      group rank in SERP position within a group of elements
                      with identical type values positions of elements with
                      different type values are omitted from rank_group
                  tasks.result.items.chat_gpt_images.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in SERP absolute position among all the
                      elements in SERP
                  tasks.result.items.chat_gpt_images.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.chat_gpt_images.items:
                    type: array
                    items:
                      type: string
                    description: items present in the element
                  tasks.result.items.chat_gpt_images.items.type:
                    type: string
                    description: type of element = 'chat_gpt_images_element'
                  tasks.result.items.chat_gpt_images.items.alt:
                    type: string
                    description: alt tag of the image
                  tasks.result.items.chat_gpt_images.items.url:
                    type: string
                    description: relevant URL
                  tasks.result.items.chat_gpt_images.items.image_url:
                    type: string
                    description: >-
                      URL of the image the URL leading to the image on the
                      original resource or DataForSEO storage (in case the
                      original source is not available)
                  tasks.result.items.chat_gpt_images.items.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.chat_gpt_local_businesses:
                    type: object
                    description: element in the response
                  tasks.result.items.chat_gpt_local_businesses.type:
                    type: string
                    description: type of element='chat_gpt_local_businesses'
                  tasks.result.items.chat_gpt_local_businesses.rank_group:
                    type: integer
                    description: >-
                      group rank in SERP position within a group of elements
                      with identical type values positions of elements with
                      different type values are omitted from rank_group
                  tasks.result.items.chat_gpt_local_businesses.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in SERP absolute position among all the
                      elements in SERP
                  tasks.result.items.chat_gpt_local_businesses.markdown:
                    type: string
                    description: >-
                      content of the element in markdown format content of the
                      result formatted in the markdown markup language
                  tasks.result.items.chat_gpt_local_businesses.items:
                    type: array
                    items:
                      type: string
                    description: items present in the element
                  tasks.result.items.chat_gpt_local_businesses.items.type:
                    type: string
                    description: type of element = 'chat_gpt_local_businesses_element'
                  tasks.result.items.chat_gpt_local_businesses.items.title:
                    type: string
                    description: title of the local business
                  tasks.result.items.chat_gpt_local_businesses.items.description:
                    type: string
                    description: description of the local business
                  tasks.result.items.chat_gpt_local_businesses.items.address:
                    type: string
                    description: address of the local business
                  tasks.result.items.chat_gpt_local_businesses.items.phone:
                    type: string
                    description: phone of the local business
                  tasks.result.items.chat_gpt_local_businesses.items.reviews_count:
                    type: integer
                    description: total number of reviews submitted for the local business
                  tasks.result.items.chat_gpt_local_businesses.items.url:
                    type: string
                    description: website URL of the local business
                  tasks.result.items.chat_gpt_local_businesses.items.domain:
                    type: string
                    description: domain name of the local business
                  tasks.result.items.chat_gpt_local_businesses.items.rating:
                    type: object
                    description: >-
                      rating of the corresponding local business popularity rate
                      based on reviews and displayed in SERP
                  tasks.result.items.chat_gpt_local_businesses.items.rating.rating_type:
                    type: string
                    description: >-
                      type of rating here you can find the following elements:
                      Max5, Percents, CustomMax
                  tasks.result.items.chat_gpt_local_businesses.items.rating.value:
                    type: number
                    description: the average rating based on all reviews
                  tasks.result.items.chat_gpt_local_businesses.items.rating.votes_count:
                    type: integer
                    description: the number of votes
                  tasks.result.items.chat_gpt_local_businesses.items.rating.rating_max:
                    type: integer
                    description: the maximum value for a rating_type
                  tasks.result.items.chat_gpt_products:
                    type: object
                    description: element in the response
                  tasks.result.items.chat_gpt_products.type:
                    type: string
                    description: type of element='chat_gpt_products'
                  tasks.result.items.chat_gpt_products.rank_group:
                    type: integer
                    description: >-
                      group rank in SERP position within a group of elements
                      with identical type values positions of elements with
                      different type values are omitted from rank_group
                  tasks.result.items.chat_gpt_products.rank_absolute:
                    type: integer
                    description: >-
                      absolute rank in SERP absolute position among all the
                      elements in SERP
                  tasks.result.items.chat_gpt_products.items:
                    type: array
                    items:
                      type: string
                    description: items present in the element
                  tasks.result.items.chat_gpt_products.items.type:
                    type: string
                    description: type of element = 'chat_gpt_products_element'
                  tasks.result.items.chat_gpt_products.items.product_id:
                    type: string
                    description: product id
                  tasks.result.items.chat_gpt_products.items.merchants:
                    type: string
                    description: merchant(s) offering the product
                  tasks.result.items.chat_gpt_products.items.id_to_token_map:
                    type: string
                    description: >-
                      product identifier token Base64-encoded token containing
                      Google Shopping product IDs associated with the product
                  tasks.result.items.chat_gpt_products.items.title:
                    type: string
                    description: title of the product
                  tasks.result.items.chat_gpt_products.items.rating:
                    type: object
                    description: >-
                      rating of the product popularity rate based on reviews and
                      displayed in SERP
                  tasks.result.items.chat_gpt_products.items.rating.rating_type:
                    type: string
                    description: >-
                      type of rating here you can find the following elements:
                      Max5, Percents, CustomMax
                  tasks.result.items.chat_gpt_products.items.rating.value:
                    type: number
                    description: the average rating based on all reviews
                  tasks.result.items.chat_gpt_products.items.rating.votes_count:
                    type: integer
                    description: the number of votes
                  tasks.result.items.chat_gpt_products.items.rating.rating_max:
                    type: integer
                    description: the maximum value for a rating_type
                  tasks.result.items.chat_gpt_products.items.price:
                    type: number
                    description: product price
                  tasks.result.items.chat_gpt_products.items.currency:
                    type: string
                    description: >-
                      currency of the listed price ISO code of the currency
                      applied to the price
                  tasks.result.items.chat_gpt_products.items.tag:
                    type: string
                    description: tag text
                  tasks.result.items.chat_gpt_products.items.url:
                    type: string
                    description: result URL
                  tasks.result.items.chat_gpt_products.items.domain:
                    type: string
                    description: result domain in SERP
                  tasks.result.items.chat_gpt_products.items.images:
                    type: array
                    items:
                      type: string
                    description: >-
                      image URLs of the element contains URLs leading to the
                      images on the original resource or DataForSEO storage (in
                      case the original source is not available)
                  tasks.result.items.chat_gpt_products.items.product_ids:
                    type: array
                    items:
                      type: string
                    description: >-
                      Google Shopping product identifiers array of Google
                      Shopping product IDs associated with the product
                  tasks.result.items.chat_gpt_products.items.product_ids.type:
                    type: string
                    description: type of element = 'chat_gpt_google_shopping_product'
                  tasks.result.items.chat_gpt_products.items.product_ids.ei:
                    type: string
                    description: event identifier internal event identifier used by Google
                  tasks.result.items.chat_gpt_products.items.product_ids.product_id:
                    type: string
                    description: >-
                      product identifier can be used as a data_docid in Google
                      Shopping API endpoints
                  tasks.result.items.chat_gpt_products.items.product_ids.catalog_id:
                    type: string
                    description: >-
                      Google Shopping catalog identifier of the product can be
                      used as a product_id in Google Shopping API endpoints
                  tasks.result.items.chat_gpt_products.items.product_ids.gpcid:
                    type: string
                    description: >-
                      Google product cluster identifier can be used as a gid in
                      Google Shopping API endpoints
                  tasks.result.items.chat_gpt_products.items.product_ids.headline_offer_docid:
                    type: string
                    description: >-
                      document identifier of the main offer in the headline can
                      be used as a data_docid in Google Shopping API endpoints
                  tasks.result.items.chat_gpt_products.items.product_ids.image_docid:
                    type: string
                    description: identifier for the displayed product’s image
                  tasks.result.items.chat_gpt_products.items.product_ids.rds:
                    type: string
                    description: >-
                      resource descriptor string internal Google resource
                      descriptor string that identifies the product within
                      Google's Shopping index
                  tasks.result.items.chat_gpt_products.items.product_ids.query:
                    type: string
                    description: >-
                      search query search query used by ChatGPT to retrieve the
                      product from Google Shopping
                  tasks.result.items.chat_gpt_products.items.product_ids.mid:
                    type: string
                    description: >-
                      merchant identifier identifier of the seller or merchant
                      account in Google Shopping
                  tasks.result.items.chat_gpt_products.items.product_ids.pvt:
                    type: string
                    description: >-
                      product view type internal Google parameter that specifies
                      the product view type used when rendering the product item
                  tasks.result.items.chat_gpt_products.items.product_ids.uule:
                    type: string
                    description: >-
                      encoded location parameter indicates the location for a
                      search
                  tasks.result.items.chat_gpt_products.items.product_ids.gl:
                    type: string
                    description: >-
                      country code indicates the location for which search
                      results are displayed
                  tasks.result.items.chat_gpt_products.items.product_ids.hl:
                    type: string
                    description: >-
                      host language code indicates the language in which search
                      results are displayed
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