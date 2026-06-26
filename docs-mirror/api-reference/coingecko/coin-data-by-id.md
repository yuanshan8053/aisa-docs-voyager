> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Coin Data by ID

> Current data (price, markets, links, community, developer data) for a coin.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/{id}
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
  /coingecko/coins/{id}:
    get:
      summary: Coin Data by ID
      description: >-
        Current data (price, markets, links, community, developer data) for a
        coin.
      operationId: coingeckoCoinById
      parameters:
        - $ref: '#/components/parameters/CoinId'
        - name: localization
          in: query
          schema:
            type: boolean
            default: true
        - name: tickers
          in: query
          schema:
            type: boolean
            default: true
        - name: market_data
          in: query
          schema:
            type: boolean
            default: true
        - name: community_data
          in: query
          schema:
            type: boolean
            default: true
        - name: developer_data
          in: query
          schema:
            type: boolean
            default: true
        - name: sparkline
          in: query
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: Coin object.
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