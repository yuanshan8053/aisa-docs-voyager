> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get LLM Responses Gemini Results by id

> Gemini LLM Responses endpoint allows you to retrieve structured responses from a specific Gemini model, based on the input parameters.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/ai_optimization/gemini/llm_responses/task_get/{id}
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
  /dataforseo/ai_optimization/gemini/llm_responses/task_get/{id}:
    get:
      summary: Get LLM Responses Gemini Results by id
      description: >-
        Gemini LLM Responses endpoint allows you to retrieve structured
        responses from a specific Gemini model, based on the input parameters.
      operationId: get_dataforseo_ai_optimization_gemini_llm_responses_task_get_id
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: >-
                      task identifier unique task identifier in our system in
                      the UUID format you will be able to use it within 30 days
                      to request the results of the task at any time
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