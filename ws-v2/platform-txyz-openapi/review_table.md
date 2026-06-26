# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 4 个接口，50 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## searchSmart

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Perform intelligent search that combines web and academic results | Run a single query that blends general web results with academic-paper results, returning a unified ranked list plus a `search_id` you can later pass to `explainSearch` for an AI explanation. | 用一次查询同时检索网页与学术论文，返回融合排序后的结果列表，并附带可交给 explainSearch 生成解读的检索标识。 |
| `param:query` | Search query for scholarly materials | The search terms to look up. | 要检索的查询词。 |
| `param:max_num_results` | Maximum number of search results to return, up to 100 | Caps how many results come back. | 限制返回结果的数量上限。 |
| `param:as_ylo` | Year of publication lower bound | Earliest publication year to include; results published before it are excluded. | 纳入结果的最早出版年份，早于该年份的结果会被排除。 |
| `param:as_yhi` | Year of publication upper bound | Latest publication year to include; results published after it are excluded. | 纳入结果的最晚出版年份，晚于该年份的结果会被排除。 |
| `resp.200.id` | Unique identifier for the search request | Identifier of this search request; pass it to `explainSearch` to get an explanation of these results. | 本次搜索请求的标识，可传给 explainSearch 以解读这批结果。 |
| `resp.200.results` | List of smart search results combining web and academic content | The blended web-and-academic result list. | 融合网页与学术内容的结果列表。 |
| `resp.200.results.title` | Title of the result | Title of the result. | 结果标题。 |
| `resp.200.results.link` | URL to access the content | URL where the result content can be opened. | 可打开该结果内容的链接。 |
| `resp.200.results.snippet` | Brief summary or abstract | Short summary or abstract of the result. | 结果的简要摘要或概述。 |
| `resp.200.results.authors` | List of authors (for academic content) | Authors of the item, populated for academic results. | 条目作者，学术类结果才会有值。 |
| `resp.200.results.number_of_citations` | Number of citations (for academic content) | How many times the item has been cited, populated for academic results. | 条目被引用的次数，学术类结果才会有值。 |
| `resp.200.results.type` | Type of the result | Whether this entry originates from the web or from academic sources. | 该条目来自网页还是学术来源。 |
| `resp.200.results.relevance_score` | Relevance score of the result | How relevant the result is to the query, on a 0-to-1 scale where higher is more relevant. | 结果与查询的相关程度，取值 0 到 1，越高越相关。 |
| `resp.200.search_type` | Type of search results included | Which mix of sources the returned results actually drew from. | 返回结果实际取自的来源组合。 |

## searchWeb

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Perform web search and return structured results | Run a web search and return structured results (title, link, snippet). The response carries a `search_id` reusable with `explainSearch`. | 执行网页搜索并返回结构化结果（标题、链接、摘要），响应中的检索标识可复用于 explainSearch。 |
| `param:query` | Search query for scholarly materials | The search terms to look up. | 要检索的查询词。 |
| `param:max_num_results` | Maximum number of search results to return, up to 100 | Caps how many results come back. | 限制返回结果的数量上限。 |
| `param:as_ylo` | Year of publication lower bound | Earliest publication year to include; results published before it are excluded. | 纳入结果的最早出版年份，早于该年份的结果会被排除。 |
| `param:as_yhi` | Year of publication upper bound | Latest publication year to include; results published after it are excluded. | 纳入结果的最晚出版年份，晚于该年份的结果会被排除。 |
| `resp.200.id` | Unique identifier for the search request | Identifier of this search request; pass it to `explainSearch` to get an explanation of these results. | 本次搜索请求的标识，可传给 explainSearch 以解读这批结果。 |
| `resp.200.results` | List of web search results | The web search result list. | 网页搜索结果列表。 |
| `resp.200.results.title` | Title of the web page | Title of the web page. | 网页标题。 |
| `resp.200.results.link` | URL to access the web page | URL where the web page can be opened. | 可打开该网页的链接。 |
| `resp.200.results.snippet` | Brief summary or preview of the web page content | Short preview of the web page content. | 网页内容的简要预览。 |
| `resp.200.results.display_url` | Display-friendly URL | Human-readable form of the URL for display. | 便于展示的可读版链接。 |
| `resp.200.results.published_date` | Publication date of the web page | When the web page was published. | 网页的发布时间。 |

