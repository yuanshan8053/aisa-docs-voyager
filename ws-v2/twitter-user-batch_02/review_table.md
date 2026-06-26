# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 5 个接口，181 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## GET /twitter/user/followings

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get user followings. Each page returns exactly 200 followings. Use cursor for pagination. | List the accounts a given user follows, identified by screen name, with cursor pagination and a configurable page size. | 按用户名获取某个用户所关注的账号列表，支持游标翻页与可配置的每页数量。 |
| `param:userName` | Screen name of the user. | Screen name (@handle, without the @) of the user whose followings you want. | 要查询其关注列表的用户名（@ 后的部分，不含 @）。 |
| `param:cursor` | The cursor to paginate through the results. First page is empty. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `param:pageSize` | The number of followings to return per page. | How many followings to return per page. | 每页返回的关注账号数量。 |
| `resp.200.followings` |  | Accounts the user follows, returned for this page. | 本页返回的该用户所关注的账号。 |
| `resp.200.followings.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.followings.userName` |  | The follower's @handle, unique across X/Twitter and used in profile URLs. | 关注者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.followings.url` |  | Web link to the follower's profile page. | 关注者资料页的网页链接。 |
| `resp.200.followings.id` |  | Unique identifier of the follower. | 关注者的唯一标识。 |
| `resp.200.followings.name` |  | The follower's display name shown on the profile. | 关注者在资料页展示的昵称。 |
| `resp.200.followings.isBlueVerified` |  | Whether the follower holds a paid X (Twitter) Blue verification. | 关注者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.followings.verifiedType` |  | The follower's verification category, such as a business or government account. | 关注者的认证类别，如企业或政府账号。 |
| `resp.200.followings.profilePicture` |  | Web link to the follower's avatar image. | 关注者头像图片的网页链接。 |
| `resp.200.followings.coverPicture` |  | Web link to the follower's profile banner image. | 关注者资料页横幅图片的网页链接。 |
| `resp.200.followings.description` |  | The follower's profile bio text. | 关注者资料页的个人简介文字。 |
| `resp.200.followings.location` |  | Free-text location the follower lists on their profile. | 关注者在资料页填写的所在地（自由文本）。 |
| `resp.200.followings.followers` |  | Number of accounts following the follower. | 关注该关注者的账号数。 |
| `resp.200.followings.following` |  | Number of accounts the follower follows. | 该关注者关注的账号数。 |
| `resp.200.followings.canDm` |  | Whether the follower currently accepts direct messages from the requester. | 该关注者当前是否接受请求方的私信。 |
| `resp.200.followings.createdAt` |  | Timestamp when the follower's account was created. | 该关注者账号的创建时间。 |
| `resp.200.followings.favouritesCount` |  | Number of tweets the follower has liked. | 该关注者点赞过的推文数。 |
| `resp.200.followings.hasCustomTimelines` |  | Whether the follower has created custom timelines. | 该关注者是否创建过自定义时间线。 |
| `resp.200.followings.isTranslator` |  | Whether the follower participates in the Twitter translation program. | 该关注者是否参与 Twitter 翻译计划。 |
| `resp.200.followings.mediaCount` |  | Number of media items the follower has posted. | 该关注者发布过的媒体条目数。 |
| `resp.200.followings.statusesCount` |  | Total number of tweets the follower has posted. | 该关注者发布过的推文总数。 |
| `resp.200.followings.withheldInCountries` |  | Country codes where the follower's account is withheld for legal reasons. | 因法律原因屏蔽该关注者账号的国家／地区代码列表。 |
| `resp.200.followings.possiblySensitive` |  | Whether the follower's posts are flagged as potentially sensitive. | 该关注者的内容是否被标记为可能含敏感信息。 |
| `resp.200.followings.pinnedTweetIds` |  | Identifiers of tweets the follower has pinned to the top of their profile. | 该关注者置顶在资料页顶部的推文标识列表。 |
| `resp.200.followings.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.followings.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.followings.unavailable` |  | Whether the follower's account is currently unavailable, for example suspended or deactivated. | 该关注者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.followings.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.followings.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.has_next_page` |  | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` |  | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` |  | Outcome marker of the request: success when followings were returned, error otherwise. | 请求结果标记：成功返回关注列表为 success，否则为 error。 |
| `resp.200.message` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/user/mentions

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get tweet mentions by user screen name. Each page returns exactly 20 mentions. | List tweets that mention a given user by screen name, in reverse-chronological order, optionally bounded by a time window and paginated with the cursor. | 按用户名获取提及该用户的推文，按时间倒序排列，可选用时间窗口限定范围并通过游标翻页。 |
| `param:userName` | The user screen name to get mentions for. | Screen name (@handle, without the @) of the user whose mentions you want. | 要查询其被提及推文的用户名（@ 后的部分，不含 @）。 |
| `param:sinceTime` | On or after a specified unix timestamp in seconds. | Only return mentions posted at or after this Unix timestamp in seconds. | 仅返回在该 Unix 时间戳（秒）当时或之后发布的提及推文。 |
| `param:untilTime` | Before a specified unix timestamp in seconds. | Only return mentions posted before this Unix timestamp in seconds. | 仅返回在该 Unix 时间戳（秒）之前发布的提及推文。 |
| `param:cursor` | The cursor to paginate through the results. First page is empty. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.tweets` |  | Tweets that mention the user, returned for this page. | 本页返回的提及该用户的推文。 |
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
| `resp.200.tweets.author` |  | Profile of the user who posted the tweet. | 发布该推文的用户资料。 |
| `resp.200.tweets.author.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.tweets.author.userName` |  | The follower's @handle, unique across X/Twitter and used in profile URLs. | 关注者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.tweets.author.url` |  | Web link to the follower's profile page. | 关注者资料页的网页链接。 |
| `resp.200.tweets.author.id` |  | Unique identifier of the follower. | 关注者的唯一标识。 |
| `resp.200.tweets.author.name` |  | The follower's display name shown on the profile. | 关注者在资料页展示的昵称。 |
| `resp.200.tweets.author.isBlueVerified` |  | Whether the follower holds a paid X (Twitter) Blue verification. | 关注者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.tweets.author.verifiedType` |  | The follower's verification category, such as a business or government account. | 关注者的认证类别，如企业或政府账号。 |
| `resp.200.tweets.author.profilePicture` |  | Web link to the follower's avatar image. | 关注者头像图片的网页链接。 |
| `resp.200.tweets.author.coverPicture` |  | Web link to the follower's profile banner image. | 关注者资料页横幅图片的网页链接。 |
| `resp.200.tweets.author.description` |  | The follower's profile bio text. | 关注者资料页的个人简介文字。 |
| `resp.200.tweets.author.location` |  | Free-text location the follower lists on their profile. | 关注者在资料页填写的所在地（自由文本）。 |
| `resp.200.tweets.author.followers` |  | Number of accounts following the follower. | 关注该关注者的账号数。 |
| `resp.200.tweets.author.following` |  | Number of accounts the follower follows. | 该关注者关注的账号数。 |
| `resp.200.tweets.author.canDm` |  | Whether the follower currently accepts direct messages from the requester. | 该关注者当前是否接受请求方的私信。 |
| `resp.200.tweets.author.createdAt` |  | Timestamp when the follower's account was created. | 该关注者账号的创建时间。 |
| `resp.200.tweets.author.favouritesCount` |  | Number of tweets the follower has liked. | 该关注者点赞过的推文数。 |
| `resp.200.tweets.author.hasCustomTimelines` |  | Whether the follower has created custom timelines. | 该关注者是否创建过自定义时间线。 |
| `resp.200.tweets.author.isTranslator` |  | Whether the follower participates in the Twitter translation program. | 该关注者是否参与 Twitter 翻译计划。 |
| `resp.200.tweets.author.mediaCount` |  | Number of media items the follower has posted. | 该关注者发布过的媒体条目数。 |
| `resp.200.tweets.author.statusesCount` |  | Total number of tweets the follower has posted. | 该关注者发布过的推文总数。 |
| `resp.200.tweets.author.withheldInCountries` |  | Country codes where the follower's account is withheld for legal reasons. | 因法律原因屏蔽该关注者账号的国家／地区代码列表。 |
| `resp.200.tweets.author.possiblySensitive` |  | Whether the follower's posts are flagged as potentially sensitive. | 该关注者的内容是否被标记为可能含敏感信息。 |
| `resp.200.tweets.author.pinnedTweetIds` |  | Identifiers of tweets the follower has pinned to the top of their profile. | 该关注者置顶在资料页顶部的推文标识列表。 |
| `resp.200.tweets.author.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.tweets.author.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.tweets.author.unavailable` |  | Whether the follower's account is currently unavailable, for example suspended or deactivated. | 该关注者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.tweets.author.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.tweets.author.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.tweets.entities` |  | Structured entities parsed from the tweet text, such as hashtags, links, and user mentions. | 从推文正文解析出的结构化实体，如话题标签、链接与用户提及。 |
| `resp.200.tweets.entities.hashtags` |  | Hashtags found in the tweet text. | 推文正文中出现的话题标签。 |
| `resp.200.tweets.entities.hashtags.indices` |  | Start and end character offsets of the hashtag within the tweet text. | 该话题标签在推文正文中的起止字符位置。 |
| `resp.200.tweets.entities.hashtags.text` |  | The hashtag word, without the leading # sign. | 话题标签的文字，不含开头的 # 号。 |
| `resp.200.tweets.entities.urls` |  | Links found in the tweet text. | 推文正文中出现的链接。 |
| `resp.200.tweets.entities.urls.display_url` |  | Shortened, human-readable form of the link as displayed in the tweet. | 推文中显示的链接的短化、易读形式。 |
| `resp.200.tweets.entities.urls.expanded_url` |  | Full destination URL the displayed link resolves to. | 显示链接最终指向的完整目标地址。 |
| `resp.200.tweets.entities.urls.indices` |  | Start and end character offsets of the link within the tweet text. | 该链接在推文正文中的起止字符位置。 |
| `resp.200.tweets.entities.urls.url` |  | The t.co shortened URL as it literally appears in the tweet text. | 推文正文中实际出现的 t.co 短链接。 |
| `resp.200.tweets.entities.user_mentions` |  | Users mentioned in the tweet text. | 推文正文中提及的用户。 |
| `resp.200.tweets.entities.user_mentions.id_str` |  | Identifier of the mentioned user. | 被提及用户的标识。 |
| `resp.200.tweets.entities.user_mentions.name` |  | Display name of the mentioned user. | 被提及用户的昵称。 |
| `resp.200.tweets.entities.user_mentions.screen_name` |  | @handle of the mentioned user. | 被提及用户的 @ 用户名。 |
| `resp.200.has_next_page` |  | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` |  | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` |  | Outcome marker of the request: success when mentions were returned, error otherwise. | 请求结果标记：成功返回提及推文为 success，否则为 error。 |
| `resp.200.message` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/user/check_follow_relationship

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Check if the user is following/followed by the target user. | Check the directional follow relationship between a source user and a target user: whether the source follows the target and whether the target follows the source back. | 查询来源用户与目标用户之间的关注关系方向：来源用户是否关注目标用户，以及目标用户是否回关来源用户。 |
| `param:source_user_name` | Screen name of the source user. | Screen name of the source user whose follow direction is being checked. | 作为关注关系起点被检查的来源用户名。 |
| `param:target_user_name` | Screen name of the target user. | Screen name of the target user the relationship is checked against. | 作为关注关系对照对象的目标用户名。 |
| `resp.200.data` |  | The directional follow relationship between the two users. | 两个用户之间的关注关系方向。 |
| `resp.200.data.following` |  | Whether the source user follows the target user. | 来源用户是否关注目标用户。 |
| `resp.200.data.followed_by` |  | Whether the target user follows the source user back. | 目标用户是否回关来源用户。 |
| `resp.200.status` |  | Outcome marker of the request: success when the relationship was returned, error otherwise. | 请求结果标记：成功返回关系为 success，否则为 error。 |
| `resp.200.message` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/user/search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Search user by keyword. | Search for users whose profile matches a keyword, paginated with the cursor. | 按关键词搜索资料匹配的用户，并通过游标翻页。 |
| `param:query` | The keyword to search. | Keyword to match against user profiles when searching. | 用于匹配用户资料的搜索关键词。 |
| `param:cursor` | The cursor to paginate through the results. First page is empty. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.users` |  | Users matching the keyword, returned for this page. | 本页返回的匹配关键词的用户。 |
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
| `resp.200.has_next_page` |  | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` |  | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` |  | Outcome marker of the request: success when users were returned, error otherwise. | 请求结果标记：成功返回用户为 success，否则为 error。 |
| `resp.200.msg` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/user/verifiedFollowers

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get user verified followers in reverse chronological order. | List the verified accounts that follow a given user, identified by user ID, in reverse-chronological order with cursor pagination. | 按用户 ID 获取关注某个用户的认证账号，按时间倒序排列并通过游标翻页。 |
| `param:user_id` | User ID of the user. | Identifier of the user whose verified followers you want. | 要查询其认证关注者的用户标识。 |
| `param:cursor` | The cursor to paginate through the results. First page is empty. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.followers` |  | Verified accounts following the user, returned for this page. | 本页返回的关注该用户的认证账号。 |
| `resp.200.followers.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.followers.userName` |  | The follower's @handle, unique across X/Twitter and used in profile URLs. | 关注者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.followers.url` |  | Web link to the follower's profile page. | 关注者资料页的网页链接。 |
| `resp.200.followers.id` |  | Unique identifier of the follower. | 关注者的唯一标识。 |
| `resp.200.followers.name` |  | The follower's display name shown on the profile. | 关注者在资料页展示的昵称。 |
| `resp.200.followers.isBlueVerified` |  | Whether the follower holds a paid X (Twitter) Blue verification. | 关注者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.followers.verifiedType` |  | The follower's verification category, such as a business or government account. | 关注者的认证类别，如企业或政府账号。 |
| `resp.200.followers.profilePicture` |  | Web link to the follower's avatar image. | 关注者头像图片的网页链接。 |
| `resp.200.followers.coverPicture` |  | Web link to the follower's profile banner image. | 关注者资料页横幅图片的网页链接。 |
| `resp.200.followers.description` |  | The follower's profile bio text. | 关注者资料页的个人简介文字。 |
| `resp.200.followers.location` |  | Free-text location the follower lists on their profile. | 关注者在资料页填写的所在地（自由文本）。 |
| `resp.200.followers.followers` |  | Number of accounts following the follower. | 关注该关注者的账号数。 |
| `resp.200.followers.following` |  | Number of accounts the follower follows. | 该关注者关注的账号数。 |
| `resp.200.followers.canDm` |  | Whether the follower currently accepts direct messages from the requester. | 该关注者当前是否接受请求方的私信。 |
| `resp.200.followers.createdAt` |  | Timestamp when the follower's account was created. | 该关注者账号的创建时间。 |
| `resp.200.followers.favouritesCount` |  | Number of tweets the follower has liked. | 该关注者点赞过的推文数。 |
| `resp.200.followers.hasCustomTimelines` |  | Whether the follower has created custom timelines. | 该关注者是否创建过自定义时间线。 |
| `resp.200.followers.isTranslator` |  | Whether the follower participates in the Twitter translation program. | 该关注者是否参与 Twitter 翻译计划。 |
| `resp.200.followers.mediaCount` |  | Number of media items the follower has posted. | 该关注者发布过的媒体条目数。 |
| `resp.200.followers.statusesCount` |  | Total number of tweets the follower has posted. | 该关注者发布过的推文总数。 |
| `resp.200.followers.withheldInCountries` |  | Country codes where the follower's account is withheld for legal reasons. | 因法律原因屏蔽该关注者账号的国家／地区代码列表。 |
| `resp.200.followers.possiblySensitive` |  | Whether the follower's posts are flagged as potentially sensitive. | 该关注者的内容是否被标记为可能含敏感信息。 |
| `resp.200.followers.pinnedTweetIds` |  | Identifiers of tweets the follower has pinned to the top of their profile. | 该关注者置顶在资料页顶部的推文标识列表。 |
| `resp.200.followers.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.followers.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.followers.unavailable` |  | Whether the follower's account is currently unavailable, for example suspended or deactivated. | 该关注者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.followers.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.followers.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.status` |  | Outcome marker of the request: success when followers were returned, error otherwise. | 请求结果标记：成功返回关注者为 success，否则为 error。 |
| `resp.200.message` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

