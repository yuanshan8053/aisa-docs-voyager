> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Check Follow Relationship

> Check Follow Relationship



## OpenAPI

````yaml openapi/twitter-user-batch_02.json GET /twitter/user/check_follow_relationship
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
  /twitter/user/check_follow_relationship:
    get:
      tags:
        - >-
          https://docs.twitterapi.io/api-reference/endpoint/check_follow_relationship
      summary: Check Follow Relationship
      description: Check if the user is following/followed by the target user.
      parameters:
        - name: source_user_name
          in: query
          required: true
          schema:
            type: string
          description: Screen name of the source user.
        - name: target_user_name
          in: query
          required: true
          schema:
            type: string
          description: Screen name of the target user.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FollowRelationshipResponse'
components:
  schemas:
    FollowRelationshipResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            following:
              type: boolean
            followed_by:
              type: boolean
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