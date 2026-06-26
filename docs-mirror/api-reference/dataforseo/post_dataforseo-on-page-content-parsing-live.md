> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live OnPage API Content Parsing

> This endpoint allows parsing the content on any page you specify and will return the structured content of the target page, including link URLs, anchors, hea...



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/on_page/content_parsing/live
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
  /dataforseo/on_page/content_parsing/live:
    post:
      summary: Live OnPage API Content Parsing
      description: >-
        This endpoint allows parsing the content on any page you specify and
        will return the structured content of the target page, including link
        URLs, anchors, headings, and textual content.
      operationId: post_dataforseo_on_page_content_parsing_live
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
                    URL of the content to parse required field URL of the page
                    to parse example: https://www.fujielectric.com/
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
                    browser_screen_scale_factor: 2 Note: to use this parameter,
                    set enable_javascript or enable_browser_rendering to true
                browser_screen_width:
                  type: integer
                  description: >-
                    browser screen width optional field you can set a custom
                    browser screen width to perform audit for a particular
                    device; if you use this field, you don’t need to indicate
                    browser_preset as it will be ignored; Note: to use this
                    parameter, set enable_javascript or enable_browser_rendering
                    to true minimum value, in pixels: 240 maximum value, in
                    pixels: 9999
                browser_screen_height:
                  type: integer
                  description: >-
                    browser screen height optional field you can set a custom
                    browser screen height to perform audit for a particular
                    device; if you use this field, you don’t need to indicate
                    browser_preset as it will be ignored; Note: to use this
                    parameter, set enable_javascript or enable_browser_rendering
                    to true minimum value, in pixels: 240 maximum value, in
                    pixels: 9999
                browser_screen_scale_factor:
                  type: number
                  description: >-
                    browser screen scale factor optional field you can set a
                    custom browser screen resolution ratio to perform audit for
                    a particular device; if you use this field, you don’t need
                    to indicate browser_preset as it will be ignored; Note: to
                    use this parameter, set enable_javascript or
                    enable_browser_rendering to true minimum value: 0.5 maximum
                    value: 3
                store_raw_html:
                  type: boolean
                  description: >-
                    store HTML of a crawled page optional field set to true if
                    you want to get the HTML of the page using the OnPage Raw
                    HTML endpoint default value: false
                disable_cookie_popup:
                  type: boolean
                  description: >-
                    disable the cookie popup optional field set to true if you
                    want to disable the popup requesting cookie consent from the
                    user; default value: false
                accept_language:
                  type: string
                  description: >-
                    language header for accessing the website optional field all
                    locale formats are supported (xx, xx-XX, xxx-XX, etc.) Note:
                    if you do not specify this parameter, some websites may deny
                    access; in this case, pages will be returned with the
                    "type":"broken in the response array
                enable_javascript:
                  type: boolean
                  description: >-
                    load javascript on a page optional field set to true if you
                    want to load the scripts available on a page default value:
                    false Note: if you use this parameter, additional charges
                    will apply; learn more about the cost of tasks with this
                    parameter in our help article; the cost can be calculated on
                    the Pricing Page
                enable_browser_rendering:
                  type: boolean
                  description: >-
                    emulate browser rendering to measure Core Web Vitals
                    optional field by using this parameter you will be able to
                    emulate a browser when loading a web page;
                    enable_browser_rendering loads styles, images, fonts,
                    animations, videos, and other resources on a page; default
                    value: false set to true to obtain Core Web Vitals (FID,
                    CLS, LCP) metrics in the response; if you use this field,
                    enable_javascript, and load_resources parameters must be set
                    to true Note: if you use this parameter, additional charges
                    will apply; learn more about the cost of tasks with this
                    parameter in our help article; the cost can be calculated on
                    the Pricing Page
                enable_xhr:
                  type: boolean
                  description: >-
                    enable XMLHttpRequest on a page optional field set to true
                    if you want our crawler to request data from a web server
                    using the XMLHttpRequest object default value: false if you
                    use this field, enable_javascript must be set to true;
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
                markdown_view:
                  type: boolean
                  description: >-
                    return page content as markdown optional field if set to
                    true, the markdown-formatted content of the page will be
                    returned in the page_as_markdown field of the response;
                    default value: false
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
                  tasks.result.crawl_status:
                    type: object
                    description: details of the crawling session
                  tasks.result.items_count:
                    type: integer
                    description: number of items in the results array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: items array
                  tasks.result.items.type:
                    type: string
                    description: type of the returned item = ‘сontent_parsing_element’
                  tasks.result.items.fetch_time:
                    type: string
                    description: >-
                      date and time when the content was fetched in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: "2022-11-01
                      10:02:52 +00:00"
                  tasks.result.items.status_code:
                    type: integer
                    description: status code of the page
                  tasks.result.items.page_content:
                    type: object
                    description: parsed content of the page
                  tasks.result.items.page_content.header:
                    type: object
                    description: parsed content of the header
                  tasks.result.items.page_content.primary_content:
                    type: array
                    items:
                      type: string
                    description: >-
                      primary content on the page you can find more information
                      about content priority calculation in this help center
                      article
                  tasks.result.items.page_content.primary_content.text:
                    type: string
                    description: content text
                  tasks.result.items.page_content.primary_content.url:
                    type: string
                    description: page URL displayed in case the text is a link anchor
                  tasks.result.items.page_content.primary_content.urls:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains other URLs and anchors found in the content
                      element
                  tasks.result.items.page_content.primary_content.urls.url:
                    type: string
                    description: other URL found in the content element
                  tasks.result.items.page_content.primary_content.urls.anchor_text:
                    type: string
                    description: text of the URL’s anchor
                  tasks.result.items.page_content.secondary_content:
                    type: array
                    items:
                      type: string
                    description: >-
                      secondary content on the page you can find more
                      information about content priority calculation in this
                      help center article
                  tasks.result.items.page_content.secondary_content.text:
                    type: string
                    description: content text
                  tasks.result.items.page_content.secondary_content.url:
                    type: string
                    description: page URL displayed in case the text is a link anchor
                  tasks.result.items.page_content.secondary_content.urls:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains other URLs and anchors found in the content
                      element
                  tasks.result.items.page_content.secondary_content.urls.url:
                    type: string
                    description: other URL found in the content element
                  tasks.result.items.page_content.secondary_content.urls.anchor_text:
                    type: string
                    description: text of the URL’s anchor
                  tasks.result.items.page_content.table_content:
                    type: array
                    items:
                      type: string
                    description: content of the table on the page
                  tasks.result.items.page_content.table_content.header:
                    type: array
                    items:
                      type: string
                    description: content of the header of the table
                  tasks.result.items.page_content.table_content.header.row_cells:
                    type: array
                    items:
                      type: string
                    description: content of the row cells of the header
                  tasks.result.items.page_content.table_content.header.row_cells.text:
                    type: string
                    description: text in the row cell
                  tasks.result.items.page_content.table_content.header.row_cells.urls:
                    type: array
                    items:
                      type: string
                    description: contains other URLs and anchors found in the cell
                  tasks.result.items.page_content.table_content.header.row_cells.urls.url:
                    type: string
                    description: URL found in the cell
                  tasks.result.items.page_content.table_content.header.row_cells.urls.anchor_text:
                    type: string
                    description: text of the URL’s anchor
                  tasks.result.items.page_content.table_content.header.row_cells.is_header:
                    type: boolean
                    description: indicates if the text belongs to the header
                  tasks.result.items.page_content.table_content.body:
                    type: array
                    items:
                      type: string
                    description: content of the body of the table
                  tasks.result.items.page_content.table_content.body.row_cells:
                    type: array
                    items:
                      type: string
                    description: content of the row cells of the header
                  tasks.result.items.page_content.table_content.body.row_cells.text:
                    type: string
                    description: text in the row cell
                  tasks.result.items.page_content.table_content.body.row_cells.urls:
                    type: array
                    items:
                      type: string
                    description: contains other URLs and anchors found in the cell
                  tasks.result.items.page_content.table_content.body.row_cells.urls.url:
                    type: string
                    description: URL found in the cell
                  tasks.result.items.page_content.table_content.body.row_cells.urls.anchor_text:
                    type: string
                    description: text of the URL’s anchor
                  tasks.result.items.page_content.table_content.body.row_cells.is_header:
                    type: boolean
                    description: indicates if the text belongs to the header
                  tasks.result.items.page_content.table_content.footer:
                    type: array
                    items:
                      type: string
                    description: content of the footer of the table
                  tasks.result.items.page_content.table_content.footer.row_cells:
                    type: array
                    items:
                      type: string
                    description: content of the row cells of the header
                  tasks.result.items.page_content.table_content.footer.row_cells.text:
                    type: string
                    description: text in the row cell
                  tasks.result.items.page_content.table_content.footer.row_cells.urls:
                    type: array
                    items:
                      type: string
                    description: contains other URLs and anchors found in the cell
                  tasks.result.items.page_content.table_content.footer.row_cells.urls.url:
                    type: string
                    description: URL found in the cell
                  tasks.result.items.page_content.table_content.footer.row_cells.urls.anchor_text:
                    type: string
                    description: text of the URL’s anchor
                  tasks.result.items.page_content.table_content.footer.row_cells.is_header:
                    type: boolean
                    description: indicates if the text belongs to the header
                  tasks.result.items.page_content.footer:
                    type: object
                    description: parsed content of the footer
                  tasks.result.items.page_content.main_topic:
                    type: array
                    items:
                      type: string
                    description: >-
                      main topic on the page you can find more information about
                      topic priority calculation in this help center article
                  tasks.result.items.page_content.main_topic.h_title:
                    type: string
                    description: meta title
                  tasks.result.items.page_content.main_topic.main_title:
                    type: string
                    description: main title of the block
                  tasks.result.items.page_content.main_topic.author:
                    type: string
                    description: content author name
                  tasks.result.items.page_content.main_topic.language:
                    type: string
                    description: content language
                  tasks.result.items.page_content.main_topic.level:
                    type: string
                    description: HTML level
                  tasks.result.items.page_content.main_topic.primary_content:
                    type: array
                    items:
                      type: string
                    description: >-
                      primary content on the page you can find more information
                      about content priority calculation in this help center
                      article
                  tasks.result.items.page_content.main_topic.text:
                    type: string
                    description: content text
                  tasks.result.items.page_content.main_topic.url:
                    type: string
                    description: page URL displayed in case the text is a link anchor
                  tasks.result.items.page_content.main_topic.urls:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains other URLs and anchors found in the content
                      element
                  tasks.result.items.page_content.main_topic.urls.url:
                    type: string
                    description: other URL found in the content element
                  tasks.result.items.page_content.main_topic.urls.anchor_text:
                    type: string
                    description: text of the URL’s anchor
                  tasks.result.items.page_content.main_topic.secondary_content:
                    type: array
                    items:
                      type: string
                    description: >-
                      secondary content on the page you can find more
                      information about content priority calculation in this
                      help center article
                  tasks.result.items.page_content.secondary_topic:
                    type: array
                    items:
                      type: string
                    description: >-
                      secondary topic on the page you can find more information
                      about topic priority calculation in this help center
                      article
                  tasks.result.items.page_content.secondary_topic.h_title:
                    type: string
                    description: meta title
                  tasks.result.items.page_content.secondary_topic.main_title:
                    type: string
                    description: main title of the block
                  tasks.result.items.page_content.secondary_topic.author:
                    type: string
                    description: content author name
                  tasks.result.items.page_content.secondary_topic.language:
                    type: string
                    description: content language
                  tasks.result.items.page_content.secondary_topic.level:
                    type: string
                    description: HTML level
                  tasks.result.items.page_content.secondary_topic.primary_content:
                    type: array
                    items:
                      type: string
                    description: >-
                      primary content on the page you can find more information
                      about content priority calculation in this help center
                      article
                  tasks.result.items.page_content.secondary_topic.text:
                    type: string
                    description: content text
                  tasks.result.items.page_content.secondary_topic.url:
                    type: string
                    description: page URL displayed in case the text is a link anchor
                  tasks.result.items.page_content.secondary_topic.urls:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains other URLs and anchors found in the content
                      element
                  tasks.result.items.page_content.secondary_topic.urls.url:
                    type: string
                    description: other URL found in the content element
                  tasks.result.items.page_content.secondary_topic.urls.anchor_text:
                    type: string
                    description: text of the URL’s anchor
                  tasks.result.items.page_content.secondary_topic.secondary_content:
                    type: array
                    items:
                      type: string
                    description: >-
                      secondary content on the page you can find more
                      information about content priority calculation in this
                      help center article
                  tasks.result.items.page_content.ratings:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains objects with rating information for the products
                      displayed on the page
                  tasks.result.items.page_content.ratings.name:
                    type: string
                    description: >-
                      rating name Note: this field is not used in this
                      particular object, and its value is always set to null
                  tasks.result.items.page_content.ratings.rating_value:
                    type: integer
                    description: the value of the rating
                  tasks.result.items.page_content.ratings.max_rating_value:
                    type: integer
                    description: maximum value for the rating
                  tasks.result.items.page_content.ratings.rating_count:
                    type: integer
                    description: the amount of feedback
                  tasks.result.items.page_content.ratings.relative_rating:
                    type: number
                    description: relative rating can take values from 0 to 1
                  tasks.result.items.page_content.offers:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of products displayed on the page contains objects
                      with information on products displayed on the page
                  tasks.result.items.page_content.offers.name:
                    type: string
                    description: name of the product
                  tasks.result.items.page_content.offers.price:
                    type: integer
                    description: price of the product
                  tasks.result.items.page_content.offers.price_currency:
                    type: string
                    description: price currency
                  tasks.result.items.page_content.offers.price_valid_until:
                    type: integer
                    description: >-
                      displays the date and time until which the price is valid
                      in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      "2022-11-01 10:02:52 +00:00"
                  tasks.result.items.page_content.comments:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of comments displayed on the page contains objects
                      with information on comments related to displayed products
                  tasks.result.items.page_content.comments.rating:
                    type: object
                    description: >-
                      product’s rating contains information about the rating a
                      customer has given to the product
                  tasks.result.items.page_content.comments.name:
                    type: string
                    description: >-
                      rating name Note: this field is not used in this
                      particular object, and its value is always null
                  tasks.result.items.page_content.comments.rating_value:
                    type: integer
                    description: the value of the rating
                  tasks.result.items.page_content.comments.max_rating_value:
                    type: integer
                    description: maximum value for the rating
                  tasks.result.items.page_content.comments.rating_count:
                    type: integer
                    description: >-
                      the amount of feedback Note: this field is not used in
                      this particular object, and its value is always null
                  tasks.result.items.page_content.comments.relative rating:
                    type: number
                    description: relative rating can take values from 0 to 1
                  tasks.result.items.page_content.comments.title:
                    type: string
                    description: title of the customer’s comment
                  tasks.result.items.page_content.comments.publish_date:
                    type: string
                    description: date when the comment was published
                  tasks.result.items.page_content.comments.author:
                    type: string
                    description: author of the comment
                  tasks.result.items.page_content.comments.primary_content:
                    type: array
                    items:
                      type: string
                    description: >-
                      primary content on the page you can find more information
                      about content priority calculation in this help center
                      article
                  tasks.result.items.page_content.comments.primary_content.text:
                    type: string
                    description: text of the comment
                  tasks.result.items.page_content.comments.primary_content.url:
                    type: string
                    description: displayed in case the text is a link anchor
                  tasks.result.items.page_content.comments.primary_content.urls:
                    type: array
                    items:
                      type: string
                    description: >-
                      contains other URLs and anchors found in the content
                      element
                  tasks.result.items.page_content.contacts:
                    type: object
                    description: >-
                      contact information contains contact information displayed
                      on the page
                  tasks.result.items.page_content.contacts.telephones:
                    type: array
                    items:
                      type: string
                    description: array of telephone numbers
                  tasks.result.items.page_content.contacts.emails:
                    type: array
                    items:
                      type: string
                    description: array of emails
                  tasks.result.items.page_as_markdown:
                    type: string
                    description: >-
                      page content in the markdown format page content in the
                      text-to-HTML markdown format specify markdown_view as true
                      in the request to return the value
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