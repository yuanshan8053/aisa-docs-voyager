> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tavily Search

> Execute a search query using Tavily Search.



## OpenAPI

````yaml openapi/tavily.json POST /tavily/search
openapi: 3.0.0
info:
  title: Tavily API
  version: 1.0.0
  description: >-
    Unified API documentation for Tavily endpoints including Search, Extract,
    Crawl, and Map.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - bearerAuth: []
paths:
  /tavily/search:
    post:
      tags:
        - https://docs.tavily.com/documentation/api-reference/endpoint/search
      summary: Execute a search query using Tavily Search.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                query:
                  type: string
                  description: The search query to execute with Tavily.
                  example: Who is Leo Messi?
                search_depth:
                  type: string
                  enum:
                    - advanced
                    - basic
                    - fast
                    - ultra-fast
                  default: basic
                  description: Controls the latency vs. relevance tradeoff.
                chunks_per_source:
                  type: integer
                  default: 3
                  description: Maximum number of relevant chunks returned per source.
                  minimum: 1
                  maximum: 3
                max_results:
                  type: integer
                  default: 5
                  description: Maximum number of search results to return.
                  minimum: 0
                  maximum: 20
                topic:
                  type: string
                  enum:
                    - general
                    - news
                    - finance
                  default: general
                  description: Category of the search.
                time_range:
                  type: string
                  enum:
                    - day
                    - week
                    - month
                    - year
                    - d
                    - w
                    - m
                    - 'y'
                  description: Time range to filter results based on publish date.
                start_date:
                  type: string
                  format: date
                  description: Return results after the specified start date.
                  example: '2025-02-09'
                end_date:
                  type: string
                  format: date
                  description: Return results before the specified end date.
                  example: '2025-12-29'
                include_answer:
                  type: boolean
                  default: false
                  description: Include an LLM-generated answer to the query.
                include_raw_content:
                  type: boolean
                  default: false
                  description: >-
                    Include cleaned and parsed HTML content of each search
                    result.
                include_images:
                  type: boolean
                  default: false
                  description: Perform an image search and include results.
                include_image_descriptions:
                  type: boolean
                  default: false
                  description: >-
                    Add descriptive text for each image when include_images is
                    true.
                include_favicon:
                  type: boolean
                  default: false
                  description: Include the favicon URL for each result.
                include_domains:
                  type: array
                  items:
                    type: string
                  description: >-
                    List of domains to specifically include in the search
                    results.
                  maxItems: 300
                exclude_domains:
                  type: array
                  items:
                    type: string
                  description: >-
                    List of domains to specifically exclude from the search
                    results.
                  maxItems: 150
                country:
                  type: string
                  description: Boost search results from a specific country.
                  enum:
                    - afghanistan
                    - albania
                    - algeria
                    - andorra
                    - angola
                    - argentina
                    - armenia
                    - australia
                    - austria
                    - azerbaijan
                    - bahamas
                    - bahrain
                    - bangladesh
                    - barbados
                    - belarus
                    - belgium
                    - belize
                    - benin
                    - bhutan
                    - bolivia
                    - bosnia and herzegovina
                    - botswana
                    - brazil
                    - brunei
                    - bulgaria
                    - burkina faso
                    - burundi
                    - cambodia
                    - cameroon
                    - canada
                    - cape verde
                    - central african republic
                    - chad
                    - chile
                    - china
                    - colombia
                    - comoros
                    - congo
                    - costa rica
                    - croatia
                    - cuba
                    - cyprus
                    - czech republic
                    - denmark
                    - djibouti
                    - dominican republic
                    - ecuador
                    - egypt
                    - el salvador
                    - equatorial guinea
                    - eritrea
                    - estonia
                    - ethiopia
                    - fiji
                    - finland
                    - france
                    - gabon
                    - gambia
                    - georgia
                    - germany
                    - ghana
                    - greece
                    - guatemala
                    - guinea
                    - haiti
                    - honduras
                    - hungary
                    - iceland
                    - india
                    - indonesia
                    - iran
                    - iraq
                    - ireland
                    - israel
                    - italy
                    - jamaica
                    - japan
                    - jordan
                    - kazakhstan
                    - kenya
                    - kuwait
                    - kyrgyzstan
                    - latvia
                    - lebanon
                    - lesotho
                    - liberia
                    - libya
                    - liechtenstein
                    - lithuania
                    - luxembourg
                    - madagascar
                    - malawi
                    - malaysia
                    - maldives
                    - mali
                    - malta
                    - mauritania
                    - mauritius
                    - mexico
                    - moldova
                    - monaco
                    - mongolia
                    - montenegro
                    - morocco
                    - mozambique
                    - myanmar
                    - namibia
                    - nepal
                    - netherlands
                    - new zealand
                    - nicaragua
                    - niger
                    - nigeria
                    - north korea
                    - north macedonia
                    - norway
                    - oman
                    - pakistan
                    - panama
                    - papua new guinea
                    - paraguay
                    - peru
                    - philippines
                    - poland
                    - portugal
                    - qatar
                    - romania
                    - russia
                    - rwanda
                    - saudi arabia
                    - senegal
                    - serbia
                    - singapore
                    - slovakia
                    - slovenia
                    - somalia
                    - south africa
                    - south korea
                    - south sudan
                    - spain
                    - sri lanka
                    - sudan
                    - sweden
                    - switzerland
                    - syria
                    - taiwan
                    - tajikistan
                    - tanzania
                    - thailand
                    - togo
                    - trinidad and tobago
                    - tunisia
                    - turkey
                    - turkmenistan
                    - uganda
                    - ukraine
                    - united arab emirates
                    - united kingdom
                    - united states
                    - uruguay
                    - uzbekistan
                    - venezuela
                    - vietnam
                    - yemen
                    - zambia
                    - zimbabwe
                auto_parameters:
                  type: boolean
                  default: false
                  description: >-
                    Automatically configure search parameters based on query
                    content.
                include_usage:
                  type: boolean
                  default: false
                  description: Include credit usage information in the response.
              required:
                - query
      responses:
        '200':
          description: Search results returned successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  query:
                    type: string
                    description: The search query that was executed.
                  answer:
                    type: string
                    description: A short answer to the user's query, generated by an LLM.
                  images:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                          description: Image URL.
                        description:
                          type: string
                          description: Image description.
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        title:
                          type: string
                          description: Title of the search result.
                        url:
                          type: string
                          description: URL of the search result.
                        content:
                          type: string
                          description: Content snippet of the search result.
                        score:
                          type: number
                          format: float
                          description: Relevance score of the search result.
                        favicon:
                          type: string
                          description: Favicon URL of the search result.
                  response_time:
                    type: number
                    format: float
                    description: Time in seconds it took to complete the request.
                  usage:
                    type: object
                    properties:
                      credits:
                        type: integer
                        description: Credit usage details for the request.
                  request_id:
                    type: string
                    description: Unique request identifier.
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````