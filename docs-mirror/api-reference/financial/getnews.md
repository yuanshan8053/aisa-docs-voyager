> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Company News

> Get real-time and historical news



## OpenAPI

````yaml openapi/openapi-financial.json GET /news
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
  /news:
    get:
      tags:
        - News
      summary: Get news articles
      description: >-
        Get recent news articles for a specific company or the broad market.
        Pass a ticker for company-specific news, or omit the ticker for general
        market news. Articles are sourced from RSS feeds of publishers like The
        Motley Fool, Investing.com, Reuters, and more.
      operationId: getNews
      parameters:
        - name: ticker
          in: query
          description: The ticker symbol of the company. Omit for broad market news.
          required: false
          schema:
            type: string
        - name: limit
          in: query
          description: 'The maximum number of news articles to return (default: 5, max: 10).'
          required: false
          schema:
            type: integer
            default: 5
            maximum: 10
      responses:
        '200':
          description: News articles response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NewsResponse'
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
    NewsResponse:
      type: object
      properties:
        news:
          type: array
          items:
            $ref: '#/components/schemas/News'
    News:
      type: object
      properties:
        ticker:
          type: string
          description: The ticker symbol.
        title:
          type: string
          description: The title of the news article.
        author:
          type: string
          description: The author of the news article.
        source:
          type: string
          description: The source of the news article.
        date:
          type: string
          format: date
          description: The date the news article was published.
        url:
          type: string
          format: uri
          description: The URL of the news article.
        sentiment:
          type: string
          description: The sentiment of the news article.
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