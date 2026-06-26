> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Coin Price by Token Address

> Current price of tokens looked up by contract address on a supported platform (Ethereum, BSC, Polygon, etc.).



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/simple/token_price/{id}
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
  /coingecko/simple/token_price/{id}:
    get:
      summary: Coin Price by Token Address
      description: >-
        Current price of one or more tokens by contract address on a supported
        platform.
      operationId: coingeckoTokenPriceByAddress
      parameters:
        - name: id
          in: path
          required: true
          description: >-
            Platform ID (e.g., `ethereum`, `binance-smart-chain`,
            `polygon-pos`).
          schema:
            type: string
          example: ethereum
        - name: contract_addresses
          in: query
          required: true
          description: Comma-separated contract addresses.
          schema:
            type: string
          example: '0xdAC17F958D2ee523a2206206994597C13D831ec7'
        - name: vs_currencies
          in: query
          required: true
          description: Comma-separated target currencies.
          schema:
            type: string
          example: usd
        - name: include_market_cap
          in: query
          schema:
            type: boolean
        - name: include_24hr_vol
          in: query
          schema:
            type: boolean
        - name: include_24hr_change
          in: query
          schema:
            type: boolean
        - name: include_last_updated_at
          in: query
          schema:
            type: boolean
      responses:
        '200':
          description: Map keyed by contract address.
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````