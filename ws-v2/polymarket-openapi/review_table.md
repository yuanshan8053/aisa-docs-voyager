# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 10 个接口，267 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## get_polymarket-markets

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches market data with optional filtering and search functionality. Supports filtering by market slug, condition ID, token ID, or tags, as well as fuzzy search across market titles and descriptions. Returns markets ordered by volume (most popular first) when filters are applied, or by start_time (most recent first) when no filters are provided. | List prediction markets with optional filtering (by slug, condition ID, token ID, tags, status, volume, time range) and keyword search. Results are ordered by volume when filters are applied, or by start time otherwise, and paginated via a cursor. | 查询预测市场列表，支持按 slug、condition ID、token ID、标签、状态、成交量、时间范围筛选及关键词搜索。施加筛选时按成交量排序，否则按开始时间排序，并以游标分页。 |
| `param:market_slug` | Filter markets by market slug(s). Can provide multiple values. | Restrict results to markets with these slugs; a slug is the market's URL identifier. Repeat the parameter for multiple values. | 按市场 slug（市场的 URL 标识）筛选，可重复传入多个值。 |
| `param:event_slug` | Filter markets by event slug(s). Can provide multiple values. | Restrict results to markets belonging to events with these slugs. Repeat the parameter for multiple values. | 按所属事件的 slug 筛选，可重复传入多个值。 |
| `param:condition_id` | Filter markets by condition ID(s). Can provide multiple values. | Restrict results to markets with these on-chain condition IDs. Repeat the parameter for multiple values. | 按市场链上 condition ID 筛选，可重复传入多个值。 |
| `param:token_id` | Filter markets by token ID(s). Matches markets where the token_id is either the primary_token_id or secondary_token_id. Can provide multiple values (maximum 100). Each token_id must be a numeric string. | Restrict results to markets whose primary or secondary outcome token matches these token IDs. Repeat the parameter for multiple values. | 按结果 token ID 筛选，命中市场的 primary 或 secondary token 即返回，可重复传入多个值。 |
| `param:tags` | Filter markets by tag(s). Can provide multiple values. | Restrict results to markets carrying these category tags. Repeat the parameter for multiple values. | 按市场所带的分类标签筛选，可重复传入多个值。 |
| `param:search` | Search markets by keywords in title and description. Must be URL encoded (e.g., 'bitcoin%20price' for 'bitcoin price'). | Fuzzy keyword search across market titles and descriptions; the value must be URL-encoded. Cannot be combined with other filter parameters. | 对市场标题与描述做模糊关键词搜索，取值需 URL 编码；不可与其他筛选参数同时使用。 |
| `param:status` | Filter markets by status (whether they're open or closed) | Restrict results to markets that are currently open or already closed. | 按市场当前是开放还是已关闭筛选。 |
| `param:min_volume` | Filter markets with total trading volume greater than or equal to this amount (USD) | Only return markets whose total trading volume (in USD) is at least this amount. | 仅返回累计成交量（美元）不低于该值的市场。 |
| `param:limit` | Number of markets to return (1-100). Default: 10 for search, 10 for regular queries. | Maximum number of markets to return in this page. | 本页最多返回的市场数量。 |
| `param:pagination_key` | Base64-encoded cursor for efficient pagination. Returned in the previous response's pagination object. Use this instead of large offsets for better performance. | Cursor for the next page; pass back the value from the previous response's pagination object. Preferred over large offsets for performance. | 翻页游标，回传上一页响应 pagination 中的值；相比大偏移量更高效。 |
| `param:start_time` | Filter markets from this Unix timestamp in seconds (inclusive) | Only return markets at or after this start time, given as a Unix timestamp in seconds. | 仅返回开始时间不早于此刻的市场，Unix 时间戳（秒）。 |
| `param:end_time` | Filter markets until this Unix timestamp in seconds (inclusive) | Only return markets at or before this time, given as a Unix timestamp in seconds. | 仅返回时间不晚于此刻的市场，Unix 时间戳（秒）。 |
| `resp.200.markets` |  | The list of markets matching the query. | 匹配查询条件的市场列表。 |
| `resp.200.markets.market_slug` |  | URL identifier of the market. | 市场的 URL 标识。 |
| `resp.200.markets.event_slug` | The event slug this market belongs to, or null if not associated with an event | Slug of the event this market belongs to; null when the market is not part of an event. | 该市场所属事件的 slug；不属于任何事件时为 null。 |
| `resp.200.markets.condition_id` |  | On-chain condition ID identifying the market. | 标识该市场的链上 condition ID。 |
| `resp.200.markets.title` |  | Human-readable market question or title. | 市场的可读问题或标题。 |
| `resp.200.markets.start_time` | Unix timestamp in seconds when the market starts | When trading on the market opens, as a Unix timestamp in seconds. | 市场开盘时间，Unix 时间戳（秒）。 |
| `resp.200.markets.end_time` | Unix timestamp in seconds when the market ends | When trading on the market ends, as a Unix timestamp in seconds. | 市场结束时间，Unix 时间戳（秒）。 |
| `resp.200.markets.completed_time` | Unix timestamp in seconds when the market was completed | When the market was completed, as a Unix timestamp in seconds; null if not yet completed. | 市场完成时间，Unix 时间戳（秒）；尚未完成时为 null。 |
| `resp.200.markets.close_time` | Unix timestamp in seconds when the market was closed | When the market was closed, as a Unix timestamp in seconds; null if still open. | 市场关闭时间，Unix 时间戳（秒）；仍开放时为 null。 |
| `resp.200.markets.game_start_time` | Datetime string in UTC format (YYYY-MM-DD HH:MM:SS.000) for when the game/event starts. Only present for sports markets that have a game start time. | For sports markets, the UTC datetime when the underlying game starts; null otherwise. | 体育类市场中对应赛事的开始时间（UTC）；非体育市场为 null。 |
| `resp.200.markets.tags` |  | Category tags attached to the market. | 市场所带的分类标签。 |
| `resp.200.markets.volume_1_week` | Trading volume in USD for the past week | Trading volume over the past week, in USD. | 过去一周的成交量（美元）。 |
| `resp.200.markets.volume_1_month` | Trading volume in USD for the past month | Trading volume over the past month, in USD. | 过去一个月的成交量（美元）。 |
| `resp.200.markets.volume_1_year` | Trading volume in USD for the past year | Trading volume over the past year, in USD. | 过去一年的成交量（美元）。 |
| `resp.200.markets.volume_total` | Total trading volume in USD | Cumulative trading volume since inception, in USD. | 自创建以来的累计成交量（美元）。 |
| `resp.200.markets.resolution_source` | URL to the data source used for market resolution | URL of the data source used to resolve the market outcome. | 用于裁定市场结果的数据源 URL。 |
| `resp.200.markets.image` | URL to the market image | URL of the market's display image. | 市场展示图片的 URL。 |
| `resp.200.markets.description` | Detailed description of the market, or null if no description is available | Detailed market description including resolution criteria; null when unavailable. | 市场的详细描述（含裁定标准）；无内容时为 null。 |
| `resp.200.markets.negative_risk_id` | Negative risk identifier for the market, or null if not applicable | Identifier linking related mutually-exclusive markets under a negative-risk group; null when not applicable. | 将互斥相关市场归入 negative-risk 组的标识；不适用时为 null。 |
| `resp.200.markets.side_a` | First side/outcome of the market | The first of the two market outcomes. | 市场两个结果中的第一个。 |
| `resp.200.markets.side_a.id` | Token ID for side A | Outcome token ID for side A. | side A 的结果 token ID。 |
| `resp.200.markets.side_a.label` | Label for side A | Display label for side A's outcome. | side A 结果的展示标签。 |
| `resp.200.markets.side_b` | Second side/outcome of the market | The second of the two market outcomes. | 市场两个结果中的第二个。 |
| `resp.200.markets.side_b.id` | Token ID for side B | Outcome token ID for side B. | side B 的结果 token ID。 |
| `resp.200.markets.side_b.label` | Label for side B | Display label for side B's outcome. | side B 结果的展示标签。 |
| `resp.200.markets.winning_side` | The winning side of the market (null if not yet resolved) | The outcome that won once resolved; null until the market is resolved. | 裁定后的获胜结果；未裁定前为 null。 |
| `resp.200.markets.status` |  | Whether the market is currently open or closed. | 市场当前为开放还是已关闭。 |
| `resp.200.markets.extra_fields` | Additional market-specific fields as a map of key-value pairs. For updown markets (markets with slugs containing '-updown-15m-', '-up-or-down-', or '-updown-4h-'), this object includes 'price_to_beat' and 'final_price' fields. Empty object if no extra fields are present. | Map of market-specific extra fields; for up/down markets it includes price_to_beat and final_price. Empty when none apply. | 市场专有的附加字段映射；涨跌（up/down）类市场含 price_to_beat 与 final_price。无附加字段时为空对象。 |
| `resp.200.pagination` |  | Pagination metadata for the result set. | 结果集的分页元信息。 |
| `resp.200.pagination.limit` |  | The page size applied to this response. | 本次响应采用的页大小。 |
| `resp.200.pagination.total` | Total number of markets matching the filters | Total number of markets matching the filters across all pages. | 所有页中匹配筛选条件的市场总数。 |
| `resp.200.pagination.has_more` | Whether there are more markets available | Whether further pages of results are available. | 是否还有更多结果页可取。 |
| `resp.200.pagination.pagination_key` | Cursor for next page. Only present when has_more is true and using cursor-based pagination. | Cursor to request the next page; present only when has_more is true under cursor pagination. | 请求下一页的游标；仅在游标分页且 has_more 为 true 时出现。 |
| `resp.400.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.400.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.500.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.500.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get_polymarket-events

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches events (groups of related markets) with optional filtering by event_slug, tags/categories and status. Events aggregate multiple markets under a single topic (e.g., 'Presidential Election 2024' contains multiple candidate markets). Returns events ordered by total volume (most popular first).<br><br>**Example Request (single event by slug):**<br>```bash<br>curl 'https://api.aisa.one/apis/v1/polymarket/events?event_slug=presidential-election-winner-2024&include_markets=true'<br>```<br><br>**Example Request (filter by tags):**<br>```bash<br>curl 'https://api.aisa.one/apis/v1/polymarket/events?tags=sports&status=open&limit=10'<br>```<br><br>**Example Request (with markets included):**<br>```bash<br>curl 'https://api.aisa.one/apis/v1/polymarket/events?include_markets=true&limit=5'<br>``` | List events, which group related markets under a single topic, with optional filtering by event slug, tags, status, and time range. Optionally embeds each event's markets when include_markets is enabled. Results are ordered by total volume and paginated via a cursor. | 查询事件列表。事件将相关市场聚合到同一主题下，支持按事件 slug、标签、状态、时间范围筛选；开启 include_markets 时内嵌各事件的市场。结果按总成交量排序并以游标分页。 |
| `param:event_slug` | Filter by specific event slug. When provided, returns a single hydrated event matching that slug (e.g., 'presidential-election-winner-2024'). Use with include_markets=true to get the full event with all its markets. | Return the single event matching this slug; combine with include_markets=true to also embed its markets. | 返回与该 slug 匹配的单个事件；配合 include_markets=true 可一并内嵌其市场。 |
| `param:tags` | Filter events by tag(s)/category. Can provide multiple values (e.g., sports, crypto, politics). | Restrict results to events carrying these category tags. Repeat the parameter for multiple values. | 按事件所带的分类标签筛选，可重复传入多个值。 |
| `param:status` | Filter events by status. An event is 'open' if any of its markets are still open, 'closed' if all markets are closed. | Filter by event status; an event is open if any of its markets is open, otherwise closed. | 按事件状态筛选；只要有一个市场开放即视为 open，全部关闭则为 closed。 |
| `param:include_markets` | Set to 'true' to include the list of markets for each event in the response. | Pass true to embed the full list of markets within each returned event. | 传 true 时在每个返回事件中内嵌其完整市场列表。 |
| `param:start_time` | Filter events starting after this Unix timestamp (seconds) | Only return events starting at or after this Unix timestamp in seconds. | 仅返回开始时间不早于此刻的事件，Unix 时间戳（秒）。 |
| `param:end_time` | Filter events starting before this Unix timestamp (seconds) | Only return events starting at or before this Unix timestamp in seconds. | 仅返回开始时间不晚于此刻的事件，Unix 时间戳（秒）。 |
| `param:game_start_time` | Filter events by game start time (Unix timestamp in seconds). Useful for filtering sports events by when the game starts. | Filter sports events by when the underlying game starts, as a Unix timestamp in seconds. | 按对应赛事开始时间筛选体育类事件，Unix 时间戳（秒）。 |
| `param:limit` | Number of events to return (1-100). Default: 10. | Maximum number of events to return in this page. | 本页最多返回的事件数量。 |
| `param:pagination_key` | Pagination key for cursor-based pagination. Use the value from the previous response's pagination.pagination_key field to get the next page of results. Do not use the deprecated 'offset' parameter. | Cursor for the next page; pass back pagination.pagination_key from the previous response. Do not use the deprecated offset parameter. | 翻页游标，回传上一页响应的 pagination.pagination_key；请勿使用已废弃的 offset 参数。 |
| `resp.200.events` |  | The list of events matching the query. | 匹配查询条件的事件列表。 |
| `resp.200.events.event_slug` | Unique identifier for the event | URL identifier uniquely naming the event. | 唯一标识事件的 URL slug。 |
| `resp.200.events.title` | Event title | Human-readable event title. | 事件的可读标题。 |
| `resp.200.events.subtitle` | Event subtitle or description | Optional subtitle or short description of the event; null when absent. | 事件的副标题或简短描述；无则为 null。 |
| `resp.200.events.status` | Event status - 'open' if any market is open, 'closed' if all markets are closed | Aggregate event status: open if any market is open, closed if all are closed. | 事件的聚合状态：有任一市场开放为 open，全部关闭为 closed。 |
| `resp.200.events.start_time` | Unix timestamp (seconds) when the event started | When the event started, as a Unix timestamp in seconds. | 事件开始时间，Unix 时间戳（秒）。 |
| `resp.200.events.end_time` | Unix timestamp (seconds) when the event ends | When the event ends, as a Unix timestamp in seconds. | 事件结束时间，Unix 时间戳（秒）。 |
| `resp.200.events.volume_fiat_amount` | Total trading volume across all markets in the event (USD) | Total trading volume across all markets in the event, in USD. | 事件下所有市场的总成交量（美元）。 |
| `resp.200.events.settlement_sources` | Resolution/settlement source for the event | Source used to settle/resolve the event; null when unspecified. | 用于结算/裁定事件的来源；未指定时为 null。 |
| `resp.200.events.rules_url` | URL to the event rules (if available) | Link to the event's rules; null when unavailable. | 事件规则的链接；无则为 null。 |
| `resp.200.events.image` | Event image URL | URL of the event's display image; null when none. | 事件展示图片的 URL；无则为 null。 |
| `resp.200.events.tags` | Array of category tags for the event | Category tags attached to the event. | 事件所带的分类标签。 |
| `resp.200.events.market_count` | Number of markets in this event | Number of markets grouped under this event. | 该事件下聚合的市场数量。 |
| `resp.200.events.markets` | List of markets in this event (only included when include_markets=true) | Markets belonging to this event; populated only when include_markets=true. | 该事件下的市场；仅在 include_markets=true 时填充。 |
| `resp.200.events.markets.market_slug` |  | URL identifier of the embedded market. | 内嵌市场的 URL 标识。 |
| `resp.200.events.markets.title` |  | Title of the embedded market. | 内嵌市场的标题。 |
| `resp.200.events.markets.condition_id` |  | On-chain condition ID of the embedded market. | 内嵌市场的链上 condition ID。 |
| `resp.200.events.markets.status` |  | Whether the embedded market is open or closed. | 内嵌市场为开放还是已关闭。 |
| `resp.200.events.markets.volume_total` |  | Cumulative trading volume of the embedded market, in USD. | 内嵌市场的累计成交量（美元）。 |
| `resp.200.pagination` |  | Pagination metadata for the result set. | 结果集的分页元信息。 |
| `resp.200.pagination.limit` | Number of events returned in this response | Number of events returned in this response. | 本次响应返回的事件数量。 |
| `resp.200.pagination.has_more` | Whether there are more events available. If true, use pagination_key to fetch the next page. | Whether further pages are available; if true, use pagination_key to continue. | 是否还有更多页；为 true 时用 pagination_key 继续翻页。 |
| `resp.200.pagination.pagination_key` | Pagination key for fetching the next page. Pass this value as the pagination_key query parameter to get the next page of results. Will be null if has_more is false. | Cursor to fetch the next page; null when has_more is false. | 获取下一页的游标；has_more 为 false 时为 null。 |
| `resp.400.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.400.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.500.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.500.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get_polymarket-orders

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches order data with optional filtering by market, condition, token, time range, and user. Returns orders that match either primary or secondary token IDs for markets. If no filters provided, fetches the latest trades happening in real-time. Only one of market_slug, token_id, or condition_id can be provided. | List on-chain order/trade records, optionally filtered by market, condition, token, user wallet, and time range. With no filters it returns the latest real-time trades. Only one of market_slug, token_id, or condition_id may be supplied. | 查询链上订单/成交记录，可按市场、condition、token、用户钱包及时间范围筛选；不传筛选时返回最新的实时成交。market_slug、token_id、condition_id 三者只能择一传入。 |
| `param:market_slug` | Filter orders by market slug | Restrict orders to a single market identified by its slug. Mutually exclusive with token_id and condition_id. | 按市场 slug 限定订单，与 token_id、condition_id 互斥。 |
| `param:condition_id` | Filter orders by condition ID | Restrict orders to a single market identified by its on-chain condition ID. Mutually exclusive with market_slug and token_id. | 按链上 condition ID 限定订单，与 market_slug、token_id 互斥。 |
| `param:token_id` | Filter orders by token ID | Restrict orders to those touching this outcome token ID. Mutually exclusive with market_slug and condition_id. | 按结果 token ID 限定订单，与 market_slug、condition_id 互斥。 |
| `param:start_time` | Filter orders from this Unix timestamp in seconds (inclusive) | Only return orders placed at or after this Unix timestamp in seconds. | 仅返回下单时间不早于此刻的订单，Unix 时间戳（秒）。 |
| `param:end_time` | Filter orders until this Unix timestamp in seconds (inclusive) | Only return orders placed at or before this Unix timestamp in seconds. | 仅返回下单时间不晚于此刻的订单，Unix 时间戳（秒）。 |
| `param:limit` | Number of orders to return (1-1000) | Maximum number of orders to return in this page. | 本页最多返回的订单数量。 |
| `param:pagination_key` | Base64-encoded cursor for efficient pagination. Returned in the previous response's pagination object. | Cursor for the next page; pass back the value from the previous response's pagination object. | 翻页游标，回传上一页响应 pagination 中的值。 |
| `param:user` | Filter orders by user (wallet address) | Restrict orders to those made by this user wallet address. | 按用户钱包地址限定订单。 |
| `resp.200.orders` |  | The list of matching order/trade records. | 匹配的订单/成交记录列表。 |
| `resp.200.orders.token_id` |  | Outcome token ID this order traded. | 该订单交易的结果 token ID。 |
| `resp.200.orders.token_label` | Human readable label for this outcome (yes/no etc) | Human-readable label of the traded outcome (e.g. Yes/No). | 所交易结果的可读标签（如 Yes/No）。 |
| `resp.200.orders.side` |  | Whether the order bought or sold the outcome token. | 该订单是买入还是卖出结果 token。 |
| `resp.200.orders.market_slug` |  | Slug of the market the order belongs to. | 订单所属市场的 slug。 |
| `resp.200.orders.condition_id` |  | On-chain condition ID of the order's market. | 订单所属市场的链上 condition ID。 |
| `resp.200.orders.shares` | Raw number of shares purchased (from the blockchain) | Raw share quantity as recorded on-chain (before normalization). | 链上记录的原始份额数量（未归一化）。 |
| `resp.200.orders.shares_normalized` | Number of shares purchased normalized (this is raw divided by 1000000) | Share quantity normalized to whole-share units (raw value scaled down by 1,000,000). | 归一化后的份额数量（原始值除以 1,000,000）。 |
| `resp.200.orders.price` | Price per share | Execution price per share.<br>[⚠️Note:源码未声明价格单位与取值范围，待研发确认。] | 每份额的成交价格。<br>[⚠️批注:源码未声明价格单位与取值范围，待研发确认。] |
| `resp.200.orders.block_number` | Block number where the order was placed | Block height at which the order was recorded on-chain. | 订单上链所在的区块高度。 |
| `resp.200.orders.log_index` | Log index of the order event in the block | Index of the order's event log within its block. | 订单事件日志在区块内的索引。 |
| `resp.200.orders.tx_hash` | Transaction hash of the order | Hash of the transaction that recorded the order. | 记录该订单的交易哈希。 |
| `resp.200.orders.title` | Market title | Title of the order's market. | 订单所属市场的标题。 |
| `resp.200.orders.timestamp` | Unix timestamp in seconds when the order was placed | When the order was placed, as a Unix timestamp in seconds. | 下单时间，Unix 时间戳（秒）。 |
| `resp.200.orders.order_hash` | Hash of the order | Hash identifying the order. | 标识该订单的哈希。 |
| `resp.200.orders.user` | Maker address of the order | Maker wallet address of the order. | 订单的 maker 钱包地址。 |
| `resp.200.orders.taker` | Taker address that was part of this trade. Note: This can often be the CTF exchange and is not always the true taker, proceed with caution using taker information | Taker wallet address in the trade; note it is often the CTF exchange rather than the true counterparty, so use with caution. | 成交中的 taker 钱包地址；注意它常是 CTF 交易所而非真实对手方，使用时需谨慎。 |
| `resp.200.pagination` |  | Pagination metadata for the result set. | 结果集的分页元信息。 |
| `resp.200.pagination.limit` |  | The page size applied to this response. | 本次响应采用的页大小。 |
| `resp.200.pagination.offset` |  | Offset applied to this response under offset-based paging. | 基于偏移分页时本次响应采用的偏移量。 |
| `resp.200.pagination.total` | Total number of orders matching the filters | Total number of orders matching the filters. | 匹配筛选条件的订单总数。 |
| `resp.200.pagination.has_more` | Whether there are more orders available | Whether further pages are available. | 是否还有更多结果页。 |
| `resp.200.pagination.pagination_key` | Base64-encoded cursor for the next page. Only present when there are more results. Use this in the next request instead of offset. | Cursor for the next page; present only when more results exist. Prefer it over offset. | 下一页的游标；仅在还有更多结果时出现，优先于 offset 使用。 |
| `resp.400.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.400.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.401.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.401.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.401.docs` |  | Link to documentation explaining the deprecation and the recommended pagination approach. | 指向相关文档的链接，说明该废弃项及推荐的分页方式。 |

## get_polymarket-orderbooks

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches historical orderbook snapshots for a specific asset (token ID) over a specified time range. If no start_time and end_time are provided, returns the latest orderbook snapshot for the market. Returns snapshots of the order book including bids, asks, and market metadata in order. All timestamps are in milliseconds. Orderbook data has history starting from October 14th, 2025. Note: When fetching the latest orderbook (without start/end times), the limit and pagination_key parameters are ignored. | Fetch historical order book snapshots for an outcome token over a time range; when no time range is given, returns only the latest snapshot. Each snapshot contains bids, asks, and market metadata. All timestamps are in milliseconds. | 查询某结果 token 在指定时间范围内的历史订单簿快照；不传时间范围时仅返回最新一份快照。每份快照包含买单、卖单及市场元数据，所有时间戳均为毫秒。 |
| `param:token_id` | The token id (asset) for the Polymarket market | The outcome token (asset) whose order book snapshots are requested. | 待查询订单簿快照的结果 token（资产）。 |
| `param:start_time` | Start time in Unix timestamp (milliseconds). Optional - if not provided along with end_time, returns the latest orderbook snapshot. | Start of the time range, as a Unix timestamp in milliseconds; omit together with end_time to get the latest snapshot only. | 时间范围起点，Unix 时间戳（毫秒）；与 end_time 一并省略时仅取最新快照。 |
| `param:end_time` | End time in Unix timestamp (milliseconds). Optional - if not provided along with start_time, returns the latest orderbook snapshot. | End of the time range, as a Unix timestamp in milliseconds; omit together with start_time to get the latest snapshot only. | 时间范围终点，Unix 时间戳（毫秒）；与 start_time 一并省略时仅取最新快照。 |
| `param:limit` | Maximum number of snapshots to return (default: 100, max: 200). Ignored when fetching the latest orderbook without start_time and end_time. | Maximum number of snapshots to return; ignored when fetching only the latest snapshot. | 最多返回的快照数量；仅取最新快照时忽略该参数。 |
| `param:pagination_key` | Pagination key to get the next chunk of data. Ignored when fetching the latest orderbook without start_time and end_time. | Cursor for the next chunk of snapshots; ignored when fetching only the latest snapshot. | 获取下一批快照的游标；仅取最新快照时忽略该参数。 |
| `resp.200.snapshots` | Array of orderbook snapshots at different points in time | Order book snapshots at successive points in time. | 按时间先后排列的订单簿快照。 |
| `resp.200.snapshots.asks` | Sell orders, ordered by price | Sell-side order book levels, ordered by price. | 卖方订单簿档位，按价格排序。 |
| `resp.200.snapshots.asks.size` |  | Quantity available at this ask level. | 该卖单档位可成交的数量。 |
| `resp.200.snapshots.asks.price` |  | Price of this ask level. | 该卖单档位的价格。 |
| `resp.200.snapshots.bids` | Buy orders, ordered by price | Buy-side order book levels, ordered by price. | 买方订单簿档位，按价格排序。 |
| `resp.200.snapshots.bids.size` |  | Quantity available at this bid level. | 该买单档位可成交的数量。 |
| `resp.200.snapshots.bids.price` |  | Price of this bid level. | 该买单档位的价格。 |
| `resp.200.snapshots.hash` |  | Content hash identifying this snapshot. | 标识该快照内容的哈希。 |
| `resp.200.snapshots.minOrderSize` |  | Minimum allowed order size for this market. | 该市场允许的最小下单数量。 |
| `resp.200.snapshots.negRisk` |  | Whether the market is part of a negative-risk group. | 该市场是否属于 negative-risk 组。 |
| `resp.200.snapshots.assetId` |  | The outcome token (asset) this snapshot is for. | 该快照对应的结果 token（资产）。 |
| `resp.200.snapshots.timestamp` | Timestamp of the snapshot in milliseconds | When the snapshot was taken, as a Unix timestamp in milliseconds. | 快照采集时间，Unix 时间戳（毫秒）。 |
| `resp.200.snapshots.tickSize` |  | Minimum price increment for the market. | 该市场的最小价格变动单位。 |
| `resp.200.snapshots.indexedAt` | When the snapshot was indexed in milliseconds | When the snapshot was indexed by the service, as a Unix timestamp in milliseconds. | 服务为该快照建立索引的时间，Unix 时间戳（毫秒）。 |
| `resp.200.snapshots.market` |  | On-chain condition ID of the market this snapshot belongs to. | 该快照所属市场的链上 condition ID。 |
| `resp.200.pagination` |  | Pagination metadata for the snapshots. | 快照结果的分页元信息。 |
| `resp.200.pagination.limit` |  | The page size applied to this response. | 本次响应采用的页大小。 |
| `resp.200.pagination.count` | Number of snapshots returned | Number of snapshots returned in this response. | 本次响应返回的快照数量。 |
| `resp.200.pagination.pagination_key` | The pagination key to pass in to get the next chunk of data | Cursor to fetch the next chunk of snapshots. | 获取下一批快照的游标。 |
| `resp.200.pagination.has_more` | Whether there are more snapshots available | Whether more snapshots are available. | 是否还有更多快照可取。 |
| `resp.400.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.400.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get_polymarket-activity

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches activity data with optional filtering by user, market, condition, and time range. Returns trading activity including `MERGES`, `SPLITS`, and `REDEEMS`. Supports efficient cursor-based pagination for large datasets. | List on-chain account activity (merges, splits, and redeems), optionally filtered by user wallet, market, condition, and time range, with cursor-based pagination. | 查询链上账户活动（合并 MERGE、拆分 SPLIT、赎回 REDEEM），可按用户钱包、市场、condition 及时间范围筛选，并支持游标分页。 |
| `param:user` | User wallet address to fetch activity for. If not provided, returns activity for all users. | Wallet address whose activity to return; omit to return activity across all users. | 待查询活动的钱包地址；省略则返回所有用户的活动。 |
| `param:start_time` | Filter activity from this Unix timestamp in seconds (inclusive) | Only return activity at or after this Unix timestamp in seconds. | 仅返回时间不早于此刻的活动，Unix 时间戳（秒）。 |
| `param:end_time` | Filter activity until this Unix timestamp in seconds (inclusive) | Only return activity at or before this Unix timestamp in seconds. | 仅返回时间不晚于此刻的活动，Unix 时间戳（秒）。 |
| `param:market_slug` | Filter activity by market slug | Restrict activity to a single market identified by its slug. Mutually exclusive with condition_id. | 按市场 slug 限定活动，与 condition_id 互斥。 |
| `param:condition_id` | Filter activity by condition ID | Restrict activity to a single market identified by its condition ID. Mutually exclusive with market_slug. | 按 condition ID 限定活动，与 market_slug 互斥。 |
| `param:limit` | Number of activities to return (1-1000) | Maximum number of activity records to return in this page. | 本页最多返回的活动记录数量。 |
| `param:pagination_key` | Base64-encoded cursor for efficient pagination. Returned in the previous response's pagination object. | Cursor for the next page; pass back the value from the previous response's pagination object. | 翻页游标，回传上一页响应 pagination 中的值。 |
| `resp.200.activities` |  | The list of matching activity records. | 匹配的活动记录列表。 |
| `resp.200.activities.token_id` |  | Outcome token ID involved in the activity. | 该活动涉及的结果 token ID。 |
| `resp.200.activities.side` |  | Type of activity: a token merge, split, or redeem. | 活动类型：token 的合并、拆分或赎回。 |
| `resp.200.activities.market_slug` |  | Slug of the market the activity relates to. | 活动关联市场的 slug。 |
| `resp.200.activities.condition_id` |  | On-chain condition ID of the related market. | 关联市场的链上 condition ID。 |
| `resp.200.activities.shares` | Raw number of shares (from the blockchain) | Raw share quantity as recorded on-chain (before normalization). | 链上记录的原始份额数量（未归一化）。 |
| `resp.200.activities.shares_normalized` | Number of shares normalized (raw divided by 1000000) | Share quantity normalized to whole-share units (raw value scaled down by 1,000,000). | 归一化后的份额数量（原始值除以 1,000,000）。 |
| `resp.200.activities.price` |  | Price associated with the activity.<br>[⚠️Note:源码未声明价格单位与取值范围，待研发确认。] | 与该活动关联的价格。<br>[⚠️批注:源码未声明价格单位与取值范围，待研发确认。] |
| `resp.200.activities.block_number` | Block number where the activity occurred | Block height at which the activity was recorded on-chain. | 活动上链所在的区块高度。 |
| `resp.200.activities.log_index` | Log index of the activity event in the block | Index of the activity's event log within its block. | 活动事件日志在区块内的索引。 |
| `resp.200.activities.tx_hash` |  | Hash of the transaction that recorded the activity. | 记录该活动的交易哈希。 |
| `resp.200.activities.title` |  | Title of the related market. | 关联市场的标题。 |
| `resp.200.activities.timestamp` | Unix timestamp in seconds when the activity occurred | When the activity occurred, as a Unix timestamp in seconds. | 活动发生时间，Unix 时间戳（秒）。 |
| `resp.200.activities.order_hash` |  | Hash of the associated order, if any. | 关联订单的哈希（若有）。 |
| `resp.200.activities.user` | User wallet address | Wallet address that performed the activity. | 执行该活动的钱包地址。 |
| `resp.200.pagination` |  | Pagination metadata for the result set. | 结果集的分页元信息。 |
| `resp.200.pagination.limit` |  | The page size applied to this response. | 本次响应采用的页大小。 |
| `resp.200.pagination.count` | Total number of activities matching the filters | Total number of activity records matching the filters. | 匹配筛选条件的活动记录总数。 |
| `resp.200.pagination.has_more` | Whether there are more activities available | Whether further pages are available. | 是否还有更多结果页。 |
| `resp.200.pagination.pagination_key` | Base64-encoded cursor for the next page. Only present when there are more results. | Cursor for the next page; present only when more results exist. | 下一页的游标；仅在还有更多结果时出现。 |
| `resp.400.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.400.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.500.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.500.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get_polymarket-market-price

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches the current market price for a market by `token_id`. When `at_time` is not provided, returns the most real-time price available. When `at_time` is provided, returns the historical market price at that specific timestamp.<br><br>**Example Request (with historical timestamp):**<br>```bash<br>curl 'https://api.aisa.one/apis/v1/polymarket/market-price/19701256321759583954581192053894521654935987478209343000964756587964612528044?at_time=1762164600'<br>```<br><br>**Example Request (real-time price):**<br>```bash<br>curl 'https://api.aisa.one/apis/v1/polymarket/market-price/19701256321759583954581192053894521654935987478209343000964756587964612528044'<br>``` | Get the current price of an outcome token by token_id; when at_time is supplied, returns the historical price at that timestamp instead of the latest. | 按 token_id 查询某结果 token 的当前价格；传入 at_time 时返回该时间点的历史价格，否则返回最新价格。 |
| `param:at_time` | Optional Unix timestamp (in seconds) to fetch a historical market price. If not provided, returns the most real-time price available. | Unix timestamp in seconds at which to read the historical price; omit to get the most real-time price. | 读取历史价格的时间点，Unix 时间戳（秒）；省略则返回最实时的价格。 |
| `resp.200.price` | The market price (between 0 and 1) | The market price of the outcome token, expressed as a probability between 0 and 1. | 该结果 token 的市场价格，以 0 到 1 之间的概率表示。 |
| `resp.200.at_time` | The timestamp for which the price was fetched (Unix timestamp in seconds) | The timestamp the returned price corresponds to, as a Unix timestamp in seconds. | 返回价格所对应的时间点，Unix 时间戳（秒）。 |
| `resp.400.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.400.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.404.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get_polymarket-positions

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches all Polymarket positions for a proxy wallet address. Returns positions with balance >= 10,000 shares (0.01 normalized) with market info. | List all Polymarket positions held by a proxy wallet, including per-position market info. Only positions with a balance of at least 10,000 raw shares (0.01 normalized) are returned, with cursor-based pagination. | 查询某代理钱包持有的全部 Polymarket 持仓，含每个持仓的市场信息。仅返回余额不低于 10,000 原始份额（归一化 0.01）的持仓，并支持游标分页。 |
| `param:limit` | Maximum number of positions to return per page. Defaults to 100, maximum 100. | Maximum number of positions to return per page. | 每页最多返回的持仓数量。 |
| `param:pagination_key` | Pagination key returned from previous request to fetch next page of results | Cursor returned by a previous request, used to fetch the next page. | 上一次请求返回的游标，用于获取下一页。 |
| `resp.200.wallet_address` | The wallet address (normalized to lowercase) | The queried wallet address, normalized to lowercase. | 被查询的钱包地址，已归一化为小写。 |
| `resp.200.positions` | Array of position objects | The wallet's position entries. | 该钱包的持仓条目。 |
| `resp.200.positions.wallet` | The wallet address | Wallet address holding the position. | 持有该持仓的钱包地址。 |
| `resp.200.positions.token_id` | The Polymarket token ID for this position | Outcome token ID held in this position. | 该持仓持有的结果 token ID。 |
| `resp.200.positions.condition_id` | The condition ID for the market | On-chain condition ID of the position's market. | 持仓所属市场的链上 condition ID。 |
| `resp.200.positions.title` | Market title | Title of the position's market. | 持仓所属市场的标题。 |
| `resp.200.positions.shares` | Number of shares (raw, not normalized) | Raw share quantity held (before normalization). | 持有的原始份额数量（未归一化）。 |
| `resp.200.positions.shares_normalized` | Number of shares normalized (divided by 1,000,000) | Share quantity normalized to whole-share units (raw value scaled down by 1,000,000). | 归一化后的份额数量（原始值除以 1,000,000）。 |
| `resp.200.positions.redeemable` | Whether this position can be redeemed (market completed and is closed) | Whether the position can be redeemed, which requires the market to be completed and closed. | 该持仓是否可赎回；需市场已完成并关闭。 |
| `resp.200.positions.market_slug` | The market slug | Slug of the position's market. | 持仓所属市场的 slug。 |
| `resp.200.positions.event_slug` | The event slug | Slug of the event the position's market belongs to. | 持仓所属市场归属事件的 slug。 |
| `resp.200.positions.image` | URL to market image | URL of the market's display image. | 市场展示图片的 URL。 |
| `resp.200.positions.label` | The outcome label for this token (e.g., 'Yes' or 'No') | Outcome label of the held token (e.g. Yes/No). | 所持 token 的结果标签（如 Yes/No）。 |
| `resp.200.positions.winning_outcome` | Information about the winning outcome if market is closed, null if market is still open or no outcome determined | Details of the winning outcome once the market is closed; null while open or undetermined. | 市场关闭后获胜结果的详情；仍开放或未定时为 null。 |
| `resp.200.positions.winning_outcome.id` | Token ID of the winning outcome | Token ID of the winning outcome. | 获胜结果的 token ID。 |
| `resp.200.positions.winning_outcome.label` | Label of the winning outcome | Label of the winning outcome. | 获胜结果的标签。 |
| `resp.200.positions.start_time` | Market start timestamp (Unix seconds) | Market start time, as a Unix timestamp in seconds. | 市场开始时间，Unix 时间戳（秒）。 |
| `resp.200.positions.end_time` | Market end timestamp (Unix seconds) | Market end time, as a Unix timestamp in seconds. | 市场结束时间，Unix 时间戳（秒）。 |
| `resp.200.positions.completed_time` | Market completion timestamp (Unix seconds), currently always null | Market completion time, as a Unix timestamp in seconds; null when not completed. | 市场完成时间，Unix 时间戳（秒）；未完成时为 null。 |
| `resp.200.positions.close_time` | Market close timestamp (Unix seconds) if market is closed, null if still open | Market close time, as a Unix timestamp in seconds; null while still open. | 市场关闭时间，Unix 时间戳（秒）；仍开放时为 null。 |
| `resp.200.positions.game_start_time` | Game start time for sports markets, null for non-sports markets | Game start time for sports markets; null for non-sports markets. | 体育类市场的赛事开始时间；非体育市场为 null。 |
| `resp.200.positions.market_status` | Whether the market is open or closed | Whether the position's market is open or closed. | 持仓所属市场为开放还是已关闭。 |
| `resp.200.positions.negativeRisk` | Whether this market has negative risk | Whether the position's market is part of a negative-risk group. | 持仓所属市场是否属于 negative-risk 组。 |
| `resp.200.pagination` | Pagination information | Pagination metadata for the positions. | 持仓结果的分页元信息。 |
| `resp.200.pagination.has_more` | Whether there are more results available | Whether more positions are available. | 是否还有更多持仓可取。 |
| `resp.200.pagination.limit` | The limit used for this request | The page size applied to this request. | 本次请求采用的页大小。 |
| `resp.200.pagination.pagination_key` | Pagination key to use for fetching next page, null if no more pages | Cursor to fetch the next page; null when there are no more pages. | 获取下一页的游标；无更多页时为 null。 |
| `resp.400.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.400.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get_polymarket-wallet

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches wallet information by providing either an EOA (Externally Owned Account) address, a proxy wallet address, or a user handle. Returns the associated EOA, proxy, wallet type, handle, pseudonym, and profile image. Optionally returns trading metrics when `with_metrics=true`. | Look up wallet information by EOA address, proxy address, or user handle, returning the associated EOA, proxy, wallet type, handle, pseudonym, and profile image. Trading metrics are included only when with_metrics=true. | 按 EOA 地址、代理地址或用户 handle 查询钱包信息，返回关联的 EOA、代理、钱包类型、handle、化名与头像。仅当 with_metrics=true 时附带交易指标。 |
| `param:eoa` | EOA (Externally Owned Account) wallet address. Either `eoa`, `proxy`, or `handle` must be provided, but not more than one. | Externally owned account address to look up. Provide exactly one of eoa, proxy, or handle. | 待查询的外部账户（EOA）地址。eoa、proxy、handle 三者须且仅须提供其一。 |
| `param:proxy` | Proxy wallet address. Either `eoa`, `proxy`, or `handle` must be provided, but not more than one. | Proxy wallet address to look up. Provide exactly one of eoa, proxy, or handle. | 待查询的代理钱包地址。eoa、proxy、handle 三者须且仅须提供其一。 |
| `param:handle` | User handle/username. Accepts both formats: `username` or `@username` (the @ prefix will be automatically stripped). Either `eoa`, `proxy`, or `handle` must be provided, but not more than one. | User handle to look up; an optional leading @ is stripped automatically. Provide exactly one of eoa, proxy, or handle. | 待查询的用户 handle，开头的 @ 会被自动去除。eoa、proxy、handle 三者须且仅须提供其一。 |
| `param:with_metrics` | Whether to include wallet trading metrics (total volume, trades, and markets). Pass `true` to include metrics. Metrics are computed only when explicitly requested for performance reasons. | Pass true to also compute and return trading metrics; they are calculated only on demand for performance. | 传 true 时额外计算并返回交易指标；出于性能考虑仅按需计算。 |
| `param:start_time` | Optional start date for metrics calculation (Unix timestamp in seconds). Only used when `with_metrics=true`. | Start of the window for metric calculation, as a Unix timestamp in seconds; only used when with_metrics=true. | 指标计算窗口的起点，Unix 时间戳（秒）；仅在 with_metrics=true 时生效。 |
| `param:end_time` | Optional end date for metrics calculation (Unix timestamp in seconds). Only used when `with_metrics=true`. | End of the window for metric calculation, as a Unix timestamp in seconds; only used when with_metrics=true. | 指标计算窗口的终点，Unix 时间戳（秒）；仅在 with_metrics=true 时生效。 |
| `resp.200.eoa` | The EOA (Externally Owned Account) wallet address | The resolved externally owned account address. | 解析得到的外部账户（EOA）地址。 |
| `resp.200.proxy` | The proxy wallet address | The resolved proxy wallet address. | 解析得到的代理钱包地址。 |
| `resp.200.wallet_type` | The type of wallet | The wallet implementation type. | 钱包的实现类型。 |
| `resp.200.handle` | User handle/username | The user's handle; null when none is set. | 用户 handle；未设置时为 null。 |
| `resp.200.pseudonym` | User pseudonym/display name | The user's display pseudonym; null when none is set. | 用户的展示化名；未设置时为 null。 |
| `resp.200.image` | User profile image URL | URL of the user's profile image; null when none is set. | 用户头像的 URL；未设置时为 null。 |
| `resp.200.wallet_metrics` | Trading metrics for this wallet (only present when with_metrics=true) | Trading metrics for the wallet; present only when with_metrics=true. | 钱包的交易指标；仅在 with_metrics=true 时出现。 |
| `resp.200.wallet_metrics.total_volume` | Total trading volume in USD | Total trading volume of the wallet, in USD. | 钱包的总交易额（美元）。 |
| `resp.200.wallet_metrics.total_trades` | Total number of trades (orders where this wallet was the maker) | Total number of trades where this wallet was the maker. | 该钱包作为 maker 的总成交笔数。 |
| `resp.200.wallet_metrics.total_markets` | Total number of unique markets traded in | Number of distinct markets the wallet has traded in. | 钱包参与交易的不同市场数量。 |
| `resp.200.wallet_metrics.highest_volume_day` | The day with the highest number of shares traded | The single day with the highest traded share volume. | 成交份额最高的单日。 |
| `resp.200.wallet_metrics.highest_volume_day.date` | Date in YYYY-MM-DD format | Calendar date of the highest-volume day. | 成交量最高那一天的日期。 |
| `resp.200.wallet_metrics.highest_volume_day.volume` | Total shares traded on that day (normalized, divided by 1,000,000) | Shares traded that day, normalized (raw value scaled down by 1,000,000). | 当日成交份额，归一化值（原始值除以 1,000,000）。 |
| `resp.200.wallet_metrics.highest_volume_day.trades` | Number of trades executed on that day | Number of trades executed that day. | 当日执行的成交笔数。 |
| `resp.200.wallet_metrics.merges` | Total number of token merges performed by this wallet | Total token merges performed by the wallet. | 钱包执行的 token 合并总次数。 |
| `resp.200.wallet_metrics.splits` | Total number of token splits performed by this wallet | Total token splits performed by the wallet. | 钱包执行的 token 拆分总次数。 |
| `resp.200.wallet_metrics.conversions` | Total number of token conversions performed by this wallet | Total token conversions performed by the wallet. | 钱包执行的 token 转换总次数。 |
| `resp.200.wallet_metrics.redemptions` | Total number of token redemptions performed by this wallet | Total token redemptions performed by the wallet. | 钱包执行的 token 赎回总次数。 |
| `resp.400.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.400.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.404.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get_polymarket-candlesticks

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches historical candlestick data for a market identified by `condition_id`, over a specified interval. | Fetch historical candlestick (OHLC) data for a market identified by condition_id over a time range, at a 1-minute, 1-hour, or 1-day interval. Each interval enforces a maximum lookback range. | 按 condition_id 查询某市场在指定时间范围内的历史 K 线（OHLC）数据，可选 1 分钟、1 小时或 1 天的时间粒度。不同粒度有各自的最大回溯范围限制。 |
| `param:condition_id` | Polymarket condition ID for the market. | On-chain condition ID identifying the market to fetch candlesticks for. | 待查询 K 线的市场链上 condition ID。 |
| `param:start_time` | Unix timestamp (in seconds) for start of time range | Start of the time range, as a Unix timestamp in seconds. | 时间范围起点，Unix 时间戳（秒）。 |
| `param:end_time` | Unix timestamp (in seconds) for end of time range | End of the time range, as a Unix timestamp in seconds. | 时间范围终点，Unix 时间戳（秒）。 |
| `param:interval` | Interval length: 1 = 1m, 60 = 1h, 1440 = 1d. Defaults to 1m. <br><br>⚠️ **Note:** There are range limits for `interval` — specifically:<br>- `1` (1m): max range **1 week**<br>- `60` (1h): max range **1 month**<br>- `1440` (1d): max range **1 year**<br><br> | Candle granularity in minutes (1 = 1m, 60 = 1h, 1440 = 1d); each granularity caps the allowed range (1m up to 1 week, 1h up to 1 month, 1d up to 1 year). | K 线粒度（按分钟：1 = 1 分钟，60 = 1 小时，1440 = 1 天）；各粒度有最大范围限制（1 分钟至多 1 周，1 小时至多 1 个月，1 天至多 1 年）。 |
| `resp.200.candlesticks` | Array of market candlestick data, where each element is a tuple containing candlestick data array and token metadata | Per-outcome candlestick series; each element pairs a candlestick data array with that token's metadata (token_id and outcome label). | 按结果划分的 K 线序列；每个元素由一段 K 线数据数组与该 token 的元数据（token_id 与结果标签）配对组成。 |
| `resp.400.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.400.required` |  | Names of the required parameters that were missing from the request. | 请求中缺失的必填参数名称。 |

## get_polymarket-wallet-pnl

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches the REALIZED profit and loss (PnL) for a specific wallet address over a specified time range and granularity. **Note:** This will differ to what you see on Polymarket's dashboard since Polymarket showcases historical unrealized PnL. This API tracks realized gains only - from either confirmed sells or redeems. We do not realize a gain/loss until a finished market is redeemed. | Return a wallet's REALIZED profit and loss over a time range at a chosen granularity. Only realized gains from confirmed sells or redeems are counted, so values differ from Polymarket's dashboard, which shows unrealized PnL. | 按选定粒度返回某钱包在指定时间范围内的「已实现」盈亏。仅计入确认卖出或赎回带来的已实现收益，因此与展示未实现盈亏的 Polymarket 看板数值不同。 |
| `param:wallet_address` | Polymarket wallet address (0x-prefixed). | The 0x-prefixed wallet address to compute PnL for. | 待计算盈亏的 0x 前缀钱包地址。 |
| `param:granularity` |  | Time bucket size for the PnL series (day, week, month, year, or the whole period). | 盈亏序列的时间分桶粒度（日、周、月、年或全部时段）。 |
| `param:start_time` | Defaults to first day of first trade if not provided. | Start of the range, as a Unix timestamp in seconds; defaults to the day of the wallet's first trade when omitted. | 范围起点，Unix 时间戳（秒）；省略时默认取该钱包首笔交易当日。 |
| `param:end_time` | Defaults to the current date if not provided. | End of the range, as a Unix timestamp in seconds; defaults to the current date when omitted. | 范围终点，Unix 时间戳（秒）；省略时默认取当前日期。 |
| `resp.200.granularity` |  | The time bucket size applied to the returned series. | 返回序列采用的时间分桶粒度。 |
| `resp.200.start_time` |  | Start of the computed range, as a Unix timestamp in seconds. | 实际计算范围的起点，Unix 时间戳（秒）。 |
| `resp.200.end_time` |  | End of the computed range, as a Unix timestamp in seconds. | 实际计算范围的终点，Unix 时间戳（秒）。 |
| `resp.200.wallet_address` |  | The wallet address the PnL was computed for. | 计算盈亏所针对的钱包地址。 |
| `resp.200.pnl_over_time` |  | Realized PnL series, one point per time bucket. | 已实现盈亏序列，每个时间分桶一个数据点。 |
| `resp.200.pnl_over_time.timestamp` |  | Start of the time bucket, as a Unix timestamp in seconds. | 该时间分桶的起点，Unix 时间戳（秒）。 |
| `resp.200.pnl_over_time.pnl_to_date` |  | Cumulative realized PnL up to this bucket.<br>[⚠️Note:源码未声明盈亏金额的货币单位，待研发确认。] | 截至该分桶的累计已实现盈亏。<br>[⚠️批注:源码未声明盈亏金额的货币单位，待研发确认。] |
| `resp.400.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.400.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.503.error` |  | Short error code identifying the failure category. | 标识失败类别的简短错误码。 |
| `resp.503.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

