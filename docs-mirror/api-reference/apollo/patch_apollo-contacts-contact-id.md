> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update or View Contact

> Update fields on an existing contact.



## OpenAPI

````yaml openapi/apollo.json PATCH /apollo/contacts/{contact_id}
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
    patch:
      summary: Update or View Contact
      description: Update fields on an existing contact. Requires a master API key.
      operationId: patch_apollo_contacts_contact_id
      parameters:
        - name: contact_id
          in: path
          required: true
          schema:
            type: string
          description: Contact ID
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
                    description: Updated contact
                  contact.id:
                    type: string
                    description: Contact ID
                  contact.first_name:
                    type: string
                    description: First name
                  contact.last_name:
                    type: string
                    description: Last name
                  contact.email:
                    type: string
                    description: Email
                  contact.title:
                    type: string
                    description: Title
                  contact.organization_name:
                    type: string
                    description: Organization name
                  contact.owner_id:
                    type: string
                    description: Owner ID
                  contact.account_id:
                    type: string
                    description: Account ID
                  contact.present_raw_address:
                    type: string
                    description: Raw address
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