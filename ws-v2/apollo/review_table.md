# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 54 个接口，506 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## post_apollo_people_match

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Use the People Enrichment endpoint to enrich data for 1 person. To enrich data for up to 10 people with a single API call, use the Bulk People Enrichment endpoint instead. Apollo relies on the information you pass via the endpoint's parameters to identify the correct person to enrich. If you provide more information about a person, Apollo is more likely to find a match within its database. If you only provide general information, such as a name without a domain or email address, you might receive a 200 response, but the response will indicate that no records have been enriched. By default, this endpoint does not return personal emails or phone numbers. Use the reveal_personal_emails and reveal_phone_number parameters to retrieve emails and phone numbers. You can also use the run_waterfall_email and run_waterfall_phone parameters to run waterfall enrichment via this endpoint. gives you broader data coverage by checking connected third-party data sources for contact emails and phone numbers. When you call this endpoint and include at least one waterfall parameter, Apollo returns an immediate synchronous response with demographic and firmographic data, along with a waterfall enrichment request status. Apollo delivers enriched emails and/or phone numbers asynchronously to a configured webhook. **Webhook Response Details:** - When using native enrichment for phone number enrichment, the webhook response follows: - When passing Waterfall flags, the webhook response follows: **Webhook Requirements:** - **HTTPS Required:** Your endpoint must be publicly accessible over HTTPS. - **Rate Limiting:** Ensure your webhook endpoint can handle the volume of webhook traffic sent by Apollo. - **Idempotency:** Apollo may retry webhook calls; your endpoint should be idempotent to handle duplicate payloads safely. Using this endpoint will consume credits based on your account's pricing plan. If you run waterfall enrichment parameters, your depends on the type of data you request (emails and/or phone numbers) and which data source returns enriched data. To view a summary of Apollo's pricing, visit the public pricing page ↗ For detailed information regarding API credit usage, see the API enrichment ↗ section on the *About Credits* page (login required). | Enrich a single person with Apollo's contact and company data; optionally trigger waterfall email/phone enrichment and reveal personal emails or phone numbers. Provide as many identifying parameters (name, email, domain, LinkedIn URL, Apollo id) as possible to improve match accuracy. | 用 Apollo 的联系人与公司数据丰富单个人；可选触发邮箱/电话瀑布式补全，并解锁个人邮箱或电话号码。尽量多提供标识参数（姓名、邮箱、域名、LinkedIn 链接、Apollo id）以提升匹配准确率。 |
| `param:first_name` | The first name of the person. This is typically used in combination with the last_name parameter. Example: tim | Person's first name; pair with last_name to identify by full name when no email or id is available. | 人的名字；在没有邮箱或 id 时与 last_name 搭配按全名匹配。 |
| `param:last_name` | The last name of the person. This is typically used in combination with the first_name parameter. Example: zheng | Person's last name; pair with first_name. | 人的姓氏；与 first_name 搭配使用。 |
| `param:name` | The full name of the person. This will typically be a first name and last name separated by a space. If you use this parameter, you do not need to use the first_name and last_name parameters. Example: tim zheng | Full name as an alternative to sending first_name and last_name separately. | 全名，可替代分别传 first_name 与 last_name。 |
| `param:email` | The email address of the person. Example: example@email.com | Person's email address; the strongest single signal for an accurate match. | 人的邮箱地址；单一最强的精确匹配信号。 |
| `param:hashed_email` | The hashed email of the person. The email should adhere to either the MD5 or SHA-256 hash format. Example: 8d935115b9ff4489f2d1f9249503cadf (MD5) or 97817c0c49994eb500ad0a5e7e2d8aed51977b26424d508f66e4e8887746a152 (SHA-256) | Hashed email used to match without sending the plaintext address.<br>[⚠️Note:源码未声明 MD5 与 SHA-256 之外的取值，详细哈希规范待研发确认。] | 邮箱哈希值，用于在不传明文邮箱的情况下匹配。<br>[⚠️批注:源码未声明 MD5 与 SHA-256 之外的取值，详细哈希规范待研发确认。] |
| `param:organization_name` | The name of the person's employer. This can be the current employer or a previous employer. Example: apollo | Name of the person's employer (current or past), used to disambiguate matches. | 人的雇主名称（现任或曾任），用于区分匹配。 |
| `param:domain` | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. Example: apollo.io or microsoft.com | Web domain of the person's employer (current or past), used to disambiguate matches. | 人的雇主主域名（现任或曾任），用于区分匹配。 |
| `param:id` | The Apollo ID for the person. Each person in the Apollo database is assigned a unique ID. To find IDs, call the People API Search endpoint and identify the values for person_id. Example: 587cf802f65125cad923a266 | Apollo identifier of the person. | 该人员的 Apollo 标识。 |
| `param:linkedin_url` | The URL for the person's LinkedIn profile. Example: http://www.linkedin.com/in/tim-zheng-677ba010 | URL of the person's LinkedIn profile; a strong matching signal. | 人的 LinkedIn 主页链接；很强的匹配信号。 |
| `param:run_waterfall_email` | Set to true to enable email waterfall enrichment | Enable waterfall email enrichment, which queries additional data sources to find an email. | 启用邮箱瀑布式补全，调用更多数据源来寻找邮箱。 |
| `param:run_waterfall_phone` | Set to true to enable phone waterfall enrichment | Enable waterfall phone enrichment, which queries additional data sources to find a phone number. | 启用电话瀑布式补全，调用更多数据源来寻找电话。 |
| `param:reveal_personal_emails` | Set to true if you want to enrich the person's data with personal emails. This potentially consumes credits as part of your Apollo pricing plan . The default value is false. If a person resides in a GDPR -compliant region, Apollo will not reveal their personal email. | Include the person's personal emails in the result; may consume extra credits. | 在结果中包含个人邮箱；可能额外消耗额度。 |
| `param:reveal_phone_number` | Set to true if you want to enrich the person's data with all available phone numbers, including mobile phone numbers. This potentially consumes credits as part of your Apollo pricing plan . The default value is false. If this parameter is set to true, you must enter a webhook URL for the webhook_url parameter. Apollo will asynchronously verify phone numbers for you, then send a JSON response that includes only details about the person's phone numbers to the webhook URL you provide. It can take several minutes for the phone numbers to be delivered. | Include all available phone numbers in the result; when enabled, webhook_url becomes required because numbers are delivered asynchronously. | 在结果中包含所有可用电话；启用后 webhook_url 变为必填，因为号码异步回传。 |
| `param:webhook_url` | If you set the reveal_phone_number parameter to true, this parameter becomes mandatory. Otherwise, do not use this parameter. Enter the webhook URL that specifies where Apollo should send a JSON response that includes the phone number you requested. Apollo suggests testing this flow to ensure you receive the separate response with the phone number. If phone numbers are not revealed delivered to the webhook URL, try applying UTF-8 encoding to the webhook URL. Example: https://webhook.site/cc4cf44e-e047-4774-8dac-473d28474e40; https%3A%2F%2Fwebhook.site%2Fcc4cf44e-e047-4774-8dac-473d28474e40 | Callback URL that receives revealed phone numbers asynchronously; required when reveal_phone_number is enabled. | 异步接收已揭示电话号码的回调地址；reveal_phone_number 启用时必填。 |
| `resp.200.person` | Response object | Enriched profile of the matched person. | 匹配到的人员的丰富后画像。 |
| `resp.200.waterfall` | Response object | Status and results of any waterfall email/phone enrichment that was triggered. | 触发的邮箱/电话瀑布式补全的状态与结果。 |

## post_apollo_people_bulk_match

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Use the Bulk People Enrichment endpoint to enrich data for up to 10 people with a single API call. To enrich data for only 1 person, use the People Enrichment endpoint instead. Apollo relies on the information you pass via the endpoint's parameters to identify the correct people to enrich. When you provide more information, Apollo is more likely to find matches within its database. If you only provide general information, such as a name without a domain or email address, you might receive a 200 response, but the response will indicate that no records have been enriched. The details for each person should be passed as an object with the details[] array. By default, this endpoint does not return personal emails or phone numbers. Use the reveal_personal_emails and reveal_phone_number parameters to retrieve emails and phone numbers. If you set either of these parameters to true, Apollo will attempt to provide emails or phone numbers for all matches. You can use also use the run_waterfall_email and run_waterfall_phone parameters to run waterfall enrichment via this endpoint. gives you broader data coverage by checking connected third-party data sources for contact emails and phone numbers. When you call this endpoint and include at least one waterfall parameter, Apollo returns an immediate synchronous response with demographic and firmographic data, along with a waterfall enrichment request status. Apollo delivers enriched emails and/or phone numbers asynchronously to a configured webhook. **Webhook Response Details:** - When using native enrichment for phone number enrichment, the webhook response follows: - When passing Waterfall flags, the webhook response follows: **Webhook Requirements:** - **HTTPS Required:** Your endpoint must be publicly accessible over HTTPS. - **Rate Limiting:** Ensure your webhook endpoint can handle the volume of webhook traffic sent by Apollo. - **Idempotency:** Apollo may retry webhook calls. Your endpoint should be idempotent to handle duplicate payloads safely. Using this endpoint will consume credits based on your account's pricing plan. If you run waterfall enrichment parameters, your depends on the type of data you request (emails and/or phone numbers) and which data source returns enriched data. To view a summary of Apollo's pricing, visit the public pricing page ↗ For detailed information regarding API credit usage, see the API enrichment ↗ section on the *About Credits* page (login required). This endpoint's rate limit is throttled to 50% of the People Enrichment endpoint's per-minute rate limit, and is 100% of the hourly and daily rate limits for the same individual endpoint. | Enrich up to 10 people in one call by passing an array of person records. Returns per-record match results plus aggregate counts of how many records were enriched and how many credits were spent. | 一次调用最多丰富 10 个人，传入人员记录数组。返回每条记录的匹配结果，以及成功丰富数量、消耗额度等汇总计数。 |
| `param:run_waterfall_email` | Set to true to enable email waterfall enrichment | Enable waterfall email enrichment for every record in the batch. | 为批次中每条记录启用邮箱瀑布式补全。 |
| `param:run_waterfall_phone` | Set to true to enable phone waterfall enrichment | Enable waterfall phone enrichment for every record in the batch. | 为批次中每条记录启用电话瀑布式补全。 |
| `param:reveal_personal_emails` | Set to true if you want to enrich all matched people with personal emails. This potentially consumes credits as part of your Apollo pricing plan . The default value is false. If a person resides in a GDPR -compliant region, Apollo will not reveal their personal email. | Include personal emails for every record; may consume extra credits. | 为每条记录包含个人邮箱；可能额外消耗额度。 |
| `param:reveal_phone_number` | Set to true if you want to enrich the data of all matched people with all available phone numbers, including mobile phone numbers. This potentially consumes credits as part of your Apollo pricing plan . The default value is false. If this parameter is set to true, you must enter a webhook URL for the webhook_url parameter. Apollo will asynchronously verify phone numbers for you, then send a JSON response that includes only details about the phone numbers to the webhook URL you provide. It can take several minutes for the phone numbers to be delivered. | Include all phone numbers for every record; requires webhook_url for asynchronous delivery. | 为每条记录包含所有电话；需 webhook_url 异步回传。 |
| `param:webhook_url` | If you set the reveal_phone_number parameter to true, this parameter becomes mandatory. Otherwise, do not use this parameter. Enter the webhook URL that specifies where Apollo should send a JSON response that includes the phone number you requested. Apollo suggests testing this flow to ensure you receive the separate response with the phone number. If phone numbers are not revealed delivered to the webhook URL, try applying UTF-8 encoding to the webhook URL. Example: https://webhook.site/cc4cf44e-e047-4774-8dac-473d28474e40; https%3A%2F%2Fwebhook.site%2Fcc4cf44e-e047-4774-8dac-473d28474e40 | Callback URL receiving revealed phone numbers; required when reveal_phone_number is enabled. | 接收已揭示电话号码的回调地址；reveal_phone_number 启用时必填。 |
| `req.details` | Provide info for each person you want to enrich as an object within this array. Add up to 10 people. | Array of person records to enrich, one object per person, up to 10. | 待丰富的人员记录数组，每人一个对象，最多 10 条。 |
| `resp.200.status` | Response field | Overall processing status of the bulk request. | 批量请求的整体处理状态。 |
| `resp.200.error_code` | Response field | Error code when the request failed; absent on success. | 失败时的错误码；成功时不返回。 |
| `resp.200.error_message` | Response field | Human-readable error detail when the request failed. | 失败时的可读错误说明。 |
| `resp.200.total_requested_enrichments` | Response field | Number of enrichments requested in this call. | 本次调用请求的丰富数量。 |
| `resp.200.unique_enriched_records` | Response field | Number of distinct records that were successfully enriched. | 成功丰富的去重记录数。 |
| `resp.200.missing_records` | Response field | Number of records that could not be matched. | 未能匹配的记录数。 |
| `resp.200.credits_consumed` | Response field | Credits spent on this bulk enrichment. | 本次批量丰富消耗的额度。 |
| `resp.200.matches` | Response array | Per-record enrichment results, aligned to the input order. | 逐条记录的丰富结果，与输入顺序对应。 |
| `resp.200.waterfall` | Response object | Aggregate status of waterfall enrichment across the batch. | 整批瀑布式补全的汇总状态。 |

