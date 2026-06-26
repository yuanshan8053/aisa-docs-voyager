> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting Google Shopping Sellers Tasks

> Google Shopping Sellers endpoint will provide you with the list of sellers that listed the specified product on Google Shopping.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/merchant/google/sellers/task_post
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
  /dataforseo/merchant/google/sellers/task_post:
    post:
      summary: Setting Google Shopping Sellers Tasks
      description: >-
        Google Shopping Sellers endpoint will provide you with the list of
        sellers that listed the specified product on Google Shopping. The
        provided data for each seller includes related product base and total
        price, shipment and purchase details and special offers. The results are
        specific to the selected location (see [the List of
        Locations](https://docs.dataforseo.com/v3/merchant/google/locations.md))
        and language (see [the List of
        Languages](https://docs.dataforseo.com/v3/merchant/google/languages.md))
        settings.
      operationId: post_dataforseo_merchant_google_sellers_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                product_id:
                  type: string
                  description: >-
                    unique product identifier on Google Shopping required field
                    if data_docid or gid is not specified we recommend
                    specifying product_id together with data_docid and gid for
                    optimal results; you can get this value for a certain
                    product by making a separate request to the Google Shopping
                    Products endpoint example: 4485466949985702538 learn more
                    about the parameter in this help center guide
                data_docid:
                  type: string
                  description: >-
                    unique identifier of the SERP data element required field if
                    product_id or gid is not specified we recommend specifying
                    data_docid together with product_id and gid for optimal
                    results; you can get this value for a certain element by
                    making a separate request to the Google Shopping Products
                    endpoint example: 13071766526042404278
                gid:
                  type: string
                  description: >-
                    global product identifier on Google Shopping required field
                    if product_id or data_docid is not specified we recommend
                    specifying gid together with product_id and data_docid for
                    optimal results; you can get this value for a certain
                    product by making a separate request to the Google Shopping
                    Products endpoint example: 4702526954592161872 learn more
                    about the parameter in this help center guide
                pvf:
                  type: string
                  description: >-
                    product variant filter on Google Shopping optional field
                    parameter in Google Shopping URL, setting optional product
                    variant filtration; example:
                    Eg4iBWNvbG9yKgV3aGl0ZRISIgxwYWNrYWdlIHNpemUqAjE0EgoiBHNpemUqAnhs
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
                depth:
                  type: integer
                  description: >-
                    parsing depth optional field number of results to be
                    retrieved from Google Shopping SERP default value: 10 max
                    value: 200 your account will be billed per each SERP
                    containing up to 10 results; setting depth above 10 may
                    result in additional charges if the search engine returns
                    more than 10 results; the cost can be calculated on the
                    Pricing page
                se_domain:
                  type: string
                  description: >-
                    search engine domain optional field we choose the relevant
                    search engine domain automatically according to the location
                    and language you specify however, you can set a custom
                    search engine domain in this field example: google.co.uk,
                    google.com.au, google.de, etc.
                get_shops_on_google:
                  type: boolean
                  description: >-
                    include “buy on Google” shops optional field if set to true,
                    the response will contain the list of sellers that allow to
                    purchase a given product directly on Google Note: if set to
                    true, the cost of a task will be doubled
                additional_specifications:
                  type: object
                  description: >-
                    object containing additional url parameters you can get
                    additional information about the product by using the
                    "additional_specifications object, which you can get by
                    making a separate request to the Google Shopping Products
                    endpoint example: "additional_specifications": { "eto":
                    "16157121050167572763_0" }
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
                - product_id
                - data_docid
                - gid
                - location_name
                - location_code
                - location_coordinate
                - language_name
                - language_code
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