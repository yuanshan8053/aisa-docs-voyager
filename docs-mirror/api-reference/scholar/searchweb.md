> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Search

> Search the web



## OpenAPI

````yaml openapi/platform-txyz-openapi.json POST /scholar/search/web
openapi: 3.0.0
info:
  title: TXYZ Platform API
  version: 1.0.0
  description: >-
    API documentation for platform.txyz.ai services including academic search
    functionality
  contact:
    email: support@txyz.ai
  license:
    name: Proprietary
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /scholar/search/web:
    post:
      tags:
        - Search
        - Web
      summary: Search the web
      description: Perform web search and return structured results
      operationId: searchWeb
      parameters:
        - name: query
          in: query
          required: true
          description: Search query for scholarly materials
          schema:
            type: string
            example: machine learning
        - name: max_num_results
          in: query
          description: Maximum number of search results to return, up to 100
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 10
        - name: as_ylo
          in: query
          description: Year of publication lower bound
          schema:
            type: integer
            nullable: true
            minimum: 1900
            maximum: 2030
        - name: as_yhi
          in: query
          description: Year of publication upper bound
          schema:
            type: integer
            nullable: true
            minimum: 1900
            maximum: 2030
      requestBody:
        required: false
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                query:
                  type: string
      responses:
        '200':
          description: Successful search response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WebSearchResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '429':
          $ref: '#/components/responses/TooManyRequests'
        '500':
          $ref: '#/components/responses/InternalError'
      security:
        - BearerAuth: []
components:
  schemas:
    WebSearchResponse:
      type: object
      required:
        - id
        - results
      properties:
        id:
          type: string
          description: Unique identifier for the search request
        results:
          type: array
          items:
            $ref: '#/components/schemas/WebResult'
          description: List of web search results
    WebResult:
      type: object
      required:
        - title
        - link
        - snippet
      properties:
        title:
          type: string
          description: Title of the web page
        link:
          type: string
          format: uri
          description: URL to access the web page
        snippet:
          type: string
          description: Brief summary or preview of the web page content
        display_url:
          type: string
          description: Display-friendly URL
        published_date:
          type: string
          format: date-time
          description: Publication date of the web page
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Error message describing what went wrong
        code:
          type: integer
          description: HTTP status code
        details:
          type: string
          description: Additional error details
  responses:
    BadRequest:
      description: Bad request - invalid parameters
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Unauthorized:
      description: Unauthorized - invalid or missing API key
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    TooManyRequests:
      description: Rate limit exceeded
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalError:
      description: Internal server error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````