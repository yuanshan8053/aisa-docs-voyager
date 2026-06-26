> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk People Enrichment

> Use the Bulk People Enrichment endpoint to enrich data for up to 10 people with a single API call.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/people/bulk_match
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
  /apollo/people/bulk_match:
    post:
      summary: Bulk People Enrichment
      description: >-
        Use the Bulk People Enrichment endpoint to enrich data for up to 10
        people with a single API call. To enrich data for only 1 person, use the
        People Enrichment endpoint instead. Apollo relies on the information you
        pass via the endpoint's parameters to identify the correct people to
        enrich. When you provide more information, Apollo is more likely to find
        matches within its database. If you only provide general information,
        such as a name without a domain or email address, you might receive a
        200 response, but the response will indicate that no records have been
        enriched. The details for each person should be passed as an object with
        the details[] array. By default, this endpoint does not return personal
        emails or phone numbers. Use the reveal_personal_emails and
        reveal_phone_number parameters to retrieve emails and phone numbers. If
        you set either of these parameters to true, Apollo will attempt to
        provide emails or phone numbers for all matches. You can use also use
        the run_waterfall_email and run_waterfall_phone parameters to run
        waterfall enrichment via this endpoint. gives you broader data coverage
        by checking connected third-party data sources for contact emails and
        phone numbers. When you call this endpoint and include at least one
        waterfall parameter, Apollo returns an immediate synchronous response
        with demographic and firmographic data, along with a waterfall
        enrichment request status. Apollo delivers enriched emails and/or phone
        numbers asynchronously to a configured webhook. **Webhook Response
        Details:** - When using native enrichment for phone number enrichment,
        the webhook response follows: - When passing Waterfall flags, the
        webhook response follows: **Webhook Requirements:** - **HTTPS
        Required:** Your endpoint must be publicly accessible over HTTPS. -
        **Rate Limiting:** Ensure your webhook endpoint can handle the volume of
        webhook traffic sent by Apollo. - **Idempotency:** Apollo may retry
        webhook calls. Your endpoint should be idempotent to handle duplicate
        payloads safely. Using this endpoint will consume credits based on your
        account's pricing plan. If you run waterfall enrichment parameters, your
        depends on the type of data you request (emails and/or phone numbers)
        and which data source returns enriched data. To view a summary of
        Apollo's pricing, visit the public pricing page ↗ For detailed
        information regarding API credit usage, see the API enrichment ↗ section
        on the *About Credits* page (login required). This endpoint's rate limit
        is throttled to 50% of the People Enrichment endpoint's per-minute rate
        limit, and is 100% of the hourly and daily rate limits for the same
        individual endpoint.
      operationId: post_apollo_people_bulk_match
      parameters:
        - name: run_waterfall_email
          in: query
          required: false
          schema:
            type: boolean
          description: Set to true to enable email waterfall enrichment
        - name: run_waterfall_phone
          in: query
          required: false
          schema:
            type: boolean
          description: Set to true to enable phone waterfall enrichment
        - name: reveal_personal_emails
          in: query
          required: false
          schema:
            type: boolean
          description: >-
            Set to true if you want to enrich all matched people with personal
            emails. This potentially consumes credits as part of your Apollo
            pricing plan . The default value is false. If a person resides in a
            GDPR -compliant region, Apollo will not reveal their personal email.
        - name: reveal_phone_number
          in: query
          required: false
          schema:
            type: boolean
          description: >-
            Set to true if you want to enrich the data of all matched people
            with all available phone numbers, including mobile phone numbers.
            This potentially consumes credits as part of your Apollo pricing
            plan . The default value is false. If this parameter is set to true,
            you must enter a webhook URL for the webhook_url parameter. Apollo
            will asynchronously verify phone numbers for you, then send a JSON
            response that includes only details about the phone numbers to the
            webhook URL you provide. It can take several minutes for the phone
            numbers to be delivered.
        - name: webhook_url
          in: query
          required: false
          schema:
            type: string
          description: >-
            If you set the reveal_phone_number parameter to true, this parameter
            becomes mandatory. Otherwise, do not use this parameter. Enter the
            webhook URL that specifies where Apollo should send a JSON response
            that includes the phone number you requested. Apollo suggests
            testing this flow to ensure you receive the separate response with
            the phone number. If phone numbers are not revealed delivered to the
            webhook URL, try applying UTF-8 encoding to the webhook URL.
            Example: https://webhook.site/cc4cf44e-e047-4774-8dac-473d28474e40;
            https%3A%2F%2Fwebhook.site%2Fcc4cf44e-e047-4774-8dac-473d28474e40
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                details:
                  type: array
                  items:
                    type: string
                  description: >-
                    Provide info for each person you want to enrich as an object
                    within this array. Add up to 10 people.
              required:
                - details
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    description: Response field
                  error_code:
                    type: string
                    description: Response field
                  error_message:
                    type: string
                    description: Response field
                  total_requested_enrichments:
                    type: integer
                    description: Response field
                  unique_enriched_records:
                    type: integer
                    description: Response field
                  missing_records:
                    type: integer
                    description: Response field
                  credits_consumed:
                    type: integer
                    description: Response field
                  matches:
                    type: array
                    items:
                      type: string
                    description: Response array
                  waterfall:
                    type: object
                    description: Response object
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