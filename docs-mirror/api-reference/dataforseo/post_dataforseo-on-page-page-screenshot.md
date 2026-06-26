> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OnPage API Page Screenshot

> Using this endpoint, you can capture a full high-quality screenshot of any webpage.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/on_page/page_screenshot
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
  /dataforseo/on_page/page_screenshot:
    post:
      summary: OnPage API Page Screenshot
      description: >-
        Using this endpoint, you can capture a full high-quality screenshot of
        any webpage. In this way, you can review the target page as the
        DataForSEO crawler and Googlebot see it.
      operationId: post_dataforseo_on_page_page_screenshot
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  description: >-
                    page url required field absolute URL of the page to snap
                    note: if the URL you indicate here returns a 404 status code
                    or the indicated value is not a valid URL, you will obtain
                    "error_message":"Screenshot is empty" in the response array
                accept_language:
                  type: string
                  description: >-
                    language header for accessing the website optional field all
                    locale formats are supported (xx, xx-XX, xxx-XX, etc.) note:
                    if you do not specify this parameter, some websites may deny
                    access; in this case, you will obtain
                    "error_message":"Screenshot is empty" in the response array
                custom_user_agent:
                  type: string
                  description: >-
                    custom user agent optional field custom user agent for
                    crawling a website example: Mozilla/5.0 (Macintosh; Intel
                    Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko)
                    Chrome/83.0.4103.116 Safari/537.36 default value:
                    Mozilla/5.0 (compatible; RSiteAuditor)
                browser_preset:
                  type: string
                  description: >-
                    preset for browser screen parameters optional field if you
                    use this field, you don’t need to indicate
                    browser_screen_width, browser_screen_height,
                    browser_screen_scale_factor possible values: desktop,
                    mobile, tablet desktop preset will apply the following
                    values: browser_screen_width: 1920 browser_screen_height:
                    1080 browser_screen_scale_factor: 1 mobile preset will apply
                    the following values: browser_screen_width: 390
                    browser_screen_height: 844 browser_screen_scale_factor: 3
                    tablet preset will apply the following values:
                    browser_screen_width: 1024 browser_screen_height: 1366
                    browser_screen_scale_factor: 2 Note: in this endpoint, the
                    enable_browser_rendering, enable_javascript, load_resources,
                    and enable_xhr parameters are always enabled.
                browser_screen_width:
                  type: integer
                  description: >-
                    browser screen width optional field you can set a custom
                    browser screen width to perform audit for a particular
                    device; if you use this field, you don’t need to indicate
                    browser_preset as it will be ignored; minimum value, in
                    pixels: 240 maximum value, in pixels: 9999
                browser_screen_height:
                  type: integer
                  description: >-
                    browser screen height optional field you can set a custom
                    browser screen height to perform audit for a particular
                    device; if you use this field, you don’t need to indicate
                    browser_preset as it will be ignored; minimum value, in
                    pixels: 240 maximum value, in pixels: 9999
                browser_screen_scale_factor:
                  type: number
                  description: >-
                    browser screen scale factor optional field you can set a
                    custom browser screen resolution ratio to perform audit for
                    a particular device; if you use this field, you don’t need
                    to indicate browser_preset as it will be ignored; minimum
                    value: 0.5 maximum value: 3
                full_page_screenshot:
                  type: boolean
                  description: >-
                    take a screenshot of the full page optional field set to
                    false if you want to capture only the part of the page
                    displayed before scrolling default value: true
                disable_cookie_popup:
                  type: boolean
                  description: >-
                    disable the cookie popup optional field set to true if you
                    want to disable the popup requesting cookie consent from the
                    user; default value: false
                switch_pool:
                  type: boolean
                  description: >-
                    switch proxy pool optional field if true, additional proxy
                    pools will be used to obtain the requested data; the
                    parameter can be used if a multitude of tasks is set
                    simultaneously, resulting in occasional rate-limit and/or
                    site_unreachable errors
                ip_pool_for_scan:
                  type: string
                  description: >-
                    proxy pool optional field you can choose a location of the
                    proxy pool that will be used to obtain the requested data;
                    the parameter can be used if page content is inaccessible in
                    one of the locations, resulting in occasional
                    site_unreachable errors possible values: us, de
              required:
                - url
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
                  tasks.result.crawl_progress:
                    type: string
                    description: >-
                      status of the crawling session possible values:
                      in_progress, finished
                  tasks.result.error_message:
                    type: string
                    description: >-
                      error message if the url you indicated returns a 404
                      status code or is not a valid URL, you will obtain
                      "error_message":"Screenshot is empty" if no error is
                      encountered, the value will be null
                  tasks.result.items_count:
                    type: integer
                    description: number of items in the results array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: items array
                  tasks.result.items.image:
                    type: string
                    description: >-
                      screenshot of the requested page URL of the page
                      screenshot on the DataForSEO storage
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