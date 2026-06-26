> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Interest Rates Snapshot

> Get the latest interest rate data snapshot



## OpenAPI

````yaml openapi/macro_snapshot.json GET /macro/interest-rates/snapshot
openapi: 3.0.3
info:
  title: Financial Datasets API — Macro Interest Rates
  version: 1.0.0
  description: >-
    Central bank interest rate data (historical series + real-time snapshot),
    proxied through AIsa.
servers:
  - url: https://api.aisa.one/apis/v1/financial
    description: Production API
security:
  - bearerAuth: []
paths:
  /macro/interest-rates/snapshot:
    get:
      summary: Interest Rates (Real-Time)
      description: >-
        Get the current interest rates from all major central banks in the
        world.
      operationId: getInterestRatesSnapshot
      parameters:
        - name: bank
          in: query
          description: >-
            The central bank code (e.g., FED, ECB, BOJ). Use the
            /macro/interest-rates/banks endpoint to get a list of available
            banks.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Interest rates snapshot response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InterestRatesResponse'
        '401':
          $ref: '#/components/responses/UnauthorizedError'
        '402':
          $ref: '#/components/responses/PaymentRequiredError'
        '404':
          $ref: '#/components/responses/NotFoundError'
components:
  schemas:
    InterestRatesResponse:
      type: object
      properties:
        interest_rates:
          type: array
          items:
            $ref: '#/components/schemas/InterestRate'
    InterestRate:
      type: object
      properties:
        bank:
          type: string
          description: The symbol of the central bank.
        name:
          type: string
          description: The name of the central bank.
        rate:
          type: number
          description: The interest rate of the central bank.
        date:
          type: string
          description: The date of the interest rate in YYYY-MM-DD format.
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