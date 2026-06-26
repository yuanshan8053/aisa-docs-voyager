> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Candlesticks

> Historical OHLC candlestick data for a Polymarket market, fetched by condition ID as a query parameter.

Fetches historical OHLC (open, high, low, close) candlestick data for a Polymarket market identified by its `condition_id`. Data is returned over a specified time range at configurable intervals (1-minute, 1-hour, or 1-day). Each candlestick includes price data, volume, open interest, and bid/ask spreads.

**Best for:** Building price charts, technical analysis, tracking market volatility, visualizing price movements over time.

**Endpoint:** `GET /polymarket/candlesticks` — `condition_id` is a **query parameter**, not a path parameter.

> **Note:** There are range limits per interval: 1-minute intervals support a maximum range of 1 week, 1-hour intervals support 1 month, and 1-day intervals support 1 year.

## Example

```bash theme={null}
curl -X GET "https://api.aisa.one/apis/v1/polymarket/candlesticks?condition_id=0x1234abcd5678ef90&start_time=1640995200&end_time=1672531200&interval=1440" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

## Response

The response returns a `candlesticks` array where each element is a tuple of a candlestick data array and token metadata. Each candlestick data object contains OHLC prices (in both raw and dollar values), volume, open interest, and yes-side bid/ask spreads. The token metadata includes the token ID and outcome label (e.g., "Yes", "No").


## OpenAPI

````yaml openapi/polymarket-openapi.json GET /polymarket/candlesticks
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
  /polymarket/candlesticks:
    parameters:
      - name: condition_id
        in: path
        required: true
        schema:
          type: string
    get:
      summary: Get Candlesticks
      description: >-
        Fetches historical candlestick data for a market identified by
        `condition_id`, over a specified interval.
      operationId: get_polymarket-candlesticks
      parameters:
        - name: condition_id
          in: query
          required: true
          description: Polymarket condition ID for the market.
          schema:
            type: string
          example: '0x1234abcd5678ef90'
        - name: start_time
          in: query
          required: true
          description: Unix timestamp (in seconds) for start of time range
          schema:
            type: integer
            example: 1640995200
        - name: end_time
          in: query
          required: true
          description: Unix timestamp (in seconds) for end of time range
          schema:
            type: integer
            example: 1672531200
        - name: interval
          in: query
          required: false
          description: |+
            Interval length: 1 = 1m, 60 = 1h, 1440 = 1d. Defaults to 1m. 

            ⚠️ **Note:** There are range limits for `interval` — specifically:
            - `1` (1m): max range **1 week**
            - `60` (1h): max range **1 month**
            - `1440` (1d): max range **1 year**

          schema:
            type: integer
            enum:
              - 1
              - 60
              - 1440
            default: 1
      responses:
        '200':
          description: Candlestick response
          content:
            application/json:
              schema:
                type: object
                properties:
                  candlesticks:
                    type: array
                    description: >-
                      Array of market candlestick data, where each element is a
                      tuple containing candlestick data array and token metadata
                    items:
                      type: array
                      description: Tuple of [candlestick_data_array, token_metadata]
                      minItems: 2
                      maxItems: 2
                      items:
                        oneOf:
                          - type: array
                            description: Candlestick data array
                            items:
                              type: object
                          - type: object
                            description: Token metadata
                            properties:
                              token_id:
                                type: string
                              side:
                                type: string
                                description: >-
                                  The outcome label for this token (e.g., 'Yes',
                                  'No', 'Up', 'Down', 'Over', 'Under', or team
                                  names for sports markets)
                      example:
                        - - end_period_ts: 1727827200
                            open_interest: 8456498
                            price:
                              open: 0
                              high: 0
                              low: 0
                              close: 0
                              open_dollars: '0.0049'
                              high_dollars: '0.0049'
                              low_dollars: '0.0048'
                              close_dollars: '0.0048'
                              mean: 0
                              mean_dollars: '0.0049'
                              previous: 0
                              previous_dollars: '0.0049'
                            volume: 8456498
                            yes_ask:
                              open: 0.00489
                              close: 0.0048200000000000005
                              high: 0.00491
                              low: 0.0048
                              open_dollars: '0.0049'
                              close_dollars: '0.0048'
                              high_dollars: '0.0049'
                              low_dollars: '0.0048'
                            yes_bid:
                              open: 0.00489
                              close: 0.004829999990880811
                              high: 0.004910000000138527
                              low: 0.0048
                              open_dollars: '0.0049'
                              close_dollars: '0.0048'
                              high_dollars: '0.0049'
                              low_dollars: '0.0048'
                        - token_id: >-
                            21742633143463906290569050155826241533067272736897614950488156847949938836455
                          side: 'Yes'
        '400':
          description: Bad Request - Invalid parameters
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Missing required query parameters
                  required:
                    type: string
                    example: start_time, end_time
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key
      description: Your AIsa API key as a Bearer token.

````