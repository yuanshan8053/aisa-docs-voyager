> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Tweet Retweeters

> Get Tweet Retweeters



## OpenAPI

````yaml openapi/twitter-tweet-batch_01.json GET /twitter/tweet/retweeters
openapi: 3.0.3
info:
  title: Twitter API Aggregated
  version: 1.0.0
  description: Aggregated API documentation for Twitter data endpoints.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - bearerAuth: []
paths:
  /twitter/tweet/retweeters:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_tweet_retweeter
      summary: Get Tweet Retweeters
      parameters:
        - name: tweetId
          in: query
          required: true
          schema:
            type: string
          description: The tweet ID to get retweeters for.
        - name: cursor
          in: query
          schema:
            type: string
          description: Cursor for pagination.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
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
                  message:
                    type: string
components:
  schemas:
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
    bearerAuth:
      type: http
      scheme: bearer

````