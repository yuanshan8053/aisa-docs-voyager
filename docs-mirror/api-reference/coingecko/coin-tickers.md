> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Coin Tickers

> Tickers (exchange-listed trading pairs) for a coin.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/{id}/tickers
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
  /coingecko/coins/{id}/tickers:
    get:
      summary: Coin Tickers
      description: Tickers (exchange-listed pairs) for a coin.
      operationId: coingeckoCoinTickers
      parameters:
        - $ref: '#/components/parameters/CoinId'
        - name: exchange_ids
          in: query
          description: Comma-separated exchange IDs.
          schema:
            type: string
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: order
          in: query
          schema:
            type: string
            enum:
              - trust_score_desc
              - trust_score_asc
              - volume_desc
        - name: depth
          in: query
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: Tickers array.
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