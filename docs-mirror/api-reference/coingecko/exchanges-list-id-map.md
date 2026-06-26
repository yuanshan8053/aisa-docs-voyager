> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exchanges List (ID Map)

> List all exchange IDs and names. Use to map exchange names to CoinGecko IDs.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/exchanges/list
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
  /coingecko/exchanges/list:
    get:
      summary: Exchanges List (ID Map)
      description: List all exchange IDs and names — use to resolve exchange names to IDs.
      operationId: coingeckoExchangesListIdMap
      responses:
        '200':
          description: Array of `{id, name}`.
          content:
            application/json:
              example:
                - id: binance
                  name: Binance
                - id: gdax
                  name: Coinbase Exchange
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````