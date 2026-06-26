> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Earnings Snapshot

> Most recent earnings snapshot for a ticker — actuals plus optional estimate, surprise, and quarter-over-quarter / year-over-year change fields when available.

The most recent earnings snapshot for a ticker. Returns the latest reported EPS and revenue, and — when available — the consensus estimate, surprise vs. estimate, and period-over-period change.

**Best for:** Earnings-day dashboards, consensus beat/miss tracking, surfacing the latest print on a ticker card.

> **Different from [`/earnings/press-releases`](/api-reference/financial/getearningspressreleases):** the press-releases endpoint returns full 8-K text; this one returns just the structured numbers.

## Example

```bash theme={null}
curl -X GET "https://api.aisa.one/apis/v1/financial/earnings?ticker=NVDA" \
  -H "Authorization: Bearer $AISA_API_KEY"
```


## OpenAPI

````yaml openapi/openapi-financial.json GET /earnings
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
  /earnings:
    get:
      tags:
        - Earnings
      summary: Get earnings snapshot
      description: >-
        Get the most recent earnings snapshot for a ticker. Optional
        estimate/surprise and change fields are returned only when available.
      operationId: getEarnings
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Earnings response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EarningsResponse'
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
    EarningsResponse:
      type: object
      properties:
        earnings:
          $ref: '#/components/schemas/Earnings'
    Earnings:
      type: object
      properties:
        ticker:
          type: string
          description: The requested ticker symbol.
        report_period:
          type: string
          format: date
          description: Most recent report period found for the ticker.
        fiscal_period:
          type: string
          nullable: true
          description: Fiscal period label (e.g. 2025-Q4 or 2025-FY).
        currency:
          type: string
          nullable: true
          description: ISO currency code (e.g. USD).
        quarterly:
          $ref: '#/components/schemas/EarningsTimeDimension'
        annual:
          $ref: '#/components/schemas/EarningsTimeDimension'
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: A short error message.
        message:
          type: string
          description: A more detailed error message.
    EarningsTimeDimension:
      type: object
      properties:
        fiscal_period:
          type: string
          nullable: true
          description: Fiscal period label (e.g. 2025-Q4 or 2025-FY).
        currency:
          type: string
          nullable: true
          description: ISO currency code (e.g. USD).
        revenue:
          type: number
          nullable: true
        estimated_revenue:
          type: number
          description: Estimated revenue. Returned only when available.
        revenue_surprise:
          type: string
          description: >-
            Revenue surprise classification versus estimate. Returned only when
            available.
          enum:
            - BEAT
            - MISS
            - MEET
        earnings_per_share:
          type: number
          nullable: true
        estimated_earnings_per_share:
          type: number
          description: Estimated earnings per share. Returned only when available.
        eps_surprise:
          type: string
          description: >-
            EPS surprise classification versus estimate. Returned only when
            available.
          enum:
            - BEAT
            - MISS
            - MEET
        net_income:
          type: number
          nullable: true
        gross_profit:
          type: number
          nullable: true
        operating_income:
          type: number
          nullable: true
        weighted_average_shares:
          type: number
          nullable: true
        weighted_average_shares_diluted:
          type: number
          nullable: true
        cash_and_equivalents:
          type: number
          nullable: true
        total_debt:
          type: number
          nullable: true
        total_assets:
          type: number
          nullable: true
        total_liabilities:
          type: number
          nullable: true
        shareholders_equity:
          type: number
          nullable: true
        net_cash_flow_from_operations:
          type: number
          nullable: true
        capital_expenditure:
          type: number
          nullable: true
        net_cash_flow_from_investing:
          type: number
          nullable: true
        net_cash_flow_from_financing:
          type: number
          nullable: true
        change_in_cash_and_equivalents:
          type: number
          nullable: true
        free_cash_flow:
          type: number
          nullable: true
        revenue_chg:
          type: number
          description: >-
            Percentage change in revenue. QoQ in quarterly payload and YoY in
            annual payload. Returned only when calculable.
        net_income_chg:
          type: number
          description: >-
            Percentage change in net income. QoQ in quarterly payload and YoY in
            annual payload. Returned only when calculable.
        operating_income_chg:
          type: number
          description: >-
            Percentage change in operating income. QoQ in quarterly payload and
            YoY in annual payload. Returned only when calculable.
        gross_profit_chg:
          type: number
          description: >-
            Percentage change in gross profit. QoQ in quarterly payload and YoY
            in annual payload. Returned only when calculable.
        net_cash_flow_from_operations_chg:
          type: number
          description: >-
            Percentage change in net cash flow from operations. QoQ in quarterly
            payload and YoY in annual payload. Returned only when calculable.
        net_cash_flow_from_investing_chg:
          type: number
          description: >-
            Percentage change in net cash flow from investing. QoQ in quarterly
            payload and YoY in annual payload. Returned only when calculable.
        net_cash_flow_from_financing_chg:
          type: number
          description: >-
            Percentage change in net cash flow from financing. QoQ in quarterly
            payload and YoY in annual payload. Returned only when calculable.
        free_cash_flow_chg:
          type: number
          description: >-
            Percentage change in free cash flow. QoQ in quarterly payload and
            YoY in annual payload. Returned only when calculable.
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