## searchScholar

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Perform academic paper search using Google Scholar or similar sources | Search academic papers (via Google Scholar or comparable sources) and return per-paper metadata such as authors, citation count, and journal. The response carries a `search_id` reusable with `explainSearch`. | 检索学术论文（通过 Google Scholar 等来源），返回作者、被引次数、期刊等论文元数据，响应中的检索标识可复用于 explainSearch。 |
| `param:query` | Search query for scholarly materials | The search terms to look up. | 要检索的查询词。 |
| `param:max_num_results` | Maximum number of search results to return, up to 100 | Caps how many results come back. | 限制返回结果的数量上限。 |
| `param:as_ylo` | Year of publication lower bound | Earliest publication year to include; results published before it are excluded. | 纳入结果的最早出版年份，早于该年份的结果会被排除。 |
| `param:as_yhi` | Year of publication upper bound | Latest publication year to include; results published after it are excluded. | 纳入结果的最晚出版年份，晚于该年份的结果会被排除。 |
| `resp.200.id` | Unique identifier for the search request | Identifier of this search request; pass it to `explainSearch` to get an explanation of these results. | 本次搜索请求的标识，可传给 explainSearch 以解读这批结果。 |
| `resp.200.results` | List of academic paper results | The academic paper result list. | 学术论文结果列表。 |
| `resp.200.results.title` | Title of the academic paper | Title of the paper. | 论文标题。 |
| `resp.200.results.link` | URL to access the full paper | URL to access the full paper. | 访问论文全文的链接。 |
| `resp.200.results.snippet` | Brief summary or abstract of the paper | Short summary or abstract of the paper. | 论文的摘要或简述。 |
| `resp.200.results.authors` | List of authors | Authors of the paper. | 论文作者。 |
| `resp.200.results.number_of_citations` | Number of citations the paper has received | How many times the paper has been cited. | 论文被引用的次数。 |
| `resp.200.results.year` | Publication year | Year the paper was published. | 论文的出版年份。 |
| `resp.200.results.journal` | Journal or conference name | Journal or conference the paper appeared in. | 论文所在的期刊或会议。 |

## explainSearch

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Generate explanations for search results in different languages and formats | Generate an AI explanation of a previous search's results, addressed by its `search_id`, with controllable output language, format, and depth. | 针对此前某次搜索（通过 search_id 指定）的结果生成 AI 解读，可控制输出语言、格式与详尽程度。 |
| `req.search_id` | ID of the search to explain | Identifier of the earlier search whose results you want explained; obtained from the `id` field of a search response. | 要解读的此前那次搜索的标识，取自某次搜索响应的 id 字段。 |
| `req.response_mode` | Format of the explanation response | Output format of the explanation: a full write-up, a condensed summary, or bullet points. | 解读的输出格式：完整长文、精简摘要或要点列表。 |
| `req.language` | Language code for the explanation (e.g., en, zh, ar) | Language the explanation should be written in, given as a language code (e.g. `en`, `zh`, `ar`). | 解读所用的语言，以语言代码给出（如 `en`、`zh`、`ar`）。 |
| `req.detail_level` | Level of detail in the explanation | How much depth the explanation should go into. | 解读展开的详尽程度。 |
| `resp.200.search_id` | ID of the search being explained | Identifier of the search this explanation refers to. | 本次解读所针对的搜索标识。 |
| `resp.200.explanation` | Detailed explanation of the search results | The generated explanation of the search results. | 针对搜索结果生成的解读正文。 |
| `resp.200.language` | Language of the explanation | Language the explanation was written in. | 解读实际使用的语言。 |
| `resp.200.response_mode` | Format of the response | Output format the explanation was rendered in. | 解读实际采用的输出格式。 |
| `resp.200.summary` | Brief summary of the explanation | A brief summary of the explanation. | 解读的简要摘要。 |
| `resp.200.key_insights` | List of key insights from the search results | Key takeaways distilled from the search results. | 从搜索结果中提炼出的关键要点。 |
| `resp.200.confidence_score` | Confidence score for the explanation | How confident the model is in the explanation, on a 0-to-1 scale where higher is more confident. | 模型对该解读的置信度，取值 0 到 1，越高越自信。 |
| `resp.200.generated_at` | Timestamp when the explanation was generated | When the explanation was generated. | 解读的生成时间。 |

