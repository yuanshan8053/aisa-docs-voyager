# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 6 个接口，46 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## authTwitterUser

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Start the OAuth flow that links a user's X/Twitter account to the AIsa API key on the request. Call this once per source user. AIsa returns an authorization URL — the user opens it in a browser, approves the requested scopes, and X redirects back to AIsa's fixed callback. AIsa stores the resulting session against your API key, and every subsequent Twitter write call (e.g., `POST /twitter/follow_twitter`) uses that session automatically.<br><br>The returned `auth_url` is short-lived; generate a fresh one every time the user needs to (re-)link. | Start the OAuth flow that links a user's X/Twitter account to your AIsa API key, returning an authorization URL for the user to approve. Once linked, AIsa reuses that session automatically for every subsequent Twitter write call. | 发起 OAuth 流程，把用户的 X/Twitter 账号关联到你的 AIsa API Key，返回供用户授权的链接。关联完成后，AIsa 会在后续每次 Twitter 写操作中自动复用该会话。 |
| `req.scopes` | Optional list of X OAuth 2.0 scopes to request. Defaults to the set required by AIsa's Twitter write endpoints: `follows.write`, `tweet.read`, `users.read`, `tweet.write`, `like.write`, `dm.read`, `dm.write`. | X OAuth 2.0 scopes to request for the link; omit to use the default set covering all of AIsa's Twitter write endpoints. | 本次关联要申请的 X OAuth 2.0 权限范围；省略则使用覆盖 AIsa 全部 Twitter 写接口的默认集合。 |
| `resp.200.auth_url` | Short-lived X OAuth authorization URL. Open it in a browser so the source user can approve the requested scopes. | Short-lived X authorization URL; open it in a browser so the source user can approve the requested scopes. Generate a fresh one each time a (re-)link is needed. | 有效期短的 X 授权链接；在浏览器打开它，让来源用户批准所申请的权限。每次需要（重新）关联都应重新生成。 |
| `resp.200.state` | Opaque CSRF state token that AIsa will validate when X redirects back to its callback. Store it client-side if you need to correlate the flow. | Opaque CSRF token AIsa validates when X redirects back; store it client-side if you need to correlate the flow. | 用于防 CSRF 的不透明令牌，X 回跳时 AIsa 会校验它；若需关联本次流程可在客户端保存。 |
| `resp.200.expires_at` | When the `auth_url` expires. Request a new one if the user hasn't completed the flow before this time. | When the authorization URL stops working; request a new one if the user hasn't finished authorizing by then. | 授权链接失效的时间；用户若未在此前完成授权需重新申请。 |

## unlikeTwitter

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Remove the source user's like from a tweet. Mirrors the [official X v2 `DELETE /2/users/{id}/likes/{tweet_id}` endpoint](https://docs.x.com/x-api/users/unlike-post), routed through the AIsa gateway. Uses POST (not DELETE) for consistency with the other AIsa Twitter write actions.<br><br>**Authentication.** Requires an OAuth session for the source user, attached to your AIsa API key. Link the account once via `POST /apis/v1/twitter/auth_twitter`.<br><br>**Scopes.** The underlying X session must hold `like.write`, `tweet.read`, and `users.read`.<br><br>Unliking a tweet the source user has not liked is a no-op and still returns `200` with `liked: false`. | Remove the authenticated source user's like from a tweet. Unliking a tweet that was never liked is a no-op and still succeeds. | 移除已授权来源用户对某条推文的点赞。对本就未点赞的推文取消点赞是空操作，仍会成功。 |
| `req.tweet_id` | Numeric ID of the tweet to unlike. Must match X's regex `^[0-9]{1,19}$`. | Identifier of the tweet to unlike. | 要取消点赞的推文标识。 |
| `resp.200.data` |  | Container for the resulting like state. | 点赞结果状态的容器。 |
| `resp.200.data.liked` | `false` once the like has been removed. | Whether the source user currently likes the tweet; `false` confirms the like was removed. | 来源用户当前是否仍点赞该推文；为 false 表示点赞已移除。 |

