> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Historical Financial Metrics

> Get historical financial metrics



## OpenAPI

````yaml openapi/openapi-financial.json GET /financial-metrics
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
  /financial-metrics:
    get:
      tags:
        - Financial Metrics
      summary: Get financial metrics
      description: >-
        Get financial metrics for a ticker, including valuation, profitability,
        efficiency, liquidity, leverage, growth, and per share metrics.
      operationId: getFinancialMetrics
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol of the company. Required if cik is not provided.
          required: false
          schema:
            type: string
        - name: cik
          in: query
          description: >-
            The Central Index Key (CIK) of the company. Can be used instead of
            ticker.
          required: false
          schema:
            type: string
        - name: period
          in: query
          description: The time period for the financial data.
          required: true
          schema:
            type: string
            enum:
              - annual
              - quarterly
              - ttm
        - name: limit
          in: query
          description: The maximum number of results to return.
          required: false
          schema:
            type: integer
        - $ref: '#/components/parameters/ReportPeriod'
        - $ref: '#/components/parameters/ReportPeriodGte'
        - $ref: '#/components/parameters/ReportPeriodLte'
        - $ref: '#/components/parameters/ReportPeriodGt'
        - $ref: '#/components/parameters/ReportPeriodLt'
      responses:
        '200':
          description: The historical financial metrics and ratios for a ticker
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FinancialMetricsResponse'
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
    FinancialMetricsResponse:
      type: object
      properties:
        ticker:
          type: string
          description: The ticker symbol of the company.
        market_cap:
          type: number
          description: The market capitalization of the company.
        enterprise_value:
          type: number
          description: The total value of the company (market cap + debt - cash).
        price_to_earnings_ratio:
          type: number
          description: Price to earnings ratio.
        price_to_book_ratio:
          type: number
          description: Price to book ratio.
        price_to_sales_ratio:
          type: number
          description: Price to sales ratio.
        enterprise_value_to_ebitda_ratio:
          type: number
          description: Enterprise value to EBITDA ratio.
        enterprise_value_to_revenue_ratio:
          type: number
          description: Enterprise value to revenue ratio.
        free_cash_flow_yield:
          type: number
          description: Free cash flow yield.
        peg_ratio:
          type: number
          description: Price to earnings growth ratio.
        gross_margin:
          type: number
          description: Gross profit as a percentage of revenue.
        operating_margin:
          type: number
          description: Operating income as a percentage of revenue.
        net_margin:
          type: number
          description: Net income as a percentage of revenue.
        return_on_equity:
          type: number
          description: Net income as a percentage of shareholders' equity.
        return_on_assets:
          type: number
          description: Net income as a percentage of total assets.
        return_on_invested_capital:
          type: number
          description: >-
            Net operating profit after taxes as a percentage of invested
            capital.
        asset_turnover:
          type: number
          description: Revenue divided by average total assets.
        inventory_turnover:
          type: number
          description: Cost of goods sold divided by average inventory.
        receivables_turnover:
          type: number
          description: Revenue divided by average accounts receivable.
        days_sales_outstanding:
          type: number
          description: Average accounts receivable divided by revenue over the period.
        operating_cycle:
          type: number
          description: Inventory turnover + receivables turnover.
        working_capital_turnover:
          type: number
          description: Revenue divided by average working capital.
        current_ratio:
          type: number
          description: Current assets divided by current liabilities.
        quick_ratio:
          type: number
          description: Quick assets divided by current liabilities.
        cash_ratio:
          type: number
          description: Cash and cash equivalents divided by current liabilities.
        operating_cash_flow_ratio:
          type: number
          description: Operating cash flow divided by current liabilities.
        debt_to_equity:
          type: number
          description: Total debt divided by shareholders' equity.
        debt_to_assets:
          type: number
          description: Total debt divided by total assets.
        interest_coverage:
          type: number
          description: EBIT divided by interest expense.
        revenue_growth:
          type: number
          description: Year-over-year growth in revenue.
        earnings_growth:
          type: number
          description: Year-over-year growth in earnings.
        book_value_growth:
          type: number
          description: Year-over-year growth in book value.
        earnings_per_share_growth:
          type: number
          description: Growth in earnings per share over the period.
        free_cash_flow_growth:
          type: number
          description: Growth in free cash flow over the period.
        operating_income_growth:
          type: number
          description: Growth in operating income over the period.
        ebitda_growth:
          type: number
          description: Growth in EBITDA over the period.
        payout_ratio:
          type: number
          description: Dividends paid as a percentage of net income.
        earnings_per_share:
          type: number
          description: Net income divided by weighted average shares outstanding.
        book_value_per_share:
          type: number
          description: Shareholders' equity divided by shares outstanding.
        free_cash_flow_per_share:
          type: number
          description: Free cash flow divided by shares outstanding.
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