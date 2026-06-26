> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Coins List (ID Map)

> List all coins with id, symbol, and name. Use to map symbols to CoinGecko IDs.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/list
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
  /coingecko/coins/list:
    get:
      summary: Coins List (ID Map)
      description: >-
        List all coins with id, symbol, and name. Use to map symbols to
        CoinGecko IDs.
      operationId: coingeckoCoinsList
      parameters:
        - name: include_platform
          in: query
          description: Include platform + contract addresses.
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: Array of coins.
          content:
            application/json:
              example:
                - id: bitcoin
                  symbol: btc
                  name: Bitcoin
                - id: ethereum
                  symbol: eth
                  name: Ethereum
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````