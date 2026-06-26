# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 4 个接口，79 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## get_kalshi-markets

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches Kalshi market data with optional filtering by market ticker, event ticker, status, and volume. Returns markets with details including pricing, volume, and status information. | List Kalshi prediction markets with their pricing, volume and status, optionally filtered by market ticker, event ticker, keyword search, status or minimum volume. Results are cursor-paginated. | 列出 Kalshi 预测市场及其价格、成交量与状态，可按 market ticker、event ticker、关键词、状态或最小成交量筛选。结果采用游标分页。 |
| `param:market_ticker` | Filter markets by market ticker(s). Can provide multiple values. | Restrict results to one or more specific Kalshi markets by their market ticker. | 按一个或多个 Kalshi 市场的 market ticker 限定返回结果。 |
| `param:event_ticker` | Filter markets by event ticker(s). Can provide multiple values. | Restrict results to markets belonging to one or more events, identified by event ticker. | 按一个或多个 event ticker 限定返回属于这些事件的市场。 |
| `param:search` | Search markets by keywords in title and description. Must be URL encoded (e.g., 'bitcoin%20price' for 'bitcoin price'). | Keyword query matched against market title and description; the value must be URL-encoded. | 针对市场标题与描述的关键词检索，取值需经 URL 编码。 |
| `param:status` | Filter markets by status (whether they're open or closed) | Filter by trading state: `open` markets still accept trades, `closed` markets no longer do. | 按交易状态筛选：`open` 表示仍可交易，`closed` 表示已停止交易。 |
| `param:min_volume` | Filter markets with total trading volume greater than or equal to this amount (in dollars) | Keep only markets whose total trading volume is at least this amount, in dollars. | 仅保留总成交量不低于该金额的市场，单位为美元。 |
| `param:limit` | Number of markets to return (1-100). Default: 10. | Number of markets to return per page. | 每页返回的市场数量。 |
| `param:pagination_key` | Base64-encoded cursor for efficient pagination. Returned in the previous response's pagination object. | Opaque cursor for fetching the next page; take it from the pagination object of the previous response. | 用于翻到下一页的不透明游标，取自上一次响应的 pagination 对象。 |
| `resp.200.markets` |  | List of matching Kalshi markets. | 匹配的 Kalshi 市场列表。 |
| `resp.200.markets.event_ticker` | The Kalshi event ticker | Ticker of the event this market belongs to. | 该市场所属事件的 ticker。 |
| `resp.200.markets.market_ticker` | The Kalshi market ticker | Ticker uniquely identifying this market; use it to query price, trades or order book. | 唯一标识该市场的 ticker，可用于查询价格、成交记录或订单簿。 |
| `resp.200.markets.title` | Market question/title | Human-readable question the market resolves. | 市场所裁决问题的可读标题。 |
| `resp.200.markets.start_time` | Unix timestamp in seconds when the market opens | When trading on the market opens. | 市场开放交易的时间。 |
| `resp.200.markets.end_time` | Unix timestamp in seconds when the market is scheduled to end | Scheduled time at which the market is expected to end. | 市场预计结束的计划时间。 |
| `resp.200.markets.close_time` | Unix timestamp in seconds when the market actually resolves/closes (may be before end_time if market finishes early, null if not yet closed) | When the market actually resolved and closed; may precede end_time if it finished early, and is null while still open. | 市场实际裁决并关闭的时间；若提前结束可能早于 end_time，仍开放时为 null。 |
| `resp.200.markets.status` | Market status | Current trading state: `open` still accepts trades, `closed` no longer does. | 当前交易状态：`open` 仍可交易，`closed` 已停止交易。 |
| `resp.200.markets.last_price` | Last traded price in cents | Price of the most recent trade. | 最近一笔成交的价格。 |
| `resp.200.markets.volume` | Total trading volume in dollars | Cumulative trading volume since the market opened. | 自市场开放以来的累计成交量。 |
| `resp.200.markets.volume_24h` | 24-hour trading volume in dollars | Trading volume over the trailing 24 hours. | 过去 24 小时的成交量。 |
| `resp.200.markets.result` | Market result (null if unresolved) | Final outcome of the market once resolved; null while unresolved.<br>[⚠️Note:已裁决时 result 的具体取值集合源码未说明，待研发确认。] | 市场裁决后的最终结果；未裁决时为 null。<br>[⚠️批注:已裁决时 result 的具体取值集合源码未说明，待研发确认。] |
| `resp.200.pagination` |  | Pagination metadata for the result set. | 结果集的分页元信息。 |
| `resp.200.pagination.limit` |  | Page size that was applied to this response. | 本次响应实际采用的每页数量。 |
| `resp.200.pagination.total` | Total number of markets matching the filters | Total number of markets matching the filters across all pages. | 在所有分页中匹配筛选条件的市场总数。 |
| `resp.200.pagination.has_more` | Whether there are more markets available | Whether further pages of results remain. | 是否还有更多分页结果。 |
| `resp.200.pagination.pagination_key` | Base64-encoded cursor for the next page. Only present when there are more results. | Cursor to pass as pagination_key on the next request; present only when more results remain. | 下次请求作为 pagination_key 传入的游标，仅在还有更多结果时出现。 |
| `resp.400.error` |  | Short machine-readable error code for the failed request. | 请求失败时的简短机器可读错误码。 |
| `resp.400.message` |  | Human-readable explanation of why the request was rejected. | 对请求被拒原因的可读说明。 |

## get_kalshi-trades

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches historical trade data for Kalshi markets with optional filtering by ticker and time range. Returns executed trades with pricing, volume, and taker side information. All timestamps are in seconds. | List historical executed trades for Kalshi markets, optionally filtered by market ticker and a time window, returning per-trade price, contract count and taker side. Results are cursor-paginated. | 列出 Kalshi 市场的历史成交记录，可按 market ticker 与时间区间筛选，返回每笔成交的价格、合约数量与吃单方向。结果采用游标分页。 |
| `param:ticker` | The Kalshi market ticker to filter trades | Restrict trades to a single Kalshi market by its ticker. | 按 market ticker 将成交记录限定到单个 Kalshi 市场。 |
| `param:start_time` | Start time in Unix timestamp (seconds) | Lower bound of the trade time window; only trades at or after this moment are returned. | 成交时间窗的下界，仅返回该时刻及之后的成交。 |
| `param:end_time` | End time in Unix timestamp (seconds) | Upper bound of the trade time window; only trades at or before this moment are returned. | 成交时间窗的上界，仅返回该时刻及之前的成交。 |
| `param:limit` | Maximum number of trades to return (default: 100) | Maximum number of trades to return per page. | 每页返回的成交记录数量上限。 |
| `param:pagination_key` | Base64-encoded cursor for efficient pagination. Returned in the previous response's pagination object. | Opaque cursor for fetching the next page; take it from the pagination object of the previous response. | 用于翻到下一页的不透明游标，取自上一次响应的 pagination 对象。 |
| `resp.200.trades` | Array of executed trades | List of executed trades matching the filters. | 匹配筛选条件的成交记录列表。 |
| `resp.200.trades.trade_id` | Unique identifier for the trade | Identifier uniquely referencing this individual trade. | 唯一引用该笔成交的标识。 |
| `resp.200.trades.market_ticker` | The Kalshi market ticker | Ticker of the market on which the trade executed. | 该笔成交所属市场的 ticker。 |
| `resp.200.trades.count` | Number of contracts traded | Number of contracts exchanged in this trade. | 该笔成交中交换的合约数量。 |
| `resp.200.trades.yes_price` | Yes side price in cents | Execution price of the yes side, expressed in cents. | yes 一侧的成交价格，以分计。 |
| `resp.200.trades.no_price` | No side price in cents | Execution price of the no side, expressed in cents. | no 一侧的成交价格，以分计。 |
| `resp.200.trades.yes_price_dollars` | Yes side price in dollars | Execution price of the yes side, expressed in dollars. | yes 一侧的成交价格，以美元计。 |
| `resp.200.trades.no_price_dollars` | No side price in dollars | Execution price of the no side, expressed in dollars. | no 一侧的成交价格，以美元计。 |
| `resp.200.trades.taker_side` | Which side was the taker (yes or no) | Which side initiated the trade by crossing the spread: `yes` or `no`. | 主动吃单成交的一方：`yes` 或 `no`。 |
| `resp.200.trades.created_time` | Timestamp of the trade in seconds (Unix timestamp) | Moment at which the trade was executed. | 该笔成交发生的时间。 |
| `resp.200.pagination` |  | Pagination metadata for the result set. | 结果集的分页元信息。 |
| `resp.200.pagination.limit` |  | Page size that was applied to this response. | 本次响应实际采用的每页数量。 |
| `resp.200.pagination.total` | Total number of trades matching the filters | Total number of trades matching the filters across all pages. | 在所有分页中匹配筛选条件的成交总数。 |
| `resp.200.pagination.has_more` | Whether there are more trades available | Whether further pages of results remain. | 是否还有更多分页结果。 |
| `resp.200.pagination.pagination_key` | Base64-encoded cursor for the next page. Only present when there are more results. | Cursor to pass as pagination_key on the next request; present only when more results remain. | 下次请求作为 pagination_key 传入的游标，仅在还有更多结果时出现。 |
| `resp.400.error` |  | Short machine-readable error code for the failed request. | 请求失败时的简短机器可读错误码。 |
| `resp.400.message` |  | Human-readable explanation of why the request was rejected. | 对请求被拒原因的可读说明。 |

## get_kalshi-market-price

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches the current market price for a Kalshi market by `market_ticker`. When `at_time` is not provided, returns the most real-time price available. When `at_time` is provided, returns the historical market price at that specific timestamp. Returns prices for both yes and no sides.<br><br>**Example Request (with historical timestamp):**<br>```bash<br>curl 'https://api.domeapi.io/v1/kalshi/market-price/KXNFLGAME-25AUG16ARIDEN-ARI?at_time=1762164600' \<br>  -H 'Authorization: Bearer YOUR_TOKEN'<br>```<br><br>**Example Request (real-time price):**<br>```bash<br>curl 'https://api.domeapi.io/v1/kalshi/market-price/KXNFLGAME-25AUG16ARIDEN-ARI' \<br>  -H 'Authorization: Bearer YOUR_TOKEN'<br>``` | Get the price of a single Kalshi market identified by its market ticker, for both the yes and no sides. Returns the latest available price by default, or the historical price at a given timestamp when at_time is supplied. | 查询由 market ticker 指定的单个 Kalshi 市场价格，包含 yes 与 no 两侧。默认返回最新可得价格；传入 at_time 时返回该时间点的历史价格。 |
| `param:at_time` | Optional Unix timestamp (in seconds) to fetch a historical market price. If not provided, returns the most real-time price available. | Fetch the historical price as of this moment; omit to get the latest available price. | 查询截至该时刻的历史价格；省略则返回最新可得价格。 |
| `resp.200.yes` | Yes side price information | Price information for the yes side of the market. | 市场 yes 一侧的价格信息。 |
| `resp.200.yes.price` | The yes side price in dollars (between 0 and 1) | Yes-side price, expressed in dollars as a probability-like value between 0 and 1. | yes 一侧价格，以美元计，取值介于 0 与 1 之间，类似概率。 |
| `resp.200.yes.at_time` | The timestamp for which the price was fetched (Unix timestamp in seconds) | Moment the returned yes-side price corresponds to. | 所返回 yes 一侧价格对应的时间点。 |
| `resp.200.no` | No side price information | Price information for the no side of the market. | 市场 no 一侧的价格信息。 |
| `resp.200.no.price` | The no side price in dollars (between 0 and 1) | No-side price, expressed in dollars as a probability-like value between 0 and 1. | no 一侧价格，以美元计，取值介于 0 与 1 之间，类似概率。 |
| `resp.200.no.at_time` | The timestamp for which the price was fetched (Unix timestamp in seconds) | Moment the returned no-side price corresponds to. | 所返回 no 一侧价格对应的时间点。 |
| `resp.400.error` |  | Short machine-readable error code for the failed request. | 请求失败时的简短机器可读错误码。 |
| `resp.400.message` |  | Human-readable explanation of why the request was rejected. | 对请求被拒原因的可读说明。 |
| `resp.404.error` |  | Short machine-readable error code indicating the market was not found. | 表示未找到该市场的简短机器可读错误码。 |
| `resp.404.message` |  | Human-readable explanation that no price data exists for the requested market. | 对所请求市场不存在价格数据的可读说明。 |

## get_kalshi-orderbooks

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Fetches historical orderbook snapshots for a specific Kalshi market (ticker) over a specified time range. If no start_time and end_time are provided, returns the latest orderbook snapshot for the market. Returns snapshots of the order book including yes/no bids and asks with prices in both cents and dollars. All timestamps are in milliseconds. Orderbook data has history starting from October 29th, 2025. Note: When fetching the latest orderbook (without start/end times), the limit parameter is ignored. | Get historical order book snapshots for a single Kalshi market over a time window, returning yes/no bid levels in both cents and dollars. When no time window is given, returns only the latest snapshot. Results are cursor-paginated. | 查询单个 Kalshi 市场在某时间区间内的历史订单簿快照，返回 yes/no 两侧的报价档位（同时给出以分和以美元计的价格）。未指定时间区间时仅返回最新一条快照。结果采用游标分页。 |
| `param:ticker` | The Kalshi market ticker | Kalshi market ticker whose order book history is requested. | 要查询订单簿历史的 Kalshi 市场 ticker。 |
| `param:start_time` | Start time in Unix timestamp (milliseconds). Optional - if not provided along with end_time, returns the latest orderbook snapshot. | Lower bound of the snapshot time window; omit together with end_time to get only the latest snapshot. | 快照时间窗的下界；与 end_time 一并省略则只返回最新一条快照。 |
| `param:end_time` | End time in Unix timestamp (milliseconds). Optional - if not provided along with start_time, returns the latest orderbook snapshot. | Upper bound of the snapshot time window; omit together with start_time to get only the latest snapshot. | 快照时间窗的上界；与 start_time 一并省略则只返回最新一条快照。 |
| `param:limit` | Maximum number of snapshots to return (default: 100, max: 200). Ignored when fetching the latest orderbook without start_time and end_time. | Maximum number of snapshots to return per page; ignored when fetching only the latest snapshot. | 每页返回的快照数量上限；仅取最新快照时该参数被忽略。 |
| `param:paginationKey` | Base64-encoded cursor for efficient pagination. Returned in the previous response's pagination object. | Opaque cursor for fetching the next page; take it from the pagination object of the previous response. | 用于翻到下一页的不透明游标，取自上一次响应的 pagination 对象。 |
| `resp.200.snapshots` | Array of orderbook snapshots at different points in time | Order book snapshots ordered through the requested time window. | 在所请求时间窗内排列的订单簿快照。 |
| `resp.200.snapshots.orderbook` |  | The bid levels of the order book at this snapshot, split by side and price unit. | 该快照时刻订单簿的报价档位，按方向与价格单位拆分。 |
| `resp.200.snapshots.orderbook.yes` | Yes side orders with prices in cents | Resting yes-side orders, each as a [price, contract count] pair with price in cents. | yes 一侧的挂单，每项为 [价格, 合约数量] 对，价格以分计。 |
| `resp.200.snapshots.orderbook.no` | No side orders with prices in cents | Resting no-side orders, each as a [price, contract count] pair with price in cents. | no 一侧的挂单，每项为 [价格, 合约数量] 对，价格以分计。 |
| `resp.200.snapshots.orderbook.yes_dollars` | Yes side orders with prices in dollars | Resting yes-side orders, each as a [price, contract count] pair with price in dollars. | yes 一侧的挂单，每项为 [价格, 合约数量] 对，价格以美元计。 |
| `resp.200.snapshots.orderbook.no_dollars` | No side orders with prices in dollars | Resting no-side orders, each as a [price, contract count] pair with price in dollars. | no 一侧的挂单，每项为 [价格, 合约数量] 对，价格以美元计。 |
| `resp.200.snapshots.timestamp` | Timestamp of the snapshot in milliseconds | Moment this order book snapshot was captured. | 该订单簿快照的采集时间。 |
| `resp.200.snapshots.ticker` | The Kalshi market ticker | Ticker of the market this snapshot belongs to. | 该快照所属市场的 ticker。 |
| `resp.200.pagination` |  | Pagination metadata for the result set. | 结果集的分页元信息。 |
| `resp.200.pagination.limit` |  | Page size that was applied to this response. | 本次响应实际采用的每页数量。 |
| `resp.200.pagination.count` | Number of snapshots returned | Number of snapshots returned in this page. | 本页返回的快照数量。 |
| `resp.200.pagination.paginationKey` | Base64-encoded cursor for fetching the next page of results. Only present when has_more is true. | Cursor to pass as paginationKey on the next request; present only when more results remain. | 下次请求作为 paginationKey 传入的游标，仅在还有更多结果时出现。 |
| `resp.200.pagination.has_more` | Whether there are more snapshots available | Whether further pages of snapshots remain. | 是否还有更多分页快照。 |
| `resp.400.error` |  | Short machine-readable error code for the failed request. | 请求失败时的简短机器可读错误码。 |
| `resp.400.message` |  | Human-readable explanation of why the request was rejected. | 对请求被拒原因的可读说明。 |

