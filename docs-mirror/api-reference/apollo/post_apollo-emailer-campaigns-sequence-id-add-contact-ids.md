> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Contacts to a Sequence

> Add contacts to a sequence.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/emailer_campaigns/{sequence_id}/add_contact_ids
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
  /apollo/emailer_campaigns/{sequence_id}/add_contact_ids:
    post:
      summary: Add Contacts to a Sequence
      description: Add contacts to a sequence. Requires a master API key.
      operationId: post_apollo_emailer_campaigns_sequence_id_add_contact_ids
      parameters:
        - name: sequence_id
          in: path
          required: true
          schema:
            type: string
          description: Sequence (emailer campaign) ID.
        - name: emailer_campaign_id
          in: query
          required: true
          schema:
            type: string
          description: Sequence ID (same as sequence_id).
        - name: contact_ids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            Contact IDs to add. Provide either contact_ids[] or label_names[]
            (or both).
        - name: label_names[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            Label names for contacts to add. Provide either label_names[] or
            contact_ids[] (or both).
        - name: send_email_from_email_account_id
          in: query
          required: true
          schema:
            type: string
          description: Email account ID (or IDs) to send from.
        - name: send_email_from_email_address
          in: query
          required: false
          schema:
            type: string
          description: Optional from-address alias.
        - name: sequence_no_email
          in: query
          required: false
          schema:
            type: boolean
          description: Allow contacts without email.
        - name: sequence_unverified_email
          in: query
          required: false
          schema:
            type: boolean
          description: Allow contacts with unverified email.
        - name: sequence_job_change
          in: query
          required: false
          schema:
            type: boolean
          description: Allow contacts with job change.
        - name: sequence_active_in_other_campaigns
          in: query
          required: false
          schema:
            type: boolean
          description: Allow contacts active in other sequences.
        - name: sequence_finished_in_other_campaigns
          in: query
          required: false
          schema:
            type: boolean
          description: Allow contacts finished in other sequences.
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                    description: Whether the add succeeded (when returned).
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