## get_apollo_organizations_enrich

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Use the Oganization Enrichment endpoint to enrich data for 1 company. To enrich data for up to 10 companies with a single API call, use the Bulk Organization Enrichment endpoint instead. Calling this endpoint does consume credits as part of your Apollo pricing plan . Enriched data potentially includes industry information, revenue, employee counts, funding round details, and corporate phone numbers and locations. Calling this endpoint does consume credits as part of your Apollo pricing plan . | Enrich a single company by its web domain, returning Apollo's full organization profile. | 按公司主域名丰富单个公司，返回 Apollo 完整的公司画像。 |
| `param:domain` | The domain of the company that you want to enrich. Do not include www., the @ symbol, or similar. Example: apollo.io or microsoft.com | Web domain of the company to enrich, e.g. apollo.io. | 待丰富公司的主域名，例如 apollo.io。 |
| `resp.200.organization` | Response object | Enriched company profile. | 丰富后的公司画像。 |

## post_apollo_organizations_bulk_enrich

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Use the Bulk Organization Enrichment endpoint to enrich data for up to 10 companies with a single API call. To enrich data for only 1 company, use the Organization Enrichment endpoint instead. Enriched data potentially includes industry information, revenue, employee counts, funding round details, and corporate phone numbers and locations. Calling this endpoint does consume credits as part of your Apollo pricing plan . This endpoint's rate limit is throttled to 50% of the Organization Enrichment endpoint's per-minute rate limit, and is 100% of the hourly and daily rate limits for the same individual endpoint. | Enrich up to 10 companies in one call by passing multiple domains. Returns matched organization profiles plus counts of requested, unique, enriched, and missing records. | 一次调用最多丰富 10 个公司，传入多个域名。返回匹配到的公司画像，以及请求数、去重数、丰富数、未命中数等计数。 |
| `param:domains[]` | The domain of each company that you want to enrich. Do not include www., the @ symbol, or similar. Example: apollo.io and microsoft.com | Company domains to enrich, up to 10 per call. | 待丰富的公司域名，每次最多 10 个。 |
| `resp.200.status` | Response field | Overall processing status of the bulk request. | 批量请求的整体处理状态。 |
| `resp.200.error_code` | Response field | Error code when the request failed; absent on success. | 失败时的错误码；成功时不返回。 |
| `resp.200.error_message` | Response field | Human-readable error detail when the request failed. | 失败时的可读错误说明。 |
| `resp.200.total_requested_domains` | Response field | Number of domains submitted in this call. | 本次调用提交的域名数量。 |
| `resp.200.unique_domains` | Response field | Number of distinct domains after deduplication. | 去重后的域名数量。 |
| `resp.200.unique_enriched_records` | Response field | Number of distinct companies successfully enriched. | 成功丰富的去重公司数。 |
| `resp.200.missing_records` | Response field | Number of domains that could not be matched. | 未能匹配的域名数。 |
| `resp.200.organizations` | Response array | Enriched company profiles, one per matched domain. | 丰富后的公司画像，每个匹配域名一条。 |

## post_apollo_mixed_people_api_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Use the People API Search endpoint to find net new people in the Apollo database. Several filters are available to help narrow your search. This endpoint is optimized for API usage and does not consume credits. This endpoint is primarily designed for prospecting net new people. This endpoint does not return email addresses or phone numbers. Use the People Enrichment or Bulk People Enrichment endpoints to enrich data. This endpoint requires a master API key. Refer to Create API Keys to learn how to create a master API key. To protect Apollo's performance for all users, this endpoint has a display limit of 50,000 records (100 records per page, up to 500 pages). Add more filters to narrow your search results as much as possible. This limitation does not restrict your access to Apollo's database; you just need to access the data in batches. | Find net-new people in the Apollo database using filters such as job title, seniority, location, employer attributes, and technologies used. Results are paginated; combine filters to narrow the audience. | 用职位、资历、地区、雇主属性、所用技术等筛选条件在 Apollo 库中查找全新人员。结果分页；组合多个筛选可缩小目标人群。 |
| `param:person_titles[]` | Job titles held by the people you want to find. For a person to be included in search results, they only need to match 1 of the job titles you add. Adding more job titles expands your search results. Results also include job titles with the same terms, even if they are not exact matches. For example, searching for marketing manager might return people with the job title content marketing manager. Use this parameter in combination with the person_seniorities[] parameter to find people based on specific job functions and seniority levels. Examples: sales development representative; marketing manager; research analyst | Job titles to match; a person is included if their current title matches any value. | 要匹配的职位；人的当前职位命中任一值即纳入。 |
| `param:include_similar_titles` | This parameter determines whether people with job titles similar to the titles you define in the person_titles[] parameter are returned in the response. Set this parameter to false when using person_titles[] to return only strict matches for job titles. | Also include people whose titles are similar to those you listed, broadening the audience. | 同时纳入职位与所列相近的人，扩大目标人群。 |
| `param:q_keywords` | A string of words over which we want to filter the results. | Free-text keywords used to further filter results. | 用于进一步筛选结果的自由文本关键词。 |
| `param:person_locations[]` | The location where people live. You can search across cities, US states, and countries. To find people based on the headquarters locations of their current employer, use the organization_locations parameter. Examples: california; ireland; chicago | Locations where people live; matches across cities, US states, and countries. | 人的居住地；可按城市、美国州、国家匹配。 |
| `param:person_seniorities[]` | The job seniority that people hold within their current employer. This enables you to find people that currently hold positions at certain reporting levels, such as Director level or senior IC level. For a person to be included in search results, they only need to match 1 of the seniorities you add. Adding more seniorities expands your search results. Searches only return results based on their current job title, so searching for Director-level employees only returns people that currently hold a Director-level title. If someone was previously a Director, but is currently a VP, they would not be included in your search results. Use this parameter in combination with the person_titles[] parameter to find people based on specific job functions and seniority levels. The following options can be used for this parameter: owner founder c_suite partner vp head director manager senior entry intern | Seniority levels held at the current employer, to target by org level. | 在现任雇主的资历层级，用于按层级定位。 |
| `param:organization_locations[]` | The location of the company headquarters for a person's current employer. You can search across cities, US states, and countries. If a company has several office locations, results are still based on the headquarters location. For example, if you search chicago but a company's HQ location is in boston, people that work for the Boston-based company will not appear in your results, even if they match other parameters. To find people based on their personal location, use the person_locations parameter. Examples: texas; tokyo; spain | Headquarters location of a person's current employer. | 人现任雇主的总部所在地。 |
| `param:q_organization_domains_list[]` | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. This parameter accepts up to 1,000 domains in a single request. Examples: apollo.io; microsoft.com | Employer web domains to match (current or past employer). | 要匹配的雇主主域名（现任或曾任）。 |
| `param:contact_email_status[]` | The email statuses for the people you want to find. You can add multiple statuses to expand your search. The statuses you can search include: verified unverified likely to engage unavailable | Email verification statuses to include, used to control match quality. | 要纳入的邮箱验证状态，用于控制匹配质量。 |
| `param:organization_ids[]` | The Apollo IDs for the companies (employers) you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, call the Organization Search endpoint and identify the values for organization_id. Example: 5e66b6381e05b4008c8331b8 | Apollo company ids whose employees should be included. | 其员工应被纳入的 Apollo 公司 id。 |
| `param:organization_num_employees_ranges[]` | The number range of employees working for the person's current company. This enables you to find people based on the headcount of their employer. You can add multiple ranges to expand your search results. Each range you add needs to be a string, with the upper and lower numbers of the range separated only by a comma. Examples: 1,10; 250,500; 10000,20000 | Employee-count ranges of the current employer, to target by company size. | 现任雇主的员工人数区间，用于按公司规模定位。 |
| `param:revenue_range[min]` | The minimum revenue the person's current employer generates. Use this parameter in combination with revenue_range[max] to set a revenue range. Do not enter currency symbols, commas, or decimal points in the figure. Examples: 500000; 1500000 | Minimum revenue of the current employer; pair with revenue_range[max]. | 现任雇主的最低营收；与 revenue_range[max] 搭配。 |
| `param:revenue_range[max]` | The maximum revenue the person's current employer generates. Use this parameter in combination with revenue_range[min] to set a revenue range. Do not enter currency symbols, commas, or decimal points in the figure. Examples: 500000; 1500000 | Maximum revenue of the current employer; pair with revenue_range[min]. | 现任雇主的最高营收；与 revenue_range[min] 搭配。 |
| `param:currently_using_all_of_technology_uids[]` | Find people based on all of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is updated regularly. Check out the full list of supported technologies by downloading this CSV file . Use underscores (_) to replace spaces and periods for the technologies listed in the CSV file. Examples: salesforce; google_analytics; wordpress_org | Match employers using all of the listed technologies (AND). | 匹配同时使用所列全部技术的雇主（与逻辑）。 |
| `param:currently_using_any_of_technology_uids[]` | Find people based on any of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is updated regularly. Check out the full list of supported technologies by downloading this CSV file . Use underscores (_) to replace spaces and periods for the technologies listed in the CSV file. Examples: salesforce; google_analytics; wordpress_org | Match employers using any of the listed technologies (OR). | 匹配使用所列任一技术的雇主（或逻辑）。 |
| `param:currently_not_using_any_of_technology_uids[]` | Exclude people from your search based on any of the technologies their current employer uses. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is updated regularly. Check out the full list of supported technologies by downloading this CSV file . Use underscores (_) to replace spaces and periods for the technologies listed in the CSV file. Examples: salesforce; google_analytics; wordpress_org | Exclude employers using any of the listed technologies. | 排除使用所列任一技术的雇主。 |
| `param:q_organization_job_titles[]` | The job titles that are listed in active job postings at the person's current employer. Examples: sales manager; research analyst | Job titles appearing in the employer's active job postings. | 出现在雇主在招职位中的职位名称。 |
| `param:organization_job_locations[]` | The locations of the jobs being actively recruited by the person's employer. Examples: atlanta; japan | Locations of jobs the employer is actively recruiting for. | 雇主正在招聘的职位所在地。 |
| `param:organization_num_jobs_range[min]` | The minimum number of job postings active at the person's current employer. Use this parameter in combination with organization_num_jobs_range[max] to set a job postings range. Examples: 50; 500 | Minimum number of active job postings at the employer. | 雇主在招职位的最少数量。 |
| `param:organization_num_jobs_range[max]` | The maximum number of job postings active at the person's current employer. Use this parameter in combination with organization_num_jobs_range[min] to set a job postings range. Examples: 50; 500 | Maximum number of active job postings at the employer. | 雇主在招职位的最多数量。 |
| `param:organization_job_posted_at_range[min]` | The earliest date when jobs were posted by the person's current employer. Use this parameter in combination with organization_job_posted_at_range[max] to set a date range for when jobs posted. Example: 2025-07-25 | Earliest job-posting date at the employer; pair with the max bound. | 雇主职位发布的最早日期；与最大值搭配。 |
| `param:organization_job_posted_at_range[max]` | The latest date when jobs were posted by the person's current employer. Use this parameter in combination with organization_job_posted_at_range[min] to set a date range for when jobs posted. Example: 2025-09-25 | Latest job-posting date at the employer; pair with the min bound. | 雇主职位发布的最晚日期；与最小值搭配。 |
| `param:page` | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4 | Page number to retrieve, used with per_page for pagination. | 要获取的页码，与 per_page 配合分页。 |
| `param:per_page` | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10 | Number of results per page; lowering it can speed up responses. | 每页结果数；调小可加快响应。 |
| `resp.200.total_entries` | Response field | Total number of people matching the filters across all pages. | 所有页中匹配该筛选的人员总数。 |
| `resp.200.people` | Response array | The page of matched people. | 当前页匹配到的人员。 |

