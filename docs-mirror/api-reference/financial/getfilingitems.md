> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Items

> Get SEC filing items



## OpenAPI

````yaml openapi/openapi-financial.json GET /filings/items
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
  /filings/items:
    get:
      tags:
        - SEC Filings
      summary: Get SEC filing items
      description: Get the raw text Items from an SEC filing.
      operationId: getFilingItems
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol.
          required: true
          schema:
            type: string
        - name: filing_type
          in: query
          description: The type of filing.
          required: true
          schema:
            type: string
            enum:
              - 10-K
              - 10-Q
              - 8-K
        - name: year
          in: query
          description: The year of the filing.
          required: true
          schema:
            type: integer
        - name: quarter
          in: query
          description: The quarter of the filing if 10-Q.
          required: false
          schema:
            type: integer
        - name: item
          in: query
          description: The item to get.
          required: false
          schema:
            type: string
            enum:
              - Item-1
              - Item-1A
              - Item-1B
              - Item-2
              - Item-3
              - Item-4
              - Item-5
              - Item-6
              - Item-7
              - Item-7A
              - Item-8
              - Item-9
              - Item-9A
              - Item-9B
              - Item-10
              - Item-11
              - Item-12
              - Item-13
              - Item-14
              - Item-15
              - Item-16
              - Item-1.01
              - Item-1.02
              - Item-1.03
              - Item-1.04
              - Item-2.01
              - Item-2.02
              - Item-2.03
              - Item-2.04
              - Item-2.05
              - Item-2.06
              - Item-3.01
              - Item-3.02
              - Item-3.03
              - Item-4.01
              - Item-4.02
              - Item-5.01
              - Item-5.02
              - Item-5.03
              - Item-5.04
              - Item-5.05
              - Item-5.06
              - Item-5.07
              - Item-5.08
              - Item-6.01
              - Item-6.02
              - Item-6.03
              - Item-6.04
              - Item-6.05
              - Item-7.01
              - Item-8.01
              - Item-9.01
        - name: accession_number
          in: query
          description: The accession number of the filing if 8-K.
          required: false
          schema:
            type: string
        - name: include_exhibits
          in: query
          description: >-
            Whether to include the raw text from linked exhibits. Only
            applicable for 8-K filings. When true, exhibit objects will include
            the 'text' field containing the full exhibit content.
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: SEC filing items response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FilingItemsResponse'
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
    FilingItemsResponse:
      type: object
      properties:
        ticker:
          type: string
          description: The ticker symbol of the company.
        cik:
          type: string
          description: The Central Index Key (CIK) of the company.
        filing_type:
          type: string
          description: The type of filing.
        accession_number:
          type: string
          description: The accession number of the filing.
        year:
          type: integer
          description: The year of the filing.
        quarter:
          type: integer
          description: The quarter of the filing.
        items:
          type: array
          items:
            $ref: '#/components/schemas/FilingItem'
    FilingItem:
      type: object
      properties:
        number:
          type: string
          description: The item number.
        name:
          type: string
          description: The item name.
        text:
          type: string
          description: The item text.
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