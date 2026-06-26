# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 19 个接口，498 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## searchLineItems

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Search for specific financial metrics across income statements, balance sheets, and cash flow statements for a list of tickers. | Search for specific financial line items across income statements, balance sheets, and cash flow statements for one or more tickers. | 在一个或多个股票代码的利润表、资产负债表与现金流量表中检索指定的财务行项目。 |
| `req.line_items` | An array of line items to apply to the search. | List of financial line-item names to retrieve across the supported statements. | 要在各支持报表中检索的财务行项目名称列表。 |
| `req.tickers` | An array of tickers to apply to the search. | List of ticker symbols whose financials are searched. | 要检索其财务数据的股票代码列表。 |
| `req.period` | The time period for the financial data. | Reporting cadence of the financial data to return. | 返回财务数据所采用的报告周期。 |
| `req.limit` | The maximum number of results to return. | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `resp.200.search_results` |  | List of stocks matching all supplied filters. | 满足全部筛选条件的股票列表。 |
| `resp.200.search_results.ticker` | The ticker symbol of the company. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.search_results.report_period` | The reporting period of the financial data. | Date the underlying report covers, marking which fiscal point the figures belong to. | 本条数据所属报告的覆盖日期，标明各数值对应的财报时点。 |
| `resp.200.search_results.period` | The time period of the financial data. | Reporting cadence to which this record's figures correspond. | 本条记录数值所对应的报告周期。 |
| `resp.200.search_results.currency` | The currency of the financial data. | Currency in which the returned financial figures are reported. | 所返回财务数值采用的计价货币。 |

## getInsiderTrades

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get insider trades like buys and sells for a ticker by a company insider. | Retrieve insider buy and sell transactions reported by a company's insiders for the given ticker. | 获取指定股票代码下公司内部人申报的买入与卖出交易记录。 |
| `param:ticker` | The ticker symbol of the company. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `param:limit` | The maximum number of transactions to return (default: 10). | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `param:name` | Filter by insider name (e.g., 'Jen Hsun Huang'). Use the /insider-trades/names endpoint to get available names for a ticker. | Filter results to a specific insider by name; obtain valid names from the insider-trades names endpoint. | 按内部人姓名筛选结果；有效姓名可从内部人姓名查询接口获取。 |
| `param:transaction_type` | Filter by transaction type (e.g., 'Open market sale', 'Gift'). Use the /insider-trades/transaction-types endpoint to get available types. | Filter results to a specific transaction type; obtain valid types from the insider-trades transaction-types endpoint. | 按交易类型筛选结果；有效类型可从内部人交易类型查询接口获取。 |
| `param:filing_date` | Filter by exact filing date in YYYY-MM-DD format. | Return only trades filed on this exact date. | 仅返回在该确切日期申报的交易。 |
| `param:filing_date_gte` | Filter by filing date greater than or equal to this date (YYYY-MM-DD). | Return only trades filed on or after this date. | 仅返回在该日期当天或之后申报的交易。 |
| `param:filing_date_lte` | Filter by filing date less than or equal to this date (YYYY-MM-DD). | Return only trades filed on or before this date. | 仅返回在该日期当天或之前申报的交易。 |
| `param:filing_date_gt` | Filter by filing date greater than this date (YYYY-MM-DD). | Return only trades filed strictly after this date. | 仅返回在该日期之后申报的交易。 |
| `param:filing_date_lt` | Filter by filing date less than this date (YYYY-MM-DD). | Return only trades filed strictly before this date. | 仅返回在该日期之前申报的交易。 |
| `resp.200.insider_trades` |  | List of insider transaction records matching the query. | 符合查询条件的内部人交易记录列表。 |
| `resp.200.insider_trades.ticker` | The ticker symbol of the company. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.insider_trades.issuer` | The name of the issuing company. | Name of the company that issued the traded security. | 发行所交易证券的公司名称。 |
| `resp.200.insider_trades.name` | The name of the insider. | Name of the insider who carried out the transaction. | 实施该交易的内部人姓名。 |
| `resp.200.insider_trades.title` | The title of the insider. | Role or title the insider holds at the company. | 内部人在公司担任的职务或头衔。 |
| `resp.200.insider_trades.is_board_director` | Whether the insider is a board director. | Whether the insider serves on the company's board of directors. | 该内部人是否为公司董事会成员。 |
| `resp.200.insider_trades.transaction_date` | The date of the transaction. | Date on which the transaction took place. | 交易发生的日期。 |
| `resp.200.insider_trades.transaction_shares` | The number of shares involved in the transaction. | Number of shares bought or sold in the transaction. | 本次交易买入或卖出的股数。 |
| `resp.200.insider_trades.transaction_price_per_share` | The price per share in the transaction. | Price per share at which the transaction was executed. | 本次交易成交的每股价格。 |
| `resp.200.insider_trades.transaction_value` | The total value of the transaction. | Total monetary value of the transaction. | 本次交易的总金额。 |
| `resp.200.insider_trades.shares_owned_before_transaction` | The number of shares owned before the transaction. | Shares the insider held before the transaction. | 交易发生前该内部人持有的股数。 |
| `resp.200.insider_trades.shares_owned_after_transaction` | The number of shares owned after the transaction. | Shares the insider held after the transaction. | 交易发生后该内部人持有的股数。 |
| `resp.200.insider_trades.security_title` | The title of the security involved in the transaction. | Title of the security involved in the transaction. | 本次交易所涉证券的名称。 |
| `resp.200.insider_trades.filing_date` | The date the transaction was filed. | Date the transaction was filed with the regulator. | 该交易向监管机构申报的日期。 |

## getInstitutionalOwnership

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get institutional ownership by investor or ticker. Requires either investor or ticker parameter, but not both. | Retrieve institutional equity holdings, queried either by investment manager or by ticker (supply exactly one of the two). | 按投资管理人或股票代码查询机构持有的股权头寸（二者须且仅须提供其一）。 |
| `param:investor` | The name of the investment manager | Name of the investment manager whose holdings to retrieve. | 要查询其持仓的投资管理人名称。 |
| `param:ticker` | The ticker symbol, if queried by investor. | Ticker symbol whose institutional holders to retrieve. | 要查询其机构持有人的股票代码。 |
| `param:limit` | The maximum number of holdings to return (default: 10). | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `resp.200.institutional-ownership` |  | List of institutional holding records matching the query. | 符合查询条件的机构持仓记录列表。 |
| `resp.200.institutional-ownership.ticker` | The ticker symbol, if queried by investor. | Ticker symbol of the held security; populated when querying by investor. | 所持证券的股票代码；按投资管理人查询时返回。 |
| `resp.200.institutional-ownership.investor` | The investor name, if queried by ticker. | Name of the holding investment manager; populated when querying by ticker. | 持有该证券的投资管理人名称；按股票代码查询时返回。 |
| `resp.200.institutional-ownership.report_period` | The reporting period of the institutional ownership. | Reporting period to which this holding record corresponds. | 本持仓记录所对应的报告期。 |
| `resp.200.institutional-ownership.price` | The estimated purchase price of the equity position. | Estimated purchase price of the equity position. | 该股权头寸的估算买入价格。 |
| `resp.200.institutional-ownership.shares` | The number of shares held by the investment manager. | Number of shares held in the position. | 该头寸持有的股数。 |
| `resp.200.institutional-ownership.market_value` | The market value of the equity position. | Market value of the equity position. | 该股权头寸的市值。 |

## getCompanyFacts

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get company facts for a ticker. | Retrieve descriptive company facts and identifiers for the given ticker. | 获取指定股票代码下公司的概况信息与标识。 |
| `param:ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `param:cik` | The CIK of the company. | SEC Central Index Key identifying the company; an alternative lookup key to the ticker. | 公司在 SEC 的中央索引号（CIK），可作为股票代码之外的查询键。 |
| `resp.200.company_facts` |  | Descriptive facts and identifiers for the company. | 公司的概况信息与标识。 |
| `resp.200.company_facts.ticker` | The ticker symbol of the company. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.company_facts.name` | The name of the company. | Full legal or common name of the company. | 公司的法定或通用名称。 |
| `resp.200.company_facts.cik` | The Central Index Key (CIK) of the company. | SEC Central Index Key assigned to the company. | SEC 为该公司分配的中央索引号（CIK）。 |
| `resp.200.company_facts.industry` | The industry of the company. | Industry classification of the company. | 公司所属的行业分类。 |
| `resp.200.company_facts.sector` | The sector of the company. | Sector classification of the company. | 公司所属的板块分类。 |
| `resp.200.company_facts.category` | The category of the company. | Business category of the company. | 公司的业务类别。 |
| `resp.200.company_facts.exchange` | The exchange of the company. | Stock exchange on which the company is listed. | 公司挂牌上市的证券交易所。 |
| `resp.200.company_facts.is_active` | Whether the company is currently active. | Whether the company is currently active. | 公司目前是否处于存续状态。 |
| `resp.200.company_facts.listing_date` | The date the company was listed on the stock exchange. | Date the company was listed on the exchange. | 公司在交易所挂牌上市的日期。 |
| `resp.200.company_facts.location` | The location of the company. | Geographic location of the company. | 公司所在的地理位置。 |
| `resp.200.company_facts.market_cap` | The market capitalization of the company. | Market capitalization of the company. | 公司的总市值。 |
| `resp.200.company_facts.number_of_employees` | The number of employees at the company. | Total number of employees at the company. | 公司的员工总数。 |
| `resp.200.company_facts.sec_filings_url` | The URL of the company's SEC filings. | URL to the company's SEC filings. | 公司 SEC 备案文件的链接。 |
| `resp.200.company_facts.sic_code` | The Standard Industrial Classification (SIC) code of the company. | Standard Industrial Classification code of the company. | 公司的标准产业分类（SIC）代码。 |
| `resp.200.company_facts.sic_industry` | The industry of the company based on the SIC code. | Industry derived from the company's SIC code. | 依据 SIC 代码归类的公司行业。 |
| `resp.200.company_facts.sic_sector` | The sector of the company based on the SIC code. | Sector derived from the company's SIC code. | 依据 SIC 代码归类的公司板块。 |
| `resp.200.company_facts.website_url` | The URL of the company's website. | URL of the company's website. | 公司官方网站的链接。 |
| `resp.200.company_facts.weighted_average_shares` | The weighted average shares of the company. | Weighted-average shares outstanding for the company. | 公司的加权平均流通股数。 |

