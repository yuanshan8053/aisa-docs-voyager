> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# New & Lost Backlinks Timeseries Summary

> This endpoint will provide you with the number of new and lost backlinks and referring domains for the domain specified in the `target` field.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/backlinks/timeseries_new_lost_summary/live
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
  /dataforseo/backlinks/timeseries_new_lost_summary/live:
    post:
      summary: New & Lost Backlinks Timeseries Summary
      description: >-
        This endpoint will provide you with the number of new and lost backlinks
        and referring domains for the domain specified in the `target` field.
      operationId: post_dataforseo_backlinks_timeseries_new_lost_summary_live
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
                    indicates the date which will be used as a threshold for new
                    and lost backlinks and referring domains; the backlinks and
                    referring domains that appeared in our index after the
                    specified date will be considered as new; the backlinks and
                    referring domains that weren’t found after the specified
                    date, but were present before, will be considered as lost;
                    minimum value: 2019-01-30 maximum value shouldn’t exceed the
                    date specified in the date_to date format: "yyyy-mm-dd"
                    example: "2021-01-01"
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
                    type: string
                    description: group_range from the POST array
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
                    description: contains relevant backlinks and referring domains data
                  tasks.result.items.type:
                    type: string
                    description: type of element = ‘backlinks_timeseries_new_lost_summary’
                  tasks.result.items.date:
                    type: string
                    description: >-
                      date and time when the data for the target was stored in
                      the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2019-11-15 12:57:46 +00:00
                  tasks.result.items.new_backlinks:
                    type: integer
                    description: >-
                      number of new backlinks number of new backlinks pointing
                      to the target
                  tasks.result.items.lost_backlinks:
                    type: integer
                    description: >-
                      number of lost backlinks number of lost backlinks of the
                      target
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
                      number of new referring main domains number of new
                      referring main domains pointing to the target
                  tasks.result.items.lost_referring_main_domains:
                    type: integer
                    description: >-
                      number of lost referring main domains number of lost
                      referring main domains of the target
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