## post_apollo_mixed_companies_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Use the Organization Search endpoint to find companies in the Apollo database. Several filters are available to help narrow your search. Calling this endpoint does consume credits as part of your Apollo pricing plan . To protect Apollo's performance for all users, this endpoint has a display limit of 50,000 records (100 records per page, up to 500 pages). Add more filters to narrow your search results as much as possible. This limitation does not restrict your access to Apollo's database; you just need to access the data in batches. | Find companies in the Apollo database using filters such as domain, headcount range, location, revenue, funding, technologies, and active job postings. Results are paginated. | 用域名、人数区间、地区、营收、融资、技术栈、在招职位等筛选条件在 Apollo 库中查找公司。结果分页。 |
| `param:q_organization_domains_list[]` | The domain name for the person's employer. This can be the current employer or a previous employer. Do not include www., the @ symbol, or similar. This parameter accepts up to 1,000 domains in a single request. Examples: apollo.io; microsoft.com | Company web domains to match. | 要匹配的公司主域名。 |
| `param:organization_num_employees_ranges[]` | The number range of employees working for the company. This enables you to find companies based on headcount. You can add multiple ranges to expand your search results. Each range you add needs to be a string, with the upper and lower numbers of the range separated only by a comma. Examples: 1,10; 250,500; 10000,20000 | Employee-count ranges to target by company size. | 按公司规模定位的员工人数区间。 |
| `param:organization_locations[]` | The location of the company headquarters. You can search across cities, US states, and countries. If a company has several office locations, results are still based on the headquarters location. For example, if you search chicago but a company's HQ location is in boston, any Boston-based companies will not appearch in your search results, even if they match other parameters.. To exclude companies based on location, use the organization_not_locations parameter. Examples: texas; tokyo; spain | Company headquarters locations to include. | 要纳入的公司总部所在地。 |
| `param:organization_not_locations[]` | Exclude companies from search results based on the location of the company headquarters. You can use cities, US states, and countries as locations to exclude. This parameter is useful for ensuring you do not prospect in an undesirable territory. For example, if you use ireland as a value, no Ireland-based companies will appear in your search results. Examples: minnesota; ireland; seoul | Company headquarters locations to exclude. | 要排除的公司总部所在地。 |
| `param:revenue_range[min]` | Search for organizations based on their revenue. Use this parameter to set the lower range of organization revenue. Use the revenue_range[max] parameter to set the upper range of revenue. Do not enter currency symbols, commas, or decimal points in the figure. Example: 300000 | Minimum company revenue; pair with revenue_range[max]. | 公司最低营收；与 revenue_range[max] 搭配。 |
| `param:revenue_range[max]` | Search for organizations based on their revenue. Use this parameter to set the upper range of organization revenue. Use the revenue_range[min] parameter to set the lower range of revenue. Do not enter currency symbols, commas, or decimal points in the figure. Example: 50000000 | Maximum company revenue; pair with revenue_range[min]. | 公司最高营收；与 revenue_range[min] 搭配。 |
| `param:currently_using_any_of_technology_uids[]` | Find organizations based on the technologies they currently use. Apollo supports filtering by 1,500+ technologies. Apollo calculates technologies data from multiple sources. This data is updated regularly. Check out the full list of supported technologies by downloading this CSV file . Use underscores (_) to replace spaces and periods for the technologies listed in the CSV file. Examples: salesforce; google_analytics; wordpress_org | Match companies using any of the listed technologies. | 匹配使用所列任一技术的公司。 |
| `param:q_organization_keyword_tags[]` | Filter search results based on keywords associated with companies. For example, you can enter mining as a value to return only companies that have an association with the mining industry. Examples: mining; sales strategy; consulting | Keyword tags describing the company's industry or focus. | 描述公司行业或方向的关键词标签。 |
| `param:q_organization_name` | Filter search results to include a specific company name. If the value you enter for this parameter does not match with a company's name, the company will not appear in search results, even if it matches other parameters. Partial matches are accepted. For example, if you filter by the value marketing, a company called NY Marketing Unlimited would still be eligible as a search result, but NY Market Analysis would not be eligible. Example: apollo or mining | Filter by company name. | 按公司名称筛选。 |
| `param:organization_ids[]` | The Apollo IDs for the companies you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, identify the values for organization_id when you call this endpoint. Example: 5e66b6381e05b4008c8331b8 | Apollo company ids to include. | 要纳入的 Apollo 公司 id。 |
| `param:latest_funding_amount_range[min]` | The minimum amount the company received with its most recent funding round. Use this parameter in combination with latest_funding_amount_range[max] to set a monetary range for the company's most recent funding round. Do not enter currency symbols, commas, or decimal points in the figure. Examples: 5000000; 15000000 | Minimum amount of the company's most recent funding round. | 公司最近一轮融资的最小金额。 |
| `param:latest_funding_amount_range[max]` | The maximium amount the company received with its most recent funding round. Use this parameter in combination with latest_funding_amount_range[min] to set a monetary range for the company's most recent funding round. Do not enter currency symbols, commas, or decimal points in the figure. Examples: 5000000; 15000000 | Maximum amount of the company's most recent funding round. | 公司最近一轮融资的最大金额。 |
| `param:total_funding_range[min]` | The minimum amount the company received during all of its funding rounds combined. Use this parameter in combination with total_funding_range[max] to set a monetary range for all of the company's funding rounds. Do not enter currency symbols, commas, or decimal points in the figure. Examples: 50000000; 350000000 | Minimum total funding raised by the company. | 公司累计融资的最小总额。 |
| `param:total_funding_range[max]` | The maximum amount the company received during all of its funding rounds combined. Use this parameter in combination with total_funding_range[min] to set a monetary range for all of the company's funding rounds. Do not enter currency symbols, commas, or decimal points in the figure. Examples: 50000000; 350000000 | Maximum total funding raised by the company. | 公司累计融资的最大总额。 |
| `param:latest_funding_date_range[min]` | The earliest date when the company received its most recent funding round. Use this parameter in combination with latest_funding_date_range[max] to set a date range for when the company received its most recent funding round. Example: 2025-07-25 | Earliest date of the company's most recent funding; pair with the max bound. | 公司最近一轮融资的最早日期；与最大值搭配。 |
| `param:latest_funding_date_range[max]` | The latest date when the company received its most recent funding round. Use this parameter in combination with latest_funding_date_range[min] to set a date range for when the company received its most recent funding round. Example: 2025-09-25 | Latest date of the company's most recent funding; pair with the min bound. | 公司最近一轮融资的最晚日期；与最小值搭配。 |
| `param:q_organization_job_titles[]` | The job titles that are listed in active job postings at the company. Examples: sales manager; research analyst | Job titles appearing in the company's active job postings. | 出现在公司在招职位中的职位名称。 |
| `param:organization_job_locations[]` | The locations of the jobs being actively recruited by the company. Examples: atlanta; japan | Locations of jobs the company is actively recruiting for. | 公司正在招聘的职位所在地。 |
| `param:organization_num_jobs_range[min]` | The minimum number of job postings active at the company. Use this parameter in combination with organization_num_jobs_range[max] to set a job postings range. Examples: 50; 500 | Minimum number of active job postings at the company. | 公司在招职位的最少数量。 |
| `param:organization_num_jobs_range[max]` | The maximum number of job postings active at the company. Use this parameter in combination with organization_num_jobs_range[min] to set a job postings range. Examples: 50; 500 | Maximum number of active job postings at the company. | 公司在招职位的最多数量。 |
| `param:organization_job_posted_at_range[min]` | The earliest date when jobs were posted by the company. Use this parameter in combination with organization_job_posted_at_range[max] to set a date range for when jobs posted. Example: 2025-07-25 | Earliest job-posting date at the company; pair with the max bound. | 公司职位发布的最早日期；与最大值搭配。 |
| `param:organization_job_posted_at_range[max]` | The latest date when jobs were posted by the company. Use this parameter in combination with organization_job_posted_at_range[min] to set a date range for when jobs posted. Example: 2025-09-25 | Latest job-posting date at the company; pair with the min bound. | 公司职位发布的最晚日期；与最小值搭配。 |
| `param:page` | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4 | Page number to retrieve, used with per_page for pagination. | 要获取的页码，与 per_page 配合分页。 |
| `param:per_page` | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10 | Number of results per page; lowering it can speed up responses. | 每页结果数；调小可加快响应。 |
| `resp.200.breadcrumbs` | Response array | Applied-filter breadcrumbs echoing how the result set was narrowed. | 已应用筛选的面包屑，回显结果是如何被缩小的。 |
| `resp.200.partial_results_only` | Response field | Whether only a partial result set was returned. | 是否只返回了部分结果。 |
| `resp.200.has_join` | Response field | Internal flag indicating a join was applied to the query.<br>[⚠️Note:源码未声明该字段的业务含义，待研发确认。] | 内部标志，表示查询进行了 join。<br>[⚠️批注:源码未声明该字段的业务含义，待研发确认。] |
| `resp.200.disable_eu_prospecting` | Response field | Whether EU prospecting was disabled for this query, per compliance settings. | 本次查询是否按合规设置禁用了欧盟潜客挖掘。 |
| `resp.200.partial_results_limit` | Response field | The cap that triggered partial results, when applicable. | 触发部分结果时所对应的上限。 |
| `resp.200.pagination` | Response object | Pagination metadata for the result set. | 结果集的分页元数据。 |
| `resp.200.accounts` | Response array | Matching companies already saved as accounts in your CRM. | 已作为账户保存在 CRM 中的匹配公司。 |
| `resp.200.organizations` | Response array | Matching companies from the Apollo database. | 来自 Apollo 库的匹配公司。 |
| `resp.200.model_ids` | Response array | Identifiers of the records backing the results.<br>[⚠️Note:源码未声明该字段的业务含义，待研发确认。] | 支撑结果的记录标识。<br>[⚠️批注:源码未声明该字段的业务含义，待研发确认。] |
| `resp.200.num_fetch_result` | Response field | Number of records fetched for this page. | 本页抓取的记录数。 |
| `resp.200.derived_params` | Response field | Query parameters Apollo derived from your input. | Apollo 根据你的输入推导出的查询参数。 |

## get_apollo_organizations_organization_id_job_postings

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Use the Organization Job Postings endpoint to retrieve the current job postings for companies. This can help you identify companies that are growing headcount in areas that are strategically important for you. Calling this endpoint does consume credits as part of your Apollo pricing plan . To protect Apollo's performance for all users, this endpoint has a display limit of 10,000 records. This limitation does not restrict your access to Apollo's database; you just need to access the data in batches. | Retrieve the current active job postings for a given organization, useful for identifying hiring signals and growth areas. | 获取指定公司当前在招的职位，可用于识别招聘信号与增长方向。 |
| `param:organization_id` | The organization ID of the company for which you want to find job postings. Each company in the Apollo database is assigned a unique ID. To find IDs, call the Organization Search endpoint and identify the values for organization_id. Example: 5e66b6381e05b4008c8331b8 | Apollo id of the company whose job postings you want. | 要查询在招职位的公司 Apollo id。 |
| `param:page` | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4 | Page number to retrieve, used with per_page for pagination. | 要获取的页码，与 per_page 配合分页。 |
| `param:per_page` | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10 | Number of results per page; lowering it can speed up responses. | 每页结果数；调小可加快响应。 |
| `resp.200.organization_job_postings` | Response array | The company's current active job postings. | 该公司当前在招的职位。 |

## get_apollo_organizations_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Use the Get Complete Organization Info endpoint to retrieve complete details about an organization in the Apollo database. This endpoint requires a master API key. If you attempt to call the endpoint without a master key, you will receive a 403 response. Refer to Create API Keys to learn how to create a master API key. u003e ? Credits u003e u003e Using this endpoint potentially consumes your account’s credits. Refer to Apollo’s for more details. | Retrieve the complete profile of an organization by its Apollo id. | 按 Apollo id 获取公司的完整画像。 |
| `param:id` | The Apollo ID for the organization that you want to research. To find organization IDs, call the Organization Search endpoint and identify the organizaton_id value for the organization. Example: 5e66b6381e05b4008c8331b8 | Apollo id of the organization to retrieve. | 要查询的公司 Apollo id。 |
| `resp.200.organization` | Response object | The full organization profile. | 公司的完整画像。 |

