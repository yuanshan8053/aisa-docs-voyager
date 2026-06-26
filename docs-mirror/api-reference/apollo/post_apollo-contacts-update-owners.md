> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Contact Owner for Multiple Contacts

> Update contact owner for multiple contacts.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/contacts/update_owners
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
  /apollo/contacts/update_owners:
    post:
      summary: Update Contact Owner for Multiple Contacts
      description: Update contact owner for multiple contacts. Requires a master API key.
      operationId: post_apollo_contacts_update_owners
      parameters:
        - name: contact_ids[]
          in: query
          required: true
          schema:
            type: string
          description: Contact IDs
        - name: owner_id
          in: query
          required: true
          schema:
            type: string
          description: New owner ID
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
                  contacts[].owner_id:
                    type: string
                    description: Owner ID
                  contacts[].crm_owner_id:
                    type: string
                    description: CRM owner ID
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