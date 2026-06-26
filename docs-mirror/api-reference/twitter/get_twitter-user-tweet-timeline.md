> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get User Tweet Timeline

> Retrieve a user's tweet timeline sorted by recency, with pagination support.



## OpenAPI

````yaml openapi/twitter-user-batch_01.json GET /twitter/user/tweet_timeline
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
  /twitter/user/tweet_timeline:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_user_timeline
      summary: Get User Tweet Timeline
      description: >-
        Retrieve tweets by user ID, sorted by created_at in reverse
        chronological order. Results are paginated with up to 20 tweets per
        page. The order matches what appears on the user's profile in the
        Twitter app. Time-based filtering is not supported.
      parameters:
        - name: userId
          in: query
          required: false
          schema:
            type: string
          description: User ID of the user whose timeline to retrieve.
        - name: includeReplies
          in: query
          required: false
          schema:
            type: boolean
            default: false
          description: Whether to include replies in the results. Defaults to false.
        - name: includeParentTweet
          in: query
          required: false
          schema:
            type: boolean
            default: false
          description: >-
            Whether to include the parent tweet when a tweet is a reply.
            Defaults to false.
        - name: cursor
          in: query
          required: false
          schema:
            type: string
          description: >-
            Cursor for paginating through results. Leave empty for the first
            page.
      responses:
        '200':
          description: User tweet timeline
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