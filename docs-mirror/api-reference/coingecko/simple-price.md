> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Simple Price

> Current price for one or more cryptocurrencies in any supported currencies.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/simple/price
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
  /coingecko/simple/price:
    get:
      summary: Simple Price
      description: Current price for any cryptocurrencies in any supported currencies.
      operationId: coingeckoSimplePrice
      parameters:
        - name: ids
          in: query
          required: true
          description: Comma-separated coin IDs.
          schema:
            type: string
          example: bitcoin,ethereum
        - name: vs_currencies
          in: query
          required: true
          description: Comma-separated target currencies.
          schema:
            type: string
          example: usd,eur
        - name: include_market_cap
          in: query
          schema:
            type: boolean
            default: false
        - name: include_24hr_vol
          in: query
          schema:
            type: boolean
            default: false
        - name: include_24hr_change
          in: query
          schema:
            type: boolean
            default: false
        - name: include_last_updated_at
          in: query
          schema:
            type: boolean
            default: false
        - name: precision
          in: query
          schema:
            type: string
      responses:
        '200':
          description: Map keyed by coin id.
          content:
            application/json:
              example:
                bitcoin:
                  usd: 67234.12
                  eur: 62019.45
                ethereum:
                  usd: 3412
                  eur: 3147.8
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````