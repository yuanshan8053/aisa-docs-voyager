> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Price Snapshot

> Real-time price snapshot for a stock — current price, day change, and day change percent.

Real-time stock price snapshot for a ticker. Returns the current price plus day-over-day change (absolute and percent).

**Best for:** Live price widgets, dashboards, triggering alerts on intraday moves, validating fills, pre-trade price sanity checks.

## Example

```bash theme={null}
curl -X GET "https://api.aisa.one/apis/v1/financial/prices/snapshot?ticker=AAPL" \
  -H "Authorization: Bearer $AISA_API_KEY"
```


## OpenAPI

````yaml openapi/openapi-financial.json GET /prices/snapshot
openapi: 3.0.1
info:
  title: Financial Datasets API
  description: >-
    Stock market API with real-time and historical financial data for 30,000+
    tickers over 30+ years. Financial statements, equity prices, insider trades,
    SEC filings, and more.
  version: 1.0.0
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT
  contact:
    name: API Support
    url: https://financialdatasets.ai/support
    email: support@financialdatasets.ai
  termsOfService: https://financialdatasets.ai/terms
servers:
  - url: https://api.aisa.one/apis/v1/financial
    description: Production server
security:
  - bearerAuth: []
tags:
  - name: Financial Statements
    description: Access to income statements, balance sheets, and cash flow statements
  - name: Market Data
    description: Real-time and historical price data
  - name: Company Information
    description: Company facts like ticker, name, and description
  - name: Earnings
    description: Earnings press releases and related data
  - name: Crypto
    description: Cryptocurrency price data and market information
  - name: News
    description: Real-time and historical news articles
  - name: SEC Filings
    description: SEC filings and regulatory documents
  - name: Insider Trades
    description: Insider trading activity and transactions
  - name: Institutional Ownership
    description: Equity holdings of investment managers
  - name: Financial Metrics
    description: Financial ratios, metrics, and key performance indicators
paths:
  /prices/snapshot:
    get:
      tags:
        - Market Data
      summary: Price Snapshot (Real-Time)
      description: >-
        Get the real-time price snapshot for a stock, including the current
        price, day change, and day change percent.
      operationId: getPriceSnapshot
      parameters:
        - name: ticker
          in: query
          description: The stock ticker symbol (e.g. AAPL, MSFT).
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Price snapshot response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PriceSnapshotResponse'
        '400':
          $ref: '#/components/responses/BadRequestError'
        '401':
          $ref: '#/components/responses/UnauthorizedError'
        '402':
          $ref: '#/components/responses/PaymentRequiredError'
        '404':
          $ref: '#/components/responses/NotFoundError'
components:
  schemas:
    PriceSnapshotResponse:
      type: object
      properties:
        snapshot:
          $ref: '#/components/schemas/PriceSnapshot'
    PriceSnapshot:
      type: object
      properties:
        price:
          type: number
          description: The current price of the stock.
        ticker:
          type: string
          description: The ticker symbol.
        day_change:
          type: number
          description: The price change since the previous trading day's close.
        day_change_percent:
          type: number
          description: The percentage price change since the previous trading day's close.
        market_cap:
          type: number
          description: The market capitalization of the company.
        time:
          type: string
          description: The timestamp of the price snapshot in human-readable format in UTC.
        time_milliseconds:
          type: number
          description: The timestamp of the price snapshot in milliseconds since epoch.
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: A short error message.
        message:
          type: string
          description: A more detailed error message.
  responses:
    BadRequestError:
      description: Bad request
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            error: Bad Request
            message: Invalid request parameters
    UnauthorizedError:
      description: Unauthorized
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            error: Unauthorized
            message: Invalid API key provided
    PaymentRequiredError:
      description: The request requires a paid subscription
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            error: Payment Required
            message: >-
              This endpoint requires a paid subscription. Please upgrade your
              plan.
    NotFoundError:
      description: The specified resource was not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
          example:
            error: Not Found
            message: Ticker XXXX not found
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````