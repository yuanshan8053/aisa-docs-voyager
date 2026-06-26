> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Community Info By Id

> Get Community Info By Id



## OpenAPI

````yaml openapi/twitter-communities.json GET /twitter/community/info
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
  /twitter/community/info:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_community_by_id
      summary: Get Community Info By Id
      description: Retrieve information about a community by its ID.
      parameters:
        - name: community_id
          in: query
          required: true
          schema:
            type: string
          description: ID of the community
      responses:
        '200':
          description: Community info response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CommunityInfo'
components:
  schemas:
    CommunityInfo:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        description:
          type: string
        question:
          type: string
        member_count:
          type: integer
        moderator_count:
          type: integer
        created_at:
          type: string
        join_policy:
          type: string
        invites_policy:
          type: string
        is_nsfw:
          type: boolean
        is_pinned:
          type: boolean
        role:
          type: string
        primary_topic:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
        banner_url:
          type: string
        search_tags:
          type: array
          items:
            type: string
        rules:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
              description:
                type: string
        creator:
          $ref: '#/components/schemas/User'
        admin:
          $ref: '#/components/schemas/User'
        members_preview:
          type: array
          items:
            type: object
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