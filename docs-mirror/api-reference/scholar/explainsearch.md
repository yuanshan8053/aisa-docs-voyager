> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Explain Search Results

> Explain search results



## OpenAPI

````yaml openapi/platform-txyz-openapi.json POST /scholar/search/explain
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
  /scholar/search/explain:
    post:
      tags:
        - Search
        - Explanation
      summary: Explain search results
      description: >-
        Generate explanations for search results in different languages and
        formats
      operationId: explainSearch
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ExplainSearchRequest'
      responses:
        '200':
          description: Successful explanation response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExplainSearchResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '429':
          $ref: '#/components/responses/TooManyRequests'
        '500':
          $ref: '#/components/responses/InternalError'
      security:
        - BearerAuth: []
components:
  schemas:
    ExplainSearchRequest:
      type: object
      required:
        - search_id
      properties:
        search_id:
          type: string
          description: ID of the search to explain
        response_mode:
          type: string
          enum:
            - COMPLETE
            - SUMMARY
            - BULLET_POINTS
          default: COMPLETE
          description: Format of the explanation response
        language:
          type: string
          default: en
          description: Language code for the explanation (e.g., en, zh, ar)
          example: ar
        detail_level:
          type: string
          enum:
            - BRIEF
            - MODERATE
            - DETAILED
          default: MODERATE
          description: Level of detail in the explanation
    ExplainSearchResponse:
      type: object
      required:
        - search_id
        - explanation
      properties:
        search_id:
          type: string
          description: ID of the search being explained
        explanation:
          type: string
          description: Detailed explanation of the search results
        language:
          type: string
          description: Language of the explanation
        response_mode:
          type: string
          description: Format of the response
        summary:
          type: string
          description: Brief summary of the explanation
        key_insights:
          type: array
          items:
            type: string
          description: List of key insights from the search results
        confidence_score:
          type: number
          minimum: 0
          maximum: 1
          description: Confidence score for the explanation
        generated_at:
          type: string
          format: date-time
          description: Timestamp when the explanation was generated
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
    NotFound:
      description: Search ID not found
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