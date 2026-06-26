# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 21 个接口，260 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## coingeckoCoinsList

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List all coins with id, symbol, and name. Use to map symbols to CoinGecko IDs. | List every coin tracked by CoinGecko with its ID, symbol and name, optionally including the platforms and contract addresses it is deployed on. Use it to map a ticker symbol to the CoinGecko coin ID that the other endpoints require. | 列出 CoinGecko 收录的全部币种及其 ID、symbol 与名称，可选附带其所在平台与合约地址。常用于把交易符号映射为其他接口所需的 CoinGecko 币种 ID。 |
| `param:include_platform` | Include platform + contract addresses. | When enabled, each coin also lists the asset platforms it lives on and the corresponding contract addresses. | 开启后，每个币种额外列出其所在的资产平台及对应合约地址。 |

## coingeckoSupportedVsCurrencies

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List of all supported fiat and crypto currencies for `vs_currency` parameters. | List all fiat and crypto currencies that can be passed as the target currency in vs_currency / vs_currencies parameters. | 列出所有可作为 vs_currency / vs_currencies 计价目标传入的法币与加密货币。 |

## coingeckoCoinsMarkets

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List all coins with market data: price, market cap, volume, and other metrics. | List coins together with their market data (price, market cap, volume and related metrics) in a chosen currency, with sorting, paging, optional sparkline and price-change windows. Narrow the list by specific coin IDs or a category. | 以指定计价货币列出币种及其行情数据（价格、市值、成交量等指标），支持排序、分页、可选迷你走势图与多档涨跌幅窗口。可按指定币种 ID 或分类缩小范围。 |
| `param:ids` | Comma-separated CoinGecko coin IDs. | Restrict the list to these CoinGecko coin IDs, given as a comma-separated string. | 将列表限定为这些 CoinGecko 币种 ID，以逗号分隔的字符串给出。 |
| `param:category` | Filter by category (see `/coins/categories/list`). | Restrict the list to coins in this category; category identifiers come from coingeckoCategoriesList. | 将列表限定为该分类下的币种；分类标识取自 coingeckoCategoriesList。 |
| `param:order` |  | Sort order of the returned coins, by market cap, volume or ID, ascending or descending. | 返回币种的排序方式，可按市值、成交量或 ID 升序或降序。 |
| `param:per_page` |  | Number of coins returned per page. | 每页返回的币种数量。 |
| `param:page` |  | Which page of results to return. | 返回结果的页码。 |
| `param:sparkline` |  | When enabled, include a 7-day price sparkline for each coin. | 开启后，为每个币种附带 7 天价格迷你走势图。 |
| `param:price_change_percentage` | Comma-separated windows: `1h,24h,7d,14d,30d,200d,1y`. | Comma-separated list of time windows for which to include price-change percentages. | 以逗号分隔的时间窗列表，指定需要附带涨跌幅百分比的窗口。 |

## coingeckoCoinById

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Current data (price, markets, links, community, developer data) for a coin. | Get the full profile of a single coin: price and market data, links, images, community and developer metrics. Toggle the heavier sections (tickers, market data, community, developer, localization, sparkline) on or off to control payload size. | 获取单个币种的完整资料：价格与行情、链接、图标、社区与开发者指标。可分别开关各较重的数据块（行情、社区、开发者、本地化、迷你走势图等）以控制返回体积。 |
| `param:localization` |  | When enabled, include localized (translated) name and description fields. | 开启后，包含本地化（翻译后）的名称与描述字段。 |
| `param:tickers` |  | When enabled, include the coin's exchange trading pairs in the response. | 开启后，在响应中包含该币种的交易所交易对。 |
| `param:market_data` |  | When enabled, include price and market data in the response. | 开启后，在响应中包含价格与行情数据。 |
| `param:community_data` |  | When enabled, include community metrics such as social followers and activity. | 开启后，包含社交关注与活跃度等社区指标。 |
| `param:developer_data` |  | When enabled, include developer metrics derived from the coin's code repositories. | 开启后，包含基于该币种代码仓库的开发者指标。 |
| `param:sparkline` |  | When enabled, include a 7-day price sparkline. | 开启后，附带 7 天价格迷你走势图。 |

## coingeckoSimplePrice

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Current price for any cryptocurrencies in any supported currencies. | Get the current price of one or more coins quoted in one or more currencies, with optional market cap, 24-hour volume, 24-hour change and last-updated timestamp. | 查询一个或多个币种以一种或多种计价货币计的当前价格，并可选附带市值、24 小时成交量、24 小时涨跌与最后更新时间。 |
| `param:ids` | Comma-separated coin IDs. | Coins to price, given as comma-separated CoinGecko coin IDs. | 需要查询价格的币种，以逗号分隔的 CoinGecko 币种 ID 给出。 |
| `param:vs_currencies` | Comma-separated target currencies. | Target currencies to quote prices in, given as a comma-separated list. | 用于计价的目标货币，以逗号分隔的列表给出。 |
| `param:include_market_cap` |  | When enabled, also return each coin's market cap. | 开启后，额外返回每个币种的市值。 |
| `param:include_24hr_vol` |  | When enabled, also return each coin's 24-hour trading volume. | 开启后，额外返回每个币种的 24 小时成交量。 |
| `param:include_24hr_change` |  | When enabled, also return each coin's 24-hour price change. | 开启后，额外返回每个币种的 24 小时价格变动。 |
| `param:include_last_updated_at` |  | When enabled, also return the timestamp at which each price was last updated. | 开启后，额外返回每个价格的最后更新时间戳。 |
| `param:precision` |  | Number of decimal places to use for the returned price values.<br>[⚠️Note:该参数接受的具体取值集合源码未声明，待研发确认。] | 返回价格数值所用的小数位数。<br>[⚠️批注:该参数接受的具体取值集合源码未声明，待研发确认。] |

## coingeckoCoinMarketChart

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Historical market data (price, market cap, 24h volume) for a coin. | Get historical price, market cap and 24-hour volume series for a coin over a trailing number of days, with data granularity controlled by the days range and interval. | 获取某币种在最近若干天内的历史价格、市值与 24 小时成交量序列，数据粒度由天数范围与 interval 共同决定。 |
| `param:interval` | `daily` (default when days ≥ 90), else auto-granular. | Data granularity of the returned series; when omitted, granularity is chosen automatically based on the days range. | 返回序列的数据粒度；省略时按天数范围自动选择粒度。 |

