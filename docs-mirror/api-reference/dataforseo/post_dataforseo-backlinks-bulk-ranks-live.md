> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Ranks

> This endpoint will provide you with rank scores of the domains, subdomains, and pages specified in the `targets` array.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/backlinks/bulk_ranks/live
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
  /dataforseo/backlinks/bulk_ranks/live:
    post:
      summary: Bulk Ranks
      description: >-
        This endpoint will provide you with rank scores of the domains,
        subdomains, and pages specified in the `targets` array. The score is
        based on the number of referring domains pointing to the specified
        domains, subdomains, or pages. The `rank` values represent real-time
        data for the date of the request and range from 0 (no backlinks
        detected) to 1,000 (highest rank). A similar scoring system is used in
        Google’s Page Rank algorithm. You can learn more about rank scores in
        [this help center
        article](https://dataforseo.com/help-center/what_is_rank_in_backlinks_api)
      operationId: post_dataforseo_backlinks_bulk_ranks_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                targets:
                  type: array
                  items:
                    type: string
                  description: >-
                    domains, subdomains or webpages to get rank for required
                    field you can set up to 1000 domains, subdomains or webpages
                    the domain or subdomain should be specified without https://
                    and www. the page should be specified with absolute URL
                    (including http:// or https://) example: "targets": [
                    "forbes.com", "cnn.com", "bbc.com", "yelp.com",
                    "https://www.apple.com/iphone/", "https://ahrefs.com/blog/",
                    "ibm.com", "https://variety.com/",
                    "https://stackoverflow.com/", "www.trustpilot.com" ]
                rank_scale:
                  type: string
                  description: >-
                    defines the scale used for calculating and displaying the
                    rank, domain_from_rank, and page_from_rank values optional
                    field you can use this parameter to choose whether rank
                    values are presented on a 0–100 or 0–1000 scale possible
                    values: one_hundred — rank values are displayed on a 0–100
                    scale one_thousand — rank values are displayed on a 0–1000
                    scale default value: one_thousand learn more about how this
                    parameter works and how ranking metrics are calculated in
                    this Help Center article
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - targets
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
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains relevant backlinks and referring domains data
                  tasks.result.items.target:
                    type: string
                    description: domain, subdomain or webpage from a POST array
                  tasks.result.items.rank:
                    type: integer
                    description: >-
                      rank of the target values represent real-time data for the
                      date of the request rank is calculated based on the method
                      for node ranking in a linked database – a principle used
                      in the original Google PageRank algorithm learn more about
                      the metric and how it is calculated in this help center
                      article
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