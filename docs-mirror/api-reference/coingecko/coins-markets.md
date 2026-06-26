> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Coins Markets

> List all coins with market data: price, market cap, volume, and other metrics.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/markets
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
  /coingecko/coins/markets:
    get:
      summary: Coins Markets
      description: >-
        List all coins with market data: price, market cap, volume, and other
        metrics.
      operationId: coingeckoCoinsMarkets
      parameters:
        - $ref: '#/components/parameters/VsCurrency'
        - name: ids
          in: query
          description: Comma-separated CoinGecko coin IDs.
          schema:
            type: string
          example: bitcoin,ethereum
        - name: category
          in: query
          description: Filter by category (see `/coins/categories/list`).
          schema:
            type: string
        - name: order
          in: query
          schema:
            type: string
            enum:
              - market_cap_desc
              - market_cap_asc
              - volume_desc
              - volume_asc
              - id_asc
              - id_desc
            default: market_cap_desc
        - name: per_page
          in: query
          schema:
            type: integer
            default: 100
            minimum: 1
            maximum: 250
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: sparkline
          in: query
          schema:
            type: boolean
            default: false
        - name: price_change_percentage
          in: query
          description: 'Comma-separated windows: `1h,24h,7d,14d,30d,200d,1y`.'
          schema:
            type: string
      responses:
        '200':
          description: Array of coin market entries.
components:
  parameters:
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````