> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Google Shopping Products Tasks

> Google Shopping Products endpoint will provide you with the list of products found on Google Shopping for the specified query.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/merchant/google/products/task_post
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
  /dataforseo/merchant/google/products/task_post:
    post:
      summary: Setting Google Shopping Products Tasks
      description: >-
        Google Shopping Products endpoint will provide you with the list of
        products found on Google Shopping for the specified query. The results
        include product title, description in Google Shopping SERP, product
        rank, price, reviews and rating as well as the related domain.
      operationId: post_dataforseo_merchant_google_products_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                keyword:
                  type: string
                  description: >-
                    keyword required field you can specify up to 700 characters
                    in the keyword filed all %## will be decoded (plus character
                    ‘+’ will be decoded to a space character) if you need to use
                    the “%” character for your keyword, please specify it as
                    “%25”; learn more about rules and limitations of keyword and
                    keywords fields in DataForSEO APIs in this Help Center
                    article
                url:
                  type: string
                  description: >-
                    direct URL of the search query optional field you can
                    specify a direct URL and we will sort it out to the
                    necessary fields. Note that this method is the most
                    difficult for our API to process and also requires you to
                    specify the exact language and location in the URL. In most
                    cases, we wouldn’t recommend using this method. example:
                    https://www.google.com/search?q=fish&hl=en&gl=US&gws_rd=cr&uule=w+CAIQIFISCQs2MuSEtepUEUK33kOSuTsc
                priority:
                  type: integer
                  description: >-
                    task priority optional field can take the following values:
                    1 – normal execution priority (set by default) 2 – high
                    execution priority You will be additionally charged for the
                    tasks with high execution priority. The cost can be
                    calculated on the Pricing page.
                location_name:
                  type: string
                  description: >-
                    full name of the location required field if you don’t
                    specify location_code or location_coordinate if you use this
                    field, you don’t need to specify location_code or
                    location_coordinate you can receive the list of available
                    Google Shopping locations with their location_name by making
                    a separate request to the
                    https://api.dataforseo.com/v3/merchant/google/locations
                    example: London,England,United Kingdom
                location_code:
                  type: integer
                  description: >-
                    location code required field if you don’t specify
                    location_name or location_coordinate if you use this field,
                    you don’t need to specify location_name or
                    location_coordinate you can receive the list of available
                    Google Shopping locations with their location_code by making
                    a separate request to the
                    https://api.dataforseo.com/v3/merchant/google/locations
                    example: 2840
                location_coordinate:
                  type: string
                  description: >-
                    GPS coordinates of a location required field if you don’t
                    specify location_name or location_code if you use this
                    field, you don’t need to specify location_name or
                    location_code location_coordinate parameter should be
                    specified in the “latitude,longitude,radius” format the
                    maximum number of decimal digits for “latitude” and
                    “longitude”: 7 the minimum value for “radius”: 199.9
                    example: 53.476225,-2.243572,200
                language_name:
                  type: string
                  description: >-
                    full name of the language required field if you don’t
                    specify language_code if you use this field, you don’t need
                    to specify language_code you can receive the list of
                    available Google Shopping languages with their language_name
                    by making a separate request to the
                    https://api.dataforseo.com/v3/merchant/google/languages
                    example: English
                language_code:
                  type: string
                  description: >-
                    language code required field if you don’t specify
                    language_name if you use this field, you don’t need to
                    specify language_name you can receive the list of available
                    Google Shopping languages with their language_code by making
                    a separate request to the
                    https://api.dataforseo.com/v3/merchant/google/languages
                    example: en
                se_domain:
                  type: string
                  description: >-
                    search engine domain optional field we choose the relevant
                    search engine domain automatically according to the location
                    and language you specify however, you can set a custom
                    search engine domain in this field example: google.co.uk,
                    google.com.au, google.de, etc.
                depth:
                  type: integer
                  description: >-
                    parsing depth optional field number of results to be
                    retrieved from Google Shopping SERP default value: 40 max
                    value: 120 Your account will be billed per each SERP
                    containing up to 40 results; Setting depth above 40 may
                    result in additional charges if the search engine returns
                    more than 40 results; The cost can be calculated on the
                    Pricing page.
                max_crawl_pages:
                  type: integer
                  description: >-
                    page crawl limit optional field number of search results
                    pages to crawl max value: 7 Note: the max_crawl_pages and
                    depth parameters complement each other; learn more at our
                    help center
                search_param:
                  type: string
                  description: >-
                    additional parameters of the search query optional field you
                    can use the following search URL parameters for customizing
                    the search; example: &tbs=ppr_min:45 – search for products
                    that cost more than 45 USD; &tbs=ppr_max:50 – search for
                    products that cost less than 50 USD; &tbs=p_ord:p – sort by
                    ascending price; &tbs=p_ord:pd – sort by descending price;
                    &tbs=p_ord:rv – sort by review score;
                    &tbs=ppr_max:50,p_ord:rv – sort by review score with the
                    maximum price of 50 USD.; &udm=28 – use new Google Shopping
                    markup with 40 SERP results returned by default (the cost
                    for one SERP is deducted accordingly); the maximum depth is
                    200; this parameter must be specified without tbm=shop in
                    the url; &shoprs=$value – specify advanced filtering and
                    sorting in the new Shopping markup; replace $value with a
                    string in protobuf Base64 format; learn more on our help
                    center. Note that search_param values will be ignored if any
                    of the following parameters are used: price_min, price_max,
                    sort_by
                price_min:
                  type: integer
                  description: >-
                    minimum product price optional field minimum price of the
                    returned products listed on Google Shopping for the
                    specified query example: 5 Note: if you specify price_min,
                    the search_param parameter will be ignored
                price_max:
                  type: integer
                  description: >-
                    maximum product price optional field maximum price of the
                    returned products listed on Google Shopping for the
                    specified query example: 100 Note: if you specify price_max,
                    the search_param parameter will be ignored
                sort_by:
                  type: string
                  description: >-
                    results sorting rules optional field the following sorting
                    rules are supported: review_score, price_low_to_high,
                    price_high_to_low example: sort_by:"review_score" Note: if
                    you specify sort_by, the search_param parameter will be
                    ignored
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
                postback_url:
                  type: string
                  description: >-
                    URL for sending task results optional field once the task is
                    completed, we will send a POST request with its results
                    compressed in the gzip format to the postback_url you
                    specified you can use the ‘$id’ string as a $id variable and
                    ‘$tag’ as urlencoded $tag variable. We will set the
                    necessary values before sending the request. example:
                    http://your-server.com/postbackscript?id=$id
                    http://your-server.com/postbackscript?id=$id&tag=$tag Note:
                    special characters in postback_url will be urlencoded; i.a.,
                    the # character will be encoded into %23 learn more on our
                    Help Center
                postback_data:
                  type: string
                  description: >-
                    postback_url datatype required field if you specify
                    postback_url corresponds to the datatype that will be sent
                    to your server possible values: advanced, html
                pingback_url:
                  type: string
                  description: >-
                    notification URL of a completed task optional field when a
                    task is completed we will notify you by GET request sent to
                    the URL you have specified you can use the ‘$id’ string as a
                    $id variable and ‘$tag’ as urlencoded $tag variable. We will
                    set the necessary values before sending the request.
                    example: http://your-server.com/pingscript?id=$id
                    http://your-server.com/pingscript?id=$id&tag=$tag Note:
                    special characters in pingback_url will be urlencoded; i.a.,
                    the # character will be encoded into %23 learn more on our
                    Help Center
              required:
                - keyword
                - location_name
                - location_code
                - location_coordinate
                - language_name
                - language_code
                - postback_data
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
                    description: the number of tasks in the tasksarray
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
                      unique task identifier in our system in the Universally
                      unique identifier (UUID) format
                  tasks.status_code:
                    type: integer
                    description: >-
                      status code of the task generated by DataForSEO; can be
                      within the following range: 10000-60000
                  tasks.status_message:
                    type: string
                    description: informational message of the task
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
                    description: array of results in this case, the value will be null
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