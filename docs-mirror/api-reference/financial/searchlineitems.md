> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search Financials

> Search specific financial metrics



## OpenAPI

````yaml openapi/openapi-financial.json POST /financials/search/line-items
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
  /financials/search/line-items:
    post:
      tags:
        - Financial Statements
      summary: Search specific financial metrics
      description: >-
        Search for specific financial metrics across income statements, balance
        sheets, and cash flow statements for a list of tickers.
      operationId: searchLineItems
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SearchLineItemsRequest'
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
components:
  schemas:
    SearchLineItemsRequest:
      type: object
      required:
        - line_items
        - tickers
      properties:
        line_items:
          type: array
          items:
            type: string
            description: The financial metric to search for.
          minItems: 1
          description: An array of line items to apply to the search.
        tickers:
          type: array
          items:
            type: string
            description: The tickers to search for.
          minItems: 1
          description: An array of tickers to apply to the search.
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
          default: 1
          description: The maximum number of results to return.
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