> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subreddit Details

> Subreddit Details

Get metadata for a subreddit — subscribers, description, and more. Subreddit names are case-sensitive.

## Example

```bash theme={null}
curl "https://api.aisa.one/apis/v1/reddit/subreddit/details" \
  -H "Authorization: Bearer YOUR_API_KEY"
```


## OpenAPI

````yaml openapi/reddit.json GET /reddit/subreddit/details
openapi: 3.0.0
info:
  title: Reddit API
  description: >-
    Read public Reddit data — search posts, browse subreddits, and fetch
    comments.
  version: 1.0.0
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - bearerAuth: []
paths:
  /reddit/subreddit/details:
    get:
      tags:
        - Reddit API
      summary: Subreddit Details
      description: >-
        Retrieves metadata about a subreddit by name or URL. The subreddit name
        must be case-sensitive. Returns display_name, description, subscribers,
        weekly_active_users, weekly_contributions, rules, icon_img, header_img,
        advertiser_category, submit_text, and created_at.
      operationId: get_reddit-subreddit-details
      parameters:
        - name: subreddit
          in: query
          required: false
          description: >-
            Subreddit name. MUST be case sensitive. So 'AskReddit' not
            'askreddit'.
          schema:
            type: string
          example: AskReddit
        - name: url
          in: query
          required: false
          description: Subreddit URL
          schema:
            type: string
          example: https://www.reddit.com/r/AbsoluteUnits/
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              example:
                success: true
                credits_remaining: 33950256
                subreddit_id: t5_a7wuv
                display_name: AbsoluteUnits
                weekly_active_users: 1428398
                weekly_contributions: 8923
                rules: >-
                  #ABSOLUTE UNITS


                  ---

                      Be in awe at the size of these lads

                  ---


                  ###[Check out our deep, well-reflected definitions of an
                  absolute
                  unit.](https://www.reddit.com/r/AbsoluteUnits/wiki/index)  
                description: >-
                  Absolute Unit : an Animal or Public Figure, who is larger than
                  we should normally expect.
                header_img: null
                icon_img: >-
                  https://styles.redditmedia.com/t5_a7wuv/styles/communityIcon_t3cspt08bl681.png?width=128&frame=1&auto=webp&s=6f7e59ccf1724bd6c8b3e0d2840c9b21297102c3
                subscribers: 1923642
                advertiser_category: ''
                created_at: '2018-01-05T10:35:24.000Z'
                submit_text: ''
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: AIsa API key. Get yours at https://aisa.one

````