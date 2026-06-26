> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update or View Contact

> View a contact by ID.



## OpenAPI

````yaml openapi/apollo.json GET /apollo/contacts/{contact_id}
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
  /apollo/contacts/{contact_id}:
    get:
      summary: Update or View Contact
      description: View a contact by ID. Requires a master API key.
      operationId: get_apollo_contacts_contact_id
      parameters:
        - name: contact_id
          in: path
          required: true
          schema:
            type: string
          description: Contact ID
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  contact:
                    type: object
                    description: Contact object
                  contact.id:
                    type: string
                    description: Contact ID
                  contact.first_name:
                    type: string
                    description: First name
                  contact.last_name:
                    type: string
                    description: Last name
                  contact.organization_name:
                    type: string
                    description: Organization name
                  contact.title:
                    type: string
                    description: Title
                  contact.email:
                    type: string
                    description: Email
                  contact.phone_numbers:
                    type: string
                    description: Phone numbers
                  contact.phone_numbers[].raw_number:
                    type: string
                    description: Raw number
                  contact.phone_numbers[].sanitized_number:
                    type: string
                    description: Sanitized number
                  contact.owner_id:
                    type: string
                    description: Owner ID
                  contact.account_id:
                    type: string
                    description: Account ID
                  contact.present_raw_address:
                    type: string
                    description: Raw address
                  contact.linkedin_url:
                    type: string
                    description: LinkedIn URL
                  contact.updated_at:
                    type: string
                    description: Updated timestamp
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