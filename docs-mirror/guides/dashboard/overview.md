> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Dashboard Overview – Monitor Your LLM API Usage

The **Overview** dashboard gives you a consolidated view of your AIsa workspace. It shows your available balance, API activity, resource consumption, and model usage in real time, allowing you to quickly assess whether your integration is working as expected and how your usage is evolving.

<img src="https://mintcdn.com/aisa/vBu2Gxq6Yg6NR9cA/images/182b273d-Screenshot_2026-01-29_184007.png?fit=max&auto=format&n=vBu2Gxq6Yg6NR9cA&q=85&s=57a3c90042c087da410cac1c9200fbef" alt="AIsa dashboard overview showing account balance, usage statistics, resource consumption, and model activity panels" width="1919" height="1107" data-path="images/182b273d-Screenshot_2026-01-29_184007.png" />

<br />

This page is typically the first place to check after setting up an API key, sending test requests, or monitoring ongoing usage in production.

## Account Data

The Account Data section reflects the current financial state of your account.

<img src="https://mintcdn.com/aisa/vBu2Gxq6Yg6NR9cA/images/553e6515-image.png?fit=max&auto=format&n=vBu2Gxq6Yg6NR9cA&q=85&s=41438d57dc7f4a7459b1714378aabe34" alt="Account Data panel showing current balance, used amount, and top-up button" width="425" height="178" data-path="images/553e6515-image.png" />

**Current Balance** shows the amount of credit available for API usage. New accounts start with **\$2.00 in free credits**, which are deducted automatically as requests are processed.

**Used** represents the total amount consumed so far across all API calls.

If your balance runs low, you can add credits using the **Top Up** action. All values update automatically as usage occurs.

## Usage Statistics

Usage Statistics provide a quick confirmation that requests are reaching AIsa.

<img src="https://mintcdn.com/aisa/vBu2Gxq6Yg6NR9cA/images/a19eb45d-image.png?fit=max&auto=format&n=vBu2Gxq6Yg6NR9cA&q=85&s=ac0317ae6dae5faa31babf19ae2f5aa7" alt="Usage Statistics panel showing total number of API requests and statistical count" width="423" height="179" data-path="images/a19eb45d-image.png" />

**Number of Requests** shows how many API calls have been received within the selected time window.

**Statistical Count** is an internal aggregation metric used for usage tracking and reporting.

Together, these indicators help you verify activity before inspecting detailed request logs.

## Resource Consumption

The Resource Consumption panel tracks how much of your account quota is being used.

<img src="https://mintcdn.com/aisa/vBu2Gxq6Yg6NR9cA/images/5d300378-image.png?fit=max&auto=format&n=vBu2Gxq6Yg6NR9cA&q=85&s=970a29e2cbdab43b9735f8ce2a2343a3" alt="Resource Consumption panel showing statistical quota and total tokens processed" width="420" height="180" data-path="images/5d300378-image.png" />

**Statistical Quota** represents total usage in monetary terms.

**Statistical Tokens** shows the total number of tokens processed across all requests.

When no traffic has been generated, these values remain at zero. As usage grows, this section becomes the primary reference for cost visibility.

## Performance Indicators

Performance Indicators describe how your requests are being processed over time.

<img src="https://mintcdn.com/aisa/vBu2Gxq6Yg6NR9cA/images/2baef908-image.png?fit=max&auto=format&n=vBu2Gxq6Yg6NR9cA&q=85&s=963916831cebea16afeab72003f122c7" alt="Performance Indicators panel showing average requests per minute and tokens per minute" width="420" height="185" data-path="images/2baef908-image.png" />

**Average RPM (Requests Per Minute)** shows the average request throughput.

**Average TPM (Tokens Per Minute)** shows the average token processing rate.

These metrics are useful for understanding traffic patterns and identifying spikes or sustained load.

## Model Data Analysis

Model Data Analysis breaks down usage by model.

<img src="https://mintcdn.com/aisa/vBu2Gxq6Yg6NR9cA/images/cffe84fe-image.png?fit=max&auto=format&n=vBu2Gxq6Yg6NR9cA&q=85&s=2fc70e528e20366a1ca333933eb56dd0" alt="Model Data Analysis charts showing consumption distribution and usage trends grouped by AI model" width="1266" height="487" data-path="images/cffe84fe-image.png" />

The **Consumption Distribution** view visualizes total usage and spend over time, grouped by model, helping you understand which models are driving cost and volume.

Additional views allow you to analyze usage trends, compare call distribution across models, and rank models by activity. These charts populate once sufficient traffic is available.

## API Information

The API Information panel displays configuration details related to API access.

If this section shows **No API information**, it usually means no API keys have been created yet or API configuration has not been completed. API keys can be created and managed from the **API Keys** section in the sidebar.

## System Notice

System Notice displays platform-level announcements or operational messages relevant to your workspace. If no notices are configured, this section remains empty.

## Service Status

Service Status shows uptime and monitoring information for AIsa services associated with your account. If monitoring is not configured, this section will not display any data.

## Related

<CardGroup cols={3}>
  <Card title="Model Playground" icon="flask" href="/guides/dashboard/playground">
    Test any model in the browser before writing code.
  </Card>

  <Card title="Usage Logs" icon="chart-line" href="/guides/dashboard/usage-logs">
    Per-request cost, latency, and audit trail.
  </Card>

  <Card title="Wallet" icon="wallet" href="/guides/pricing/wallet">
    Top up credits and manage billing.
  </Card>
</CardGroup>
