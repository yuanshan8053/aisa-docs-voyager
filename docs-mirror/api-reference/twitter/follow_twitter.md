> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Follow a User

> Make the authenticated source user follow a target user on X/Twitter. Proxies the official X v2 follow-user endpoint through the AIsa gateway.

Follow a user on X/Twitter on behalf of the authenticated source user. This is a direct proxy for the official [X v2 `POST /2/users/{id}/following` endpoint](https://docs.x.com/x-api/users/follow-user), routed through the AIsa gateway at `https://api.aisa.one/apis/v1/twitter/follow_twitter`.

## Prerequisites

* An **AIsa API key** (Bearer token for every request).
* A one-time **OAuth authorization** for the source user account. Link your X account by calling [`POST /apis/v1/twitter/auth_twitter`](/api-reference/twitter/auth_twitter) — that endpoint kicks off the OAuth flow and stores the resulting session against your AIsa key, so you do not pass OAuth tokens in the request body here.
* The X session must hold the following scopes: `follows.write`, `tweet.read`, `users.read`.

<Tip>
  Looking to follow by `@username` instead of numeric ID? Resolve the user first with [`GET /twitter/user/info`](/api-reference/twitter/get_twitter-user-info), then pass the returned `id` as `target_user_id`.
</Tip>

## Response fields

| Field                 | Type    | Meaning                                                                                                                          |
| --------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `data.following`      | boolean | `true` once the source user follows the target. For public accounts this is the success signal.                                  |
| `data.pending_follow` | boolean | `true` when the target is a **protected** account — the follow request has been sent and is awaiting the target user's approval. |

For the full set of error responses and retry guidance, see [Error Codes](/api-reference/errors). Write endpoints count toward your standard key RPM/TPM — see [Rate Limits](/api-reference/rate-limits).


## OpenAPI

````yaml openapi/twitter-actions.json POST /twitter/follow_twitter
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
  /twitter/follow_twitter:
    post:
      summary: Follow a user on X/Twitter
      description: >-
        Make the authenticated source user follow the given target user on
        X/Twitter. Mirrors the [official X v2 `POST /2/users/{id}/following`
        endpoint](https://docs.x.com/x-api/users/follow-user), routed through
        the AIsa gateway.


        **Authentication.** This is a write action that requires an OAuth
        session for the source user, attached to your AIsa API key. Link your X
        account once by calling `POST /apis/v1/twitter/auth_twitter` — AIsa then
        uses that session automatically for every write request sent with your
        key.


        **Scopes.** The underlying X session must hold `follows.write`,
        `tweet.read`, and `users.read`.
      operationId: followTwitterUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - target_user_id
              properties:
                target_user_id:
                  type: string
                  description: >-
                    Numeric ID of the X/Twitter user to follow. Must match the X
                    regex `^[0-9]{1,19}$`.
                  pattern: ^[0-9]{1,19}$
                  example: '6253282'
            examples:
              follow_user:
                summary: Follow @TwitterDev (id 2244994945)
                value:
                  target_user_id: '2244994945'
      responses:
        '200':
          description: Follow succeeded (or was already in place).
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      following:
                        type: boolean
                        description: >-
                          `true` when the source user now follows the target
                          user.
                      pending_follow:
                        type: boolean
                        description: >-
                          `true` when a follow request has been sent to a
                          protected account and is awaiting approval.
              example:
                data:
                  following: true
                  pending_follow: false
        '400':
          description: Invalid request — missing or malformed `target_user_id`.
        '401':
          description: Missing or invalid AIsa API key.
        '403':
          description: >-
            OAuth session missing, expired, or lacking the `follows.write`
            scope. Re-authorize from the dashboard.
        '429':
          description: >-
            Rate limit hit — either your AIsa key's RPM cap or the upstream X
            rate limit.
        '500':
          description: Internal error.
        '502':
          description: >-
            Upstream X API unreachable or returned an error. Safe to retry with
            exponential backoff.
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