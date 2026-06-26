> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exchanges List

> List all exchanges with current trading volume and metadata.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/exchanges
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
  /coingecko/exchanges:
    get:
      summary: Exchanges List
      description: List all exchanges with current trading volume and metadata.
      operationId: coingeckoExchangesList
      parameters:
        - name: per_page
          in: query
          schema:
            type: integer
            default: 100
            maximum: 250
        - name: page
          in: query
          schema:
            type: integer
            default: 1
      responses:
        '200':
          description: Array of exchange objects.
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````