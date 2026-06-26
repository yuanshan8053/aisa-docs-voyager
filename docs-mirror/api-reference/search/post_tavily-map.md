> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tavily Map

> Generate comprehensive site maps using Tavily Map.



## OpenAPI

````yaml openapi/tavily.json POST /tavily/map
openapi: 3.0.0
info:
  title: Tavily API
  version: 1.0.0
  description: >-
    Unified API documentation for Tavily endpoints including Search, Extract,
    Crawl, and Map.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - bearerAuth: []
paths:
  /tavily/map:
    post:
      tags:
        - https://docs.tavily.com/documentation/api-reference/endpoint/map
      summary: Generate comprehensive site maps using Tavily Map.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  description: The root URL to begin the mapping.
                  example: docs.tavily.com
                instructions:
                  type: string
                  description: Natural language instructions for the crawler.
                max_depth:
                  type: integer
                  default: 1
                  description: Max depth of the mapping.
                  minimum: 1
                  maximum: 5
                max_breadth:
                  type: integer
                  default: 20
                  description: Max number of links to follow per level of the tree.
                  minimum: 1
                  maximum: 500
                limit:
                  type: integer
                  default: 50
                  description: >-
                    Total number of links the crawler will process before
                    stopping.
                  minimum: 1
                select_paths:
                  type: array
                  items:
                    type: string
                  description: >-
                    Regex patterns to select only URLs with specific path
                    patterns.
                select_domains:
                  type: array
                  items:
                    type: string
                  description: >-
                    Regex patterns to select crawling to specific domains or
                    subdomains.
                exclude_paths:
                  type: array
                  items:
                    type: string
                  description: Regex patterns to exclude URLs with specific path patterns.
                exclude_domains:
                  type: array
                  items:
                    type: string
                  description: >-
                    Regex patterns to exclude specific domains or subdomains
                    from mapping.
                allow_external:
                  type: boolean
                  default: true
                  description: Include external domain links in the final results list.
                timeout:
                  type: number
                  format: float
                  default: 150
                  description: Maximum time in seconds to wait for the map operation.
                  minimum: 10
                  maximum: 150
                include_usage:
                  type: boolean
                  default: false
                  description: Include credit usage information in the response.
              required:
                - url
      responses:
        '200':
          description: Map results returned successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  base_url:
                    type: string
                    description: The base URL that was mapped.
                  results:
                    type: array
                    items:
                      type: string
                      description: URLs discovered during the mapping.
                  response_time:
                    type: number
                    format: float
                    description: Time in seconds it took to complete the request.
                  usage:
                    type: object
                    properties:
                      credits:
                        type: integer
                        description: Credit usage details for the request.
                  request_id:
                    type: string
                    description: Unique request identifier.
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````