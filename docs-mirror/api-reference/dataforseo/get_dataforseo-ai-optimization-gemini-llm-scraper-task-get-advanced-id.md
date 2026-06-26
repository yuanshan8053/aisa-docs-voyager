> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Gemini LLM Scraper Advanced

> ![checked](https://docs.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/ai_optimization/gemini/llm_scraper/task_get/advanced/{id}
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
  /dataforseo/ai_optimization/gemini/llm_scraper/task_get/advanced/{id}:
    get:
      summary: Get Gemini LLM Scraper Advanced
      description: >-
        ![checked](https://docs.dataforseo.com/v3/wp-content/themes/dataforseo/assets/img/icons/checked-circle.svg)
        GET
        https://api.dataforseo.com/v3/ai\_optimization/gemini/llm\_scraper/task\_get/advanced/$id
      operationId: get_dataforseo_ai_optimization_gemini_llm_scraper_task_get_advanced_id
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
                      task identifier a universally unique identifier (UUID)
                      unique task identifier in our system you will be able to
                      use it within 30 days to request the results of the task
                      at any time
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