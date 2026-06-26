> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Update Contacts

> Bulk update contacts.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/contacts/bulk_update
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
  /apollo/contacts/bulk_update:
    post:
      summary: Bulk Update Contacts
      description: Bulk update contacts. Requires a master API key.
      operationId: post_apollo_contacts_bulk_update
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  contacts:
                    type: string
                    description: Updated contacts
                  contacts[].id:
                    type: string
                    description: Contact ID
                  contacts[].first_name:
                    type: string
                    description: First name
                  contacts[].last_name:
                    type: string
                    description: Last name
                  contacts[].email:
                    type: string
                    description: Email
                  contacts[].title:
                    type: string
                    description: Title
                  contacts[].organization_name:
                    type: string
                    description: Organization name
                  contacts[].owner_id:
                    type: string
                    description: Owner ID
                  contacts[].account_id:
                    type: string
                    description: Account ID
                  contacts[].present_raw_address:
                    type: string
                    description: Raw address
                  contacts[].linkedin_url:
                    type: string
                    description: LinkedIn URL
                  contacts[].updated_at:
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