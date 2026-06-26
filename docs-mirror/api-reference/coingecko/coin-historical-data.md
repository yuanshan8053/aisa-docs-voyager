> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Coin Historical Data

> Historical snapshot (price, market cap, volume) for a coin on a given date.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/{id}/history
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
  /coingecko/coins/{id}/history:
    get:
      summary: Coin Historical Data
      description: >-
        Historical snapshot (price, market cap, volume) for a coin on a given
        date.
      operationId: coingeckoCoinHistory
      parameters:
        - $ref: '#/components/parameters/CoinId'
        - name: date
          in: query
          required: true
          description: Date in `dd-mm-yyyy` format.
          schema:
            type: string
          example: 30-12-2024
        - name: localization
          in: query
          schema:
            type: boolean
            default: true
      responses:
        '200':
          description: Snapshot object for the given date.
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````