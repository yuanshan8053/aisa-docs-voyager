# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 3 个接口，169 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## GET /twitter/list/tweets_timeline

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get timeline tweets from a list. Each page returns up to 20 tweets. Use cursor for pagination. | Fetch the reverse-chronological tweets posted by members of a given Twitter list, one page at a time. Pass the cursor returned by the previous call to walk through older tweets. | 按时间倒序获取某个 Twitter 列表内成员发布的推文，每次返回一页。把上一次返回的游标传入即可继续翻看更早的推文。 |
| `param:listId` | The list ID to get tweets from. e.g. 1846987139428634858 | Identifier of the Twitter list whose member tweets you want to read. | 要读取其成员推文的 Twitter 列表标识。 |
| `param:cursor` | Cursor for paginating through results. Leave empty for the first page. | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.tweets` | Array of tweets from the list | Tweets returned for this page of the list timeline. | 本页列表时间线返回的推文集合。 |
| `resp.200.tweets.type` |  | Object type tag identifying the entry as a tweet. | 对象类型标记，标识该条目为推文。 |
| `resp.200.tweets.id` | The ID of the tweet | Unique identifier of the tweet. | 推文的唯一标识。 |
| `resp.200.tweets.url` | The URL of the tweet | Web link to the tweet on X/Twitter. | 推文在 X/Twitter 上的网页链接。 |
| `resp.200.tweets.text` | The text of the tweet | Full text content of the tweet. | 推文的完整正文内容。 |
| `resp.200.tweets.source` | The source client of the tweet | Name of the client application used to post the tweet, such as the web or a mobile app. | 发布该推文所用的客户端应用名称，如网页或某款手机应用。 |
| `resp.200.tweets.retweetCount` |  | Number of times the tweet has been retweeted. | 推文被转发的次数。 |
| `resp.200.tweets.replyCount` |  | Number of replies to the tweet. | 推文收到的回复数。 |
| `resp.200.tweets.likeCount` |  | Number of likes on the tweet. | 推文获得的点赞数。 |
| `resp.200.tweets.quoteCount` |  | Number of quote tweets referencing this tweet. | 引用该推文的引用推文数。 |
| `resp.200.tweets.viewCount` |  | Number of times the tweet has been viewed. | 推文的浏览次数。 |
| `resp.200.tweets.createdAt` | The date and time the tweet was created | Timestamp when the tweet was created. | 推文的创建时间。 |
| `resp.200.tweets.lang` | The language of the tweet | Detected language of the tweet text, as a language code. | 推文正文被识别出的语言，以语言代码表示。 |
| `resp.200.tweets.bookmarkCount` |  | Number of times the tweet has been bookmarked. | 推文被收藏的次数。 |
| `resp.200.tweets.isReply` |  | Whether the tweet is a reply to another tweet. | 该推文是否为对另一条推文的回复。 |
| `resp.200.tweets.inReplyToId` |  | Identifier of the tweet this one directly replies to; present only when isReply is true. | 该推文直接回复的目标推文标识；仅当 isReply 为真时存在。 |
| `resp.200.tweets.conversationId` |  | Identifier of the root tweet that started the conversation thread this tweet belongs to. | 该推文所属对话线程的起始推文标识。 |
| `resp.200.tweets.inReplyToUserId` |  | Identifier of the user being replied to. | 被回复用户的标识。 |
| `resp.200.tweets.inReplyToUsername` |  | Username of the user being replied to. | 被回复用户的用户名。 |
| `resp.200.tweets.author` |  | Profile of the user who posted the tweet. | 发布该推文的用户资料。 |
| `resp.200.tweets.author.type` | Type of the user | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.tweets.author.userName` | Username of the user | The user's @handle, unique across X/Twitter and used in profile URLs. | 用户的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.tweets.author.url` | URL of the user's profile | Web link to the user's profile page. | 用户资料页的网页链接。 |
| `resp.200.tweets.author.id` | ID of the user | Unique identifier of the user. | 用户的唯一标识。 |
| `resp.200.tweets.author.name` | Name of the user | The user's display name shown on the profile. | 用户在资料页展示的昵称。 |
| `resp.200.tweets.author.isBlueVerified` | Indicates if the user is blue verified | Whether the user holds a paid X (Twitter) Blue verification. | 用户是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.tweets.author.verifiedType` | Type of verification | The user's verification category, such as a business or government account. | 用户的认证类别，如企业或政府账号。 |
| `resp.200.tweets.author.profilePicture` | URL of the profile picture | Web link to the user's avatar image. | 用户头像图片的网页链接。 |
| `resp.200.tweets.author.coverPicture` | URL of the cover picture | Web link to the user's profile banner image. | 用户资料页横幅图片的网页链接。 |
| `resp.200.tweets.author.description` | Description of the user | The user's profile bio text. | 用户资料页的个人简介文字。 |
| `resp.200.tweets.author.location` | Location of the user | Free-text location the user lists on their profile. | 用户在资料页填写的所在地（自由文本）。 |
| `resp.200.tweets.author.followers` | Number of followers | Number of accounts following the user. | 关注该用户的账号数。 |
| `resp.200.tweets.author.following` | Number of followings | Number of accounts the user follows. | 该用户关注的账号数。 |
| `resp.200.tweets.author.canDm` | Indicates if the user can be direct messaged | Whether the user currently accepts direct messages from the requester. | 该用户当前是否接受请求方的私信。 |
| `resp.200.tweets.author.createdAt` | Account creation date | Timestamp when the user's account was created. | 该用户账号的创建时间。 |
| `resp.200.tweets.author.favouritesCount` | Number of favorites | Number of tweets the user has liked. | 该用户点赞过的推文数。 |
| `resp.200.tweets.author.hasCustomTimelines` | Indicates if the user has custom timelines | Whether the user has created custom timelines. | 该用户是否创建过自定义时间线。 |
| `resp.200.tweets.author.isTranslator` | Indicates if the user is a translator | Whether the user participates in the Twitter translation program. | 该用户是否参与 Twitter 翻译计划。 |
| `resp.200.tweets.author.mediaCount` | Number of media items | Number of media items the user has posted. | 该用户发布过的媒体条目数。 |
| `resp.200.tweets.author.statusesCount` | Number of statuses | Total number of tweets the user has posted. | 该用户发布过的推文总数。 |
| `resp.200.tweets.author.withheldInCountries` | List of countries where the user is withheld | Country codes where the user's account is withheld for legal reasons. | 因法律原因屏蔽该用户账号的国家／地区代码列表。 |
| `resp.200.tweets.author.possiblySensitive` | Indicates if the user has sensitive content | Whether the user's posts are flagged as potentially sensitive. | 该用户的内容是否被标记为可能含敏感信息。 |
| `resp.200.tweets.author.pinnedTweetIds` | List of pinned tweet IDs | Identifiers of tweets the user has pinned to the top of their profile. | 该用户置顶在资料页顶部的推文标识列表。 |
| `resp.200.tweets.author.isAutomated` | Indicates if the account is automated | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.tweets.author.automatedBy` | Indicates who automated the account | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.tweets.author.unavailable` | Indicates if the account is unavailable | Whether the user's account is currently unavailable, for example suspended or deactivated. | 该用户账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.tweets.author.message` | Message about the account | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.tweets.author.unavailableReason` | Reason for unavailability | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.tweets.author.profile_bio` |  | Structured profile bio, including the raw description text and the entities parsed out of it. | 结构化的资料简介，包含简介原文及从中解析出的实体。 |
| `resp.200.tweets.author.profile_bio.description` | Bio description | Raw bio text exactly as shown on the profile. | 资料页展示的简介原文。 |
| `resp.200.tweets.author.profile_bio.entities` |  | Entities parsed from the bio, grouping links found in the description text and in the profile's website field. | 从简介中解析出的实体，分别归类简介正文中的链接与资料网址字段中的链接。 |
| `resp.200.tweets.author.profile_bio.entities.description` |  | Links detected within the bio description text. | 在简介正文中检测到的链接。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls` |  | List of links found in the bio description. | 简介正文中找到的链接列表。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.display_url` | Display URL | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.expanded_url` | Expanded URL | Full destination URL the website link resolves to. | 网址链接最终指向的完整目标地址。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.indices` | Indices of the URL | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.url` | URL | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
| `resp.200.tweets.author.profile_bio.entities.url` |  | Links detected in the profile's dedicated website field. | 在资料页专门的网址字段中检测到的链接。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls` |  | List of links found in the profile website field. | 资料网址字段中找到的链接列表。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.display_url` | Display URL | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.expanded_url` | Expanded URL | Full destination URL the website link resolves to. | 网址链接最终指向的完整目标地址。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.indices` | Indices of the URL | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.url` | URL | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
| `resp.200.has_next_page` | Indicates if there are more results available | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` | Cursor for fetching the next page of results | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` | Status of the request | Outcome marker of the request: success when the timeline was returned, error otherwise. | 请求结果标记：成功返回时间线为 success，否则为 error。 |
| `resp.200.msg` | Message of the request, error message if status is error | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/list/followers

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get followers of a list. Page size is 20. | List the users who follow a given Twitter list, one page at a time, paginating with the cursor from the previous response. | 分页获取关注某个 Twitter 列表的用户，使用上一次响应返回的游标继续翻页。 |
| `param:list_id` | ID of the list | Identifier of the Twitter list whose followers you want to read. | 要读取其关注者的 Twitter 列表标识。 |
| `param:cursor` | Cursor of the page | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.followers` |  | Users following the list, returned for this page. | 本页返回的关注该列表的用户。 |
| `resp.200.followers.type` | Type of the user | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.followers.userName` | Username of the user | The user's @handle, unique across X/Twitter and used in profile URLs. | 用户的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.followers.url` | URL of the user's profile | Web link to the user's profile page. | 用户资料页的网页链接。 |
| `resp.200.followers.id` | ID of the user | Unique identifier of the user. | 用户的唯一标识。 |
| `resp.200.followers.name` | Name of the user | The user's display name shown on the profile. | 用户在资料页展示的昵称。 |
| `resp.200.followers.isBlueVerified` | Indicates if the user is blue verified | Whether the user holds a paid X (Twitter) Blue verification. | 用户是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.followers.verifiedType` | Type of verification | The user's verification category, such as a business or government account. | 用户的认证类别，如企业或政府账号。 |
| `resp.200.followers.profilePicture` | URL of the profile picture | Web link to the user's avatar image. | 用户头像图片的网页链接。 |
| `resp.200.followers.coverPicture` | URL of the cover picture | Web link to the user's profile banner image. | 用户资料页横幅图片的网页链接。 |
| `resp.200.followers.description` | Description of the user | The user's profile bio text. | 用户资料页的个人简介文字。 |
| `resp.200.followers.location` | Location of the user | Free-text location the user lists on their profile. | 用户在资料页填写的所在地（自由文本）。 |
| `resp.200.followers.followers` | Number of followers | Number of accounts following the user. | 关注该用户的账号数。 |
| `resp.200.followers.following` | Number of followings | Number of accounts the user follows. | 该用户关注的账号数。 |
| `resp.200.followers.canDm` | Indicates if the user can be direct messaged | Whether the user currently accepts direct messages from the requester. | 该用户当前是否接受请求方的私信。 |
| `resp.200.followers.createdAt` | Account creation date | Timestamp when the user's account was created. | 该用户账号的创建时间。 |
| `resp.200.followers.favouritesCount` | Number of favorites | Number of tweets the user has liked. | 该用户点赞过的推文数。 |
| `resp.200.followers.hasCustomTimelines` | Indicates if the user has custom timelines | Whether the user has created custom timelines. | 该用户是否创建过自定义时间线。 |
| `resp.200.followers.isTranslator` | Indicates if the user is a translator | Whether the user participates in the Twitter translation program. | 该用户是否参与 Twitter 翻译计划。 |
| `resp.200.followers.mediaCount` | Number of media items | Number of media items the user has posted. | 该用户发布过的媒体条目数。 |
| `resp.200.followers.statusesCount` | Number of statuses | Total number of tweets the user has posted. | 该用户发布过的推文总数。 |
| `resp.200.followers.withheldInCountries` | List of countries where the user is withheld | Country codes where the user's account is withheld for legal reasons. | 因法律原因屏蔽该用户账号的国家／地区代码列表。 |
| `resp.200.followers.possiblySensitive` | Indicates if the user has sensitive content | Whether the user's posts are flagged as potentially sensitive. | 该用户的内容是否被标记为可能含敏感信息。 |
| `resp.200.followers.pinnedTweetIds` | List of pinned tweet IDs | Identifiers of tweets the user has pinned to the top of their profile. | 该用户置顶在资料页顶部的推文标识列表。 |
| `resp.200.followers.isAutomated` | Indicates if the account is automated | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.followers.automatedBy` | Indicates who automated the account | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.followers.unavailable` | Indicates if the account is unavailable | Whether the user's account is currently unavailable, for example suspended or deactivated. | 该用户账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.followers.message` | Message about the account | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.followers.unavailableReason` | Reason for unavailability | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.followers.profile_bio` |  | Structured profile bio, including the raw description text and the entities parsed out of it. | 结构化的资料简介，包含简介原文及从中解析出的实体。 |
| `resp.200.followers.profile_bio.description` | Bio description | Raw bio text exactly as shown on the profile. | 资料页展示的简介原文。 |
| `resp.200.followers.profile_bio.entities` |  | Entities parsed from the bio, grouping links found in the description text and in the profile's website field. | 从简介中解析出的实体，分别归类简介正文中的链接与资料网址字段中的链接。 |
| `resp.200.followers.profile_bio.entities.description` |  | Links detected within the bio description text. | 在简介正文中检测到的链接。 |
| `resp.200.followers.profile_bio.entities.description.urls` |  | List of links found in the bio description. | 简介正文中找到的链接列表。 |
| `resp.200.followers.profile_bio.entities.description.urls.display_url` | Display URL | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.followers.profile_bio.entities.description.urls.expanded_url` | Expanded URL | Full destination URL the website link resolves to. | 网址链接最终指向的完整目标地址。 |
| `resp.200.followers.profile_bio.entities.description.urls.indices` | Indices of the URL | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.followers.profile_bio.entities.description.urls.url` | URL | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
| `resp.200.followers.profile_bio.entities.url` |  | Links detected in the profile's dedicated website field. | 在资料页专门的网址字段中检测到的链接。 |
| `resp.200.followers.profile_bio.entities.url.urls` |  | List of links found in the profile website field. | 资料网址字段中找到的链接列表。 |
| `resp.200.followers.profile_bio.entities.url.urls.display_url` | Display URL | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.followers.profile_bio.entities.url.urls.expanded_url` | Expanded URL | Full destination URL the website link resolves to. | 网址链接最终指向的完整目标地址。 |
| `resp.200.followers.profile_bio.entities.url.urls.indices` | Indices of the URL | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.followers.profile_bio.entities.url.urls.url` | URL | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
| `resp.200.has_next_page` | Indicates if there are more results available | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` | Cursor for fetching the next page of results | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` | Status of the request | Outcome marker of the request: success when followers were returned, error otherwise. | 请求结果标记：成功返回关注者为 success，否则为 error。 |
| `resp.200.msg` | Message of the request, error message if status is error | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

