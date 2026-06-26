> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Technologies Summary

> The Technologies Summary endpoint will provide you with the number of domains across different countries and languages that use the specified technology name...



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/domain_analytics/technologies/technologies_summary/live
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
  /dataforseo/domain_analytics/technologies/technologies_summary/live:
    post:
      summary: Technologies Summary
      description: >-
        The Technologies Summary endpoint will provide you with the number of
        domains across different countries and languages that use the specified
        technology names, technology groups, or technology categories.
      operationId: post_dataforseo_domain_analytics_technologies_technologies_summary_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                technology_paths:
                  type: array
                  items:
                    type: string
                  description: >-
                    target technology paths required field if you don’t specify
                    groups, technologies and categories each technology path
                    should be specified as a separate object containing “path”
                    and “name”, where “path” is specified as
                    “$group_id.$category_id” and “name” – as the name of the
                    target technology; each object with a technology path should
                    be separated with a comma you can find the full list of
                    technology group ids, category ids and technology names on
                    this page note: you can specify up to 10 technology paths in
                    this array example: [{"path": "content.cms","name":
                    "wordpress"}, {"path": "marketing.crm","name":
                    "salesforce"}]
                groups:
                  type: array
                  items:
                    type: string
                  description: >-
                    ids of the target technology groups required field if you
                    don’t specify technologies, technology_paths, categories, or
                    keywords you can find the full list of technology group ids
                    on this page note: you can specify up to 10 technology
                    groups in this array example: ["sales", "marketing"]
                categories:
                  type: array
                  items:
                    type: string
                  description: >-
                    ids of the target technology categories required field if
                    you don’t specify groups, technology_paths, technologies, or
                    keywords you can find the full list of technology category
                    ids on this page note: you can specify up to 10 technology
                    categories in this array example:
                    ["payment_processors","crm"]
                technologies:
                  type: array
                  items:
                    type: string
                  description: >-
                    target technologies required field if you don’t specify
                    groups, technology_paths, categories, or keywords you can
                    find the full list of technologies you can specify here on
                    this page note: you can specify up to 10 technologies in
                    this array example: ["Google Pay","Salesforce"]
                keywords:
                  type: array
                  items:
                    type: string
                  description: >-
                    target keywords in the domain’s title, description or meta
                    keywords required field if you don’t specify groups,
                    technology_paths, categories, or technologies you can
                    specify the maximum of 10 keywords; UTF-8 encoding; example:
                    ["seo","software"] learn more about rules and limitations of
                    keyword and keywords fields in DataForSEO APIs in this Help
                    Center article
                mode:
                  type: string
                  description: >-
                    search mode optional field possible search mode types: as_is
                    – search for results exactly matching the specified group
                    ids, category ids, or technology names entry – search for
                    results matching a part of the specified group ids, category
                    ids, or technology names default value: as_is
                filters:
                  type: array
                  items:
                    type: string
                  description: >-
                    array of results filtering parameters optional field you can
                    add several filters at once (8 filters maximum) you should
                    set a logical operator and, or between the conditions the
                    following operators are supported: , , >, >=, =, , in,
                    not_in, like,not_like you can use the % operator with like
                    and not_like to match any string of zero or more characters
                    you can use the following parameters to filter the results:
                    domain_rank, last_visited, country_iso_code, language_code,
                    content_language_code example:
                    [["country_iso_code","=","US"], "and",
                    ["domain_rank",">",800]] for more information about filters,
                    please refer to Domain Analytics Technologies API – Filters
                internal_list_limit:
                  type: integer
                  description: >-
                    maximum number of elements within internal arrays optional
                    field you can use this field to limit the number of elements
                    within the following arrays: countries, languages,
                    content_languages, keywords default value: 10 minimum value:
                    1 maximum value: 10000
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - technology_paths
                - groups
                - categories
                - technologies
                - keywords
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
                  tasks.result.countries:
                    type: object
                    description: >-
                      distribution of websites by country contains country codes
                      and number of websites per country
                  tasks.result.languages:
                    type: object
                    description: >-
                      distribution of websites by language contains language
                      codes and number of websites per language
                  tasks.result.content_languages:
                    type: object
                    description: >-
                      distribution of websites by content language contains
                      content language codes and number of websites per language
                  tasks.result.keywords:
                    type: object
                    description: >-
                      distribution of websites by keywords contains keywords
                      found in the websites’ titles, descriptions or meta
                      keywords, and number of websites using each keyword
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