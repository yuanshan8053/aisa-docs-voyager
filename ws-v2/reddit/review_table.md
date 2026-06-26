# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 5 个接口，20 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## get_reddit-search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Searches across all of Reddit for posts matching a query. Each post includes title, author, selftext, subreddit, score, ups, upvote_ratio, num_comments, created_utc, url, permalink, and is_video. Supports sort (relevance, new, top, comment_count), timeframe filtering, pagination via the after token, and a trim parameter for lighter responses. | Search across all of Reddit for posts matching a query, with sorting, time-window filtering, and token-based pagination. Read-only. | 在整个 Reddit 范围内检索匹配查询词的帖子,支持排序、时间窗口筛选与基于令牌的翻页。只读接口。 |
| `param:query` | Search query | The search phrase used to match posts across Reddit. | 用于在全站匹配帖子的搜索短语。 |
| `param:sort` | Sort by | Ordering of the matched posts: `relevance` by best match to the query, `new` by most recent, `top` by highest score, and `comment_count` by most-discussed. | 命中帖子的排序方式:`relevance` 按与查询词的匹配度,`new` 按发布时间从新到旧,`top` 按得分从高到低,`comment_count` 按评论数从多到少。 |
| `param:timeframe` | Timeframe | Restricts results to posts created within a time window, from all time down to the last day. Most meaningful when combined with score- or comment-based sorting. | 将结果限定在某个时间窗口内创建的帖子,范围从全部时间到最近一天。与按得分或评论数排序搭配时最有意义。 |
| `param:after` | Used to paginate to next page | Pagination token for the next page; take it from the `after` field of a previous response. Omit it to start from the first page. | 翻页令牌,用于取下一页;取自上一次响应的 `after` 字段。留空则从第一页开始。 |
| `param:trim` | Set to true for a trimmed down version of the response | When enabled, returns a lighter response with fewer per-post fields, reducing payload size. | 开启后返回更精简的响应,削减每条帖子的字段,降低载荷体积。 |

## get_reddit-subreddit

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches posts from a subreddit with sorting and filtering options. Each post includes title, author, selftext, score, ups, upvote_ratio, num_comments, created_utc, url, permalink, subreddit_subscribers, and is_video. Supports sort (best, hot, new, top, rising), timeframe filtering, pagination via the after token, and a trim parameter for lighter responses. | List posts from a single subreddit, with sorting, time-window filtering, and token-based pagination. Read-only. | 列出某个子版块(subreddit)内的帖子,支持排序、时间窗口筛选与基于令牌的翻页。只读接口。 |
| `param:subreddit` | Subreddit name | Name of the subreddit to list posts from. | 要列出帖子的子版块名称。 |
| `param:timeframe` | Timeframe to get posts from | Restricts listed posts to those created within a time window, from all time down to the last day. Most meaningful with score-based sorting. | 将列出的帖子限定在某个时间窗口内创建的,范围从全部时间到最近一天。与按得分排序搭配时最有意义。 |
| `param:sort` | Sort order | Ordering of the listed posts: `best` by Reddit's blended ranking, `hot` by current trending activity, `new` by most recent, `top` by highest score, and `rising` by posts gaining traction quickly. | 列出帖子的排序方式:`best` 按 Reddit 综合排名,`hot` 按当前热度,`new` 按发布时间从新到旧,`top` 按得分从高到低,`rising` 按正在快速升温的帖子。 |
| `param:after` | After to get more posts. Get 'after' from previous response. | Pagination token for the next page; take it from the `after` field of a previous response. Omit it to start from the first page. | 翻页令牌,用于取下一页;取自上一次响应的 `after` 字段。留空则从第一页开始。 |
| `param:trim` | Set to true for a trimmed down version of the response | When enabled, returns a lighter response with fewer per-post fields, reducing payload size. | 开启后返回更精简的响应,削减每条帖子的字段,降低载荷体积。 |

