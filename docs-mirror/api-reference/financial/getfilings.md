> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Filings

> Get SEC filings



## OpenAPI

````yaml openapi/openapi-financial.json GET /filings
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
  /filings:
    get:
      tags:
        - SEC Filings
      summary: Get SEC filings
      description: Get SEC filings for a company.
      operationId: getFilings
      parameters:
        - name: cik
          in: query
          description: The Central Index Key (CIK) of the company.
          required: false
          schema:
            type: string
        - name: ticker
          in: query
          description: The ticker symbol.
          required: false
          schema:
            type: string
        - name: filing_type
          in: query
          description: >-
            Filter by one or more filing types. Repeat the query parameter to
            pass multiple values (e.g. filing_type=10-Q&filing_type=10-K).
          required: false
          schema:
            type: array
            items:
              type: string
              enum:
                - 10-K
                - 10-Q
                - 8-K
                - 20-F
                - 6-K
          style: form
          explode: true
        - name: limit
          in: query
          description: 'The maximum number of filings to return (default: 10).'
          required: false
          schema:
            type: integer
            minimum: 1
            default: 10
      responses:
        '200':
          description: SEC filings response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FilingsResponse'
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
    FilingsResponse:
      type: object
      properties:
        filings:
          type: array
          items:
            $ref: '#/components/schemas/Filing'
    Filing:
      type: object
      properties:
        cik:
          type: integer
          description: The Central Index Key (CIK) of the company.
        accession_number:
          type: string
          description: The accession number of the filing.
        filing_type:
          type: string
          description: The type of the SEC filing (e.g., 10-Q, 8-K).
        report_date:
          type: string
          format: date
          description: The date of the report.
        ticker:
          type: string
          description: The ticker symbol.
        url:
          type: string
          format: uri
          description: The URL of the SEC filing.
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