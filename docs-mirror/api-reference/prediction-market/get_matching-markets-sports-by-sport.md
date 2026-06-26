> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sport by Date

> Get Matching Markets for Sports by Sport and Date

Sport by Date finds equivalent markets across different prediction market platforms (Polymarket, Kalshi, etc.) for all sports events of a given sport on a specific date. Supports NFL, MLB, NBA, NHL, college football, college basketball, PGA, and tennis.

**Best for:** Discovering all cross-platform markets for a game day, building daily sports betting dashboards, comparing odds across platforms by date.

**Endpoint:** `GET /matching-markets/sports/{sport}`

> **Note:** Supported sport abbreviations: `nfl` (Football), `mlb` (Baseball), `cfb` (College Football), `nba` (Basketball), `nhl` (Hockey), `cbb` (College Basketball), `pga` (Golf), `tennis` (Tennis).

## Example

```bash theme={null}
curl -X GET "https://api.aisa.one/apis/v1/matching-markets/sports/nfl?date=2025-08-16" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

## Response

The response returns a `markets` object keyed by event identifier, where each key maps to an array of platform-specific market objects. Kalshi objects include `platform`, `event_ticker`, and `market_tickers`. Polymarket objects include `platform`, `market_slug`, and `token_ids`. The response also includes the `sport` and `date` fields echoing the request parameters.


## OpenAPI

````yaml openapi/matching-markets-openapi.json GET /matching-markets/sports/{sport}
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
  /matching-markets/sports/{sport}:
    parameters:
      - name: sport
        in: path
        required: true
        description: |-
          The sport to find matching markets for.

          Sport abbreviations:
          - nfl = Football
          - mlb = Baseball
          - cfb = College Football
          - nba = Basketball
          - nhl = Hockey
          - cbb = College Basketball
          - pga = Golf
          - tennis = Tennis
        schema:
          type: string
          enum:
            - nfl
            - mlb
            - cfb
            - nba
            - nhl
            - cbb
            - pga
            - tennis
          example: nfl
    get:
      summary: Get Matching Markets for Sports by Sport and Date
      description: >-
        Find equivalent markets across different prediction market platforms
        (Polymarket, Kalshi, etc.) for sports events by sport and date.
      operationId: get_matching-markets-sports-by-sport
      parameters:
        - name: date
          in: query
          required: true
          description: The date to find matching markets for in YYYY-MM-DD format
          schema:
            type: string
            pattern: ^\d{4}-\d{2}-\d{2}$
            example: '2025-08-16'
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
                  sport:
                    type: string
                    example: nfl
                  date:
                    type: string
                    example: '2025-08-16'
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
                    example: date parameter is required
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key
      description: Your AIsa API key as a Bearer token.

````