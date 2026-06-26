# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 3 个接口，184 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## GET /twitter/tweet/thread_context

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get the thread context of a tweet. | Retrieve the conversation thread surrounding a tweet, returning the replies that make up its context. Works whether the given tweet is an original tweet or itself a reply. | 获取某条推文所在对话线程的上下文，返回构成该上下文的回复。无论传入的是原推文还是回复推文均可使用。 |
| `param:tweetId` | The tweet ID to get. Can be a reply tweet or an original tweet. | Identifier of the tweet whose thread context you want; may be an original tweet or a reply. | 要获取其线程上下文的推文标识；可以是原推文或回复推文。 |
| `param:cursor` | The cursor to paginate through the results. First page is empty. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.replies` |  | Reply tweets making up the thread context, returned for this page. | 本页返回的构成线程上下文的回复推文。 |
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
| `resp.200.replies.author.userName` |  | The author's @handle, unique across X/Twitter and used in profile URLs. | 作者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.replies.author.url` |  | Web link to the author's profile page. | 作者资料页的网页链接。 |
| `resp.200.replies.author.id` |  | Unique identifier of the author. | 作者的唯一标识。 |
| `resp.200.replies.author.name` |  | The author's display name shown on the profile. | 作者在资料页展示的昵称。 |
| `resp.200.replies.author.isBlueVerified` |  | Whether the author holds a paid X (Twitter) Blue verification. | 作者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.replies.author.verifiedType` |  | The author's verification category, such as a business or government account. | 作者的认证类别，如企业或政府账号。 |
| `resp.200.replies.author.profilePicture` |  | Web link to the author's avatar image. | 作者头像图片的网页链接。 |
| `resp.200.replies.author.coverPicture` |  | Web link to the author's profile banner image. | 作者资料页横幅图片的网页链接。 |
| `resp.200.replies.author.description` |  | The author's profile bio text. | 作者资料页的个人简介文字。 |
| `resp.200.replies.author.location` |  | Free-text location the author lists on their profile. | 作者在资料页填写的所在地（自由文本）。 |
| `resp.200.replies.author.followers` |  | Number of accounts following the author. | 关注作者的账号数。 |
| `resp.200.replies.author.following` |  | Number of accounts the author follows. | 作者关注的账号数。 |
| `resp.200.replies.author.canDm` |  | Whether the author currently accepts direct messages from the requester. | 作者当前是否接受请求方的私信。 |
| `resp.200.replies.author.createdAt` |  | Timestamp when the author's account was created. | 作者账号的创建时间。 |
| `resp.200.replies.author.favouritesCount` |  | Number of tweets the author has liked. | 作者点赞过的推文数。 |
| `resp.200.replies.author.hasCustomTimelines` |  | Whether the author has created custom timelines. | 作者是否创建过自定义时间线。 |
| `resp.200.replies.author.isTranslator` |  | Whether the author participates in the Twitter translation program. | 作者是否参与 Twitter 翻译计划。 |
| `resp.200.replies.author.mediaCount` |  | Number of media items the author has posted. | 作者发布过的媒体条目数。 |
| `resp.200.replies.author.statusesCount` |  | Total number of tweets the author has posted. | 作者发布过的推文总数。 |
| `resp.200.replies.author.withheldInCountries` |  | Country codes where the author's account is withheld for legal reasons. | 因法律原因屏蔽作者账号的国家／地区代码列表。 |
| `resp.200.replies.author.possiblySensitive` |  | Whether the author's posts are flagged as potentially sensitive. | 作者的内容是否被标记为可能含敏感信息。 |
| `resp.200.replies.author.pinnedTweetIds` |  | Identifiers of tweets the author has pinned to the top of their profile. | 作者置顶在资料页顶部的推文标识列表。 |
| `resp.200.replies.author.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.replies.author.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.replies.author.unavailable` |  | Whether the author's account is currently unavailable, for example suspended or deactivated. | 作者账号当前是否不可用，例如被封禁或停用。 |
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
| `resp.200.status` |  | Outcome marker of the request: success when the thread was returned, error otherwise. | 请求结果标记：成功返回线程为 success，否则为 error。 |
| `resp.200.message` |  | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/article

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get article by tweet ID. | Retrieve the long-form Article attached to a tweet, including its title, cover image, and body content blocks. | 获取某条推文所附带的长文 Article，包含标题、封面图与正文内容块。 |
| `param:tweet_id` | The tweet ID of the article. | Identifier of the tweet that carries the Article you want. | 承载所需 Article 的推文标识。 |
| `resp.200.article` |  | The long-form Article content and metadata. | 长文 Article 的内容与元数据。 |
| `resp.200.article.author` |  | Profile of the user who wrote the article. | 撰写该文章的用户资料。 |
| `resp.200.article.author.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.article.author.userName` |  | The author's @handle, unique across X/Twitter and used in profile URLs. | 作者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.article.author.url` |  | Web link to the author's profile page. | 作者资料页的网页链接。 |
| `resp.200.article.author.id` |  | Unique identifier of the author. | 作者的唯一标识。 |
| `resp.200.article.author.name` |  | The author's display name shown on the profile. | 作者在资料页展示的昵称。 |
| `resp.200.article.author.isBlueVerified` |  | Whether the author holds a paid X (Twitter) Blue verification. | 作者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.article.author.verifiedType` |  | The author's verification category, such as a business or government account. | 作者的认证类别，如企业或政府账号。 |
| `resp.200.article.author.profilePicture` |  | Web link to the author's avatar image. | 作者头像图片的网页链接。 |
| `resp.200.article.author.coverPicture` |  | Web link to the author's profile banner image. | 作者资料页横幅图片的网页链接。 |
| `resp.200.article.author.description` |  | The author's profile bio text. | 作者资料页的个人简介文字。 |
| `resp.200.article.author.location` |  | Free-text location the author lists on their profile. | 作者在资料页填写的所在地（自由文本）。 |
| `resp.200.article.author.followers` |  | Number of accounts following the author. | 关注作者的账号数。 |
| `resp.200.article.author.following` |  | Number of accounts the author follows. | 作者关注的账号数。 |
| `resp.200.article.author.canDm` |  | Whether the author currently accepts direct messages from the requester. | 作者当前是否接受请求方的私信。 |
| `resp.200.article.author.createdAt` |  | Timestamp when the author's account was created. | 作者账号的创建时间。 |
| `resp.200.article.author.favouritesCount` |  | Number of tweets the author has liked. | 作者点赞过的推文数。 |
| `resp.200.article.author.hasCustomTimelines` |  | Whether the author has created custom timelines. | 作者是否创建过自定义时间线。 |
| `resp.200.article.author.isTranslator` |  | Whether the author participates in the Twitter translation program. | 作者是否参与 Twitter 翻译计划。 |
| `resp.200.article.author.mediaCount` |  | Number of media items the author has posted. | 作者发布过的媒体条目数。 |
| `resp.200.article.author.statusesCount` |  | Total number of tweets the author has posted. | 作者发布过的推文总数。 |
| `resp.200.article.author.withheldInCountries` |  | Country codes where the author's account is withheld for legal reasons. | 因法律原因屏蔽作者账号的国家／地区代码列表。 |
| `resp.200.article.author.possiblySensitive` |  | Whether the author's posts are flagged as potentially sensitive. | 作者的内容是否被标记为可能含敏感信息。 |
| `resp.200.article.author.pinnedTweetIds` |  | Identifiers of tweets the author has pinned to the top of their profile. | 作者置顶在资料页顶部的推文标识列表。 |
| `resp.200.article.author.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.article.author.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.article.author.unavailable` |  | Whether the author's account is currently unavailable, for example suspended or deactivated. | 作者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.article.author.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.article.author.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.article.replyCount` |  | Number of replies to the article's tweet. | 文章所在推文收到的回复数。 |
| `resp.200.article.likeCount` |  | Number of likes on the article's tweet. | 文章所在推文获得的点赞数。 |
| `resp.200.article.quoteCount` |  | Number of quote tweets referencing the article's tweet. | 引用文章所在推文的引用推文数。 |
| `resp.200.article.viewCount` |  | Number of times the article's tweet has been viewed. | 文章所在推文的浏览次数。 |
| `resp.200.article.createdAt` |  | Timestamp when the article was created. | 文章的创建时间。 |
| `resp.200.article.title` |  | Title of the article. | 文章的标题。 |
| `resp.200.article.preview_text` |  | Short preview excerpt of the article body. | 文章正文的简短预览摘录。 |
| `resp.200.article.cover_media_img_url` |  | Web link to the article's cover image. | 文章封面图片的网页链接。 |
| `resp.200.article.contents` |  | Ordered content blocks making up the article body. | 构成文章正文的有序内容块。 |
| `resp.200.article.contents.text` |  | Text of a single article content block. | 单个文章内容块的文字。 |
| `resp.200.status` |  | Outcome marker of the request: success when the article was returned, failed otherwise. | 请求结果标记：成功返回文章为 success，否则为 failed。 |
| `resp.200.message` |  | Human-readable message; carries the error detail on failure. | 可读的提示信息；失败时承载错误详情。 |

