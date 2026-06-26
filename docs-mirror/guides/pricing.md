> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AIsa Pricing – Usage-Based Billing for LLMs & Data APIs

AIsa uses a usage-based billing system. Charges are applied based on the type of API you use.

There are two distinct pricing models:

1. **AI Model (LLM) Pricing:** billed per token
2. **Per-Call API Pricing:** billed per request

This page provides a high-level overview of both models and links to their detailed pricing pages.

## 1. AI Model (LLM) Pricing

AI model APIs are billed based on token usage.

<img src="https://mintcdn.com/aisa/vBu2Gxq6Yg6NR9cA/images/50b7cb91-Screenshot_2026-03-13_165258.png?fit=max&auto=format&n=vBu2Gxq6Yg6NR9cA&q=85&s=5298ef8771c63eaa4fca5614df1c0482" alt="AIsa AI model pricing overview showing token-based billing for LLM inference" width="1919" height="1108" data-path="images/50b7cb91-Screenshot_2026-03-13_165258.png" />

Each request is charged separately for:

* **Input tokens** (prompt tokens)
* **Output tokens** (generated tokens)

Prices are defined per **1 million tokens (1M tokens)**, and input and output tokens are billed independently.

This pricing model applies to:

* Chat completions
* Text generation
* Vision-enabled models
* Tool-enabled models
* Streaming responses

For the full model pricing table and detailed billing explanation, see **AI Model Pricing**

## 2. Per-Call API Pricing

All non-LLM APIs use a fixed per-request billing model.

<img src="https://mintcdn.com/aisa/vBu2Gxq6Yg6NR9cA/images/a991d244-image.png?fit=max&auto=format&n=vBu2Gxq6Yg6NR9cA&q=85&s=592cd4cb504085ad2a16cc7d53d53fcb" alt="Per-call API pricing table showing fixed per-request costs for search, financial, Twitter, and data APIs" width="1600" height="576" data-path="images/a991d244-image.png" />

Each successful request to an endpoint incurs a predefined charge, regardless of response size.

This pricing model applies to APIs such as:

* Search APIs
* Financial APIs
* YouTube APIs
* Scholar APIs
* Twitter APIs
* Other structured data and retrieval services

For endpoint-level pricing details and billing behavior, see **Per-Call API Pricing**

## Choosing the Correct Pricing Model

If your API request:

* Uses a language model to generate text → **Token-based pricing applies**
* Retrieves structured data or performs a search → **Per-call pricing applies**

The Marketplace displays the billing type for each model or endpoint.

## Usage Tracking and Transparency

All API activity, whether token-based or per-call, is recorded in:

* **Usage Logs**
* Account billing summaries

You can review:

* Tokens consumed (for AI models)
* Number of requests (for per-call APIs)
* Final cost per request
* Applied pricing rules or group ratios

Charges are deducted from your account balance based on the applicable pricing model.

## Additional Notes

* Pricing is usage-based; no fixed monthly platform fees.
* Pricing may vary by model, provider, group, or endpoint.
* Always refer to the Marketplace for the most up-to-date rates.
* Detailed billing breakdowns are available in Usage Logs.
