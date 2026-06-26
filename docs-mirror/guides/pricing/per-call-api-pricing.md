> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Per-Call API Pricing – Search, Financial, Twitter & Data APIs

This page explains the pricing model for all non-LLM APIs available through AIsa.

<img src="https://mintcdn.com/aisa/vBu2Gxq6Yg6NR9cA/images/6b7da6af-image.png?fit=max&auto=format&n=vBu2Gxq6Yg6NR9cA&q=85&s=cbf7512437eb4e5d09ca2503df57289e" alt="Per-call API pricing table in the AIsa dashboard showing endpoint names and flat request costs" width="1600" height="576" data-path="images/6b7da6af-image.png" />

These APIs use a **fixed per-request billing model**. Each successful request to an endpoint incurs a predefined charge, independent of response size, token count, or processing time.

Per-call pricing applies to APIs such as:

* Search APIs
* Financial APIs
* YouTube APIs
* Scholar APIs
* Twitter APIs
* Other structured data and retrieval services

## Billing Model Overview

Per-call APIs are billed using a flat-rate structure:

`Total Cost = Number of successful API calls × Per-call price`

Each endpoint has its own fixed cost per request, listed in USD.

Unlike AI model inference:

* There is no input/output token billing
* Response length does not affect cost
* Streaming does not apply

## What Counts as a Billable Call

A billable event occurs when:

* A request is successfully processed by the endpoint
* A response is returned

If a request fails before processing (for example, due to authentication errors), it typically does not generate usage charges. Actual billed events can be verified in the **Usage Logs** page.

## Endpoint-Based Pricing

Each per-call API endpoint has its own defined cost.

In the Marketplace, each listing displays:

* Endpoint name
* API path
* Price per call (USD)

Example format:

`$0.020000 / per call`

Pricing varies by endpoint and may reflect:

* Data source cost
* Upstream provider fees
* Processing complexity

Always refer to the Marketplace for the latest pricing.

## Retries and Duplicate Requests

Because billing is per request:

* Each successful call is billed independently
* Retried requests that are processed successfully will incur additional charges

It is recommended to implement idempotency and retry handling carefully within your application logic.

## Rate Limits and Billing

Rate limits (such as RPM restrictions) control traffic flow but do not alter pricing.

* If a request is accepted and processed, it is billed
* If a request is rejected due to rate limiting, it does not incur usage charges

## Group-Based Pricing

If your workspace uses multiple groups, per-call pricing may vary by group.

Group-level pricing rules or ratios (if configured) are applied automatically during billing. The final amount applied is shown on the **Usage Logs** page.

## Usage Visibility and Cost Transparency

All per-call API activity appears in **Usage Logs**, where you can review:

* Timestamp
* API key used
* Group
* Endpoint
* Final cost charged

This allows you to:

* Audit usage patterns
* Monitor endpoint-level spend
* Verify billing accuracy

## Important Notes

* All prices are listed in USD.
* Billing is triggered per successful API request.
* There is no token-based billing for these endpoints.
* Response size does not impact cost.
* Pricing may change as endpoints evolve.
* Refer to the Marketplace for up-to-date pricing.
