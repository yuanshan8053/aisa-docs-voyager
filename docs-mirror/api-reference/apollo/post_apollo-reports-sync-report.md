> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Analytics Report

> Query analytics report.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/reports/sync_report
openapi: 3.0.3
info:
  title: Apollo API
  version: 1.0.0
  description: Apollo API endpoints exposed through the AIsa unified gateway.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /apollo/reports/sync_report:
    post:
      summary: Query Analytics Report
      description: Query analytics report. Requires a master API key.
      operationId: post_apollo_reports_sync_report
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                metrics:
                  type: array
                  items:
                    type: string
                  description: Metrics to compute.
                group_by:
                  type: array
                  items:
                    type: string
                  description: Dimensions to group by.
                pivot_group_by:
                  type: array
                  items:
                    type: string
                  description: Optional pivot dimensions.
                sorts:
                  type: array
                  items:
                    type: string
                  description: Sort specs.
                filters:
                  type: string
                  description: Filter specs.
                date_range:
                  type: object
                  description: Date range filter (when supported).
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  report:
                    type: object
                    description: Report result (shape depends on request).
        '400':
          description: Bad request
        '401':
          description: Unauthorized
        '429':
          description: Rate limit exceeded
        '500':
          description: Internal server error
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````