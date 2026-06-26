# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 4 个接口，245 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## GET /twitter/tweets

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Tweets by IDs | Look up the full content of multiple tweets in one call by passing their tweet IDs. | 一次请求传入多个推文 ID，批量查询这些推文的完整内容。 |
| `param:tweet_ids` | Comma-separated list of tweet IDs. | Comma-separated list of tweet IDs to look up in this batch. | 本次批量查询的推文 ID 列表，以逗号分隔。 |
| `resp.200.tweets` |  | The requested tweets, one entry per matched ID. | 所查询的推文，每个匹配到的 ID 对应一条。 |
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
| `resp.200.tweets.author.userName` |  | The user's @handle, unique across X/Twitter and used in profile URLs. | 用户的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.tweets.author.url` |  | Web link to the user's profile page. | 用户资料页的网页链接。 |
| `resp.200.tweets.author.id` |  | Unique identifier of the user. | 用户的唯一标识。 |
| `resp.200.tweets.author.name` |  | The user's display name shown on the profile. | 用户在资料页展示的昵称。 |
| `resp.200.tweets.author.isBlueVerified` |  | Whether the user holds a paid X (Twitter) Blue verification. | 用户是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.tweets.author.verifiedType` |  | The user's verification category, such as a business or government account. | 用户的认证类别，如企业或政府账号。 |
| `resp.200.tweets.author.profilePicture` |  | Web link to the user's avatar image. | 用户头像图片的网页链接。 |
| `resp.200.tweets.author.coverPicture` |  | Web link to the user's profile banner image. | 用户资料页横幅图片的网页链接。 |
| `resp.200.tweets.author.description` |  | The user's profile bio text. | 用户资料页的个人简介文字。 |
| `resp.200.tweets.author.location` |  | Free-text location the user lists on their profile. | 用户在资料页填写的所在地（自由文本）。 |
| `resp.200.tweets.author.followers` |  | Number of accounts following the user. | 关注该用户的账号数。 |
| `resp.200.tweets.author.following` |  | Number of accounts the user follows. | 该用户关注的账号数。 |
| `resp.200.tweets.author.canDm` |  | Whether the user currently accepts direct messages from the requester. | 该用户当前是否接受请求方的私信。 |
| `resp.200.tweets.author.createdAt` |  | Timestamp when the user's account was created. | 该用户账号的创建时间。 |
| `resp.200.tweets.author.favouritesCount` |  | Number of tweets the user has liked. | 该用户点赞过的推文数。 |
| `resp.200.tweets.author.hasCustomTimelines` |  | Whether the user has created custom timelines. | 该用户是否创建过自定义时间线。 |
| `resp.200.tweets.author.isTranslator` |  | Whether the user participates in the Twitter translation program. | 该用户是否参与 Twitter 翻译计划。 |
| `resp.200.tweets.author.mediaCount` |  | Number of media items the user has posted. | 该用户发布过的媒体条目数。 |
| `resp.200.tweets.author.statusesCount` |  | Total number of tweets the user has posted. | 该用户发布过的推文总数。 |
| `resp.200.tweets.author.withheldInCountries` |  | Country codes where the user's account is withheld for legal reasons. | 因法律原因屏蔽该用户账号的国家／地区代码列表。 |
| `resp.200.tweets.author.possiblySensitive` |  | Whether the user's posts are flagged as potentially sensitive. | 该用户的内容是否被标记为可能含敏感信息。 |
| `resp.200.tweets.author.pinnedTweetIds` |  | Identifiers of tweets the user has pinned to the top of their profile. | 该用户置顶在资料页顶部的推文标识列表。 |
| `resp.200.tweets.author.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.tweets.author.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.tweets.author.unavailable` |  | Whether the user's account is currently unavailable, for example suspended or deactivated. | 该用户账号当前是否不可用，例如被封禁或停用。 |
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
| `resp.200.tweets.quoted_tweet` |  | The tweet quoted by this tweet, when it is a quote tweet.<br>[⚠️Note:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] | 当该推文为引用推文时，其所引用的推文。<br>[⚠️批注:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] |
| `resp.200.tweets.retweeted_tweet` |  | The original tweet this tweet retweets, when it is a retweet.<br>[⚠️Note:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] | 当该推文为转发时，其所转发的原推文。<br>[⚠️批注:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] |
| `resp.200.tweets.isLimitedReply` |  | Whether replies to this tweet are restricted by the author's reply settings. | 该推文的回复是否受作者的回复权限设置限制。 |
| `resp.200.status` |  | Outcome marker of the request, such as success or error. | 请求结果标记，如成功或失败。 |
| `resp.200.message` |  | Human-readable message; carries the error detail on failure. | 可读的提示信息；失败时承载错误详情。 |

## GET /twitter/tweet/replies

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Tweet Replies | List the replies to a given tweet, paginated with the cursor. | 获取某条推文下的回复，并通过游标翻页。 |
| `param:tweetId` | The tweet ID to get replies for. | Identifier of the tweet whose replies you want. | 要获取其回复的推文标识。 |
| `param:cursor` | Cursor for pagination. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.replies` |  | Reply tweets to the target tweet, returned for this page. | 本页返回的针对目标推文的回复推文。 |
| `resp.200.replies.type` |  | Object type tag identifying the entry as a tweet. | 对象类型标记，标识该条目为推文。 |
| `resp.200.replies.id` |  | Unique identifier of the tweet. | 推文的唯一标识。 |
| `resp.200.replies.url` |  | Web link to the tweet on X/Twitter. | 推文在 X/Twitter 上的网页链接。 |
| `resp.200.replies.text` |  | Full text content of the tweet. | 推文的完整正文内容。 |
| `resp.200.replies.source` |  | Name of the client application used to post the tweet. | 发布该推文所用的客户端应用名称。 |
| `resp.200.replies.retweetCount` |  | Number of times the tweet has been retweeted. | 推文被转发的次数。 |
| `resp.200.replies.replyCount` |  | Number of replies to the tweet. | 推文收到的回复数。 |
| `resp.200.replies.likeCount` |  | Number of likes on the tweet. | 推文获得的点赞数。 |
| `resp.200.replies.quoteCount` |  | Number of quote tweets referencing this tweet. | 引用该推文的引用推文数。 |
| `resp.200.replies.viewCount` |  | Number of times the tweet has been viewed. | 推文的浏览次数。 |
| `resp.200.replies.createdAt` |  | Timestamp when the tweet was created. | 推文的创建时间。 |
| `resp.200.replies.lang` |  | Detected language of the tweet text, as a language code. | 推文正文被识别出的语言，以语言代码表示。 |
| `resp.200.replies.bookmarkCount` |  | Number of times the tweet has been bookmarked. | 推文被收藏的次数。 |
| `resp.200.replies.isReply` |  | Whether the tweet is a reply to another tweet. | 该推文是否为对另一条推文的回复。 |
| `resp.200.replies.inReplyToId` |  | Identifier of the tweet this one directly replies to; present only when isReply is true. | 该推文直接回复的目标推文标识；仅当 isReply 为真时存在。 |
| `resp.200.replies.conversationId` |  | Identifier of the root tweet that started the conversation thread this tweet belongs to. | 该推文所属对话线程的起始推文标识。 |
| `resp.200.replies.displayTextRange` |  | Start and end character offsets marking the displayable portion of the tweet text. | 标记推文正文中可显示部分的起止字符位置。 |
| `resp.200.replies.inReplyToUserId` |  | Identifier of the user being replied to. | 被回复用户的标识。 |
| `resp.200.replies.inReplyToUsername` |  | Username of the user being replied to. | 被回复用户的用户名。 |
| `resp.200.replies.author` |  | Profile of the user who posted the tweet. | 发布该推文的用户资料。 |
| `resp.200.replies.author.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.replies.author.userName` |  | The user's @handle, unique across X/Twitter and used in profile URLs. | 用户的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.replies.author.url` |  | Web link to the user's profile page. | 用户资料页的网页链接。 |
| `resp.200.replies.author.id` |  | Unique identifier of the user. | 用户的唯一标识。 |
| `resp.200.replies.author.name` |  | The user's display name shown on the profile. | 用户在资料页展示的昵称。 |
| `resp.200.replies.author.isBlueVerified` |  | Whether the user holds a paid X (Twitter) Blue verification. | 用户是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.replies.author.verifiedType` |  | The user's verification category, such as a business or government account. | 用户的认证类别，如企业或政府账号。 |
| `resp.200.replies.author.profilePicture` |  | Web link to the user's avatar image. | 用户头像图片的网页链接。 |
| `resp.200.replies.author.coverPicture` |  | Web link to the user's profile banner image. | 用户资料页横幅图片的网页链接。 |
| `resp.200.replies.author.description` |  | The user's profile bio text. | 用户资料页的个人简介文字。 |
| `resp.200.replies.author.location` |  | Free-text location the user lists on their profile. | 用户在资料页填写的所在地（自由文本）。 |
| `resp.200.replies.author.followers` |  | Number of accounts following the user. | 关注该用户的账号数。 |
| `resp.200.replies.author.following` |  | Number of accounts the user follows. | 该用户关注的账号数。 |
| `resp.200.replies.author.canDm` |  | Whether the user currently accepts direct messages from the requester. | 该用户当前是否接受请求方的私信。 |
| `resp.200.replies.author.createdAt` |  | Timestamp when the user's account was created. | 该用户账号的创建时间。 |
| `resp.200.replies.author.favouritesCount` |  | Number of tweets the user has liked. | 该用户点赞过的推文数。 |
| `resp.200.replies.author.hasCustomTimelines` |  | Whether the user has created custom timelines. | 该用户是否创建过自定义时间线。 |
| `resp.200.replies.author.isTranslator` |  | Whether the user participates in the Twitter translation program. | 该用户是否参与 Twitter 翻译计划。 |
| `resp.200.replies.author.mediaCount` |  | Number of media items the user has posted. | 该用户发布过的媒体条目数。 |
| `resp.200.replies.author.statusesCount` |  | Total number of tweets the user has posted. | 该用户发布过的推文总数。 |
| `resp.200.replies.author.withheldInCountries` |  | Country codes where the user's account is withheld for legal reasons. | 因法律原因屏蔽该用户账号的国家／地区代码列表。 |
| `resp.200.replies.author.possiblySensitive` |  | Whether the user's posts are flagged as potentially sensitive. | 该用户的内容是否被标记为可能含敏感信息。 |
| `resp.200.replies.author.pinnedTweetIds` |  | Identifiers of tweets the user has pinned to the top of their profile. | 该用户置顶在资料页顶部的推文标识列表。 |
| `resp.200.replies.author.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.replies.author.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.replies.author.unavailable` |  | Whether the user's account is currently unavailable, for example suspended or deactivated. | 该用户账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.replies.author.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.replies.author.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.replies.entities` |  | Structured entities parsed from the tweet text, such as hashtags, links, and user mentions. | 从推文正文解析出的结构化实体，如话题标签、链接与用户提及。 |
| `resp.200.replies.entities.hashtags` |  | Hashtags found in the tweet text. | 推文正文中出现的话题标签。 |
| `resp.200.replies.entities.hashtags.indices` |  | Start and end character offsets of the hashtag within the tweet text. | 该话题标签在推文正文中的起止字符位置。 |
| `resp.200.replies.entities.hashtags.text` |  | The hashtag word, without the leading # sign. | 话题标签的文字，不含开头的 # 号。 |
| `resp.200.replies.entities.urls` |  | Links found in the tweet text. | 推文正文中出现的链接。 |
| `resp.200.replies.entities.urls.display_url` |  | Shortened, human-readable form of the link as displayed in the tweet. | 推文中显示的链接的短化、易读形式。 |
| `resp.200.replies.entities.urls.expanded_url` |  | Full destination URL the displayed link resolves to. | 显示链接最终指向的完整目标地址。 |
| `resp.200.replies.entities.urls.indices` |  | Start and end character offsets of the link within the tweet text. | 该链接在推文正文中的起止字符位置。 |
| `resp.200.replies.entities.urls.url` |  | The t.co shortened URL as it literally appears in the tweet text. | 推文正文中实际出现的 t.co 短链接。 |
| `resp.200.replies.entities.user_mentions` |  | Users mentioned in the tweet text. | 推文正文中提及的用户。 |
| `resp.200.replies.entities.user_mentions.id_str` |  | Identifier of the mentioned user. | 被提及用户的标识。 |
| `resp.200.replies.entities.user_mentions.name` |  | Display name of the mentioned user. | 被提及用户的昵称。 |
| `resp.200.replies.entities.user_mentions.screen_name` |  | @handle of the mentioned user. | 被提及用户的 @ 用户名。 |
| `resp.200.replies.quoted_tweet` |  | The tweet quoted by this tweet, when it is a quote tweet.<br>[⚠️Note:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] | 当该推文为引用推文时，其所引用的推文。<br>[⚠️批注:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] |
| `resp.200.replies.retweeted_tweet` |  | The original tweet this tweet retweets, when it is a retweet.<br>[⚠️Note:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] | 当该推文为转发时，其所转发的原推文。<br>[⚠️批注:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] |
| `resp.200.replies.isLimitedReply` |  | Whether replies to this tweet are restricted by the author's reply settings. | 该推文的回复是否受作者的回复权限设置限制。 |
| `resp.200.has_next_page` |  | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` |  | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` |  | Outcome marker of the request, such as success or error. | 请求结果标记，如成功或失败。 |
| `resp.200.message` |  | Human-readable message; carries the error detail on failure. | 可读的提示信息；失败时承载错误详情。 |

