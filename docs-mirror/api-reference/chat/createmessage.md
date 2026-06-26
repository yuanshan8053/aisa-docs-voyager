> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Messages

> Create a message

Creates a Claude model response using the Anthropic-compatible Messages API. This endpoint mirrors the [Anthropic `/v1/messages` specification](https://platform.claude.com/docs/en/api/messages/create), routed through the AIsa gateway at `https://api.aisa.one/v1/messages`.

Use this endpoint when you want to call Claude models (`claude-opus-4-7`, `claude-sonnet-4-6`, `claude-haiku-4-5-20251001`, etc.) with Anthropic's native request format — including extended thinking, tool use, and prompt caching. If you prefer OpenAI-style chat completions, the same Claude models are also available via the [OpenAI Chat](/api-reference/chat/createchatcompletion) endpoint.

Authentication uses your AIsa API key as a Bearer token. See the [model catalog](/guides/models) for the full list of supported Claude variants and context windows, and [pricing](/guides/pricing/ai-model-pricing-llm-inference) for per-token rates.


## OpenAPI

````yaml openapi/claude-messages.json POST /messages
openapi: 3.0.3
info:
  title: Claude Messages API
  version: 1.0.0
  description: >-
    Anthropic-compatible Messages API, exposed through AIsa. Send structured
    messages and generate responses using Claude models.
servers:
  - url: https://api.aisa.one/v1
security:
  - BearerAuth: []
paths:
  /messages:
    post:
      summary: Create a message
      description: >-
        Send a structured conversation to a Claude model and receive a response.
        Compatible with the Anthropic Messages API.
      operationId: createMessage
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - model
                - max_tokens
                - messages
              properties:
                model:
                  type: string
                  description: >-
                    Claude model identifier. Examples: claude-opus-4-7,
                    claude-sonnet-4-6, claude-haiku-4-5-20251001.
                  example: claude-sonnet-4-6
                max_tokens:
                  type: integer
                  description: Maximum number of tokens to generate before stopping.
                  example: 1024
                messages:
                  type: array
                  description: Conversation turns.
                  items:
                    type: object
                    required:
                      - role
                      - content
                    properties:
                      role:
                        type: string
                        enum:
                          - user
                          - assistant
                      content:
                        description: String or array of content blocks.
                        oneOf:
                          - type: string
                          - type: array
                            items:
                              type: object
                  example:
                    - role: user
                      content: Hello, Claude
                system:
                  description: System prompt. String or array of text blocks.
                  oneOf:
                    - type: string
                    - type: array
                      items:
                        type: object
                temperature:
                  type: number
                  format: float
                  minimum: 0
                  maximum: 1
                  default: 1
                  description: Randomness. 0 = deterministic, 1 = creative.
                top_p:
                  type: number
                  format: float
                  description: Nucleus sampling. Use instead of temperature.
                top_k:
                  type: integer
                  description: Only sample from the top K options for each token.
                stop_sequences:
                  type: array
                  items:
                    type: string
                  description: Custom sequences that stop generation.
                stream:
                  type: boolean
                  default: false
                  description: Enable SSE streaming.
                tools:
                  type: array
                  description: Tools the model may use.
                  items:
                    type: object
                    required:
                      - name
                      - input_schema
                    properties:
                      name:
                        type: string
                      description:
                        type: string
                      input_schema:
                        type: object
                      type:
                        type: string
                        example: custom
                tool_choice:
                  type: object
                  description: How the model uses tools.
                  properties:
                    type:
                      type: string
                      enum:
                        - auto
                        - any
                        - tool
                        - none
                    name:
                      type: string
                      description: Required when type is tool.
                    disable_parallel_tool_use:
                      type: boolean
                      default: false
                thinking:
                  type: object
                  description: Enable extended thinking for complex reasoning.
                  properties:
                    type:
                      type: string
                      enum:
                        - enabled
                    budget_tokens:
                      type: integer
                      example: 10000
                    display:
                      type: string
                      enum:
                        - summarized
                        - omitted
                metadata:
                  type: object
                  properties:
                    user_id:
                      type: string
                      description: External user ID (no PII).
                service_tier:
                  type: string
                  enum:
                    - auto
                    - standard_only
                  default: auto
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: msg_024e7cf42f5d47cfa6982b5ff8b55642
                  type:
                    type: string
                    example: message
                  role:
                    type: string
                    example: assistant
                  content:
                    type: array
                    description: Response content blocks (text, tool_use, thinking, etc.).
                    items:
                      type: object
                  model:
                    type: string
                    example: claude-sonnet-4-6
                  stop_reason:
                    type: string
                    enum:
                      - end_turn
                      - stop_sequence
                      - max_tokens
                      - tool_use
                  stop_sequence:
                    type: string
                    nullable: true
                  usage:
                    type: object
                    properties:
                      input_tokens:
                        type: integer
                      output_tokens:
                        type: integer
                      cache_creation_input_tokens:
                        type: integer
                      cache_read_input_tokens:
                        type: integer
        '400':
          description: Invalid request parameters
        '401':
          description: Missing or invalid API key
        '429':
          description: Rate limit exceeded
        '500':
          description: Internal server error
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key
      description: Your AIsa API key as a Bearer token.

````