> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Backlinks Timeseries Summary

> This endpoint will provide you with an overview of backlink data for the `target` domain available during a period between the two indicated dates.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/backlinks/timeseries_summary/live
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
  /dataforseo/backlinks/timeseries_summary/live:
    post:
      summary: Backlinks Timeseries Summary
      description: >-
        This endpoint will provide you with an overview of backlink data for the
        `target` domain available during a period between the two indicated
        dates. Backlink metrics will be grouped by the time range that you
        define: day, week, month, or year.
      operationId: post_dataforseo_backlinks_timeseries_summary_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                target:
                  type: string
                  description: >-
                    domain to get data for required field a domain should be
                    specified without https:// and www. example: "forbes.com"
                date_from:
                  type: string
                  description: >-
                    starting date of the time range optional field this field
                    indicates the date which will be used as a threshold for
                    summary data; minimum value: 2019-01-30 maximum value
                    shouldn’t exceed the date specified in the date_to date
                    format: "yyyy-mm-dd" example: "2021-01-01"
                date_to:
                  type: string
                  description: >-
                    ending date of the time range optional field if you don’t
                    specify this field, the today’s date will be used by default
                    minimum value shouldn’t preceed the date specified in the
                    date_from maximum value: today’s date date format:
                    "yyyy-mm-dd" example: "2021-01-15"
                group_range:
                  type: string
                  description: >-
                    time range which will be used to group the results optional
                    field default value: month possible values: day, week,
                    month, year note: for day, we will return items
                    corresponding to all dates between and including date_from
                    and date_to; for week/month/year, we will return items
                    corresponding to full weeks/months/years, where each item
                    will indicate the last day of the week/month/year for
                    example, if you specify: "group_range": "month",
                    "date_from": "2022-03-23", "date_to": "2022-05-13" we will
                    return items falling between 2022-03-01 and 2022-05-31,
                    namely, three items corresponding to the following dates:
                    2022-03-31, 2022-04-30, 2022-05-31 if there is no data for a
                    certain day/week/month/year, we will return 0
                include_subdomains:
                  type: boolean
                  description: >-
                    indicates if the subdomains of the target will be included
                    in the search optional field if set to false, the subdomains
                    will be ignored default value: true
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
                - target
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
                  tasks.result.target:
                    type: string
                    description: target from a POST array
                  tasks.result.date_from:
                    type: string
                    description: >-
                      starting date of the time range in the UTC format:
                      “yyyy-mm-dd” example: 2019-01-01
                  tasks.result.date_to:
                    type: string
                    description: >-
                      ending date of the time range in the UTC format:
                      "yyyy-mm-dd" example: "2019-01-15"
                  tasks.result.group_range:
                    type: object
                    description: group_range from a POST array
                  tasks.result.total_count:
                    type: integer
                    description: total amount of results relevant the request
                  tasks.result.items_count:
                    type: integer
                    description: the number of results returned in the items array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: contains relevant summary data
                  tasks.result.items.type:
                    type: string
                    description: type of element = ‘backlinks_timeseries_summary’
                  tasks.result.items.date:
                    type: string
                    description: >-
                      date and time when the data for the target was stored in
                      the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2019-11-15 12:57:46 +00:00
                  tasks.result.items.rank:
                    type: integer
                    description: >-
                      target rank for the given date learn more about the metric
                      and how it is calculated in this help center article
                  tasks.result.items.backlinks:
                    type: integer
                    description: number of backlinks for the given date
                  tasks.result.items.backlinks_nofollow:
                    type: integer
                    description: number of nofollow backlinks for the given date
                  tasks.result.items.referring_pages:
                    type: integer
                    description: number of pages pointing to target for the given date
                  tasks.result.items.referring_domains:
                    type: integer
                    description: >-
                      number of referring domains for the given date referring
                      domains include subdomains that are counted as separate
                      domains for this metric
                  tasks.result.items.referring_domains_nofollow:
                    type: integer
                    description: >-
                      number of domains pointing at least one nofollow link to
                      the target for the given date
                  tasks.result.items.referring_main_domains:
                    type: integer
                    description: number of referring main domains for the given date
                  tasks.result.items.referring_main_domains_nofollow:
                    type: integer
                    description: >-
                      number of main domains pointing at least one nofollow link
                      to the target for the given date
                  tasks.result.items.referring_ips:
                    type: integer
                    description: >-
                      number of referring IP addresses for the given date number
                      of IP addresses pointing to this page
                  tasks.result.items.referring_subnets:
                    type: integer
                    description: number of referring subnetworks for the given date
                  tasks.result.items.referring_pages_nofollow:
                    type: integer
                    description: >-
                      number of referring pages pointing at least one nofollow
                      link to the target for the given date
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