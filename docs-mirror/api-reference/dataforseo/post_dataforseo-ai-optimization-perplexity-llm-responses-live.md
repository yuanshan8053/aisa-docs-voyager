> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Live Perplexity LLM Responses

> Live Perplexity LLM Responses endpoint allows you to retrieve structured responses from a specific Perplexity AI model, based on the input parameters.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/ai_optimization/perplexity/llm_responses/live
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
  /dataforseo/ai_optimization/perplexity/llm_responses/live:
    post:
      summary: Live Perplexity LLM Responses
      description: >-
        Live Perplexity LLM Responses endpoint allows you to retrieve structured
        responses from a specific Perplexity AI model, based on the input
        parameters.
      operationId: post_dataforseo_ai_optimization_perplexity_llm_responses_live
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
                    default; you can receive the list of available LLM models by
                    making a separate request to the following endpoint:
                    https://api.dataforseo.com/v3/ai_optimization/perplexity/llm_responses/models
                max_output_tokens:
                  type: integer
                  description: >-
                    maximum number of tokens in the AI response optional field
                    minimum value: 1 maximum value: 4096; default value: 2048;
                    Note: if the reasoning model is specified in the request,
                    the output token count may exceed the specified
                    max_output_tokens limit
                temperature:
                  type: number
                  description: >-
                    randomness of the AI response optional field higher values
                    make output more diverse lower values make output more
                    focused minimum value: 0 maximum value: 1.9 default value:
                    0.77
                top_p:
                  type: number
                  description: >-
                    diversity of the AI response optional field controls
                    diversity of the response by limiting token selection
                    minimum value: 0 maximum value: 1 default value: 0.9
                web_search_country_iso_code:
                  type: string
                  description: >-
                    country code for web search localization optional field
                    specify the country ISO code to get localized web search
                    results Note: available only for Perplexity Sonar models
                    example: US
                system_message:
                  type: string
                  description: >-
                    instructions for the AI behavior optional field defines the
                    AI's role, tone, or specific behavior you can specify up to
                    500 characters in the system_message field
                message_chain:
                  type: array
                  items:
                    type: string
                  description: >-
                    conversation history optional field array of message objects
                    representing previous conversation turns; each object must
                    contain: role string with either user or ai role; message
                    string with message content (max 500 characters); you can
                    specify maximum of 10 message objects in the array; Note:
                    for Perplexity models, messages must strictly alternate
                    between user and AI roles (user → ai); example:
                    "message_chain": [{"role":"user","message":"Hello, what’s
                    up?"},{"role":"ai","message":"Hello! I’m doing well, thank
                    you. How can I assist you today?"}]
                tag:
                  type: string
                  description: >-
                    user-defined task identifier optional field the character
                    limit is 255 you can use this parameter to identify the task
                    and match it with the result you will find the specified tag
                    value in the data object of the response
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
                    description: >-
                      cost of the task, USD includes the base task price plus
                      the money_spent value
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
                  tasks.result.model_name:
                    type: string
                    description: name of the AI model used
                  tasks.result.input_tokens:
                    type: integer
                    description: >-
                      number of tokens in the input total count of tokens
                      processed
                  tasks.result.output_tokens:
                    type: integer
                    description: >-
                      number of tokens in the output total count of tokens
                      generated in the AI response
                  tasks.result.web_search:
                    type: boolean
                    description: >-
                      indicates if web search was used Note: web search is
                      enabled by default in Perplexity Sonar models
                  tasks.result.money_spent:
                    type: number
                    description: >-
                      cost of AI tokens, USD the price charged by the
                      third-party AI model provider for according to its Pricing
                  tasks.result.datetime:
                    type: string
                    description: >-
                      date and time when the result was received in the UTC
                      format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15
                      12:57:46 +00:00
                  tasks.result.items:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of response items contains structured AI response
                      data
                  tasks.result.items.type:
                    type: string
                    description: type of the element = 'message'
                  tasks.result.items.sections:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of content sections contains different parts of the
                      AI response
                  tasks.result.items.sections.type:
                    type: string
                    description: type of element='text'
                  tasks.result.items.sections.text:
                    type: string
                    description: AI-generated text content
                  tasks.result.items.sections.annotations:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of references used to generate the response equals
                      null if the web_search parameter is not set to true Note:
                      annotations may return empty even when web_search is true,
                      as the AI will attempt to retrieve web information but may
                      not find relevant results
                  tasks.result.items.sections.annotations.title:
                    type: string
                    description: the domain name or title of the quoted source
                  tasks.result.items.sections.annotations.url:
                    type: string
                    description: URL of the quoted source
                  tasks.result.fan_out_queries:
                    type: array
                    items:
                      type: string
                    description: >-
                      array of fan-out queries contains related search queries
                      derived from the main query to provide a more
                      comprehensive response
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