## GET /twitter/tweet/advanced_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Advanced search for tweets. | Search tweets using a query string, choosing between the most recent matches or the top-ranked ones, with cursor pagination. | 使用查询字符串搜索推文，可在最新匹配与热门排序结果之间选择，并通过游标翻页。 |
| `param:query` | The query to search for. | Search query string; supports advanced search operators to filter tweets. | 搜索查询字符串，支持高级搜索运算符以筛选推文。 |
| `param:queryType` | The query type to search for. | Ranking mode of the results: Latest returns the most recent matches, Top returns the most relevant or popular ones. | 结果的排序模式：Latest 返回最新匹配，Top 返回最相关或最热门的结果。 |
| `param:cursor` | The cursor to paginate through the results. First page is empty. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.tweets` |  | Tweets matching the search, returned for this page. | 本页返回的匹配搜索条件的推文。 |
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
| `resp.200.tweets.author.userName` |  | The author's @handle, unique across X/Twitter and used in profile URLs. | 作者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.tweets.author.url` |  | Web link to the author's profile page. | 作者资料页的网页链接。 |
| `resp.200.tweets.author.id` |  | Unique identifier of the author. | 作者的唯一标识。 |
| `resp.200.tweets.author.name` |  | The author's display name shown on the profile. | 作者在资料页展示的昵称。 |
| `resp.200.tweets.author.isBlueVerified` |  | Whether the author holds a paid X (Twitter) Blue verification. | 作者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.tweets.author.verifiedType` |  | The author's verification category, such as a business or government account. | 作者的认证类别，如企业或政府账号。 |
| `resp.200.tweets.author.profilePicture` |  | Web link to the author's avatar image. | 作者头像图片的网页链接。 |
| `resp.200.tweets.author.coverPicture` |  | Web link to the author's profile banner image. | 作者资料页横幅图片的网页链接。 |
| `resp.200.tweets.author.description` |  | The author's profile bio text. | 作者资料页的个人简介文字。 |
| `resp.200.tweets.author.location` |  | Free-text location the author lists on their profile. | 作者在资料页填写的所在地（自由文本）。 |
| `resp.200.tweets.author.followers` |  | Number of accounts following the author. | 关注作者的账号数。 |
| `resp.200.tweets.author.following` |  | Number of accounts the author follows. | 作者关注的账号数。 |
| `resp.200.tweets.author.canDm` |  | Whether the author currently accepts direct messages from the requester. | 作者当前是否接受请求方的私信。 |
| `resp.200.tweets.author.createdAt` |  | Timestamp when the author's account was created. | 作者账号的创建时间。 |
| `resp.200.tweets.author.favouritesCount` |  | Number of tweets the author has liked. | 作者点赞过的推文数。 |
| `resp.200.tweets.author.hasCustomTimelines` |  | Whether the author has created custom timelines. | 作者是否创建过自定义时间线。 |
| `resp.200.tweets.author.isTranslator` |  | Whether the author participates in the Twitter translation program. | 作者是否参与 Twitter 翻译计划。 |
| `resp.200.tweets.author.mediaCount` |  | Number of media items the author has posted. | 作者发布过的媒体条目数。 |
| `resp.200.tweets.author.statusesCount` |  | Total number of tweets the author has posted. | 作者发布过的推文总数。 |
| `resp.200.tweets.author.withheldInCountries` |  | Country codes where the author's account is withheld for legal reasons. | 因法律原因屏蔽作者账号的国家／地区代码列表。 |
| `resp.200.tweets.author.possiblySensitive` |  | Whether the author's posts are flagged as potentially sensitive. | 作者的内容是否被标记为可能含敏感信息。 |
| `resp.200.tweets.author.pinnedTweetIds` |  | Identifiers of tweets the author has pinned to the top of their profile. | 作者置顶在资料页顶部的推文标识列表。 |
| `resp.200.tweets.author.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.tweets.author.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.tweets.author.unavailable` |  | Whether the author's account is currently unavailable, for example suspended or deactivated. | 作者账号当前是否不可用，例如被封禁或停用。 |
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

