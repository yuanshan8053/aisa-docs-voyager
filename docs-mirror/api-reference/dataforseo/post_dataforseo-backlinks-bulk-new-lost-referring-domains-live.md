> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk New & Lost Referring Domains

> This endpoint will provide you with the number of referring domains pointing to the domains, subdomains and pages specified in the `targets` array.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/backlinks/bulk_new_lost_referring_domains/live
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
  /dataforseo/backlinks/bulk_new_lost_referring_domains/live:
    post:
      summary: Bulk New & Lost Referring Domains
      description: >-
        This endpoint will provide you with the number of referring domains
        pointing to the domains, subdomains and pages specified in the `targets`
        array.
      operationId: post_dataforseo_backlinks_bulk_new_lost_referring_domains_live
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
                    domains, subdomains or webpages to get new & lost referring
                    domains for required field you can set up to 1000 domains,
                    subdomains or webpages the domain or subdomain should be
                    specified without https:// and www. the page should be
                    specified with absolute URL (including http:// or https://)
                    example: "targets": [ "forbes.com", "cnn.com", "bbc.com",
                    "yelp.com", "https://www.apple.com/iphone/",
                    "https://ahrefs.com/blog/", "ibm.com",
                    "https://variety.com/", "https://stackoverflow.com/",
                    "www.trustpilot.com" ]
                date_from:
                  type: string
                  description: >-
                    starting date of the time range optional field this field
                    indicates the date which will be used as a threshold for new
                    and lost referring domains; the referring domains that
                    appeared in our index after the specified date will be
                    considered as new; the referring domains that weren’t found
                    after the specified date, but were present before, will be
                    considered as lost; default value: today’s date -(minus) one
                    month; e.g. if today is 2021-10-13, default date_from will
                    be 2021-09-13. minimum value equals today’s date -(minus)
                    one year; e.g. if today is 2021-10-13, minimum date_from
                    will be 2020-10-13. date format: "yyyy-mm-dd" example:
                    "2021-01-01"
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
                  tasks.result.items.new_referring_domains:
                    type: integer
                    description: >-
                      number of new referring domains number of new referring
                      domains pointing to the target
                  tasks.result.items.lost_referring_domains:
                    type: integer
                    description: >-
                      number of lost referring domains number of lost referring
                      domains of the target
                  tasks.result.items.new_referring_main_domains:
                    type: integer
                    description: >-
                      number of new referring main domains pointing to the
                      target
                  tasks.result.items.lost_referring_main_domains:
                    type: integer
                    description: >-
                      number of lost referring main domains pointing to the
                      target
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