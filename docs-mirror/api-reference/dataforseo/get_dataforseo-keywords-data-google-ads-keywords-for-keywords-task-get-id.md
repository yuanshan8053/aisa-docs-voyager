> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get ‘Keywords For Keywords’ Results by id

> Note that Google Ads Keywords Data API is based on the latest version of the [Google Ads API](https://developers.



## OpenAPI

````yaml openapi/dataforseo.json GET /dataforseo/keywords_data/google_ads/keywords_for_keywords/task_get/{id}
openapi: 3.0.3
info:
  title: DataForSEO API
  version: 1.0.0
  description: DataForSEO API endpoints exposed through the AIsa unified gateway.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /dataforseo/keywords_data/google_ads/keywords_for_keywords/task_get/{id}:
    get:
      summary: Get ‘Keywords For Keywords’ Results by id
      description: >-
        Note that Google Ads Keywords Data API is based on the latest version of
        the [Google Ads
        API](https://developers.google.com/google-ads/api/docs/start) that has
        replaced legacy Google AdWords API. If you’re using [DataForSEO Google
        AdWords
        API](https://docs.dataforseo.com/v3/keywords_data/google/overview.md),
        you need to upgrade to [DataForSEO Google Ads
        API](https://docs.dataforseo.com/v3/keywords_data/google_ads/overview.md).
      operationId: >-
        get_dataforseo_keywords_data_google_ads_keywords_for_keywords_task_get_id
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    description: >-
                      task identifier unique task identifier in our system in
                      the UUID format you will be able to use it within 30 days
                      to request the results of the task at any time
        '400':
          description: Bad request
        '401':
          description: Unauthorized
        '429':
          description: Rate limit exceeded
        '500':
          description: Internal server error
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````