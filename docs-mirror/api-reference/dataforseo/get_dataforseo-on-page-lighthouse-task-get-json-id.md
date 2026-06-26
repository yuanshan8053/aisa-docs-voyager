> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Lighthouse Results by ID

> The OnPage Lighthouse API is based on Google’s open-source Lighthouse project for measuring the quality of web pages and web apps.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/on_page/lighthouse/task_get/json/{id}
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
  /dataforseo/on_page/lighthouse/task_get/json/{id}:
    get:
      summary: Get Lighthouse Results by ID
      description: >-
        The OnPage Lighthouse API is based on Google’s open-source Lighthouse
        project for measuring the quality of web pages and web apps. This
        endpoint will provide you with the results of Lighthouse Audit. Use the
        `id` received in the response of your [Task
        POST](https://docs.dataforseo.com/v3/on_page/lighthouse/task_post.md)
        request to get the results. The response will include data about all
        categories and audits specified in the Task POST. By default, the
        response will include all available data about the webpage including its
        performance, accessibility, progressive web apps, SEO, and compliance
        with best practices.
      operationId: get_dataforseo_on_page_lighthouse_task_get_json_id
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
                      task identifier required field you can get this ID in the
                      response of the Task POST endpoint example:
                      “07131248-1535-0216-1000-17384017ad04”
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