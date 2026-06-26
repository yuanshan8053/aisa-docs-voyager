> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Coin OHLC

> OHLC candles for a coin.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/{id}/ohlc
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
  /coingecko/coins/{id}/ohlc:
    get:
      summary: Coin OHLC
      description: OHLC candles for a coin.
      operationId: coingeckoCoinOhlc
      parameters:
        - $ref: '#/components/parameters/CoinId'
        - $ref: '#/components/parameters/VsCurrency'
        - name: days
          in: query
          required: true
          description: '`1`, `7`, `14`, `30`, `90`, `180`, `365`.'
          schema:
            type: string
          example: '7'
      responses:
        '200':
          description: 'Array of OHLC rows: `[timestamp, open, high, low, close]`.'
          content:
            application/json:
              example:
                - - 1713398400000
                  - 67000
                  - 67500
                  - 66900
                  - 67234.12
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