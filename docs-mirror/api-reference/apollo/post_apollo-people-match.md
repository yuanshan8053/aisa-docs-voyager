> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# People Enrichment

> Use the People Enrichment endpoint to enrich data for 1 person.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/people/match
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
  /apollo/people/match:
    post:
      summary: People Enrichment
      description: >-
        Use the People Enrichment endpoint to enrich data for 1 person. To
        enrich data for up to 10 people with a single API call, use the Bulk
        People Enrichment endpoint instead. Apollo relies on the information you
        pass via the endpoint's parameters to identify the correct person to
        enrich. If you provide more information about a person, Apollo is more
        likely to find a match within its database. If you only provide general
        information, such as a name without a domain or email address, you might
        receive a 200 response, but the response will indicate that no records
        have been enriched. By default, this endpoint does not return personal
        emails or phone numbers. Use the reveal_personal_emails and
        reveal_phone_number parameters to retrieve emails and phone numbers. You
        can also use the run_waterfall_email and run_waterfall_phone parameters
        to run waterfall enrichment via this endpoint. gives you broader data
        coverage by checking connected third-party data sources for contact
        emails and phone numbers. When you call this endpoint and include at
        least one waterfall parameter, Apollo returns an immediate synchronous
        response with demographic and firmographic data, along with a waterfall
        enrichment request status. Apollo delivers enriched emails and/or phone
        numbers asynchronously to a configured webhook. **Webhook Response
        Details:** - When using native enrichment for phone number enrichment,
        the webhook response follows: - When passing Waterfall flags, the
        webhook response follows: **Webhook Requirements:** - **HTTPS
        Required:** Your endpoint must be publicly accessible over HTTPS. -
        **Rate Limiting:** Ensure your webhook endpoint can handle the volume of
        webhook traffic sent by Apollo. - **Idempotency:** Apollo may retry
        webhook calls; your endpoint should be idempotent to handle duplicate
        payloads safely. Using this endpoint will consume credits based on your
        account's pricing plan. If you run waterfall enrichment parameters, your
        depends on the type of data you request (emails and/or phone numbers)
        and which data source returns enriched data. To view a summary of
        Apollo's pricing, visit the public pricing page ↗ For detailed
        information regarding API credit usage, see the API enrichment ↗ section
        on the *About Credits* page (login required).
      operationId: post_apollo_people_match
      parameters:
        - name: first_name
          in: query
          required: false
          schema:
            type: string
          description: >-
            The first name of the person. This is typically used in combination
            with the last_name parameter. Example: tim
        - name: last_name
          in: query
          required: false
          schema:
            type: string
          description: >-
            The last name of the person. This is typically used in combination
            with the first_name parameter. Example: zheng
        - name: name
          in: query
          required: false
          schema:
            type: string
          description: >-
            The full name of the person. This will typically be a first name and
            last name separated by a space. If you use this parameter, you do
            not need to use the first_name and last_name parameters. Example:
            tim zheng
        - name: email
          in: query
          required: false
          schema:
            type: string
          description: 'The email address of the person. Example: example@email.com'
        - name: hashed_email
          in: query
          required: false
          schema:
            type: string
          description: >-
            The hashed email of the person. The email should adhere to either
            the MD5 or SHA-256 hash format. Example:
            8d935115b9ff4489f2d1f9249503cadf (MD5) or
            97817c0c49994eb500ad0a5e7e2d8aed51977b26424d508f66e4e8887746a152
            (SHA-256)
        - name: organization_name
          in: query
          required: false
          schema:
            type: string
          description: >-
            The name of the person's employer. This can be the current employer
            or a previous employer. Example: apollo
        - name: domain
          in: query
          required: false
          schema:
            type: string
          description: >-
            The domain name for the person's employer. This can be the current
            employer or a previous employer. Do not include www., the @ symbol,
            or similar. Example: apollo.io or microsoft.com
        - name: id
          in: query
          required: false
          schema:
            type: string
          description: >-
            The Apollo ID for the person. Each person in the Apollo database is
            assigned a unique ID. To find IDs, call the People API Search
            endpoint and identify the values for person_id. Example:
            587cf802f65125cad923a266
        - name: linkedin_url
          in: query
          required: false
          schema:
            type: string
          description: >-
            The URL for the person's LinkedIn profile. Example:
            http://www.linkedin.com/in/tim-zheng-677ba010
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
            Set to true if you want to enrich the person's data with personal
            emails. This potentially consumes credits as part of your Apollo
            pricing plan . The default value is false. If a person resides in a
            GDPR -compliant region, Apollo will not reveal their personal email.
        - name: reveal_phone_number
          in: query
          required: false
          schema:
            type: boolean
          description: >-
            Set to true if you want to enrich the person's data with all
            available phone numbers, including mobile phone numbers. This
            potentially consumes credits as part of your Apollo pricing plan .
            The default value is false. If this parameter is set to true, you
            must enter a webhook URL for the webhook_url parameter. Apollo will
            asynchronously verify phone numbers for you, then send a JSON
            response that includes only details about the person's phone numbers
            to the webhook URL you provide. It can take several minutes for the
            phone numbers to be delivered.
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
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  person:
                    type: object
                    description: Response object
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