## coingeckoExchangesList

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List all exchanges with current trading volume and metadata. | List exchanges with their current trading volume and metadata, paginated. | 分页列出各交易所及其当前成交量与元信息。 |
| `param:per_page` |  | Number of exchanges returned per page. | 每页返回的交易所数量。 |
| `param:page` |  | Which page of results to return. | 返回结果的页码。 |

## coingeckoTrendingSearch

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Top-7 trending coin searches on CoinGecko in the last 24 hours. | Get the coins most searched on CoinGecko over the last 24 hours. | 获取过去 24 小时内 CoinGecko 上搜索量最高的币种。 |

## coingeckoCategoriesList

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List all categories used by CoinGecko. | List all coin categories defined by CoinGecko; use the returned identifiers to filter other endpoints by category. | 列出 CoinGecko 定义的全部币种分类；返回的标识可用于在其他接口中按分类筛选。 |

## coingeckoCoinTickers

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Tickers (exchange-listed pairs) for a coin. | List the exchange trading pairs (tickers) for a coin, with sorting and paging, optionally filtered to specific exchanges and optionally including order-book depth. | 列出某币种在各交易所的交易对（ticker），支持排序与分页，可限定到指定交易所，并可选附带订单簿深度。 |
| `param:exchange_ids` | Comma-separated exchange IDs. | Restrict tickers to these exchanges, given as comma-separated exchange IDs; IDs come from coingeckoExchangesListIdMap. | 将交易对限定到这些交易所，以逗号分隔的交易所 ID 给出；ID 取自 coingeckoExchangesListIdMap。 |
| `param:page` |  | Which page of tickers to return. | 返回交易对的页码。 |
| `param:order` |  | Sort order of the returned tickers, by trust score or volume. | 返回交易对的排序方式，可按信任评分或成交量排序。 |
| `param:depth` |  | When enabled, include order-book depth (2% cost-to-move) for each ticker. | 开启后，为每个交易对附带订单簿深度（2% 价位的成交成本）。 |

## coingeckoCoinHistory

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Historical snapshot (price, market cap, volume) for a coin on a given date. | Get a one-day historical snapshot of a coin (price, market cap and volume) as of a specific calendar date. | 获取某币种在指定日历日期当天的历史快照（价格、市值与成交量）。 |
| `param:date` | Date in `dd-mm-yyyy` format. | Calendar date of the snapshot to retrieve, in day-month-year form. | 要获取快照的日历日期，采用日-月-年格式。 |
| `param:localization` |  | When enabled, include localized (translated) name fields. | 开启后，包含本地化（翻译后）的名称字段。 |

## coingeckoCoinOhlc

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | OHLC candles for a coin. | Get open/high/low/close candlestick data for a coin over a trailing number of days, in a chosen currency. | 获取某币种在最近若干天内、以指定计价货币计的开高低收（OHLC）K 线数据。 |
| `param:days` | `1`, `7`, `14`, `30`, `90`, `180`, `365`. | How many trailing days of candles to return. | 返回最近多少天的 K 线数据。 |

## coingeckoExchangesListIdMap

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List all exchange IDs and names — use to resolve exchange names to IDs. | List all exchange IDs and names; use it to resolve a human exchange name to the ID required by other exchange endpoints. | 列出全部交易所 ID 与名称；用于把交易所名称解析为其他交易所接口所需的 ID。 |

## coingeckoExchangeById

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Detailed data for a single exchange (volume, tickers, trust score, etc.). | Get detailed data for a single exchange, including volume, trust score and listed tickers. | 获取单个交易所的详细数据，包含成交量、信任评分与挂牌交易对。 |

## coingeckoCategoriesMarketData

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | All categories with market cap, volume, and top-3 coins. | List all coin categories with aggregated market data (market cap, volume and top coins), with sorting. | 列出全部币种分类及其汇总行情数据（市值、成交量与代表币种），支持排序。 |
| `param:order` |  | Sort order of the returned categories, by market cap, name or 24-hour market-cap change. | 返回分类的排序方式，可按市值、名称或 24 小时市值变动排序。 |

## coingeckoNews

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Latest crypto news articles aggregated by CoinGecko. | Get the latest crypto news articles aggregated by CoinGecko. | 获取 CoinGecko 聚合的最新加密货币新闻。 |

## coingeckoExchangeTickers

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Tickers traded on a given exchange. | List the trading pairs (tickers) traded on a given exchange, with sorting and paging, optionally filtered to specific coins and optionally including order-book depth. | 列出某交易所上交易的交易对（ticker），支持排序与分页，可限定到指定币种，并可选附带订单簿深度。 |
| `param:coin_ids` | Filter by coin IDs (comma-separated). | Restrict tickers to these coins, given as comma-separated CoinGecko coin IDs. | 将交易对限定到这些币种，以逗号分隔的 CoinGecko 币种 ID 给出。 |
| `param:page` |  | Which page of tickers to return. | 返回交易对的页码。 |
| `param:depth` |  | When enabled, include order-book depth (2% cost-to-move) for each ticker. | 开启后，为每个交易对附带订单簿深度（2% 价位的成交成本）。 |
| `param:order` |  | Sort order of the returned tickers, by trust score or volume. | 返回交易对的排序方式，可按信任评分或成交量排序。 |

