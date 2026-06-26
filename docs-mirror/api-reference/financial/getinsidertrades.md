> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Insider Trades (by ticker)

> Get insider trades



## OpenAPI

````yaml openapi/openapi-financial.json GET /insider-trades
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
  /insider-trades:
    get:
      tags:
        - Insider Trades
      summary: Get insider trades
      description: >-
        Get insider trades like buys and sells for a ticker by a company
        insider.
      operationId: getInsiderTrades
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol of the company.
          required: true
          schema:
            type: string
        - name: limit
          in: query
          description: 'The maximum number of transactions to return (default: 10).'
          required: false
          schema:
            type: integer
            default: 10
        - name: name
          in: query
          description: >-
            Filter by insider name (e.g., 'Jen Hsun Huang'). Use the
            /insider-trades/names endpoint to get available names for a ticker.
          required: false
          schema:
            type: string
        - name: transaction_type
          in: query
          description: >-
            Filter by transaction type (e.g., 'Open market sale', 'Gift'). Use
            the /insider-trades/transaction-types endpoint to get available
            types.
          required: false
          schema:
            type: string
        - name: filing_date
          in: query
          description: Filter by exact filing date in YYYY-MM-DD format.
          required: false
          schema:
            type: string
            format: date
        - name: filing_date_gte
          in: query
          description: >-
            Filter by filing date greater than or equal to this date
            (YYYY-MM-DD).
          required: false
          schema:
            type: string
            format: date
        - name: filing_date_lte
          in: query
          description: Filter by filing date less than or equal to this date (YYYY-MM-DD).
          required: false
          schema:
            type: string
            format: date
        - name: filing_date_gt
          in: query
          description: Filter by filing date greater than this date (YYYY-MM-DD).
          required: false
          schema:
            type: string
            format: date
        - name: filing_date_lt
          in: query
          description: Filter by filing date less than this date (YYYY-MM-DD).
          required: false
          schema:
            type: string
            format: date
      responses:
        '200':
          description: Insider trades response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InsiderTradesResponse'
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
    InsiderTradesResponse:
      type: object
      properties:
        insider_trades:
          type: array
          items:
            $ref: '#/components/schemas/InsiderTrade'
    InsiderTrade:
      type: object
      properties:
        ticker:
          type: string
          description: The ticker symbol of the company.
        issuer:
          type: string
          description: The name of the issuing company.
        name:
          type: string
          description: The name of the insider.
        title:
          type: string
          description: The title of the insider.
        is_board_director:
          type: boolean
          description: Whether the insider is a board director.
        transaction_date:
          type: string
          format: date
          description: The date of the transaction.
        transaction_shares:
          type: number
          description: The number of shares involved in the transaction.
        transaction_price_per_share:
          type: number
          description: The price per share in the transaction.
        transaction_value:
          type: number
          description: The total value of the transaction.
        shares_owned_before_transaction:
          type: number
          description: The number of shares owned before the transaction.
        shares_owned_after_transaction:
          type: number
          description: The number of shares owned after the transaction.
        security_title:
          type: string
          description: The title of the security involved in the transaction.
        filing_date:
          type: string
          format: date
          description: The date the transaction was filed.
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