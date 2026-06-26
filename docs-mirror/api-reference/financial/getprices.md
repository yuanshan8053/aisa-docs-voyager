> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Historical Prices

> Get historical price data



## OpenAPI

````yaml openapi/openapi-financial.json GET /prices
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
  /prices:
    get:
      tags:
        - Market Data
      summary: Get historical stock price data
      description: Get end-of-day (EOD) historical price data for stocks.
      operationId: getPrices
      parameters:
        - name: ticker
          in: query
          description: The stock ticker symbol (e.g. AAPL, MSFT).
          required: true
          schema:
            type: string
        - name: interval
          in: query
          description: The time interval for the price data.
          required: true
          schema:
            type: string
            enum:
              - day
              - week
              - month
              - year
        - name: start_date
          in: query
          description: 'The start date for the price data (format: YYYY-MM-DD).'
          required: true
          schema:
            type: string
            format: date
        - name: end_date
          in: query
          description: 'The end date for the price data (format: YYYY-MM-DD).'
          required: true
          schema:
            type: string
            format: date
      responses:
        '200':
          description: Price data response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PricesResponse'
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
    PricesResponse:
      type: object
      properties:
        prices:
          type: array
          items:
            $ref: '#/components/schemas/Price'
        next_page_url:
          type: string
          description: The URL to the next page of results.
    Price:
      type: object
      properties:
        open:
          type: number
          description: The open price of the ticker in the given time period.
        close:
          type: number
          description: The close price of the ticker in the given time period.
        high:
          type: number
          description: The high price of the ticker in the given time period.
        low:
          type: number
          description: The low price of the ticker in the given time period.
        volume:
          type: integer
          format: number
          description: The volume of the ticker in the given time period.
        time:
          type: string
          description: The human-readable time format of the price in UTC.
        time_milliseconds:
          type: number
          description: The timestamp of the price in milliseconds since epoch.
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