## post_apollo_news_articles_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Use the News Articles Search endpoint to find news articles related to companies in the Apollo database. Several filters are available to help narrow your search. Calling this endpoint does consume credits as part of your Apollo pricing plan . | Find news articles tied to companies in the Apollo database, optionally filtered by organization, category, and publish-date window. Results are paginated. | 查找与 Apollo 库中公司关联的新闻，可按公司、类别、发布时间窗口筛选。结果分页。 |
| `param:organization_ids[]` | The Apollo IDs for the companies you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, call the Organization Search endpoint and identify the values for organization_id. Example: 5e66b6381e05b4008c8331b8 | Apollo company ids whose news you want. | 要查询新闻的 Apollo 公司 id。 |
| `param:categories[]` | Filter your search to include only certain categories or sub-categories of news. Use the News search filter for companies within Apollo to uncover all possible categories and sub-categories. Examples: hires; investment; contract | News categories to filter by, such as funding or leadership changes.<br>[⚠️Note:源码未声明完整的类别取值，待研发确认。] | 要筛选的新闻类别，如融资、管理层变动等。<br>[⚠️批注:源码未声明完整的类别取值，待研发确认。] |
| `param:published_at[min]` | Set the lower bound of the date range you want to search. Use this parameter in combination with the published_at[max] parameter. This date should fall before the published_at[max] date. The date should be formatted as YYYY-MM-DD. Example: 2025-02-15 | Earliest publish date; pair with published_at[max]. | 最早发布日期；与 published_at[max] 搭配。 |
| `param:published_at[max]` | Set the upper bound of the date range you want to search. Use this parameter in combination with the published_at[min] parameter. This date should fall after the published_at[min] date. The date should be formatted as YYYY-MM-DD. Example: 2025-05-15 | Latest publish date; pair with published_at[min]. | 最晚发布日期；与 published_at[min] 搭配。 |
| `param:page` | The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the per_page parameter to make search results for navigable and improve the performance of the endpoint. Example: 4 | Page number to retrieve, used with per_page for pagination. | 要获取的页码，与 per_page 配合分页。 |
| `param:per_page` | The number of search results that should be returned for each page. Limiting the number of results per page improves the endpoint's performance. Use the page parameter to search the different pages of data. Example: 10 | Number of results per page; lowering it can speed up responses. | 每页结果数；调小可加快响应。 |
| `resp.200.pagination` | Response object | Pagination metadata for the result set. | 结果集的分页元数据。 |
| `resp.200.news_articles` | Response array | The page of matching news articles. | 当前页匹配到的新闻。 |