## getFilings

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get SEC filings for a company. | Retrieve the list of SEC filings submitted by a company. | 获取公司向 SEC 提交的备案文件列表。 |
| `param:cik` | The Central Index Key (CIK) of the company. | SEC Central Index Key identifying the company; an alternative lookup key to the ticker. | 公司在 SEC 的中央索引号（CIK），可作为股票代码之外的查询键。 |
| `param:ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `param:filing_type` | Filter by one or more filing types. Repeat the query parameter to pass multiple values (e.g. filing_type=10-Q&filing_type=10-K). | Filter by one or more SEC filing types; repeat the parameter to pass multiple values. | 按一种或多种 SEC 备案类型筛选；重复该参数可传入多个值。 |
| `param:limit` | The maximum number of filings to return (default: 10). | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `resp.200.filings` |  | List of SEC filings matching the query. | 符合查询条件的 SEC 备案文件列表。 |
| `resp.200.filings.cik` | The Central Index Key (CIK) of the company. | SEC Central Index Key of the filing company. | 备案公司的 SEC 中央索引号（CIK）。 |
| `resp.200.filings.accession_number` | The accession number of the filing. | SEC accession number uniquely identifying the filing. | 唯一标识该备案的 SEC 受理编号。 |
| `resp.200.filings.filing_type` | The type of the SEC filing (e.g., 10-Q, 8-K). | SEC form type of the filing. | 该备案的 SEC 表格类型。 |
| `resp.200.filings.report_date` | The date of the report. | Date the filing's report covers. | 该备案报告所覆盖的日期。 |
| `resp.200.filings.ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.filings.url` | The URL of the SEC filing. | URL to the filing on the SEC website. | 该备案在 SEC 网站上的链接。 |

## getFilingItems

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get the raw text Items from an SEC filing. | Retrieve the raw text of individual Items within a specific SEC filing. | 获取某份 SEC 备案文件中各独立条目（Item）的原始正文。 |
| `param:ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `param:filing_type` | The type of filing. | SEC form type of the filing to read items from. | 要读取条目的备案 SEC 表格类型。 |
| `param:year` | The year of the filing. | Filing year to select. | 要选取的备案年份。 |
| `param:quarter` | The quarter of the filing if 10-Q. | Filing quarter, used for 10-Q filings. | 备案季度，用于 10-Q 季报。 |
| `param:item` | The item to get. | Specific filing Item to retrieve. | 要获取的具体备案条目（Item）。 |
| `param:accession_number` | The accession number of the filing if 8-K. | Accession number identifying the filing, used for 8-K filings. | 标识该备案的受理编号，用于 8-K 文件。 |
| `param:include_exhibits` | Whether to include the raw text from linked exhibits. Only applicable for 8-K filings. When true, exhibit objects will include the 'text' field containing the full exhibit content. | Whether to include the raw text of linked exhibits; applies only to 8-K filings, and when enabled each exhibit object carries its full text. | 是否包含所链接附件的原始正文；仅对 8-K 文件生效，启用后每个附件对象将携带其完整正文。 |
| `resp.200.ticker` | The ticker symbol of the company. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.cik` | The Central Index Key (CIK) of the company. | SEC Central Index Key of the filing company. | 备案公司的 SEC 中央索引号（CIK）。 |
| `resp.200.filing_type` | The type of filing. | SEC form type of the filing. | 该备案的 SEC 表格类型。 |
| `resp.200.accession_number` | The accession number of the filing. | SEC accession number identifying the filing. | 标识该备案的 SEC 受理编号。 |
| `resp.200.year` | The year of the filing. | Year of the filing. | 备案所属年份。 |
| `resp.200.quarter` | The quarter of the filing. | Quarter of the filing. | 备案所属季度。 |
| `resp.200.items` |  | List of Item sections extracted from the filing. | 从该备案中抽取的条目（Item）小节列表。 |
| `resp.200.items.number` | The item number. | Identifier of the filing Item. | 备案条目的编号。 |
| `resp.200.items.name` | The item name. | Title of the filing Item. | 备案条目的标题。 |
| `resp.200.items.text` | The item text. | Raw text content of the filing Item. | 备案条目的原始正文内容。 |

## getSegmentedRevenues

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Deprecated. Use /financials/income-statements/segments instead. | Deprecated. Retrieve revenue broken down by reporting segment; use the income-statement segments endpoint instead. | 已废弃。按报告分部拆分获取营业收入，建议改用利润表分部接口。 |
| `param:ticker` | The ticker symbol. Required if cik is not provided. | Stock ticker symbol of the company; required when `cik` is not provided. | 目标公司的股票代码；未提供 `cik` 时必填。 |
| `param:period` | The date or time period to which the reported revenue data relates in ISO 8601 format (YYYY-MM-DD). | Date or time period the reported revenue relates to, in ISO 8601 format. | 所报告营收对应的日期或时间区间，采用 ISO 8601 格式。 |
| `param:limit` | The maximum number of revenue statements to return. | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `param:cik` | The Central Index Key (CIK) of the company. | SEC Central Index Key identifying the company; an alternative lookup key to the ticker. | 公司在 SEC 的中央索引号（CIK），可作为股票代码之外的查询键。 |
| `resp.200.segmented_revenues` |  | List of segmented-revenue records for the company. | 公司分部营收记录列表。 |
| `resp.200.segmented_revenues.ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.segmented_revenues.report_period` | The reporting period of the revenue. | Date the underlying report covers, marking which fiscal point the figures belong to. | 本条数据所属报告的覆盖日期，标明各数值对应的财报时点。 |
| `resp.200.segmented_revenues.period` | The time period of the revenue. | Reporting cadence to which this record's figures correspond. | 本条记录数值所对应的报告周期。 |
| `resp.200.segmented_revenues.items` | An array of revenue segments from SEC filings (10-Ks and 10-Qs) in XBRL format | Revenue segments parsed from SEC 10-K and 10-Q filings in XBRL form. | 从 SEC 10-K 与 10-Q 备案的 XBRL 数据中解析出的营收分部。 |
| `resp.200.segmented_revenues.items.name` | The name of the revenue segment. | Name of the revenue segment. | 该营收分部的名称。 |
| `resp.200.segmented_revenues.items.amount` | The numerical amount reported for the specified financial metric, expressed in the company's reporting currency; default is USD. | Reported revenue amount for the segment, in the company's reporting currency (default USD). | 该分部报告的营收金额，以公司报告货币计价（默认美元）。 |
| `resp.200.segmented_revenues.items.end_period` | The end period of the revenue segment.  Only provided for quarterly data. | End of the segment's reporting interval; provided only for quarterly data. | 该分部报告区间的结束时点；仅季度数据提供。 |
| `resp.200.segmented_revenues.items.start_period` | The start period of the revenue segment.  Only provided for quarterly data. | Start of the segment's reporting interval; provided only for quarterly data. | 该分部报告区间的起始时点；仅季度数据提供。 |
| `resp.200.segmented_revenues.items.segments` |  | Dimension breakdown describing how the segment is classified. | 描述该分部如何归类的维度拆分。 |
| `resp.200.segmented_revenues.items.segments.label` | The label for the revenue segment. | Label of the segment dimension. | 分部维度的标签。 |
| `resp.200.segmented_revenues.items.segments.type` | The type of revenue segment. | Type of the segment dimension. | 分部维度的类型。 |

## getIncomeStatements

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get income statements for a ticker. | Retrieve income statements for the given ticker. | 获取指定股票代码的利润表。 |
| `param:ticker` | The ticker symbol. Required if cik is not provided. | Stock ticker symbol of the company; required when `cik` is not provided. | 目标公司的股票代码；未提供 `cik` 时必填。 |
| `param:period` | The time period of the income statements. | Reporting cadence of the financial data to return. | 返回财务数据所采用的报告周期。 |
| `param:limit` | The maximum number of income statements to return. | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `param:cik` | The Central Index Key (CIK) of the company. | SEC Central Index Key identifying the company; an alternative lookup key to the ticker. | 公司在 SEC 的中央索引号（CIK），可作为股票代码之外的查询键。 |
| `resp.200.income_statements` |  | List of income statement records for the ticker. | 该股票代码的利润表记录列表。 |
| `resp.200.income_statements.ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.income_statements.report_period` | The reporting period of the income statement. | Date the underlying report covers, marking which fiscal point the figures belong to. | 本条数据所属报告的覆盖日期，标明各数值对应的财报时点。 |
| `resp.200.income_statements.fiscal_period` | The fiscal period of the income statement. | Issuer's fiscal-period label for the reporting interval. | 本报告区间对应的公司财年周期标签。 |
| `resp.200.income_statements.period` | The time period of the income statement. | Reporting cadence to which this record's figures correspond. | 本条记录数值所对应的报告周期。 |
| `resp.200.income_statements.currency` | The currency in which the financial data is reported. | Currency in which the monetary figures in this record are reported. | 本条记录中各金额数值所采用的计价货币。 |
| `resp.200.income_statements.revenue` | The total revenue of the company. | Total sales the company generated over the reporting period. | 公司在报告期内实现的销售总额。 |
| `resp.200.income_statements.cost_of_revenue` | The cost of revenue of the company. | Direct costs attributable to producing the goods or services sold. | 与所售商品或服务直接相关的生产成本。 |
| `resp.200.income_statements.gross_profit` | The gross profit of the company. | Revenue remaining after subtracting the cost of revenue. | 营业收入扣除营业成本后的毛利润。 |
| `resp.200.income_statements.operating_expense` | The operating expenses of the company. | Operating costs incurred outside the direct cost of revenue. | 营业成本之外发生的运营费用。 |
| `resp.200.income_statements.selling_general_and_administrative_expenses` | The selling, general, and administrative expenses of the company. | Selling, general, and administrative overhead for the period. | 报告期内的销售、一般及管理费用。 |
| `resp.200.income_statements.research_and_development` | The research and development expenses of the company. | Spending on research and development activities. | 研发活动支出。 |
| `resp.200.income_statements.operating_income` | The operating income of the company. | Profit from core operations before interest and taxes. | 核心经营在扣除利息与税项前产生的营业利润。 |
| `resp.200.income_statements.interest_expense` | The interest expenses of the company. | Cost of interest on the company's borrowings. | 公司债务产生的利息支出。 |
| `resp.200.income_statements.ebit` | The earnings before interest and taxes of the company. | Earnings before interest and taxes. | 息税前利润（EBIT）。 |
| `resp.200.income_statements.income_tax_expense` | The income tax expenses of the company. | Income tax charged against the period's profit. | 计入本期利润的所得税费用。 |
| `resp.200.income_statements.net_income_discontinued_operations` | The net income from discontinued operations of the company. | Net income contributed by operations that have been discontinued. | 已终止经营业务贡献的净利润。 |
| `resp.200.income_statements.net_income_non_controlling_interests` | The net income from non-controlling interests of the company. | Portion of net income attributable to non-controlling (minority) interests. | 归属于非控股（少数股东）权益的净利润部分。 |
| `resp.200.income_statements.net_income` | The net income of the company. | Bottom-line profit after all expenses, interest, and taxes. | 扣除全部费用、利息与税项后的净利润。 |
| `resp.200.income_statements.net_income_common_stock` | The net income available to common stockholders of the company. | Net income attributable to common shareholders after preferred claims. | 扣除优先股索偿后归属于普通股股东的净利润。 |
| `resp.200.income_statements.preferred_dividends_impact` | The impact of preferred dividends on the net income of the company. | Effect of preferred dividends on income available to common shareholders. | 优先股股息对可分配给普通股股东利润的影响。 |
| `resp.200.income_statements.consolidated_income` | The consolidated income of the company. | Total consolidated income including all controlled entities. | 涵盖全部受控主体的合并总收益。 |
| `resp.200.income_statements.earnings_per_share` | The earnings per share of the company. | Net income allocated to each outstanding common share. | 分摊到每股流通普通股的净利润（基本每股收益）。 |
| `resp.200.income_statements.earnings_per_share_diluted` | The diluted earnings per share of the company. | Earnings per share assuming all dilutive securities are converted. | 假设全部稀释性证券转换后的每股收益（稀释每股收益）。 |
| `resp.200.income_statements.dividends_per_common_share` | The dividends per common share of the company. | Dividends declared per common share for the period. | 报告期内每股普通股宣派的股息。 |
| `resp.200.income_statements.weighted_average_shares` | The weighted average shares of the company. | Time-weighted average of common shares outstanding during the period. | 报告期内流通普通股的加权平均股数。 |
| `resp.200.income_statements.weighted_average_shares_diluted` | The diluted weighted average shares of the company. | Diluted weighted-average share count including dilutive securities. | 计入稀释性证券后的加权平均稀释股数。 |

## getBalanceSheets

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get balance sheets for a ticker. | Retrieve balance sheets for the given ticker. | 获取指定股票代码的资产负债表。 |
| `param:ticker` | The ticker symbol. Required if cik is not provided. | Stock ticker symbol of the company; required when `cik` is not provided. | 目标公司的股票代码；未提供 `cik` 时必填。 |
| `param:period` | The time period of the balance sheets. | Reporting cadence of the financial data to return. | 返回财务数据所采用的报告周期。 |
| `param:limit` | The maximum number of balance sheets to return | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `param:cik` | The Central Index Key (CIK) of the company. | SEC Central Index Key identifying the company; an alternative lookup key to the ticker. | 公司在 SEC 的中央索引号（CIK），可作为股票代码之外的查询键。 |
| `resp.200.balance_sheets` |  | List of balance sheet records for the ticker. | 该股票代码的资产负债表记录列表。 |
| `resp.200.balance_sheets.ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.balance_sheets.report_period` | The reporting period of the balance sheet. | Date the underlying report covers, marking which fiscal point the figures belong to. | 本条数据所属报告的覆盖日期，标明各数值对应的财报时点。 |
| `resp.200.balance_sheets.fiscal_period` | The fiscal period of the balance sheet. | Issuer's fiscal-period label for the reporting interval. | 本报告区间对应的公司财年周期标签。 |
| `resp.200.balance_sheets.period` | The time period of the balance sheet. | Reporting cadence to which this record's figures correspond. | 本条记录数值所对应的报告周期。 |
| `resp.200.balance_sheets.currency` | The currency in which the financial data is reported. | Currency in which the monetary figures in this record are reported. | 本条记录中各金额数值所采用的计价货币。 |
| `resp.200.balance_sheets.total_assets` | The total assets of the company. | Sum of all assets the company holds. | 公司持有的全部资产合计。 |
| `resp.200.balance_sheets.current_assets` | The current assets of the company. | Assets expected to be converted to cash or used within one year. | 预计在一年内变现或耗用的流动资产。 |
| `resp.200.balance_sheets.cash_and_equivalents` | The cash and equivalents of the company. | Cash on hand plus highly liquid short-term holdings. | 库存现金及高流动性的短期等价物。 |
| `resp.200.balance_sheets.inventory` | The inventory of the company. | Value of goods held for sale or production. | 为销售或生产而持有的存货价值。 |
| `resp.200.balance_sheets.current_investments` | The current investments of the company. | Short-term investments classified as current assets. | 归类为流动资产的短期投资。 |
| `resp.200.balance_sheets.trade_and_non_trade_receivables` | The trade and non-trade receivables of the company. | Amounts owed to the company from trade and non-trade sources. | 公司应收的贸易与非贸易款项。 |
| `resp.200.balance_sheets.non_current_assets` | The non-current assets of the company. | Assets not expected to be realized within one year. | 预计一年内无法变现的非流动资产。 |
| `resp.200.balance_sheets.property_plant_and_equipment` | The property, plant, and equipment of the company. | Carrying value of property, plant, and equipment. | 房产、厂房及设备的账面价值。 |
| `resp.200.balance_sheets.goodwill_and_intangible_assets` | The goodwill and intangible assets of the company. | Goodwill together with other intangible assets. | 商誉及其他无形资产合计。 |
| `resp.200.balance_sheets.investments` | The investments of the company. | Total investment holdings of the company. | 公司投资持仓合计。 |
| `resp.200.balance_sheets.non_current_investments` | The non-current investments of the company. | Investments held beyond one year. | 持有期超过一年的非流动投资。 |
| `resp.200.balance_sheets.outstanding_shares` | The outstanding shares of the company. | Number of common shares currently issued and outstanding. | 当前已发行并流通在外的普通股股数。 |
| `resp.200.balance_sheets.tax_assets` | The tax assets of the company. | Recognized tax-related assets such as deferred tax assets. | 已确认的税务相关资产，如递延所得税资产。 |
| `resp.200.balance_sheets.total_liabilities` | The total liabilities of the company. | Sum of all the company's liabilities. | 公司全部负债合计。 |
| `resp.200.balance_sheets.current_liabilities` | The current liabilities of the company. | Obligations due within one year. | 一年内到期的流动负债。 |
| `resp.200.balance_sheets.current_debt` | The current debt of the company. | Portion of debt due within one year. | 一年内到期的债务部分。 |
| `resp.200.balance_sheets.trade_and_non_trade_payables` | The trade and non-trade payables of the company. | Amounts the company owes from trade and non-trade sources. | 公司应付的贸易与非贸易款项。 |
| `resp.200.balance_sheets.deferred_revenue` | The deferred revenue of the company. | Payments received for goods or services not yet delivered. | 已收取但尚未交付商品或服务对应的递延收入。 |
| `resp.200.balance_sheets.deposit_liabilities` | The deposit liabilities of the company. | Liabilities arising from customer or counterparty deposits. | 客户或交易对手存入款项形成的存款负债。 |
| `resp.200.balance_sheets.non_current_liabilities` | The non-current liabilities of the company. | Obligations due beyond one year. | 一年以上到期的非流动负债。 |
| `resp.200.balance_sheets.non_current_debt` | The non-current debt of the company. | Portion of debt due beyond one year. | 一年以上到期的债务部分。 |
| `resp.200.balance_sheets.tax_liabilities` | The tax liabilities of the company. | Recognized tax-related obligations such as deferred tax liabilities. | 已确认的税务相关负债，如递延所得税负债。 |
| `resp.200.balance_sheets.shareholders_equity` | The shareholders' equity of the company. | Residual interest in assets after deducting liabilities. | 资产扣除负债后归属于股东的剩余权益。 |
| `resp.200.balance_sheets.retained_earnings` | The retained earnings of the company. | Cumulative earnings retained rather than distributed as dividends. | 历年留存而未作为股息分配的累计利润。 |
| `resp.200.balance_sheets.accumulated_other_comprehensive_income` | The accumulated other comprehensive income of the company. | Cumulative gains and losses recorded outside the income statement. | 计入损益表之外的累计其他综合收益。 |
| `resp.200.balance_sheets.total_debt` | The total debt of the company. | Combined current and non-current interest-bearing debt. | 流动与非流动有息债务合计。 |

## getCashFlowStatements

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get cash flow statements for a ticker. | Retrieve cash flow statements for the given ticker. | 获取指定股票代码的现金流量表。 |
| `param:ticker` | The ticker symbol. Required if cik is not provided. | Stock ticker symbol of the company; required when `cik` is not provided. | 目标公司的股票代码；未提供 `cik` 时必填。 |
| `param:period` | The time period of the cash flow statements. | Reporting cadence of the financial data to return. | 返回财务数据所采用的报告周期。 |
| `param:limit` | The maximum number of cash flow statements to return. | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `param:cik` | The Central Index Key (CIK) of the company. | SEC Central Index Key identifying the company; an alternative lookup key to the ticker. | 公司在 SEC 的中央索引号（CIK），可作为股票代码之外的查询键。 |
| `resp.200.cash_flow_statements` |  | List of cash flow statement records for the ticker. | 该股票代码的现金流量表记录列表。 |
| `resp.200.cash_flow_statements.ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.cash_flow_statements.report_period` | The reporting period of the cash flow statement. | Date the underlying report covers, marking which fiscal point the figures belong to. | 本条数据所属报告的覆盖日期，标明各数值对应的财报时点。 |
| `resp.200.cash_flow_statements.fiscal_period` | The fiscal period of the cash flow statement. | Issuer's fiscal-period label for the reporting interval. | 本报告区间对应的公司财年周期标签。 |
| `resp.200.cash_flow_statements.period` | The time period of the cash flow statement. | Reporting cadence to which this record's figures correspond. | 本条记录数值所对应的报告周期。 |
| `resp.200.cash_flow_statements.currency` | The currency in which the financial data is reported. | Currency in which the monetary figures in this record are reported. | 本条记录中各金额数值所采用的计价货币。 |
| `resp.200.cash_flow_statements.net_income` | The net income of the company. | Net income carried from the income statement as the starting point of the cash flow. | 由损益表结转、作为现金流量起点的净利润。 |
| `resp.200.cash_flow_statements.depreciation_and_amortization` | The depreciation and amortization of the company. | Non-cash depreciation and amortization added back to earnings. | 加回利润的非现金折旧与摊销。 |
| `resp.200.cash_flow_statements.share_based_compensation` | The share-based compensation of the company. | Non-cash expense from share-based employee compensation. | 以股份为基础的员工薪酬产生的非现金费用。 |
| `resp.200.cash_flow_statements.net_cash_flow_from_operations` | The net cash flow from operations of the company. | Net cash generated by core operating activities. | 核心经营活动产生的净现金流。 |
| `resp.200.cash_flow_statements.capital_expenditure` | The capital expenditure of the company. | Cash spent acquiring or upgrading long-term assets. | 用于购置或升级长期资产的资本性支出。 |
| `resp.200.cash_flow_statements.business_acquisitions_and_disposals` | The business acquisitions and disposals of the company. | Net cash from acquiring or disposing of businesses. | 收购或处置业务产生的净现金。 |
| `resp.200.cash_flow_statements.investment_acquisitions_and_disposals` | The investment acquisitions and disposals of the company. | Net cash from buying or selling investments. | 买入或卖出投资产生的净现金。 |
| `resp.200.cash_flow_statements.net_cash_flow_from_investing` | The net cash flow from investing of the company. | Net cash generated or used by investing activities. | 投资活动产生或消耗的净现金流。 |
| `resp.200.cash_flow_statements.issuance_or_repayment_of_debt_securities` | The issuance or repayment of debt securities of the company. | Net cash from issuing or repaying debt securities. | 发行或偿还债务证券产生的净现金。 |
| `resp.200.cash_flow_statements.issuance_or_purchase_of_equity_shares` | The issuance or purchase of equity shares of the company. | Net cash from issuing or repurchasing equity shares. | 发行或回购股本产生的净现金。 |
| `resp.200.cash_flow_statements.dividends_and_other_cash_distributions` | The dividends and other cash distributions of the company. | Cash paid out as dividends and other distributions. | 以股息及其他形式分配支付的现金。 |
| `resp.200.cash_flow_statements.net_cash_flow_from_financing` | The net cash flow from financing of the company. | Net cash generated or used by financing activities. | 融资活动产生或消耗的净现金流。 |
| `resp.200.cash_flow_statements.change_in_cash_and_equivalents` | The change in cash and equivalents of the company. | Net change in cash and equivalents over the period. | 报告期内现金及等价物的净变动额。 |
| `resp.200.cash_flow_statements.effect_of_exchange_rate_changes` | The effect of exchange rate changes of the company. | Impact of foreign-exchange rate movements on cash balances. | 汇率变动对现金余额的影响。 |
| `resp.200.cash_flow_statements.ending_cash_balance` | The ending cash balance of the company. | Cash and equivalents balance at the end of the period. | 报告期末的现金及等价物余额。 |
| `resp.200.cash_flow_statements.free_cash_flow` | The free cash flow of the company. | Operating cash flow remaining after capital expenditure. | 经营现金流扣除资本性支出后的自由现金流。 |

## getEarningsPressReleases

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get earnings press releases for a ticker. | Retrieve earnings-related press releases for the given ticker. | 获取指定股票代码的财报相关新闻稿。 |
| `param:ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.press_releases` |  | List of earnings press releases for the ticker. | 该股票代码的财报新闻稿列表。 |
| `resp.200.press_releases.ticker` | The ticker symbol of the company. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.press_releases.title` | The title of the press release. | Headline of the press release. | 新闻稿的标题。 |
| `resp.200.press_releases.url` | The URL of the press release. | URL to the full press release. | 新闻稿全文的链接。 |
| `resp.200.press_releases.date` | The date the press release was published. | Publication date of the press release. | 新闻稿的发布日期。 |
| `resp.200.press_releases.text` | The full text of the press release. | Full body text of the press release. | 新闻稿的完整正文。 |