## coingeckoTokenPriceByAddress

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Current price of one or more tokens by contract address on a supported platform. | Get the current price of one or more tokens identified by their on-chain contract address on a given asset platform, quoted in one or more currencies, with optional market cap, 24-hour volume, 24-hour change and last-updated timestamp. | 查询某资产平台上由链上合约地址标识的一个或多个代币的当前价格，以一种或多种计价货币计，并可选附带市值、24 小时成交量、24 小时涨跌与最后更新时间。 |
| `param:id` | Platform ID (e.g., `ethereum`, `binance-smart-chain`, `polygon-pos`). | Asset platform on which the tokens live, given by its CoinGecko platform ID; valid IDs come from CoinGecko's asset platforms list. | 代币所在的资产平台，以其 CoinGecko 平台 ID 给出；有效 ID 取自 CoinGecko 的资产平台列表。 |
| `param:contract_addresses` | Comma-separated contract addresses. | On-chain contract addresses of the tokens to price, given as a comma-separated list. | 要查询价格的代币链上合约地址，以逗号分隔的列表给出。 |
| `param:vs_currencies` | Comma-separated target currencies. | Target currencies to quote prices in, given as a comma-separated list. | 用于计价的目标货币，以逗号分隔的列表给出。 |
| `param:include_market_cap` |  | When enabled, also return each token's market cap. | 开启后，额外返回每个代币的市值。 |
| `param:include_24hr_vol` |  | When enabled, also return each token's 24-hour trading volume. | 开启后，额外返回每个代币的 24 小时成交量。 |
| `param:include_24hr_change` |  | When enabled, also return each token's 24-hour price change. | 开启后，额外返回每个代币的 24 小时价格变动。 |
| `param:include_last_updated_at` |  | When enabled, also return the timestamp at which each price was last updated. | 开启后，额外返回每个价格的最后更新时间戳。 |

