> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Segmented Revenues

> Get segmented revenue data



## OpenAPI

````yaml openapi/openapi-financial.json GET /financials/segmented-revenues
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
  /financials/segmented-revenues:
    get:
      tags:
        - Financial Statements
      summary: Get segmented revenue data (deprecated)
      description: Deprecated. Use /financials/income-statements/segments instead.
      operationId: getSegmentedRevenues
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol. Required if cik is not provided.
          required: false
          schema:
            type: string
        - name: period
          in: query
          description: >-
            The date or time period to which the reported revenue data relates
            in ISO 8601 format (YYYY-MM-DD).
          required: true
          schema:
            type: string
            enum:
              - annual
              - quarterly
        - name: limit
          in: query
          description: The maximum number of revenue statements to return.
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
          description: Segmented revenue response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SegmentedRevenuesResponse'
        '400':
          $ref: '#/components/responses/BadRequestError'
        '401':
          $ref: '#/components/responses/UnauthorizedError'
        '402':
          $ref: '#/components/responses/PaymentRequiredError'
        '404':
          $ref: '#/components/responses/NotFoundError'
      deprecated: true
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
    SegmentedRevenuesResponse:
      type: object
      properties:
        segmented_revenues:
          type: array
          items:
            $ref: '#/components/schemas/SegmentedRevenues'
    SegmentedRevenues:
      type: object
      properties:
        ticker:
          type: string
          description: The ticker symbol.
        report_period:
          type: string
          format: date
          description: The reporting period of the revenue.
        period:
          type: string
          enum:
            - quarterly
            - annual
          description: The time period of the revenue.
        items:
          type: array
          description: >-
            An array of revenue segments from SEC filings (10-Ks and 10-Qs) in
            XBRL format
          items:
            type: object
            properties:
              name:
                type: string
                description: The name of the revenue segment.
              amount:
                type: number
                description: >-
                  The numerical amount reported for the specified financial
                  metric, expressed in the company's reporting currency; default
                  is USD.
              end_period:
                type: string
                format: date
                nullable: true
                description: >-
                  The end period of the revenue segment.  Only provided for
                  quarterly data.
              start_period:
                type: string
                format: date
                nullable: true
                description: >-
                  The start period of the revenue segment.  Only provided for
                  quarterly data.
              segments:
                type: array
                items:
                  type: object
                  properties:
                    label:
                      type: string
                      description: The label for the revenue segment.
                    type:
                      type: string
                      description: The type of revenue segment.
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