## getPriceSnapshot

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get the real-time price snapshot for a stock, including the current price, day change, and day change percent. | Retrieve a real-time price snapshot for a stock, including current price, day change, and day change percent. | 获取股票的实时价格快照，含当前价格、当日涨跌额与当日涨跌幅。 |
| `param:ticker` | The stock ticker symbol (e.g. AAPL, MSFT). | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.snapshot` |  | Real-time price snapshot for the stock. | 该股票的实时价格快照。 |
| `resp.200.snapshot.price` | The current price of the stock. | Current trading price of the stock. | 该股票的当前成交价格。 |
| `resp.200.snapshot.ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.snapshot.day_change` | The price change since the previous trading day's close. | Price change since the previous trading day's close. | 相对上一交易日收盘价的价格变动额。 |
| `resp.200.snapshot.day_change_percent` | The percentage price change since the previous trading day's close. | Percentage price change since the previous trading day's close. | 相对上一交易日收盘价的价格变动百分比。 |
| `resp.200.snapshot.market_cap` | The market capitalization of the company. | Current market capitalization of the company. | 公司当前的总市值。 |
| `resp.200.snapshot.time` | The timestamp of the price snapshot in human-readable format in UTC. | Timestamp of the snapshot as a human-readable UTC value. | 快照时点的可读时间戳（UTC）。 |
| `resp.200.snapshot.time_milliseconds` | The timestamp of the price snapshot in milliseconds since epoch. | Timestamp of the snapshot in milliseconds since the Unix epoch. | 快照时点的时间戳，以 Unix 纪元起算的毫秒数表示。 |

## getAllFinancialStatements

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get all financial statements for a ticker. | Retrieve income statements, balance sheets, and cash flow statements for the given ticker in a single response. | 一次性获取指定股票代码的利润表、资产负债表与现金流量表。 |
| `param:ticker` | The ticker symbol. Required if cik is not provided. | Stock ticker symbol of the company; required when `cik` is not provided. | 目标公司的股票代码；未提供 `cik` 时必填。 |
| `param:period` | The time period of the financial statements. | Reporting cadence of the financial data to return. | 返回财务数据所采用的报告周期。 |
| `param:limit` | The maximum number of financial statements to return. | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `param:cik` | The Central Index Key (CIK) of the company. | SEC Central Index Key identifying the company; an alternative lookup key to the ticker. | 公司在 SEC 的中央索引号（CIK），可作为股票代码之外的查询键。 |
| `resp.200.financials` |  | Container bundling the income statements, balance sheets, and cash flow statements. | 汇总利润表、资产负债表与现金流量表的容器。 |
| `resp.200.financials.income_statements` |  | List of income statement records for the ticker. | 该股票代码的利润表记录列表。 |
| `resp.200.financials.income_statements.ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.financials.income_statements.report_period` | The reporting period of the income statement. | Date the underlying report covers, marking which fiscal point the figures belong to. | 本条数据所属报告的覆盖日期，标明各数值对应的财报时点。 |
| `resp.200.financials.income_statements.fiscal_period` | The fiscal period of the income statement. | Issuer's fiscal-period label for the reporting interval. | 本报告区间对应的公司财年周期标签。 |
| `resp.200.financials.income_statements.period` | The time period of the income statement. | Reporting cadence to which this record's figures correspond. | 本条记录数值所对应的报告周期。 |
| `resp.200.financials.income_statements.currency` | The currency in which the financial data is reported. | Currency in which the monetary figures in this record are reported. | 本条记录中各金额数值所采用的计价货币。 |
| `resp.200.financials.income_statements.revenue` | The total revenue of the company. | Total sales the company generated over the reporting period. | 公司在报告期内实现的销售总额。 |
| `resp.200.financials.income_statements.cost_of_revenue` | The cost of revenue of the company. | Direct costs attributable to producing the goods or services sold. | 与所售商品或服务直接相关的生产成本。 |
| `resp.200.financials.income_statements.gross_profit` | The gross profit of the company. | Revenue remaining after subtracting the cost of revenue. | 营业收入扣除营业成本后的毛利润。 |
| `resp.200.financials.income_statements.operating_expense` | The operating expenses of the company. | Operating costs incurred outside the direct cost of revenue. | 营业成本之外发生的运营费用。 |
| `resp.200.financials.income_statements.selling_general_and_administrative_expenses` | The selling, general, and administrative expenses of the company. | Selling, general, and administrative overhead for the period. | 报告期内的销售、一般及管理费用。 |
| `resp.200.financials.income_statements.research_and_development` | The research and development expenses of the company. | Spending on research and development activities. | 研发活动支出。 |
| `resp.200.financials.income_statements.operating_income` | The operating income of the company. | Profit from core operations before interest and taxes. | 核心经营在扣除利息与税项前产生的营业利润。 |
| `resp.200.financials.income_statements.interest_expense` | The interest expenses of the company. | Cost of interest on the company's borrowings. | 公司债务产生的利息支出。 |
| `resp.200.financials.income_statements.ebit` | The earnings before interest and taxes of the company. | Earnings before interest and taxes. | 息税前利润（EBIT）。 |
| `resp.200.financials.income_statements.income_tax_expense` | The income tax expenses of the company. | Income tax charged against the period's profit. | 计入本期利润的所得税费用。 |
| `resp.200.financials.income_statements.net_income_discontinued_operations` | The net income from discontinued operations of the company. | Net income contributed by operations that have been discontinued. | 已终止经营业务贡献的净利润。 |
| `resp.200.financials.income_statements.net_income_non_controlling_interests` | The net income from non-controlling interests of the company. | Portion of net income attributable to non-controlling (minority) interests. | 归属于非控股（少数股东）权益的净利润部分。 |
| `resp.200.financials.income_statements.net_income` | The net income of the company. | Bottom-line profit after all expenses, interest, and taxes. | 扣除全部费用、利息与税项后的净利润。 |
| `resp.200.financials.income_statements.net_income_common_stock` | The net income available to common stockholders of the company. | Net income attributable to common shareholders after preferred claims. | 扣除优先股索偿后归属于普通股股东的净利润。 |
| `resp.200.financials.income_statements.preferred_dividends_impact` | The impact of preferred dividends on the net income of the company. | Effect of preferred dividends on income available to common shareholders. | 优先股股息对可分配给普通股股东利润的影响。 |
| `resp.200.financials.income_statements.consolidated_income` | The consolidated income of the company. | Total consolidated income including all controlled entities. | 涵盖全部受控主体的合并总收益。 |
| `resp.200.financials.income_statements.earnings_per_share` | The earnings per share of the company. | Net income allocated to each outstanding common share. | 分摊到每股流通普通股的净利润（基本每股收益）。 |
| `resp.200.financials.income_statements.earnings_per_share_diluted` | The diluted earnings per share of the company. | Earnings per share assuming all dilutive securities are converted. | 假设全部稀释性证券转换后的每股收益（稀释每股收益）。 |
| `resp.200.financials.income_statements.dividends_per_common_share` | The dividends per common share of the company. | Dividends declared per common share for the period. | 报告期内每股普通股宣派的股息。 |
| `resp.200.financials.income_statements.weighted_average_shares` | The weighted average shares of the company. | Time-weighted average of common shares outstanding during the period. | 报告期内流通普通股的加权平均股数。 |
| `resp.200.financials.income_statements.weighted_average_shares_diluted` | The diluted weighted average shares of the company. | Diluted weighted-average share count including dilutive securities. | 计入稀释性证券后的加权平均稀释股数。 |
| `resp.200.financials.balance_sheets` |  | List of balance sheet records for the ticker. | 该股票代码的资产负债表记录列表。 |
| `resp.200.financials.balance_sheets.ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.financials.balance_sheets.report_period` | The reporting period of the balance sheet. | Date the underlying report covers, marking which fiscal point the figures belong to. | 本条数据所属报告的覆盖日期，标明各数值对应的财报时点。 |
| `resp.200.financials.balance_sheets.fiscal_period` | The fiscal period of the balance sheet. | Issuer's fiscal-period label for the reporting interval. | 本报告区间对应的公司财年周期标签。 |
| `resp.200.financials.balance_sheets.period` | The time period of the balance sheet. | Reporting cadence to which this record's figures correspond. | 本条记录数值所对应的报告周期。 |
| `resp.200.financials.balance_sheets.currency` | The currency in which the financial data is reported. | Currency in which the monetary figures in this record are reported. | 本条记录中各金额数值所采用的计价货币。 |
| `resp.200.financials.balance_sheets.total_assets` | The total assets of the company. | Sum of all assets the company holds. | 公司持有的全部资产合计。 |
| `resp.200.financials.balance_sheets.current_assets` | The current assets of the company. | Assets expected to be converted to cash or used within one year. | 预计在一年内变现或耗用的流动资产。 |
| `resp.200.financials.balance_sheets.cash_and_equivalents` | The cash and equivalents of the company. | Cash on hand plus highly liquid short-term holdings. | 库存现金及高流动性的短期等价物。 |
| `resp.200.financials.balance_sheets.inventory` | The inventory of the company. | Value of goods held for sale or production. | 为销售或生产而持有的存货价值。 |
| `resp.200.financials.balance_sheets.current_investments` | The current investments of the company. | Short-term investments classified as current assets. | 归类为流动资产的短期投资。 |
| `resp.200.financials.balance_sheets.trade_and_non_trade_receivables` | The trade and non-trade receivables of the company. | Amounts owed to the company from trade and non-trade sources. | 公司应收的贸易与非贸易款项。 |
| `resp.200.financials.balance_sheets.non_current_assets` | The non-current assets of the company. | Assets not expected to be realized within one year. | 预计一年内无法变现的非流动资产。 |
| `resp.200.financials.balance_sheets.property_plant_and_equipment` | The property, plant, and equipment of the company. | Carrying value of property, plant, and equipment. | 房产、厂房及设备的账面价值。 |
| `resp.200.financials.balance_sheets.goodwill_and_intangible_assets` | The goodwill and intangible assets of the company. | Goodwill together with other intangible assets. | 商誉及其他无形资产合计。 |
| `resp.200.financials.balance_sheets.investments` | The investments of the company. | Total investment holdings of the company. | 公司投资持仓合计。 |
| `resp.200.financials.balance_sheets.non_current_investments` | The non-current investments of the company. | Investments held beyond one year. | 持有期超过一年的非流动投资。 |
| `resp.200.financials.balance_sheets.outstanding_shares` | The outstanding shares of the company. | Number of common shares currently issued and outstanding. | 当前已发行并流通在外的普通股股数。 |
| `resp.200.financials.balance_sheets.tax_assets` | The tax assets of the company. | Recognized tax-related assets such as deferred tax assets. | 已确认的税务相关资产，如递延所得税资产。 |
| `resp.200.financials.balance_sheets.total_liabilities` | The total liabilities of the company. | Sum of all the company's liabilities. | 公司全部负债合计。 |
| `resp.200.financials.balance_sheets.current_liabilities` | The current liabilities of the company. | Obligations due within one year. | 一年内到期的流动负债。 |
| `resp.200.financials.balance_sheets.current_debt` | The current debt of the company. | Portion of debt due within one year. | 一年内到期的债务部分。 |
| `resp.200.financials.balance_sheets.trade_and_non_trade_payables` | The trade and non-trade payables of the company. | Amounts the company owes from trade and non-trade sources. | 公司应付的贸易与非贸易款项。 |
| `resp.200.financials.balance_sheets.deferred_revenue` | The deferred revenue of the company. | Payments received for goods or services not yet delivered. | 已收取但尚未交付商品或服务对应的递延收入。 |
| `resp.200.financials.balance_sheets.deposit_liabilities` | The deposit liabilities of the company. | Liabilities arising from customer or counterparty deposits. | 客户或交易对手存入款项形成的存款负债。 |
| `resp.200.financials.balance_sheets.non_current_liabilities` | The non-current liabilities of the company. | Obligations due beyond one year. | 一年以上到期的非流动负债。 |
| `resp.200.financials.balance_sheets.non_current_debt` | The non-current debt of the company. | Portion of debt due beyond one year. | 一年以上到期的债务部分。 |
| `resp.200.financials.balance_sheets.tax_liabilities` | The tax liabilities of the company. | Recognized tax-related obligations such as deferred tax liabilities. | 已确认的税务相关负债，如递延所得税负债。 |
| `resp.200.financials.balance_sheets.shareholders_equity` | The shareholders' equity of the company. | Residual interest in assets after deducting liabilities. | 资产扣除负债后归属于股东的剩余权益。 |
| `resp.200.financials.balance_sheets.retained_earnings` | The retained earnings of the company. | Cumulative earnings retained rather than distributed as dividends. | 历年留存而未作为股息分配的累计利润。 |
| `resp.200.financials.balance_sheets.accumulated_other_comprehensive_income` | The accumulated other comprehensive income of the company. | Cumulative gains and losses recorded outside the income statement. | 计入损益表之外的累计其他综合收益。 |
| `resp.200.financials.balance_sheets.total_debt` | The total debt of the company. | Combined current and non-current interest-bearing debt. | 流动与非流动有息债务合计。 |
| `resp.200.financials.cash_flow_statements` |  | List of cash flow statement records for the ticker. | 该股票代码的现金流量表记录列表。 |
| `resp.200.financials.cash_flow_statements.ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.financials.cash_flow_statements.report_period` | The reporting period of the cash flow statement. | Date the underlying report covers, marking which fiscal point the figures belong to. | 本条数据所属报告的覆盖日期，标明各数值对应的财报时点。 |
| `resp.200.financials.cash_flow_statements.fiscal_period` | The fiscal period of the cash flow statement. | Issuer's fiscal-period label for the reporting interval. | 本报告区间对应的公司财年周期标签。 |
| `resp.200.financials.cash_flow_statements.period` | The time period of the cash flow statement. | Reporting cadence to which this record's figures correspond. | 本条记录数值所对应的报告周期。 |
| `resp.200.financials.cash_flow_statements.currency` | The currency in which the financial data is reported. | Currency in which the monetary figures in this record are reported. | 本条记录中各金额数值所采用的计价货币。 |
| `resp.200.financials.cash_flow_statements.net_income` | The net income of the company. | Net income carried from the income statement as the starting point of the cash flow. | 由损益表结转、作为现金流量起点的净利润。 |
| `resp.200.financials.cash_flow_statements.depreciation_and_amortization` | The depreciation and amortization of the company. | Non-cash depreciation and amortization added back to earnings. | 加回利润的非现金折旧与摊销。 |
| `resp.200.financials.cash_flow_statements.share_based_compensation` | The share-based compensation of the company. | Non-cash expense from share-based employee compensation. | 以股份为基础的员工薪酬产生的非现金费用。 |
| `resp.200.financials.cash_flow_statements.net_cash_flow_from_operations` | The net cash flow from operations of the company. | Net cash generated by core operating activities. | 核心经营活动产生的净现金流。 |
| `resp.200.financials.cash_flow_statements.capital_expenditure` | The capital expenditure of the company. | Cash spent acquiring or upgrading long-term assets. | 用于购置或升级长期资产的资本性支出。 |
| `resp.200.financials.cash_flow_statements.business_acquisitions_and_disposals` | The business acquisitions and disposals of the company. | Net cash from acquiring or disposing of businesses. | 收购或处置业务产生的净现金。 |
| `resp.200.financials.cash_flow_statements.investment_acquisitions_and_disposals` | The investment acquisitions and disposals of the company. | Net cash from buying or selling investments. | 买入或卖出投资产生的净现金。 |
| `resp.200.financials.cash_flow_statements.net_cash_flow_from_investing` | The net cash flow from investing of the company. | Net cash generated or used by investing activities. | 投资活动产生或消耗的净现金流。 |
| `resp.200.financials.cash_flow_statements.issuance_or_repayment_of_debt_securities` | The issuance or repayment of debt securities of the company. | Net cash from issuing or repaying debt securities. | 发行或偿还债务证券产生的净现金。 |
| `resp.200.financials.cash_flow_statements.issuance_or_purchase_of_equity_shares` | The issuance or purchase of equity shares of the company. | Net cash from issuing or repurchasing equity shares. | 发行或回购股本产生的净现金。 |
| `resp.200.financials.cash_flow_statements.dividends_and_other_cash_distributions` | The dividends and other cash distributions of the company. | Cash paid out as dividends and other distributions. | 以股息及其他形式分配支付的现金。 |
| `resp.200.financials.cash_flow_statements.net_cash_flow_from_financing` | The net cash flow from financing of the company. | Net cash generated or used by financing activities. | 融资活动产生或消耗的净现金流。 |
| `resp.200.financials.cash_flow_statements.change_in_cash_and_equivalents` | The change in cash and equivalents of the company. | Net change in cash and equivalents over the period. | 报告期内现金及等价物的净变动额。 |
| `resp.200.financials.cash_flow_statements.effect_of_exchange_rate_changes` | The effect of exchange rate changes of the company. | Impact of foreign-exchange rate movements on cash balances. | 汇率变动对现金余额的影响。 |
| `resp.200.financials.cash_flow_statements.ending_cash_balance` | The ending cash balance of the company. | Cash and equivalents balance at the end of the period. | 报告期末的现金及等价物余额。 |
| `resp.200.financials.cash_flow_statements.free_cash_flow` | The free cash flow of the company. | Operating cash flow remaining after capital expenditure. | 经营现金流扣除资本性支出后的自由现金流。 |

## getNews

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get recent news articles for a specific company or the broad market. Pass a ticker for company-specific news, or omit the ticker for general market news. Articles are sourced from RSS feeds of publishers like The Motley Fool, Investing.com, Reuters, and more. | Retrieve recent news articles for a specific company, or broad-market news when the ticker is omitted. | 获取指定公司的近期新闻；省略股票代码时返回大盘新闻。 |
| `param:ticker` | The ticker symbol of the company. Omit for broad market news. | Ticker symbol for company-specific news; omit to receive broad-market news. | 用于获取特定公司新闻的股票代码；省略则返回大盘新闻。 |
| `param:limit` | The maximum number of news articles to return (default: 5, max: 10). | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `resp.200.news` |  | List of news articles matching the query. | 符合查询条件的新闻文章列表。 |
| `resp.200.news.ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.news.title` | The title of the news article. | Headline of the news article. | 新闻文章的标题。 |
| `resp.200.news.author` | The author of the news article. | Author of the news article. | 新闻文章的作者。 |
| `resp.200.news.source` | The source of the news article. | Publisher or source of the news article. | 新闻文章的发布方或来源。 |
| `resp.200.news.date` | The date the news article was published. | Publication date of the news article. | 新闻文章的发布日期。 |
| `resp.200.news.url` | The URL of the news article. | URL to the full news article. | 新闻文章全文的链接。 |
| `resp.200.news.sentiment` | The sentiment of the news article. | Sentiment classification assigned to the news article. | 为该新闻文章判定的情感倾向分类。 |

## getPrices

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get end-of-day (EOD) historical price data for stocks. | Retrieve end-of-day historical price data for a stock over a date range. | 按日期区间获取股票的日终历史价格数据。 |
| `param:ticker` | The stock ticker symbol (e.g. AAPL, MSFT). | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `param:interval` | The time interval for the price data. | Aggregation interval of each returned price bar. | 每条返回价格数据的聚合时间粒度。 |
| `param:start_date` | The start date for the price data (format: YYYY-MM-DD). | Earliest date to include in the returned price series. | 返回价格序列纳入的最早日期。 |
| `param:end_date` | The end date for the price data (format: YYYY-MM-DD). | Latest date to include in the returned price series. | 返回价格序列纳入的最晚日期。 |
| `resp.200.prices` |  | List of historical price bars for the ticker. | 该股票代码的历史价格数据列表。 |
| `resp.200.prices.open` | The open price of the ticker in the given time period. | Opening price of the ticker for the interval. | 该时间区间内的开盘价。 |
| `resp.200.prices.close` | The close price of the ticker in the given time period. | Closing price of the ticker for the interval. | 该时间区间内的收盘价。 |
| `resp.200.prices.high` | The high price of the ticker in the given time period. | Highest price of the ticker during the interval. | 该时间区间内的最高价。 |
| `resp.200.prices.low` | The low price of the ticker in the given time period. | Lowest price of the ticker during the interval. | 该时间区间内的最低价。 |
| `resp.200.prices.volume` | The volume of the ticker in the given time period. | Trading volume of the ticker during the interval. | 该时间区间内的成交量。 |
| `resp.200.prices.time` | The human-readable time format of the price in UTC. | Interval timestamp as a human-readable UTC value. | 该数据时点的可读时间戳（UTC）。 |
| `resp.200.prices.time_milliseconds` | The timestamp of the price in milliseconds since epoch. | Interval timestamp in milliseconds since the Unix epoch. | 该数据时点的时间戳，以 Unix 纪元起算的毫秒数表示。 |
| `resp.200.next_page_url` | The URL to the next page of results. | URL to fetch the next page of price results, when more data is available. | 当存在更多数据时，用于获取下一页价格结果的链接。 |

## getFinancialMetrics

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get financial metrics for a ticker, including valuation, profitability, efficiency, liquidity, leverage, growth, and per share metrics. | Retrieve financial metrics for a ticker across valuation, profitability, efficiency, liquidity, leverage, growth, and per-share categories. | 获取指定股票代码的财务指标，涵盖估值、盈利能力、运营效率、流动性、杠杆、成长性与每股指标。 |
| `param:ticker` | The ticker symbol of the company. Required if cik is not provided. | Stock ticker symbol of the company; required when `cik` is not provided. | 目标公司的股票代码；未提供 `cik` 时必填。 |
| `param:cik` | The Central Index Key (CIK) of the company. Can be used instead of ticker. | SEC Central Index Key of the company; an alternative to the ticker. | 公司的 SEC 中央索引号（CIK），可替代股票代码使用。 |
| `param:period` | The time period for the financial data. | Reporting cadence of the financial data to return. | 返回财务数据所采用的报告周期。 |
| `param:limit` | The maximum number of results to return. | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `resp.200.ticker` | The ticker symbol of the company. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.market_cap` | The market capitalization of the company. | Total market value of the company's outstanding shares. | 公司全部流通股的总市值。 |
| `resp.200.enterprise_value` | The total value of the company (market cap + debt - cash). | Total company value combining equity market cap with debt, net of cash. | 以股权市值叠加债务、扣除现金后的公司整体价值。 |
| `resp.200.price_to_earnings_ratio` | Price to earnings ratio. | Share price relative to earnings per share. | 股价相对于每股收益的倍数（市盈率）。 |
| `resp.200.price_to_book_ratio` | Price to book ratio. | Share price relative to book value per share. | 股价相对于每股账面价值的倍数（市净率）。 |
| `resp.200.price_to_sales_ratio` | Price to sales ratio. | Share price relative to revenue per share. | 股价相对于每股营收的倍数（市销率）。 |
| `resp.200.enterprise_value_to_ebitda_ratio` | Enterprise value to EBITDA ratio. | Enterprise value relative to EBITDA. | 企业价值相对于 EBITDA 的倍数。 |
| `resp.200.enterprise_value_to_revenue_ratio` | Enterprise value to revenue ratio. | Enterprise value relative to revenue. | 企业价值相对于营业收入的倍数。 |
| `resp.200.free_cash_flow_yield` | Free cash flow yield. | Free cash flow relative to market capitalization.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 自由现金流相对于市值的收益率。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.peg_ratio` | Price to earnings growth ratio. | Price-to-earnings ratio relative to earnings growth. | 市盈率相对于盈利增长的比率（PEG）。 |
| `resp.200.gross_margin` | Gross profit as a percentage of revenue. | Gross profit expressed relative to revenue.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 毛利润相对于营业收入的占比（毛利率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.operating_margin` | Operating income as a percentage of revenue. | Operating income expressed relative to revenue.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 营业利润相对于营业收入的占比（营业利润率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.net_margin` | Net income as a percentage of revenue. | Net income expressed relative to revenue.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 净利润相对于营业收入的占比（净利率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.return_on_equity` | Net income as a percentage of shareholders' equity. | Net income expressed relative to shareholders' equity.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 净利润相对于股东权益的回报水平（净资产收益率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.return_on_assets` | Net income as a percentage of total assets. | Net income expressed relative to total assets.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 净利润相对于总资产的回报水平（总资产收益率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.return_on_invested_capital` | Net operating profit after taxes as a percentage of invested capital. | After-tax operating profit relative to invested capital.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 税后营业利润相对于投入资本的回报水平。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.asset_turnover` | Revenue divided by average total assets. | Revenue generated per unit of average total assets. | 每单位平均总资产所产生的营业收入（总资产周转率）。 |
| `resp.200.inventory_turnover` | Cost of goods sold divided by average inventory. | Cost of goods sold relative to average inventory. | 销货成本相对于平均存货的周转倍数（存货周转率）。 |
| `resp.200.receivables_turnover` | Revenue divided by average accounts receivable. | Revenue relative to average accounts receivable. | 营业收入相对于平均应收账款的周转倍数（应收账款周转率）。 |
| `resp.200.days_sales_outstanding` | Average accounts receivable divided by revenue over the period. | Average number of days to collect receivables. | 收回应收账款平均所需的天数。 |
| `resp.200.operating_cycle` | Inventory turnover + receivables turnover. | Combined cycle of converting inventory and receivables into cash. | 存货与应收账款转化为现金的合计周期。 |
| `resp.200.working_capital_turnover` | Revenue divided by average working capital. | Revenue generated per unit of average working capital. | 每单位平均营运资本所产生的营业收入。 |
| `resp.200.current_ratio` | Current assets divided by current liabilities. | Current assets relative to current liabilities. | 流动资产相对于流动负债的比率（流动比率）。 |
| `resp.200.quick_ratio` | Quick assets divided by current liabilities. | Liquid current assets relative to current liabilities. | 速动资产相对于流动负债的比率（速动比率）。 |
| `resp.200.cash_ratio` | Cash and cash equivalents divided by current liabilities. | Cash and equivalents relative to current liabilities. | 现金及等价物相对于流动负债的比率（现金比率）。 |
| `resp.200.operating_cash_flow_ratio` | Operating cash flow divided by current liabilities. | Operating cash flow relative to current liabilities. | 经营现金流相对于流动负债的比率。 |
| `resp.200.debt_to_equity` | Total debt divided by shareholders' equity. | Total debt relative to shareholders' equity. | 总债务相对于股东权益的比率（产权比率）。 |
| `resp.200.debt_to_assets` | Total debt divided by total assets. | Total debt relative to total assets. | 总债务相对于总资产的比率（资产负债率）。 |
| `resp.200.interest_coverage` | EBIT divided by interest expense. | EBIT relative to interest expense. | 息税前利润相对于利息支出的覆盖倍数（利息保障倍数）。 |
| `resp.200.revenue_growth` | Year-over-year growth in revenue. | Year-over-year change in revenue.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 营业收入的同比变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.earnings_growth` | Year-over-year growth in earnings. | Year-over-year change in earnings.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 盈利的同比变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.book_value_growth` | Year-over-year growth in book value. | Year-over-year change in book value.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 账面价值的同比变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.earnings_per_share_growth` | Growth in earnings per share over the period. | Change in earnings per share over the period.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 每股收益在报告期内的变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.free_cash_flow_growth` | Growth in free cash flow over the period. | Change in free cash flow over the period.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 自由现金流在报告期内的变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.operating_income_growth` | Growth in operating income over the period. | Change in operating income over the period.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 营业利润在报告期内的变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.ebitda_growth` | Growth in EBITDA over the period. | Change in EBITDA over the period.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | EBITDA 在报告期内的变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.payout_ratio` | Dividends paid as a percentage of net income. | Dividends paid relative to net income.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 已派股息相对于净利润的占比（派息率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.earnings_per_share` | Net income divided by weighted average shares outstanding. | Net income allocated to each outstanding common share. | 分摊到每股流通普通股的净利润。 |
| `resp.200.book_value_per_share` | Shareholders' equity divided by shares outstanding. | Shareholders' equity allocated to each outstanding share. | 分摊到每股流通股的股东权益（每股账面价值）。 |
| `resp.200.free_cash_flow_per_share` | Free cash flow divided by shares outstanding. | Free cash flow allocated to each outstanding share. | 分摊到每股流通股的自由现金流。 |

## getFinancialMetricsSnapshot

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get the real-time financial metrics snapshot for a stock, including valuation ratios, profitability, efficiency, liquidity, leverage, growth, and per share metrics. | Retrieve a real-time snapshot of a stock's financial metrics across valuation, profitability, efficiency, liquidity, leverage, growth, and per-share categories. | 获取股票财务指标的实时快照，涵盖估值、盈利能力、运营效率、流动性、杠杆、成长性与每股指标。 |
| `param:ticker` | The ticker symbol of the company. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `param:cik` | The Central Index Key (CIK) of the company. Can be used instead of ticker. | SEC Central Index Key of the company; an alternative to the ticker. | 公司的 SEC 中央索引号（CIK），可替代股票代码使用。 |
| `resp.200.snapshot` |  | Real-time snapshot of the stock's financial metrics. | 该股票财务指标的实时快照。 |
| `resp.200.snapshot.ticker` | The ticker symbol of the company. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.snapshot.market_cap` | The total market capitalization (stock price × shares outstanding). | Total market capitalization, computed from current share price and shares outstanding. | 按当前股价与流通股数计算的总市值。 |
| `resp.200.snapshot.enterprise_value` | The total value of the company (market cap + debt - cash). | Total company value combining equity market cap with debt, net of cash. | 以股权市值叠加债务、扣除现金后的公司整体价值。 |
| `resp.200.snapshot.price_to_earnings_ratio` | Price to earnings ratio. | Share price relative to earnings per share. | 股价相对于每股收益的倍数（市盈率）。 |
| `resp.200.snapshot.price_to_book_ratio` | Price to book ratio. | Share price relative to book value per share. | 股价相对于每股账面价值的倍数（市净率）。 |
| `resp.200.snapshot.price_to_sales_ratio` | Price to sales ratio. | Share price relative to revenue per share. | 股价相对于每股营收的倍数（市销率）。 |
| `resp.200.snapshot.enterprise_value_to_ebitda_ratio` | Enterprise value to EBITDA ratio. | Enterprise value relative to EBITDA. | 企业价值相对于 EBITDA 的倍数。 |
| `resp.200.snapshot.enterprise_value_to_revenue_ratio` | Enterprise value to revenue ratio. | Enterprise value relative to revenue. | 企业价值相对于营业收入的倍数。 |
| `resp.200.snapshot.free_cash_flow_yield` | Free cash flow yield. | Free cash flow relative to market capitalization.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 自由现金流相对于市值的收益率。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.peg_ratio` | Price to earnings growth ratio. | Price-to-earnings ratio relative to earnings growth. | 市盈率相对于盈利增长的比率（PEG）。 |
| `resp.200.snapshot.gross_margin` | Gross profit as a percentage of revenue. | Gross profit expressed relative to revenue.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 毛利润相对于营业收入的占比（毛利率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.operating_margin` | Operating income as a percentage of revenue. | Operating income expressed relative to revenue.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 营业利润相对于营业收入的占比（营业利润率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.net_margin` | Net income as a percentage of revenue. | Net income expressed relative to revenue.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 净利润相对于营业收入的占比（净利率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.return_on_equity` | Net income as a percentage of shareholders' equity. | Net income expressed relative to shareholders' equity.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 净利润相对于股东权益的回报水平（净资产收益率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.return_on_assets` | Net income as a percentage of total assets. | Net income expressed relative to total assets.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 净利润相对于总资产的回报水平（总资产收益率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.return_on_invested_capital` | Net operating profit after taxes as a percentage of invested capital. | After-tax operating profit relative to invested capital.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 税后营业利润相对于投入资本的回报水平。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.asset_turnover` | Revenue divided by average total assets. | Revenue generated per unit of average total assets. | 每单位平均总资产所产生的营业收入（总资产周转率）。 |
| `resp.200.snapshot.inventory_turnover` | Cost of goods sold divided by average inventory. | Cost of goods sold relative to average inventory. | 销货成本相对于平均存货的周转倍数（存货周转率）。 |
| `resp.200.snapshot.receivables_turnover` | Revenue divided by average accounts receivable. | Revenue relative to average accounts receivable. | 营业收入相对于平均应收账款的周转倍数（应收账款周转率）。 |
| `resp.200.snapshot.days_sales_outstanding` | Average accounts receivable divided by revenue over the period. | Average number of days to collect receivables. | 收回应收账款平均所需的天数。 |
| `resp.200.snapshot.operating_cycle` | Inventory turnover + receivables turnover. | Combined cycle of converting inventory and receivables into cash. | 存货与应收账款转化为现金的合计周期。 |
| `resp.200.snapshot.working_capital_turnover` | Revenue divided by average working capital. | Revenue generated per unit of average working capital. | 每单位平均营运资本所产生的营业收入。 |
| `resp.200.snapshot.current_ratio` | Current assets divided by current liabilities. | Current assets relative to current liabilities. | 流动资产相对于流动负债的比率（流动比率）。 |
| `resp.200.snapshot.quick_ratio` | Quick assets divided by current liabilities. | Liquid current assets relative to current liabilities. | 速动资产相对于流动负债的比率（速动比率）。 |
| `resp.200.snapshot.cash_ratio` | Cash and cash equivalents divided by current liabilities. | Cash and equivalents relative to current liabilities. | 现金及等价物相对于流动负债的比率（现金比率）。 |
| `resp.200.snapshot.operating_cash_flow_ratio` | Operating cash flow divided by current liabilities. | Operating cash flow relative to current liabilities. | 经营现金流相对于流动负债的比率。 |
| `resp.200.snapshot.debt_to_equity` | Total debt divided by shareholders' equity. | Total debt relative to shareholders' equity. | 总债务相对于股东权益的比率（产权比率）。 |
| `resp.200.snapshot.debt_to_assets` | Total debt divided by total assets. | Total debt relative to total assets. | 总债务相对于总资产的比率（资产负债率）。 |
| `resp.200.snapshot.interest_coverage` | EBIT divided by interest expense. | EBIT relative to interest expense. | 息税前利润相对于利息支出的覆盖倍数（利息保障倍数）。 |
| `resp.200.snapshot.revenue_growth` | Year-over-year growth in revenue. | Year-over-year change in revenue.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 营业收入的同比变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.earnings_growth` | Year-over-year growth in earnings. | Year-over-year change in earnings.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 盈利的同比变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.book_value_growth` | Year-over-year growth in book value. | Year-over-year change in book value.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 账面价值的同比变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.earnings_per_share_growth` | Growth in earnings per share over the period. | Change in earnings per share over the period.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 每股收益在报告期内的变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.free_cash_flow_growth` | Growth in free cash flow over the period. | Change in free cash flow over the period.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 自由现金流在报告期内的变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.operating_income_growth` | Growth in operating income over the period. | Change in operating income over the period.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 营业利润在报告期内的变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.ebitda_growth` | Growth in EBITDA over the period. | Change in EBITDA over the period.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | EBITDA 在报告期内的变动幅度。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.payout_ratio` | Dividends paid as a percentage of net income. | Dividends paid relative to net income.<br>[⚠️Note:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] | 已派股息相对于净利润的占比（派息率）。<br>[⚠️批注:源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| `resp.200.snapshot.earnings_per_share` | Net income divided by weighted average shares outstanding. | Net income allocated to each outstanding common share. | 分摊到每股流通普通股的净利润。 |
| `resp.200.snapshot.book_value_per_share` | Shareholders' equity divided by shares outstanding. | Shareholders' equity allocated to each outstanding share. | 分摊到每股流通股的股东权益（每股账面价值）。 |
| `resp.200.snapshot.free_cash_flow_per_share` | Free cash flow divided by shares outstanding. | Free cash flow allocated to each outstanding share. | 分摊到每股流通股的自由现金流。 |

## stockScreener

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Search for stocks by filtering across financial metrics from income statements, balance sheets, and cash flow statements. | Screen for stocks by applying filters across financial metrics drawn from income statements, balance sheets, and cash flow statements. | 通过对取自利润表、资产负债表与现金流量表的财务指标设定筛选条件来检索股票。 |
| `req.period` | The time period for the financial data. | Reporting cadence of the financial data to return. | 返回财务数据所采用的报告周期。 |
| `req.limit` | The maximum number of results to return. | Upper bound on the number of records returned in one response. | 单次响应返回记录数的上限。 |
| `req.order_by` | The field to order the results by.  Use -field to order in descending order. | Field used to sort the results; prefix with a minus sign to sort in descending order. | 用于结果排序的字段；前缀加减号表示降序排列。 |
| `req.currency` | The currency of the financial data. | Currency in which the screened financial figures are expressed. | 筛选所依据的财务数值采用的计价货币。 |
| `req.historical` | Whether to return historical financial data. | Whether to evaluate filters against historical financial data rather than the latest only. | 是否对历史财务数据（而非仅最新数据）应用筛选条件。 |
| `req.filters` | An array of filter objects to apply to the search. | List of filter conditions combined to screen the stock universe. | 用于组合筛选股票池的过滤条件列表。 |
| `req.filters.field` | The criteria to filter on.  For financial metric fields, use 'gt', 'lt', 'gte', 'lte', 'eq' operators.  For 'ticker' and 'cik' fields, use the 'in' operator to filter against multiple values. | Financial metric or identifier the condition is evaluated on; use comparison operators for metric fields and the 'in' operator for ticker or cik. | 该条件所作用的财务指标或标识；指标字段使用比较运算符，ticker 或 cik 使用 'in' 运算符。 |
| `req.filters.operator` | The comparison operator. The 'in' operator can only be used with a field value of 'ticker' or 'cik' and lets you filter against multiple values. | Comparison operator applied between the field and the value; the 'in' operator works only with the ticker or cik field for multi-value matching. | 在字段与取值之间施加的比较运算符；'in' 运算符仅可与 ticker 或 cik 字段配合用于多值匹配。 |
| `req.filters.value` |  | Value to compare against: a single number for comparison operators, or a list of ticker/cik strings for the 'in' operator. | 用于比较的取值：比较运算符对应单个数值，'in' 运算符对应 ticker/cik 字符串列表。 |
| `resp.200.search_results` |  | List of stocks matching all supplied filters. | 满足全部筛选条件的股票列表。 |
| `resp.200.search_results.ticker` | The ticker symbol of the company. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.search_results.report_period` | The reporting period of the financial data. | Date the underlying report covers, marking which fiscal point the figures belong to. | 本条数据所属报告的覆盖日期，标明各数值对应的财报时点。 |
| `resp.200.search_results.period` | The time period of the financial data. | Reporting cadence to which this record's figures correspond. | 本条记录数值所对应的报告周期。 |
| `resp.200.search_results.currency` | The currency of the financial data. | Currency in which the returned financial figures are reported. | 所返回财务数值采用的计价货币。 |

## getEarnings

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get the most recent earnings snapshot for a ticker. Optional estimate/surprise and change fields are returned only when available. | Retrieve the most recent earnings snapshot for a ticker; optional estimate, surprise, and change fields are returned only when available. | 获取指定股票代码的最新财报快照；可选的预期、超预期及变动字段仅在可获取时返回。 |
| `param:ticker` | The ticker symbol. | Stock ticker symbol identifying the company to query. | 标识目标公司的股票代码。 |
| `resp.200.earnings` |  | Earnings snapshot for the ticker, split into quarterly and annual views. | 该股票代码的财报快照，分为季度与年度两组视图。 |
| `resp.200.earnings.ticker` | The requested ticker symbol. | Ticker symbol the snapshot was requested for. | 本次查询所针对的股票代码。 |
| `resp.200.earnings.report_period` | Most recent report period found for the ticker. | Most recent report period found for the ticker. | 该股票代码可获取的最近报告期。 |
| `resp.200.earnings.fiscal_period` | Fiscal period label (e.g. 2025-Q4 or 2025-FY). | Fiscal-period label for the snapshot. | 本快照对应的财年周期标签。 |
| `resp.200.earnings.currency` | ISO currency code (e.g. USD). | ISO currency code in which the figures are reported. | 各数值采用的 ISO 货币代码。 |
| `resp.200.earnings.quarterly` |  | Quarterly earnings view, where change fields are quarter-over-quarter. | 季度财报视图，其中变动字段为环比口径。 |
| `resp.200.earnings.quarterly.fiscal_period` | Fiscal period label (e.g. 2025-Q4 or 2025-FY). | Issuer's fiscal-period label for the reporting interval. | 本报告区间对应的公司财年周期标签。 |
| `resp.200.earnings.quarterly.currency` | ISO currency code (e.g. USD). | Currency in which the monetary figures in this record are reported. | 本条记录中各金额数值所采用的计价货币。 |
| `resp.200.earnings.quarterly.revenue` |  | Reported revenue for the period. | 报告期内实现的营业收入。 |
| `resp.200.earnings.quarterly.estimated_revenue` | Estimated revenue. Returned only when available. | Analyst-consensus estimated revenue for the period; present only when available. | 本期分析师一致预期的营业收入；仅在可获取时返回。 |
| `resp.200.earnings.quarterly.revenue_surprise` | Revenue surprise classification versus estimate. Returned only when available. | Whether reported revenue beat, missed, or met the estimate; present only when available. | 实际营业收入相对于预期为超预期、低于预期还是符合预期；仅在可获取时返回。 |
| `resp.200.earnings.quarterly.earnings_per_share` |  | Reported earnings per share for the period. | 报告期内的每股收益。 |
| `resp.200.earnings.quarterly.estimated_earnings_per_share` | Estimated earnings per share. Returned only when available. | Analyst-consensus estimated earnings per share; present only when available. | 本期分析师一致预期的每股收益；仅在可获取时返回。 |
| `resp.200.earnings.quarterly.eps_surprise` | EPS surprise classification versus estimate. Returned only when available. | Whether reported EPS beat, missed, or met the estimate; present only when available. | 实际每股收益相对于预期为超预期、低于预期还是符合预期；仅在可获取时返回。 |
| `resp.200.earnings.quarterly.net_income` |  | Reported net income for the period. | 报告期内的净利润。 |
| `resp.200.earnings.quarterly.gross_profit` |  | Reported gross profit for the period. | 报告期内的毛利润。 |
| `resp.200.earnings.quarterly.operating_income` |  | Reported operating income for the period. | 报告期内的营业利润。 |
| `resp.200.earnings.quarterly.weighted_average_shares` |  | Weighted-average common shares outstanding for the period. | 报告期内的加权平均流通普通股股数。 |
| `resp.200.earnings.quarterly.weighted_average_shares_diluted` |  | Diluted weighted-average share count for the period. | 报告期内的加权平均稀释股数。 |
| `resp.200.earnings.quarterly.cash_and_equivalents` |  | Cash and equivalents at period end. | 报告期末的现金及等价物。 |
| `resp.200.earnings.quarterly.total_debt` |  | Total interest-bearing debt at period end. | 报告期末的有息债务合计。 |
| `resp.200.earnings.quarterly.total_assets` |  | Total assets at period end. | 报告期末的资产合计。 |
| `resp.200.earnings.quarterly.total_liabilities` |  | Total liabilities at period end. | 报告期末的负债合计。 |
| `resp.200.earnings.quarterly.shareholders_equity` |  | Shareholders' equity at period end. | 报告期末的股东权益。 |
| `resp.200.earnings.quarterly.net_cash_flow_from_operations` |  | Net cash from operating activities for the period. | 报告期内经营活动产生的净现金流。 |
| `resp.200.earnings.quarterly.capital_expenditure` |  | Capital expenditure for the period. | 报告期内的资本性支出。 |
| `resp.200.earnings.quarterly.net_cash_flow_from_investing` |  | Net cash from investing activities for the period. | 报告期内投资活动产生的净现金流。 |
| `resp.200.earnings.quarterly.net_cash_flow_from_financing` |  | Net cash from financing activities for the period. | 报告期内融资活动产生的净现金流。 |
| `resp.200.earnings.quarterly.change_in_cash_and_equivalents` |  | Net change in cash and equivalents for the period. | 报告期内现金及等价物的净变动额。 |
| `resp.200.earnings.quarterly.free_cash_flow` |  | Free cash flow for the period. | 报告期内的自由现金流。 |
| `resp.200.earnings.quarterly.revenue_chg` | Percentage change in revenue. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in revenue, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 营业收入的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.quarterly.net_income_chg` | Percentage change in net income. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in net income, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 净利润的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.quarterly.operating_income_chg` | Percentage change in operating income. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in operating income, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 营业利润的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.quarterly.gross_profit_chg` | Percentage change in gross profit. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in gross profit, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 毛利润的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.quarterly.net_cash_flow_from_operations_chg` | Percentage change in net cash flow from operations. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in operating cash flow, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 经营现金流的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.quarterly.net_cash_flow_from_investing_chg` | Percentage change in net cash flow from investing. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in investing cash flow, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 投资现金流的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.quarterly.net_cash_flow_from_financing_chg` | Percentage change in net cash flow from financing. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in financing cash flow, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 融资现金流的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.quarterly.free_cash_flow_chg` | Percentage change in free cash flow. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in free cash flow, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 自由现金流的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.annual` |  | Annual earnings view, where change fields are year-over-year. | 年度财报视图，其中变动字段为同比口径。 |
| `resp.200.earnings.annual.fiscal_period` | Fiscal period label (e.g. 2025-Q4 or 2025-FY). | Issuer's fiscal-period label for the reporting interval. | 本报告区间对应的公司财年周期标签。 |
| `resp.200.earnings.annual.currency` | ISO currency code (e.g. USD). | Currency in which the monetary figures in this record are reported. | 本条记录中各金额数值所采用的计价货币。 |
| `resp.200.earnings.annual.revenue` |  | Reported revenue for the period. | 报告期内实现的营业收入。 |
| `resp.200.earnings.annual.estimated_revenue` | Estimated revenue. Returned only when available. | Analyst-consensus estimated revenue for the period; present only when available. | 本期分析师一致预期的营业收入；仅在可获取时返回。 |
| `resp.200.earnings.annual.revenue_surprise` | Revenue surprise classification versus estimate. Returned only when available. | Whether reported revenue beat, missed, or met the estimate; present only when available. | 实际营业收入相对于预期为超预期、低于预期还是符合预期；仅在可获取时返回。 |
| `resp.200.earnings.annual.earnings_per_share` |  | Reported earnings per share for the period. | 报告期内的每股收益。 |
| `resp.200.earnings.annual.estimated_earnings_per_share` | Estimated earnings per share. Returned only when available. | Analyst-consensus estimated earnings per share; present only when available. | 本期分析师一致预期的每股收益；仅在可获取时返回。 |
| `resp.200.earnings.annual.eps_surprise` | EPS surprise classification versus estimate. Returned only when available. | Whether reported EPS beat, missed, or met the estimate; present only when available. | 实际每股收益相对于预期为超预期、低于预期还是符合预期；仅在可获取时返回。 |
| `resp.200.earnings.annual.net_income` |  | Reported net income for the period. | 报告期内的净利润。 |
| `resp.200.earnings.annual.gross_profit` |  | Reported gross profit for the period. | 报告期内的毛利润。 |
| `resp.200.earnings.annual.operating_income` |  | Reported operating income for the period. | 报告期内的营业利润。 |
| `resp.200.earnings.annual.weighted_average_shares` |  | Weighted-average common shares outstanding for the period. | 报告期内的加权平均流通普通股股数。 |
| `resp.200.earnings.annual.weighted_average_shares_diluted` |  | Diluted weighted-average share count for the period. | 报告期内的加权平均稀释股数。 |
| `resp.200.earnings.annual.cash_and_equivalents` |  | Cash and equivalents at period end. | 报告期末的现金及等价物。 |
| `resp.200.earnings.annual.total_debt` |  | Total interest-bearing debt at period end. | 报告期末的有息债务合计。 |
| `resp.200.earnings.annual.total_assets` |  | Total assets at period end. | 报告期末的资产合计。 |
| `resp.200.earnings.annual.total_liabilities` |  | Total liabilities at period end. | 报告期末的负债合计。 |
| `resp.200.earnings.annual.shareholders_equity` |  | Shareholders' equity at period end. | 报告期末的股东权益。 |
| `resp.200.earnings.annual.net_cash_flow_from_operations` |  | Net cash from operating activities for the period. | 报告期内经营活动产生的净现金流。 |
| `resp.200.earnings.annual.capital_expenditure` |  | Capital expenditure for the period. | 报告期内的资本性支出。 |
| `resp.200.earnings.annual.net_cash_flow_from_investing` |  | Net cash from investing activities for the period. | 报告期内投资活动产生的净现金流。 |
| `resp.200.earnings.annual.net_cash_flow_from_financing` |  | Net cash from financing activities for the period. | 报告期内融资活动产生的净现金流。 |
| `resp.200.earnings.annual.change_in_cash_and_equivalents` |  | Net change in cash and equivalents for the period. | 报告期内现金及等价物的净变动额。 |
| `resp.200.earnings.annual.free_cash_flow` |  | Free cash flow for the period. | 报告期内的自由现金流。 |
| `resp.200.earnings.annual.revenue_chg` | Percentage change in revenue. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in revenue, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 营业收入的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.annual.net_income_chg` | Percentage change in net income. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in net income, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 净利润的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.annual.operating_income_chg` | Percentage change in operating income. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in operating income, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 营业利润的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.annual.gross_profit_chg` | Percentage change in gross profit. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in gross profit, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 毛利润的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.annual.net_cash_flow_from_operations_chg` | Percentage change in net cash flow from operations. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in operating cash flow, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 经营现金流的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.annual.net_cash_flow_from_investing_chg` | Percentage change in net cash flow from investing. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in investing cash flow, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 投资现金流的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.annual.net_cash_flow_from_financing_chg` | Percentage change in net cash flow from financing. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in financing cash flow, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 融资现金流的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |
| `resp.200.earnings.annual.free_cash_flow_chg` | Percentage change in free cash flow. QoQ in quarterly payload and YoY in annual payload. Returned only when calculable. | Percentage change in free cash flow, QoQ in the quarterly payload and YoY in the annual payload; present only when calculable. | 自由现金流的变动幅度，季度数据为环比、年度数据为同比；仅在可计算时返回。 |

