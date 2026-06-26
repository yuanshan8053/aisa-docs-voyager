> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Categories with Market Data

> All categories with market cap, volume, and top-3 coins.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/categories
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
  /coingecko/coins/categories:
    get:
      summary: Categories with Market Data
      description: All categories with market cap, volume, and top-3 coins.
      operationId: coingeckoCategoriesMarketData
      parameters:
        - name: order
          in: query
          schema:
            type: string
            enum:
              - market_cap_desc
              - market_cap_asc
              - name_desc
              - name_asc
              - market_cap_change_24h_desc
              - market_cap_change_24h_asc
      responses:
        '200':
          description: Array of categories with market data.
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````