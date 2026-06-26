# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 2 个接口，14 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## getInterestRatesHistorical

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Historical interest rates for all major central banks in the world. | Return the historical policy interest-rate series for a single central bank, optionally bounded to a date window. This is a read-only time-series query: omit the dates to get the full available history, or set a start and/or end to slice a range. Typical uses are charting rate trends and back-testing rate-sensitive models. | 返回单个央行的历史政策利率序列,可选地限定日期区间。这是只读的时间序列查询:不传日期则取全部可得历史,或设定起止日期截取某段区间。典型场景为绘制利率走势、回测对利率敏感的模型。 |
| `param:bank` | The bank whose interest rates to return. Use the /macro/interest-rates/banks endpoint to get a list of available banks. | Identifier of the central bank whose rate history to return, e.g. `FED` or `ECB`. The full list of accepted bank codes is available from the `/macro/interest-rates/banks` endpoint. | 要查询利率历史的央行标识,如 `FED`、`ECB`。完整的可用央行代码可通过 `/macro/interest-rates/banks` 接口获取。 |
| `param:start_date` | The start date of the interest rates to return in YYYY-MM-DD format. | Lower bound of the date window, in `YYYY-MM-DD`. Records on or after this date are returned. Omit it to start from the earliest available record. | 日期区间的下界,格式 `YYYY-MM-DD`,返回该日期及之后的记录。留空则从最早的可得记录开始。 |
| `param:end_date` | The end date of the interest rates to return in YYYY-MM-DD format. | Upper bound of the date window, in `YYYY-MM-DD`. Records on or before this date are returned. Omit it to run through the most recent record. | 日期区间的上界,格式 `YYYY-MM-DD`,返回该日期及之前的记录。留空则一直取到最新记录。 |
| `resp.200.interest_rates` |  | The current rate record for the requested bank. Returned as a list for shape consistency with the historical endpoint, typically holding the single latest observation. | 所查央行的当前利率记录。为与历史接口保持结构一致而以列表返回,通常只含最新一条观测。 |
| `resp.200.interest_rates.bank` | The symbol of the central bank. | Code of the central bank this record belongs to, matching the `bank` you queried. | 本条记录所属央行的代码,与查询的 `bank` 一致。 |
| `resp.200.interest_rates.name` | The name of the central bank. | Full human-readable name of the central bank. | 央行的完整可读名称。 |
| `resp.200.interest_rates.rate` | The interest rate of the central bank. | The bank's policy interest rate currently in effect.<br>[⚠️Note:源码未声明利率单位(百分数还是小数,如 5.25 还是 0.0525),待研发确认。] | 该央行当前生效的政策利率。<br>[⚠️批注:源码未声明利率单位(百分数还是小数,如 5.25 还是 0.0525),待研发确认。] |
| `resp.200.interest_rates.date` | The date of the interest rate in YYYY-MM-DD format. | Date this current rate took effect, in `YYYY-MM-DD`. | 该当前利率的生效日期,格式 `YYYY-MM-DD`。 |

## getInterestRatesSnapshot

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get the current interest rates from all major central banks in the world. | Return the current policy interest rate for a single central bank — the latest point in its rate series, not the full history. Use it when you only need the rate in effect right now, e.g. for a live dashboard or a one-off lookup. | 返回单个央行当前的政策利率 —— 即其利率序列的最新一点,而非完整历史。当你只需当下生效的利率时使用,例如实时看板或一次性查询。 |
| `param:bank` | The central bank code (e.g., FED, ECB, BOJ). Use the /macro/interest-rates/banks endpoint to get a list of available banks. | Identifier of the central bank whose current rate to return, e.g. `FED`, `ECB`, `BOJ`. The full list of accepted bank codes is available from the `/macro/interest-rates/banks` endpoint. | 要查询当前利率的央行标识,如 `FED`、`ECB`、`BOJ`。完整的可用央行代码可通过 `/macro/interest-rates/banks` 接口获取。 |
| `resp.200.interest_rates` |  | The current rate record for the requested bank. Returned as a list for shape consistency with the historical endpoint, typically holding the single latest observation. | 所查央行的当前利率记录。为与历史接口保持结构一致而以列表返回,通常只含最新一条观测。 |
| `resp.200.interest_rates.bank` | The symbol of the central bank. | Code of the central bank this record belongs to, matching the `bank` you queried. | 本条记录所属央行的代码,与查询的 `bank` 一致。 |
| `resp.200.interest_rates.name` | The name of the central bank. | Full human-readable name of the central bank. | 央行的完整可读名称。 |
| `resp.200.interest_rates.rate` | The interest rate of the central bank. | The bank's policy interest rate currently in effect.<br>[⚠️Note:源码未声明利率单位(百分数还是小数,如 5.25 还是 0.0525),待研发确认。] | 该央行当前生效的政策利率。<br>[⚠️批注:源码未声明利率单位(百分数还是小数,如 5.25 还是 0.0525),待研发确认。] |
| `resp.200.interest_rates.date` | The date of the interest rate in YYYY-MM-DD format. | Date this current rate took effect, in `YYYY-MM-DD`. | 该当前利率的生效日期,格式 `YYYY-MM-DD`。 |

