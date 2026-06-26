> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get User Mentions

> Get User Mentions



## OpenAPI

````yaml openapi/twitter-user-batch_02.json GET /twitter/user/mentions
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
  /twitter/user/mentions:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_user_mention
      summary: Get User Mentions
      description: >-
        Get tweet mentions by user screen name. Each page returns exactly 20
        mentions.
      parameters:
        - name: userName
          in: query
          required: true
          schema:
            type: string
          description: The user screen name to get mentions for.
        - name: sinceTime
          in: query
          schema:
            type: integer
            format: int64
          description: On or after a specified unix timestamp in seconds.
        - name: untilTime
          in: query
          schema:
            type: integer
            format: int64
          description: Before a specified unix timestamp in seconds.
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
                $ref: '#/components/schemas/UserMentionsResponse'
components:
  schemas:
    UserMentionsResponse:
      type: object
      properties:
        tweets:
          type: array
          items:
            $ref: '#/components/schemas/Tweet'
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
    Tweet:
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
        author:
          $ref: '#/components/schemas/User'
        entities:
          type: object
          properties:
            hashtags:
              type: array
              items:
                type: object
                properties:
                  indices:
                    type: array
                    items:
                      type: integer
                  text:
                    type: string
            urls:
              type: array
              items:
                type: object
                properties:
                  display_url:
                    type: string
                  expanded_url:
                    type: string
                  indices:
                    type: array
                    items:
                      type: integer
                  url:
                    type: string
            user_mentions:
              type: array
              items:
                type: object
                properties:
                  id_str:
                    type: string
                  name:
                    type: string
                  screen_name:
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