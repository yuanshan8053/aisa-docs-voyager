# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 1 个接口，8 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## getAnalystEstimates

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Analyst Estimates | Return consensus Wall Street analyst estimates — projected revenue and earnings per share — for a single US stock ticker, broken down by fiscal period. This is a read-only query: pick annual or quarterly granularity and cap how many periods come back. Typical uses are valuation models, earnings previews, and comparison against actuals. | 返回单只美股的华尔街分析师一致预期 —— 预估营收与每股收益 —— 并按财报周期拆分。这是只读查询:可选年度或季度粒度,并限定返回的周期数量。典型场景为估值建模、财报前瞻,以及与实际值对比。 |
| `param:ticker` | The ticker to get analyst estimates for. | Stock ticker symbol of the US-listed company to pull analyst estimates for, e.g. `AAPL`. One ticker per request. | 要查询分析师预估的美股股票代码,如 `AAPL`。每次请求一只。 |
| `param:period` | The period to get analyst estimates for. Use the /analyst-estimates/periods endpoint to get a list of available periods. Defaults to 'annual'. | Fiscal granularity of the estimates: `annual` for full-year projections, `quarterly` for per-quarter ones. The list of valid periods can be checked via the `/analyst-estimates/periods` endpoint. | 预估的财报粒度:`annual` 为整年预测,`quarterly` 为分季度预测。可用周期可通过 `/analyst-estimates/periods` 接口查询。 |
| `param:limit` | The maximum number of estimates to return (max 3 for annual, 12 for quarterly). | Caps how many of the most recent estimate periods are returned. The accepted ceiling depends on granularity — up to 3 for annual and 12 for quarterly. Higher values are clamped to that ceiling. | 限定返回最近多少个预估周期。上限随粒度而定 —— 年度最多 3 个、季度最多 12 个;超出会被截到上限。 |
| `resp.200.analyst_estimates` |  | List of analyst estimate records, one per fiscal period, ordered from most recent. | 分析师预估记录列表,每个财报周期一条,按时间从近到远排列。 |
| `resp.200.analyst_estimates.fiscal_period` | The fiscal period of the analyst estimate. | The fiscal period the estimate applies to, expressed as the period's date. Combine it with `period` to know whether it denotes a fiscal year or a fiscal quarter. | 该预估对应的财报周期,以周期日期表示。结合 `period` 可判断它代表的是某个财年还是财季。 |
| `resp.200.analyst_estimates.period` | The period of the analyst estimate. | Whether this record is an annual or a quarterly estimate, matching the requested granularity. | 本条记录是年度还是季度预估,与请求的粒度一致。 |
| `resp.200.analyst_estimates.revenue` | The estimated revenue. | Consensus estimated total revenue for the fiscal period, in the company's reporting currency.<br>[⚠️Note:源码未声明金额单位(整额或千/百万),待研发确认。] | 该财报周期的一致预期总营收,以公司报告币种计。<br>[⚠️批注:源码未声明金额单位(整额或千/百万),待研发确认。] |
| `resp.200.analyst_estimates.earnings_per_share` | The estimated earnings per share. | Consensus estimated earnings per share (EPS) for the fiscal period, in the company's reporting currency. | 该财报周期的一致预期每股收益(EPS),以公司报告币种计。 |

