> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Earnings Press Releases

> Get earnings press releases



## OpenAPI

````yaml openapi/openapi-financial.json GET /earnings/press-releases
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
  /earnings/press-releases:
    get:
      tags:
        - Earnings
      summary: Get earnings press releases
      description: Get earnings press releases for a ticker.
      operationId: getEarningsPressReleases
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Earnings press releases response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PressReleasesResponse'
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
    PressReleasesResponse:
      type: object
      properties:
        press_releases:
          type: array
          items:
            $ref: '#/components/schemas/PressRelease'
    PressRelease:
      type: object
      properties:
        ticker:
          type: string
          description: The ticker symbol of the company.
        title:
          type: string
          description: The title of the press release.
        url:
          type: string
          format: uri
          description: The URL of the press release.
        date:
          type: string
          format: date
          description: The date the press release was published.
        text:
          type: string
          description: The full text of the press release.
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