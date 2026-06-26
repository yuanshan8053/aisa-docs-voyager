# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 2 个接口，61 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## GET /twitter/trends

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get trends by WOEID. | Return the list of trending topics for a given location, identified by its WOEID. | 返回指定地点（以 WOEID 标识）的热门趋势列表。 |
| `param:woeid` | The WOEID of the location. Example: 2418046. | The WOEID (Where On Earth ID) identifying the location whose trends you want. | 标识目标地点的 WOEID（Where On Earth ID），用于取该地的趋势。 |
| `param:count` | The number of trends to return. Default is 30. | How many trends to return. | 返回趋势的数量。 |
| `resp.200.trends` |  | The list of trending topics for the requested location. | 所请求地点的热门趋势列表。 |
| `resp.200.trends.name` |  | Display name of the trend. | 趋势的显示名称。 |
| `resp.200.trends.target` |  | The search target this trend resolves to. | 该趋势对应的搜索目标。 |
| `resp.200.trends.target.query` |  | The search query string that opens this trend's results. | 打开该趋势结果所用的搜索查询字符串。 |
| `resp.200.trends.rank` |  | Position of the trend in the list, where a smaller number ranks higher. | 趋势在榜单中的名次，数字越小排名越靠前。 |
| `resp.200.trends.meta_description` |  | Supplementary descriptive text for the trend, such as associated post volume or context. | 趋势的补充描述文本，如相关讨论量或背景信息。 |
| `resp.200.status` |  | Whether the request succeeded or errored. | 请求是成功还是出错。 |
| `resp.200.msg` |  | Accompanying message, typically the error detail when the request did not succeed. | 附带消息，通常是请求未成功时的错误详情。 |

