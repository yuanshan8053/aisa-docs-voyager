# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 6 个接口，192 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## GET /twitter/user_about

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get User Profile About | Fetch the public profile and the 'About this account' panel for a single user identified by screen name, including account origin, identity labels, and affiliate badges. | 按用户名获取单个用户的公开资料及「关于此账号」面板，包含账号归属地、身份标签与所属机构徽章等信息。 |
| `param:userName` | The screen name of the user | Screen name (@handle, without the @) of the user whose About profile you want. | 要查询其 About 资料的用户名（@ 后的部分，不含 @）。 |
| `resp.200.data` |  | The user's profile and About-panel details. | 用户的资料及 About 面板详情。 |
| `resp.200.data.id` |  | Unique identifier of the user. | 用户的唯一标识。 |
| `resp.200.data.name` |  | The user's display name shown on the profile. | 用户在资料页展示的昵称。 |
| `resp.200.data.userName` |  | The user's @handle, unique across X/Twitter. | 用户的 @ 用户名，在 X/Twitter 上唯一。 |
| `resp.200.data.createdAt` |  | Timestamp when the user's account was created. | 用户账号的创建时间。 |
| `resp.200.data.isBlueVerified` |  | Whether the user holds a paid X (Twitter) Blue verification. | 用户是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.data.protected` |  | Whether the account is protected, meaning its tweets are visible only to approved followers. | 账号是否为受保护状态，即推文仅对获批准的关注者可见。 |
| `resp.200.data.affiliates_highlighted_label` |  | The highlighted affiliation badge that marks the user as belonging to a parent organization. | 突出展示的所属机构徽章，标识用户隶属于某个母机构。 |
| `resp.200.data.affiliates_highlighted_label.label` |  | Details of the affiliation badge. | 所属机构徽章的详情。 |
| `resp.200.data.affiliates_highlighted_label.label.badge` |  | The badge image of the affiliation. | 所属机构徽章的图标。 |
| `resp.200.data.affiliates_highlighted_label.label.badge.url` |  | Web link to the badge image. | 徽章图标的网页链接。 |
| `resp.200.data.affiliates_highlighted_label.label.description` |  | Text describing the affiliation, such as the parent organization's name. | 描述所属机构的文字，如母机构名称。 |
| `resp.200.data.affiliates_highlighted_label.label.url` |  | Link the affiliation badge points to. | 所属机构徽章指向的链接。 |
| `resp.200.data.affiliates_highlighted_label.label.url.url` |  | Destination address of the affiliation link. | 所属机构链接的目标地址。 |
| `resp.200.data.affiliates_highlighted_label.label.url.urlType` |  | Category of the affiliation link, indicating how it should be handled.<br>[⚠️Note:源码未声明 urlType 的可取值及各自含义，待研发确认。] | 所属机构链接的类别，指示其处理方式。<br>[⚠️批注:源码未声明 urlType 的可取值及各自含义，待研发确认。] |
| `resp.200.data.affiliates_highlighted_label.label.userLabelDisplayType` |  | How the affiliation label is rendered on the profile.<br>[⚠️Note:源码未声明 userLabelDisplayType 的可取值及各自含义，待研发确认。] | 该所属机构标签在资料页的呈现方式。<br>[⚠️批注:源码未声明 userLabelDisplayType 的可取值及各自含义，待研发确认。] |
| `resp.200.data.affiliates_highlighted_label.label.userLabelType` |  | The kind of user label this badge represents.<br>[⚠️Note:源码未声明 userLabelType 的可取值及各自含义，待研发确认。] | 该徽章所代表的用户标签种类。<br>[⚠️批注:源码未声明 userLabelType 的可取值及各自含义，待研发确认。] |
| `resp.200.data.about_profile` |  | Contents of the 'About this account' panel, such as where the account is based and how that location was determined. | 「关于此账号」面板的内容，如账号所在地及其判定方式。 |
| `resp.200.data.about_profile.account_based_in` |  | Country or region X reports the account is based in. | X 标注的账号所在国家或地区。 |
| `resp.200.data.about_profile.location_accurate` |  | Whether the reported account location is considered accurate. | 标注的账号所在地是否被认为准确。 |
| `resp.200.data.about_profile.learn_more_url` |  | Link to X's help page explaining the About-account information. | 指向 X 帮助页的链接，说明账号相关信息。 |
| `resp.200.data.about_profile.affiliate_username` |  | Screen name of the organization this account is affiliated with. | 该账号所属机构的用户名。 |
| `resp.200.data.about_profile.source` |  | Where the About-account information was sourced from.<br>[⚠️Note:源码未声明 source 的可取值及各自含义，待研发确认。] | 「关于此账号」信息的来源。<br>[⚠️批注:源码未声明 source 的可取值及各自含义，待研发确认。] |
| `resp.200.data.about_profile.username_changes` |  | Summary of how often the account has changed its username. | 账号修改用户名的次数概况。 |
| `resp.200.data.about_profile.username_changes.count` |  | Number of times the account has changed its username. | 账号修改过用户名的次数。 |
| `resp.200.data.identity_profile_labels_highlighted_label` |  | Highlighted identity label, such as a government or official-account marker. | 突出展示的身份标签，如政府或官方账号标记。 |
| `resp.200.data.identity_profile_labels_highlighted_label.label` |  | Details of the identity label. | 身份标签的详情。 |
| `resp.200.data.identity_profile_labels_highlighted_label.label.description` |  | Text describing the identity label. | 描述该身份标签的文字。 |
| `resp.200.data.identity_profile_labels_highlighted_label.label.badge` |  | The badge image of the identity label. | 身份标签的徽章图标。 |
| `resp.200.data.identity_profile_labels_highlighted_label.label.badge.url` |  | Web link to the badge image. | 徽章图标的网页链接。 |
| `resp.200.data.identity_profile_labels_highlighted_label.label.url` |  | Link the identity label points to. | 身份标签指向的链接。 |
| `resp.200.data.identity_profile_labels_highlighted_label.label.url.url` |  | Destination address of the identity-label link. | 身份标签链接的目标地址。 |
| `resp.200.data.identity_profile_labels_highlighted_label.label.url.urlType` |  | Category of the identity-label link, indicating how it should be handled.<br>[⚠️Note:源码未声明 urlType 的可取值及各自含义，待研发确认。] | 身份标签链接的类别，指示其处理方式。<br>[⚠️批注:源码未声明 urlType 的可取值及各自含义，待研发确认。] |
| `resp.200.data.identity_profile_labels_highlighted_label.label.userLabelDisplayType` |  | How the identity label is rendered on the profile.<br>[⚠️Note:源码未声明 userLabelDisplayType 的可取值及各自含义，待研发确认。] | 该身份标签在资料页的呈现方式。<br>[⚠️批注:源码未声明 userLabelDisplayType 的可取值及各自含义，待研发确认。] |
| `resp.200.data.identity_profile_labels_highlighted_label.label.userLabelType` |  | The kind of user label this identity badge represents.<br>[⚠️Note:源码未声明 userLabelType 的可取值及各自含义，待研发确认。] | 该身份徽章所代表的用户标签种类。<br>[⚠️批注:源码未声明 userLabelType 的可取值及各自含义，待研发确认。] |
| `resp.200.status` |  | Outcome marker of the request: success when the profile was returned, error otherwise. | 请求结果标记：成功返回资料为 success，否则为 error。 |
| `resp.200.msg` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/user/batch_info_by_ids

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Batch Get User Info By UserIds | Look up the profiles of multiple users in one call by passing their numeric user IDs, avoiding one request per user. | 一次请求传入多个数字用户 ID，批量查询这些用户的资料，避免逐个用户单独请求。 |
| `param:userIds` | Comma-separated user IDs | Comma-separated list of numeric user IDs to look up in this batch. | 本次批量查询的数字用户 ID 列表，以逗号分隔。 |
| `resp.200.users` |  | Followers of the user, returned for this page. | 本页返回的关注该用户的关注者。 |
| `resp.200.users.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.users.userName` |  | The follower's @handle, unique across X/Twitter and used in profile URLs. | 关注者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.users.url` |  | Web link to the follower's profile page. | 关注者资料页的网页链接。 |
| `resp.200.users.id` |  | Unique identifier of the follower. | 关注者的唯一标识。 |
| `resp.200.users.name` |  | The follower's display name shown on the profile. | 关注者在资料页展示的昵称。 |
| `resp.200.users.isBlueVerified` |  | Whether the follower holds a paid X (Twitter) Blue verification. | 关注者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.users.verifiedType` |  | The follower's verification category, such as a business or government account. | 关注者的认证类别，如企业或政府账号。 |
| `resp.200.users.profilePicture` |  | Web link to the follower's avatar image. | 关注者头像图片的网页链接。 |
| `resp.200.users.coverPicture` |  | Web link to the follower's profile banner image. | 关注者资料页横幅图片的网页链接。 |
| `resp.200.users.description` |  | The follower's profile bio text. | 关注者资料页的个人简介文字。 |
| `resp.200.users.location` |  | Free-text location the follower lists on their profile. | 关注者在资料页填写的所在地（自由文本）。 |
| `resp.200.users.followers` |  | Number of accounts following the follower. | 关注该关注者的账号数。 |
| `resp.200.users.following` |  | Number of accounts the follower follows. | 该关注者关注的账号数。 |
| `resp.200.users.canDm` |  | Whether the follower currently accepts direct messages from the requester. | 该关注者当前是否接受请求方的私信。 |
| `resp.200.users.createdAt` |  | Timestamp when the follower's account was created. | 该关注者账号的创建时间。 |
| `resp.200.users.favouritesCount` |  | Number of tweets the follower has liked. | 该关注者点赞过的推文数。 |
| `resp.200.users.hasCustomTimelines` |  | Whether the follower has created custom timelines. | 该关注者是否创建过自定义时间线。 |
| `resp.200.users.isTranslator` |  | Whether the follower participates in the Twitter translation program. | 该关注者是否参与 Twitter 翻译计划。 |
| `resp.200.users.mediaCount` |  | Number of media items the follower has posted. | 该关注者发布过的媒体条目数。 |
| `resp.200.users.statusesCount` |  | Total number of tweets the follower has posted. | 该关注者发布过的推文总数。 |
| `resp.200.users.withheldInCountries` |  | Country codes where the follower's account is withheld for legal reasons. | 因法律原因屏蔽该关注者账号的国家／地区代码列表。 |
| `resp.200.users.possiblySensitive` |  | Whether the follower's posts are flagged as potentially sensitive. | 该关注者的内容是否被标记为可能含敏感信息。 |
| `resp.200.users.pinnedTweetIds` |  | Identifiers of tweets the follower has pinned to the top of their profile. | 该关注者置顶在资料页顶部的推文标识列表。 |
| `resp.200.users.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.users.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.users.unavailable` |  | Whether the follower's account is currently unavailable, for example suspended or deactivated. | 该关注者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.users.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.users.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.status` |  | Outcome marker of the request: success when followers were returned, error otherwise. | 请求结果标记：成功返回关注者为 success，否则为 error。 |
| `resp.200.msg` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/user/info

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get User Info | Fetch the profile of a single user identified by screen name. | 按用户名获取单个用户的资料。 |
| `param:userName` | The screen name of the user | Screen name (@handle, without the @) of the user whose profile you want. | 要查询其资料的用户名（@ 后的部分，不含 @）。 |
| `resp.200.users` |  | Followers of the user, returned for this page. | 本页返回的关注该用户的关注者。 |
| `resp.200.users.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.users.userName` |  | The follower's @handle, unique across X/Twitter and used in profile URLs. | 关注者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.users.url` |  | Web link to the follower's profile page. | 关注者资料页的网页链接。 |
| `resp.200.users.id` |  | Unique identifier of the follower. | 关注者的唯一标识。 |
| `resp.200.users.name` |  | The follower's display name shown on the profile. | 关注者在资料页展示的昵称。 |
| `resp.200.users.isBlueVerified` |  | Whether the follower holds a paid X (Twitter) Blue verification. | 关注者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.users.verifiedType` |  | The follower's verification category, such as a business or government account. | 关注者的认证类别，如企业或政府账号。 |
| `resp.200.users.profilePicture` |  | Web link to the follower's avatar image. | 关注者头像图片的网页链接。 |
| `resp.200.users.coverPicture` |  | Web link to the follower's profile banner image. | 关注者资料页横幅图片的网页链接。 |
| `resp.200.users.description` |  | The follower's profile bio text. | 关注者资料页的个人简介文字。 |
| `resp.200.users.location` |  | Free-text location the follower lists on their profile. | 关注者在资料页填写的所在地（自由文本）。 |
| `resp.200.users.followers` |  | Number of accounts following the follower. | 关注该关注者的账号数。 |
| `resp.200.users.following` |  | Number of accounts the follower follows. | 该关注者关注的账号数。 |
| `resp.200.users.canDm` |  | Whether the follower currently accepts direct messages from the requester. | 该关注者当前是否接受请求方的私信。 |
| `resp.200.users.createdAt` |  | Timestamp when the follower's account was created. | 该关注者账号的创建时间。 |
| `resp.200.users.favouritesCount` |  | Number of tweets the follower has liked. | 该关注者点赞过的推文数。 |
| `resp.200.users.hasCustomTimelines` |  | Whether the follower has created custom timelines. | 该关注者是否创建过自定义时间线。 |
| `resp.200.users.isTranslator` |  | Whether the follower participates in the Twitter translation program. | 该关注者是否参与 Twitter 翻译计划。 |
| `resp.200.users.mediaCount` |  | Number of media items the follower has posted. | 该关注者发布过的媒体条目数。 |
| `resp.200.users.statusesCount` |  | Total number of tweets the follower has posted. | 该关注者发布过的推文总数。 |
| `resp.200.users.withheldInCountries` |  | Country codes where the follower's account is withheld for legal reasons. | 因法律原因屏蔽该关注者账号的国家／地区代码列表。 |
| `resp.200.users.possiblySensitive` |  | Whether the follower's posts are flagged as potentially sensitive. | 该关注者的内容是否被标记为可能含敏感信息。 |
| `resp.200.users.pinnedTweetIds` |  | Identifiers of tweets the follower has pinned to the top of their profile. | 该关注者置顶在资料页顶部的推文标识列表。 |
| `resp.200.users.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.users.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.users.unavailable` |  | Whether the follower's account is currently unavailable, for example suspended or deactivated. | 该关注者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.users.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.users.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.status` |  | Outcome marker of the request: success when followers were returned, error otherwise. | 请求结果标记：成功返回关注者为 success，否则为 error。 |
| `resp.200.msg` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/user/tweet_timeline

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Retrieve tweets by user ID, sorted by created_at in reverse chronological order. Results are paginated with up to 20 tweets per page. The order matches what appears on the user's profile in the Twitter app. Time-based filtering is not supported. | Retrieve a user's own tweets in reverse-chronological order, matching the ordering shown on their profile. Optionally include replies and the parent tweets they reply to; paginate with the cursor. | 按时间倒序获取某个用户自己发布的推文，顺序与其资料页一致。可选择是否包含回复及被回复的父推文，并通过游标翻页。 |
| `param:userId` | User ID of the user whose timeline to retrieve. | Identifier of the user whose timeline to retrieve. | 要获取其时间线的用户标识。 |
| `param:includeReplies` | Whether to include replies in the results. Defaults to false. | Whether replies posted by the user are included alongside their original tweets. | 是否在用户的原创推文之外一并返回其发布的回复。 |
| `param:includeParentTweet` | Whether to include the parent tweet when a tweet is a reply. Defaults to false. | When a returned tweet is a reply, whether to also include the tweet it replies to. | 当返回的推文是一条回复时，是否同时返回其所回复的父推文。 |
| `param:cursor` | Cursor for paginating through results. Leave empty for the first page. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.tweets` |  | The user's most recent tweets returned for this page. | 本页返回的用户最新推文。 |
| `resp.200.tweets.type` |  | Object type tag identifying the entry as a tweet. | 对象类型标记，标识该条目为推文。 |
| `resp.200.tweets.id` |  | Unique identifier of the tweet. | 推文的唯一标识。 |
| `resp.200.tweets.url` |  | Web link to the tweet on X/Twitter. | 推文在 X/Twitter 上的网页链接。 |
| `resp.200.tweets.text` |  | Full text content of the tweet. | 推文的完整正文内容。 |
| `resp.200.tweets.source` |  | Name of the client application used to post the tweet. | 发布该推文所用的客户端应用名称。 |
| `resp.200.tweets.retweetCount` |  | Number of times the tweet has been retweeted. | 推文被转发的次数。 |
| `resp.200.tweets.replyCount` |  | Number of replies to the tweet. | 推文收到的回复数。 |
| `resp.200.tweets.likeCount` |  | Number of likes on the tweet. | 推文获得的点赞数。 |
| `resp.200.tweets.quoteCount` |  | Number of quote tweets referencing this tweet. | 引用该推文的引用推文数。 |
| `resp.200.tweets.viewCount` |  | Number of times the tweet has been viewed. | 推文的浏览次数。 |
| `resp.200.tweets.createdAt` |  | Timestamp when the tweet was created. | 推文的创建时间。 |
| `resp.200.tweets.lang` |  | Detected language of the tweet text, as a language code. | 推文正文被识别出的语言，以语言代码表示。 |
| `resp.200.tweets.bookmarkCount` |  | Number of times the tweet has been bookmarked. | 推文被收藏的次数。 |
| `resp.200.tweets.isReply` |  | Whether the tweet is a reply to another tweet. | 该推文是否为对另一条推文的回复。 |
| `resp.200.tweets.inReplyToId` |  | Identifier of the tweet this one directly replies to; present only when isReply is true. | 该推文直接回复的目标推文标识；仅当 isReply 为真时存在。 |
| `resp.200.tweets.conversationId` |  | Identifier of the root tweet that started the conversation thread this tweet belongs to. | 该推文所属对话线程的起始推文标识。 |
| `resp.200.tweets.displayTextRange` |  | Start and end character offsets marking the displayable portion of the tweet text. | 标记推文正文中可显示部分的起止字符位置。 |
| `resp.200.tweets.inReplyToUserId` |  | Identifier of the user being replied to. | 被回复用户的标识。 |
| `resp.200.tweets.inReplyToUsername` |  | Username of the user being replied to. | 被回复用户的用户名。 |
| `resp.200.has_next_page` |  | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` |  | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` |  | Outcome marker of the request: success when tweets were returned, error otherwise. | 请求结果标记：成功返回推文为 success，否则为 error。 |
| `resp.200.message` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/user/last_tweets

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get User Last Tweets | Retrieve a user's most recent tweets, identified by either user ID or screen name, with optional replies and cursor pagination. | 获取某个用户最近发布的推文，可用用户 ID 或用户名指定，支持可选包含回复及游标翻页。 |
| `param:userId` | User ID of the user | Identifier of the user whose recent tweets to retrieve; provide this or userName. | 要获取其最新推文的用户标识；与 userName 二选一提供。 |
| `param:userName` | Screen name of the user | Screen name of the user whose recent tweets to retrieve; provide this or userId. | 要获取其最新推文的用户名；与 userId 二选一提供。 |
| `param:cursor` | Cursor for pagination | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `param:includeReplies` | Include replies in the results | Whether replies posted by the user are included alongside their original tweets. | 是否在用户的原创推文之外一并返回其发布的回复。 |
| `resp.200.tweets` |  | The user's most recent tweets returned for this page. | 本页返回的用户最新推文。 |
| `resp.200.tweets.type` |  | Object type tag identifying the entry as a tweet. | 对象类型标记，标识该条目为推文。 |
| `resp.200.tweets.id` |  | Unique identifier of the tweet. | 推文的唯一标识。 |
| `resp.200.tweets.url` |  | Web link to the tweet on X/Twitter. | 推文在 X/Twitter 上的网页链接。 |
| `resp.200.tweets.text` |  | Full text content of the tweet. | 推文的完整正文内容。 |
| `resp.200.tweets.source` |  | Name of the client application used to post the tweet. | 发布该推文所用的客户端应用名称。 |
| `resp.200.tweets.retweetCount` |  | Number of times the tweet has been retweeted. | 推文被转发的次数。 |
| `resp.200.tweets.replyCount` |  | Number of replies to the tweet. | 推文收到的回复数。 |
| `resp.200.tweets.likeCount` |  | Number of likes on the tweet. | 推文获得的点赞数。 |
| `resp.200.tweets.quoteCount` |  | Number of quote tweets referencing this tweet. | 引用该推文的引用推文数。 |
| `resp.200.tweets.viewCount` |  | Number of times the tweet has been viewed. | 推文的浏览次数。 |
| `resp.200.tweets.createdAt` |  | Timestamp when the tweet was created. | 推文的创建时间。 |
| `resp.200.tweets.lang` |  | Detected language of the tweet text, as a language code. | 推文正文被识别出的语言，以语言代码表示。 |
| `resp.200.tweets.bookmarkCount` |  | Number of times the tweet has been bookmarked. | 推文被收藏的次数。 |
| `resp.200.tweets.isReply` |  | Whether the tweet is a reply to another tweet. | 该推文是否为对另一条推文的回复。 |
| `resp.200.tweets.inReplyToId` |  | Identifier of the tweet this one directly replies to; present only when isReply is true. | 该推文直接回复的目标推文标识；仅当 isReply 为真时存在。 |
| `resp.200.tweets.conversationId` |  | Identifier of the root tweet that started the conversation thread this tweet belongs to. | 该推文所属对话线程的起始推文标识。 |
| `resp.200.tweets.displayTextRange` |  | Start and end character offsets marking the displayable portion of the tweet text. | 标记推文正文中可显示部分的起止字符位置。 |
| `resp.200.tweets.inReplyToUserId` |  | Identifier of the user being replied to. | 被回复用户的标识。 |
| `resp.200.tweets.inReplyToUsername` |  | Username of the user being replied to. | 被回复用户的用户名。 |
| `resp.200.has_next_page` |  | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` |  | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` |  | Outcome marker of the request: success when tweets were returned, error otherwise. | 请求结果标记：成功返回推文为 success，否则为 error。 |
| `resp.200.message` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/user/followers

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get User Followers | List the accounts that follow a given user, identified by screen name, with cursor pagination and a configurable page size. | 按用户名获取关注某个用户的账号列表，支持游标翻页与可配置的每页数量。 |
| `param:userName` | Screen name of the user | Screen name (@handle, without the @) of the user whose followers you want. | 要查询其关注者的用户名（@ 后的部分，不含 @）。 |
| `param:cursor` | Cursor for pagination | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `param:pageSize` | Number of followers per page | How many followers to return per page. | 每页返回的关注者数量。 |
| `resp.200.users` |  | Followers of the user, returned for this page. | 本页返回的关注该用户的关注者。 |
| `resp.200.users.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.users.userName` |  | The follower's @handle, unique across X/Twitter and used in profile URLs. | 关注者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.users.url` |  | Web link to the follower's profile page. | 关注者资料页的网页链接。 |
| `resp.200.users.id` |  | Unique identifier of the follower. | 关注者的唯一标识。 |
| `resp.200.users.name` |  | The follower's display name shown on the profile. | 关注者在资料页展示的昵称。 |
| `resp.200.users.isBlueVerified` |  | Whether the follower holds a paid X (Twitter) Blue verification. | 关注者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.users.verifiedType` |  | The follower's verification category, such as a business or government account. | 关注者的认证类别，如企业或政府账号。 |
| `resp.200.users.profilePicture` |  | Web link to the follower's avatar image. | 关注者头像图片的网页链接。 |
| `resp.200.users.coverPicture` |  | Web link to the follower's profile banner image. | 关注者资料页横幅图片的网页链接。 |
| `resp.200.users.description` |  | The follower's profile bio text. | 关注者资料页的个人简介文字。 |
| `resp.200.users.location` |  | Free-text location the follower lists on their profile. | 关注者在资料页填写的所在地（自由文本）。 |
| `resp.200.users.followers` |  | Number of accounts following the follower. | 关注该关注者的账号数。 |
| `resp.200.users.following` |  | Number of accounts the follower follows. | 该关注者关注的账号数。 |
| `resp.200.users.canDm` |  | Whether the follower currently accepts direct messages from the requester. | 该关注者当前是否接受请求方的私信。 |
| `resp.200.users.createdAt` |  | Timestamp when the follower's account was created. | 该关注者账号的创建时间。 |
| `resp.200.users.favouritesCount` |  | Number of tweets the follower has liked. | 该关注者点赞过的推文数。 |
| `resp.200.users.hasCustomTimelines` |  | Whether the follower has created custom timelines. | 该关注者是否创建过自定义时间线。 |
| `resp.200.users.isTranslator` |  | Whether the follower participates in the Twitter translation program. | 该关注者是否参与 Twitter 翻译计划。 |
| `resp.200.users.mediaCount` |  | Number of media items the follower has posted. | 该关注者发布过的媒体条目数。 |
| `resp.200.users.statusesCount` |  | Total number of tweets the follower has posted. | 该关注者发布过的推文总数。 |
| `resp.200.users.withheldInCountries` |  | Country codes where the follower's account is withheld for legal reasons. | 因法律原因屏蔽该关注者账号的国家／地区代码列表。 |
| `resp.200.users.possiblySensitive` |  | Whether the follower's posts are flagged as potentially sensitive. | 该关注者的内容是否被标记为可能含敏感信息。 |
| `resp.200.users.pinnedTweetIds` |  | Identifiers of tweets the follower has pinned to the top of their profile. | 该关注者置顶在资料页顶部的推文标识列表。 |
| `resp.200.users.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.users.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.users.unavailable` |  | Whether the follower's account is currently unavailable, for example suspended or deactivated. | 该关注者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.users.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.users.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.status` |  | Outcome marker of the request: success when followers were returned, error otherwise. | 请求结果标记：成功返回关注者为 success，否则为 error。 |
| `resp.200.msg` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

