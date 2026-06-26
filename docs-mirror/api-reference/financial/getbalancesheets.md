> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Balance Sheets

> Get balance sheets



## OpenAPI

````yaml openapi/openapi-financial.json GET /financials/balance-sheets
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
  /financials/balance-sheets:
    get:
      tags:
        - Financial Statements
      summary: Get balance sheets
      description: Get balance sheets for a ticker.
      operationId: getBalanceSheets
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol. Required if cik is not provided.
          required: false
          schema:
            type: string
        - name: period
          in: query
          description: The time period of the balance sheets.
          required: true
          schema:
            type: string
            enum:
              - annual
              - quarterly
              - ttm
        - name: limit
          in: query
          description: The maximum number of balance sheets to return
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
          description: Balance sheets response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BalanceSheetResponse'
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
    BalanceSheetResponse:
      type: object
      properties:
        balance_sheets:
          type: array
          items:
            $ref: '#/components/schemas/BalanceSheet'
    BalanceSheet:
      type: object
      properties:
        ticker:
          type: string
          description: The ticker symbol.
        report_period:
          type: string
          format: date
          description: The reporting period of the balance sheet.
        fiscal_period:
          type: string
          description: The fiscal period of the balance sheet.
        period:
          type: string
          enum:
            - quarterly
            - ttm
            - annual
          description: The time period of the balance sheet.
        currency:
          type: string
          description: The currency in which the financial data is reported.
        total_assets:
          type: number
          nullable: false
          description: The total assets of the company.
        current_assets:
          type: number
          nullable: false
          description: The current assets of the company.
        cash_and_equivalents:
          type: number
          nullable: false
          description: The cash and equivalents of the company.
        inventory:
          type: number
          nullable: false
          description: The inventory of the company.
        current_investments:
          type: number
          nullable: false
          description: The current investments of the company.
        trade_and_non_trade_receivables:
          type: number
          nullable: false
          description: The trade and non-trade receivables of the company.
        non_current_assets:
          type: number
          nullable: false
          description: The non-current assets of the company.
        property_plant_and_equipment:
          type: number
          nullable: false
          description: The property, plant, and equipment of the company.
        goodwill_and_intangible_assets:
          type: number
          nullable: false
          description: The goodwill and intangible assets of the company.
        investments:
          type: number
          nullable: false
          description: The investments of the company.
        non_current_investments:
          type: number
          nullable: false
          description: The non-current investments of the company.
        outstanding_shares:
          type: number
          nullable: false
          description: The outstanding shares of the company.
        tax_assets:
          type: number
          nullable: false
          description: The tax assets of the company.
        total_liabilities:
          type: number
          nullable: false
          description: The total liabilities of the company.
        current_liabilities:
          type: number
          nullable: false
          description: The current liabilities of the company.
        current_debt:
          type: number
          nullable: false
          description: The current debt of the company.
        trade_and_non_trade_payables:
          type: number
          nullable: false
          description: The trade and non-trade payables of the company.
        deferred_revenue:
          type: number
          nullable: false
          description: The deferred revenue of the company.
        deposit_liabilities:
          type: number
          nullable: false
          description: The deposit liabilities of the company.
        non_current_liabilities:
          type: number
          nullable: false
          description: The non-current liabilities of the company.
        non_current_debt:
          type: number
          nullable: false
          description: The non-current debt of the company.
        tax_liabilities:
          type: number
          nullable: false
          description: The tax liabilities of the company.
        shareholders_equity:
          type: number
          nullable: false
          description: The shareholders' equity of the company.
        retained_earnings:
          type: number
          nullable: false
          description: The retained earnings of the company.
        accumulated_other_comprehensive_income:
          type: number
          nullable: false
          description: The accumulated other comprehensive income of the company.
        total_debt:
          type: number
          nullable: false
          description: The total debt of the company.
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