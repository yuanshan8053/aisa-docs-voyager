> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Facts

> Get company facts



## OpenAPI

````yaml openapi/openapi-financial.json GET /company/facts
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
  /company/facts:
    get:
      tags:
        - Company Information
      summary: Get company facts
      description: Get company facts for a ticker.
      operationId: getCompanyFacts
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol.
          required: false
          schema:
            type: string
        - name: cik
          in: query
          description: The CIK of the company.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Company facts response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CompanyFactsResponse'
        '400':
          $ref: '#/components/responses/BadRequestError'
        '401':
          $ref: '#/components/responses/UnauthorizedError'
        '404':
          $ref: '#/components/responses/NotFoundError'
components:
  schemas:
    CompanyFactsResponse:
      type: object
      properties:
        company_facts:
          $ref: '#/components/schemas/CompanyFacts'
    CompanyFacts:
      type: object
      properties:
        ticker:
          type: string
          description: The ticker symbol of the company.
        name:
          type: string
          description: The name of the company.
        cik:
          type: string
          description: The Central Index Key (CIK) of the company.
        industry:
          type: string
          description: The industry of the company.
        sector:
          type: string
          description: The sector of the company.
        category:
          type: string
          description: The category of the company.
        exchange:
          type: string
          description: The exchange of the company.
        is_active:
          type: boolean
          description: Whether the company is currently active.
        listing_date:
          type: string
          format: date
          description: The date the company was listed on the stock exchange.
        location:
          type: string
          description: The location of the company.
        market_cap:
          type: number
          description: The market capitalization of the company.
        number_of_employees:
          type: number
          description: The number of employees at the company.
        sec_filings_url:
          type: string
          format: uri
          description: The URL of the company's SEC filings.
        sic_code:
          type: string
          description: The Standard Industrial Classification (SIC) code of the company.
        sic_industry:
          type: string
          description: The industry of the company based on the SIC code.
        sic_sector:
          type: string
          description: The sector of the company based on the SIC code.
        website_url:
          type: string
          format: uri
          description: The URL of the company's website.
        weighted_average_shares:
          type: number
          description: The weighted average shares of the company.
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