> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Coin Market Chart Range

> Historical market data for a coin within an explicit UNIX timestamp range.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/{id}/market_chart/range
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
  /coingecko/coins/{id}/market_chart/range:
    get:
      summary: Coin Market Chart Range
      description: Historical market data within an explicit UNIX timestamp range.
      operationId: coingeckoCoinMarketChartRange
      parameters:
        - $ref: '#/components/parameters/CoinId'
        - $ref: '#/components/parameters/VsCurrency'
        - name: from
          in: query
          required: true
          description: Start UNIX timestamp (seconds).
          schema:
            type: integer
          example: 1713398400
        - name: to
          in: query
          required: true
          description: End UNIX timestamp (seconds).
          schema:
            type: integer
          example: 1713484800
      responses:
        '200':
          description: Same shape as `/coins/{id}/market_chart`.
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````