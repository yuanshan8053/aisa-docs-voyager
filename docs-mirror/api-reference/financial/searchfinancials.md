> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Stock Screener

> Stock Screener



## OpenAPI

````yaml openapi/openapi-financial.json POST /financials/search/screener
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
  /financials/search/screener:
    post:
      tags:
        - Financials
        - Search
      summary: Search financial statements
      description: >-
        Search for stocks by filtering across financial metrics from income
        statements, balance sheets, and cash flow statements.
      operationId: stockScreener
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SearchFiltersRequest'
      responses:
        '200':
          description: Successful search response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FinancialsSearchResponse'
        '400':
          $ref: '#/components/responses/BadRequestError'
        '401':
          $ref: '#/components/responses/UnauthorizedError'
        '402':
          $ref: '#/components/responses/PaymentRequiredError'
        '404':
          $ref: '#/components/responses/NotFoundError'
      security:
        - bearerAuth: []
components:
  schemas:
    SearchFiltersRequest:
      type: object
      required:
        - filters
      properties:
        period:
          type: string
          enum:
            - annual
            - quarterly
            - ttm
          default: ttm
          description: The time period for the financial data.
        limit:
          type: integer
          minimum: 1
          maximum: 100
          default: 100
          description: The maximum number of results to return.
        order_by:
          type: string
          enum:
            - ticker
            - '-ticker'
            - report_period
            - '-report_period'
          default: ticker
          description: >-
            The field to order the results by.  Use -field to order in
            descending order.
        currency:
          type: string
          enum:
            - USD
            - EUR
            - GBP
            - JPY
            - CHF
            - AUD
            - CAD
            - SEK
          description: The currency of the financial data.
        historical:
          type: boolean
          default: false
          description: Whether to return historical financial data.
        filters:
          type: array
          items:
            type: object
            required:
              - field
              - operator
              - value
            properties:
              field:
                type: string
                description: >-
                  The criteria to filter on.  For financial metric fields, use
                  'gt', 'lt', 'gte', 'lte', 'eq' operators.  For 'ticker' and
                  'cik' fields, use the 'in' operator to filter against multiple
                  values.
              operator:
                type: string
                enum:
                  - gt
                  - lt
                  - gte
                  - lte
                  - eq
                  - in
                description: >-
                  The comparison operator. The 'in' operator can only be used
                  with a field value of 'ticker' or 'cik' and lets you filter
                  against multiple values.
              value:
                oneOf:
                  - type: number
                    description: >-
                      The value to compare against for single-value operators
                      (gt, lt, gte, lte, eq)
                  - type: array
                    items:
                      type: string
                    description: >-
                      Array of ticker or cik values to compare against when
                      using the 'in' operator
          minItems: 1
          description: An array of filter objects to apply to the search.
    FinancialsSearchResponse:
      type: object
      properties:
        search_results:
          type: array
          items:
            type: object
            properties:
              ticker:
                type: string
                description: The ticker symbol of the company.
              report_period:
                type: string
                format: date
                description: The reporting period of the financial data.
              period:
                type: string
                enum:
                  - annual
                  - quarterly
                  - ttm
                description: The time period of the financial data.
              currency:
                type: string
                description: The currency of the financial data.
            additionalProperties:
              type: string
              description: Additional financial metrics based on the search criteria.
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