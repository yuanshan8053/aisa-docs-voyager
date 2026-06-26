> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tavily Extract

> Extract web page content from specified URLs using Tavily Extract.



## OpenAPI

````yaml openapi/tavily.json POST /tavily/extract
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
  /tavily/extract:
    post:
      tags:
        - https://docs.tavily.com/documentation/api-reference/endpoint/extract
      summary: Extract web page content from specified URLs using Tavily Extract.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                urls:
                  type: array
                  items:
                    type: string
                  description: The URLs to extract content from.
                  example:
                    - https://en.wikipedia.org/wiki/Artificial_intelligence
                query:
                  type: string
                  description: User intent for reranking extracted content chunks.
                chunks_per_source:
                  type: integer
                  default: 3
                  description: Maximum number of relevant chunks returned per source.
                  minimum: 1
                  maximum: 5
                extract_depth:
                  type: string
                  enum:
                    - basic
                    - advanced
                  default: basic
                  description: Depth of the extraction process.
                include_images:
                  type: boolean
                  default: false
                  description: Include a list of images extracted from the URLs.
                include_favicon:
                  type: boolean
                  default: false
                  description: Include the favicon URL for each result.
                format:
                  type: string
                  enum:
                    - markdown
                    - text
                  default: markdown
                  description: Format of the extracted web page content.
                timeout:
                  type: number
                  format: float
                  description: Maximum time in seconds to wait for the URL extraction.
                  minimum: 1
                  maximum: 60
                include_usage:
                  type: boolean
                  default: false
                  description: Include credit usage information in the response.
              required:
                - urls
      responses:
        '200':
          description: Extraction results returned successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        url:
                          type: string
                          description: URL of the extracted content.
                        raw_content:
                          type: string
                          description: Extracted raw content from the URL.
                        favicon:
                          type: string
                          description: Favicon URL of the extracted content.
                  failed_results:
                    type: array
                    items:
                      type: string
                    description: List of URLs that could not be processed.
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