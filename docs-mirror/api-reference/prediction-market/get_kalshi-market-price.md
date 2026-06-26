> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kalshi Market Price

> Get Kalshi Market Price

Market Price fetches the current or historical price for a Kalshi market identified by its market ticker. Returns prices for both the yes and no sides. When the `at_time` parameter is omitted, it returns the most real-time price available. When `at_time` is provided, it returns the historical market price at that specific timestamp.

**Best for:** Real-time price lookups, historical price snapshots, tracking both sides of a binary market, building price charts.

**Endpoint:** `GET /kalshi/market-price/{market_ticker}`

## Example

```bash theme={null}
curl -X GET "https://api.aisa.one/apis/v1/kalshi/market-price/KXNFLGAME-25AUG16ARIDEN-ARI?at_time=1762164600" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

## Response

The response returns a `yes` object and a `no` object, each containing a `price` field (a number between 0 and 1 representing the dollar price) and an `at_time` field (Unix timestamp in seconds) indicating the point in time for which the price was fetched.


## OpenAPI

````yaml openapi/kalshi-openapi.json GET /kalshi/market-price/{market_ticker}
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
  /kalshi/market-price/{market_ticker}:
    parameters:
      - name: market_ticker
        in: path
        required: true
        description: The market ticker for the Kalshi market
        schema:
          type: string
          example: KXNFLGAME-25AUG16ARIDEN-ARI
    get:
      summary: Get Kalshi Market Price
      description: >-
        Fetches the current market price for a Kalshi market by `market_ticker`.
        When `at_time` is not provided, returns the most real-time price
        available. When `at_time` is provided, returns the historical market
        price at that specific timestamp. Returns prices for both yes and no
        sides.


        **Example Request (with historical timestamp):**

        ```bash

        curl
        'https://api.domeapi.io/v1/kalshi/market-price/KXNFLGAME-25AUG16ARIDEN-ARI?at_time=1762164600'
        \
          -H 'Authorization: Bearer YOUR_TOKEN'
        ```


        **Example Request (real-time price):**

        ```bash

        curl
        'https://api.domeapi.io/v1/kalshi/market-price/KXNFLGAME-25AUG16ARIDEN-ARI'
        \
          -H 'Authorization: Bearer YOUR_TOKEN'
        ```
      operationId: get_kalshi-market-price
      parameters:
        - name: at_time
          in: query
          required: false
          description: >-
            Optional Unix timestamp (in seconds) to fetch a historical market
            price. If not provided, returns the most real-time price available.
          schema:
            type: integer
            example: 1762164600
      responses:
        '200':
          description: Market price response
          content:
            application/json:
              schema:
                type: object
                properties:
                  'yes':
                    type: object
                    description: Yes side price information
                    properties:
                      price:
                        type: number
                        description: The yes side price in dollars (between 0 and 1)
                        example: 0.75
                      at_time:
                        type: integer
                        description: >-
                          The timestamp for which the price was fetched (Unix
                          timestamp in seconds)
                        example: 1762164600
                    required:
                      - price
                      - at_time
                  'no':
                    type: object
                    description: No side price information
                    properties:
                      price:
                        type: number
                        description: The no side price in dollars (between 0 and 1)
                        example: 0.25
                      at_time:
                        type: integer
                        description: >-
                          The timestamp for which the price was fetched (Unix
                          timestamp in seconds)
                        example: 1762164600
                    required:
                      - price
                      - at_time
                required:
                  - 'yes'
                  - 'no'
              examples:
                with_at_time:
                  summary: Historical price lookup
                  description: Response when `at_time` parameter is provided
                  value:
                    'yes':
                      price: 0.75
                      at_time: 1762164600
                    'no':
                      price: 0.25
                      at_time: 1762164600
                real_time:
                  summary: Real-time price lookup
                  description: >-
                    Response when `at_time` parameter is omitted (most recent
                    price)
                  value:
                    'yes':
                      price: 0.82
                      at_time: 1757008834
                    'no':
                      price: 0.18
                      at_time: 1757008834
        '400':
          description: Bad Request - Invalid parameters
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Invalid at_time parameter
                  message:
                    type: string
                    example: at_time must be a valid Unix timestamp in seconds
        '404':
          description: Not Found - Market not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Not Found
                  message:
                    type: string
                    example: >-
                      No price data found for market_ticker
                      KXNFLGAME-25AUG16ARIDEN-ARI
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key
      description: Your AIsa API key as a Bearer token.

````