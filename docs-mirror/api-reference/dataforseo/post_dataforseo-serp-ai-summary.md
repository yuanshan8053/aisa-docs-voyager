> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SERP API AI Summary

> The Live SERP API AI Summary endpoint provides a summary of the content found on any SERP and generates a response based on the user prompt.



## OpenAPI

````yaml openapi/dataforseo.json POST /dataforseo/serp/ai_summary
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
  /dataforseo/serp/ai_summary:
    post:
      summary: SERP API AI Summary
      description: >-
        The Live SERP API AI Summary endpoint provides a summary of the content
        found on any SERP and generates a response based on the user prompt.
        Your account is charged for each request.
      operationId: post_dataforseo_serp_ai_summary
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                task_id:
                  type: string
                  description: >-
                    Unique identifier of the associated task in UUID format; can
                    be used within 30 days
                prompt:
                  type: string
                  description: Additional AI prompt; maximum 2000 characters
                support_extra:
                  type: boolean
                  description: >-
                    Whether to consider extra SERP features such as answer_box,
                    knowledge_graph, and featured_snippet; default true
                fetch_content:
                  type: boolean
                  description: Whether to fetch content from pages in SERPs; default false
                include_links:
                  type: boolean
                  description: >-
                    Whether to include source links in the summary; default
                    false
              required:
                - task_id
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
                    description: The current version of the API
                  status_code:
                    type: integer
                    description: General status code
                  status_message:
                    type: string
                    description: General informational message
                  time:
                    type: string
                    description: Execution time, seconds
                  cost:
                    type: number
                    description: Total task cost, USD
                  tasks:
                    type: array
                    items:
                      type: string
                    description: Array of tasks
                  tasks[].id:
                    type: string
                    description: Task identifier in UUID format
                  tasks[].status_code:
                    type: integer
                    description: Task status code
                  tasks[].status_message:
                    type: string
                    description: Task status message
                  tasks[].result_count:
                    type: integer
                    description: Number of elements in the result array
                  tasks[].path:
                    type: array
                    items:
                      type: string
                    description: URL path
                  tasks[].data:
                    type: object
                    description: Contains the same parameters specified in the POST request
                  tasks[].result:
                    type: array
                    items:
                      type: string
                    description: Array of results
                  tasks[].result[].items_count:
                    type: integer
                    description: Number of items in the result array
                  tasks[].result[].items:
                    type: array
                    items:
                      type: string
                    description: Items array
                  tasks[].result[].items[].summary:
                    type: string
                    description: Generated summary
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