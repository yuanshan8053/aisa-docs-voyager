> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Create Contacts

> Bulk create contacts.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/contacts/bulk_create
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
  /apollo/contacts/bulk_create:
    post:
      summary: Bulk Create Contacts
      description: Bulk create contacts. Requires a master API key.
      operationId: post_apollo_contacts_bulk_create
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                contacts:
                  type: string
                  description: Array of contacts to create
                append_label_names:
                  type: string
                  description: Label names to append to each created contact
                run_dedupe:
                  type: boolean
                  description: Enable deduplication. Default false.
              required:
                - contacts
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  created_contacts:
                    type: string
                    description: Contacts created in this request
                  created_contacts[].id:
                    type: string
                    description: Contact ID
                  created_contacts[].first_name:
                    type: string
                    description: First name
                  created_contacts[].last_name:
                    type: string
                    description: Last name
                  created_contacts[].organization_name:
                    type: string
                    description: Organization name
                  created_contacts[].title:
                    type: string
                    description: Title
                  created_contacts[].owner_id:
                    type: string
                    description: Owner ID
                  created_contacts[].account_id:
                    type: string
                    description: Account ID
                  created_contacts[].email:
                    type: string
                    description: Email
                  created_contacts[].phone_numbers:
                    type: string
                    description: Phone numbers
                  created_contacts[].typed_custom_fields:
                    type: object
                    description: Typed custom fields object
                  created_contacts[].updated_at:
                    type: string
                    description: Updated timestamp
                  existing_contacts:
                    type: string
                    description: Contacts that already existed (dedupe matches)
                  existing_contacts[].id:
                    type: string
                    description: Contact ID
                  existing_contacts[].first_name:
                    type: string
                    description: First name
                  existing_contacts[].last_name:
                    type: string
                    description: Last name
                  existing_contacts[].organization_name:
                    type: string
                    description: Organization name
                  existing_contacts[].title:
                    type: string
                    description: Title
                  existing_contacts[].owner_id:
                    type: string
                    description: Owner ID
                  existing_contacts[].account_id:
                    type: string
                    description: Account ID
                  existing_contacts[].email:
                    type: string
                    description: Email
                  existing_contacts[].phone_numbers:
                    type: string
                    description: Phone numbers
                  existing_contacts[].typed_custom_fields:
                    type: object
                    description: Typed custom fields object
                  existing_contacts[].updated_at:
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