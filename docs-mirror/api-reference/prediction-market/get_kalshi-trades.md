> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kalshi Trade History

> Get Kalshi Trades

Trade History fetches executed trade data for Kalshi markets with optional filtering by market ticker and time range. Returns trades with pricing for both yes and no sides, contract counts, taker side information, and timestamps. All timestamps are in seconds.

**Best for:** Analyzing trading activity on Kalshi, tracking executed trades for specific markets, monitoring real-time trade flow, building trade history datasets.

**Endpoint:** `GET /kalshi/trades`

## Example

```bash theme={null}
curl -X GET "https://api.aisa.one/apis/v1/kalshi/trades?ticker=KXNFLGAME-25NOV09PITLAC-PIT&limit=10" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

## Response

The response returns a `trades` array containing trade objects with fields such as trade ID, market ticker, contract count, yes/no prices (in both cents and dollars), taker side, and creation timestamp. A `pagination` object with `has_more` and `pagination_key` fields supports cursor-based pagination.


## OpenAPI

````yaml openapi/kalshi-openapi.json GET /kalshi/trades
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
  /kalshi/trades:
    get:
      summary: Get Kalshi Trades
      description: >-
        Fetches historical trade data for Kalshi markets with optional filtering
        by ticker and time range. Returns executed trades with pricing, volume,
        and taker side information. All timestamps are in seconds.
      operationId: get_kalshi-trades
      parameters:
        - name: ticker
          in: query
          required: false
          description: The Kalshi market ticker to filter trades
          schema:
            type: string
            example: KXNFLGAME-25NOV09PITLAC-PIT
        - name: start_time
          in: query
          required: false
          description: Start time in Unix timestamp (seconds)
          schema:
            type: integer
            example: 1762716000
        - name: end_time
          in: query
          required: false
          description: End time in Unix timestamp (seconds)
          schema:
            type: integer
            example: 1762720600
        - name: limit
          in: query
          required: false
          description: 'Maximum number of trades to return (default: 100)'
          schema:
            type: integer
            default: 100
            example: 10
        - name: pagination_key
          in: query
          required: false
          description: >-
            Base64-encoded cursor for efficient pagination. Returned in the
            previous response's pagination object.
          schema:
            type: string
            example: >-
              eyJjcmVhdGVkX3RpbWUiOiIyMDI1LTAxLTE5VDEyOjAwOjAwLjAwMFoiLCJ0cmFkZV9pZCI6IjEyMzQ1Njc4OTAiLCJ0b3RhbCI6NTAwMDB9
      responses:
        '200':
          description: Kalshi trades response with pagination
          content:
            application/json:
              schema:
                type: object
                properties:
                  trades:
                    type: array
                    description: Array of executed trades
                    items:
                      type: object
                      properties:
                        trade_id:
                          type: string
                          description: Unique identifier for the trade
                          example: 587f9eb0-1ae1-7b53-9536-fcf3fc503630
                        market_ticker:
                          type: string
                          description: The Kalshi market ticker
                          example: KXNFLGAME-25NOV09PITLAC-PIT
                        count:
                          type: integer
                          description: Number of contracts traded
                          example: 93
                        yes_price:
                          type: integer
                          description: Yes side price in cents
                          example: 1
                        no_price:
                          type: integer
                          description: No side price in cents
                          example: 99
                        yes_price_dollars:
                          type: number
                          description: Yes side price in dollars
                          example: 0.01
                        no_price_dollars:
                          type: number
                          description: No side price in dollars
                          example: 0.99
                        taker_side:
                          type: string
                          description: Which side was the taker (yes or no)
                          enum:
                            - 'yes'
                            - 'no'
                          example: 'yes'
                        created_time:
                          type: integer
                          description: Timestamp of the trade in seconds (Unix timestamp)
                          example: 1762718746
                  pagination:
                    type: object
                    properties:
                      limit:
                        type: integer
                        example: 50
                      total:
                        type: integer
                        description: Total number of trades matching the filters
                        example: 43154
                      has_more:
                        type: boolean
                        description: Whether there are more trades available
                        example: true
                      pagination_key:
                        type: string
                        description: >-
                          Base64-encoded cursor for the next page. Only present
                          when there are more results.
                        example: >-
                          eyJjcmVhdGVkX3RpbWUiOiIyMDI1LTAxLTE5VDEyOjAwOjAwLjAwMFoiLCJ0cmFkZV9pZCI6IjEyMzQ1Njc4OTAiLCJ0b3RhbCI6NTAwMDB9
        '400':
          description: Bad Request - Invalid parameters
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Invalid parameters
                  message:
                    type: string
                    example: Invalid time range or parameters
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key
      description: Your AIsa API key as a Bearer token.

````