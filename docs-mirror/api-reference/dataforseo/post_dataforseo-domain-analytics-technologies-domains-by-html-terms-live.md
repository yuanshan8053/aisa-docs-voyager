> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Domains by HTML Terms

> This endpoint provides domains based on the HTML terms they use on their homepage.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/domain_analytics/technologies/domains_by_html_terms/live
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
  /dataforseo/domain_analytics/technologies/domains_by_html_terms/live:
    post:
      summary: Domains by HTML Terms
      description: >-
        This endpoint provides domains based on the HTML terms they use on their
        homepage. In addition to the list of domains, you will also get their
        technology profiles, the country and language they belong to, and other
        related data.
      operationId: post_dataforseo_domain_analytics_technologies_domains_by_html_terms_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                search_terms:
                  type: array
                  items:
                    type: string
                  description: >-
                    target search terms required field specify target HTML
                    elements, tags, attributes, their content or all of the
                    above if you specify more than one search term, you will
                    receive only the domains containing all of the specified
                    terms in the HTML code of their homepage maximum number of
                    search terms you can specify: 10 example: ["data-attrid"]
                keywords:
                  type: array
                  items:
                    type: string
                  description: >-
                    target keywords in the domain’s title, description or meta
                    keywords optional field UTF-8 encoding maximum number of
                    keywords you can specify: 10 example: ["seo","software"]
                    learn more about rules and limitations of keyword and
                    keywords fields in DataForSEO APIs in this Help Center
                    article
                mode:
                  type: string
                  description: >-
                    search mode optional field possible search mode types:
                    strict_entry – search for results exactly matching the
                    order, intervals and separators in the specified search
                    terms entry – search for results ignoring the order,
                    intervals and separators in the specified search terms
                    default value: entry
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: , , >, >=, =, , in,
                    not_in, like, not_like you can use the % operator with like
                    and not_like to match any string of zero or more characters
                    example: ["domain","like","%seo%"]
                    [["country_iso_code","=","US"], "and",
                    ["domain_rank",">",100]] [["domain_rank",">",100], "and",
                    [["country_iso_code","=","US"],"or",["country_iso_code","=","CA"]]]
                    for more information about filters, please refer to Domain
                    Analytics Technologies API – Filters
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    results sorting rules optional field available fields:
                    domain_rank, domain, last_visited, country_iso_code,
                    language_code, content_language_code possible sorting types:
                    asc – results will be sorted in the ascending order desc –
                    results will be sorted in the descending order you should
                    use a comma to set up a sorting type example:
                    ["last_visited,desc"] default rule: ["domain_rank,desc"]
                    note that you can set no more than three sorting rules in a
                    single request you should use a comma to separate several
                    sorting rules example:
                    ["last_visited,desc","domain_rank,desc"]
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned domains optional field
                    default value: 100 maximum value: 10000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned domains optional
                    field default value: 0 if you specify the 10 value, the
                    first ten domains in the results array will be omitted and
                    the data will be provided for the successive domains; Note:
                    the maximum value is 9999, the sum of limit and offset must
                    not exceed 10000; use the offset_token if you would like to
                    offset more results
                offset_token:
                  type: string
                  description: >-
                    token for subsequent requests optional field provided in the
                    identical filed of the response to each request; use this
                    parameter to avoid timeouts while trying to obtain over
                    100,000 results in a single request; by specifying the
                    unique offset_token value from the response array, you will
                    get the subsequent results of the initial task; offset_token
                    values are unique for each subsequent task Note: if the
                    offset_token is specified in the request, all other
                    parameters should be identical to the previous request learn
                    more about this parameter on our Help Center
              required:
                - search_terms
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
                    description: total number of relevant items in the database
                  tasks.result.items_count:
                    type: integer
                    description: number of items in the results array
                  tasks.result.offset:
                    type: integer
                    description: specified offset value
                  tasks.result.offset_token:
                    type: string
                    description: >-
                      token for subsequent requests by specifying the unique
                      offset_token when setting a new task, you will get the
                      subsequent results of the initial task; offset_token
                      values are unique for each subsequent task
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: items array
                  tasks.result.type:
                    type: string
                    description: type of the item = ‘domain_technology_item’
                  tasks.result.domain:
                    type: string
                    description: specified domain name
                  tasks.result.title:
                    type: string
                    description: domain meta title
                  tasks.result.description:
                    type: string
                    description: domain meta description
                  tasks.result.meta_keywords:
                    type: array
                    items:
                      type: string
                    description: domain meta keywords
                  tasks.result.domain_rank:
                    type: string
                    description: >-
                      backlink rank of the target domain learn more about the
                      metric and how it is calculated in this help center
                      article
                  tasks.result.last_visited:
                    type: string
                    description: >-
                      most recent date when our crawler visited the domain in
                      the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2022-10-10 12:57:46 +00:00
                  tasks.result.country_iso_code:
                    type: string
                    description: >-
                      domain ISO code ISO code of the country that target domain
                      is determined to belong to
                  tasks.result.language_code:
                    type: string
                    description: >-
                      domain language code of the language that target domain is
                      determined to be associated with
                  tasks.result.content_language_code:
                    type: string
                    description: >-
                      content language code of the language that content on the
                      target domain is written with
                  tasks.result.phone_numbers:
                    type: array
                    items:
                      type: string
                    description: >-
                      phone numbers of the target contact phone numbers
                      indicated on the target website
                  tasks.result.emails:
                    type: array
                    items:
                      type: string
                    description: >-
                      emails of the target emails indicated on the target
                      website
                  tasks.result.social_graph_urls:
                    type: array
                    items:
                      type: string
                    description: >-
                      social media links and handles social media URLs detected
                      in the social graphs of the target website
                  tasks.result.technologies:
                    type: object
                    description: >-
                      technologies used by target domain contains objects with
                      the names of technologies used on the website; to get a
                      full list of technologies and their structure, refer to
                      the technologies endpoint
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