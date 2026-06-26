> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tavily Crawl

> Graph-based website traversal tool using Tavily Crawl.



## OpenAPI

````yaml openapi/tavily.json POST /tavily/crawl
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
  /tavily/crawl:
    post:
      tags:
        - https://docs.tavily.com/documentation/api-reference/endpoint/crawl
      summary: Graph-based website traversal tool using Tavily Crawl.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                url:
                  type: string
                  description: The root URL to begin the crawl.
                  example: docs.tavily.com
                instructions:
                  type: string
                  description: Natural language instructions for the crawler.
                chunks_per_source:
                  type: integer
                  default: 3
                  description: Maximum number of relevant chunks returned per source.
                  minimum: 1
                  maximum: 5
                max_depth:
                  type: integer
                  default: 1
                  description: Max depth of the crawl.
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
                    from crawling.
                allow_external:
                  type: boolean
                  default: true
                  description: Include external domain links in the final results list.
                include_images:
                  type: boolean
                  default: false
                  description: Include images in the crawl results.
                extract_depth:
                  type: string
                  enum:
                    - basic
                    - advanced
                  default: basic
                  description: Depth of the extraction process.
                format:
                  type: string
                  enum:
                    - markdown
                    - text
                  default: markdown
                  description: Format of the extracted web page content.
                include_favicon:
                  type: boolean
                  default: false
                  description: Include the favicon URL for each result.
                timeout:
                  type: number
                  format: float
                  default: 150
                  description: Maximum time in seconds to wait for the crawl operation.
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
          description: Crawl results returned successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  base_url:
                    type: string
                    description: The base URL that was crawled.
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                          description: URL of the crawled page.
                        raw_content:
                          type: string
                          description: Extracted raw content from the page.
                        favicon:
                          type: string
                          description: Favicon URL of the crawled page.
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