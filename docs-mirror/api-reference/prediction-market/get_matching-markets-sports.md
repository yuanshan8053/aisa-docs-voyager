> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sports

> Get Matching Markets for Sports

Sports finds equivalent markets across different prediction market platforms (Polymarket, Kalshi, etc.) for sports events. Provide either one or more Polymarket market slugs or Kalshi event tickers to discover the corresponding markets on other platforms, including their token IDs and market tickers.

**Best for:** Cross-platform arbitrage detection, comparing odds across prediction markets, building multi-platform sports dashboards, finding liquidity across venues.

**Endpoint:** `GET /matching-markets/sports`

> **Note:** Exactly one of `polymarket_market_slug` or `kalshi_event_ticker` must be provided. They cannot be combined in the same request. Multiple values for either parameter are supported.

## Example

```bash theme={null}
curl -X GET "https://api.aisa.one/apis/v1/matching-markets/sports?polymarket_market_slug=nfl-ari-den-2025-08-16&polymarket_market_slug=nfl-dal-phi-2025-09-04" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

## Response

The response returns a `markets` object keyed by the input identifier (slug or ticker). Each key maps to an array of platform-specific market objects. Kalshi objects include `platform`, `event_ticker`, and `market_tickers`. Polymarket objects include `platform`, `market_slug`, and `token_ids`.


## OpenAPI

````yaml openapi/matching-markets-openapi.json GET /matching-markets/sports
openapi: 3.0.3
info:
  title: AIsa API proxy
  description: APIs for prediction markets.
  version: 0.0.1
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /matching-markets/sports:
    get:
      summary: Get Matching Markets for Sports
      description: >-
        Find equivalent markets across different prediction market platforms
        (Polymarket, Kalshi, etc.) for sports events. Provide either one or more
        Polymarket market slugs or Kalshi event tickers.
      operationId: get_matching-markets-sports
      parameters:
        - name: polymarket_market_slug
          in: query
          required: false
          description: >-
            The Polymarket market slug(s) to find matching markets for. To get
            multiple markets at once, provide the query param multiple times
            with different slugs. Can not be combined with kalshi_event_ticker.
          schema:
            type: array
            items:
              type: string
            example:
              - nfl-ari-den-2025-08-16
              - nfl-dal-phi-2025-09-04
          style: form
          explode: true
        - name: kalshi_event_ticker
          in: query
          required: false
          description: >-
            The Kalshi event ticker(s) to find matching markets for. To get
            multiple markets at once, provide the query param multiple times
            with different tickers. Can not be combined with
            polymarket_market_slug.
          schema:
            type: array
            items:
              type: string
            example:
              - KXNFLGAME-25AUG16ARIDEN
              - KXNFLGAME-25SEP04DALPHI
          style: form
          explode: true
      responses:
        '200':
          description: Matching markets response
          content:
            application/json:
              schema:
                type: object
                properties:
                  markets:
                    type: object
                    additionalProperties:
                      type: array
                      items:
                        oneOf:
                          - type: object
                            description: Kalshi market
                            properties:
                              platform:
                                type: string
                                enum:
                                  - KALSHI
                                example: KALSHI
                              event_ticker:
                                type: string
                                example: KXNFLGAME-25AUG16ARIDEN
                              market_tickers:
                                type: array
                                items:
                                  type: string
                                example:
                                  - KXNFLGAME-25AUG16ARIDEN-ARI
                                  - KXNFLGAME-25AUG16ARIDEN-DEN
                            required:
                              - platform
                              - event_ticker
                              - market_tickers
                          - type: object
                            description: Polymarket market
                            properties:
                              platform:
                                type: string
                                enum:
                                  - POLYMARKET
                                example: POLYMARKET
                              market_slug:
                                type: string
                                example: nfl-ari-den-2025-08-16
                              token_ids:
                                type: array
                                items:
                                  type: string
                                example:
                                  - >-
                                    34541522652444763571858406546623861155130750437169507355470933750634189084033
                                  - >-
                                    104612081187206848956763018128517335758189185749897027211060738913329108425255
                            required:
                              - platform
                              - market_slug
                              - token_ids
                    example:
                      nfl-ari-den-2025-08-16:
                        - platform: KALSHI
                          event_ticker: KXNFLGAME-25AUG16ARIDEN
                          market_tickers:
                            - KXNFLGAME-25AUG16ARIDEN-ARI
                            - KXNFLGAME-25AUG16ARIDEN-DEN
                        - platform: POLYMARKET
                          market_slug: nfl-ari-den-2025-08-16
                          token_ids:
                            - >-
                              34541522652444763571858406546623861155130750437169507355470933750634189084033
                            - >-
                              104612081187206848956763018128517335758189185749897027211060738913329108425255
                      nfl-dal-phi-2025-09-04:
                        - platform: KALSHI
                          event_ticker: KXNFLGAME-25SEP04DALPHI
                          market_tickers:
                            - KXNFLGAME-25SEP04DALPHI-DAL
                            - KXNFLGAME-25SEP04DALPHI-PHI
        '400':
          description: Bad Request - Missing or invalid parameters
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Missing required parameter
                  message:
                    type: string
                    example: >-
                      At least one polymarket_market_slug or kalshi_event_ticker
                      is required
        '404':
          description: Not Found - No matching markets found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Not found
                  message:
                    type: string
                    example: No matching markets found for the provided parameters
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key
      description: Your AIsa API key as a Bearer token.

````