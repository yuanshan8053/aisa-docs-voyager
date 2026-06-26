> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Crypto News

> Latest crypto news articles aggregated by CoinGecko.



## OpenAPI

````yaml openapi/coingecko.json GET /coingecko/news
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
  /coingecko/news:
    get:
      summary: Crypto News
      description: Latest crypto news articles aggregated by CoinGecko.
      operationId: coingeckoNews
      responses:
        '200':
          description: Array of news articles.
          content:
            application/json:
              example:
                data:
                  - title: Bitcoin hits new high
                    url: https://example.com/article
                    published_at: 1713398400
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````