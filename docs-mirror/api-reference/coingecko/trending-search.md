> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Trending Search

> Top-7 trending coin searches on CoinGecko in the last 24 hours.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/search/trending
openapi: 3.0.3
info:
  title: CoinGecko API
  version: 1.0.0
  description: >-
    CoinGecko crypto market data routed through the AIsa gateway. Covers coin
    metadata, live and historical prices, OHLC, exchanges, tickers, categories,
    and trending search. Proxies the public CoinGecko v3 API at
    `https://api.coingecko.com/api/v3/`.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /coingecko/search/trending:
    get:
      summary: Trending Search
      description: Top-7 trending coin searches on CoinGecko in the last 24 hours.
      operationId: coingeckoTrendingSearch
      responses:
        '200':
          description: Trending coins, nfts, and categories.
          content:
            application/json:
              example:
                coins:
                  - item:
                      id: bitcoin
                      name: Bitcoin
                      symbol: BTC
                      market_cap_rank: 1
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````