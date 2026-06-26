> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Supported Currencies

> List of all supported fiat and crypto currencies accepted as `vs_currency`.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/simple/supported_vs_currencies
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
  /coingecko/simple/supported_vs_currencies:
    get:
      summary: Supported Currencies
      description: >-
        List of all supported fiat and crypto currencies for `vs_currency`
        parameters.
      operationId: coingeckoSupportedVsCurrencies
      responses:
        '200':
          description: Array of currency codes.
          content:
            application/json:
              example:
                - btc
                - eth
                - usd
                - eur
                - jpy
                - gbp
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````