## coingeckoCoinByTokenAddress

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | This endpoint allows you to **query all the metadata (image, websites, socials, description, contract address, etc.) and market data (price, ATH, exchange tickers, etc.) of a coin from the CoinGecko coin page based on an asset platform and a particular token contract address** | Get the full coin profile (metadata, links, contract address and market data) for a token identified by its asset platform and on-chain contract address, mirroring the data on its CoinGecko coin page. | 通过资产平台与链上合约地址定位某代币，获取其完整资料（元信息、链接、合约地址与行情数据），内容与其 CoinGecko 币种页一致。 |
| `param:id` | Asset platform ID (e.g., `ethereum`). Refers to the `/asset_platforms` list on CoinGecko. | Asset platform on which the token lives, given by its CoinGecko platform ID; valid IDs come from CoinGecko's asset platforms list. | 代币所在的资产平台，以其 CoinGecko 平台 ID 给出；有效 ID 取自 CoinGecko 的资产平台列表。 |
| `param:contract_address` | The contract address of the token. | On-chain contract address of the token to look up. | 要查询代币的链上合约地址。 |
| `resp.200.id` | coin ID | CoinGecko coin ID for this token; use it to query other coin endpoints such as coingeckoCoinById. | 该代币的 CoinGecko coin ID，可用于调用 coingeckoCoinById 等其他币种接口。 |
| `resp.200.symbol` | coin symbol | Trading symbol of the coin. | 币种的交易符号。 |
| `resp.200.name` | coin name | Display name of the coin. | 币种的展示名称。 |
| `resp.200.web_slug` | coin web slug | URL slug used for the coin on CoinGecko's website. | 该币种在 CoinGecko 网站上使用的 URL slug。 |
| `resp.200.asset_platform_id` | coin asset platform ID | CoinGecko platform ID of the chain the token is issued on. | 代币发行所在链的 CoinGecko 平台 ID。 |
| `resp.200.platforms` | coin asset platform and contract address | Mapping of each asset platform the coin is available on to its contract address on that chain. | 该币种所在各资产平台到其在对应链上合约地址的映射。 |
| `resp.200.detail_platforms` | detailed coin asset platform and contract address | Per-platform contract details, including the contract address and token decimal places. | 各平台的合约明细，含合约地址与代币精度（小数位数）。 |
| `resp.200.block_time_in_minutes` | blockchain block time in minutes | Average block time of the coin's blockchain, in minutes. | 该币种所在区块链的平均出块时间，单位为分钟。 |
| `resp.200.hashing_algorithm` | blockchain hashing algorithm | Hashing algorithm used by the coin's blockchain; null when not applicable. | 该币种区块链所用的哈希算法；不适用时为 null。 |
| `resp.200.categories` | coin categories | CoinGecko categories the coin is classified under. | 该币种所归属的 CoinGecko 分类。 |
| `resp.200.preview_listing` | preview listing coin | Whether the coin is a preview (pre-launch) listing rather than a fully listed asset. | 标识该币种是否为预览（上线前）列表条目，而非已正式上线的资产。 |
| `resp.200.public_notice` | public notice | Public notice shown for the coin, if any; null when none. | 针对该币种展示的公开提示（如有）；无则为 null。 |
| `resp.200.additional_notices` | additional notices | Additional notices shown for the coin. | 针对该币种展示的额外提示信息。 |
| `resp.200.localization` | coin name localization | Map of locale code to the coin's localized name. | 语言区域代码到该币种本地化名称的映射。 |
| `resp.200.description` | coin description | Map of locale code to the coin's description text in that language. | 语言区域代码到该币种对应语言描述文本的映射。 |
| `resp.200.links` | links | Collection of the coin's external links and social handles. | 该币种的各类外部链接与社交账号集合。 |
| `resp.200.links.homepage` | coin website url | Official website URLs of the coin. | 该币种的官方网站 URL。 |
| `resp.200.links.whitepaper` | coin whitepaper url | Whitepaper URLs of the coin. | 该币种的白皮书 URL。 |
| `resp.200.links.blockchain_site` | coin block explorer url | Block explorer URLs for the coin. | 该币种的区块浏览器 URL。 |
| `resp.200.links.official_forum_url` | coin official forum url | Official forum URLs of the coin. | 该币种的官方论坛 URL。 |
| `resp.200.links.chat_url` | coin chat url | Chat or community channel URLs of the coin. | 该币种的聊天或社区频道 URL。 |
| `resp.200.links.announcement_url` | coin announcement url | Announcement page URLs of the coin. | 该币种的公告页面 URL。 |
| `resp.200.links.snapshot_url` | coin snapshot url | Snapshot governance page URL of the coin. | 该币种的 Snapshot 治理页面 URL。 |
| `resp.200.links.twitter_screen_name` | coin twitter handle | Twitter (X) handle of the coin. | 该币种的 Twitter（X）账号。 |
| `resp.200.links.facebook_username` | coin facebook username | Facebook username of the coin. | 该币种的 Facebook 用户名。 |
| `resp.200.links.bitcointalk_thread_identifier` | coin bitcointalk thread identifier | Bitcointalk forum thread identifier of the coin. | 该币种的 Bitcointalk 论坛帖子标识。 |
| `resp.200.links.telegram_channel_identifier` | coin telegram channel identifier | Telegram channel identifier of the coin. | 该币种的 Telegram 频道标识。 |
| `resp.200.links.subreddit_url` | coin subreddit url | Subreddit URL of the coin. | 该币种的 subreddit URL。 |
| `resp.200.links.repos_url` | coin repository url | Source code repository URLs of the coin, grouped by host. | 该币种按托管平台分组的源代码仓库 URL。 |
| `resp.200.links.repos_url.github` | coin github repository url | GitHub repository URLs of the coin. | 该币种的 GitHub 仓库 URL。 |
| `resp.200.links.repos_url.bitbucket` | coin bitbucket repository url | Bitbucket repository URLs of the coin. | 该币种的 Bitbucket 仓库 URL。 |
| `resp.200.image` | coin image url | Coin logo image URLs in several sizes. | 该币种不同尺寸的 logo 图片 URL。 |
| `resp.200.image.thumb` |  | Thumbnail-size logo URL. | 缩略图尺寸的 logo URL。 |
| `resp.200.image.small` |  | Small-size logo URL. | 小尺寸的 logo URL。 |
| `resp.200.image.large` |  | Large-size logo URL. | 大尺寸的 logo URL。 |
| `resp.200.country_origin` | coin country of origin | Country of origin of the coin's project. | 该币种项目的来源国家。 |
| `resp.200.genesis_date` | coin genesis date | Genesis (launch) date of the coin as an ISO 8601 timestamp; null when unknown. | 该币种的创世（上线）日期，ISO 8601 时间戳；未知时为 null。 |
| `resp.200.contract_address` | coin contract address | On-chain contract address of the token. | 该代币的链上合约地址。 |
| `resp.200.sentiment_votes_up_percentage` | coin sentiment votes up percentage | Percentage of community sentiment votes that are positive. | 社区情绪投票中看涨（正面）票的占比百分比。 |
| `resp.200.sentiment_votes_down_percentage` | coin sentiment votes down percentage | Percentage of community sentiment votes that are negative. | 社区情绪投票中看跌（负面）票的占比百分比。 |
| `resp.200.watchlist_portfolio_users` | number of users watching this coin in portfolio | Number of users tracking this coin in their CoinGecko portfolio watchlist. | 在 CoinGecko 投资组合关注列表中关注该币种的用户数。 |
| `resp.200.market_cap_rank` | coin rank by market cap | Rank of the coin by market capitalization. | 该币种按市值排序的排名。 |
| `resp.200.market_cap_rank_with_rehypothecated` | coin rank by market cap including rehypothecated tokens | Rank of the coin by market capitalization, including rehypothecated tokens. | 计入再抵押（rehypothecated）代币后，该币种按市值排序的排名。 |
| `resp.200.market_data` | coin market data | Market metrics for the coin: prices, market cap, volume, supply and price-change figures. | 该币种的市场指标：价格、市值、交易量、供应量与价格涨跌幅等。 |
| `resp.200.market_data.current_price` | coin current price in currency | Map of the coin's current price keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的该币种当前价格。 |
| `resp.200.market_data.current_price.btc` |  | Current price denominated in BTC. | 以 BTC 计价的当前价格。 |
| `resp.200.market_data.current_price.eur` |  | Current price denominated in EUR. | 以 EUR 计价的当前价格。 |
| `resp.200.market_data.current_price.usd` |  | Current price denominated in USD. | 以 USD 计价的当前价格。 |
| `resp.200.market_data.total_value_locked` | total value locked | Total value locked (TVL) in the coin's protocol; null when not applicable. | 该币种协议的总锁仓价值（TVL）；不适用时为 null。 |
| `resp.200.market_data.mcap_to_tvl_ratio` | market cap to total value locked ratio | Ratio of market cap to total value locked; null when not applicable. | 市值与总锁仓价值（TVL）的比值；不适用时为 null。 |
| `resp.200.market_data.fdv_to_tvl_ratio` | fully diluted valuation to total value locked ratio | Ratio of fully diluted valuation to total value locked; null when not applicable. | 完全稀释估值（FDV）与总锁仓价值（TVL）的比值；不适用时为 null。 |
| `resp.200.market_data.roi` | coin return on investment | Return on investment for the coin; null when not available. | 该币种的投资回报率（ROI）；不可用时为 null。 |
| `resp.200.market_data.ath` | coin all time high (ATH) in currency | Map of the coin's all-time-high price keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的该币种历史最高价（ATH）。 |
| `resp.200.market_data.ath.btc` |  | All-time-high price denominated in BTC. | 以 BTC 计价的历史最高价（ATH）。 |
| `resp.200.market_data.ath.eur` |  | All-time-high price denominated in EUR. | 以 EUR 计价的历史最高价（ATH）。 |
| `resp.200.market_data.ath.usd` |  | All-time-high price denominated in USD. | 以 USD 计价的历史最高价（ATH）。 |
| `resp.200.market_data.ath_change_percentage` | coin all time high (ATH) change in percentage | Map of percentage change from the all-time high keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的相对历史最高价（ATH）的涨跌幅百分比。 |
| `resp.200.market_data.ath_change_percentage.btc` |  | Percentage change from the all-time-high price denominated in BTC. | 以 BTC 计价的相对历史最高价（ATH）的涨跌幅百分比。 |
| `resp.200.market_data.ath_change_percentage.eur` |  | Percentage change from the all-time-high price denominated in EUR. | 以 EUR 计价的相对历史最高价（ATH）的涨跌幅百分比。 |
| `resp.200.market_data.ath_change_percentage.usd` |  | Percentage change from the all-time-high price denominated in USD. | 以 USD 计价的相对历史最高价（ATH）的涨跌幅百分比。 |
| `resp.200.market_data.ath_date` | coin all time high (ATH) date | Map of the all-time-high date keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的创下历史最高价（ATH）的日期。 |
| `resp.200.market_data.ath_date.btc` |  | Date the all-time high was reached against BTC, as an ISO 8601 timestamp. | 相对 BTC 的创下历史最高价（ATH）的日期，ISO 8601 时间戳。 |
| `resp.200.market_data.ath_date.eur` |  | Date the all-time high was reached against EUR, as an ISO 8601 timestamp. | 相对 EUR 的创下历史最高价（ATH）的日期，ISO 8601 时间戳。 |
| `resp.200.market_data.ath_date.usd` |  | Date the all-time high was reached against USD, as an ISO 8601 timestamp. | 相对 USD 的创下历史最高价（ATH）的日期，ISO 8601 时间戳。 |
| `resp.200.market_data.atl` | coin all time low (atl) in currency | Map of the coin's all-time-low price keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的该币种历史最低价（ATL）。 |
| `resp.200.market_data.atl.btc` |  | All-time-low price denominated in BTC. | 以 BTC 计价的历史最低价（ATL）。 |
| `resp.200.market_data.atl.eur` |  | All-time-low price denominated in EUR. | 以 EUR 计价的历史最低价（ATL）。 |
| `resp.200.market_data.atl.usd` |  | All-time-low price denominated in USD. | 以 USD 计价的历史最低价（ATL）。 |
| `resp.200.market_data.atl_change_percentage` | coin all time low (atl) change in percentage | Map of percentage change from the all-time low keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的相对历史最低价（ATL）的涨跌幅百分比。 |
| `resp.200.market_data.atl_change_percentage.btc` |  | Percentage change from the all-time-low price denominated in BTC. | 以 BTC 计价的相对历史最低价（ATL）的涨跌幅百分比。 |
| `resp.200.market_data.atl_change_percentage.eur` |  | Percentage change from the all-time-low price denominated in EUR. | 以 EUR 计价的相对历史最低价（ATL）的涨跌幅百分比。 |
| `resp.200.market_data.atl_change_percentage.usd` |  | Percentage change from the all-time-low price denominated in USD. | 以 USD 计价的相对历史最低价（ATL）的涨跌幅百分比。 |
| `resp.200.market_data.atl_date` | coin all time low (atl) date | Map of the all-time-low date keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的创下历史最低价（ATL）的日期。 |
| `resp.200.market_data.atl_date.btc` |  | Date the all-time low was reached against BTC, as an ISO 8601 timestamp. | 相对 BTC 的创下历史最低价（ATL）的日期，ISO 8601 时间戳。 |
| `resp.200.market_data.atl_date.eur` |  | Date the all-time low was reached against EUR, as an ISO 8601 timestamp. | 相对 EUR 的创下历史最低价（ATL）的日期，ISO 8601 时间戳。 |
| `resp.200.market_data.atl_date.usd` |  | Date the all-time low was reached against USD, as an ISO 8601 timestamp. | 相对 USD 的创下历史最低价（ATL）的日期，ISO 8601 时间戳。 |
| `resp.200.market_data.market_cap` | coin market cap in currency | Map of the coin's market capitalization keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的该币种市值。 |
| `resp.200.market_data.market_cap.btc` |  | Market capitalization denominated in BTC. | 以 BTC 计价的市值。 |
| `resp.200.market_data.market_cap.eur` |  | Market capitalization denominated in EUR. | 以 EUR 计价的市值。 |
| `resp.200.market_data.market_cap.usd` |  | Market capitalization denominated in USD. | 以 USD 计价的市值。 |
| `resp.200.market_data.market_cap_rank` | coin rank by market cap | Rank of the coin by market capitalization. | 该币种按市值排序的排名。 |
| `resp.200.market_data.outstanding_token_value_usd` | outstanding token value in USD | Value of outstanding tokens in USD; null when not available. | 流通在外代币的美元价值；不可用时为 null。 |
| `resp.200.market_data.market_cap_rank_with_rehypothecated` | coin rank by market cap including rehypothecated tokens | Rank by market cap including rehypothecated tokens. | 计入再抵押（rehypothecated）代币后按市值排序的排名。 |
| `resp.200.market_data.fully_diluted_valuation` | coin fully diluted valuation (fdv) in currency | Map of the coin's fully diluted valuation keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的该币种完全稀释估值（FDV）。 |
| `resp.200.market_data.fully_diluted_valuation.btc` |  | Fully diluted valuation denominated in BTC. | 以 BTC 计价的完全稀释估值（FDV）。 |
| `resp.200.market_data.fully_diluted_valuation.eur` |  | Fully diluted valuation denominated in EUR. | 以 EUR 计价的完全稀释估值（FDV）。 |
| `resp.200.market_data.fully_diluted_valuation.usd` |  | Fully diluted valuation denominated in USD. | 以 USD 计价的完全稀释估值（FDV）。 |
| `resp.200.market_data.market_cap_fdv_ratio` | market cap to fully diluted valuation ratio | Ratio of market cap to fully diluted valuation. | 市值与完全稀释估值（FDV）的比值。 |
| `resp.200.market_data.total_volume` | coin total trading volume in currency | Map of the coin's total trading volume keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的该币种总交易量。 |
| `resp.200.market_data.total_volume.btc` |  | Total trading volume denominated in BTC. | 以 BTC 计价的总交易量。 |
| `resp.200.market_data.total_volume.eur` |  | Total trading volume denominated in EUR. | 以 EUR 计价的总交易量。 |
| `resp.200.market_data.total_volume.usd` |  | Total trading volume denominated in USD. | 以 USD 计价的总交易量。 |
| `resp.200.market_data.high_24h` | coin 24hr price high in currency | Map of the 24h high price keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的24 小时最高价。 |
| `resp.200.market_data.high_24h.btc` |  | 24-hour high price denominated in BTC. | 以 BTC 计价的24 小时最高价。 |
| `resp.200.market_data.high_24h.eur` |  | 24-hour high price denominated in EUR. | 以 EUR 计价的24 小时最高价。 |
| `resp.200.market_data.high_24h.usd` |  | 24-hour high price denominated in USD. | 以 USD 计价的24 小时最高价。 |
| `resp.200.market_data.low_24h` | coin 24hr price low in currency | Map of the 24h low price keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的24 小时最低价。 |
| `resp.200.market_data.low_24h.btc` |  | 24-hour low price denominated in BTC. | 以 BTC 计价的24 小时最低价。 |
| `resp.200.market_data.low_24h.eur` |  | 24-hour low price denominated in EUR. | 以 EUR 计价的24 小时最低价。 |
| `resp.200.market_data.low_24h.usd` |  | 24-hour low price denominated in USD. | 以 USD 计价的24 小时最低价。 |
| `resp.200.market_data.price_change_24h` | coin 24hr price change in currency | Absolute price change over the last 24 hours. | 过去 24 小时的价格绝对变动。 |
| `resp.200.market_data.price_change_percentage_24h` | coin 24hr price change in percentage | Price change over the last 24 hours, in percent. | 过去 24 小时的价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_7d` | coin 7d price change in percentage | Price change over the last 7 days, in percent. | 过去 7 天的价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_14d` | coin 14d price change in percentage | Price change over the last 14 days, in percent. | 过去 14 天的价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_30d` | coin 30d price change in percentage | Price change over the last 30 days, in percent. | 过去 30 天的价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_60d` | coin 60d price change in percentage | Price change over the last 60 days, in percent. | 过去 60 天的价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_200d` | coin 200d price change in percentage | Price change over the last 200 days, in percent. | 过去 200 天的价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_1y` | coin 1y price change in percentage | Price change over the last year, in percent. | 过去 1 年的价格变动百分比。 |
| `resp.200.market_data.market_cap_change_24h` | coin 24hr market cap change in currency | Absolute market cap change over the last 24 hours. | 过去 24 小时的市值绝对变动。 |
| `resp.200.market_data.market_cap_change_percentage_24h` | coin 24hr market cap change in percentage | Market cap change over the last 24 hours, in percent. | 过去 24 小时的市值变动百分比。 |
| `resp.200.market_data.price_change_24h_in_currency` | coin 24hr price change in currency | Map of 24h price change keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的24 小时价格变动。 |
| `resp.200.market_data.price_change_24h_in_currency.btc` |  | 24-hour price change denominated in BTC. | 以 BTC 计价的24 小时价格变动。 |
| `resp.200.market_data.price_change_24h_in_currency.eur` |  | 24-hour price change denominated in EUR. | 以 EUR 计价的24 小时价格变动。 |
| `resp.200.market_data.price_change_24h_in_currency.usd` |  | 24-hour price change denominated in USD. | 以 USD 计价的24 小时价格变动。 |
| `resp.200.market_data.price_change_percentage_1h_in_currency` | coin 1h price change in currency | Map of 1h price change percentage keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的1 小时价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_1h_in_currency.btc` |  | 1-hour price change percentage denominated in BTC. | 以 BTC 计价的1 小时价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_1h_in_currency.eur` |  | 1-hour price change percentage denominated in EUR. | 以 EUR 计价的1 小时价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_1h_in_currency.usd` |  | 1-hour price change percentage denominated in USD. | 以 USD 计价的1 小时价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_24h_in_currency` | coin 24hr price change in currency | Map of 24h price change percentage keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的24 小时价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_24h_in_currency.btc` |  | 24-hour price change percentage denominated in BTC. | 以 BTC 计价的24 小时价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_24h_in_currency.eur` |  | 24-hour price change percentage denominated in EUR. | 以 EUR 计价的24 小时价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_24h_in_currency.usd` |  | 24-hour price change percentage denominated in USD. | 以 USD 计价的24 小时价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_7d_in_currency` | coin 7d price change in currency | Map of 7d price change percentage keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的7 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_7d_in_currency.btc` |  | 7-day price change percentage denominated in BTC. | 以 BTC 计价的7 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_7d_in_currency.eur` |  | 7-day price change percentage denominated in EUR. | 以 EUR 计价的7 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_7d_in_currency.usd` |  | 7-day price change percentage denominated in USD. | 以 USD 计价的7 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_14d_in_currency` | coin 14d price change in currency | Map of 14d price change percentage keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的14 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_14d_in_currency.btc` |  | 14-day price change percentage denominated in BTC. | 以 BTC 计价的14 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_14d_in_currency.eur` |  | 14-day price change percentage denominated in EUR. | 以 EUR 计价的14 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_14d_in_currency.usd` |  | 14-day price change percentage denominated in USD. | 以 USD 计价的14 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_30d_in_currency` | coin 30d price change in currency | Map of 30d price change percentage keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的30 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_30d_in_currency.btc` |  | 30-day price change percentage denominated in BTC. | 以 BTC 计价的30 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_30d_in_currency.eur` |  | 30-day price change percentage denominated in EUR. | 以 EUR 计价的30 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_30d_in_currency.usd` |  | 30-day price change percentage denominated in USD. | 以 USD 计价的30 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_60d_in_currency` | coin 60d price change in currency | Map of 60d price change percentage keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的60 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_60d_in_currency.btc` |  | 60-day price change percentage denominated in BTC. | 以 BTC 计价的60 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_60d_in_currency.eur` |  | 60-day price change percentage denominated in EUR. | 以 EUR 计价的60 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_60d_in_currency.usd` |  | 60-day price change percentage denominated in USD. | 以 USD 计价的60 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_200d_in_currency` | coin 200d price change in currency | Map of 200d price change percentage keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的200 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_200d_in_currency.btc` |  | 200-day price change percentage denominated in BTC. | 以 BTC 计价的200 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_200d_in_currency.eur` |  | 200-day price change percentage denominated in EUR. | 以 EUR 计价的200 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_200d_in_currency.usd` |  | 200-day price change percentage denominated in USD. | 以 USD 计价的200 天价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_1y_in_currency` | coin 1y price change in currency | Map of 1y price change percentage keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的1 年价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_1y_in_currency.btc` |  | 1-year price change percentage denominated in BTC. | 以 BTC 计价的1 年价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_1y_in_currency.eur` |  | 1-year price change percentage denominated in EUR. | 以 EUR 计价的1 年价格变动百分比。 |
| `resp.200.market_data.price_change_percentage_1y_in_currency.usd` |  | 1-year price change percentage denominated in USD. | 以 USD 计价的1 年价格变动百分比。 |
| `resp.200.market_data.market_cap_change_24h_in_currency` | coin 24hr market cap change in currency | Map of 24h market cap change keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的24 小时市值变动。 |
| `resp.200.market_data.market_cap_change_24h_in_currency.btc` |  | 24-hour market cap change denominated in BTC. | 以 BTC 计价的24 小时市值变动。 |
| `resp.200.market_data.market_cap_change_24h_in_currency.eur` |  | 24-hour market cap change denominated in EUR. | 以 EUR 计价的24 小时市值变动。 |
| `resp.200.market_data.market_cap_change_24h_in_currency.usd` |  | 24-hour market cap change denominated in USD. | 以 USD 计价的24 小时市值变动。 |
| `resp.200.market_data.market_cap_change_percentage_24h_in_currency` | coin 24hr market cap change in percentage | Map of 24h market cap change percentage keyed by currency code (e.g. btc, eur, usd). | 按货币代码（如 btc、eur、usd）分组的24 小时市值变动百分比。 |
| `resp.200.market_data.market_cap_change_percentage_24h_in_currency.btc` |  | 24-hour market cap change percentage denominated in BTC. | 以 BTC 计价的24 小时市值变动百分比。 |
| `resp.200.market_data.market_cap_change_percentage_24h_in_currency.eur` |  | 24-hour market cap change percentage denominated in EUR. | 以 EUR 计价的24 小时市值变动百分比。 |
| `resp.200.market_data.market_cap_change_percentage_24h_in_currency.usd` |  | 24-hour market cap change percentage denominated in USD. | 以 USD 计价的24 小时市值变动百分比。 |
| `resp.200.market_data.total_supply` | coin total supply | Total amount of the coin that exists. | 该币种已存在的代币总量。 |
| `resp.200.market_data.max_supply` | coin max supply | Maximum supply of the coin; null when unbounded or unknown. | 该币种的最大供应量；无上限或未知时为 null。 |
| `resp.200.market_data.max_supply_infinite` | whether max supply is infinite | Whether the coin's maximum supply is uncapped. | 标识该币种最大供应量是否无上限。 |
| `resp.200.market_data.circulating_supply` | coin circulating supply | Amount of the coin currently in circulation. | 该币种当前流通的代币数量。 |
| `resp.200.market_data.outstanding_supply` | tokens outstanding in the market, circulated/tradable or planned for circulation | Tokens outstanding in the market: circulated/tradable or planned for circulation; null when not available. | 市场中流通在外的代币数量：已流通/可交易或计划流通的部分；不可用时为 null。 |
| `resp.200.market_data.last_updated` | coin market data last updated timestamp | Timestamp when the market data was last refreshed, as an ISO 8601 timestamp. | 市场数据最近一次刷新的时间，ISO 8601 时间戳。 |
| `resp.200.community_data` | coin community data | Community engagement metrics for the coin across social platforms. | 该币种在各社交平台上的社区活跃度指标。 |
| `resp.200.community_data.facebook_likes` | coin facebook likes | Number of Facebook likes for the coin's page. | 该币种 Facebook 主页的点赞数。 |
| `resp.200.community_data.reddit_average_posts_48h` | coin reddit average posts in 48 hours | Average number of subreddit posts over the last 48 hours. | 过去 48 小时 subreddit 的平均发帖数。 |
| `resp.200.community_data.reddit_average_comments_48h` | coin reddit average comments in 48 hours | Average number of subreddit comments over the last 48 hours. | 过去 48 小时 subreddit 的平均评论数。 |
| `resp.200.community_data.reddit_subscribers` | coin reddit subscribers | Number of subscribers to the coin's subreddit. | 该币种 subreddit 的订阅者数量。 |
| `resp.200.community_data.reddit_accounts_active_48h` | coin reddit active accounts in 48 hours | Number of subreddit accounts active over the last 48 hours. | 过去 48 小时 subreddit 的活跃账号数。 |
| `resp.200.community_data.telegram_channel_user_count` | coin telegram channel user count | Number of users in the coin's Telegram channel. | 该币种 Telegram 频道的用户数。 |
| `resp.200.developer_data` | coin developer data | Development activity metrics derived from the coin's source repositories. | 基于该币种源代码仓库的开发活跃度指标。 |
| `resp.200.developer_data.forks` | coin repository forks | Number of forks of the coin's repositories. | 该币种仓库的 fork 数。 |
| `resp.200.developer_data.stars` | coin repository stars | Number of stars on the coin's repositories. | 该币种仓库的 star 数。 |
| `resp.200.developer_data.subscribers` | coin repository subscribers | Number of watchers/subscribers of the coin's repositories. | 该币种仓库的关注（watch/subscribe）数。 |
| `resp.200.developer_data.total_issues` | coin repository total issues | Total number of issues in the coin's repositories. | 该币种仓库的 issue 总数。 |
| `resp.200.developer_data.closed_issues` | coin repository closed issues | Number of closed issues in the coin's repositories. | 该币种仓库已关闭的 issue 数。 |
| `resp.200.developer_data.pull_requests_merged` | coin repository pull requests merged | Number of merged pull requests in the coin's repositories. | 该币种仓库已合并的 pull request 数。 |
| `resp.200.developer_data.pull_request_contributors` | coin repository pull request contributors | Number of pull request contributors to the coin's repositories. | 该币种仓库的 pull request 贡献者数。 |
| `resp.200.developer_data.code_additions_deletions_4_weeks` | coin code additions and deletions in 4 weeks | Lines of code added and removed over the last 4 weeks. | 过去 4 周新增与删除的代码行数。 |
| `resp.200.developer_data.code_additions_deletions_4_weeks.additions` |  | Lines of code added over the last 4 weeks. | 过去 4 周新增的代码行数。 |
| `resp.200.developer_data.code_additions_deletions_4_weeks.deletions` |  | Lines of code removed over the last 4 weeks. | 过去 4 周删除的代码行数。 |
| `resp.200.developer_data.commit_count_4_weeks` | coin repository commit count in 4 weeks | Number of commits over the last 4 weeks. | 过去 4 周的提交（commit）数。 |
| `resp.200.developer_data.last_4_weeks_commit_activity_series` | coin repository last 4 weeks commit activity series | Daily commit counts over the last 4 weeks. | 过去 4 周每日提交（commit）数的序列。 |
| `resp.200.status_updates` | coin status updates | Recent status updates published for the coin. | 该币种近期发布的状态动态。 |
| `resp.200.last_updated` | coin last updated timestamp | Timestamp when the coin record was last updated, as an ISO 8601 timestamp. | 该币种记录最近一次更新的时间，ISO 8601 时间戳。 |
| `resp.200.tickers` | coin tickers | Trading pairs (tickers) for the coin across exchanges. | 该币种在各交易所上的交易对（ticker）。 |
| `resp.200.tickers.base` | coin ticker base currency | Base currency of the trading pair. | 交易对的基础货币（base）。 |
| `resp.200.tickers.target` | coin ticker target currency | Target (quote) currency of the trading pair. | 交易对的目标（计价）货币（target）。 |
| `resp.200.tickers.market` | coin ticker exchange | Exchange the ticker is traded on. | 该 ticker 所在的交易所。 |
| `resp.200.tickers.market.name` | coin ticker exchange name | Display name of the exchange. | 交易所的展示名称。 |
| `resp.200.tickers.market.identifier` | coin ticker exchange identifier | CoinGecko identifier of the exchange. | 交易所的 CoinGecko 标识。 |
| `resp.200.tickers.market.has_trading_incentive` | coin ticker exchange trading incentive | Whether the exchange offers trading incentives for this pair. | 标识该交易所是否对此交易对提供交易激励。 |
| `resp.200.tickers.last` | coin ticker last price | Last traded price of the pair. | 该交易对的最新成交价。 |
| `resp.200.tickers.volume` | coin ticker volume | Trading volume of the pair. | 该交易对的交易量。 |
| `resp.200.tickers.converted_last` | coin ticker converted last price | Last traded price converted into reference currencies. | 换算为参考货币后的最新成交价。 |
| `resp.200.tickers.converted_last.btc` |  | Last traded price denominated in BTC. | 以 BTC 计价的最新成交价。 |
| `resp.200.tickers.converted_last.eth` |  | Last traded price denominated in ETH. | 以 ETH 计价的最新成交价。 |
| `resp.200.tickers.converted_last.usd` |  | Last traded price denominated in USD. | 以 USD 计价的最新成交价。 |
| `resp.200.tickers.converted_volume` | coin ticker converted volume | Trading volume converted into reference currencies. | 换算为参考货币后的交易量。 |
| `resp.200.tickers.converted_volume.btc` |  | Trading volume denominated in BTC. | 以 BTC 计价的交易量。 |
| `resp.200.tickers.converted_volume.eth` |  | Trading volume denominated in ETH. | 以 ETH 计价的交易量。 |
| `resp.200.tickers.converted_volume.usd` |  | Trading volume denominated in USD. | 以 USD 计价的交易量。 |
| `resp.200.tickers.trust_score` | coin ticker trust score | Trust score assigned to the ticker; null when unscored. | 为该 ticker 评定的信任评分（trust score）；未评分时为 null。 |
| `resp.200.tickers.bid_ask_spread_percentage` | coin ticker bid ask spread percentage | Bid-ask spread of the pair, in percent. | 该交易对的买卖价差（bid-ask spread）百分比。 |
| `resp.200.tickers.timestamp` | coin ticker timestamp | Ticker timestamp as an ISO 8601 timestamp. | 该 ticker 的时间，ISO 8601 时间戳。 |
| `resp.200.tickers.last_traded_at` | coin ticker last traded timestamp | Time of the last trade for the pair, as an ISO 8601 timestamp. | 该交易对最近一次成交的时间，ISO 8601 时间戳。 |
| `resp.200.tickers.last_fetch_at` | coin ticker last fetch timestamp | Time the ticker was last fetched, as an ISO 8601 timestamp. | 该 ticker 最近一次抓取的时间，ISO 8601 时间戳。 |
| `resp.200.tickers.is_anomaly` | coin ticker anomaly | Whether the ticker is flagged as anomalous. | 标识该 ticker 是否被标记为异常。 |
| `resp.200.tickers.is_stale` | coin ticker stale | Whether the ticker data is considered stale. | 标识该 ticker 数据是否被视为陈旧（stale）。 |
| `resp.200.tickers.trade_url` | coin ticker trade url | URL to trade this pair on the exchange. | 在该交易所交易此交易对的 URL。 |
| `resp.200.tickers.token_info_url` | coin ticker token info url | URL to token information for the pair on the exchange. | 该交易所上此交易对代币信息的 URL。 |
| `resp.200.tickers.coin_id` | coin ticker base currency coin ID | CoinGecko coin ID of the base currency. | 基础货币（base）的 CoinGecko coin ID。 |
| `resp.200.tickers.target_coin_id` | coin ticker target currency coin ID | CoinGecko coin ID of the target currency. | 目标货币（target）的 CoinGecko coin ID。 |
| `resp.200.tickers.coin_mcap_usd` | coin market cap in USD | Market capitalization of the coin in USD. | 该币种以美元计的市值。 |

