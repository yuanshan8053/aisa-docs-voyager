> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Coin Historical Chart by Contract

> Historical market data for a token by contract address on a supported platform.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/{id}/contract/{contract_address}/market_chart
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
  /coingecko/coins/{id}/contract/{contract_address}/market_chart:
    get:
      summary: Coin Historical Chart by Contract
      description: Historical market data for a token by contract address.
      operationId: coingeckoCoinMarketChartByContract
      parameters:
        - name: id
          in: path
          required: true
          description: Platform ID.
          schema:
            type: string
          example: ethereum
        - name: contract_address
          in: path
          required: true
          description: Contract address.
          schema:
            type: string
        - $ref: '#/components/parameters/VsCurrency'
        - $ref: '#/components/parameters/Days'
      responses:
        '200':
          description: Same shape as `/coins/{id}/market_chart`.
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