> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Space Detail

> Get Space Detail



## OpenAPI

````yaml openapi/twitter-trend.json GET /twitter/spaces/detail
openapi: 3.0.3
info:
  title: TwitterAPI Unified API
  version: 1.0.0
  description: Unified OpenAPI 3.0 specification for TwitterAPI endpoints.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /twitter/spaces/detail:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_space_detail
      summary: Get Space Detail
      description: Get details of a Twitter Space by its ID.
      parameters:
        - name: space_id
          in: query
          required: true
          schema:
            type: string
          description: The ID of the space.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SpaceDetailResponse'
components:
  schemas:
    SpaceDetailResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/SpaceDetail'
        status:
          type: string
          enum:
            - success
            - error
        msg:
          type: string
    SpaceDetail:
      type: object
      properties:
        id:
          type: string
        title:
          type: string
        state:
          type: string
        created_at:
          type: string
          format: date-time
        scheduled_start:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
        media_key:
          type: string
        is_subscribed:
          type: boolean
        settings:
          type: object
          properties:
            conversation_controls:
              type: integer
            disallow_join:
              type: boolean
            is_employee_only:
              type: boolean
            is_locked:
              type: boolean
            is_muted:
              type: boolean
            is_space_available_for_clipping:
              type: boolean
            is_space_available_for_replay:
              type: boolean
            no_incognito:
              type: boolean
            narrow_cast_space_type:
              type: integer
            max_guest_sessions:
              type: integer
            max_admin_capacity:
              type: integer
        stats:
          type: object
          properties:
            total_replay_watched:
              type: integer
            total_live_listeners:
              type: integer
            total_participants:
              type: integer
        creator:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
            userName:
              type: string
            location:
              type: string
            url:
              type: string
            description:
              type: string
            protected:
              type: boolean
            isVerified:
              type: boolean
            isBlueVerified:
              type: boolean
            verifiedType:
              type: string
            followers:
              type: integer
            following:
              type: integer
            favouritesCount:
              type: integer
            statusesCount:
              type: integer
            mediaCount:
              type: integer
            createdAt:
              type: string
              format: date-time
            coverPicture:
              type: string
            profilePicture:
              type: string
            canDm:
              type: boolean
            affiliatesHighlightedLabel:
              type: object
            isAutomated:
              type: boolean
            automatedBy:
              type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````