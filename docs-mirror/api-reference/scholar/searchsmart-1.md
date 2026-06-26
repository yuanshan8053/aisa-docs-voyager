> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Search

> Smart search combining web and academic results



## OpenAPI

````yaml openapi/platform-txyz-openapi.json POST /scholar/search/mixed
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
  /scholar/search/mixed:
    post:
      tags:
        - Search
        - Smart
      summary: Smart search combining web and academic results
      description: Perform intelligent search that combines web and academic results
      operationId: searchSmart
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
                $ref: '#/components/schemas/SmartSearchResponse'
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
    SmartSearchResponse:
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
            $ref: '#/components/schemas/SmartResult'
          description: List of smart search results combining web and academic content
        search_type:
          type: string
          enum:
            - web
            - academic
            - hybrid
          description: Type of search results included
    SmartResult:
      type: object
      required:
        - title
        - link
        - snippet
      properties:
        title:
          type: string
          description: Title of the result
        link:
          type: string
          format: uri
          description: URL to access the content
        snippet:
          type: string
          description: Brief summary or abstract
        authors:
          type: array
          items:
            type: string
          description: List of authors (for academic content)
        number_of_citations:
          type: integer
          minimum: 0
          description: Number of citations (for academic content)
        type:
          type: string
          enum:
            - web
            - academic
          description: Type of the result
        relevance_score:
          type: number
          minimum: 0
          maximum: 1
          description: Relevance score of the result
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