## coingeckoCoinMarketChartByContract

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Historical market data for a token by contract address. | Get historical price, market cap and 24-hour volume series for a token identified by its asset platform and contract address; the response has the same shape as coingeckoCoinMarketChart. | 通过资产平台与合约地址定位某代币，获取其历史价格、市值与 24 小时成交量序列；返回结构与 coingeckoCoinMarketChart 相同。 |
| `param:id` | Platform ID. | Asset platform on which the token lives, given by its CoinGecko platform ID. | 代币所在的资产平台，以其 CoinGecko 平台 ID 给出。 |
| `param:contract_address` | Contract address. | On-chain contract address of the token whose history is requested. | 要查询历史数据的代币链上合约地址。 |

## coingeckoCoinMarketChartRange

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Historical market data within an explicit UNIX timestamp range. | Get historical price, market cap and 24-hour volume series for a coin between an explicit start and end UNIX timestamp; the response has the same shape as coingeckoCoinMarketChart. | 获取某币种在明确的起止 UNIX 时间戳之间的历史价格、市值与 24 小时成交量序列；返回结构与 coingeckoCoinMarketChart 相同。 |
| `param:from` | Start UNIX timestamp (seconds). | Start of the historical window, as a UNIX timestamp in seconds. | 历史数据窗口的起点，以秒为单位的 UNIX 时间戳。 |
| `param:to` | End UNIX timestamp (seconds). | End of the historical window, as a UNIX timestamp in seconds. | 历史数据窗口的终点，以秒为单位的 UNIX 时间戳。 |

