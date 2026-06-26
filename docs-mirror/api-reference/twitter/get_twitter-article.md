> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Article

> Get Article



## OpenAPI

````yaml openapi/twitter-tweet-batch_02.json GET /twitter/article
openapi: 3.0.3
info:
  title: Twitter API Aggregated Documentation
  version: 1.0.0
  description: >-
    This OpenAPI specification aggregates multiple Twitter API endpoints into a
    single document.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - bearerAuth: []
paths:
  /twitter/article:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_article
      summary: Get Article
      description: Get article by tweet ID.
      parameters:
        - name: tweet_id
          in: query
          required: true
          schema:
            type: string
          description: The tweet ID of the article.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ArticleResponse'
components:
  schemas:
    ArticleResponse:
      type: object
      properties:
        article:
          $ref: '#/components/schemas/Article'
        status:
          type: string
          enum:
            - success
            - failed
        message:
          type: string
    Article:
      type: object
      properties:
        author:
          $ref: '#/components/schemas/User'
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
        title:
          type: string
        preview_text:
          type: string
        cover_media_img_url:
          type: string
        contents:
          type: array
          items:
            type: object
            properties:
              text:
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
    bearerAuth:
      type: http
      scheme: bearer

````