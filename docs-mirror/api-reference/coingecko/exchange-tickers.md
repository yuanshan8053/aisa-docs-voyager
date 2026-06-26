> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exchange Tickers

> Tickers (trading pairs) listed on a given exchange.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/exchanges/{id}/tickers
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
  /coingecko/exchanges/{id}/tickers:
    get:
      summary: Exchange Tickers
      description: Tickers traded on a given exchange.
      operationId: coingeckoExchangeTickers
      parameters:
        - $ref: '#/components/parameters/ExchangeId'
        - name: coin_ids
          in: query
          description: Filter by coin IDs (comma-separated).
          schema:
            type: string
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: depth
          in: query
          schema:
            type: boolean
            default: false
        - name: order
          in: query
          schema:
            type: string
            enum:
              - trust_score_desc
              - volume_desc
      responses:
        '200':
          description: Tickers array.
components:
  parameters:
    ExchangeId:
      name: id
      in: path
      required: true
      description: >-
        CoinGecko exchange ID (e.g., `binance`, `gdax`). Get the list via
        `/exchanges/list`.
      schema:
        type: string
      example: binance
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````