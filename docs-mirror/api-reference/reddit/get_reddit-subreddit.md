> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subreddit Posts

> Subreddit Posts

Get the post stream of a subreddit. Subreddit names are case-sensitive (`AskReddit`, not `askreddit`).

## Example

```bash theme={null}
curl "https://api.aisa.one/apis/v1/reddit/subreddit?subreddit=VALUE" \
  -H "Authorization: Bearer YOUR_API_KEY"
```


## OpenAPI

````yaml openapi/reddit.json GET /reddit/subreddit
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
  /reddit/subreddit:
    get:
      tags:
        - Reddit API
      summary: Subreddit Posts
      description: >-
        Fetches posts from a subreddit with sorting and filtering options. Each
        post includes title, author, selftext, score, ups, upvote_ratio,
        num_comments, created_utc, url, permalink, subreddit_subscribers, and
        is_video. Supports sort (best, hot, new, top, rising), timeframe
        filtering, pagination via the after token, and a trim parameter for
        lighter responses.
      operationId: get_reddit-subreddit
      parameters:
        - name: subreddit
          in: query
          required: true
          description: Subreddit name
          schema:
            type: string
        - name: timeframe
          in: query
          required: false
          description: Timeframe to get posts from
          schema:
            type: string
            enum:
              - all
              - day
              - week
              - month
              - year
        - name: sort
          in: query
          required: false
          description: Sort order
          schema:
            type: string
            enum:
              - best
              - hot
              - new
              - top
              - rising
        - name: after
          in: query
          required: false
          description: After to get more posts. Get 'after' from previous response.
          schema:
            type: string
          example: t3_1234567890
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
                posts:
                  - id: 1lfbo7u
                    author: Vetro_Nodulare2
                    author_fullname: t2_16syu27ar1
                    subreddit: AskReddit
                    title: What is a thing you love that lots of people hate?
                    downs: 0
                    name: t3_1lfbo7u
                    upvote_ratio: 0.9
                    ups: 45
                    total_awards_received: 0
                    score: 45
                    created: 1750341959
                    num_comments: 349
                    url: >-
                      https://www.reddit.com/r/AskReddit/comments/1lfbo7u/what_is_a_thing_you_love_that_lots_of_people_hate/
                    subreddit_subscribers: 56146328
                    is_video: false
                    created_utc: 1750341959
                after: t3_1lfogps
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: AIsa API key. Get yours at https://aisa.one

````