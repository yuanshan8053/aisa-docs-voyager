> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get User Last Tweets

> Get User Last Tweets



## OpenAPI

````yaml openapi/twitter-user-batch_01.json GET /twitter/user/last_tweets
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
  /twitter/user/last_tweets:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_user_last_tweets
      summary: Get User Last Tweets
      parameters:
        - name: userId
          in: query
          schema:
            type: string
          description: User ID of the user
        - name: userName
          in: query
          schema:
            type: string
          description: Screen name of the user
        - name: cursor
          in: query
          schema:
            type: string
          description: Cursor for pagination
        - name: includeReplies
          in: query
          schema:
            type: boolean
            default: false
          description: Include replies in the results
      responses:
        '200':
          description: User tweets
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserTweetsResponse'
components:
  schemas:
    UserTweetsResponse:
      type: object
      properties:
        tweets:
          type: array
          items:
            type: object
            properties:
              type:
                type: string
              id:
                type: string
              url:
                type: string
              text:
                type: string
              source:
                type: string
              retweetCount:
                type: integer
              replyCount:
                type: integer
              likeCount:
                type: integer
              quoteCount:
                type: integer
              viewCount:
                type: integer
              createdAt:
                type: string
              lang:
                type: string
              bookmarkCount:
                type: integer
              isReply:
                type: boolean
              inReplyToId:
                type: string
              conversationId:
                type: string
              displayTextRange:
                type: array
                items:
                  type: integer
              inReplyToUserId:
                type: string
              inReplyToUsername:
                type: string
        has_next_page:
          type: boolean
        next_cursor:
          type: string
        status:
          type: string
          enum:
            - success
            - error
        message:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````