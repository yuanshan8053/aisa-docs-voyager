> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Metrics

> Query Metrics



## OpenAPI

````yaml openapi/agentmail.json GET /agentmail/metrics
openapi: 3.1.0
info:
  title: AgentMail API
  version: 1.0.0
  description: >-
    AgentMail email API endpoints exposed through the AIsa unified gateway.
    Adapted from the upstream docs.agentmail.to OpenAPI spec.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - Bearer: []
paths:
  /agentmail/metrics:
    get:
      tags:
        - subpackage_metrics
      summary: Query Metrics
      description: |-
        **CLI:**
        ```bash
        agentmail metrics list
        ```
      operationId: query
      parameters:
        - name: event_types
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type_metrics_MetricEventTypes'
        - name: start
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type_metrics_Start'
        - name: end
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type_metrics_End'
        - name: period
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type_metrics_Period'
        - name: limit
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type_metrics_MetricLimit'
        - name: descending
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/type_metrics_Descending'
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type_metrics_QueryMetricsResponse'
        '400':
          description: Error response with status 400
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/type__ValidationErrorResponse'
components:
  schemas:
    type_metrics_MetricEventTypes:
      type: array
      items:
        $ref: '#/components/schemas/type_metrics_MetricEventType'
      description: List of metric event types to query.
      title: MetricEventTypes
    type_metrics_Start:
      type: string
      format: date-time
      description: Start timestamp for the query.
      title: Start
    type_metrics_End:
      type: string
      format: date-time
      description: End timestamp for the query.
      title: End
    type_metrics_Period:
      type: string
      description: Period in number of seconds for the query.
      title: Period
    type_metrics_MetricLimit:
      type: integer
      description: Limit on number of buckets to return.
      title: MetricLimit
    type_metrics_Descending:
      type: boolean
      description: Sort in descending order.
      title: Descending
    type_metrics_QueryMetricsResponse:
      type: object
      additionalProperties:
        type: array
        items:
          $ref: '#/components/schemas/type_metrics_MetricBucket'
      description: Metrics grouped by event type.
      title: QueryMetricsResponse
    type__ValidationErrorResponse:
      type: object
      properties:
        name:
          $ref: '#/components/schemas/type__ErrorName'
        errors:
          description: Validation errors.
      required:
        - name
        - errors
      title: ValidationErrorResponse
    type_metrics_MetricEventType:
      type: string
      enum:
        - message.sent
        - message.delivered
        - message.bounced
        - message.delayed
        - message.rejected
        - message.complained
        - message.received
      description: Type of metric event.
      title: MetricEventType
    type_metrics_MetricBucket:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
          description: Timestamp of the bucket.
        count:
          type: integer
          description: Count of events in the bucket.
      required:
        - timestamp
        - count
      title: MetricBucket
    type__ErrorName:
      type: string
      description: Name of error.
      title: ErrorName
  securitySchemes:
    Bearer:
      type: http
      scheme: bearer

````