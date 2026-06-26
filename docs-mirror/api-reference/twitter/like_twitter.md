> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Like a Tweet

> Like a tweet on behalf of the authenticated source user. Proxies the official X v2 like-post endpoint through the AIsa gateway.

Like a tweet on behalf of the authenticated source user. Proxies the official [X v2 `POST /2/users/{id}/likes` endpoint](https://docs.x.com/x-api/users/like-post), routed through the AIsa gateway at `https://api.aisa.one/apis/v1/twitter/like_twitter`.

## Prerequisites

* An **AIsa API key** (Bearer token for every request).
* A one-time **OAuth authorization** for the source user account. Link your X account by calling [`POST /apis/v1/twitter/auth_twitter`](/api-reference/twitter/auth_twitter) — AIsa stores the session against your API key and uses it automatically on every write call.
* The X session must hold `like.write`, `tweet.read`, `users.read`.

## Response fields

| Field        | Type    | Meaning                                                 |
| ------------ | ------- | ------------------------------------------------------- |
| `data.liked` | boolean | `true` once the source user has liked the target tweet. |

## Idempotency

Liking a tweet the source user has already liked is a no-op. The endpoint still returns `200` with `{ "data": { "liked": true } }`. Safe to retry.

## Common 4xx causes

* `400 invalid-request` — missing or non-numeric `tweet_id`
* `403 client-forbidden` — OAuth session missing the `like.write` scope. Re-link via `auth_twitter`.
* `404 resource-not-found` — tweet doesn't exist or isn't visible to the source user (e.g., a protected account the source user doesn't follow).

See [Error Codes](/api-reference/errors) and [Rate Limits](/api-reference/rate-limits) for more.

## Related

<CardGroup cols={3}>
  <Card title="Link an X Account" icon="key" href="/api-reference/twitter/auth_twitter">
    Start the OAuth flow this endpoint requires.
  </Card>

  <Card title="Post a Tweet" icon="pen" href="/api-reference/twitter/post_twitter">
    Create tweets you (or your agents) can like.
  </Card>

  <Card title="Follow a User" icon="user-plus" href="/api-reference/twitter/follow_twitter">
    Another write endpoint using the same OAuth session.
  </Card>
</CardGroup>


## OpenAPI

````yaml openapi/twitter-actions.json POST /twitter/like_twitter
openapi: 3.0.3
info:
  title: Twitter Actions API
  version: 1.0.0
  description: >-
    Write actions against X/Twitter, routed through the AIsa gateway. Modeled
    after the official X v2 API endpoints (e.g., POST /2/users/{id}/following).
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /twitter/like_twitter:
    post:
      summary: Like a tweet
      description: >-
        Like a tweet on behalf of the authenticated source user. Mirrors the
        [official X v2 `POST /2/users/{id}/likes`
        endpoint](https://docs.x.com/x-api/users/like-post), routed through the
        AIsa gateway.


        **Authentication.** Requires an OAuth session for the source user,
        attached to your AIsa API key. Link the account once via `POST
        /apis/v1/twitter/auth_twitter`.


        **Scopes.** The underlying X session must hold `like.write`,
        `tweet.read`, and `users.read`.


        Liking a tweet already liked is a no-op and still returns `200` with
        `liked: true`.
      operationId: likeTwitter
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - tweet_id
              properties:
                tweet_id:
                  type: string
                  description: >-
                    Numeric ID of the tweet to like. Must match X's regex
                    `^[0-9]{1,19}$`.
                  pattern: ^[0-9]{1,19}$
                  example: '1346889436626259968'
            examples:
              like_tweet:
                summary: Like tweet 1346889436626259968
                value:
                  tweet_id: '1346889436626259968'
      responses:
        '200':
          description: Like succeeded (or was already in place).
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      liked:
                        type: boolean
                        description: >-
                          `true` once the source user has liked the target
                          tweet.
              example:
                data:
                  liked: true
        '400':
          description: Invalid request — missing or malformed `tweet_id`.
        '401':
          description: Missing or invalid AIsa API key.
        '403':
          description: >-
            OAuth session missing, expired, or lacking `like.write`.
            Re-authorize via `POST /apis/v1/twitter/auth_twitter`.
        '404':
          description: Tweet not found or not visible to the source user.
        '429':
          description: >-
            Rate limit hit — either your AIsa key's RPM cap or the upstream X
            rate limit.
        '500':
          description: Internal error.
        '502':
          description: Upstream X API unreachable. Safe to retry with exponential backoff.
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key
      description: >-
        Your AIsa API key. The authenticated source user (the account doing the
        follow) is determined by the OAuth session attached to your key.

````