> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Income Statements

> Get income statements



## OpenAPI

````yaml openapi/openapi-financial.json GET /financials/income-statements
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
  /financials/income-statements:
    get:
      tags:
        - Financial Statements
      summary: Get income statements
      description: Get income statements for a ticker.
      operationId: getIncomeStatements
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol. Required if cik is not provided.
          required: false
          schema:
            type: string
        - name: period
          in: query
          description: The time period of the income statements.
          required: true
          schema:
            type: string
            enum:
              - annual
              - quarterly
              - ttm
        - name: limit
          in: query
          description: The maximum number of income statements to return.
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
          description: Income statements response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IncomeStatementResponse'
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
    IncomeStatementResponse:
      type: object
      properties:
        income_statements:
          type: array
          items:
            $ref: '#/components/schemas/IncomeStatement'
    IncomeStatement:
      type: object
      properties:
        ticker:
          type: string
          description: The ticker symbol.
        report_period:
          type: string
          format: date
          description: The reporting period of the income statement.
        fiscal_period:
          type: string
          description: The fiscal period of the income statement.
        period:
          type: string
          enum:
            - quarterly
            - ttm
            - annual
          description: The time period of the income statement.
        currency:
          type: string
          description: The currency in which the financial data is reported.
        revenue:
          type: number
          nullable: false
          description: The total revenue of the company.
        cost_of_revenue:
          type: number
          nullable: false
          description: The cost of revenue of the company.
        gross_profit:
          type: number
          nullable: false
          description: The gross profit of the company.
        operating_expense:
          type: number
          nullable: false
          description: The operating expenses of the company.
        selling_general_and_administrative_expenses:
          type: number
          nullable: false
          description: The selling, general, and administrative expenses of the company.
        research_and_development:
          type: number
          nullable: false
          description: The research and development expenses of the company.
        operating_income:
          type: number
          nullable: false
          description: The operating income of the company.
        interest_expense:
          type: number
          nullable: false
          description: The interest expenses of the company.
        ebit:
          type: number
          nullable: false
          description: The earnings before interest and taxes of the company.
        income_tax_expense:
          type: number
          nullable: false
          description: The income tax expenses of the company.
        net_income_discontinued_operations:
          type: number
          nullable: false
          description: The net income from discontinued operations of the company.
        net_income_non_controlling_interests:
          type: number
          nullable: false
          description: The net income from non-controlling interests of the company.
        net_income:
          type: number
          nullable: false
          description: The net income of the company.
        net_income_common_stock:
          type: number
          nullable: false
          description: The net income available to common stockholders of the company.
        preferred_dividends_impact:
          type: number
          nullable: false
          description: The impact of preferred dividends on the net income of the company.
        consolidated_income:
          type: number
          nullable: false
          description: The consolidated income of the company.
        earnings_per_share:
          type: number
          nullable: false
          description: The earnings per share of the company.
        earnings_per_share_diluted:
          type: number
          nullable: false
          description: The diluted earnings per share of the company.
        dividends_per_common_share:
          type: number
          nullable: false
          description: The dividends per common share of the company.
        weighted_average_shares:
          type: number
          nullable: false
          description: The weighted average shares of the company.
        weighted_average_shares_diluted:
          type: number
          nullable: false
          description: The diluted weighted average shares of the company.
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