## GET /twitter/spaces/detail

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get details of a Twitter Space by its ID. | Return the full details of a single Twitter Space, including its settings, audience stats, and creator profile. | 返回单个 Twitter Space 的完整详情，包括设置、听众统计与创建者资料。 |
| `param:space_id` | The ID of the space. | Identifier of the Twitter Space to look up. | 要查询的 Twitter Space 标识。 |
| `resp.200.data` |  | The Space's detail payload. | Space 的详情数据。 |
| `resp.200.data.id` |  | Identifier of the Space. | Space 的标识。 |
| `resp.200.data.title` |  | Title of the Space. | Space 的标题。 |
| `resp.200.data.state` |  | Current lifecycle state of the Space, such as whether it is scheduled, live, or ended. | Space 当前的生命周期状态，如已排期、直播中或已结束。 |
| `resp.200.data.created_at` |  | When the Space was created. | Space 的创建时间。 |
| `resp.200.data.scheduled_start` |  | When the Space is scheduled to start. | Space 计划开始的时间。 |
| `resp.200.data.updated_at` |  | When the Space's record was last updated. | Space 记录最近一次更新的时间。 |
| `resp.200.data.media_key` |  | Media key referencing the Space's audio stream. | 指向该 Space 音频流的媒体键。 |
| `resp.200.data.is_subscribed` |  | Whether the requesting user is subscribed to the Space. | 发起请求的用户是否已订阅该 Space。 |
| `resp.200.data.settings` |  | The Space's configuration settings. | Space 的配置项。 |
| `resp.200.data.settings.conversation_controls` |  | Coded value indicating who is permitted to participate in the conversation.<br>[⚠️Note:源码未声明该整数各取值的含义，待研发确认。] | 表示谁可参与对话的编码值。<br>[⚠️批注:源码未声明该整数各取值的含义，待研发确认。] |
| `resp.200.data.settings.disallow_join` |  | Whether new participants are blocked from joining the Space. | 是否禁止新参与者加入该 Space。 |
| `resp.200.data.settings.is_employee_only` |  | Whether the Space is restricted to employees only. | 该 Space 是否仅限员工。 |
| `resp.200.data.settings.is_locked` |  | Whether the Space is locked. | 该 Space 是否已锁定。 |
| `resp.200.data.settings.is_muted` |  | Whether the Space is muted for the requesting user. | 该 Space 对发起请求的用户是否已静音。 |
| `resp.200.data.settings.is_space_available_for_clipping` |  | Whether clips may be created from the Space. | 是否允许从该 Space 制作剪辑。 |
| `resp.200.data.settings.is_space_available_for_replay` |  | Whether a replay of the Space is available. | 该 Space 是否提供回放。 |
| `resp.200.data.settings.no_incognito` |  | Whether anonymous (incognito) listening is disallowed. | 是否禁止匿名（隐身）收听。 |
| `resp.200.data.settings.narrow_cast_space_type` |  | Coded value indicating the Space's narrowcast type.<br>[⚠️Note:源码未声明该整数各取值的含义，待研发确认。] | 表示该 Space 定向广播类型的编码值。<br>[⚠️批注:源码未声明该整数各取值的含义，待研发确认。] |
| `resp.200.data.settings.max_guest_sessions` |  | Maximum number of concurrent guest speaker sessions allowed. | 允许的并发嘉宾发言会话数上限。 |
| `resp.200.data.settings.max_admin_capacity` |  | Maximum number of admins the Space can have. | 该 Space 可拥有的管理员数量上限。 |
| `resp.200.data.stats` |  | Audience statistics for the Space. | Space 的听众统计。 |
| `resp.200.data.stats.total_replay_watched` |  | Total number of replay views. | 回放观看的总次数。 |
| `resp.200.data.stats.total_live_listeners` |  | Total number of live listeners. | 实时收听的总人数。 |
| `resp.200.data.stats.total_participants` |  | Total number of participants across the Space. | 该 Space 的参与者总人数。 |
| `resp.200.data.creator` |  | Profile of the user who created the Space. | 创建该 Space 的用户资料。 |
| `resp.200.data.creator.id` |  | Identifier of the creator. | 创建者的标识。 |
| `resp.200.data.creator.name` |  | Display name of the creator. | 创建者的显示名称。 |
| `resp.200.data.creator.userName` |  | Handle (@username) of the creator. | 创建者的用户名（@username）。 |
| `resp.200.data.creator.location` |  | Location listed on the creator's profile. | 创建者资料中填写的所在地。 |
| `resp.200.data.creator.url` |  | Website URL listed on the creator's profile. | 创建者资料中填写的网站链接。 |
| `resp.200.data.creator.description` |  | Bio text on the creator's profile. | 创建者资料中的简介文本。 |
| `resp.200.data.creator.protected` |  | Whether the creator's account is protected (private). | 创建者账号是否受保护（私密）。 |
| `resp.200.data.creator.isVerified` |  | Whether the creator's account is verified. | 创建者账号是否已认证。 |
| `resp.200.data.creator.isBlueVerified` |  | Whether the creator holds a Twitter Blue verification. | 创建者是否拥有 Twitter Blue 认证。 |
| `resp.200.data.creator.verifiedType` |  | The kind of verification the creator's account holds. | 创建者账号所持认证的类型。 |
| `resp.200.data.creator.followers` |  | Number of accounts following the creator. | 关注该创建者的账号数。 |
| `resp.200.data.creator.following` |  | Number of accounts the creator follows. | 该创建者关注的账号数。 |
| `resp.200.data.creator.favouritesCount` |  | Number of tweets the creator has liked. | 该创建者点赞过的推文数。 |
| `resp.200.data.creator.statusesCount` |  | Number of tweets the creator has posted. | 该创建者发布的推文数。 |
| `resp.200.data.creator.mediaCount` |  | Number of media items the creator has posted. | 该创建者发布的媒体条目数。 |
| `resp.200.data.creator.createdAt` |  | When the creator's account was created. | 创建者账号的注册时间。 |
| `resp.200.data.creator.coverPicture` |  | URL of the creator's profile cover image. | 创建者资料封面图的链接。 |
| `resp.200.data.creator.profilePicture` |  | URL of the creator's profile avatar. | 创建者头像的链接。 |
| `resp.200.data.creator.canDm` |  | Whether the requesting user can send the creator a direct message. | 发起请求的用户是否可以向该创建者发送私信。 |
| `resp.200.data.creator.affiliatesHighlightedLabel` |  | Highlighted affiliation label shown on the creator's profile. | 创建者资料上展示的关联机构高亮标签。 |
| `resp.200.data.creator.isAutomated` |  | Whether the creator's account is marked as automated (a bot). | 创建者账号是否被标记为自动化（机器人）账号。 |
| `resp.200.data.creator.automatedBy` |  | Identifier of the account that manages this automated account. | 管理该自动化账号的账号标识。 |
| `resp.200.status` |  | Whether the request succeeded or errored. | 请求是成功还是出错。 |
| `resp.200.msg` |  | Accompanying message, typically the error detail when the request did not succeed. | 附带消息，通常是请求未成功时的错误详情。 |

