> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Coin Historical Chart

> Historical market data (price, market cap, 24h volume) for a coin over the last N days.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/{id}/market_chart
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
  /coingecko/coins/{id}/market_chart:
    get:
      summary: Coin Historical Chart
      description: Historical market data (price, market cap, 24h volume) for a coin.
      operationId: coingeckoCoinMarketChart
      parameters:
        - $ref: '#/components/parameters/CoinId'
        - $ref: '#/components/parameters/VsCurrency'
        - $ref: '#/components/parameters/Days'
        - name: interval
          in: query
          description: '`daily` (default when days ≥ 90), else auto-granular.'
          schema:
            type: string
            enum:
              - daily
      responses:
        '200':
          description: Three time-series arrays.
          content:
            application/json:
              example:
                prices:
                  - - 1713398400000
                    - 67234.12
                  - - 1713402000000
                    - 67301.55
                market_caps:
                  - - 1713398400000
                    - 1321498765432
                total_volumes:
                  - - 1713398400000
                    - 25679876543
components:
  parameters:
    CoinId:
      name: id
      in: path
      required: true
      description: >-
        CoinGecko coin ID (e.g., `bitcoin`, `ethereum`). Get the list via
        `/coins/list`.
      schema:
        type: string
      example: bitcoin
    VsCurrency:
      name: vs_currency
      in: query
      required: true
      description: >-
        Target currency for price (e.g., `usd`, `eur`, `btc`). See
        `/simple/supported_vs_currencies`.
      schema:
        type: string
        default: usd
    Days:
      name: days
      in: query
      required: true
      description: >-
        Data up to N days ago. Accepts `1`, `7`, `14`, `30`, `90`, `180`, `365`,
        or `max`.
      schema:
        type: string
      example: '7'
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````