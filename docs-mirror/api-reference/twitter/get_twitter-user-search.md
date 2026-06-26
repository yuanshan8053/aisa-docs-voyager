> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search User by Keyword

> Search User by Keyword



## OpenAPI

````yaml openapi/twitter-user-batch_02.json GET /twitter/user/search
openapi: 3.0.3
info:
  title: Twitter API
  version: 1.0.0
  description: Twitter API endpoints for user data and interactions.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /twitter/user/search:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/search_user
      summary: Search User by Keyword
      description: Search user by keyword.
      parameters:
        - name: query
          in: query
          required: true
          schema:
            type: string
          description: The keyword to search.
        - name: cursor
          in: query
          schema:
            type: string
          description: The cursor to paginate through the results. First page is empty.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SearchUserResponse'
components:
  schemas:
    SearchUserResponse:
      type: object
      properties:
        users:
          type: array
          items:
            $ref: '#/components/schemas/User'
        has_next_page:
          type: boolean
        next_cursor:
          type: string
        status:
          type: string
          enum:
            - success
            - error
        msg:
          type: string
    User:
      type: object
      properties:
        type:
          type: string
        userName:
          type: string
        url:
          type: string
        id:
          type: string
        name:
          type: string
        isBlueVerified:
          type: boolean
        verifiedType:
          type: string
        profilePicture:
          type: string
        coverPicture:
          type: string
        description:
          type: string
        location:
          type: string
        followers:
          type: integer
        following:
          type: integer
        canDm:
          type: boolean
        createdAt:
          type: string
        favouritesCount:
          type: integer
        hasCustomTimelines:
          type: boolean
        isTranslator:
          type: boolean
        mediaCount:
          type: integer
        statusesCount:
          type: integer
        withheldInCountries:
          type: array
          items:
            type: string
        possiblySensitive:
          type: boolean
        pinnedTweetIds:
          type: array
          items:
            type: string
        isAutomated:
          type: boolean
        automatedBy:
          type: string
        unavailable:
          type: boolean
        message:
          type: string
        unavailableReason:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````