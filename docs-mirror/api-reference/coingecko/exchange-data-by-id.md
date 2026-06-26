> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exchange Data by ID

> Detailed data for a single exchange: volume, tickers, trust score, and metadata.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/exchanges/{id}
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
  /coingecko/exchanges/{id}:
    get:
      summary: Exchange Data by ID
      description: >-
        Detailed data for a single exchange (volume, tickers, trust score,
        etc.).
      operationId: coingeckoExchangeById
      parameters:
        - $ref: '#/components/parameters/ExchangeId'
      responses:
        '200':
          description: Exchange object.
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