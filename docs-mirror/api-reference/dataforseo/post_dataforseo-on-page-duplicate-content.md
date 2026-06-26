> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OnPage API Duplicate Content

> This endpoint returns a list of pages that have content similar to the page specified in the request.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/on_page/duplicate_content
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
  /dataforseo/on_page/duplicate_content:
    post:
      summary: OnPage API Duplicate Content
      description: >-
        This endpoint returns a list of pages that have content similar to the
        page specified in the request. The response also contains data related
        to page performance and the similarity index that indicates how similar
        the compared pages are.
      operationId: post_dataforseo_on_page_duplicate_content
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: string
                  description: >-
                    ID of the task required field you can get this ID in the
                    response of the Task POST endpoint example:
                    “07131248-1535-0216-1000-17384017ad04”
                url:
                  type: string
                  description: >-
                    page URL required field specify the initial page you want to
                    receive duplicate content for
                similarity:
                  type: integer
                  description: >-
                    content similarity score by default, the content is
                    considered duplicate if the value is greater than or equals
                    6 you can specify any similarity score in the 0-to-10 range
                limit:
                  type: integer
                  description: >-
                    the maximum number of returned pages optional field default
                    value: 100 maximum value: 1000
                offset:
                  type: integer
                  description: >-
                    offset in the results array of returned pages optional field
                    default value: 0 if you specify the 10 value, the first ten
                    pages in the results array will be omitted and the data will
                    be provided for the successive pages
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
              required:
                - id
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
                  tasks.result.crawl_status.max_crawl_pages:
                    type: integer
                    description: >-
                      maximum number of pages to crawl indicates the
                      max_crawl_pages limit you specified when setting a task
                  tasks.result.crawl_status.pages_in_queue:
                    type: integer
                    description: number of pages that are currently in the crawling queue
                  tasks.result.crawl_status.pages_crawled:
                    type: integer
                    description: number of crawled pages
                  tasks.result.items_count:
                    type: integer
                    description: number of items in the results array
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: items array
                  tasks.result.items.url:
                    type: string
                    description: URL of the specified page
                  tasks.result.items.total_count:
                    type: integer
                    description: total count of duplicate pages
                  tasks.result.items.pages:
                    type: array
                    items:
                      type: string
                    description: pages with duplicate content
                  tasks.result.items.pages.similarity:
                    type: integer
                    description: >-
                      content similarity score by default, the content is
                      considered duplicate if the value is greater than or
                      equals 6 can take values from 0 to 10
                  tasks.result.items.pages.page:
                    type: array
                    items:
                      type: string
                    description: information about the page with duplicate content
                  tasks.result.items.pages.page.resource_type:
                    type: string
                    description: type of the returned resource = ‘html’
                  tasks.result.items.pages.page.status_code:
                    type: integer
                    description: status code of the page
                  tasks.result.items.pages.page.location:
                    type: string
                    description: location header indicates the URL to redirect a page to
                  tasks.result.items.pages.page.url:
                    type: string
                    description: page URL
                  tasks.result.items.pages.page.meta:
                    type: object
                    description: page properties the value depends on the resource_type
                  tasks.result.items.pages.page.meta.title:
                    type: integer
                    description: page title
                  tasks.result.items.pages.page.meta.charset:
                    type: integer
                    description: 'code page example: 65001'
                  tasks.result.items.pages.page.meta.follow:
                    type: boolean
                    description: >-
                      indicates whether a page’s ‘meta robots’ allows crawlers
                      to follow the links on the page if false, the page’s ‘meta
                      robots’ tag contains “nofollow” parameter instructing
                      crawlers not to follow the links on the page
                  tasks.result.items.pages.page.meta.generator:
                    type: string
                    description: meta tag generator
                  tasks.result.items.pages.page.meta.htags:
                    type: object
                    description: HTML header tags
                  tasks.result.items.pages.page.meta.description:
                    type: string
                    description: content of the meta description tag
                  tasks.result.items.pages.page.meta.favicon:
                    type: string
                    description: favicon of the page
                  tasks.result.items.pages.page.meta.meta_keywords:
                    type: string
                    description: content of the keywords meta tag
                  tasks.result.items.pages.page.meta.canonical:
                    type: string
                    description: canonical page
                  tasks.result.items.pages.page.meta.internal_links_count:
                    type: integer
                    description: number of internal links on the page
                  tasks.result.items.pages.page.meta.external_links_count:
                    type: integer
                    description: number of external links on the page
                  tasks.result.items.pages.page.meta.inbound_links_count:
                    type: integer
                    description: number of internal links pointing at the page
                  tasks.result.items.pages.page.meta.images_count:
                    type: integer
                    description: number of images on the page
                  tasks.result.items.pages.page.meta.images_size:
                    type: integer
                    description: total size of images on the page measured in bytes
                  tasks.result.items.pages.page.meta.scripts_count:
                    type: integer
                    description: number of scripts on the page
                  tasks.result.items.pages.page.meta.scripts_size:
                    type: integer
                    description: total size of scripts on the page measured in bytes
                  tasks.result.items.pages.page.meta.stylesheets_count:
                    type: integer
                    description: number of stylesheets on the page
                  tasks.result.items.pages.page.meta.stylesheets_size:
                    type: integer
                    description: total size of stylesheets on the page measured in bytes
                  tasks.result.items.pages.page.meta.title_length:
                    type: integer
                    description: length of the title tag in characters
                  tasks.result.items.pages.page.meta.description_length:
                    type: integer
                    description: length of the description tag in characters
                  tasks.result.items.pages.page.meta.render_blocking_scripts_count:
                    type: integer
                    description: number of scripts on the page that block page rendering
                  tasks.result.items.pages.page.meta.render_blocking_stylesheets_count:
                    type: integer
                    description: number of CSS styles on the page that block page rendering
                  tasks.result.items.pages.page.meta.cumulative_layout_shift:
                    type: number
                    description: >-
                      Core Web Vitals metric measuring the layout stability of a
                      page measures the sum total of all individual layout shift
                      scores for every unexpected layout shift that occurs
                      during the entire lifespan of the page. Learn more.
                  tasks.result.items.pages.page.meta.content:
                    type: object
                    description: overall information about content of the page
                  tasks.result.items.pages.page.meta.content.plain_text_size:
                    type: integer
                    description: total size of the text on the page measured in bytes
                  tasks.result.items.pages.page.meta.content.plain_text_rate:
                    type: integer
                    description: plaintext rate value plain_text_size to size ratio
                  tasks.result.items.pages.page.meta.content.plain_text_word_count:
                    type: number
                    description: number of words on the page
                  tasks.result.items.pages.page.meta.content.automated_readability_index:
                    type: number
                    description: Automated Readability Index
                  tasks.result.items.pages.page.meta.content.coleman_liau_readability_index:
                    type: number
                    description: Coleman–Liau Index
                  tasks.result.items.pages.page.meta.content.dale_chall_readability_index:
                    type: number
                    description: Dale–Chall Readability Index
                  tasks.result.items.pages.page.meta.content.flesch_kincaid_readability_index:
                    type: number
                    description: Flesch–Kincaid Readability Index
                  tasks.result.items.pages.page.meta.content.smog_readability_index:
                    type: number
                    description: SMOG Readability Index
                  tasks.result.items.pages.page.meta.content.description_to_content_consistency:
                    type: number
                    description: >-
                      consistency of the meta description tag with the page
                      content measured from 0 to 1
                  tasks.result.items.pages.page.meta.content.title_to_content_consistency:
                    type: number
                    description: >-
                      consistency of the meta title tag with the page content
                      measured from 0 to 1
                  tasks.result.items.pages.page.meta.content.meta_keywords_to_content_consistency:
                    type: number
                    description: >-
                      consistency of meta keywordstag with the page content
                      measured from 0 to 1
                  tasks.result.items.pages.page.meta.deprecated_tags:
                    type: array
                    items:
                      type: string
                    description: deprecated tags on the page
                  tasks.result.items.pages.page.meta.duplicate_meta_tags:
                    type: array
                    items:
                      type: string
                    description: duplicate meta tags on the page
                  tasks.result.items.pages.page.meta.spell:
                    type: object
                    description: spellcheck hunspell spellcheck errors
                  tasks.result.items.pages.page.meta.spell.hunspell_language_code:
                    type: string
                    description: spellcheck language code
                  tasks.result.items.pages.page.meta.spell.misspelled:
                    type: array
                    items:
                      type: string
                    description: array of misspelled words
                  tasks.result.items.pages.page.meta.spell.misspelled.word:
                    type: string
                    description: misspelled word
                  tasks.result.items.pages.page.meta.resource_errors:
                    type: object
                    description: resource errors and warnings
                  tasks.result.items.pages.page.meta.resource_errors.errors:
                    type: array
                    items:
                      type: string
                    description: resource errors
                  tasks.result.items.pages.page.meta.resource_errors.errors.line:
                    type: integer
                    description: line where the error was found
                  tasks.result.items.pages.page.meta.resource_errors.errors.message:
                    type: string
                    description: >-
                      text message of the error the full list of possible HTML
                      errors can be found here
                  tasks.result.items.pages.page.meta.resource_errors.warnings:
                    type: array
                    items:
                      type: string
                    description: resource warnings
                  tasks.result.items.pages.page.meta.resource_errors.warnings.line:
                    type: integer
                    description: >-
                      line the warning relates to note that if "line": 0, the
                      warning relates to the whole page
                  tasks.result.items.pages.page.meta.resource_errors.warnings.message:
                    type: string
                    description: >-
                      text message of the warning possible messages: "Has node
                      with more than 60 childs." – HTML page has at least 1 tag
                      nesting over 60 tags of the same level "Has more that 1500
                      nodes." – DOM tree contains over 1,500 elements "HTML
                      depth more than 32 tags." – DOM depth exceeds 32 nodes
                  tasks.result.items.pages.page.meta.social_media_tags:
                    type: object
                    description: >-
                      array of social media tags found on the page contains
                      social media tags and their content supported tags include
                      but are not limited to Open Graph and Twitter card
                  tasks.result.items.pages.page.page_timing:
                    type: object
                    description: object of page load metrics
                  tasks.result.items.pages.page.page_timing.time_to_interactive:
                    type: integer
                    description: >-
                      Time To Interactive (TTI) metric the time it takes until
                      the user can interact with a page (in milliseconds)
                  tasks.result.items.pages.page.page_timing.dom_complete:
                    type: integer
                    description: >-
                      time to load resources the time it takes until the page
                      and all of its subresources are downloaded (in
                      milliseconds)
                  tasks.result.items.pages.page.page_timing.largest_contentful_paint:
                    type: number
                    description: >-
                      Core Web Vitals metric measuring how fast the largest
                      above-the-fold content element is displayed The amount of
                      time (in milliseconds) to render the largest content
                      element visible in the viewport, from when the user
                      requests the URL. Learn more.
                  tasks.result.items.pages.page.page_timing.first_input_delay:
                    type: number
                    description: >-
                      Core Web Vitals metric indicating the responsiveness of a
                      page The time (in milliseconds) from when a user first
                      interacts with your page to the time when the browser
                      responds to that interaction. Learn more.
                  tasks.result.items.pages.page.page_timing.connection_time:
                    type: integer
                    description: >-
                      time to connect to a server the time it takes until the
                      connection with a server is established (in milliseconds)
                  tasks.result.items.pages.page.page_timing.time_to_secure_connection:
                    type: integer
                    description: >-
                      time to establish a secure connection the time it takes
                      until the secure connection with a server is established
                      (in milliseconds)
                  tasks.result.items.pages.page.page_timing.request_sent_time:
                    type: integer
                    description: >-
                      time to send a request to a server the time it takes until
                      the request to a server is sent (in milliseconds)
                  tasks.result.items.pages.page.page_timing.waiting_time:
                    type: integer
                    description: time to first byte (TTFB) in milliseconds
                  tasks.result.items.pages.page.page_timing.download_time:
                    type: integer
                    description: >-
                      time it takes for a browser to receive a response (in
                      milliseconds)
                  tasks.result.items.pages.page.page_timing.duration_time:
                    type: integer
                    description: >-
                      total time it takes until a browser receives a complete
                      response from a server (in milliseconds)
                  tasks.result.items.pages.page.page_timing.fetch_start:
                    type: integer
                    description: >-
                      time to start downloading the HTML resource the amount of
                      time the browser needs to start downloading a page
                  tasks.result.items.pages.page.page_timing.fetch_end:
                    type: integer
                    description: >-
                      time to complete downloading the HTML resource the amount
                      of time the browser needs to complete downloading a page
                  tasks.result.items.pages.page.onpage_score:
                    type: number
                    description: >-
                      shows how page is optimized on a 100-point scale this
                      field shows how page is optimized considering critical
                      on-page issues and warnings detected; 100 is the highest
                      possible score that means the page does not have any
                      critical on-page issues and important warnings; learn more
                      about how the metric is calculated in this help center
                      article
                  tasks.result.items.pages.page.total_dom_size:
                    type: integer
                    description: total DOM size of a page
                  tasks.result.items.pages.page.custom_js_response:
                    type: string
                    description: >-
                      the result of executing a specified JS script note that
                      you should specify a custom_js field when setting a task
                      to receive this data and the field type and its value will
                      totally depend on the script you specified;you can also
                      filter the results by this value specifying filters in the
                      following way: ["custom_js_response.url", "like", "pixel"]
                  tasks.result.items.pages.page.custom_js_client_exception:
                    type: string
                    description: >-
                      error when executing a custom js if the error occurred
                      when executing the script you specified in the custom_js
                      field, the error message would be displayed here
                  tasks.result.items.pages.page.broken_resources:
                    type: boolean
                    description: indicates whether a page contains broken resources
                  tasks.result.items.pages.page.broken_links:
                    type: boolean
                    description: indicates whether a page contains broken links
                  tasks.result.items.pages.page.duplicate_title:
                    type: boolean
                    description: indicates whether a page has duplicate title tags
                  tasks.result.items.pages.page.duplicate_description:
                    type: boolean
                    description: indicates whether a page has a duplicate description
                  tasks.result.items.pages.page.duplicate_content:
                    type: boolean
                    description: indicates whether a page has duplicate content
                  tasks.result.items.pages.page.click_depth:
                    type: integer
                    description: >-
                      number of clicks it takes to get to the page indicates the
                      number of clicks from the homepage needed before landing
                      at the target page
                  tasks.result.items.pages.page.size:
                    type: integer
                    description: >-
                      resource size indicates the size of a given page measured
                      in bytes
                  tasks.result.items.pages.page.encoded_size:
                    type: integer
                    description: >-
                      page size after encoding indicates the size of the encoded
                      page measured in bytes
                  tasks.result.items.pages.page.total_transfer_size:
                    type: integer
                    description: >-
                      compressed page size indicates the compressed size of a
                      given page
                  tasks.result.items.pages.page.fetch_time:
                    type: string
                    description: >-
                      date and time when a resource was fetched in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items.pages.page.cache_control:
                    type: object
                    description: instructions for caching
                  tasks.result.items.pages.page.cache_control.cachable:
                    type: boolean
                    description: indicates whether the page is cacheable
                  tasks.result.items.pages.page.cache_control.ttl:
                    type: integer
                    description: >-
                      time to live the amount of time the browser caches a
                      resource
                  tasks.result.items.pages.page.checks:
                    type: object
                    description: website checks on-page check-ups related to the page
                  tasks.result.items.pages.page.checks.no_content_encoding:
                    type: boolean
                    description: >-
                      page with no content encoding indicates whether a page has
                      no compression algorithm of the content
                  tasks.result.items.pages.page.checks.high_loading_time:
                    type: boolean
                    description: >-
                      page with high loading time indicates whether a page
                      loading time exceeds 3 seconds
                  tasks.result.items.pages.page.checks.is_redirect:
                    type: boolean
                    description: >-
                      page with redirects indicates whether a page has 3XX
                      redirects to other pages
                  tasks.result.items.pages.page.checks.is_4xx_code:
                    type: boolean
                    description: >-
                      page with 4xx status codes indicates whether a page has
                      4xx response code
                  tasks.result.items.pages.page.checks.is_5xx_code:
                    type: boolean
                    description: >-
                      page with 5xx status codes indicates whether a page has
                      5xx response code
                  tasks.result.items.pages.page.checks.is_broken:
                    type: boolean
                    description: >-
                      broken page indicates whether a page returns a response
                      code less than 200 or greater than 400
                  tasks.result.items.pages.page.checks.is_www:
                    type: boolean
                    description: >-
                      page with www indicates whether a page is on a www
                      subdomain
                  tasks.result.items.pages.page.checks.is_https:
                    type: boolean
                    description: page with the https protocol
                  tasks.result.items.pages.page.checks.is_http:
                    type: boolean
                    description: page with the http protocol
                  tasks.result.items.pages.page.checks.high_waiting_time:
                    type: boolean
                    description: >-
                      page with high waiting time indicates whether a page
                      waiting time (aka Time to First Byte) exceeds 1.5 seconds
                  tasks.result.items.pages.page.checks.no_doctype:
                    type: boolean
                    description: >-
                      page with no doctype indicates whether a page is without
                      the declaration
                  tasks.result.items.pages.page.checks.canonical:
                    type: boolean
                    description: page is canonical
                  tasks.result.items.pages.page.checks.no_encoding_meta_tag:
                    type: boolean
                    description: >-
                      page with no meta tag encoding indicates whether a page is
                      without Content-Type; informative only if the encoding is
                      not explicit in the Content-Type header; for example:
                      Content-Type: "text/html; charset=utf8"; Note: available
                      for pages with canonical check set to true
                  tasks.result.items.pages.page.checks.no_h1_tag:
                    type: boolean
                    description: >-
                      page with empty or absent h1 tags Note: available for
                      pages with canonical check set to true
                  tasks.result.items.pages.page.checks.https_to_http_links:
                    type: boolean
                    description: >-
                      HTTPS page has links to HTTP pages if true, this HTTPS
                      page has links to HTTP pages Note: available for pages
                      with canonical check set to true
                  tasks.result.items.pages.page.checks.has_html_doctype:
                    type: boolean
                    description: >-
                      page with HTML doctype declaration if true, the page has
                      HTML DOCTYPE declaration
                  tasks.result.items.pages.page.checks.size_greater_than_3mb:
                    type: boolean
                    description: >-
                      page with size larger than 3 MB if true, the page size is
                      exceeding 3 MB; Note: available for pages with canonical
                      check set to true
                  tasks.result.items.pages.page.checks.meta_charset_consistency:
                    type: boolean
                    description: >-
                      consistency between charset encoding and page charset if
                      true, the page’s charset encoding doesn’t match the actual
                      charset of the page; Note: available for pages with
                      canonical check set to true
                  tasks.result.items.pages.page.checks.has_meta_refresh_redirect:
                    type: boolean
                    description: >-
                      pages with meta refresh redirect if true, the page has tag
                      that instructs a browser to load another page after a
                      specified time span; Note: available for pages with
                      canonical check set to true
                  tasks.result.items.pages.page.checks.has_render_blocking_resources:
                    type: boolean
                    description: >-
                      page with render-blocking resources if true, the page has
                      render-blocking scripts or stylesheets; Note: available
                      for pages with canonical check set to true
                  tasks.result.items.pages.page.checks.redirect_chain:
                    type: boolean
                    description: >-
                      page with multiple redirects if true, there were at least
                      two redirects before our crawler reached this page
                  tasks.result.items.pages.page.checks.low_content_rate:
                    type: boolean
                    description: >-
                      page with low content rate indicates whether a page has
                      the plaintext size to page size ratio of less than 0.1;
                      Note: available for pages with canonical check set to true
                  tasks.result.items.pages.page.checks.high_content_rate:
                    type: boolean
                    description: >-
                      page with high content rate indicates whether a page has
                      the plaintext size to page size ratio of more than 0.9;
                      Note: available for pages with canonical check set to true
                  tasks.result.items.pages.page.checks.low_character_count:
                    type: boolean
                    description: >-
                      indicates whether the page has less than 1024 characters
                      Note: available for pages with canonical check set to true
                  tasks.result.items.pages.page.checks.high_character_count:
                    type: boolean
                    description: >-
                      indicates whether the page has more than 256,000
                      characters Note: available for pages with canonical check
                      set to true
                  tasks.result.items.pages.page.checks.small_page_size:
                    type: boolean
                    description: >-
                      indicates whether a page is too small the value will be
                      true if a page size is smaller than 1024 bytes; Note:
                      available for pages with canonical check set to true
                  tasks.result.items.pages.page.checks.large_page_size:
                    type: boolean
                    description: >-
                      indicates whether a page is too heavy the value will be
                      true if a page size exceeds 1 megabyte; Note: available
                      for pages with canonical check set to true
                  tasks.result.items.pages.page.checks.low_readability_rate:
                    type: boolean
                    description: >-
                      page with a low readability rate indicates whether a page
                      is scored less than 15 points on the Flesch–Kincaid
                      readability test; Note: available for pages with canonical
                      check set to true
                  tasks.result.items.pages.page.checks.irrelevant_description:
                    type: boolean
                    description: >-
                      page with irrelevant description indicates whether a page
                      description tag is irrelevant to the content of a page;
                      the relevance threshold is 0.2; Note: available for pages
                      with canonical check set to true
                  tasks.result.items.pages.page.checks.irrelevant_title:
                    type: boolean
                    description: >-
                      page with irrelevant title indicates whether a page title
                      tag is irrelevant to the content of the page the relevance
                      threshold is 0.3 Note: available for pages with canonical
                      check set to true
                  tasks.result.items.pages.page.checks.irrelevant_meta_keywords:
                    type: boolean
                    description: >-
                      page with irrelevant meta keywords indicates whether a
                      page keywords tags are irrelevant to the content of a page
                      the relevance threshold is 0.6 Note: available for pages
                      with canonical check set to true
                  tasks.result.items.pages.page.checks.title_too_long:
                    type: boolean
                    description: >-
                      page with a long title indicates whether the content of
                      the title tag exceeds 65 characters; Note: available for
                      pages with canonical check set to true
                  tasks.result.items.pages.page.checks.title_too_short:
                    type: boolean
                    description: >-
                      page with short titles indicates whether the content of
                      title tag is shorter than 30 characters; Note: available
                      for pages with canonical check set to true
                  tasks.result.items.pages.page.checks.deprecated_html_tags:
                    type: boolean
                    description: >-
                      page with deprecated tags indicates whether a page has
                      deprecated HTML tags; Note: available for pages with
                      canonical check set to true
                  tasks.result.items.pages.page.checks.duplicate_meta_tags:
                    type: boolean
                    description: >-
                      page with duplicate meta tags indicates whether a page has
                      more than one meta tag of the same type; Note: available
                      for pages with canonical check set to true
                  tasks.result.items.pages.page.checks.duplicate_title_tag:
                    type: boolean
                    description: >-
                      page with more than one title tag indicates whether a page
                      has more than one title tag; Note: available for pages
                      with canonical check set to true
                  tasks.result.items.pages.page.checks.no_image_alt:
                    type: boolean
                    description: >-
                      images without alt tags Note: available for pages with
                      canonical check set to true
                  tasks.result.items.pages.page.checks.no_image_title:
                    type: boolean
                    description: >-
                      images without title tags Note: available for pages with
                      canonical check set to true
                  tasks.result.items.pages.page.checks.no_description:
                    type: boolean
                    description: >-
                      pages with no description indicates whether a page has an
                      empty or absent description meta tag; Note: available for
                      pages with canonical check set to true
                  tasks.result.items.pages.page.checks.no_title:
                    type: boolean
                    description: >-
                      page with no title indicates whether a page has an empty
                      or absent title tag; Note: available for pages with
                      canonical check set to true
                  tasks.result.items.pages.page.checks.no_favicon:
                    type: boolean
                    description: >-
                      page with no favicon Note: available for pages with
                      canonical check set to true
                  tasks.result.items.pages.page.checks.seo_friendly_url:
                    type: boolean
                    description: >-
                      page with seo-frienldy URL the ‘SEO-friendliness’ of a
                      page URL is checked by four parameters: – the length of
                      the relative path is less than 120 characters – no special
                      characters – no dynamic parameters – relevance of the URL
                      to the page if at least one of them is failed then such
                      URL is considered as not ‘SEO-friendly’; Note: available
                      for pages with canonical check set to true
                  tasks.result.items.pages.page.checks.flash:
                    type: boolean
                    description: >-
                      page with flash indicates whether a page has flash
                      elements
                  tasks.result.items.pages.page.checks.frame:
                    type: boolean
                    description: >-
                      page with frames indicates whether a page contains frame,
                      iframe, frameset tags
                  tasks.result.items.pages.page.checks.lorem_ipsum:
                    type: boolean
                    description: >-
                      page with lorem ipsum indicates whether a page has lorem
                      ipsum content; Note: available for pages with canonical
                      check set to true
                  tasks.result.items.pages.page.checks.has_misspelling:
                    type: boolean
                    description: page with misspelled content
                  tasks.result.items.pages.page.checks.seo_friendly_url_characters_check:
                    type: boolean
                    description: >-
                      URL characters check-up indicates whether a page URL
                      containing only uppercase and lowercase Latin characters,
                      digits and dashes
                  tasks.result.items.pages.page.checks.seo_friendly_url_dynamic_check:
                    type: boolean
                    description: >-
                      URL dynamic check-up the value will be true if a page has
                      no dynamic parameters in the url
                  tasks.result.items.pages.page.checks.seo_friendly_url_keywords_check:
                    type: boolean
                    description: >-
                      URL keyword check-up indicates whether a page URL is
                      consistent with the title meta tag
                  tasks.result.items.pages.page.checks.seo_friendly_url_relative_length_check:
                    type: boolean
                    description: >-
                      URL length check-up the value will be true if a page URL
                      no longer than 120 characters
                  tasks.result.items.pages.page.checks.is_orphan_page:
                    type: boolean
                    description: >-
                      page with no internal links pointing to it true if the
                      page has no reference from other pages of the domain
                  tasks.result.items.pages.page.checks.is_link_relation_conflict:
                    type: boolean
                    description: >-
                      mix of both followed and nofollowed incoming internal
                      links true if the page receives at least one link with the
                      rel="nofollow" attribute and at least one dofollow link
                  tasks.result.items.pages.page.checks.has_links_to_redirects:
                    type: boolean
                    description: >-
                      page is pointing to a page that redirect elsewhere true if
                      the page is pointing to a page that responds with a 3XX
                      redirect
                  tasks.result.items.pages.page.checks.recursive_canonical:
                    type: boolean
                    description: >-
                      recursive canonical error true if the page contains
                      rel="canonical" tag to another page, which in turn, refers
                      back to the initial page
                  tasks.result.items.pages.page.checks.canonical_chain:
                    type: boolean
                    description: >-
                      pages with canonical pointing to a page that has a
                      canonical pointing elsewhere true if the page has a
                      canonical link element pointing to a page that has a
                      canonical pointing to a different page e.g. page a is
                      canonicalized to page b, which is canonicalized to page c
                  tasks.result.items.pages.page.checks.canonical_to_redirect:
                    type: boolean
                    description: >-
                      canonical page pointing to a page that redirect elsewhere
                      true if the page has a canonical link element pointing to
                      a page that responds with a 3XX redirect
                  tasks.result.items.pages.page.checks.canonical_to_broken:
                    type: boolean
                    description: >-
                      canonical link pointing to a broken page true if the page
                      has a a canonical link pointing to a page that responds
                      with a 4xx or 5xx response codes
                  tasks.result.items.pages.page.content_encoding:
                    type: string
                    description: type of encoding
                  tasks.result.items.pages.page.media_type:
                    type: string
                    description: types of media used to display a page
                  tasks.result.items.pages.page.server:
                    type: string
                    description: server version
                  tasks.result.items.pages.page.is_resource:
                    type: boolean
                    description: indicates whether a page is a single resource
                  tasks.result.items.pages.page.last_modified:
                    type: object
                    description: >-
                      contains data on changes related to the resource if there
                      is no data, the value will be null
                  tasks.result.items.pages.page.header:
                    type: string
                    description: >-
                      date and time when the header was last modified in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00 if there is no data, the value will be
                      null
                  tasks.result.items.pages.page.sitemap:
                    type: string
                    description: >-
                      date and time when the sitemap was last modified in the
                      UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2019-11-15 12:57:46 +00:00 if there is no data, the value
                      will be null
                  tasks.result.items.pages.page.meta_tag:
                    type: string
                    description: >-
                      date and time when the meta tag was last modified in the
                      UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example:
                      2019-11-15 12:57:46 +00:00 if there is no data, the value
                      will be null
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