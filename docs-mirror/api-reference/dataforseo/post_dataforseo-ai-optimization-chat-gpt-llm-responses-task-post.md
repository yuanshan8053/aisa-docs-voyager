> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting ‘LLM Responses ChatGPT’ Tasks

> ChatGPT LLM Responses endpoint allows you to retrieve structured responses from a specific ChatGPT model, based on the input parameters.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/ai_optimization/chat_gpt/llm_responses/task_post
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
  /dataforseo/ai_optimization/chat_gpt/llm_responses/task_post:
    post:
      summary: Setting ‘LLM Responses ChatGPT’ Tasks
      description: >-
        ChatGPT LLM Responses endpoint allows you to retrieve structured
        responses from a specific ChatGPT model, based on the input parameters.
      operationId: post_dataforseo_ai_optimization_chat_gpt_llm_responses_task_post
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
                    default; for example, if gpt-4.1 is specified, the
                    gpt-4.1-2025-04-14 will be set as model_name automatically;
                    you can receive the list of available LLM models by making a
                    separate request to the
                    https://api.dataforseo.com/v3/ai_optimization/chat_gpt/llm_responses/models
                max_output_tokens:
                  type: integer
                  description: >-
                    maximum number of tokens in the AI response optional field
                    minimum value for reasoning models (e.g., reasoning is true
                    in the Models endpoint): 1024; minimum value for
                    non-reasoning models: 16; maximum value: 4096; default
                    value: 2048
                temperature:
                  type: number
                  description: >-
                    randomness of the AI response optional field higher values
                    make output more diverse; lower values make output more
                    focused; minimum value: 0 maximum value: 2 default value:
                    0.94 Note: not supported in reasoning models
                top_p:
                  type: number
                  description: ''
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
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data array of the response
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