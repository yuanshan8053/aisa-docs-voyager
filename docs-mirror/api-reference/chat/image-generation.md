> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Generation via Chat

> Generate images with wan2.7-image and wan2.7-image-pro. These models route through /v1/chat/completions (not /v1/images/generations) using OpenAI's multimodal chat schema.

Wan 2.7 image models are exposed through the **Chat Completions** endpoint, not the OpenAI-style `/v1/images/generations` path. Send a standard chat request with a multimodal `content` array containing a text prompt, and AIsa returns generated images as `{type: "image"}` parts inside `choices[].message.content[]`.

<Note>
  Looking for Seedream (`seedream-4-5-251128`)? It uses a different route — [`/v1/images/generations`](#). Gemini image previews use [`/v1/models/{model}:generateContent`](/api-reference/chat/generatecontent). This page only covers the **Wan 2.7 family**.
</Note>

## Supported models

| Model              | Cost per image | Typical use                                                     |
| ------------------ | -------------- | --------------------------------------------------------------- |
| `wan2.7-image`     | \$0.030        | Fast, general-purpose image generation                          |
| `wan2.7-image-pro` | \$0.075        | Higher fidelity; also supports image-to-video via separate flow |

## Request

The request schema is the same `POST /v1/chat/completions` you already use for text — the only differences are which model you pass and how `content` is structured.

**Critical rule:** `messages[].content` must be an **array of typed parts**. Passing a plain string returns `400 invalid_parameter_error` with the message `"Input should be a valid list: messages[*].content"`.

<CodeGroup>
  ```bash curl theme={null}
  curl -sS -X POST "https://api.aisa.one/v1/chat/completions" \
    -H "Authorization: Bearer $AISA_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "wan2.7-image",
      "messages": [
        {
          "role": "user",
          "content": [
            { "type": "text", "text": "A cute red panda, ultra-detailed, cinematic lighting" }
          ]
        }
      ],
      "n": 1
    }'
  ```

  ```python Python theme={null}
  from openai import OpenAI

  client = OpenAI(base_url="https://api.aisa.one/v1", api_key="sk-aisa-...")

  resp = client.chat.completions.create(
      model="wan2.7-image",
      messages=[
          {
              "role": "user",
              "content": [
                  {"type": "text", "text": "A cute red panda, ultra-detailed, cinematic lighting"}
              ],
          }
      ],
      n=1,
  )

  # Pull image URLs out of the response
  for choice in resp.choices:
      for part in choice.message.content:
          if part["type"] == "image":
              print(part["image"])
  ```

  ```typescript TypeScript theme={null}
  import OpenAI from "openai";

  const client = new OpenAI({
    baseURL: "https://api.aisa.one/v1",
    apiKey: process.env.AISA_API_KEY,
  });

  const resp = await client.chat.completions.create({
    model: "wan2.7-image",
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: "A cute red panda, ultra-detailed, cinematic lighting" },
        ] as any,
      },
    ],
    n: 1,
  });

  const urls = resp.choices
    .flatMap((c) => (c.message.content as any[]))
    .filter((p) => p.type === "image")
    .map((p) => p.image);
  ```
</CodeGroup>

### Request fields

| Field                                | Type    | Required              | Notes                                                                        |
| ------------------------------------ | ------- | --------------------- | ---------------------------------------------------------------------------- |
| `model`                              | string  | yes                   | `wan2.7-image` or `wan2.7-image-pro`                                         |
| `messages[].role`                    | string  | yes                   | `user` for the prompt turn                                                   |
| `messages[].content`                 | array   | **yes**               | Must be an array, not a string                                               |
| `messages[].content[].type`          | string  | yes                   | `text` for prompt parts; `image_url` for image-to-image inputs               |
| `messages[].content[].text`          | string  | when `type=text`      | The prompt                                                                   |
| `messages[].content[].image_url.url` | string  | when `type=image_url` | Reference image URL                                                          |
| `n`                                  | integer | no                    | Number of images. **Default is 4** for `wan2.7-image`; pass `1` to save cost |

## Response shape

```json theme={null}
{
  "id": "chatcmpl-fcc86dfd-...",
  "object": "chat.completion",
  "created": 1776495713,
  "model": "wan2.7-image",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": [
          { "type": "image", "image": "https://cdn.aisa.one/images/wan2.7/..." }
        ]
      }
    }
  ],
  "usage": {
    "prompt_tokens": 104,
    "completion_tokens": 8,
    "total_tokens": 112
  }
}
```

* **One choice per image.** If `n=4`, you get 4 entries in `choices`.
* **Every `choice.message.content`** is an array with a single `{ "type": "image", "image": "..." }` part.
* `image` is a short-lived URL (download it soon) or base64 data, depending on your workspace configuration.
* `usage.total_tokens` reflects the small token cost of the request framing — **billing is per-image** at the rate in the table above, not per token.

## Image-to-image

Prepend an `image_url` part to the `content` array and follow it with a text instruction:

```json theme={null}
{
  "model": "wan2.7-image-pro",
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "image_url", "image_url": { "url": "https://example.com/reference.jpg" } },
        { "type": "text", "text": "Transform into an oil painting in the style of Van Gogh" }
      ]
    }
  ],
  "n": 1
}
```

## Why the playground shows the Chat Completions path

The playground sends exactly the same `POST /v1/chat/completions` request the standard [OpenAI Chat](/api-reference/chat/createchatcompletion) endpoint uses — only the `model` and `content` shape are tuned for images. Your existing OpenAI-compatible SDK code works without modification; just swap the model and content shape.

## Common 4xx causes

* `400 invalid_parameter_error — Input should be a valid list: messages[*].content` — `content` was passed as a string; wrap in an array of typed parts.
* `400` referencing `messages` — you sent the Gemini-style `contents`/`parts`. Use `messages` with OpenAI multimodal parts for Wan models.
* `404 openai_error` on `/v1/images/generations` — wrong endpoint. Wan models do **not** route through that path.
* `500 model_not_found` — your workspace isn't provisioned for the Wan family. Contact support.

See [Error Codes](/api-reference/errors) and [Rate Limits](/api-reference/rate-limits) for more.

## Related

<CardGroup cols={3}>
  <Card title="OpenAI Chat" icon="message" href="/api-reference/chat/createchatcompletion">
    The same endpoint used for text models.
  </Card>

  <Card title="Gemini generateContent" icon="google" href="/api-reference/chat/generatecontent">
    Image preview through the Gemini 3 Pro endpoint.
  </Card>

  <Card title="Media Gen skill" icon="image" href="/agent-skills/mediagen">
    Agent skill that wraps image + video generation.
  </Card>
</CardGroup>


## OpenAPI

````yaml openapi/chat-image-generation.json POST /chat/completions
openapi: 3.0.3
info:
  title: Image Generation via Chat Completions
  version: 1.0.0
  description: >-
    Wan 2.7 image models (`wan2.7-image`, `wan2.7-image-pro`) are exposed
    through the standard `POST /v1/chat/completions` endpoint rather than
    `/v1/images/generations`. Send a chat request with a multimodal `content`
    array; AIsa returns `choices[].message.content[]` containing one or more
    `{type: "image"}` parts.
servers:
  - url: https://api.aisa.one/v1
security:
  - BearerAuth: []
paths:
  /chat/completions:
    post:
      summary: Generate images via Chat Completions (wan2.7 family)
      description: >-
        Generate images with the Wan 2.7 image models. Request shape matches
        OpenAI Chat Completions with multimodal content; the response contains
        `choices[].message.content[]` where each item is `{type: "image", image:
        "<url or base64>"}`.


        **Important:** `messages[].content` must be an **array of typed parts**,
        not a plain string. Passing a string returns `400
        invalid_parameter_error` with `Input should be a valid list:
        messages[*].content`.


        By default `wan2.7-image` returns **4 candidate images** (billed per
        image). Set `n` to request a different count.
      operationId: generateImageViaChat
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - model
                - messages
              properties:
                model:
                  type: string
                  enum:
                    - wan2.7-image
                    - wan2.7-image-pro
                  description: >-
                    Image-generation model. `wan2.7-image` ($0.030/image) for
                    standard quality, `wan2.7-image-pro` ($0.075/image) for
                    higher fidelity.
                messages:
                  type: array
                  description: >-
                    Conversation messages. Image prompts go in the last user
                    message's `content` array as `{type: "text"}` parts.
                  items:
                    type: object
                    required:
                      - role
                      - content
                    properties:
                      role:
                        type: string
                        enum:
                          - system
                          - user
                          - assistant
                      content:
                        type: array
                        description: >-
                          Multimodal parts. For image generation, include at
                          least one `{type: "text"}` part with the prompt.
                        items:
                          type: object
                          required:
                            - type
                          properties:
                            type:
                              type: string
                              enum:
                                - text
                                - image_url
                            text:
                              type: string
                              description: 'Used when `type: "text"`.'
                            image_url:
                              type: object
                              description: >-
                                Used when `type: "image_url"` (image-to-image
                                use cases).
                              properties:
                                url:
                                  type: string
                                  format: uri
                'n':
                  type: integer
                  minimum: 1
                  maximum: 4
                  default: 4
                  description: >-
                    Number of images to generate. `wan2.7-image` returns 4 by
                    default; pass `1` to save cost.
            examples:
              basic:
                summary: Single-image prompt (n=1)
                value:
                  model: wan2.7-image
                  messages:
                    - role: user
                      content:
                        - type: text
                          text: A cute red panda, ultra-detailed, cinematic lighting
                  'n': 1
              four_variants:
                summary: Default 4 candidates for selection
                value:
                  model: wan2.7-image
                  messages:
                    - role: user
                      content:
                        - type: text
                          text: >-
                            A futuristic cyberpunk city, neon lights, rainy
                            night, 8k
              pro:
                summary: Higher-fidelity pro model
                value:
                  model: wan2.7-image-pro
                  messages:
                    - role: user
                      content:
                        - type: text
                          text: >-
                            Oil painting of a rolling hillside at sunset,
                            artstation
                  'n': 1
              image_to_image:
                summary: Image-to-image (reference + prompt)
                value:
                  model: wan2.7-image-pro
                  messages:
                    - role: user
                      content:
                        - type: image_url
                          image_url:
                            url: https://example.com/reference.jpg
                        - type: text
                          text: >-
                            Transform into an oil painting in the style of Van
                            Gogh
                  'n': 1
      responses:
        '200':
          description: >-
            Images generated. Returned as Chat Completion with
            `message.content[]` image parts.
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: chatcmpl-fcc86dfd-9424-9523-b0bd-cdf07383bee2
                  object:
                    type: string
                    example: chat.completion
                  created:
                    type: integer
                    example: 1776495713
                  model:
                    type: string
                    example: wan2.7-image
                  choices:
                    type: array
                    description: One entry per generated image.
                    items:
                      type: object
                      properties:
                        index:
                          type: integer
                          nullable: true
                        finish_reason:
                          type: string
                          example: stop
                        message:
                          type: object
                          properties:
                            role:
                              type: string
                              example: assistant
                            content:
                              type: array
                              items:
                                type: object
                                required:
                                  - type
                                properties:
                                  type:
                                    type: string
                                    enum:
                                      - image
                                  image:
                                    type: string
                                    description: >-
                                      Short-lived URL to the generated image (or
                                      base64-encoded data, depending on your
                                      account configuration).
                  usage:
                    type: object
                    properties:
                      prompt_tokens:
                        type: integer
                      completion_tokens:
                        type: integer
                      total_tokens:
                        type: integer
              example:
                id: chatcmpl-fcc86dfd-9424-9523-b0bd-cdf07383bee2
                object: chat.completion
                created: 1776495713
                model: wan2.7-image
                choices:
                  - index: 0
                    finish_reason: stop
                    message:
                      role: assistant
                      content:
                        - type: image
                          image: https://cdn.aisa.one/images/wan2.7/20260418-abc.png
                usage:
                  prompt_tokens: 104
                  completion_tokens: 8
                  total_tokens: 112
        '400':
          description: >-
            Invalid request. Most common: `content` passed as a string instead
            of an array → `"Input should be a valid list: messages[*].content"`.
        '401':
          description: Missing or invalid AIsa API key.
        '429':
          description: Rate limit hit.
        '500':
          description: Internal error.
        '502':
          description: Upstream provider unreachable.
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: AISA API Key

````