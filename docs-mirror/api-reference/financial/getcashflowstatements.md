> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cash Flow Statements

> Get cash flow statements



## OpenAPI

````yaml openapi/openapi-financial.json GET /financials/cash-flow-statements
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
  /financials/cash-flow-statements:
    get:
      tags:
        - Financial Statements
      summary: Get cash flow statements
      description: Get cash flow statements for a ticker.
      operationId: getCashFlowStatements
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol. Required if cik is not provided.
          required: false
          schema:
            type: string
        - name: period
          in: query
          description: The time period of the cash flow statements.
          required: true
          schema:
            type: string
            enum:
              - annual
              - quarterly
              - ttm
        - name: limit
          in: query
          description: The maximum number of cash flow statements to return.
          schema:
            type: integer
            format: int32
        - name: cik
          in: query
          description: The Central Index Key (CIK) of the company.
          required: false
          schema:
            type: string
        - $ref: '#/components/parameters/ReportPeriod'
        - $ref: '#/components/parameters/ReportPeriodGte'
        - $ref: '#/components/parameters/ReportPeriodLte'
        - $ref: '#/components/parameters/ReportPeriodGt'
        - $ref: '#/components/parameters/ReportPeriodLt'
      responses:
        '200':
          description: Cash flow statements response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CashFlowStatementResponse'
        '400':
          $ref: '#/components/responses/BadRequestError'
        '401':
          $ref: '#/components/responses/UnauthorizedError'
        '402':
          $ref: '#/components/responses/PaymentRequiredError'
        '404':
          $ref: '#/components/responses/NotFoundError'
components:
  parameters:
    ReportPeriod:
      name: report_period
      in: query
      description: Filter by exact report period date in YYYY-MM-DD format.
      required: false
      schema:
        type: string
        format: date
    ReportPeriodGte:
      name: report_period_gte
      in: query
      description: >-
        Filter by report period greater than or equal to date in YYYY-MM-DD
        format.
      required: false
      schema:
        type: string
        format: date
    ReportPeriodLte:
      name: report_period_lte
      in: query
      description: Filter by report period less than or equal to date in YYYY-MM-DD format.
      required: false
      schema:
        type: string
        format: date
    ReportPeriodGt:
      name: report_period_gt
      in: query
      description: Filter by report period greater than date in YYYY-MM-DD format.
      required: false
      schema:
        type: string
        format: date
    ReportPeriodLt:
      name: report_period_lt
      in: query
      description: Filter by report period less than date in YYYY-MM-DD format.
      required: false
      schema:
        type: string
        format: date
  schemas:
    CashFlowStatementResponse:
      type: object
      properties:
        cash_flow_statements:
          type: array
          items:
            $ref: '#/components/schemas/CashFlowStatement'
    CashFlowStatement:
      type: object
      properties:
        ticker:
          type: string
          description: The ticker symbol.
        report_period:
          type: string
          format: date
          description: The reporting period of the cash flow statement.
        fiscal_period:
          type: string
          description: The fiscal period of the cash flow statement.
        period:
          type: string
          enum:
            - quarterly
            - ttm
            - annual
          description: The time period of the cash flow statement.
        currency:
          type: string
          description: The currency in which the financial data is reported.
        net_income:
          type: number
          nullable: false
          description: The net income of the company.
        depreciation_and_amortization:
          type: number
          nullable: false
          description: The depreciation and amortization of the company.
        share_based_compensation:
          type: number
          nullable: false
          description: The share-based compensation of the company.
        net_cash_flow_from_operations:
          type: number
          nullable: false
          description: The net cash flow from operations of the company.
        capital_expenditure:
          type: number
          nullable: false
          description: The capital expenditure of the company.
        business_acquisitions_and_disposals:
          type: number
          nullable: false
          description: The business acquisitions and disposals of the company.
        investment_acquisitions_and_disposals:
          type: number
          nullable: false
          description: The investment acquisitions and disposals of the company.
        net_cash_flow_from_investing:
          type: number
          nullable: false
          description: The net cash flow from investing of the company.
        issuance_or_repayment_of_debt_securities:
          type: number
          nullable: false
          description: The issuance or repayment of debt securities of the company.
        issuance_or_purchase_of_equity_shares:
          type: number
          nullable: false
          description: The issuance or purchase of equity shares of the company.
        dividends_and_other_cash_distributions:
          type: number
          nullable: false
          description: The dividends and other cash distributions of the company.
        net_cash_flow_from_financing:
          type: number
          nullable: false
          description: The net cash flow from financing of the company.
        change_in_cash_and_equivalents:
          type: number
          nullable: false
          description: The change in cash and equivalents of the company.
        effect_of_exchange_rate_changes:
          type: number
          nullable: false
          description: The effect of exchange rate changes of the company.
        ending_cash_balance:
          type: number
          nullable: false
          description: The ending cash balance of the company.
        free_cash_flow:
          type: number
          nullable: false
          description: The free cash flow of the company.
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