## get_reddit-subreddit-details

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Retrieves metadata about a subreddit by name or URL. The subreddit name must be case-sensitive. Returns display_name, description, subscribers, weekly_active_users, weekly_contributions, rules, icon_img, header_img, advertiser_category, submit_text, and created_at. | Retrieve metadata about a single subreddit, looked up by its name or URL. Read-only. | 按名称或 URL 查询单个子版块的元信息。只读接口。 |
| `param:subreddit` | Subreddit name. MUST be case sensitive. So 'AskReddit' not 'askreddit'. | Name of the subreddit to look up. The name is case-sensitive, so it must match the community's exact casing. | 要查询的子版块名称。该名称区分大小写,须与社区的精确写法一致。 |
| `param:url` | Subreddit URL | Full URL of the subreddit, usable as an alternative to looking it up by name. | 子版块的完整 URL,可作为按名称查询之外的另一种定位方式。 |

## get_reddit-subreddit-search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Searches within a specific subreddit for posts, comments, and media matching a query. Returns posts with title, votes, num_comments, url, and created_at; comments with author, body, votes, and parent post info; and media with title, media_type, image dimensions, and gallery_count. Supports sort, timeframe filtering, and cursor-based pagination. | Search within one subreddit for matching posts, comments, and media, with sorting, time-window filtering, and cursor-based pagination. Read-only. | 在指定子版块内检索匹配的帖子、评论与媒体,支持排序、时间窗口筛选与基于游标的翻页。只读接口。 |
| `param:subreddit` | Subreddit name (e.g. 'Fitness', not 'r/Fitness' or a full URL) | Name of the subreddit to search within. Pass the bare community name, not an `r/`-prefixed name or a full URL. | 要在其中搜索的子版块名称。传入纯社区名,不要带 `r/` 前缀,也不要传完整 URL。 |
| `param:query` | Search query to find matching content | Search phrase used to match content inside the subreddit. | 用于在该子版块内匹配内容的搜索短语。 |
| `param:sort` | Sort order. For posts/media: relevance, hot, top, new, comments. For comments: relevance, top, new | Ordering of results. The applicable values differ by content kind: posts and media support relevance, hot, top, new, and comment-count ordering, while comments support relevance, top, and new. | 结果的排序方式。可用取值随内容类型而异:帖子与媒体支持按相关性、热度、得分、时间及评论数排序,评论支持按相关性、得分与时间排序。 |
| `param:timeframe` | Timeframe to filter results | Restricts results to content created within a time window, from all time down to the last hour. | 将结果限定在某个时间窗口内创建的内容,范围从全部时间到最近一小时。 |
| `param:cursor` | Cursor to get more results. Get 'cursor' from previous response. | Cursor for the next page of results; take it from the `cursor` field of a previous response. Omit it to start from the first page. | 用于取下一页结果的游标;取自上一次响应的 `cursor` 字段。留空则从第一页开始。 |

## get_reddit-post-comments

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Retrieves comments and post details from a Reddit post by URL. Returns the post with title, author, score, ups, upvote_ratio, num_comments, and created_utc, plus a comments array where each comment includes author, body, body_html, score, created_utc, parent_id, permalink, and nested replies. Supports cursor-based pagination for loading more comments and a trim parameter for lighter responses. | Fetch a post together with its comment tree, identified by the post URL, with cursor-based pagination for loading more comments and replies. Read-only. | 按帖子 URL 获取该帖及其评论树,支持以游标翻页加载更多评论与回复。只读接口。 |
| `param:url` | Reddit post URL | URL of the Reddit post whose comments and details you want to fetch. | 要获取评论与详情的 Reddit 帖子 URL。 |
| `param:cursor` | Cursor to get more comments, or replies. | Cursor for loading more comments or replies; take it from a previous response. Omit it to load the first batch. | 用于加载更多评论或回复的游标;取自上一次响应。留空则加载首批。 |
| `param:trim` | Set to true for a trimmed down version of the response | When enabled, returns a lighter response with fewer fields, reducing payload size. | 开启后返回更精简的响应,削减字段,降低载荷体积。 |

