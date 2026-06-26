> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Link an X Account

> Start the OAuth flow that links an X/Twitter account to your AIsa API key. Call once per source user before using any Twitter write endpoint (follow, like, post, DM).

`POST /apis/v1/twitter/auth_twitter` is the first step for any X/Twitter **write** action routed through AIsa. It returns a short-lived X OAuth authorization URL — the source user opens it in a browser, approves the requested scopes, and X redirects back to AIsa's fixed callback. AIsa stores the resulting session against your API key, and every subsequent write call (e.g., [`POST /twitter/follow_twitter`](/api-reference/twitter/follow_twitter)) uses that session automatically.

## When to call it

* **Once per source user**, the first time you link their X account.
* **Again** if the stored session is revoked, expired, or you need a different scope set.

You do not call it before every write request. The OAuth session persists against your AIsa API key.

## Flow

<Steps>
  <Step title="Start the flow">
    Send `POST /apis/v1/twitter/auth_twitter` with your AIsa API key. Optionally include a `scopes` array in the body to request a narrower set than the default.
  </Step>

  <Step title="Open the auth URL">
    The response returns an `auth_url` and a `state` token. Open `auth_url` in the source user's browser. X shows its standard "Authorize AIsa to access your account" screen.
  </Step>

  <Step title="User approves">
    After the user clicks Authorize, X redirects to AIsa's fixed callback (`https://api.aisa.one/apis/v1/twitter/oauth_callback`). AIsa validates the `state` token, exchanges the authorization code for tokens, and stores the session against your API key.
  </Step>

  <Step title="Write endpoints unlock">
    From this point on, any call to a Twitter write endpoint using your AIsa API key acts on behalf of the linked source user. You never pass OAuth tokens in the body of those calls.
  </Step>
</Steps>

## Default scopes

If you omit the `scopes` field, AIsa requests the full set needed for every Twitter write endpoint we expose:

* `follows.write` — [follow](/api-reference/twitter/follow_twitter) / unfollow
* `tweet.read` — read tweets (required by most write actions)
* `users.read` — resolve users, read profile info
* `tweet.write` — post, reply, quote
* `like.write` — like / unlike
* `dm.read` — read DM threads
* `dm.write` — send DMs

Pass a narrower array (e.g., `["follows.write", "tweet.read", "users.read"]`) if you only need a subset. Write calls that require a missing scope return `403`.

## Expiry

The `auth_url` returned by this endpoint is **short-lived** (typically 10 minutes). If the user doesn't complete the flow before `expires_at`, call `POST /apis/v1/twitter/auth_twitter` again to generate a fresh URL.

The stored OAuth **session** itself lives longer (subject to X's token rotation rules) and is refreshed automatically as long as the user doesn't revoke access from X's app settings.

## Related

<CardGroup cols={3}>
  <Card title="Follow a user" icon="user-plus" href="/api-reference/twitter/follow_twitter">
    First write endpoint that uses the session stored by this flow.
  </Card>

  <Card title="Twitter Autopilot skill" icon="twitter" href="/agent-skills/twitter-autopilot">
    Agent skill that wraps the full read + write surface.
  </Card>

  <Card title="Authentication" icon="key" href="/guides/authentication">
    AIsa API key lifecycle and storage best practices.
  </Card>
</CardGroup>


## OpenAPI

````yaml openapi/twitter-actions.json POST /twitter/auth_twitter
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
  /twitter/auth_twitter:
    post:
      summary: Link an X/Twitter account (start OAuth)
      description: >-
        Start the OAuth flow that links a user's X/Twitter account to the AIsa
        API key on the request. Call this once per source user. AIsa returns an
        authorization URL — the user opens it in a browser, approves the
        requested scopes, and X redirects back to AIsa's fixed callback. AIsa
        stores the resulting session against your API key, and every subsequent
        Twitter write call (e.g., `POST /twitter/follow_twitter`) uses that
        session automatically.


        The returned `auth_url` is short-lived; generate a fresh one every time
        the user needs to (re-)link.
      operationId: authTwitterUser
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                scopes:
                  type: array
                  items:
                    type: string
                  description: >-
                    Optional list of X OAuth 2.0 scopes to request. Defaults to
                    the set required by AIsa's Twitter write endpoints:
                    `follows.write`, `tweet.read`, `users.read`, `tweet.write`,
                    `like.write`, `dm.read`, `dm.write`.
                  example:
                    - follows.write
                    - tweet.read
                    - users.read
            example: {}
      responses:
        '200':
          description: Authorization URL generated.
          content:
            application/json:
              schema:
                type: object
                required:
                  - auth_url
                  - state
                properties:
                  auth_url:
                    type: string
                    format: uri
                    description: >-
                      Short-lived X OAuth authorization URL. Open it in a
                      browser so the source user can approve the requested
                      scopes.
                  state:
                    type: string
                    description: >-
                      Opaque CSRF state token that AIsa will validate when X
                      redirects back to its callback. Store it client-side if
                      you need to correlate the flow.
                  expires_at:
                    type: string
                    format: date-time
                    description: >-
                      When the `auth_url` expires. Request a new one if the user
                      hasn't completed the flow before this time.
              example:
                auth_url: >-
                  https://twitter.com/i/oauth2/authorize?response_type=code&client_id=AIsa&redirect_uri=https%3A%2F%2Fapi.aisa.one%2Fapis%2Fv1%2Ftwitter%2Foauth_callback&scope=follows.write%20tweet.read%20users.read&state=0c2...d1f&code_challenge=...&code_challenge_method=S256
                state: 0c2ad1f...
                expires_at: '2026-04-18T07:00:00Z'
        '400':
          description: Invalid `scopes` list — contains an unsupported scope.
        '401':
          description: Missing or invalid AIsa API key.
        '429':
          description: Rate limit hit.
        '500':
          description: Internal error generating the OAuth URL.
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