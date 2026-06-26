> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Categories List

> List all categories used by CoinGecko.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/coins/categories/list
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
  /coingecko/coins/categories/list:
    get:
      summary: Categories List
      description: List all categories used by CoinGecko.
      operationId: coingeckoCategoriesList
      responses:
        '200':
          description: Array of categories.
          content:
            application/json:
              example:
                - category_id: layer-1
                  name: Layer 1 (L1)
                - category_id: meme-token
                  name: Meme
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````