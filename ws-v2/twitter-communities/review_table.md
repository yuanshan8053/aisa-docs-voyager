# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 5 个接口，376 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## GET /twitter/community/info

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Retrieve information about a community by its ID. | Retrieve detailed information about a single community by its ID, including its profile, membership counts, topic, rules, and the requester's role. | 按社区 ID 获取单个社区的详细信息，包含其资料、成员数量、主题、规则以及请求方在该社区中的角色。 |
| `param:community_id` | ID of the community | Identifier of the community whose information you want to retrieve. | 要获取信息的社区标识。 |
| `resp.200.id` |  | Unique identifier of the community. | 社区的唯一标识。 |
| `resp.200.name` |  | Display name of the community. | 社区的显示名称。 |
| `resp.200.description` |  | Description text introducing the community. | 介绍该社区的描述文字。 |
| `resp.200.question` |  | Membership question prospective members are asked when joining. | 新成员加入时被问及的入会问题。 |
| `resp.200.member_count` |  | Total number of members in the community. | 社区的成员总数。 |
| `resp.200.moderator_count` |  | Total number of moderators in the community. | 社区的版主总数。 |
| `resp.200.created_at` |  | Timestamp when the community was created. | 社区的创建时间。 |
| `resp.200.join_policy` |  | Policy governing how new members may join the community. | 规定新成员如何加入该社区的策略。 |
| `resp.200.invites_policy` |  | Policy governing who may invite others to the community. | 规定谁可以邀请他人加入该社区的策略。 |
| `resp.200.is_nsfw` |  | Whether the community is marked as not safe for work. | 该社区是否被标记为不适宜在工作场合浏览（NSFW）。 |
| `resp.200.is_pinned` |  | Whether the community is pinned by the requester. | 该社区是否被请求方置顶。 |
| `resp.200.role` |  | The requester's role within the community, such as member, moderator, or admin. | 请求方在该社区中的角色，如成员、版主或管理员。 |
| `resp.200.primary_topic` |  | The community's primary topic. | 社区的主要主题。 |
| `resp.200.primary_topic.id` |  | Identifier of the primary topic. | 主要主题的标识。 |
| `resp.200.primary_topic.name` |  | Display name of the primary topic. | 主要主题的显示名称。 |
| `resp.200.banner_url` |  | Web link to the community's banner image. | 社区横幅图片的网页链接。 |
| `resp.200.search_tags` |  | Tags associated with the community to aid discovery in search. | 与该社区关联、便于在搜索中被发现的标签。 |
| `resp.200.rules` |  | Rules that members of the community must follow. | 社区成员需遵守的规则。 |
| `resp.200.rules.id` |  | Identifier of the rule. | 规则的标识。 |
| `resp.200.rules.name` |  | Short name or title of the rule. | 规则的简短名称或标题。 |
| `resp.200.rules.description` |  | Detailed text explaining the rule. | 解释该规则的详细文字。 |
| `resp.200.creator` |  | Profile of the user who created the community. | 创建该社区的用户资料。 |
| `resp.200.creator.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.creator.userName` |  | The author's @handle, unique across X/Twitter and used in profile URLs. | 作者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.creator.url` |  | Web link to the author's profile page. | 作者资料页的网页链接。 |
| `resp.200.creator.id` |  | Unique identifier of the author. | 作者的唯一标识。 |
| `resp.200.creator.name` |  | The author's display name shown on the profile. | 作者在资料页展示的昵称。 |
| `resp.200.creator.isBlueVerified` |  | Whether the author holds a paid X (Twitter) Blue verification. | 作者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.creator.verifiedType` |  | The author's verification category, such as a business or government account. | 作者的认证类别，如企业或政府账号。 |
| `resp.200.creator.profilePicture` |  | Web link to the author's avatar image. | 作者头像图片的网页链接。 |
| `resp.200.creator.coverPicture` |  | Web link to the author's profile banner image. | 作者资料页横幅图片的网页链接。 |
| `resp.200.creator.description` |  | The author's profile bio text. | 作者资料页的个人简介文字。 |
| `resp.200.creator.location` |  | Free-text location the author lists on their profile. | 作者在资料页填写的所在地（自由文本）。 |
| `resp.200.creator.followers` |  | Number of accounts following the author. | 关注作者的账号数。 |
| `resp.200.creator.following` |  | Number of accounts the author follows. | 作者关注的账号数。 |
| `resp.200.creator.canDm` |  | Whether the author currently accepts direct messages from the requester. | 作者当前是否接受请求方的私信。 |
| `resp.200.creator.createdAt` |  | Timestamp when the author's account was created. | 作者账号的创建时间。 |
| `resp.200.creator.favouritesCount` |  | Number of tweets the author has liked. | 作者点赞过的推文数。 |
| `resp.200.creator.hasCustomTimelines` |  | Whether the author has created custom timelines. | 作者是否创建过自定义时间线。 |
| `resp.200.creator.isTranslator` |  | Whether the author participates in the Twitter translation program. | 作者是否参与 Twitter 翻译计划。 |
| `resp.200.creator.mediaCount` |  | Number of media items the author has posted. | 作者发布过的媒体条目数。 |
| `resp.200.creator.statusesCount` |  | Total number of tweets the author has posted. | 作者发布过的推文总数。 |
| `resp.200.creator.withheldInCountries` |  | Country codes where the author's account is withheld for legal reasons. | 因法律原因屏蔽作者账号的国家／地区代码列表。 |
| `resp.200.creator.possiblySensitive` |  | Whether the author's posts are flagged as potentially sensitive. | 作者的内容是否被标记为可能含敏感信息。 |
| `resp.200.creator.pinnedTweetIds` |  | Identifiers of tweets the author has pinned to the top of their profile. | 作者置顶在资料页顶部的推文标识列表。 |
| `resp.200.creator.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.creator.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.creator.unavailable` |  | Whether the author's account is currently unavailable, for example suspended or deactivated. | 作者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.creator.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.creator.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.creator.profile_bio` |  | The author's profile bio along with the entities parsed from it. | 作者的资料简介及从中解析出的实体。 |
| `resp.200.creator.profile_bio.description` |  | The raw bio text shown on the author's profile. | 作者资料页展示的原始简介文字。 |
| `resp.200.creator.profile_bio.entities` |  | Structured entities parsed from the bio, covering both the bio text and the profile website field. | 从简介中解析出的结构化实体，涵盖简介文字与资料页网址字段。 |
| `resp.200.creator.profile_bio.entities.description` |  | Entities parsed from the bio description text. | 从简介描述文字中解析出的实体。 |
| `resp.200.creator.profile_bio.entities.description.urls` |  | Links found in the bio description text. | 简介描述文字中出现的链接。 |
| `resp.200.creator.profile_bio.entities.description.urls.display_url` |  | Shortened, human-readable form of the link as displayed in the bio. | 简介中显示的链接的短化、易读形式。 |
| `resp.200.creator.profile_bio.entities.description.urls.expanded_url` |  | Full destination URL the displayed link resolves to. | 显示链接最终指向的完整目标地址。 |
| `resp.200.creator.profile_bio.entities.description.urls.indices` |  | Start and end character offsets of the link within the bio text. | 该链接在简介文字中的起止字符位置。 |
| `resp.200.creator.profile_bio.entities.description.urls.url` |  | The t.co shortened URL as it literally appears in the bio text. | 简介文字中实际出现的 t.co 短链接。 |
| `resp.200.creator.profile_bio.entities.url` |  | Entities parsed from the profile website field. | 从资料页网址字段中解析出的实体。 |
| `resp.200.creator.profile_bio.entities.url.urls` |  | Links found in the profile website field. | 资料页网址字段中出现的链接。 |
| `resp.200.creator.profile_bio.entities.url.urls.display_url` |  | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.creator.profile_bio.entities.url.urls.expanded_url` |  | Full destination URL the displayed website link resolves to. | 显示的网址链接最终指向的完整目标地址。 |
| `resp.200.creator.profile_bio.entities.url.urls.indices` |  | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.creator.profile_bio.entities.url.urls.url` |  | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
| `resp.200.admin` |  | Profile of the community's administrator. | 社区管理员的用户资料。 |
| `resp.200.admin.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.admin.userName` |  | The author's @handle, unique across X/Twitter and used in profile URLs. | 作者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.admin.url` |  | Web link to the author's profile page. | 作者资料页的网页链接。 |
| `resp.200.admin.id` |  | Unique identifier of the author. | 作者的唯一标识。 |
| `resp.200.admin.name` |  | The author's display name shown on the profile. | 作者在资料页展示的昵称。 |
| `resp.200.admin.isBlueVerified` |  | Whether the author holds a paid X (Twitter) Blue verification. | 作者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.admin.verifiedType` |  | The author's verification category, such as a business or government account. | 作者的认证类别，如企业或政府账号。 |
| `resp.200.admin.profilePicture` |  | Web link to the author's avatar image. | 作者头像图片的网页链接。 |
| `resp.200.admin.coverPicture` |  | Web link to the author's profile banner image. | 作者资料页横幅图片的网页链接。 |
| `resp.200.admin.description` |  | The author's profile bio text. | 作者资料页的个人简介文字。 |
| `resp.200.admin.location` |  | Free-text location the author lists on their profile. | 作者在资料页填写的所在地（自由文本）。 |
| `resp.200.admin.followers` |  | Number of accounts following the author. | 关注作者的账号数。 |
| `resp.200.admin.following` |  | Number of accounts the author follows. | 作者关注的账号数。 |
| `resp.200.admin.canDm` |  | Whether the author currently accepts direct messages from the requester. | 作者当前是否接受请求方的私信。 |
| `resp.200.admin.createdAt` |  | Timestamp when the author's account was created. | 作者账号的创建时间。 |
| `resp.200.admin.favouritesCount` |  | Number of tweets the author has liked. | 作者点赞过的推文数。 |
| `resp.200.admin.hasCustomTimelines` |  | Whether the author has created custom timelines. | 作者是否创建过自定义时间线。 |
| `resp.200.admin.isTranslator` |  | Whether the author participates in the Twitter translation program. | 作者是否参与 Twitter 翻译计划。 |
| `resp.200.admin.mediaCount` |  | Number of media items the author has posted. | 作者发布过的媒体条目数。 |
| `resp.200.admin.statusesCount` |  | Total number of tweets the author has posted. | 作者发布过的推文总数。 |
| `resp.200.admin.withheldInCountries` |  | Country codes where the author's account is withheld for legal reasons. | 因法律原因屏蔽作者账号的国家／地区代码列表。 |
| `resp.200.admin.possiblySensitive` |  | Whether the author's posts are flagged as potentially sensitive. | 作者的内容是否被标记为可能含敏感信息。 |
| `resp.200.admin.pinnedTweetIds` |  | Identifiers of tweets the author has pinned to the top of their profile. | 作者置顶在资料页顶部的推文标识列表。 |
| `resp.200.admin.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.admin.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.admin.unavailable` |  | Whether the author's account is currently unavailable, for example suspended or deactivated. | 作者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.admin.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.admin.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.admin.profile_bio` |  | The author's profile bio along with the entities parsed from it. | 作者的资料简介及从中解析出的实体。 |
| `resp.200.admin.profile_bio.description` |  | The raw bio text shown on the author's profile. | 作者资料页展示的原始简介文字。 |
| `resp.200.admin.profile_bio.entities` |  | Structured entities parsed from the bio, covering both the bio text and the profile website field. | 从简介中解析出的结构化实体，涵盖简介文字与资料页网址字段。 |
| `resp.200.admin.profile_bio.entities.description` |  | Entities parsed from the bio description text. | 从简介描述文字中解析出的实体。 |
| `resp.200.admin.profile_bio.entities.description.urls` |  | Links found in the bio description text. | 简介描述文字中出现的链接。 |
| `resp.200.admin.profile_bio.entities.description.urls.display_url` |  | Shortened, human-readable form of the link as displayed in the bio. | 简介中显示的链接的短化、易读形式。 |
| `resp.200.admin.profile_bio.entities.description.urls.expanded_url` |  | Full destination URL the displayed link resolves to. | 显示链接最终指向的完整目标地址。 |
| `resp.200.admin.profile_bio.entities.description.urls.indices` |  | Start and end character offsets of the link within the bio text. | 该链接在简介文字中的起止字符位置。 |
| `resp.200.admin.profile_bio.entities.description.urls.url` |  | The t.co shortened URL as it literally appears in the bio text. | 简介文字中实际出现的 t.co 短链接。 |
| `resp.200.admin.profile_bio.entities.url` |  | Entities parsed from the profile website field. | 从资料页网址字段中解析出的实体。 |
| `resp.200.admin.profile_bio.entities.url.urls` |  | Links found in the profile website field. | 资料页网址字段中出现的链接。 |
| `resp.200.admin.profile_bio.entities.url.urls.display_url` |  | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.admin.profile_bio.entities.url.urls.expanded_url` |  | Full destination URL the displayed website link resolves to. | 显示的网址链接最终指向的完整目标地址。 |
| `resp.200.admin.profile_bio.entities.url.urls.indices` |  | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.admin.profile_bio.entities.url.urls.url` |  | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
| `resp.200.members_preview` |  | A small preview sample of community members. | 社区成员的小幅预览样本。 |

