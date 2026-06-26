> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Aggregation Technologies

> The Aggregation Technologies endpoint will provide you with a list of the most popular technologies websites use alongside the technologies you specify.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/domain_analytics/technologies/aggregation_technologies/live
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
  /dataforseo/domain_analytics/technologies/aggregation_technologies/live:
    post:
      summary: Aggregation Technologies
      description: >-
        The Aggregation Technologies endpoint will provide you with a list of
        the most popular technologies websites use alongside the technologies
        you specify. Alternatively, you can specify technology categories or
        groups to obtain wider stats.
      operationId: >-
        post_dataforseo_domain_analytics_technologies_aggregation_technologies_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                group:
                  type: string
                  description: >-
                    id of the target technology group required field if you
                    don’t specify technology, category or keyword at least one
                    field (group, category, keyword, technology) must be set you
                    can find the full list of technology group ids on this page
                    example: "marketing"
                category:
                  type: string
                  description: >-
                    id of the target technology category required field if you
                    don’t specify group, keyword or technology at least one
                    field (group, category, keyword, technology) must be set you
                    can find the full list of technology category ids on this
                    page example: "crm"
                technology:
                  type: string
                  description: >-
                    target technology required field if you don’t specify group,
                    keyword or category at least one field (group, category,
                    keyword, technology) must be set you can find the full list
                    of technologies on this page example: "Salesforce"
                keyword:
                  type: string
                  description: >-
                    target keyword in the domain’s meta keywords required field
                    if you don’t specify group, category or technology at least
                    one field (group, category, keyword, technology) must be set
                    UTF-8 encoding example: "seo"learn more about rules and
                    limitations of keyword and keywords fields in DataForSEO
                    APIs in this Help Center article
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
                    content_language_code Note: all filtering parameters are
                    taken from the domain_technology_item of the
                    domain_technologies endpoint; example:
                    [["country_iso_code","=","US"], "and",
                    ["domain_rank",">",800]]for more information about filters,
                    please refer to Domain Analytics Technologies API – Filters
                order_by:
                  type: array
                  items:
                    type: string
                  description: >-
                    results sorting rules optional field you can use the
                    following values to sort the results: groups_count,
                    categories_count, technologies_count possible sorting types:
                    asc – results will be sorted in the ascending order desc –
                    results will be sorted in the descending order you should
                    use a comma to set up a sorting type example:
                    ["groups_count,desc"] note that you can set no more than
                    three sorting rules in a single request you should use a
                    comma to separate several sorting rules example:
                    ["groups_count,desc","technologies_count,desc"] default
                    value:
                    ["groups_count,desc","categories_count,desc","technologies_count,desc"]
                internal_groups_list_limit:
                  type: integer
                  description: >-
                    maximum number of returned technology groups optional field
                    you can use this field to limit the number of items with
                    identical "group" in the results default value: 5 minimum
                    value: 1 maximum value: 10000
                internal_categories_list_limit:
                  type: integer
                  description: >-
                    maximum number of returned technology categories within the
                    same group optional field you can use this field to limit
                    the number of items with identical "category" in the results
                    default value: 5 minimum value: 1 maximum value: 10000
                internal_technologies_list_limit:
                  type: integer
                  description: >-
                    maximum number of returned technologies within the same
                    category optional field you can use this field to limit the
                    number of items with identical "technology" in the results
                    default value: 10 minimum value: 1 maximum value: 10000
                internal_list_limit:
                  type: integer
                  description: >-
                    maximum number of items with identical "category", "group",
                    and "technology" optional field if you use this field, the
                    values specified in internal_groups_list_limit,
                    internal_categories_list_limit and
                    internal_technologies_list_limit will be ignored; you can
                    use this field to limit the number of items with identical
                    "category", "group", or "technology" default value: 10
                    minimum value: 1 maximum value: 10000
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned technologies optional field
                    default value: 100 maximum value: 10000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned domains optional
                    field default value: 0 maximum value: 9999 if you specify
                    the 10 value, the first ten technologies in the results
                    array will be omitted and the data will be provided for the
                    successive technologies
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - group
                - category
                - technology
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
                  tasks.result.total_count:
                    type: integer
                    description: >-
                      total amount of results in our database relevant to your
                      request
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.:
                    type: string
                    description: type of element = ‘aggregation_technologies_item’
                  tasks.result.group:
                    type: string
                    description: technology group id
                  tasks.result.category:
                    type: string
                    description: technology category id
                  tasks.result.technology:
                    type: string
                    description: technology name
                  tasks.result.groups_count:
                    type: integer
                    description: >-
                      technology groups count number of domains that match the
                      parameters you specified and are using technologies from
                      the indicated group
                  tasks.result.categories_count:
                    type: integer
                    description: >-
                      technology categories count number of domains that match
                      the parameters you specified and are using technologies
                      from the indicated category
                  tasks.result.technologies_count:
                    type: integer
                    description: >-
                      technologies count number of domains that match the
                      parameters you specified and are using the indicated
                      technology
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