## GET /twitter/list/members

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get members of a list. Page size is 20. | List the users who are members of a given Twitter list, one page at a time, paginating with the cursor from the previous response. | 分页获取某个 Twitter 列表的成员用户，使用上一次响应返回的游标继续翻页。 |
| `param:list_id` | ID of the list | Identifier of the Twitter list whose members you want to read. | 要读取其成员的 Twitter 列表标识。 |
| `param:cursor` | Cursor of the page | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.members` |  | Member users of the list, returned for this page. | 本页返回的列表成员用户。 |
| `resp.200.members.type` | Type of the user | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.members.userName` | Username of the user | The user's @handle, unique across X/Twitter and used in profile URLs. | 用户的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.members.url` | URL of the user's profile | Web link to the user's profile page. | 用户资料页的网页链接。 |
| `resp.200.members.id` | ID of the user | Unique identifier of the user. | 用户的唯一标识。 |
| `resp.200.members.name` | Name of the user | The user's display name shown on the profile. | 用户在资料页展示的昵称。 |
| `resp.200.members.isBlueVerified` | Indicates if the user is blue verified | Whether the user holds a paid X (Twitter) Blue verification. | 用户是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.members.verifiedType` | Type of verification | The user's verification category, such as a business or government account. | 用户的认证类别，如企业或政府账号。 |
| `resp.200.members.profilePicture` | URL of the profile picture | Web link to the user's avatar image. | 用户头像图片的网页链接。 |
| `resp.200.members.coverPicture` | URL of the cover picture | Web link to the user's profile banner image. | 用户资料页横幅图片的网页链接。 |
| `resp.200.members.description` | Description of the user | The user's profile bio text. | 用户资料页的个人简介文字。 |
| `resp.200.members.location` | Location of the user | Free-text location the user lists on their profile. | 用户在资料页填写的所在地（自由文本）。 |
| `resp.200.members.followers` | Number of followers | Number of accounts following the user. | 关注该用户的账号数。 |
| `resp.200.members.following` | Number of followings | Number of accounts the user follows. | 该用户关注的账号数。 |
| `resp.200.members.canDm` | Indicates if the user can be direct messaged | Whether the user currently accepts direct messages from the requester. | 该用户当前是否接受请求方的私信。 |
| `resp.200.members.createdAt` | Account creation date | Timestamp when the user's account was created. | 该用户账号的创建时间。 |
| `resp.200.members.favouritesCount` | Number of favorites | Number of tweets the user has liked. | 该用户点赞过的推文数。 |
| `resp.200.members.hasCustomTimelines` | Indicates if the user has custom timelines | Whether the user has created custom timelines. | 该用户是否创建过自定义时间线。 |
| `resp.200.members.isTranslator` | Indicates if the user is a translator | Whether the user participates in the Twitter translation program. | 该用户是否参与 Twitter 翻译计划。 |
| `resp.200.members.mediaCount` | Number of media items | Number of media items the user has posted. | 该用户发布过的媒体条目数。 |
| `resp.200.members.statusesCount` | Number of statuses | Total number of tweets the user has posted. | 该用户发布过的推文总数。 |
| `resp.200.members.withheldInCountries` | List of countries where the user is withheld | Country codes where the user's account is withheld for legal reasons. | 因法律原因屏蔽该用户账号的国家／地区代码列表。 |
| `resp.200.members.possiblySensitive` | Indicates if the user has sensitive content | Whether the user's posts are flagged as potentially sensitive. | 该用户的内容是否被标记为可能含敏感信息。 |
| `resp.200.members.pinnedTweetIds` | List of pinned tweet IDs | Identifiers of tweets the user has pinned to the top of their profile. | 该用户置顶在资料页顶部的推文标识列表。 |
| `resp.200.members.isAutomated` | Indicates if the account is automated | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.members.automatedBy` | Indicates who automated the account | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.members.unavailable` | Indicates if the account is unavailable | Whether the user's account is currently unavailable, for example suspended or deactivated. | 该用户账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.members.message` | Message about the account | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.members.unavailableReason` | Reason for unavailability | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.members.profile_bio` |  | Structured profile bio, including the raw description text and the entities parsed out of it. | 结构化的资料简介，包含简介原文及从中解析出的实体。 |
| `resp.200.members.profile_bio.description` | Bio description | Raw bio text exactly as shown on the profile. | 资料页展示的简介原文。 |
| `resp.200.members.profile_bio.entities` |  | Entities parsed from the bio, grouping links found in the description text and in the profile's website field. | 从简介中解析出的实体，分别归类简介正文中的链接与资料网址字段中的链接。 |
| `resp.200.members.profile_bio.entities.description` |  | Links detected within the bio description text. | 在简介正文中检测到的链接。 |
| `resp.200.members.profile_bio.entities.description.urls` |  | List of links found in the bio description. | 简介正文中找到的链接列表。 |
| `resp.200.members.profile_bio.entities.description.urls.display_url` | Display URL | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.members.profile_bio.entities.description.urls.expanded_url` | Expanded URL | Full destination URL the website link resolves to. | 网址链接最终指向的完整目标地址。 |
| `resp.200.members.profile_bio.entities.description.urls.indices` | Indices of the URL | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.members.profile_bio.entities.description.urls.url` | URL | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
| `resp.200.members.profile_bio.entities.url` |  | Links detected in the profile's dedicated website field. | 在资料页专门的网址字段中检测到的链接。 |
| `resp.200.members.profile_bio.entities.url.urls` |  | List of links found in the profile website field. | 资料网址字段中找到的链接列表。 |
| `resp.200.members.profile_bio.entities.url.urls.display_url` | Display URL | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.members.profile_bio.entities.url.urls.expanded_url` | Expanded URL | Full destination URL the website link resolves to. | 网址链接最终指向的完整目标地址。 |
| `resp.200.members.profile_bio.entities.url.urls.indices` | Indices of the URL | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.members.profile_bio.entities.url.urls.url` | URL | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
| `resp.200.has_next_page` | Indicates if there are more results available | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` | Cursor for fetching the next page of results | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |
| `resp.200.status` | Status of the request | Outcome marker of the request: success when members were returned, error otherwise. | 请求结果标记：成功返回成员为 success，否则为 error。 |
| `resp.200.msg` | Message of the request, error message if status is error | Human-readable message; carries the error detail when status is error. | 可读的提示信息；当 status 为 error 时承载错误详情。 |

