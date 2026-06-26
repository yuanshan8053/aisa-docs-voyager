> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# YouTube Search API

> YouTube Search



## OpenAPI

````yaml openapi/youte-search.json GET /youtube/search
openapi: 3.0.3
info:
  title: YouTube Search API
  description: SearchApi.io YouTube Search endpoint
  version: 1.0.0
servers:
  - url: https://api.aisa.one/apis/v1
    description: YouTube Search API Server
security:
  - bearerAuth: []
paths:
  /youtube/search:
    get:
      tags:
        - YouTube Search
      summary: YouTube Search
      description: Perform a YouTube search via SearchApi
      parameters:
        - name: engine
          in: query
          required: true
          schema:
            type: string
            enum:
              - youtube
          description: Engine identifier for YouTube Search
        - name: q
          in: query
          required: true
          schema:
            type: string
          description: Search query
        - name: sp
          in: query
          required: false
          schema:
            type: string
          description: YouTube filter token (pagination or advanced filters)
        - name: gl
          in: query
          required: false
          schema:
            type: string
          description: Country code (e.g. us, jp)
        - name: hl
          in: query
          required: false
          schema:
            type: string
          description: Interface language
      responses:
        '200':
          description: Successful YouTube search response
          content:
            application/json:
              schema:
                type: object
                description: YouTube search result payload
                properties:
                  search_metadata:
                    type: object
                    description: Search metadata
                  search_results:
                    type: array
                    items:
                      type: object
                      properties:
                        video_id:
                          type: string
                        title:
                          type: string
                        link:
                          type: string
                        channel_name:
                          type: string
        '400':
          description: Invalid request parameters
        '401':
          description: Unauthorized / Invalid API key
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````