## GET /twitter/tweet/quotes

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Tweet Quotations | List the quote tweets that reference a given tweet, paginated with the cursor. | 获取引用了某条推文的引用推文，并通过游标翻页。 |
| `param:tweetId` | The tweet ID to get quotes for. | Identifier of the tweet whose quote tweets you want. | 要获取其引用推文的推文标识。 |
| `param:cursor` | Cursor for pagination. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.tweets` |  | Quote tweets referencing the target tweet, returned for this page. | 本页返回的引用了目标推文的引用推文。 |
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
| `resp.200.tweets.author.userName` |  | The user's @handle, unique across X/Twitter and used in profile URLs. | 用户的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.tweets.author.url` |  | Web link to the user's profile page. | 用户资料页的网页链接。 |
| `resp.200.tweets.author.id` |  | Unique identifier of the user. | 用户的唯一标识。 |
| `resp.200.tweets.author.name` |  | The user's display name shown on the profile. | 用户在资料页展示的昵称。 |
| `resp.200.tweets.author.isBlueVerified` |  | Whether the user holds a paid X (Twitter) Blue verification. | 用户是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.tweets.author.verifiedType` |  | The user's verification category, such as a business or government account. | 用户的认证类别，如企业或政府账号。 |
| `resp.200.tweets.author.profilePicture` |  | Web link to the user's avatar image. | 用户头像图片的网页链接。 |
| `resp.200.tweets.author.coverPicture` |  | Web link to the user's profile banner image. | 用户资料页横幅图片的网页链接。 |
| `resp.200.tweets.author.description` |  | The user's profile bio text. | 用户资料页的个人简介文字。 |
| `resp.200.tweets.author.location` |  | Free-text location the user lists on their profile. | 用户在资料页填写的所在地（自由文本）。 |
| `resp.200.tweets.author.followers` |  | Number of accounts following the user. | 关注该用户的账号数。 |
| `resp.200.tweets.author.following` |  | Number of accounts the user follows. | 该用户关注的账号数。 |
| `resp.200.tweets.author.canDm` |  | Whether the user currently accepts direct messages from the requester. | 该用户当前是否接受请求方的私信。 |
| `resp.200.tweets.author.createdAt` |  | Timestamp when the user's account was created. | 该用户账号的创建时间。 |
| `resp.200.tweets.author.favouritesCount` |  | Number of tweets the user has liked. | 该用户点赞过的推文数。 |
| `resp.200.tweets.author.hasCustomTimelines` |  | Whether the user has created custom timelines. | 该用户是否创建过自定义时间线。 |
| `resp.200.tweets.author.isTranslator` |  | Whether the user participates in the Twitter translation program. | 该用户是否参与 Twitter 翻译计划。 |
| `resp.200.tweets.author.mediaCount` |  | Number of media items the user has posted. | 该用户发布过的媒体条目数。 |
| `resp.200.tweets.author.statusesCount` |  | Total number of tweets the user has posted. | 该用户发布过的推文总数。 |
| `resp.200.tweets.author.withheldInCountries` |  | Country codes where the user's account is withheld for legal reasons. | 因法律原因屏蔽该用户账号的国家／地区代码列表。 |
| `resp.200.tweets.author.possiblySensitive` |  | Whether the user's posts are flagged as potentially sensitive. | 该用户的内容是否被标记为可能含敏感信息。 |
| `resp.200.tweets.author.pinnedTweetIds` |  | Identifiers of tweets the user has pinned to the top of their profile. | 该用户置顶在资料页顶部的推文标识列表。 |
| `resp.200.tweets.author.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.tweets.author.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.tweets.author.unavailable` |  | Whether the user's account is currently unavailable, for example suspended or deactivated. | 该用户账号当前是否不可用，例如被封禁或停用。 |
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
| `resp.200.tweets.quoted_tweet` |  | The tweet quoted by this tweet, when it is a quote tweet.<br>[⚠️Note:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] | 当该推文为引用推文时，其所引用的推文。<br>[⚠️批注:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] |
| `resp.200.tweets.retweeted_tweet` |  | The original tweet this tweet retweets, when it is a retweet.<br>[⚠️Note:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] | 当该推文为转发时，其所转发的原推文。<br>[⚠️批注:源码将该字段声明为 string 类型，但其承载的具体内容（如完整推文对象或推文 ID）未声明，待研发确认。] |
| `resp.200.tweets.isLimitedReply` |  | Whether replies to this tweet are restricted by the author's reply settings. | 该推文的回复是否受作者的回复权限设置限制。 |
| `resp.200.has_next_page` |  | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` |  | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` |  | Outcome marker of the request, such as success or error. | 请求结果标记，如成功或失败。 |
| `resp.200.message` |  | Human-readable message; carries the error detail on failure. | 可读的提示信息；失败时承载错误详情。 |

## GET /twitter/tweet/retweeters

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get Tweet Retweeters | List the users who retweeted a given tweet, paginated with the cursor. | 获取转发了某条推文的用户，并通过游标翻页。 |
| `param:tweetId` | The tweet ID to get retweeters for. | Identifier of the tweet whose retweeters you want. | 要获取其转发者的推文标识。 |
| `param:cursor` | Cursor for pagination. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.users` |  | Users who retweeted the target tweet, returned for this page. | 本页返回的转发了目标推文的用户。 |
| `resp.200.users.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.users.userName` |  | The user's @handle, unique across X/Twitter and used in profile URLs. | 用户的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.users.url` |  | Web link to the user's profile page. | 用户资料页的网页链接。 |
| `resp.200.users.id` |  | Unique identifier of the user. | 用户的唯一标识。 |
| `resp.200.users.name` |  | The user's display name shown on the profile. | 用户在资料页展示的昵称。 |
| `resp.200.users.isBlueVerified` |  | Whether the user holds a paid X (Twitter) Blue verification. | 用户是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.users.verifiedType` |  | The user's verification category, such as a business or government account. | 用户的认证类别，如企业或政府账号。 |
| `resp.200.users.profilePicture` |  | Web link to the user's avatar image. | 用户头像图片的网页链接。 |
| `resp.200.users.coverPicture` |  | Web link to the user's profile banner image. | 用户资料页横幅图片的网页链接。 |
| `resp.200.users.description` |  | The user's profile bio text. | 用户资料页的个人简介文字。 |
| `resp.200.users.location` |  | Free-text location the user lists on their profile. | 用户在资料页填写的所在地（自由文本）。 |
| `resp.200.users.followers` |  | Number of accounts following the user. | 关注该用户的账号数。 |
| `resp.200.users.following` |  | Number of accounts the user follows. | 该用户关注的账号数。 |
| `resp.200.users.canDm` |  | Whether the user currently accepts direct messages from the requester. | 该用户当前是否接受请求方的私信。 |
| `resp.200.users.createdAt` |  | Timestamp when the user's account was created. | 该用户账号的创建时间。 |
| `resp.200.users.favouritesCount` |  | Number of tweets the user has liked. | 该用户点赞过的推文数。 |
| `resp.200.users.hasCustomTimelines` |  | Whether the user has created custom timelines. | 该用户是否创建过自定义时间线。 |
| `resp.200.users.isTranslator` |  | Whether the user participates in the Twitter translation program. | 该用户是否参与 Twitter 翻译计划。 |
| `resp.200.users.mediaCount` |  | Number of media items the user has posted. | 该用户发布过的媒体条目数。 |
| `resp.200.users.statusesCount` |  | Total number of tweets the user has posted. | 该用户发布过的推文总数。 |
| `resp.200.users.withheldInCountries` |  | Country codes where the user's account is withheld for legal reasons. | 因法律原因屏蔽该用户账号的国家／地区代码列表。 |
| `resp.200.users.possiblySensitive` |  | Whether the user's posts are flagged as potentially sensitive. | 该用户的内容是否被标记为可能含敏感信息。 |
| `resp.200.users.pinnedTweetIds` |  | Identifiers of tweets the user has pinned to the top of their profile. | 该用户置顶在资料页顶部的推文标识列表。 |
| `resp.200.users.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.users.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.users.unavailable` |  | Whether the user's account is currently unavailable, for example suspended or deactivated. | 该用户账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.users.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.users.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.has_next_page` |  | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` |  | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` |  | Outcome marker of the request, such as success or error. | 请求结果标记，如成功或失败。 |
| `resp.200.message` |  | Human-readable message; carries the error detail on failure. | 可读的提示信息；失败时承载错误详情。 |