## GET /twitter/community/members

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Retrieve members of a community. | Retrieve the members of a community, returned one page at a time with cursor pagination. | 获取某社区的成员，按页返回并通过游标翻页。 |
| `param:community_id` | ID of the community | Identifier of the community whose members you want to list. | 要列出其成员的社区标识。 |
| `param:cursor` | Cursor for pagination | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.members` |  | Community members returned for this page. | 本页返回的社区成员。 |
| `resp.200.members.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.members.userName` |  | The author's @handle, unique across X/Twitter and used in profile URLs. | 作者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.members.url` |  | Web link to the author's profile page. | 作者资料页的网页链接。 |
| `resp.200.members.id` |  | Unique identifier of the author. | 作者的唯一标识。 |
| `resp.200.members.name` |  | The author's display name shown on the profile. | 作者在资料页展示的昵称。 |
| `resp.200.members.isBlueVerified` |  | Whether the author holds a paid X (Twitter) Blue verification. | 作者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.members.verifiedType` |  | The author's verification category, such as a business or government account. | 作者的认证类别，如企业或政府账号。 |
| `resp.200.members.profilePicture` |  | Web link to the author's avatar image. | 作者头像图片的网页链接。 |
| `resp.200.members.coverPicture` |  | Web link to the author's profile banner image. | 作者资料页横幅图片的网页链接。 |
| `resp.200.members.description` |  | The author's profile bio text. | 作者资料页的个人简介文字。 |
| `resp.200.members.location` |  | Free-text location the author lists on their profile. | 作者在资料页填写的所在地（自由文本）。 |
| `resp.200.members.followers` |  | Number of accounts following the author. | 关注作者的账号数。 |
| `resp.200.members.following` |  | Number of accounts the author follows. | 作者关注的账号数。 |
| `resp.200.members.canDm` |  | Whether the author currently accepts direct messages from the requester. | 作者当前是否接受请求方的私信。 |
| `resp.200.members.createdAt` |  | Timestamp when the author's account was created. | 作者账号的创建时间。 |
| `resp.200.members.favouritesCount` |  | Number of tweets the author has liked. | 作者点赞过的推文数。 |
| `resp.200.members.hasCustomTimelines` |  | Whether the author has created custom timelines. | 作者是否创建过自定义时间线。 |
| `resp.200.members.isTranslator` |  | Whether the author participates in the Twitter translation program. | 作者是否参与 Twitter 翻译计划。 |
| `resp.200.members.mediaCount` |  | Number of media items the author has posted. | 作者发布过的媒体条目数。 |
| `resp.200.members.statusesCount` |  | Total number of tweets the author has posted. | 作者发布过的推文总数。 |
| `resp.200.members.withheldInCountries` |  | Country codes where the author's account is withheld for legal reasons. | 因法律原因屏蔽作者账号的国家／地区代码列表。 |
| `resp.200.members.possiblySensitive` |  | Whether the author's posts are flagged as potentially sensitive. | 作者的内容是否被标记为可能含敏感信息。 |
| `resp.200.members.pinnedTweetIds` |  | Identifiers of tweets the author has pinned to the top of their profile. | 作者置顶在资料页顶部的推文标识列表。 |
| `resp.200.members.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.members.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.members.unavailable` |  | Whether the author's account is currently unavailable, for example suspended or deactivated. | 作者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.members.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.members.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.members.profile_bio` |  | The author's profile bio along with the entities parsed from it. | 作者的资料简介及从中解析出的实体。 |
| `resp.200.members.profile_bio.description` |  | The raw bio text shown on the author's profile. | 作者资料页展示的原始简介文字。 |
| `resp.200.members.profile_bio.entities` |  | Structured entities parsed from the bio, covering both the bio text and the profile website field. | 从简介中解析出的结构化实体，涵盖简介文字与资料页网址字段。 |
| `resp.200.members.profile_bio.entities.description` |  | Entities parsed from the bio description text. | 从简介描述文字中解析出的实体。 |
| `resp.200.members.profile_bio.entities.description.urls` |  | Links found in the bio description text. | 简介描述文字中出现的链接。 |
| `resp.200.members.profile_bio.entities.description.urls.display_url` |  | Shortened, human-readable form of the link as displayed in the bio. | 简介中显示的链接的短化、易读形式。 |
| `resp.200.members.profile_bio.entities.description.urls.expanded_url` |  | Full destination URL the displayed link resolves to. | 显示链接最终指向的完整目标地址。 |
| `resp.200.members.profile_bio.entities.description.urls.indices` |  | Start and end character offsets of the link within the bio text. | 该链接在简介文字中的起止字符位置。 |
| `resp.200.members.profile_bio.entities.description.urls.url` |  | The t.co shortened URL as it literally appears in the bio text. | 简介文字中实际出现的 t.co 短链接。 |
| `resp.200.members.profile_bio.entities.url` |  | Entities parsed from the profile website field. | 从资料页网址字段中解析出的实体。 |
| `resp.200.members.profile_bio.entities.url.urls` |  | Links found in the profile website field. | 资料页网址字段中出现的链接。 |
| `resp.200.members.profile_bio.entities.url.urls.display_url` |  | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.members.profile_bio.entities.url.urls.expanded_url` |  | Full destination URL the displayed website link resolves to. | 显示的网址链接最终指向的完整目标地址。 |
| `resp.200.members.profile_bio.entities.url.urls.indices` |  | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.members.profile_bio.entities.url.urls.url` |  | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
| `resp.200.has_next_page` |  | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` |  | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |

## GET /twitter/community/moderators

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Retrieve moderators of a community. | Retrieve the moderators of a community, returned one page at a time with cursor pagination. | 获取某社区的版主，按页返回并通过游标翻页。 |
| `param:community_id` | ID of the community | Identifier of the community whose moderators you want to list. | 要列出其版主的社区标识。 |
| `param:cursor` | Cursor for pagination | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.members` |  | Community moderators returned for this page. | 本页返回的社区版主。 |
| `resp.200.members.type` |  | Object type tag identifying the entry as a user. | 对象类型标记，标识该条目为用户。 |
| `resp.200.members.userName` |  | The author's @handle, unique across X/Twitter and used in profile URLs. | 作者的 @ 用户名，在 X/Twitter 上唯一，用于资料页地址。 |
| `resp.200.members.url` |  | Web link to the author's profile page. | 作者资料页的网页链接。 |
| `resp.200.members.id` |  | Unique identifier of the author. | 作者的唯一标识。 |
| `resp.200.members.name` |  | The author's display name shown on the profile. | 作者在资料页展示的昵称。 |
| `resp.200.members.isBlueVerified` |  | Whether the author holds a paid X (Twitter) Blue verification. | 作者是否拥有付费的 X（Twitter）Blue 认证。 |
| `resp.200.members.verifiedType` |  | The author's verification category, such as a business or government account. | 作者的认证类别，如企业或政府账号。 |
| `resp.200.members.profilePicture` |  | Web link to the author's avatar image. | 作者头像图片的网页链接。 |
| `resp.200.members.coverPicture` |  | Web link to the author's profile banner image. | 作者资料页横幅图片的网页链接。 |
| `resp.200.members.description` |  | The author's profile bio text. | 作者资料页的个人简介文字。 |
| `resp.200.members.location` |  | Free-text location the author lists on their profile. | 作者在资料页填写的所在地（自由文本）。 |
| `resp.200.members.followers` |  | Number of accounts following the author. | 关注作者的账号数。 |
| `resp.200.members.following` |  | Number of accounts the author follows. | 作者关注的账号数。 |
| `resp.200.members.canDm` |  | Whether the author currently accepts direct messages from the requester. | 作者当前是否接受请求方的私信。 |
| `resp.200.members.createdAt` |  | Timestamp when the author's account was created. | 作者账号的创建时间。 |
| `resp.200.members.favouritesCount` |  | Number of tweets the author has liked. | 作者点赞过的推文数。 |
| `resp.200.members.hasCustomTimelines` |  | Whether the author has created custom timelines. | 作者是否创建过自定义时间线。 |
| `resp.200.members.isTranslator` |  | Whether the author participates in the Twitter translation program. | 作者是否参与 Twitter 翻译计划。 |
| `resp.200.members.mediaCount` |  | Number of media items the author has posted. | 作者发布过的媒体条目数。 |
| `resp.200.members.statusesCount` |  | Total number of tweets the author has posted. | 作者发布过的推文总数。 |
| `resp.200.members.withheldInCountries` |  | Country codes where the author's account is withheld for legal reasons. | 因法律原因屏蔽作者账号的国家／地区代码列表。 |
| `resp.200.members.possiblySensitive` |  | Whether the author's posts are flagged as potentially sensitive. | 作者的内容是否被标记为可能含敏感信息。 |
| `resp.200.members.pinnedTweetIds` |  | Identifiers of tweets the author has pinned to the top of their profile. | 作者置顶在资料页顶部的推文标识列表。 |
| `resp.200.members.isAutomated` |  | Whether the account is labeled as an automated (bot) account. | 该账号是否被标记为自动化（机器人）账号。 |
| `resp.200.members.automatedBy` |  | Username of the person or entity managing the automated account. | 管理该自动化账号的个人或机构的用户名。 |
| `resp.200.members.unavailable` |  | Whether the author's account is currently unavailable, for example suspended or deactivated. | 作者账号当前是否不可用，例如被封禁或停用。 |
| `resp.200.members.message` |  | Explanatory message returned when the account is unavailable. | 账号不可用时返回的说明信息。 |
| `resp.200.members.unavailableReason` |  | Reason code or text describing why the account is unavailable. | 描述账号不可用原因的代码或文字。 |
| `resp.200.members.profile_bio` |  | The author's profile bio along with the entities parsed from it. | 作者的资料简介及从中解析出的实体。 |
| `resp.200.members.profile_bio.description` |  | The raw bio text shown on the author's profile. | 作者资料页展示的原始简介文字。 |
| `resp.200.members.profile_bio.entities` |  | Structured entities parsed from the bio, covering both the bio text and the profile website field. | 从简介中解析出的结构化实体，涵盖简介文字与资料页网址字段。 |
| `resp.200.members.profile_bio.entities.description` |  | Entities parsed from the bio description text. | 从简介描述文字中解析出的实体。 |
| `resp.200.members.profile_bio.entities.description.urls` |  | Links found in the bio description text. | 简介描述文字中出现的链接。 |
| `resp.200.members.profile_bio.entities.description.urls.display_url` |  | Shortened, human-readable form of the link as displayed in the bio. | 简介中显示的链接的短化、易读形式。 |
| `resp.200.members.profile_bio.entities.description.urls.expanded_url` |  | Full destination URL the displayed link resolves to. | 显示链接最终指向的完整目标地址。 |
| `resp.200.members.profile_bio.entities.description.urls.indices` |  | Start and end character offsets of the link within the bio text. | 该链接在简介文字中的起止字符位置。 |
| `resp.200.members.profile_bio.entities.description.urls.url` |  | The t.co shortened URL as it literally appears in the bio text. | 简介文字中实际出现的 t.co 短链接。 |
| `resp.200.members.profile_bio.entities.url` |  | Entities parsed from the profile website field. | 从资料页网址字段中解析出的实体。 |
| `resp.200.members.profile_bio.entities.url.urls` |  | Links found in the profile website field. | 资料页网址字段中出现的链接。 |
| `resp.200.members.profile_bio.entities.url.urls.display_url` |  | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.members.profile_bio.entities.url.urls.expanded_url` |  | Full destination URL the displayed website link resolves to. | 显示的网址链接最终指向的完整目标地址。 |
| `resp.200.members.profile_bio.entities.url.urls.indices` |  | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.members.profile_bio.entities.url.urls.url` |  | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
| `resp.200.has_next_page` |  | Whether more pages remain; if true, call again with next_cursor to fetch them. | 是否还有更多页；为真时用 next_cursor 再次请求即可获取。 |
| `resp.200.next_cursor` |  | Cursor to pass as the cursor parameter on the next call to fetch the following page. | 下一次请求时作为 cursor 参数传入，用于获取下一页的游标。 |

