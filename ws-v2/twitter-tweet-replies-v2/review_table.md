# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 1 个接口，27 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## GET /twitter/tweet/replies/v2

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get tweet replies by tweet ID (V2). Each page returns up to 20 replies. Supports sorting by Relevance, Latest, or Likes. | Fetch the replies to a given tweet, returned one page at a time and ordered by relevance, recency, or like count. Read-only; use the returned cursor to walk through subsequent pages. | 拉取某条推文下的回复,分页返回,可按相关性、时间或点赞数排序。只读接口,借响应中返回的游标逐页向后翻。 |
| `param:tweetId` | The tweet ID to get replies for. e.g. 1846987139428634858 | Identifier of the tweet whose replies you want to retrieve. It is the numeric ID found in the tweet's URL. | 要获取回复的目标推文标识,即推文 URL 中的那串数字 ID。 |
| `param:cursor` | Cursor for paginating through results. Leave empty for the first page. | Pagination token pointing at the next batch of replies. Take it from the `next_cursor` of a previous response; leave it unset to start from the first page. | 指向下一批回复的翻页令牌。取自上一次响应的 `next_cursor`;首次请求留空即从第一页开始。 |
| `param:queryType` | Sort order for replies. Default is Relevance. | Ordering applied to the returned replies: `Relevance` surfaces the replies the platform deems most relevant, `Latest` orders by most recent first, and `Likes` orders by most-liked first. | 返回回复的排序方式:`Relevance` 优先展示平台判定最相关的回复,`Latest` 按时间从新到旧,`Likes` 按点赞数从高到低。 |
| `resp.200.replies` | Array of reply tweets | The replies on this page, each a full tweet object. | 本页的回复,每个元素是一条完整的推文对象。 |
| `resp.200.replies.type` |  | Object kind of the record, distinguishing a tweet from other entities the API may return. | 记录的对象类型,用于区分推文与接口可能返回的其他实体。 |
| `resp.200.replies.id` | The ID of the tweet | The reply tweet's unique identifier; use it to fetch this reply's own replies or to build its URL. | 该回复推文的唯一标识;可用于获取这条回复下的下级回复,或拼接其 URL。 |
| `resp.200.replies.url` | The URL of the tweet | Direct, clickable link to the reply tweet. | 该回复推文的可直接点击链接。 |
| `resp.200.replies.text` | The text of the tweet | Full body text of the reply. | 回复的正文文本。 |
| `resp.200.replies.source` | The source client of the tweet | The client application from which the reply was posted, such as a web or mobile app. | 发布该回复所用的客户端应用,例如网页端或移动端 App。 |
| `resp.200.replies.retweetCount` |  | Number of times the reply has been retweeted. | 该回复被转推的次数。 |
| `resp.200.replies.replyCount` |  | Number of replies this reply itself has received. | 该回复自身收到的回复数。 |
| `resp.200.replies.likeCount` |  | Number of likes the reply has received. | 该回复收到的点赞数。 |
| `resp.200.replies.quoteCount` |  | Number of times the reply has been quote-tweeted. | 该回复被引用转推的次数。 |
| `resp.200.replies.viewCount` |  | Number of times the reply has been viewed. | 该回复的浏览次数。 |
| `resp.200.replies.createdAt` | The date and time the tweet was created | Timestamp of when the reply was posted. | 该回复的发布时间。 |
| `resp.200.replies.lang` | The language of the tweet | Detected language of the reply text, as a language code. | 回复文本经识别得到的语言,以语言代码表示。 |
| `resp.200.replies.bookmarkCount` |  | Number of times the reply has been bookmarked. | 该回复被加入书签的次数。 |
| `resp.200.replies.isReply` |  | Whether this tweet is itself a reply to another tweet. | 该推文本身是否为对另一条推文的回复。 |
| `resp.200.replies.inReplyToId` |  | Identifier of the tweet this reply is responding to. | 该回复所回应的那条推文的标识。 |
| `resp.200.replies.conversationId` |  | Identifier of the conversation thread the reply belongs to; typically the ID of the original tweet that started the thread. | 该回复所属对话串的标识,通常为开启该对话的原始推文 ID。 |
| `resp.200.replies.inReplyToUserId` |  | Identifier of the user being replied to. | 被回复用户的标识。 |
| `resp.200.replies.inReplyToUsername` |  | Handle of the user being replied to. | 被回复用户的用户名。 |
| `resp.200.replies.isLimitedReply` | Whether the tweet is a limited reply | Whether replying to this tweet is restricted by the author's reply settings. | 该推文是否因作者的回复设置而受限,无法自由回复。 |
| `resp.200.has_next_page` | Indicates if there are more results available | Whether more replies remain beyond the current page. | 当前页之后是否还有更多回复。 |
| `resp.200.next_cursor` | Cursor for fetching the next page of results | Token to pass back as `cursor` to retrieve the next page of replies. | 用于取回下一页回复的令牌,回传给 `cursor` 参数即可。 |
| `resp.200.status` | Status of the request | Outcome of the request: `success` for a normal result, `error` when the request failed. | 请求结果:`success` 表示正常返回,`error` 表示请求失败。 |
| `resp.200.message` | Error message if status is error | Human-readable error detail, populated only when the request failed. | 可读的错误说明,仅在请求失败时才有内容。 |

