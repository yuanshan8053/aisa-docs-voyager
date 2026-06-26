> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Live ‘Bing Ads Audience Estimation’ Tasks

> This endpoint provides estimated audience size for an ad campaign based on specified targeting criteria.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/keywords_data/bing/audience_estimation/live
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
  /dataforseo/keywords_data/bing/audience_estimation/live:
    post:
      summary: Setting Live ‘Bing Ads Audience Estimation’ Tasks
      description: >-
        This endpoint provides estimated audience size for an ad campaign based
        on specified targeting criteria. It returns data on the total estimated
        audience, such as suggested bid and budget for an ad campaign and
        estimated engagement metrics.
      operationId: post_dataforseo_keywords_data_bing_audience_estimation_live
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                location_name:
                  type: string
                  description: >-
                    full name of search engine location required field if you
                    don’t specify location_code or location_coordinate if you
                    use this field, you don’t need to specify location_code or
                    location_coordinate you can receive the list of available
                    locations of the search engine with their location_name by
                    making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/bing/locations
                    example: London,England,United Kingdom
                location_code:
                  type: integer
                  description: >-
                    search engine location code required field if you don’t
                    specify location_name or location_coordinate if you use this
                    field, you don’t need to specify location_name or
                    location_coordinate you can receive the list of available
                    locations of the search engines with their location_code by
                    making a separate request to
                    https://api.dataforseo.com/v3/keywords_data/bing/locations
                    example: 2840
                location_coordinate:
                  type: string
                  description: >-
                    GPS coordinates of a location required field if you don’t
                    specify location_name or location_code if you use this
                    field, you don’t need to specify location_name or
                    location_code location_coordinate parameter should be
                    specified in the “latitude,longitude,radius (in km)” format
                    the data will be provided for the country the specified
                    coordinates belong to example: 29.6821525,-82.4098881,100
                age:
                  type: array
                  items:
                    type: string
                  description: >-
                    selection of age ranges for targeting possible values:
                    eighteen_to_twenty_four, fifty_to_sixty_four,
                    sixty_five_and_above, thirteen_to_seventeen,
                    thirty_five_to_forty_nine, twenty_five_to_thirty_four,
                    unknown, zero_to_twelve
                bid:
                  type: number
                  description: 'desired bid setting value in USD maximum value: 1000'
                daily_budget:
                  type: number
                  description: 'daily campaign budget value in USD maximum value: 10000'
                gender:
                  type: array
                  items:
                    type: string
                  description: 'gender to target possible values: male, female, unknown'
                industry:
                  type: array
                  items:
                    type: string
                  description: >-
                    industry of LinkedIn profile targeting if you use this
                    field, you can receive the list of available industry names
                    with industry_id by making a separate request to the
                    https://api.dataforseo.com/v3/keywords_data/bing/audience_estimation/industries
                    example: 806301758
                job_function:
                  type: array
                  items:
                    type: string
                  description: >-
                    job function of LinkedIn profile targeting if you use this
                    field, you can receive the list of available job function
                    names with job_function_id by making a separate request to
                    the
                    https://api.dataforseo.com/v3/keywords_data/bing/audience_estimation/job_functions
                    example: 806300451
              required:
                - location_name
                - location_code
                - location_coordinate
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
                      full list of response codes here
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
                  tasks.result.est_impressions:
                    type: object
                    description: monthly estimated impressions range
                  tasks.result.est_impressions.high:
                    type: integer
                    description: indicates the upper bound of the range result
                  tasks.result.est_impressions.low:
                    type: integer
                    description: indicates the lower bound of the range result
                  tasks.result.est_audience_size:
                    type: object
                    description: monthly estimated reach user count range
                  tasks.result.est_audience_size.high:
                    type: integer
                    description: indicates the upper bound of the range result
                  tasks.result.est_audience_size.low:
                    type: integer
                    description: indicates the lower bound of the range result
                  tasks.result.est_clicks:
                    type: object
                    description: monthly estimated click count range
                  tasks.result.est_clicks.high:
                    type: integer
                    description: indicates the upper bound of the range result
                  tasks.result.est_clicks.low:
                    type: integer
                    description: indicates the lower bound of the range result
                  tasks.result.est_spend:
                    type: object
                    description: monthly estimated spending range
                  tasks.result.est_spend.high:
                    type: integer
                    description: indicates the upper bound of the range result
                  tasks.result.est_spend.low:
                    type: integer
                    description: indicates the lower bound of the range result
                  tasks.result.est_cost_per_event:
                    type: object
                    description: indicates the estimated cost per event with range result
                  tasks.result.est_cost_per_event.high:
                    type: number
                    description: indicates the upper bound of the range result
                  tasks.result.est_cost_per_event.low:
                    type: number
                    description: indicates the lower bound of the range result
                  tasks.result.est_ctr:
                    type: object
                    description: estimated click-through rate range
                  tasks.result.est_ctr.high:
                    type: number
                    description: indicates the upper bound of the range result
                  tasks.result.est_ctr.low:
                    type: number
                    description: indicates the lower bound of the range result
                  tasks.result.suggested_bid:
                    type: number
                    description: suggested bid value under the current targeting
                  tasks.result.suggested_budget:
                    type: integer
                    description: >-
                      suggested daily budget value under the current targeting
                      and bid
                  tasks.result.events_lost_to_bid:
                    type: integer
                    description: indicates event lost count due to insufficient input bid
                  tasks.result.events_lost_to_budget:
                    type: integer
                    description: >-
                      indicates the event lost count due to insufficient input
                      budget
                  tasks.result.est_reach_audience_size:
                    type: integer
                    description: monthly estimated user count
                  tasks.result.est_reach_impressions:
                    type: integer
                    description: monthly estimated impressions
                  tasks.result.currency:
                    type: integer
                    description: 'currency name example: USDollar'
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