## GET /twitter/community/tweets

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Retrieve tweets of a community. | Retrieve tweets posted within a community, returned one page at a time with cursor pagination. | 获取某社区内发布的推文，按页返回并通过游标翻页。 |
| `param:community_id` | ID of the community | Identifier of the community whose tweets you want to list. | 要列出其推文的社区标识。 |
| `param:cursor` | Cursor for pagination | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.tweets` |  | Tweets posted in the community, returned for this page. | 本页返回的该社区内发布的推文。 |
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
| `resp.200.tweets.author.profile_bio` |  | The author's profile bio along with the entities parsed from it. | 作者的资料简介及从中解析出的实体。 |
| `resp.200.tweets.author.profile_bio.description` |  | The raw bio text shown on the author's profile. | 作者资料页展示的原始简介文字。 |
| `resp.200.tweets.author.profile_bio.entities` |  | Structured entities parsed from the bio, covering both the bio text and the profile website field. | 从简介中解析出的结构化实体，涵盖简介文字与资料页网址字段。 |
| `resp.200.tweets.author.profile_bio.entities.description` |  | Entities parsed from the bio description text. | 从简介描述文字中解析出的实体。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls` |  | Links found in the bio description text. | 简介描述文字中出现的链接。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.display_url` |  | Shortened, human-readable form of the link as displayed in the bio. | 简介中显示的链接的短化、易读形式。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.expanded_url` |  | Full destination URL the displayed link resolves to. | 显示链接最终指向的完整目标地址。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.indices` |  | Start and end character offsets of the link within the bio text. | 该链接在简介文字中的起止字符位置。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.url` |  | The t.co shortened URL as it literally appears in the bio text. | 简介文字中实际出现的 t.co 短链接。 |
| `resp.200.tweets.author.profile_bio.entities.url` |  | Entities parsed from the profile website field. | 从资料页网址字段中解析出的实体。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls` |  | Links found in the profile website field. | 资料页网址字段中出现的链接。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.display_url` |  | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.expanded_url` |  | Full destination URL the displayed website link resolves to. | 显示的网址链接最终指向的完整目标地址。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.indices` |  | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.url` |  | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
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

## GET /twitter/community/get_tweets_from_all_community

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Search tweets from all communities. | Search tweets across all communities using a query string, choosing between the most recent matches or the top-ranked ones, with cursor pagination. | 使用查询字符串跨全部社区搜索推文，可在最新匹配与热门排序结果之间选择，并通过游标翻页。 |
| `param:query` | Search query (e.g., keyword) | Search query string, such as a keyword, used to match tweets across all communities. | 搜索查询字符串（如关键词），用于跨全部社区匹配推文。 |
| `param:queryType` | Query type (Latest or Top) | Ranking mode of the results: Latest returns the most recent matches, Top returns the most relevant or popular ones. | 结果的排序模式：Latest 返回最新匹配，Top 返回最相关或最热门的结果。 |
| `param:cursor` | Cursor for pagination | Pagination cursor from the previous response's next_cursor; leave empty to start from the first page. | 翻页游标，取自上一次响应的 next_cursor；首页请求留空即可。 |
| `resp.200.tweets` |  | Tweets matching the search across communities, returned for this page. | 本页返回的跨社区匹配搜索条件的推文。 |
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
| `resp.200.tweets.author.profile_bio` |  | The author's profile bio along with the entities parsed from it. | 作者的资料简介及从中解析出的实体。 |
| `resp.200.tweets.author.profile_bio.description` |  | The raw bio text shown on the author's profile. | 作者资料页展示的原始简介文字。 |
| `resp.200.tweets.author.profile_bio.entities` |  | Structured entities parsed from the bio, covering both the bio text and the profile website field. | 从简介中解析出的结构化实体，涵盖简介文字与资料页网址字段。 |
| `resp.200.tweets.author.profile_bio.entities.description` |  | Entities parsed from the bio description text. | 从简介描述文字中解析出的实体。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls` |  | Links found in the bio description text. | 简介描述文字中出现的链接。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.display_url` |  | Shortened, human-readable form of the link as displayed in the bio. | 简介中显示的链接的短化、易读形式。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.expanded_url` |  | Full destination URL the displayed link resolves to. | 显示链接最终指向的完整目标地址。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.indices` |  | Start and end character offsets of the link within the bio text. | 该链接在简介文字中的起止字符位置。 |
| `resp.200.tweets.author.profile_bio.entities.description.urls.url` |  | The t.co shortened URL as it literally appears in the bio text. | 简介文字中实际出现的 t.co 短链接。 |
| `resp.200.tweets.author.profile_bio.entities.url` |  | Entities parsed from the profile website field. | 从资料页网址字段中解析出的实体。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls` |  | Links found in the profile website field. | 资料页网址字段中出现的链接。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.display_url` |  | Shortened, human-readable form of the website link as displayed. | 显示的网址链接的短化、易读形式。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.expanded_url` |  | Full destination URL the displayed website link resolves to. | 显示的网址链接最终指向的完整目标地址。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.indices` |  | Start and end character offsets of the link within the website field. | 该链接在网址字段中的起止字符位置。 |
| `resp.200.tweets.author.profile_bio.entities.url.urls.url` |  | The t.co shortened URL as it literally appears in the website field. | 网址字段中实际出现的 t.co 短链接。 |
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

