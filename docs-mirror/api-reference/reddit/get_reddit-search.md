> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Reddit

> Search Reddit

Search across all of Reddit for posts matching a query.

## Example

```bash theme={null}
curl "https://api.aisa.one/apis/v1/reddit/search?query=VALUE" \
  -H "Authorization: Bearer YOUR_API_KEY"
```


## OpenAPI

````yaml openapi/reddit.json GET /reddit/search
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
  /reddit/search:
    get:
      tags:
        - Reddit API
      summary: Search Reddit
      description: >-
        Searches across all of Reddit for posts matching a query. Each post
        includes title, author, selftext, subreddit, score, ups, upvote_ratio,
        num_comments, created_utc, url, permalink, and is_video. Supports sort
        (relevance, new, top, comment_count), timeframe filtering, pagination
        via the after token, and a trim parameter for lighter responses.
      operationId: get_reddit-search
      parameters:
        - name: query
          in: query
          required: true
          description: Search query
          schema:
            type: string
        - name: sort
          in: query
          required: false
          description: Sort by
          schema:
            type: string
            enum:
              - relevance
              - new
              - top
              - comment_count
          example: relevance
        - name: timeframe
          in: query
          required: false
          description: Timeframe
          schema:
            type: string
            enum:
              - all
              - day
              - week
              - month
              - year
          example: all
        - name: after
          in: query
          required: false
          description: Used to paginate to next page
          schema:
            type: string
          example: t3_1i8z28z
        - name: trim
          in: query
          required: false
          description: Set to true for a trimmed down version of the response
          schema:
            type: boolean
          example: 'false'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              example:
                success: true
                posts:
                  - id: w63dgy
                    author: Morgentau7
                    author_fullname: t2_2hy2xjit
                    subreddit: MadeMeSmile
                    title: Player realizes that he nearly stole the dogs job
                    downs: 0
                    name: t3_w63dgy
                    upvote_ratio: 0.97
                    ups: 220403
                    total_awards_received: 0
                    score: 220403
                    created: 1658580900
                    num_comments: 1246
                    url: >-
                      https://www.reddit.com/r/MadeMeSmile/comments/w63dgy/player_realizes_that_he_nearly_stole_the_dogs_job/
                    subreddit_subscribers: 11605207
                    is_video: true
                    created_utc: 1658580900
                after: t3_1izmcgx
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: AIsa API key. Get yours at https://aisa.one

````