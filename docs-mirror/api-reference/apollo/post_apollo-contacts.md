> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Contact

> Create a new contact.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/contacts
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
  /apollo/contacts:
    post:
      summary: Create a Contact
      description: Create a new contact. Requires a master API key.
      operationId: post_apollo_contacts
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                first_name:
                  type: string
                  description: First name
                last_name:
                  type: string
                  description: Last name
                organization_name:
                  type: string
                  description: Organization name
                title:
                  type: string
                  description: Title
                account_id:
                  type: string
                  description: Account ID
                email:
                  type: string
                  description: Email
                website_url:
                  type: string
                  description: Website URL
                label_names:
                  type: string
                  description: Labels to set on the contact
                contact_stage_id:
                  type: string
                  description: Contact stage ID
                present_raw_address:
                  type: string
                  description: Raw address
                direct_phone:
                  type: string
                  description: Direct phone
                corporate_phone:
                  type: string
                  description: Corporate phone
                mobile_phone:
                  type: string
                  description: Mobile phone
                home_phone:
                  type: string
                  description: Home phone
                other_phone:
                  type: string
                  description: Other phone
                typed_custom_fields:
                  type: object
                  description: Typed custom fields object
                run_dedupe:
                  type: boolean
                  description: Enable deduplication. Default false.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
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