> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kalshi Orderbook History

> Get Kalshi Orderbook History

Orderbook History fetches historical orderbook snapshots for a specific Kalshi market identified by its ticker over a specified time range. If no start and end times are provided, it returns the latest orderbook snapshot. Returns snapshots of the order book including yes/no bids and asks with prices in both cents and dollars.

**Best for:** Analyzing market depth on Kalshi, tracking bid/ask spread over time, building orderbook visualizations, monitoring liquidity.

**Endpoint:** `GET /kalshi/orderbooks`

> **Note:** All timestamps are in milliseconds. Orderbook data has history starting from October 29th, 2025. When fetching the latest orderbook (without start/end times), the `limit` parameter is ignored.

## Example

```bash theme={null}
curl -X GET "https://api.aisa.one/apis/v1/kalshi/orderbooks?ticker=KXNFLGAME-25AUG16ARIDEN-ARI&start_time=1760470000000&end_time=1760480000000&limit=100" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

## Response

The response returns a `snapshots` array containing orderbook snapshot objects, each with an `orderbook` object containing `yes`, `no`, `yes_dollars`, and `no_dollars` arrays of price-quantity pairs, along with a `timestamp` (in milliseconds) and `ticker`. A `pagination` object with `has_more` and `paginationKey` fields supports cursor-based pagination.


## OpenAPI

````yaml openapi/kalshi-openapi.json GET /kalshi/orderbooks
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
  /kalshi/orderbooks:
    get:
      summary: Get Kalshi Orderbook History
      description: >-
        Fetches historical orderbook snapshots for a specific Kalshi market
        (ticker) over a specified time range. If no start_time and end_time are
        provided, returns the latest orderbook snapshot for the market. Returns
        snapshots of the order book including yes/no bids and asks with prices
        in both cents and dollars. All timestamps are in milliseconds. Orderbook
        data has history starting from October 29th, 2025. Note: When fetching
        the latest orderbook (without start/end times), the limit parameter is
        ignored.
      operationId: get_kalshi-orderbooks
      parameters:
        - name: ticker
          in: query
          required: true
          description: The Kalshi market ticker
          schema:
            type: string
            example: KXNFLGAME-25AUG16ARIDEN-ARI
        - name: start_time
          in: query
          required: false
          description: >-
            Start time in Unix timestamp (milliseconds). Optional - if not
            provided along with end_time, returns the latest orderbook snapshot.
          schema:
            type: integer
            example: 1760470000000
        - name: end_time
          in: query
          required: false
          description: >-
            End time in Unix timestamp (milliseconds). Optional - if not
            provided along with start_time, returns the latest orderbook
            snapshot.
          schema:
            type: integer
            example: 1760480000000
        - name: limit
          in: query
          required: false
          description: >-
            Maximum number of snapshots to return (default: 100, max: 200).
            Ignored when fetching the latest orderbook without start_time and
            end_time.
          schema:
            type: integer
            default: 100
            maximum: 200
            example: 100
        - name: paginationKey
          in: query
          required: false
          description: >-
            Base64-encoded cursor for efficient pagination. Returned in the
            previous response's pagination object.
          schema:
            type: string
            example: >-
              eyJ0aW1lc3RhbXAiOjE3NjA0NzAwMDAwMDAsInRpY2tlciI6IktYTkZMR0FNRS0yNUFVRzE2QVJJREVOLUFSSSIsInRvdGFsIjoxMDB9
      responses:
        '200':
          description: Kalshi orderbook history response
          content:
            application/json:
              schema:
                type: object
                properties:
                  snapshots:
                    type: array
                    description: Array of orderbook snapshots at different points in time
                    items:
                      type: object
                      properties:
                        orderbook:
                          type: object
                          properties:
                            'yes':
                              type: array
                              description: Yes side orders with prices in cents
                              items:
                                type: array
                                description: '[price_in_cents, contract_count]'
                                items:
                                  type: number
                                minItems: 2
                                maxItems: 2
                                example:
                                  - 75
                                  - 100
                            'no':
                              type: array
                              description: No side orders with prices in cents
                              items:
                                type: array
                                description: '[price_in_cents, contract_count]'
                                items:
                                  type: number
                                minItems: 2
                                maxItems: 2
                                example:
                                  - 25
                                  - 100
                            yes_dollars:
                              type: array
                              description: Yes side orders with prices in dollars
                              items:
                                type: array
                                description: '[price_as_dollar_string, contract_count]'
                                minItems: 2
                                maxItems: 2
                                items:
                                  oneOf:
                                    - type: string
                                    - type: number
                                example:
                                  - '0.75'
                                  - 100
                            no_dollars:
                              type: array
                              description: No side orders with prices in dollars
                              items:
                                type: array
                                description: '[price_as_dollar_string, contract_count]'
                                minItems: 2
                                maxItems: 2
                                items:
                                  oneOf:
                                    - type: string
                                    - type: number
                                example:
                                  - '0.25'
                                  - 100
                        timestamp:
                          type: integer
                          description: Timestamp of the snapshot in milliseconds
                          example: 1760471849407
                        ticker:
                          type: string
                          description: The Kalshi market ticker
                          example: KXNFLGAME-25AUG16ARIDEN-ARI
                  pagination:
                    type: object
                    properties:
                      limit:
                        type: integer
                        example: 100
                      count:
                        type: integer
                        description: Number of snapshots returned
                        example: 4
                      paginationKey:
                        type: string
                        description: >-
                          Base64-encoded cursor for fetching the next page of
                          results. Only present when has_more is true.
                        example: >-
                          eyJ0aW1lc3RhbXAiOjE3NjA0NzAwMDAwMDAsInRpY2tlciI6IktYTkZMR0FNRS0yNUFVRzE2QVJJREVOLUFSSSIsInRvdGFsIjoxMDB9
                      has_more:
                        type: boolean
                        description: Whether there are more snapshots available
                        example: false
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
                    example: ticker, start_time, and end_time are required
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key
      description: Your AIsa API key as a Bearer token.

````