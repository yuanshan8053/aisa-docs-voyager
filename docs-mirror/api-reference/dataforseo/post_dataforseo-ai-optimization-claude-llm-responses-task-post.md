> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting LLM Responses Claude Tasks

> Claude LLM Responses endpoint allows you to retrieve structured responses from a specific Claude model, based on the input parameters.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/ai_optimization/claude/llm_responses/task_post
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
  /dataforseo/ai_optimization/claude/llm_responses/task_post:
    post:
      summary: Setting LLM Responses Claude Tasks
      description: >-
        Claude LLM Responses endpoint allows you to retrieve structured
        responses from a specific Claude model, based on the input parameters.
      operationId: post_dataforseo_ai_optimization_claude_llm_responses_task_post
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                user_prompt:
                  type: string
                  description: >-
                    prompt for the AI model required field the question or task
                    you want to send to the AI model; you can specify up to 500
                    characters in the user_prompt field
                model_name:
                  type: string
                  description: >-
                    name of the AI model required field model_nameconsists of
                    the actual model name and version name; if the basic model
                    name is specified, its latest version will be set by
                    default; for example, if claude-opus-4-0 is specified, the
                    claude-opus-4-20250514 will be set as model_name
                    automatically; you can receive the list of available LLM
                    models by making a separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/claude/llm_responses/models
                max_output_tokens:
                  type: integer
                  description: >-
                    maximum number of tokens in the AI response optional field
                    minimum value: 1; maximum value: 4096; default value: 2048;
                    Note: if web_search is set to true or the reasoning model is
                    specified in the request, the output token count may exceed
                    the specified max_output_tokens limit Note #2: if
                    use_reasoning is set to true, the minimum value for
                    max_output_tokens is 1025
                temperature:
                  type: number
                  description: >-
                    randomness of the AI response optional field higher values
                    make output more diverse; lower values make output more
                    focused; minimum value: 0 maximum value: 1 default value:
                    0.7Note: temperature cannot be used together with top_p in
                    the same request
                top_p:
                  type: number
                  description: >-
                    diversity of the AI response optional field controls
                    diversity of the response by limiting token selection;
                    minimum value: 0 maximum value: 1 default value: nullNote:
                    top_p cannot be used together with temperature in the same
                    request
                web_search:
                  type: boolean
                  description: >-
                    enable web search for current information optional field
                    when enabled, the AI model can access and cite current web
                    information; Note: refer to the Models endpoint for a list
                    of models that support web_search; default value: false; The
                    cost of the parameter can be calculated on the Pricing page
                force_web_search:
                  type: boolean
                  description: >-
                    force AI agent to use web search optional field to enable
                    this parameter, web_search must also be enabled; when
                    enabled, the AI model is forced to access and cite current
                    web information; default value: false; Note: even if the
                    parameter is set to true, there is no guarantee web sources
                    will be cited in the response
                web_search_country_iso_code:
                  type: string
                  description: >-
                    ISO country code of the location optional field possible
                    values:
                    'AR','AT','AU','BE','BR','CA','CH','CL','CN','DE','DK','ES','FI','FR','GB','HK','ID','IN','IT','JP','KR','MX','MY','NL','NO','NZ','PH','PL','PT','RU','SA','SE','TR','TW','US','ZA'
                web_search_city:
                  type: string
                  description: >-
                    city name of the location optional field Note: specify
                    web_search_country_iso_code to use this parameter
                system_message:
                  type: string
                  description: >-
                    instructions for the AI behaviour optional field defines the
                    AI's role, tone, or specific behavior; you can specify up to
                    500 characters in the system_message field
                message_chain:
                  type: array
                  items:
                    type: string
                  description: >-
                    conversation history optional field array of message objects
                    representing previous conversation turns; each object must
                    contain role and message parameters: role string with either
                    user or ai role; message string with message content (max
                    500 characters); you can specify the maximum of 10 message
                    objects in the array; example: "message_chain":
                    [{"role":"user","message":"Hello, what’s
                    up?"},{"role":"ai","message":"Hello! I’m doing well, thank
                    you. How can I assist you today?"}]
                use_reasoning:
                  type: boolean
                  description: >-
                    enable reasoning for the AI model optional field when
                    enabled, the model will perform reasoning before generating
                    a response refer to the Models endpoint for a list of models
                    that support reasoning default value: false Note: if set to
                    true, the minimum value for max_output_tokens is 1025 Note
                    #2: if set to true, force_web_search must be set to false
                    Note #3: if set to true, the temperature and top_p cannot be
                    used
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
                    special character in postback_url will be urlencoded; i.a.,
                    the # character will be encoded into %23learn more on our
                    Help Center
                pingback_url:
                  type: string
                  description: >-
                    notification URL of a completed task optional field when a
                    task is completed we will notify you by GET request sent to
                    the URL you have specified you can use the ‘$id’ string as a
                    $id variable and ‘$tag’ as urlencoded $tag variable. We will
                    set the necessary values before sending the request example:
                    http://your-server.com/pingscript?id=$id
                    http://your-server.com/pingscript?id=$id&tag=$tag Note:
                    special character in pingback_url will be urlencoded; i.a.,
                    the # character will be encoded into %23learn more on our
                    Help Center
              required:
                - user_prompt
                - model_name
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
                      unique task identifier in our system unique task
                      identifier in the UUID format
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