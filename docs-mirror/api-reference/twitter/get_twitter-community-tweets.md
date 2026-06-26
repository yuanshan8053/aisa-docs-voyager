> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Community Tweets

> Get Community Tweets



## OpenAPI

````yaml openapi/twitter-communities.json GET /twitter/community/tweets
openapi: 3.0.3
info:
  title: Twitter API - Community Endpoints
  version: 1.0.0
  description: Consolidated API documentation for Twitter community-related endpoints.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - bearerAuth: []
paths:
  /twitter/community/tweets:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_community_tweets
      summary: Get Community Tweets
      description: Retrieve tweets of a community.
      parameters:
        - name: community_id
          in: query
          required: true
          schema:
            type: string
          description: ID of the community
        - name: cursor
          in: query
          required: false
          schema:
            type: string
          description: Cursor for pagination
      responses:
        '200':
          description: Community tweets response
          content:
            application/json:
              schema:
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
components:
  schemas:
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
        quoted_tweet:
          type: string
        retweeted_tweet:
          type: string
        isLimitedReply:
          type: boolean
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
        profile_bio:
          type: object
          properties:
            description:
              type: string
            entities:
              type: object
              properties:
                description:
                  type: object
                  properties:
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
                url:
                  type: object
                  properties:
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````