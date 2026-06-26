> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Post a Tweet

> Publish a tweet — plain text, reply, quote, poll, or with media — on behalf of the authenticated source user. Also supports editing an existing tweet within X's edit window.

Publish a tweet on behalf of the authenticated source user. Proxies the official [X v2 `POST /2/tweets` endpoint](https://docs.x.com/x-api/posts/create-post), routed through the AIsa gateway at `https://api.aisa.one/apis/v1/twitter/post_twitter`.

One endpoint covers every variant:

<CardGroup cols={3}>
  <Card title="Plain text" icon="pen">
    `{ "text": "Hello, World!" }`
  </Card>

  <Card title="Reply" icon="reply">
    Set `reply.in_reply_to_tweet_id`.
  </Card>

  <Card title="Quote tweet" icon="quote-left">
    Set `quote_tweet_id`.
  </Card>

  <Card title="With a poll" icon="square-poll-vertical">
    Set `poll.options` + `poll.duration_minutes`.
  </Card>

  <Card title="With media" icon="image">
    Set `media.media_ids` (1–4 IDs).
  </Card>

  <Card title="Edit a tweet" icon="pen-to-square">
    Set `edit_options.previous_post_id` (within X's edit window).
  </Card>
</CardGroup>

## Prerequisites

* An **AIsa API key** (Bearer token for every request).
* A one-time **OAuth authorization** for the source user account. Link your X account by calling [`POST /apis/v1/twitter/auth_twitter`](/api-reference/twitter/auth_twitter) — AIsa stores the session against your API key and uses it automatically on every write call.
* The X session must hold `tweet.read`, `tweet.write`, `users.read`.

## Mutually exclusive fields

At most **one** of these may appear in a single request:

* `media`
* `poll`
* `quote_tweet_id`
* `card_uri`

X will reject the request (`400 invalid-request`) if more than one is set.

## Response

On success the endpoint returns `201 Created`:

```json theme={null}
{
  "data": {
    "id": "1346889436626259968",
    "text": "Hello, World!"
  }
}
```

The returned `text` reflects what X actually stored (e.g., shortened URLs). Use `data.id` to reference this tweet in subsequent calls (reply, quote, like, edit, delete).

## Editing tweets

Pass `edit_options.previous_post_id` to edit an existing tweet instead of creating a new one. Edits are subject to X's edit window and edit count limits; the endpoint returns `409 conflict` if the window has passed or the edit quota is exhausted.

## Reply settings

Restrict who can reply with `reply_settings`:

| Value            | Who can reply                           |
| ---------------- | --------------------------------------- |
| `following`      | People you follow                       |
| `mentionedUsers` | Users explicitly mentioned in the tweet |
| `subscribers`    | Your X Premium subscribers              |
| `verified`       | Verified accounts                       |

Omit the field for the default (everyone).

## Common 4xx causes

* `400 invalid-request` — set two mutually-exclusive fields, text too long, invalid poll duration, etc.
* `403 client-forbidden` — OAuth session missing the `tweet.write` scope. Re-link via `auth_twitter`.
* `404 resource-not-found` — referenced `in_reply_to_tweet_id`, `quote_tweet_id`, or `previous_post_id` doesn't exist or isn't visible to the source user.
* `409 conflict` — duplicate content, or edit outside the allowed window.

See the full list on [Error Codes](/api-reference/errors) and [Rate Limits](/api-reference/rate-limits) for tier caps.

## Related

<CardGroup cols={3}>
  <Card title="Link an X Account" icon="key" href="/api-reference/twitter/auth_twitter">
    Start the OAuth flow this endpoint requires.
  </Card>

  <Card title="Follow a User" icon="user-plus" href="/api-reference/twitter/follow_twitter">
    Another write endpoint using the same OAuth session.
  </Card>

  <Card title="Twitter Autopilot skill" icon="twitter" href="/agent-skills/twitter-autopilot">
    Agent skill that wraps the full Twitter surface.
  </Card>
</CardGroup>


## OpenAPI

````yaml openapi/twitter-actions.json POST /twitter/post_twitter
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
  /twitter/post_twitter:
    post:
      summary: Post or edit a tweet
      description: >-
        Publish a new tweet on behalf of the authenticated source user, or edit
        an existing tweet. Mirrors the [official X v2 `POST /2/tweets`
        endpoint](https://docs.x.com/x-api/posts/create-post), routed through
        the AIsa gateway.


        **Authentication.** Requires an OAuth session for the source user,
        attached to your AIsa API key. Link the account once via `POST
        /apis/v1/twitter/auth_twitter`.


        **Scopes.** The underlying X session must hold `tweet.read`,
        `tweet.write`, and `users.read`.


        **Mutually exclusive fields.** `media`, `poll`, `quote_tweet_id`, and
        `card_uri` cannot be combined in the same request. At most one of them
        may be set.
      operationId: postTwitter
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                text:
                  type: string
                  description: >-
                    The content of the tweet. Optional when posting media, a
                    poll, or a quote tweet; required otherwise.
                  example: Hello from AIsa — shipping agent-friendly Twitter APIs.
                reply:
                  type: object
                  description: Post as a reply to another tweet.
                  required:
                    - in_reply_to_tweet_id
                  properties:
                    in_reply_to_tweet_id:
                      type: string
                      description: Tweet ID being replied to.
                      pattern: ^[0-9]{1,19}$
                    auto_populate_reply_metadata:
                      type: boolean
                      description: Auto-populate reply @-mentions from the original tweet.
                    exclude_reply_user_ids:
                      type: array
                      items:
                        type: string
                        pattern: ^[0-9]{1,19}$
                      maxItems: 10
                      description: User IDs to exclude from reply auto-mentions (max 10).
                quote_tweet_id:
                  type: string
                  description: >-
                    Tweet ID to quote. Mutually exclusive with `media`, `poll`,
                    and `card_uri`.
                  pattern: ^[0-9]{1,19}$
                media:
                  type: object
                  description: >-
                    Attach media. Mutually exclusive with `poll`,
                    `quote_tweet_id`, and `card_uri`.
                  required:
                    - media_ids
                  properties:
                    media_ids:
                      type: array
                      items:
                        type: string
                      minItems: 1
                      maxItems: 4
                      description: 1–4 media IDs from the X media-upload API.
                    tagged_user_ids:
                      type: array
                      items:
                        type: string
                        pattern: ^[0-9]{1,19}$
                      maxItems: 10
                      description: User IDs tagged in the media (max 10).
                poll:
                  type: object
                  description: >-
                    Attach a poll. Mutually exclusive with `media`,
                    `quote_tweet_id`, and `card_uri`.
                  required:
                    - options
                    - duration_minutes
                  properties:
                    options:
                      type: array
                      items:
                        type: string
                        maxLength: 25
                      minItems: 2
                      maxItems: 4
                      description: 2–4 poll choices, each 1–25 characters.
                    duration_minutes:
                      type: integer
                      minimum: 5
                      maximum: 10080
                      description: Poll duration in minutes (5–10080, i.e. up to 7 days).
                    reply_settings:
                      type: string
                      enum:
                        - following
                        - mentionedUsers
                        - subscribers
                        - verified
                card_uri:
                  type: string
                  description: >-
                    Card URI. Mutually exclusive with `media`, `poll`,
                    `quote_tweet_id`, and `direct_message_deep_link`.
                direct_message_deep_link:
                  type: string
                  description: Deep link that takes the conversation into a private DM.
                geo:
                  type: object
                  description: Attach a place to the tweet.
                  properties:
                    place_id:
                      type: string
                      description: X place ID.
                reply_settings:
                  type: string
                  enum:
                    - following
                    - mentionedUsers
                    - subscribers
                    - verified
                  description: Who is allowed to reply.
                for_super_followers_only:
                  type: boolean
                  default: false
                  description: Only visible to super followers.
                nullcast:
                  type: boolean
                  default: false
                  description: >-
                    Nullcast (promoted-only) tweet — not shown in the public
                    timeline or to followers.
                paid_partnership:
                  type: boolean
                  description: Marks the tweet as a paid partnership.
                made_with_ai:
                  type: boolean
                  description: Flags the tweet as containing AI-generated media.
                community_id:
                  type: string
                  pattern: ^[0-9]{1,19}$
                  description: Post into the specified community.
                share_with_followers:
                  type: boolean
                  default: false
                  description: Also share the community post with your followers.
                edit_options:
                  type: object
                  description: >-
                    Edit an existing tweet instead of creating a new one
                    (subject to X's edit window).
                  required:
                    - previous_post_id
                  properties:
                    previous_post_id:
                      type: string
                      pattern: ^[0-9]{1,19}$
                      description: Tweet ID to edit.
            examples:
              simple_text:
                summary: Plain text tweet
                value:
                  text: Hello, World!
              reply:
                summary: Reply to a tweet
                value:
                  text: Totally agree 👌
                  reply:
                    in_reply_to_tweet_id: '1234567890123456789'
                    auto_populate_reply_metadata: true
              with_poll:
                summary: Tweet with a poll
                value:
                  text: 'Pick your favorite:'
                  poll:
                    options:
                      - Option A
                      - Option B
                      - Option C
                    duration_minutes: 60
              with_media:
                summary: Tweet with media
                value:
                  text: Ship log 📸
                  media:
                    media_ids:
                      - '1146654567674912769'
                    tagged_user_ids:
                      - '2244994945'
              quote:
                summary: Quote tweet
                value:
                  text: 'Worth reading:'
                  quote_tweet_id: '1234567890123456789'
              edit:
                summary: Edit an existing tweet
                value:
                  text: Updated tweet content (typo fixed).
                  edit_options:
                    previous_post_id: '1234567890123456789'
      responses:
        '201':
          description: Tweet created (or edited) successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      id:
                        type: string
                        pattern: ^[0-9]{1,19}$
                        description: ID of the newly created or edited tweet.
                      text:
                        type: string
                        description: Final text of the tweet as stored by X.
              example:
                data:
                  id: '1346889436626259968'
                  text: Hello, World!
        '400':
          description: >-
            Invalid request — violated a mutual-exclusivity rule, missing
            required field, or text too long.
        '401':
          description: Missing or invalid AIsa API key.
        '403':
          description: >-
            OAuth session missing, expired, or lacking `tweet.write`.
            Re-authorize via `POST /apis/v1/twitter/auth_twitter`.
        '404':
          description: Referenced tweet (reply, quote, or edit target) not found.
        '409':
          description: >-
            Conflict — e.g., duplicate tweet content or edit outside the allowed
            window.
        '429':
          description: Rate limit hit.
        '500':
          description: Internal error.
        '502':
          description: Upstream X API unreachable.
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