## post_apollo_accounts

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Create a new account. Duplicate domains are not allowed. Requires a master API key. | Create a new account (a company saved in your team's CRM). Duplicate domains are rejected. Requires a master API key. | 创建账户（保存在团队 CRM 中的公司）。域名重复会被拒绝。需主 API key。 |
| `req.name` | Account name | Account (company) name to create. | 要创建的账户（公司）名称。 |
| `req.domain` | Account domain | Account's primary web domain; must be unique, duplicates are rejected. | 账户的主域名；须唯一，重复会被拒绝。 |
| `req.owner_id` | Owner ID | Apollo user id to assign as the account owner. | 指派为账户负责人的 Apollo 用户 id。 |
| `req.account_stage_id` | Account stage ID | Id of the stage to place the account in. | 将账户置于其中的阶段 id。 |

## patch_apollo_accounts_account_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Update fields on an existing account. Requires a master API key. | Update fields on an existing account identified by account_id. Only the fields you send are changed. Requires a master API key. | 按 account_id 更新已有账户的字段，仅修改你传入的字段。需主 API key。 |
| `param:account_id` | Account ID | Apollo id of the account to update. | 要更新的账户 Apollo id。 |
| `req.name` | Account name | New account name. | 新的账户名称。 |
| `req.domain` | Account domain | New primary web domain. | 新的主域名。 |
| `req.owner_id` | Owner ID | New account owner's Apollo user id. | 新的账户负责人 Apollo 用户 id。 |
| `req.account_stage_id` | Account stage ID | New stage id for the account. | 账户的新阶段 id。 |
| `req.raw_address` | Raw address | Free-text postal address for the account. | 账户的自由文本邮寄地址。 |
| `req.phone` | Phone number | Account's phone number. | 账户的电话号码。 |
| `req.typed_custom_fields` | Typed custom fields object | Custom-field values to set, keyed by field id. | 要设置的自定义字段值，以字段 id 为键。 |

## post_apollo_accounts_bulk_create

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Bulk create accounts. Requires a master API key. | Create multiple accounts in one call. The response separates records newly created from those that already existed. Requires a master API key. | 一次创建多个账户。响应把新建记录与已存在记录分开返回。需主 API key。 |
| `req.accounts` | Array of accounts to create | Array of account objects to create. | 要创建的账户对象数组。 |
| `req.append_label_names` | Label names to append to each created account | Label names to attach to every created account. | 附加到每个新建账户上的标签名。 |
| `req.run_dedupe` | Enable deduplication. Default false. | Run deduplication so existing accounts are reused instead of duplicated. | 执行去重，使已存在账户被复用而非重复创建。 |
| `resp.200.created_accounts` | Accounts created in this request | Accounts newly created by this call. | 本次新建的账户。 |
| `resp.200.created_accounts[].id` | Account ID | Apollo id of the account. | 该账户的 Apollo id。 |
| `resp.200.created_accounts[].name` | Account name | Account (company) name. | 账户（公司）名称。 |
| `resp.200.created_accounts[].domain` | Account domain | Account's primary web domain. | 账户的主域名。 |
| `resp.200.created_accounts[].team_id` | Team ID | Id of the team that owns this account. | 拥有该账户的团队 id。 |
| `resp.200.created_accounts[].owner_id` | Owner ID | Apollo user id of the account owner. | 账户负责人的 Apollo 用户 id。 |
| `resp.200.created_accounts[].account_stage_id` | Account stage ID | Id of the account's current stage. | 账户当前阶段的 id。 |
| `resp.200.created_accounts[].phone` | Phone number | Account's phone number. | 账户的电话号码。 |
| `resp.200.created_accounts[].created_at` | Created timestamp | Timestamp when the account was created. | 账户创建时间。 |
| `resp.200.created_accounts[].updated_at` | Updated timestamp | Timestamp when the account was last updated. | 账户最近更新时间。 |
| `resp.200.existing_accounts` | Accounts that already existed (dedupe matches) | Accounts that already existed and were matched instead of created. | 已存在、被匹配而非新建的账户。 |
| `resp.200.existing_accounts[].id` | Account ID | Apollo id of the account. | 该账户的 Apollo id。 |
| `resp.200.existing_accounts[].name` | Account name | Account (company) name. | 账户（公司）名称。 |
| `resp.200.existing_accounts[].domain` | Account domain | Account's primary web domain. | 账户的主域名。 |
| `resp.200.existing_accounts[].team_id` | Team ID | Id of the team that owns this account. | 拥有该账户的团队 id。 |
| `resp.200.existing_accounts[].owner_id` | Owner ID | Apollo user id of the account owner. | 账户负责人的 Apollo 用户 id。 |
| `resp.200.existing_accounts[].account_stage_id` | Account stage ID | Id of the account's current stage. | 账户当前阶段的 id。 |
| `resp.200.existing_accounts[].phone` | Phone number | Account's phone number. | 账户的电话号码。 |
| `resp.200.existing_accounts[].created_at` | Created timestamp | Timestamp when the account was created. | 账户创建时间。 |
| `resp.200.existing_accounts[].updated_at` | Updated timestamp | Timestamp when the account was last updated. | 账户最近更新时间。 |

## post_apollo_accounts_bulk_update

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Bulk update accounts. Requires a master API key. | Update multiple accounts in one call by pairing account_ids with the attributes to change. Supports asynchronous processing. Requires a master API key. | 一次更新多个账户，将 account_ids 与要修改的属性配对。支持异步处理。需主 API key。 |
| `req.account_ids` | IDs of accounts to update | Ids of the accounts to update. | 要更新的账户 id。 |
| `req.account_attributes` | List of account attribute update objects | Attribute values applied to the targeted accounts. | 应用到目标账户的属性值。 |
| `req.account_attributes[].name` | Account name | New account name to apply. | 要应用的新账户名称。 |
| `req.account_attributes[].owner_id` | Owner ID | New owner's Apollo user id to apply. | 要应用的新负责人 Apollo 用户 id。 |
| `req.account_attributes[].account_stage_id` | Account stage ID | New stage id to apply. | 要应用的新阶段 id。 |
| `req.async` | Run asynchronously. Default false. | Process the update asynchronously rather than waiting for completion. | 异步处理更新，而非等待完成。 |
| `resp.200.accounts` | Updated accounts | The updated accounts. | 已更新的账户。 |
| `resp.200.accounts[].id` | Account ID | Apollo id of the updated account. | 已更新账户的 Apollo id。 |
| `resp.200.accounts[].account_stage_id` | Account stage ID | Account's stage id after the update. | 更新后账户的阶段 id。 |

## post_apollo_accounts_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Search for accounts. Requires a master API key. | Search your team's accounts by name, stage, and label, with sorting and pagination. Requires a master API key. | 按名称、阶段、标签搜索团队账户，支持排序与分页。需主 API key。 |
| `req.q_organization_name` | Organization name query | Filter accounts by company name. | 按公司名称筛选账户。 |
| `req.account_stage_ids` | Filter by account stage IDs | Only include accounts in these stages. | 仅纳入处于这些阶段的账户。 |
| `req.account_label_ids` | Filter by account label IDs | Only include accounts carrying these labels. | 仅纳入带有这些标签的账户。 |
| `req.sort_by_field` | Sort field (e.g. account_last_activity_date, account_created_at, account_updated_at) | Field to sort the results by. | 结果排序所依据的字段。 |
| `req.sort_ascending` | Sort ascending | Sort ascending when true, descending when false. | 为 true 时升序，false 时降序。 |
| `req.page` | Page number | Page number to retrieve. | 要获取的页码。 |
| `req.per_page` | Items per page | Number of results per page. | 每页结果数。 |

## get_apollo_accounts_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | View an account by ID. Requires a master API key. | Retrieve a single account by its id. Requires a master API key. | 按 id 获取单个账户。需主 API key。 |
| `param:id` | Account ID | Apollo id of the account to retrieve. | 要查询的账户 Apollo id。 |

## post_apollo_accounts_update_owners

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Update account owner for multiple accounts. Requires a master API key. | Reassign the owner of multiple accounts at once. Requires a master API key. | 一次为多个账户重新指派负责人。需主 API key。 |
| `param:account_ids[]` | Account IDs | Ids of the accounts to reassign. | 要重新指派的账户 id。 |
| `param:owner_id` | New owner ID | Apollo user id of the new owner for all listed accounts. | 所有所列账户的新负责人 Apollo 用户 id。 |
| `resp.200.accounts` | Updated accounts | The accounts whose owner was changed. | 负责人已变更的账户。 |
| `resp.200.accounts[].id` | Account ID | Apollo id of the account. | 账户的 Apollo id。 |
| `resp.200.accounts[].owner_id` | Owner ID | Account owner's Apollo user id after the change. | 变更后账户负责人的 Apollo 用户 id。 |
| `resp.200.accounts[].crm_owner_id` | CRM owner ID | Corresponding owner id in the connected CRM, when synced. | 已同步时在所连 CRM 中对应的负责人 id。 |

## get_apollo_account_stages

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List account stages. Requires a master API key. | List all account stages configured for your team. Use the returned ids to set or filter account_stage_id elsewhere. Requires a master API key. | 列出团队配置的所有账户阶段。返回的 id 可在别处用于设置或筛选 account_stage_id。需主 API key。 |
| `resp.200.account_stages` | Account stages list | The list of configured account stages. | 已配置的账户阶段列表。 |
| `resp.200.account_stages[].id` | Stage ID | Stage id; use it to set or filter account_stage_id. | 阶段 id；可用于设置或筛选 account_stage_id。 |
| `resp.200.account_stages[].team_id` | Team ID | Id of the team that owns the stage. | 拥有该阶段的团队 id。 |
| `resp.200.account_stages[].display_name` | Display name | Stage name shown in the Apollo UI. | 在 Apollo 界面中显示的阶段名称。 |
| `resp.200.account_stages[].name` | Name | Internal name of the stage. | 阶段的内部名称。 |
| `resp.200.account_stages[].display_order` | Display order | Position of the stage in the ordered pipeline. | 阶段在有序流程中的位置。 |
| `resp.200.account_stages[].default_exclude_for_leadgen` | Default exclude for leadgen | Whether accounts in this stage are excluded from lead generation by default. | 处于该阶段的账户是否默认从潜客生成中排除。 |
| `resp.200.account_stages[].category` | Category | Category the stage belongs to.<br>[⚠️Note:源码未声明该字段的取值集合，待研发确认。] | 阶段所属的类别。<br>[⚠️批注:源码未声明该字段的取值集合，待研发确认。] |
| `resp.200.account_stages[].is_meeting_set` | Is meeting set | Whether this stage represents a meeting having been set. | 该阶段是否代表已安排会议。 |

## post_apollo_contacts

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Create a new contact. Requires a master API key. | Create a new contact (a person saved in your team's CRM). Requires a master API key. | 创建联系人（保存在团队 CRM 中的人）。需主 API key。 |
| `req.first_name` | First name | Contact's first name. | 联系人的名字。 |
| `req.last_name` | Last name | Contact's last name. | 联系人的姓氏。 |
| `req.organization_name` | Organization name | Name of the contact's employer. | 联系人雇主的名称。 |
| `req.title` | Title | Contact's job title. | 联系人的职位。 |
| `req.account_id` | Account ID | Apollo id of the account to link this contact to. | 要关联此联系人的账户 Apollo id。 |
| `req.email` | Email | Contact's email address. | 联系人的邮箱地址。 |
| `req.website_url` | Website URL | Contact's website URL. | 联系人的网站链接。 |
| `req.label_names` | Labels to set on the contact | Labels to apply to the contact. | 要应用到联系人的标签。 |
| `req.contact_stage_id` | Contact stage ID | Id of the stage to place the contact in. | 将联系人置于其中的阶段 id。 |
| `req.present_raw_address` | Raw address | Contact's current free-text address. | 联系人当前的自由文本地址。 |
| `req.direct_phone` | Direct phone | Contact's direct phone number. | 联系人的直拨电话。 |
| `req.corporate_phone` | Corporate phone | Contact's corporate phone number. | 联系人的公司电话。 |
| `req.mobile_phone` | Mobile phone | Contact's mobile phone number. | 联系人的手机号码。 |
| `req.home_phone` | Home phone | Contact's home phone number. | 联系人的家庭电话。 |
| `req.other_phone` | Other phone | Contact's other phone number. | 联系人的其他电话。 |
| `req.typed_custom_fields` | Typed custom fields object | Custom-field values to set, keyed by field id. | 要设置的自定义字段值，以字段 id 为键。 |
| `req.run_dedupe` | Enable deduplication. Default false. | Run deduplication so an existing matching contact is reused instead of duplicated. | 执行去重，使匹配到的已有联系人被复用而非重复创建。 |

## get_apollo_contacts_contact_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | View a contact by ID. Requires a master API key. | Retrieve a single contact by its id. Requires a master API key. | 按 id 获取单个联系人。需主 API key。 |
| `param:contact_id` | Contact ID | Apollo id of the contact to retrieve. | 要查询的联系人 Apollo id。 |
| `resp.200.contact` | Contact object | The retrieved contact. | 查询到的联系人。 |
| `resp.200.contact.id` | Contact ID | Apollo id of the contact. | 联系人的 Apollo id。 |
| `resp.200.contact.first_name` | First name | Contact's first name. | 联系人的名字。 |
| `resp.200.contact.last_name` | Last name | Contact's last name. | 联系人的姓氏。 |
| `resp.200.contact.organization_name` | Organization name | Name of the contact's employer. | 联系人雇主的名称。 |
| `resp.200.contact.title` | Title | Contact's job title. | 联系人的职位。 |
| `resp.200.contact.email` | Email | Contact's email address. | 联系人的邮箱地址。 |
| `resp.200.contact.phone_numbers` | Phone numbers | The contact's phone numbers. | 联系人的电话号码列表。 |
| `resp.200.contact.phone_numbers[].raw_number` | Raw number | Phone number as originally stored. | 原始存储的电话号码。 |
| `resp.200.contact.phone_numbers[].sanitized_number` | Sanitized number | Phone number normalized to a standard format. | 规范化为标准格式的电话号码。 |
| `resp.200.contact.owner_id` | Owner ID | Apollo user id of the contact owner. | 联系人负责人的 Apollo 用户 id。 |
| `resp.200.contact.account_id` | Account ID | Apollo id of the linked account. | 所关联账户的 Apollo id。 |
| `resp.200.contact.present_raw_address` | Raw address | Contact's current free-text address. | 联系人当前的自由文本地址。 |
| `resp.200.contact.linkedin_url` | LinkedIn URL | URL of the contact's LinkedIn profile. | 联系人 LinkedIn 主页链接。 |
| `resp.200.contact.updated_at` | Updated timestamp | Timestamp when the contact was last updated. | 联系人最近更新时间。 |

## patch_apollo_contacts_contact_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Update fields on an existing contact. Requires a master API key. | Update fields on an existing contact identified by contact_id. Only the fields you send are changed. Requires a master API key. | 按 contact_id 更新已有联系人的字段，仅修改你传入的字段。需主 API key。 |
| `param:contact_id` | Contact ID | Apollo id of the contact to update. | 要更新的联系人 Apollo id。 |
| `req.first_name` | First name | Contact's first name. | 联系人的名字。 |
| `req.last_name` | Last name | Contact's last name. | 联系人的姓氏。 |
| `req.organization_name` | Organization name | Name of the contact's employer. | 联系人雇主的名称。 |
| `req.title` | Title | Contact's job title. | 联系人的职位。 |
| `req.account_id` | Account ID | Apollo id of the account to link this contact to. | 要关联此联系人的账户 Apollo id。 |
| `req.email` | Email | Contact's email address. | 联系人的邮箱地址。 |
| `req.website_url` | Website URL | Contact's website URL. | 联系人的网站链接。 |
| `req.label_names` | Labels to set on the contact | Labels to apply to the contact. | 要应用到联系人的标签。 |
| `req.contact_stage_id` | Contact stage ID | Id of the stage to place the contact in. | 将联系人置于其中的阶段 id。 |
| `req.present_raw_address` | Raw address | Contact's current free-text address. | 联系人当前的自由文本地址。 |
| `req.direct_phone` | Direct phone | Contact's direct phone number. | 联系人的直拨电话。 |
| `req.corporate_phone` | Corporate phone | Contact's corporate phone number. | 联系人的公司电话。 |
| `req.mobile_phone` | Mobile phone | Contact's mobile phone number. | 联系人的手机号码。 |
| `req.home_phone` | Home phone | Contact's home phone number. | 联系人的家庭电话。 |
| `req.other_phone` | Other phone | Contact's other phone number. | 联系人的其他电话。 |
| `req.typed_custom_fields` | Typed custom fields object | Custom-field values to set, keyed by field id. | 要设置的自定义字段值，以字段 id 为键。 |
| `resp.200.contact` | Updated contact | The updated contact. | 已更新的联系人。 |
| `resp.200.contact.id` | Contact ID | Apollo id of the contact. | 联系人的 Apollo id。 |
| `resp.200.contact.first_name` | First name | Contact's first name. | 联系人的名字。 |
| `resp.200.contact.last_name` | Last name | Contact's last name. | 联系人的姓氏。 |
| `resp.200.contact.email` | Email | Contact's email address. | 联系人的邮箱地址。 |
| `resp.200.contact.title` | Title | Contact's job title. | 联系人的职位。 |
| `resp.200.contact.organization_name` | Organization name | Name of the contact's employer. | 联系人雇主的名称。 |
| `resp.200.contact.owner_id` | Owner ID | Apollo user id of the contact owner. | 联系人负责人的 Apollo 用户 id。 |
| `resp.200.contact.account_id` | Account ID | Apollo id of the linked account. | 所关联账户的 Apollo id。 |
| `resp.200.contact.present_raw_address` | Raw address | Contact's current free-text address. | 联系人当前的自由文本地址。 |

## post_apollo_contacts_bulk_create

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Bulk create contacts. Requires a master API key. | Create multiple contacts in one call. The response separates records newly created from those that already existed. Requires a master API key. | 一次创建多个联系人。响应把新建记录与已存在记录分开返回。需主 API key。 |
| `req.contacts` | Array of contacts to create | Array of contact objects to create. | 要创建的联系人对象数组。 |
| `req.append_label_names` | Label names to append to each created contact | Label names to attach to every created contact. | 附加到每个新建联系人上的标签名。 |
| `req.run_dedupe` | Enable deduplication. Default false. | Run deduplication so existing contacts are reused instead of duplicated. | 执行去重，使已存在联系人被复用而非重复创建。 |
| `resp.200.created_contacts` | Contacts created in this request | Contacts newly created by this call. | 本次新建的联系人。 |
| `resp.200.created_contacts[].id` | Contact ID | Apollo id of the contact. | 联系人的 Apollo id。 |
| `resp.200.created_contacts[].first_name` | First name | Contact's first name. | 联系人的名字。 |
| `resp.200.created_contacts[].last_name` | Last name | Contact's last name. | 联系人的姓氏。 |
| `resp.200.created_contacts[].organization_name` | Organization name | Name of the contact's employer. | 联系人雇主的名称。 |
| `resp.200.created_contacts[].title` | Title | Contact's job title. | 联系人的职位。 |
| `resp.200.created_contacts[].owner_id` | Owner ID | Apollo user id of the contact owner. | 联系人负责人的 Apollo 用户 id。 |
| `resp.200.created_contacts[].account_id` | Account ID | Apollo id of the linked account. | 所关联账户的 Apollo id。 |
| `resp.200.created_contacts[].email` | Email | Contact's email address. | 联系人的邮箱地址。 |
| `resp.200.created_contacts[].phone_numbers` | Phone numbers | The contact's phone numbers. | 联系人的电话号码列表。 |
| `resp.200.created_contacts[].typed_custom_fields` | Typed custom fields object | Custom-field values on the contact. | 联系人上的自定义字段值。 |
| `resp.200.created_contacts[].updated_at` | Updated timestamp | Timestamp when the contact was last updated. | 联系人最近更新时间。 |
| `resp.200.existing_contacts` | Contacts that already existed (dedupe matches) | Contacts that already existed and were matched instead of created. | 已存在、被匹配而非新建的联系人。 |
| `resp.200.existing_contacts[].id` | Contact ID | Apollo id of the contact. | 联系人的 Apollo id。 |
| `resp.200.existing_contacts[].first_name` | First name | Contact's first name. | 联系人的名字。 |
| `resp.200.existing_contacts[].last_name` | Last name | Contact's last name. | 联系人的姓氏。 |
| `resp.200.existing_contacts[].organization_name` | Organization name | Name of the contact's employer. | 联系人雇主的名称。 |
| `resp.200.existing_contacts[].title` | Title | Contact's job title. | 联系人的职位。 |
| `resp.200.existing_contacts[].owner_id` | Owner ID | Apollo user id of the contact owner. | 联系人负责人的 Apollo 用户 id。 |
| `resp.200.existing_contacts[].account_id` | Account ID | Apollo id of the linked account. | 所关联账户的 Apollo id。 |
| `resp.200.existing_contacts[].email` | Email | Contact's email address. | 联系人的邮箱地址。 |
| `resp.200.existing_contacts[].phone_numbers` | Phone numbers | The contact's phone numbers. | 联系人的电话号码列表。 |
| `resp.200.existing_contacts[].typed_custom_fields` | Typed custom fields object | Custom-field values on the contact. | 联系人上的自定义字段值。 |
| `resp.200.existing_contacts[].updated_at` | Updated timestamp | Timestamp when the contact was last updated. | 联系人最近更新时间。 |

## post_apollo_contacts_bulk_update

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Bulk update contacts. Requires a master API key. | Update multiple contacts in one call. Requires a master API key. | 一次更新多个联系人。需主 API key。 |
| `resp.200.contacts` | Updated contacts | The updated contacts. | 已更新的联系人。 |
| `resp.200.contacts[].id` | Contact ID | Apollo id of the contact. | 联系人的 Apollo id。 |
| `resp.200.contacts[].first_name` | First name | Contact's first name. | 联系人的名字。 |
| `resp.200.contacts[].last_name` | Last name | Contact's last name. | 联系人的姓氏。 |
| `resp.200.contacts[].email` | Email | Contact's email address. | 联系人的邮箱地址。 |
| `resp.200.contacts[].title` | Title | Contact's job title. | 联系人的职位。 |
| `resp.200.contacts[].organization_name` | Organization name | Name of the contact's employer. | 联系人雇主的名称。 |
| `resp.200.contacts[].owner_id` | Owner ID | Apollo user id of the contact owner. | 联系人负责人的 Apollo 用户 id。 |
| `resp.200.contacts[].account_id` | Account ID | Apollo id of the linked account. | 所关联账户的 Apollo id。 |
| `resp.200.contacts[].present_raw_address` | Raw address | Contact's current free-text address. | 联系人当前的自由文本地址。 |
| `resp.200.contacts[].linkedin_url` | LinkedIn URL | URL of the contact's LinkedIn profile. | 联系人 LinkedIn 主页链接。 |
| `resp.200.contacts[].updated_at` | Updated timestamp | Timestamp when the contact was last updated. | 联系人最近更新时间。 |

## post_apollo_contacts_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Search for contacts. Requires a master API key. | Search your team's contacts by keyword, stage, and label, with sorting and pagination. Requires a master API key. | 按关键词、阶段、标签搜索团队联系人，支持排序与分页。需主 API key。 |
| `req.q_keywords` | Keyword query | Free-text keywords to filter contacts by. | 用于筛选联系人的自由文本关键词。 |
| `req.contact_stage_ids` | Filter by contact stage IDs | Only include contacts in these stages. | 仅纳入处于这些阶段的联系人。 |
| `req.contact_label_ids` | Filter by contact label IDs | Only include contacts carrying these labels. | 仅纳入带有这些标签的联系人。 |
| `req.sort_by_field` | Sort field (e.g. contact_last_activity_date, contact_created_at, contact_updated_at) | Field to sort the results by. | 结果排序所依据的字段。 |
| `req.sort_ascending` | Sort ascending. Default false. | Sort ascending when true, descending when false. | 为 true 时升序，false 时降序。 |
| `req.per_page` | Items per page | Number of results per page. | 每页结果数。 |
| `req.page` | Page number | Page number to retrieve. | 要获取的页码。 |

## post_apollo_contacts_update_stages

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Update contact stage for multiple contacts. Requires a master API key. | Move multiple contacts to a single contact stage at once. Requires a master API key. | 一次把多个联系人移动到同一个联系人阶段。需主 API key。 |
| `param:contact_ids[]` | Contact IDs | Ids of the contacts to move. | 要移动的联系人 id。 |
| `param:contact_stage_id` | New contact stage ID | Id of the stage to move all listed contacts into. | 将所有所列联系人移入的阶段 id。 |
| `resp.200.contacts` | Updated contacts | The contacts whose stage was changed. | 阶段已变更的联系人。 |
| `resp.200.contacts[].id` | Contact ID | Apollo id of the contact. | 联系人的 Apollo id。 |
| `resp.200.contacts[].first_name` | First name | Contact's first name. | 联系人的名字。 |
| `resp.200.contacts[].last_name` | Last name | Contact's last name. | 联系人的姓氏。 |
| `resp.200.contacts[].contact_stage_id` | Contact stage ID | Contact's stage id after the change. | 变更后联系人的阶段 id。 |
| `resp.200.contacts[].owner_id` | Owner ID | Apollo user id of the contact owner. | 联系人负责人的 Apollo 用户 id。 |
| `resp.200.contacts[].email` | Email | Contact's email address. | 联系人的邮箱地址。 |
| `resp.200.contacts[].organization_name` | Organization name | Name of the contact's employer. | 联系人雇主的名称。 |

## post_apollo_contacts_update_owners

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Update contact owner for multiple contacts. Requires a master API key. | Reassign the owner of multiple contacts at once. Requires a master API key. | 一次为多个联系人重新指派负责人。需主 API key。 |
| `param:contact_ids[]` | Contact IDs | Ids of the contacts to reassign. | 要重新指派的联系人 id。 |
| `param:owner_id` | New owner ID | Apollo user id of the new owner for all listed contacts. | 所有所列联系人的新负责人 Apollo 用户 id。 |
| `resp.200.contacts` | Updated contacts | The contacts whose owner was changed. | 负责人已变更的联系人。 |
| `resp.200.contacts[].id` | Contact ID | Apollo id of the contact. | 联系人的 Apollo id。 |
| `resp.200.contacts[].owner_id` | Owner ID | Contact owner's Apollo user id after the change. | 变更后联系人负责人的 Apollo 用户 id。 |
| `resp.200.contacts[].crm_owner_id` | CRM owner ID | Corresponding owner id in the connected CRM, when synced. | 已同步时在所连 CRM 中对应的负责人 id。 |

## get_apollo_contact_stages

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List contact stages. Requires a master API key. | List all contact stages configured for your team. Use the returned ids to set or filter contact_stage_id elsewhere. Requires a master API key. | 列出团队配置的所有联系人阶段。返回的 id 可在别处用于设置或筛选 contact_stage_id。需主 API key。 |
| `resp.200.contact_stages` | Contact stages list | The list of configured contact stages. | 已配置的联系人阶段列表。 |
| `resp.200.contact_stages[].id` | Stage ID | Stage id; use it to set or filter contact_stage_id. | 阶段 id；可用于设置或筛选 contact_stage_id。 |
| `resp.200.contact_stages[].team_id` | Team ID | Id of the team that owns the stage. | 拥有该阶段的团队 id。 |
| `resp.200.contact_stages[].display_name` | Display name | Stage name shown in the Apollo UI. | 在 Apollo 界面中显示的阶段名称。 |
| `resp.200.contact_stages[].name` | Name | Internal name of the stage. | 阶段的内部名称。 |
| `resp.200.contact_stages[].display_order` | Display order | Position of the stage in the ordered pipeline. | 阶段在有序流程中的位置。 |
| `resp.200.contact_stages[].ignore_trigger_override` | Ignore trigger override | Whether automation triggers are ignored when contacts enter this stage. | 联系人进入该阶段时是否忽略自动化触发。 |
| `resp.200.contact_stages[].category` | Category | Category the stage belongs to.<br>[⚠️Note:源码未声明该字段的取值集合，待研发确认。] | 阶段所属的类别。<br>[⚠️批注:源码未声明该字段的取值集合，待研发确认。] |
| `resp.200.contact_stages[].is_meeting_set` | Is meeting set | Whether this stage represents a meeting having been set. | 该阶段是否代表已安排会议。 |

## post_apollo_opportunities

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Create a deal (opportunity). Requires a master API key. | Create a deal (opportunity) tied to an account. Requires a master API key. | 创建商机（deal），并关联到某个账户。需主 API key。 |
| `req.name` | Deal name | Deal name to create. | 要创建的商机名称。 |
| `req.owner_id` | Owner ID | Apollo user id to assign as the deal owner. | 指派为商机负责人的 Apollo 用户 id。 |
| `req.account_id` | Account ID | Apollo id of the account this deal belongs to. | 该商机所属账户的 Apollo id。 |
| `req.amount` | Deal amount | Monetary value of the deal. | 商机的金额。 |
| `req.opportunity_stage_id` | Deal stage ID | Id of the stage to place the deal in. | 将商机置于其中的阶段 id。 |
| `req.closed_date` | Closed date (date string) | Expected or actual close date of the deal. | 商机的预计或实际关闭日期。 |
| `req.typed_custom_fields` | Typed custom fields object | Custom-field values to set, keyed by field id. | 要设置的自定义字段值，以字段 id 为键。 |

## get_apollo_opportunities_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List all deals (opportunities). Requires a master API key. | List all deals (opportunities), with sorting and pagination. Requires a master API key. | 列出全部商机，支持排序与分页。需主 API key。 |
| `param:sort_by_field` | Sort field | Field to sort the deals by. | 商机排序所依据的字段。 |
| `param:page` | Page number | Page number to retrieve. | 要获取的页码。 |
| `param:per_page` | Items per page | Number of results per page. | 每页结果数。 |
| `resp.200.opportunities` | Opportunities list | The page of deals. | 当前页的商机。 |
| `resp.200.opportunities[].id` | Opportunity ID | Apollo id of the deal. | 商机的 Apollo id。 |
| `resp.200.opportunities[].owner_id` | Owner ID | Apollo user id of the deal owner. | 商机负责人的 Apollo 用户 id。 |
| `resp.200.opportunities[].account_id` | Account ID | Apollo id of the account the deal belongs to. | 商机所属账户的 Apollo id。 |
| `resp.200.opportunities[].amount` | Amount | Monetary value of the deal. | 商机的金额。 |
| `resp.200.opportunities[].name` | Name | Deal name. | 商机名称。 |
| `resp.200.opportunities[].opportunity_stage_id` | Stage ID | Id of the deal's current stage. | 商机当前阶段的 id。 |
| `resp.200.opportunities[].is_closed` | Is closed | Whether the deal has been closed (won or lost). | 商机是否已关闭（赢单或输单）。 |
| `resp.200.opportunities[].is_won` | Is won | Whether the deal was won. | 商机是否赢单。 |
| `resp.200.opportunities[].created_at` | Created timestamp | Timestamp when the deal was created. | 商机创建时间。 |
| `resp.200.pagination` | Pagination object | Pagination metadata for the result set. | 结果集的分页元数据。 |
| `resp.200.pagination.page` | Page number | Current page number. | 当前页码。 |
| `resp.200.pagination.per_page` | Items per page | Results per page used. | 所用的每页结果数。 |
| `resp.200.pagination.total_entries` | Total entries | Total number of deals across all pages. | 所有页的商机总数。 |
| `resp.200.pagination.total_pages` | Total pages | Total number of pages. | 总页数。 |

## get_apollo_opportunities_opportunity_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | View a deal (opportunity) by ID. Requires a master API key. | Retrieve a single deal (opportunity) by its id. Requires a master API key. | 按 id 获取单个商机。需主 API key。 |
| `param:opportunity_id` | Opportunity ID | Apollo id of the deal to retrieve. | 要查询的商机 Apollo id。 |
| `resp.200.opportunity` | Opportunity object | The retrieved deal. | 查询到的商机。 |
| `resp.200.opportunity.id` | Opportunity ID | Apollo id of the deal. | 商机的 Apollo id。 |
| `resp.200.opportunity.owner_id` | Owner ID | Apollo user id of the deal owner. | 商机负责人的 Apollo 用户 id。 |
| `resp.200.opportunity.account_id` | Account ID | Apollo id of the account the deal belongs to. | 商机所属账户的 Apollo id。 |
| `resp.200.opportunity.amount` | Amount | Monetary value of the deal. | 商机的金额。 |
| `resp.200.opportunity.name` | Name | Deal name. | 商机名称。 |
| `resp.200.opportunity.opportunity_stage_id` | Stage ID | Id of the deal's current stage. | 商机当前阶段的 id。 |
| `resp.200.opportunity.is_closed` | Is closed | Whether the deal has been closed (won or lost). | 商机是否已关闭（赢单或输单）。 |
| `resp.200.opportunity.is_won` | Is won | Whether the deal was won. | 商机是否赢单。 |
| `resp.200.opportunity.created_at` | Created timestamp | Timestamp when the deal was created. | 商机创建时间。 |

## patch_apollo_opportunities_opportunity_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Update fields on an existing deal (opportunity). Requires a master API key. | Update fields on an existing deal (opportunity). Only the fields you send are changed. Requires a master API key. | 更新已有商机的字段，仅修改你传入的字段。需主 API key。 |
| `param:opportunity_id` | Opportunity ID | Apollo id of the deal to update. | 要更新的商机 Apollo id。 |
| `req.owner_id` | Owner ID | New deal owner's Apollo user id. | 新的商机负责人 Apollo 用户 id。 |
| `req.name` | Opportunity name | New deal name. | 新的商机名称。 |
| `req.amount` | Amount | New monetary value of the deal. | 商机的新金额。 |
| `req.opportunity_stage_id` | Stage ID | New stage id for the deal. | 商机的新阶段 id。 |
| `req.closed_date` | Closed date (date string) | New expected or actual close date. | 新的预计或实际关闭日期。 |
| `req.typed_custom_fields` | Typed custom fields object | Custom-field values to set, keyed by field id. | 要设置的自定义字段值，以字段 id 为键。 |

## get_apollo_opportunity_stages

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List deal stages (opportunity stages). Requires a master API key. | List all deal stages (opportunity stages) configured for your team. Use the returned ids to set or filter opportunity_stage_id elsewhere. Requires a master API key. | 列出团队配置的所有商机阶段。返回的 id 可在别处用于设置或筛选 opportunity_stage_id。需主 API key。 |
| `resp.200.opportunity_stages` | Opportunity stages list | The list of configured deal stages. | 已配置的商机阶段列表。 |
| `resp.200.opportunity_stages[].id` | Stage ID | Stage id; use it to set or filter opportunity_stage_id. | 阶段 id；可用于设置或筛选 opportunity_stage_id。 |
| `resp.200.opportunity_stages[].team_id` | Team ID | Id of the team that owns the stage. | 拥有该阶段的团队 id。 |
| `resp.200.opportunity_stages[].name` | Name | Stage name. | 阶段名称。 |
| `resp.200.opportunity_stages[].display_order` | Display order | Position of the stage in the ordered pipeline. | 阶段在有序流程中的位置。 |
| `resp.200.opportunity_stages[].forecast_category_cd` | Forecast category code | Forecast category this stage rolls up into.<br>[⚠️Note:源码未声明该字段的取值集合，待研发确认。] | 该阶段归入的预测类别。<br>[⚠️批注:源码未声明该字段的取值集合，待研发确认。] |
| `resp.200.opportunity_stages[].is_won` | Is won | Whether reaching this stage means the deal is won. | 到达该阶段是否代表赢单。 |
| `resp.200.opportunity_stages[].is_closed` | Is closed | Whether reaching this stage means the deal is closed. | 到达该阶段是否代表关闭。 |
| `resp.200.opportunity_stages[].probability` | Probability | Win probability associated with this stage. | 与该阶段关联的赢单概率。 |
| `resp.200.opportunity_stages[].description` | Description | Free-text description of the stage. | 阶段的描述。 |
| `resp.200.opportunity_stages[].opportunity_pipeline_id` | Opportunity pipeline ID | Id of the pipeline this stage belongs to. | 该阶段所属流程的 id。 |
| `resp.200.opportunity_stages[].type` | Type | Type of the stage.<br>[⚠️Note:源码未声明该字段的取值集合，待研发确认。] | 阶段的类型。<br>[⚠️批注:源码未声明该字段的取值集合，待研发确认。] |

## post_apollo_emailer_campaigns_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Search for sequences (emailer campaigns) in your Apollo account. Requires a master API key. | Search the sequences (emailer campaigns) in your Apollo account by name, with pagination. Requires a master API key. | 按名称搜索 Apollo 账号中的序列（外联活动），支持分页。需主 API key。 |
| `param:q_name` | Keywords to match sequence names. | Filter sequences by name. | 按名称筛选序列。 |
| `param:page` | Page number. | Page number to retrieve. | 要获取的页码。 |
| `param:per_page` | Results per page. | Number of results per page. | 每页结果数。 |
| `resp.200.emailer_campaigns` | Sequence records (when returned). | The page of matching sequences. | 当前页匹配到的序列。 |
| `resp.200.pagination` | Pagination metadata (when returned). | Pagination metadata for the result set. | 结果集的分页元数据。 |

## post_apollo_emailer_campaigns_sequence_id_add_contact_ids

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Add contacts to a sequence. Requires a master API key. | Add contacts to a sequence by contact ids and/or label names. Several flags let you override safety checks (e.g. allow contacts without email or already active in other sequences). Requires a master API key. | 通过联系人 id 和/或标签名把联系人加入序列。多个开关可覆盖安全校验（如允许无邮箱、或已在其他序列中活跃的联系人）。需主 API key。 |
| `param:sequence_id` | Sequence (emailer campaign) ID. | Id of the sequence to add contacts to. | 要添加联系人的序列 id。 |
| `param:emailer_campaign_id` | Sequence ID (same as sequence_id). | Same sequence id as in the path; provide as a body alias. | 与路径相同的序列 id；作为请求体别名提供。 |
| `param:contact_ids[]` | Contact IDs to add. Provide either contact_ids[] or label_names[] (or both). | Contact ids to add; supply this and/or label_names[]. | 要添加的联系人 id；与 label_names[] 二者可任选其一或同时提供。 |
| `param:label_names[]` | Label names for contacts to add. Provide either label_names[] or contact_ids[] (or both). | Label names whose contacts should be added; supply this and/or contact_ids[]. | 要添加其联系人的标签名；与 contact_ids[] 二者可任选其一或同时提供。 |
| `param:send_email_from_email_account_id` | Email account ID (or IDs) to send from. | Email account id(s) the sequence should send from. | 序列发信所用的邮箱账户 id（可多个）。 |
| `param:send_email_from_email_address` | Optional from-address alias. | Optional from-address alias to send under. | 可选的发件地址别名。 |
| `param:sequence_no_email` | Allow contacts without email. | Allow adding contacts that have no email address. | 允许添加没有邮箱的联系人。 |
| `param:sequence_unverified_email` | Allow contacts with unverified email. | Allow adding contacts whose email is unverified. | 允许添加邮箱未验证的联系人。 |
| `param:sequence_job_change` | Allow contacts with job change. | Allow adding contacts flagged as having changed jobs. | 允许添加被标记为已换工作的联系人。 |
| `param:sequence_active_in_other_campaigns` | Allow contacts active in other sequences. | Allow adding contacts already active in other sequences. | 允许添加已在其他序列中活跃的联系人。 |
| `param:sequence_finished_in_other_campaigns` | Allow contacts finished in other sequences. | Allow adding contacts already finished in other sequences. | 允许添加已在其他序列中结束的联系人。 |
| `resp.200.success` | Whether the add succeeded (when returned). | Whether the contacts were added successfully. | 联系人是否添加成功。 |

## post_apollo_emailer_campaigns_remove_or_stop_contact_ids

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Update contact status in a sequence. Requires a master API key. | Remove or stop contacts in one or more sequences. The mode parameter selects whether to mark as finished, remove, or stop the contacts. Requires a master API key. | 在一个或多个序列中移除或停止联系人。mode 参数决定是标记完成、移除还是停止。需主 API key。 |
| `param:emailer_campaign_ids[]` | Sequence IDs. | Ids of the sequences to act on. | 要操作的序列 id。 |
| `param:contact_ids[]` | Contact IDs. | Ids of the contacts to remove or stop. | 要移除或停止的联系人 id。 |
| `param:mode` | One of: mark_as_finished, remove, stop. | Action to take on the contacts: mark them as finished, remove them, or stop them. | 对联系人采取的动作：标记完成、移除或停止。 |
| `resp.200.success` | Whether the update succeeded (when returned). | Whether the operation succeeded. | 操作是否成功。 |

## post_apollo_emailer_campaigns_sequence_id_approve

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Activate a sequence. Requires a master API key. | Activate a sequence so it starts sending. Requires a master API key. | 激活序列，使其开始发送。需主 API key。 |
| `param:sequence_id` | Sequence ID. | Id of the sequence to act on. | 要操作的序列 id。 |
| `resp.200.emailer_campaign` | Sequence object (when returned). | The activated sequence. | 已激活的序列。 |
| `resp.200.emailer_steps` | Sequence steps (when returned). | The steps of the activated sequence. | 已激活序列的各个步骤。 |

## post_apollo_emailer_campaigns_sequence_id_abort

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Deactivate a sequence. Requires a master API key. | Deactivate a sequence so it stops sending. Requires a master API key. | 停用序列，使其停止发送。需主 API key。 |
| `param:sequence_id` | Sequence ID. | Id of the sequence to act on. | 要操作的序列 id。 |
| `resp.200.emailer_campaign` | Sequence object (when returned). | The deactivated sequence. | 已停用的序列。 |

## post_apollo_emailer_campaigns_sequence_id_archive

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Archive a sequence (marks it inactive and finishes contacts). Requires a master API key. | Archive a sequence: marks it inactive and finishes its contacts. Requires a master API key. | 归档序列：将其标记为非活跃并结束其中的联系人。需主 API key。 |
| `param:sequence_id` | Sequence ID. | Id of the sequence to act on. | 要操作的序列 id。 |
| `resp.200.emailer_campaign` | Archived sequence object (when returned). | The archived sequence. | 已归档的序列。 |

## get_apollo_emailer_messages_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Search for outreach emails. Requires a master API key. | Search outreach emails, filtered by message stats, reply class, user, email account, and sequence. Results are paginated. Requires a master API key. | 搜索外联邮件，可按邮件统计、回复分类、用户、邮箱账户、序列筛选。结果分页。需主 API key。 |
| `param:emailer_message_stats[]` | Filter by message stats (e.g., open, click). | Filter by message engagement stats such as opened or clicked.<br>[⚠️Note:源码未声明完整的取值集合，待研发确认。] | 按邮件互动统计筛选，如已打开、已点击。<br>[⚠️批注:源码未声明完整的取值集合，待研发确认。] |
| `param:emailer_message_reply_classes[]` | Filter by reply classes. | Filter by reply classification, such as positive or out-of-office.<br>[⚠️Note:源码未声明完整的取值集合，待研发确认。] | 按回复分类筛选，如正面、休假自动回复等。<br>[⚠️批注:源码未声明完整的取值集合，待研发确认。] |
| `param:user_ids[]` | Filter by user IDs. | Only include messages sent by these users. | 仅纳入这些用户发出的邮件。 |
| `param:email_account_id_and_aliases` | Filter by email account and aliases. | Filter by a sending email account and its aliases. | 按发件邮箱账户及其别名筛选。 |
| `param:emailer_campaign_ids[]` | Only include these sequence IDs. | Only include messages from these sequences. | 仅纳入来自这些序列的邮件。 |
| `param:not_emailer_campaign_ids[]` | Exclude these sequence IDs. | Exclude messages from these sequences. | 排除来自这些序列的邮件。 |
| `param:page` | Page number. | Page number to retrieve. | 要获取的页码。 |
| `param:per_page` | Results per page. | Number of results per page. | 每页结果数。 |
| `resp.200.emailer_messages` | Outreach emails (when returned). | The page of matching outreach emails. | 当前页匹配到的外联邮件。 |
| `resp.200.pagination` | Pagination metadata (when returned). | Pagination metadata for the result set. | 结果集的分页元数据。 |

## get_apollo_emailer_messages_id_activities

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Check email stats for a specific outreach email. Requires a master API key. | Retrieve the activity log (opens, clicks, replies, etc.) for one outreach email. Requires a master API key. | 获取单封外联邮件的活动记录（打开、点击、回复等）。需主 API key。 |
| `param:id` | Emailer message ID. | Id of the outreach email whose activity you want. | 要查询活动记录的外联邮件 id。 |
| `resp.200.emailer_message` | Email object (when returned). | The outreach email being inspected. | 被查询的外联邮件。 |
| `resp.200.activities` | Activity events (when returned). | Activity events for the email, such as opens, clicks, and replies. | 该邮件的活动事件，如打开、点击、回复。 |

## post_apollo_tasks

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Create a task. Requires a master API key. | Create a single task assigned to a user and linked to a contact. Requires a master API key. | 创建单个任务，指派给某用户并关联到联系人。需主 API key。 |
| `req.user_id` | Task owner user ID. | Apollo user id to assign the task to. | 要指派任务的 Apollo 用户 id。 |
| `req.contact_id` | Contact ID. | Apollo id of the contact the task is about. | 任务针对的联系人 Apollo id。 |
| `req.type` | Task type. | Kind of task, such as a call or an email.<br>[⚠️Note:源码未声明该字段的取值集合，待研发确认。] | 任务类型，如电话或邮件。<br>[⚠️批注:源码未声明该字段的取值集合，待研发确认。] |
| `req.priority` | Task priority (default: medium). | Task priority level.<br>[⚠️Note:源码未声明优先级取值集合，待研发确认。] | 任务优先级。<br>[⚠️批注:源码未声明优先级取值集合，待研发确认。] |
| `req.status` | Task status. | Task status.<br>[⚠️Note:源码未声明状态取值集合，待研发确认。] | 任务状态。<br>[⚠️批注:源码未声明状态取值集合，待研发确认。] |
| `req.due_at` | ISO 8601 due datetime. | When the task is due. | 任务到期时间。 |
| `req.title` | Optional title. | Task title. | 任务标题。 |
| `resp.200.task` | Created task (when returned). | The created task. | 创建的任务。 |

## post_apollo_tasks_bulk_create

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Bulk create tasks. Requires a master API key. | Create one task for each of multiple contacts in a single call. Requires a master API key. | 一次为多个联系人各创建一个任务。需主 API key。 |
| `req.user_id` | Task owner user ID. | Apollo user id to assign all created tasks to. | 要指派所有新建任务的 Apollo 用户 id。 |
| `req.contact_ids` | Contact IDs. | Contact ids to create one task for each. | 为其各创建一个任务的联系人 id。 |
| `req.type` | Task type. | Kind of task applied to every created task.<br>[⚠️Note:源码未声明该字段的取值集合，待研发确认。] | 应用到每个新建任务的任务类型。<br>[⚠️批注:源码未声明该字段的取值集合，待研发确认。] |
| `req.priority` | Task priority (default: medium). | Priority applied to every created task.<br>[⚠️Note:源码未声明优先级取值集合，待研发确认。] | 应用到每个新建任务的优先级。<br>[⚠️批注:源码未声明优先级取值集合，待研发确认。] |
| `req.status` | Task status. | Status applied to every created task.<br>[⚠️Note:源码未声明状态取值集合，待研发确认。] | 应用到每个新建任务的状态。<br>[⚠️批注:源码未声明状态取值集合，待研发确认。] |
| `req.due_at` | ISO 8601 due datetime. | Due time applied to every created task. | 应用到每个新建任务的到期时间。 |
| `req.title` | Optional title. | Title applied to every created task. | 应用到每个新建任务的标题。 |
| `resp.200.tasks` | Created tasks (when returned). | The created tasks. | 创建的任务列表。 |

## post_apollo_tasks_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Search tasks. Requires a master API key. | Search tasks with sorting and pagination. Requires a master API key. | 搜索任务，支持排序与分页。需主 API key。 |
| `param:sort_by_field` | Sort field. | Field to sort the tasks by. | 任务排序所依据的字段。 |
| `param:open_factor_names[]` | Optional open factors. | Optional open-factor names used to refine which tasks are returned.<br>[⚠️Note:源码未声明该字段的取值集合，待研发确认。] | 可选的 open factor 名称，用于进一步限定返回的任务。<br>[⚠️批注:源码未声明该字段的取值集合，待研发确认。] |
| `param:page` | Page number. | Page number to retrieve. | 要获取的页码。 |
| `param:per_page` | Results per page. | Number of results per page. | 每页结果数。 |
| `resp.200.tasks` | Tasks (when returned). | The page of matching tasks. | 当前页匹配到的任务。 |
| `resp.200.pagination` | Pagination metadata (when returned). | Pagination metadata for the result set. | 结果集的分页元数据。 |

## post_apollo_reports_sync_report

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Query analytics report. Requires a master API key. | Run an analytics report synchronously, specifying metrics, grouping dimensions, sorts, filters, and a date range. Requires a master API key. | 同步查询分析报表，指定指标、分组维度、排序、筛选和时间范围。需主 API key。 |
| `req.metrics` | Metrics to compute. | Metrics to compute in the report. | 报表要计算的指标。 |
| `req.group_by` | Dimensions to group by. | Dimensions to group the report rows by. | 报表行所依据的分组维度。 |
| `req.pivot_group_by` | Optional pivot dimensions. | Optional dimensions to pivot the report into columns. | 可选的透视维度，将报表透视为列。 |
| `req.sorts` | Sort specs. | Sort specifications for the report rows. | 报表行的排序规格。 |
| `req.filters` | Filter specs. | Filter specifications limiting which records are included. | 限定纳入哪些记录的筛选规格。 |
| `req.date_range` | Date range filter (when supported). | Date-range filter constraining the report window. | 约束报表时间窗口的日期范围筛选。 |
| `resp.200.report` | Report result (shape depends on request). | The computed report. | 计算得到的报表。 |

## post_apollo_phone_calls

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Create call records. Requires a master API key. | Log one or more phone-call records against a contact and account. Requires a master API key. | 为联系人与账户登记一条或多条通话记录。需主 API key。 |
| `param:logged` | Whether to create an individual record. | Whether to create an individual logged record for the call. | 是否为该通话创建单独的登记记录。 |
| `param:user_id[]` | Caller user IDs. | Apollo user id(s) of the caller(s). | 主叫方的 Apollo 用户 id（可多个）。 |
| `param:contact_id` | Contact ID. | Apollo id of the contact involved in the call. | 参与通话的联系人 Apollo id。 |
| `param:account_id` | Account ID. | Apollo id of the account involved in the call. | 参与通话的账户 Apollo id。 |
| `param:to_number` | Dialed phone number. | Phone number that was dialed. | 被拨打的电话号码。 |
| `param:from_number` | Caller phone number. | Phone number the caller used. | 主叫方使用的电话号码。 |
| `param:status` | Call status. | Outcome status of the call.<br>[⚠️Note:源码未声明状态取值集合，待研发确认。] | 通话的结果状态。<br>[⚠️批注:源码未声明状态取值集合，待研发确认。] |
| `param:start_time` | ISO 8601 start time. | When the call started. | 通话开始时间。 |
| `param:end_time` | ISO 8601 end time. | When the call ended. | 通话结束时间。 |
| `param:duration` | Duration in seconds. | Call length in seconds. | 通话时长，单位为秒。 |
| `param:phone_call_purpose_id` | Purpose ID. | Id of the configured call purpose. | 已配置的通话目的 id。 |
| `param:phone_call_outcome_id` | Outcome ID. | Id of the configured call outcome. | 已配置的通话结果 id。 |
| `resp.200.phone_call` | Call record (when returned). | The created call record. | 创建的通话记录。 |

## get_apollo_phone_calls_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Search calls. Requires a master API key. | Search call records by date range, duration, direction, user, label, purpose, outcome, and keyword. Results are paginated. Requires a master API key. | 按时间范围、时长、呼叫方向、用户、标签、目的、结果、关键词搜索通话记录。结果分页。需主 API key。 |
| `param:date_range[max]` | Upper bound for call date range (YYYY-MM-DD). | Latest call date to include; pair with date_range[min]. | 纳入的最晚通话日期；与 date_range[min] 搭配。 |
| `param:date_range[min]` | Lower bound for call date range (YYYY-MM-DD). | Earliest call date to include; pair with date_range[max]. | 纳入的最早通话日期；与 date_range[max] 搭配。 |
| `param:duration[max]` | Upper bound for duration (seconds). | Maximum call duration in seconds; pair with duration[min]. | 最大通话时长（秒）；与 duration[min] 搭配。 |
| `param:duration[min]` | Lower bound for duration (seconds). | Minimum call duration in seconds; pair with duration[max]. | 最小通话时长（秒）；与 duration[max] 搭配。 |
| `param:inbound` | Inbound or outbound. | Filter to inbound calls when true, outbound when false. | 为 true 时筛选呼入通话，false 时筛选呼出通话。 |
| `param:user_ids[]` | User IDs. | Only include calls by these users. | 仅纳入这些用户的通话。 |
| `param:contact_label_ids[]` | Contact label IDs. | Only include calls with contacts carrying these labels. | 仅纳入联系人带有这些标签的通话。 |
| `param:phone_call_purpose_ids[]` | Purpose IDs. | Only include calls with these purposes. | 仅纳入具有这些目的的通话。 |
| `param:phone_call_outcome_ids[]` | Outcome IDs. | Only include calls with these outcomes. | 仅纳入具有这些结果的通话。 |
| `param:q_keywords` | Keyword filter. | Free-text keywords to filter calls by. | 用于筛选通话的自由文本关键词。 |
| `param:page` | Page number. | Page number to retrieve. | 要获取的页码。 |
| `param:per_page` | Results per page. | Number of results per page. | 每页结果数。 |
| `resp.200.phone_calls` | Calls (when returned). | The page of matching call records. | 当前页匹配到的通话记录。 |
| `resp.200.pagination` | Pagination metadata (when returned). | Pagination metadata for the result set. | 结果集的分页元数据。 |

## put_apollo_phone_calls_id

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Update call records. Requires a master API key. | Update an existing call record identified by id. Requires a master API key. | 按 id 更新已有的通话记录。需主 API key。 |
| `param:id` | Call record ID. | Apollo id of the call record to update. | 要更新的通话记录 Apollo id。 |
| `param:logged` | Whether to create an individual record. | Whether to create an individual logged record for the call. | 是否为该通话创建单独的登记记录。 |
| `param:user_id[]` | Caller user IDs. | Apollo user id(s) of the caller(s). | 主叫方的 Apollo 用户 id（可多个）。 |
| `param:contact_id` | Contact ID. | Apollo id of the contact involved in the call. | 参与通话的联系人 Apollo id。 |
| `param:account_id` | Account ID. | Apollo id of the account involved in the call. | 参与通话的账户 Apollo id。 |
| `param:to_number` | Dialed phone number. | Phone number that was dialed. | 被拨打的电话号码。 |
| `param:from_number` | Caller phone number. | Phone number the caller used. | 主叫方使用的电话号码。 |
| `param:status` | Call status. | Outcome status of the call.<br>[⚠️Note:源码未声明状态取值集合，待研发确认。] | 通话的结果状态。<br>[⚠️批注:源码未声明状态取值集合，待研发确认。] |
| `param:start_time` | ISO 8601 start time. | When the call started. | 通话开始时间。 |
| `param:end_time` | ISO 8601 end time. | When the call ended. | 通话结束时间。 |
| `param:duration` | Duration in seconds. | Call length in seconds. | 通话时长，单位为秒。 |
| `param:phone_call_purpose_id` | Purpose ID. | Id of the configured call purpose. | 已配置的通话目的 id。 |
| `param:phone_call_outcome_id` | Outcome ID. | Id of the configured call outcome. | 已配置的通话结果 id。 |
| `resp.200.phone_call` | Updated call record (when returned). | The updated call record. | 已更新的通话记录。 |

## post_apollo_usage_stats_api_usage_stats

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | View API usage stats and rate limits. Requires a master API key. | Retrieve your API usage statistics and current rate-limit status. Requires a master API key. | 获取你的 API 用量统计和当前限流状态。需主 API key。 |
| `resp.200.api_usage_stats` | Usage stats and rate limits (when returned). | Your API usage statistics and current rate-limit status. | 你的 API 用量统计与当前限流状态。 |

## get_apollo_users_search

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get a list of users. Requires a master API key. | Get a paginated list of users on your team. Use the returned ids to populate owner_id / user_id elsewhere. Requires a master API key. | 分页获取团队用户列表。返回的 id 可用于在别处填写 owner_id / user_id。需主 API key。 |
| `param:page` | Page number. | Page number to retrieve. | 要获取的页码。 |
| `param:per_page` | Results per page. | Number of results per page. | 每页结果数。 |
| `resp.200.users` | Users (when returned). | The page of users. | 当前页的用户。 |
| `resp.200.pagination` | Pagination metadata (when returned). | Pagination metadata for the result set. | 结果集的分页元数据。 |

## get_apollo_email_accounts

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get a list of email accounts. Requires a master API key. | Get the list of email accounts connected for sending. Use the returned ids as send_email_from_email_account_id. Requires a master API key. | 获取已连接用于发信的邮箱账户列表。返回的 id 可作为 send_email_from_email_account_id。需主 API key。 |
| `resp.200.email_accounts` | Email accounts (when returned). | The list of connected sending email accounts. | 已连接用于发信的邮箱账户列表。 |

## get_apollo_labels

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get a list of all lists (labels). Requires a master API key. | Get a list of all lists (labels) in your account. Requires a master API key. | 获取账号中所有列表（标签）。需主 API key。 |
| `resp.200.[]` | List objects (when returned). | The list of label (list) names in your account. | 账号中标签（列表）名称的集合。 |

## get_apollo_typed_custom_fields

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get a list of all custom fields. Requires a master API key. | Get all typed custom fields defined for your team. Requires a master API key. | 获取团队定义的所有带类型自定义字段。需主 API key。 |
| `resp.200.typed_custom_fields` | Custom field definitions (when returned). | The list of typed custom fields defined for your team. | 团队定义的带类型自定义字段列表。 |

## get_apollo_fields

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get a list of fields. Requires a master API key. | Get the list of fields available on your team's records. Requires a master API key. | 获取团队记录上可用的字段列表。需主 API key。 |
| `resp.200.fields` | Field definitions (when returned). | The list of fields available on your records. | 记录上可用的字段列表。 |

## post_apollo_fields

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Create a custom field. Requires a master API key. | Create a custom field on a given entity modality (e.g. contact). Requires a master API key. | 在指定实体类型（如 contact）上创建自定义字段。需主 API key。 |
| `req.label` | Field label. | Display label of the custom field to create. | 要创建的自定义字段的显示标签。 |
| `req.modality` | Entity modality (e.g., contact). | Entity type the field applies to, such as contact or account. | 字段适用的实体类型，如 contact 或 account。 |
| `req.type` | Field type (e.g., textarea). | Data type of the custom field, such as a text area.<br>[⚠️Note:源码未声明完整的类型取值集合，待研发确认。] | 自定义字段的数据类型，如文本域。<br>[⚠️批注:源码未声明完整的类型取值集合，待研发确认。] |
| `req.meta` | Additional field config. | Additional configuration for the field, such as allowed options. | 字段的附加配置，如可选项等。 |
| `resp.200.typed_custom_fields` | Created field(s) (when returned). | The custom fields after the new one is created. | 创建新字段后的自定义字段列表。 |

## get_apollo_notes

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Get a list of notes. Requires a master API key. | Get a list of notes, optionally filtered by the record they are attached to (contact, account, opportunity, calendar event, conversation). Requires a master API key. | 获取备注列表，可按所附记录（联系人、账户、商机、日历事件、会话）筛选。需主 API key。 |
| `param:contact_id` | Filter by a contact ID. | Only include notes attached to this contact. | 仅纳入附在该联系人上的备注。 |
| `param:account_id` | Filter by an account ID. | Only include notes attached to this account. | 仅纳入附在该账户上的备注。 |
| `param:opportunity_id` | Filter by an opportunity ID. | Only include notes attached to this deal. | 仅纳入附在该商机上的备注。 |
| `param:calendar_event_id` | Filter by a calendar event ID. | Only include notes attached to this calendar event. | 仅纳入附在该日历事件上的备注。 |
| `param:conversation_id` | Filter by a conversation ID. | Only include notes attached to this conversation. | 仅纳入附在该会话上的备注。 |
| `param:conversation_ids` | Filter by conversation IDs. | Only include notes attached to these conversations. | 仅纳入附在这些会话上的备注。 |
| `param:contact_ids` | Filter by contact IDs. | Only include notes attached to these contacts. | 仅纳入附在这些联系人上的备注。 |
| `param:start_date` | Only include notes created on/after this date (when supported). | Only include notes created on or after this date, where supported. | 仅纳入在该日期当天或之后创建的备注（在支持时）。 |
| `param:page` | Page number (when supported). | Page number to retrieve. | 要获取的页码。 |
| `param:per_page` | Results per page (when supported). | Number of results per page. | 每页结果数。 |
| `resp.200.notes` | Notes (when returned). | The page of matching notes. | 当前页匹配到的备注。 |
| `resp.200.pagination` | Pagination metadata (when returned). | Pagination metadata for the result set. | 结果集的分页元数据。 |

