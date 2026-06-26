> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get User Info

> Get User Info



## OpenAPI

````yaml openapi/twitter-user-batch_01.json GET /twitter/user/info
openapi: 3.0.3
info:
  title: Twitter API
  version: 1.0.0
  description: Twitter data API, providing endpoints for user and tweet information.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /twitter/user/info:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_user_by_username
      summary: Get User Info
      parameters:
        - name: userName
          in: query
          required: true
          schema:
            type: string
          description: The screen name of the user
      responses:
        '200':
          description: User information
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchUserInfoResponse'
components:
  schemas:
    BatchUserInfoResponse:
      type: object
      properties:
        users:
          type: array
          items:
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
        status:
          type: string
          enum:
            - success
            - error
        msg:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````