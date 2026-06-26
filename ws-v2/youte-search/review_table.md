# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 1 个接口，11 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## GET /youtube/search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Perform a YouTube search via SearchApi | Search YouTube through the SearchApi aggregation engine and return a structured list of matching videos. This is a read-only query: narrow results with a country and interface language, or paginate and apply advanced sorting via YouTube's own filter token. Typical uses are content discovery, competitive monitoring, and sourcing material. | 通过 SearchApi 聚合引擎检索 YouTube 视频,返回结构化的命中列表。这是只读查询接口:可用地区与界面语言收窄结果,或借 YouTube 自身的过滤令牌翻页并施加高级排序。典型场景为内容发现、竞品监测与素材采集。 |
| `param:engine` | Engine identifier for YouTube Search | Selects which search backend to route the request to. For this endpoint it is always `youtube`, pinning the call to YouTube's search channel. | 选择请求路由到哪个搜索后端。本接口固定为 `youtube`,将调用锁定在 YouTube 搜索通道。 |
| `param:q` | Search query | The search phrase, exactly as a user would type it into YouTube's search box. It is the primary signal that determines which videos come back and in what relevance order. | 搜索短语,等同用户在 YouTube 搜索框中键入的内容。它是决定返回哪些视频、以何种相关性排序的首要信号。 |
| `param:sp` | YouTube filter token (pagination or advanced filters) | YouTube's opaque filter token. Pass it to page forward or to carry advanced filters such as upload date, duration, or sort order. The value is not constructed by hand — copy it from a previous response or from YouTube's frontend and pass it through unchanged. | YouTube 的不透明过滤令牌。用它向后翻页,或承载上传时间、时长、排序等高级筛选。该值不靠手工拼造 —— 从上一次响应或 YouTube 前端取得后原样透传。 |
| `param:gl` | Country code (e.g. us, jp) | Country of the search context, given as a two-letter code such as `us` or `jp`. It localizes which results surface and how they rank. Omit it to fall back to the engine's default region. | 检索所处的国家,用 `us`、`jp` 这类两字母代码表示。它决定结果的地域化呈现与排序。留空则回落到引擎默认地区。 |
| `param:hl` | Interface language | Interface language for the search, given as a language code. It controls the language of localized text in the results, not which videos match. Omit it to fall back to the engine's default language. | 检索的界面语言,用语言代码表示。它影响结果中本地化文案的语言,而非命中哪些视频。留空则回落到引擎默认语言。 |
| `resp.200.search_metadata` | Search metadata | Metadata about this search request, recording status and other query-level context useful for troubleshooting and auditing. | 本次检索请求的元信息,记录状态等查询级上下文,便于排障与审计。 |
| `resp.200.search_results` |  | The matched videos, ordered by the engine's relevance ranking. Each element is one video record. | 命中的视频,按引擎相关性排序。每个元素是一条视频记录。 |
| `resp.200.search_results.video_id` |  | YouTube's unique identifier for the video. Use it to build a watch URL or as the input to downstream video APIs. | 视频在 YouTube 上的唯一标识。可用于拼接播放地址,或作为下游视频接口的入参。 |
| `resp.200.search_results.title` |  | The video's display title. | 视频的展示标题。 |
| `resp.200.search_results.link` |  | Direct, clickable watch URL for the video. | 视频的可直接点击播放链接。 |
| `resp.200.search_results.channel_name` |  | Name of the channel that published the video. | 发布该视频的频道名称。 |

