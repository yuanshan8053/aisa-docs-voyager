> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get User Profile About

> Get User Profile About



## OpenAPI

````yaml openapi/twitter-user-batch_01.json GET /twitter/user_about
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
  /twitter/user_about:
    get:
      tags:
        - https://docs.twitterapi.io/api-reference/endpoint/get_user_about
      summary: Get User Profile About
      parameters:
        - name: userName
          in: query
          required: true
          schema:
            type: string
          description: The screen name of the user
      responses:
        '200':
          description: User profile information
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserProfileAboutResponse'
components:
  schemas:
    UserProfileAboutResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            id:
              type: string
            name:
              type: string
            userName:
              type: string
            createdAt:
              type: string
            isBlueVerified:
              type: boolean
            protected:
              type: boolean
            affiliates_highlighted_label:
              type: object
              properties:
                label:
                  type: object
                  properties:
                    badge:
                      type: object
                      properties:
                        url:
                          type: string
                    description:
                      type: string
                    url:
                      type: object
                      properties:
                        url:
                          type: string
                        urlType:
                          type: string
                    userLabelDisplayType:
                      type: string
                    userLabelType:
                      type: string
            about_profile:
              type: object
              properties:
                account_based_in:
                  type: string
                location_accurate:
                  type: boolean
                learn_more_url:
                  type: string
                affiliate_username:
                  type: string
                source:
                  type: string
                username_changes:
                  type: object
                  properties:
                    count:
                      type: string
            identity_profile_labels_highlighted_label:
              type: object
              properties:
                label:
                  type: object
                  properties:
                    badge:
                      type: object
                      properties:
                        url:
                          type: string
                    description:
                      type: string
                    url:
                      type: object
                      properties:
                        url:
                          type: string
                        urlType:
                          type: string
                    userLabelDisplayType:
                      type: string
                    userLabelType:
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