# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 2 个接口，13 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## get_matching-markets-sports

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Find equivalent markets across different prediction market platforms (Polymarket, Kalshi, etc.) for sports events. Provide either one or more Polymarket market slugs or Kalshi event tickers. | Match equivalent prediction markets for the same sports events across platforms such as Polymarket and Kalshi. Seed the lookup with one or more Polymarket market slugs or Kalshi event tickers — the two seed types are mutually exclusive. Typical uses are cross-platform price comparison and arbitrage discovery. | 为同一批体育赛事在 Polymarket、Kalshi 等平台间匹配等价的预测市场。用一个或多个 Polymarket market slug 或 Kalshi event ticker 作为查询种子 —— 两类种子互斥。典型场景为跨平台比价与套利发现。 |
| `param:polymarket_market_slug` | The Polymarket market slug(s) to find matching markets for. To get multiple markets at once, provide the query param multiple times with different slugs. Can not be combined with kalshi_event_ticker. | One or more Polymarket market slugs to find cross-platform equivalents for. Repeat the query parameter to pass several at once. Cannot be combined with `kalshi_event_ticker` — choose one seed type per request. | 一个或多个用于查找跨平台等价市场的 Polymarket market slug。重复该查询参数即可一次传入多个。不能与 `kalshi_event_ticker` 同时使用 —— 每次请求只选一种种子。 |
| `param:kalshi_event_ticker` | The Kalshi event ticker(s) to find matching markets for. To get multiple markets at once, provide the query param multiple times with different tickers. Can not be combined with polymarket_market_slug. | One or more Kalshi event tickers to find cross-platform equivalents for. Repeat the query parameter to pass several at once. Cannot be combined with `polymarket_market_slug` — choose one seed type per request. | 一个或多个用于查找跨平台等价市场的 Kalshi event ticker。重复该查询参数即可一次传入多个。不能与 `polymarket_market_slug` 同时使用 —— 每次请求只选一种种子。 |
| `resp.200.markets` |  | Matched markets grouped by your seed: each key is the slug or ticker you supplied, and its value is the list of equivalent markets found across platforms. Each entry carries a `platform` discriminator (`KALSHI` or `POLYMARKET`) and that platform's native identifiers. | 按种子分组的匹配结果:每个键是你传入的 slug 或 ticker,其值是各平台上找到的等价市场列表。每条记录带有 `platform` 判别字段(`KALSHI` 或 `POLYMARKET`)及该平台的原生标识。 |
| `resp.400.error` |  | Short machine-readable error label for a bad request, e.g. missing required parameters. | 请求无效时的简短机器可读错误标签,例如缺少必填参数。 |
| `resp.400.message` |  | Human-readable detail explaining what was wrong with the request. | 对请求错误原因的可读详细说明。 |
| `resp.404.error` |  | Short machine-readable error label indicating no matching markets were found. | 表示未匹配到市场的简短机器可读错误标签。 |
| `resp.404.message` |  | Human-readable detail explaining that no equivalent markets matched the supplied seeds. | 对未匹配到等价市场的可读详细说明。 |

## get_matching-markets-sports-by-sport

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Find equivalent markets across different prediction market platforms (Polymarket, Kalshi, etc.) for sports events by sport and date. | Match equivalent prediction markets across platforms for a given sport on a given date, instead of seeding by specific market identifiers. Pick the sport from the path and the day from the query. Typical use is sweeping a whole day's slate for cross-platform equivalents. | 针对某项运动在某一天的赛事,跨平台匹配等价的预测市场,而非以具体市场标识作为种子。运动取自路径,日期取自查询参数。典型场景为扫描某日全部赛程以寻找跨平台等价市场。 |
| `param:date` | The date to find matching markets for in YYYY-MM-DD format | The day to search, in `YYYY-MM-DD`. Only events scheduled on this date are matched. | 要检索的日期,格式 `YYYY-MM-DD`。仅匹配当天进行的赛事。 |
| `resp.200.markets` |  | Matched markets grouped by event: each key is an event identifier and its value is the list of equivalent markets found across platforms. Each entry carries a `platform` discriminator (`KALSHI` or `POLYMARKET`) and that platform's native identifiers. | 按赛事分组的匹配结果:每个键是一个赛事标识,其值是各平台上找到的等价市场列表。每条记录带有 `platform` 判别字段(`KALSHI` 或 `POLYMARKET`)及该平台的原生标识。 |
| `resp.200.sport` |  | Echoes the sport code that was searched. | 回显本次检索的运动代码。 |
| `resp.200.date` |  | Echoes the date that was searched, in `YYYY-MM-DD`. | 回显本次检索的日期,格式 `YYYY-MM-DD`。 |
| `resp.400.error` |  | Short machine-readable error label for a bad request, e.g. a missing required parameter. | 请求无效时的简短机器可读错误标签,例如缺少必填参数。 |
| `resp.400.message` |  | Human-readable detail explaining what was wrong with the request, such as a missing `date`. | 对请求错误原因的可读详细说明,例如缺少 `date`。 |

