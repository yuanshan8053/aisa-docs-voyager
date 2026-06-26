> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wallet Profit-and-Loss

> Realized profit and loss for a Polymarket wallet address over a specified time range and granularity.

Fetches the realized PnL for a specific Polymarket wallet address over a specified time range and granularity. This tracks realized gains only — from either confirmed sells or redeems. A gain or loss is not realized until a finished market is redeemed.

**Best for:** Tracking wallet profitability, analyzing trading performance over time, building PnL dashboards, comparing realized returns across periods.

**Endpoint:** `GET /polymarket/wallet/pnl` — `wallet_address` is a **query parameter**, not a path parameter.

> **Note:** This returns realized PnL only, which differs from Polymarket's dashboard that shows historical unrealized PnL.

## Example

```bash theme={null}
curl -X GET "https://api.aisa.one/apis/v1/polymarket/wallet/pnl?wallet_address=0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b&granularity=day&start_time=1726857600&end_time=1758316829" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

## Response

The response returns the `granularity`, `start_time`, `end_time`, and `wallet_address` fields, along with a `pnl_over_time` array. Each element in the array contains a `timestamp` and `pnl_to_date` value representing the cumulative realized profit and loss at that point in time.


## OpenAPI

````yaml openapi/polymarket-openapi.json GET /polymarket/wallet/pnl
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
  /polymarket/wallet/pnl:
    parameters:
      - name: wallet_address
        in: path
        required: true
        schema:
          type: string
          pattern: ^0x[0-9a-fA-F]{40}$
          example: '0x1234567890abcdef1234567890abcdef12345678'
    get:
      summary: Get Wallet PnL
      description: >-
        Fetches the REALIZED profit and loss (PnL) for a specific wallet address
        over a specified time range and granularity. **Note:** This will differ
        to what you see on Polymarket's dashboard since Polymarket showcases
        historical unrealized PnL. This API tracks realized gains only - from
        either confirmed sells or redeems. We do not realize a gain/loss until a
        finished market is redeemed.
      operationId: get_polymarket-wallet-pnl
      parameters:
        - name: wallet_address
          in: query
          required: true
          description: Polymarket wallet address (0x-prefixed).
          schema:
            type: string
          example: '0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b'
        - name: granularity
          in: query
          required: true
          schema:
            type: string
            enum:
              - day
              - week
              - month
              - year
              - all
            example: day
        - name: start_time
          in: query
          required: false
          description: Defaults to first day of first trade if not provided.
          schema:
            type: integer
            example: 1726857600
        - name: end_time
          in: query
          required: false
          description: Defaults to the current date if not provided.
          schema:
            type: integer
            example: 1758316829
      responses:
        '200':
          description: PnL response
          content:
            application/json:
              schema:
                type: object
                properties:
                  granularity:
                    type: string
                    example: day
                  start_time:
                    type: integer
                    example: 1726857600
                  end_time:
                    type: integer
                    example: 1758316829
                  wallet_address:
                    type: string
                    example: '0x7c3db723f1d4d8cb9c550095203b686cb11e5c6b'
                  pnl_over_time:
                    type: array
                    items:
                      type: object
                      properties:
                        timestamp:
                          type: integer
                          example: 1726857600
                        pnl_to_date:
                          type: number
                          example: 2001
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: BAD_REQUEST
                  message:
                    type: string
                    example: Invalid or missing parameters.
        '503':
          description: Internal Server Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: INTERNAL_SERVER_ERROR
                  message:
                    type: string
                    example: Internal Server Error. Dome Admins contacted.
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key
      description: Your AIsa API key as a Bearer token.

````