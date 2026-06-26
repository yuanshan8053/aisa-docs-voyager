> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get User Verified Followers

> Get User Verified Followers



## OpenAPI

````yaml openapi/twitter-user-batch_02.json GET /twitter/user/verifiedFollowers
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
  /twitter/user/verifiedFollowers:
    get:
      tags:
        - >-
          https://docs.twitterapi.io/api-reference/endpoint/get_user_verified_followers
      summary: Get User Verified Followers
      description: Get user verified followers in reverse chronological order.
      parameters:
        - name: user_id
          in: query
          required: true
          schema:
            type: string
          description: User ID of the user.
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
                $ref: '#/components/schemas/VerifiedFollowersResponse'
components:
  schemas:
    VerifiedFollowersResponse:
      type: object
      properties:
        followers:
          type: array
          items:
            $ref: '#/components/schemas/User'
        status:
          type: string
          enum:
            - success
            - error
        message:
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