## likeTwitter

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Like a tweet on behalf of the authenticated source user. Mirrors the [official X v2 `POST /2/users/{id}/likes` endpoint](https://docs.x.com/x-api/users/like-post), routed through the AIsa gateway.<br><br>**Authentication.** Requires an OAuth session for the source user, attached to your AIsa API key. Link the account once via `POST /apis/v1/twitter/auth_twitter`.<br><br>**Scopes.** The underlying X session must hold `like.write`, `tweet.read`, and `users.read`.<br><br>Liking a tweet already liked is a no-op and still returns `200` with `liked: true`. | Like a tweet on behalf of the authenticated source user. Liking an already-liked tweet is a no-op and still succeeds. | 代表已授权来源用户点赞某条推文。对已点赞的推文再次点赞是空操作，仍会成功。 |
| `req.tweet_id` | Numeric ID of the tweet to like. Must match X's regex `^[0-9]{1,19}$`. | Identifier of the tweet to like. | 要点赞的推文标识。 |
| `resp.200.data` |  | Container for the resulting like state. | 点赞结果状态的容器。 |
| `resp.200.data.liked` | `true` once the source user has liked the target tweet. | Whether the source user currently likes the tweet; `true` confirms the like is in place. | 来源用户当前是否点赞该推文；为 true 表示已点赞。 |

## postTwitter

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Publish a new tweet on behalf of the authenticated source user, or edit an existing tweet. Mirrors the [official X v2 `POST /2/tweets` endpoint](https://docs.x.com/x-api/posts/create-post), routed through the AIsa gateway.<br><br>**Authentication.** Requires an OAuth session for the source user, attached to your AIsa API key. Link the account once via `POST /apis/v1/twitter/auth_twitter`.<br><br>**Scopes.** The underlying X session must hold `tweet.read`, `tweet.write`, and `users.read`.<br><br>**Mutually exclusive fields.** `media`, `poll`, `quote_tweet_id`, and `card_uri` cannot be combined in the same request. At most one of them may be set. | Publish a new tweet on behalf of the authenticated source user, or edit an existing one. At most one of `media`, `poll`, `quote_tweet_id`, and `card_uri` may be set in a single request. | 代表已授权来源用户发布新推文，或编辑已有推文。media、poll、quote_tweet_id、card_uri 在同一次请求中至多只能设置其一。 |
| `req.text` | The content of the tweet. Optional when posting media, a poll, or a quote tweet; required otherwise. | Body text of the tweet; optional when posting media, a poll, or a quote, otherwise required. | 推文正文；发布媒体、投票或引用时可省略，否则必填。 |
| `req.reply` | Post as a reply to another tweet. | Settings that turn this tweet into a reply to another tweet. | 把本推文设为对另一条推文回复的相关设置。 |
| `req.reply.in_reply_to_tweet_id` | Tweet ID being replied to. | Identifier of the tweet being replied to. | 被回复推文的标识。 |
| `req.reply.auto_populate_reply_metadata` | Auto-populate reply @-mentions from the original tweet. | Whether to automatically @-mention the participants of the original tweet in the reply. | 是否在回复中自动 @ 原推文的参与者。 |
| `req.reply.exclude_reply_user_ids` | User IDs to exclude from reply auto-mentions (max 10). | User IDs to leave out of the auto-generated reply mentions. | 从自动生成的回复 @ 名单中排除的用户 ID。 |
| `req.quote_tweet_id` | Tweet ID to quote. Mutually exclusive with `media`, `poll`, and `card_uri`. | Identifier of the tweet to quote; mutually exclusive with `media`, `poll`, and `card_uri`. | 要引用的推文标识；与 media、poll、card_uri 互斥。 |
| `req.media` | Attach media. Mutually exclusive with `poll`, `quote_tweet_id`, and `card_uri`. | Attaches uploaded media to the tweet; mutually exclusive with `poll`, `quote_tweet_id`, and `card_uri`. | 为推文附加上传的媒体；与 poll、quote_tweet_id、card_uri 互斥。 |
| `req.media.media_ids` | 1–4 media IDs from the X media-upload API. | Identifiers of media to attach, obtained beforehand from X's media-upload API. | 要附加的媒体标识，需事先通过 X 的媒体上传接口获取。 |
| `req.media.tagged_user_ids` | User IDs tagged in the media (max 10). | User IDs to tag in the attached media. | 在所附媒体中标记的用户 ID。 |
| `req.poll` | Attach a poll. Mutually exclusive with `media`, `quote_tweet_id`, and `card_uri`. | Attaches a poll to the tweet; mutually exclusive with `media`, `quote_tweet_id`, and `card_uri`. | 为推文附加投票；与 media、quote_tweet_id、card_uri 互斥。 |
| `req.poll.options` | 2–4 poll choices, each 1–25 characters. | The poll's choices. | 投票的选项。 |
| `req.poll.duration_minutes` | Poll duration in minutes (5–10080, i.e. up to 7 days). | How long the poll stays open, in minutes. | 投票开放的时长，单位为分钟。 |
| `req.poll.reply_settings` |  | Restricts who may reply to the tweet that carries this poll. | 限制谁可以回复这条带投票的推文。 |
| `req.card_uri` | Card URI. Mutually exclusive with `media`, `poll`, `quote_tweet_id`, and `direct_message_deep_link`. | URI of a card to attach; mutually exclusive with `media`, `poll`, `quote_tweet_id`, and `direct_message_deep_link`. | 要附加的卡片 URI；与 media、poll、quote_tweet_id、direct_message_deep_link 互斥。 |
| `req.direct_message_deep_link` | Deep link that takes the conversation into a private DM. | Deep link that routes the conversation into a private direct message. | 将对话引导进入私信的深度链接。 |
| `req.geo` | Attach a place to the tweet. | Attaches a place to the tweet. | 为推文附加地点。 |
| `req.geo.place_id` | X place ID. | Identifier of the X place to attach. | 要附加的 X 地点标识。 |
| `req.reply_settings` | Who is allowed to reply. | Restricts who is allowed to reply to the tweet. | 限制谁可以回复该推文。 |
| `req.for_super_followers_only` | Only visible to super followers. | Whether to make the tweet visible only to super followers. | 是否让该推文仅对超级粉丝可见。 |
| `req.nullcast` | Nullcast (promoted-only) tweet — not shown in the public timeline or to followers. | Whether to post as a nullcast (promoted-only) tweet that does not appear in the public timeline or to followers. | 是否发布为 nullcast（仅推广）推文，不出现在公开时间线或粉丝处。 |
| `req.paid_partnership` | Marks the tweet as a paid partnership. | Whether to mark the tweet as a paid partnership. | 是否将该推文标记为付费合作。 |
| `req.made_with_ai` | Flags the tweet as containing AI-generated media. | Whether to flag the tweet as containing AI-generated media. | 是否标记该推文含 AI 生成的媒体。 |
| `req.community_id` | Post into the specified community. | Identifier of the community to post into. | 要发布到的社区标识。 |
| `req.share_with_followers` | Also share the community post with your followers. | Whether to also surface the community post to your followers. | 是否同时把社区帖子展示给你的粉丝。 |
| `req.edit_options` | Edit an existing tweet instead of creating a new one (subject to X's edit window). | Switches the call to edit an existing tweet rather than create a new one, subject to X's edit window. | 将本次调用切换为编辑已有推文而非新建，受 X 的编辑时限约束。 |
| `req.edit_options.previous_post_id` | Tweet ID to edit. | Identifier of the existing tweet to edit. | 要编辑的已有推文标识。 |
| `resp.201.data` |  | Container for the created or edited tweet. | 已创建或已编辑推文的容器。 |
| `resp.201.data.id` | ID of the newly created or edited tweet. | Identifier of the resulting tweet. | 生成推文的标识。 |
| `resp.201.data.text` | Final text of the tweet as stored by X. | Final text of the tweet as stored by X. | X 实际保存的推文最终文本。 |

## unfollowTwitterUser

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Make the authenticated source user unfollow the given target user on X/Twitter. Mirrors the [official X v2 `DELETE /2/users/{source_user_id}/following/{target_user_id}` endpoint](https://docs.x.com/x-api/users/unfollow-user), routed through the AIsa gateway. Uses POST (not DELETE) for consistency with the other AIsa Twitter write actions.<br><br>**Authentication.** Requires an OAuth session for the source user, attached to your AIsa API key. Link the account once via `POST /apis/v1/twitter/auth_twitter`.<br><br>**Scopes.** The underlying X session must hold `follows.write`, `tweet.read`, and `users.read`.<br><br>Unfollowing a user you don't currently follow is a no-op and still returns `200` with `following: false`. | Make the authenticated source user unfollow a target user on X/Twitter. Unfollowing someone not currently followed is a no-op and still succeeds. | 让已授权来源用户取消关注 X/Twitter 上的目标用户。取消关注本就未关注的用户是空操作，仍会成功。 |
| `req.target_user_id` | Numeric ID of the X/Twitter user to unfollow. Must match the X regex `^[0-9]{1,19}$`. | Identifier of the X/Twitter user to unfollow. | 要取消关注的 X/Twitter 用户标识。 |
| `resp.200.data` |  | Container for the resulting follow state. | 关注结果状态的容器。 |
| `resp.200.data.following` | `false` once the source user no longer follows the target user. | Whether the source user still follows the target; `false` confirms the unfollow. | 来源用户是否仍关注目标用户；为 false 表示已取消关注。 |

## followTwitterUser

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Make the authenticated source user follow the given target user on X/Twitter. Mirrors the [official X v2 `POST /2/users/{id}/following` endpoint](https://docs.x.com/x-api/users/follow-user), routed through the AIsa gateway.<br><br>**Authentication.** This is a write action that requires an OAuth session for the source user, attached to your AIsa API key. Link your X account once by calling `POST /apis/v1/twitter/auth_twitter` — AIsa then uses that session automatically for every write request sent with your key.<br><br>**Scopes.** The underlying X session must hold `follows.write`, `tweet.read`, and `users.read`. | Make the authenticated source user follow a target user on X/Twitter. Following a protected account yields a pending follow request awaiting approval. | 让已授权来源用户关注 X/Twitter 上的目标用户。关注受保护账号时会产生待对方批准的关注请求。 |
| `req.target_user_id` | Numeric ID of the X/Twitter user to follow. Must match the X regex `^[0-9]{1,19}$`. | Identifier of the X/Twitter user to follow. | 要关注的 X/Twitter 用户标识。 |
| `resp.200.data` |  | Container for the resulting follow state. | 关注结果状态的容器。 |
| `resp.200.data.following` | `true` when the source user now follows the target user. | Whether the source user now follows the target user. | 来源用户当前是否已关注目标用户。 |
| `resp.200.data.pending_follow` | `true` when a follow request has been sent to a protected account and is awaiting approval. | Whether a follow request was sent to a protected account and is awaiting the target's approval. | 是否已向受保护账号发出关注请求并等待对方批准。 |

