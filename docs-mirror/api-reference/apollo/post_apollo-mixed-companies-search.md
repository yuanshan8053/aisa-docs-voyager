> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organization Search

> Use the Organization Search endpoint to find companies in the Apollo database.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/mixed_companies/search
openapi: 3.0.3
info:
  title: Apollo API
  version: 1.0.0
  description: Apollo API endpoints exposed through the AIsa unified gateway.
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - BearerAuth: []
paths:
  /apollo/mixed_companies/search:
    post:
      summary: Organization Search
      description: >-
        Use the Organization Search endpoint to find companies in the Apollo
        database. Several filters are available to help narrow your search.
        Calling this endpoint does consume credits as part of your Apollo
        pricing plan . To protect Apollo's performance for all users, this
        endpoint has a display limit of 50,000 records (100 records per page, up
        to 500 pages). Add more filters to narrow your search results as much as
        possible. This limitation does not restrict your access to Apollo's
        database; you just need to access the data in batches.
      operationId: post_apollo_mixed_companies_search
      parameters:
        - name: q_organization_domains_list[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The domain name for the person's employer. This can be the current
            employer or a previous employer. Do not include www., the @ symbol,
            or similar. This parameter accepts up to 1,000 domains in a single
            request. Examples: apollo.io; microsoft.com
        - name: organization_num_employees_ranges[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The number range of employees working for the company. This enables
            you to find companies based on headcount. You can add multiple
            ranges to expand your search results. Each range you add needs to be
            a string, with the upper and lower numbers of the range separated
            only by a comma. Examples: 1,10; 250,500; 10000,20000
        - name: organization_locations[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The location of the company headquarters. You can search across
            cities, US states, and countries. If a company has several office
            locations, results are still based on the headquarters location. For
            example, if you search chicago but a company's HQ location is in
            boston, any Boston-based companies will not appearch in your search
            results, even if they match other parameters.. To exclude companies
            based on location, use the organization_not_locations parameter.
            Examples: texas; tokyo; spain
        - name: organization_not_locations[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            Exclude companies from search results based on the location of the
            company headquarters. You can use cities, US states, and countries
            as locations to exclude. This parameter is useful for ensuring you
            do not prospect in an undesirable territory. For example, if you use
            ireland as a value, no Ireland-based companies will appear in your
            search results. Examples: minnesota; ireland; seoul
        - name: revenue_range[min]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            Search for organizations based on their revenue. Use this parameter
            to set the lower range of organization revenue. Use the
            revenue_range[max] parameter to set the upper range of revenue. Do
            not enter currency symbols, commas, or decimal points in the figure.
            Example: 300000
        - name: revenue_range[max]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            Search for organizations based on their revenue. Use this parameter
            to set the upper range of organization revenue. Use the
            revenue_range[min] parameter to set the lower range of revenue. Do
            not enter currency symbols, commas, or decimal points in the figure.
            Example: 50000000
        - name: currently_using_any_of_technology_uids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            Find organizations based on the technologies they currently use.
            Apollo supports filtering by 1,500+ technologies. Apollo calculates
            technologies data from multiple sources. This data is updated
            regularly. Check out the full list of supported technologies by
            downloading this CSV file . Use underscores (_) to replace spaces
            and periods for the technologies listed in the CSV file. Examples:
            salesforce; google_analytics; wordpress_org
        - name: q_organization_keyword_tags[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            Filter search results based on keywords associated with companies.
            For example, you can enter mining as a value to return only
            companies that have an association with the mining industry.
            Examples: mining; sales strategy; consulting
        - name: q_organization_name
          in: query
          required: false
          schema:
            type: string
          description: >-
            Filter search results to include a specific company name. If the
            value you enter for this parameter does not match with a company's
            name, the company will not appear in search results, even if it
            matches other parameters. Partial matches are accepted. For example,
            if you filter by the value marketing, a company called NY Marketing
            Unlimited would still be eligible as a search result, but NY Market
            Analysis would not be eligible. Example: apollo or mining
        - name: organization_ids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The Apollo IDs for the companies you want to include in your search
            results. Each company in the Apollo database is assigned a unique
            ID. To find IDs, identify the values for organization_id when you
            call this endpoint. Example: 5e66b6381e05b4008c8331b8
        - name: latest_funding_amount_range[min]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The minimum amount the company received with its most recent funding
            round. Use this parameter in combination with
            latest_funding_amount_range[max] to set a monetary range for the
            company's most recent funding round. Do not enter currency symbols,
            commas, or decimal points in the figure. Examples: 5000000; 15000000
        - name: latest_funding_amount_range[max]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The maximium amount the company received with its most recent
            funding round. Use this parameter in combination with
            latest_funding_amount_range[min] to set a monetary range for the
            company's most recent funding round. Do not enter currency symbols,
            commas, or decimal points in the figure. Examples: 5000000; 15000000
        - name: total_funding_range[min]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The minimum amount the company received during all of its funding
            rounds combined. Use this parameter in combination with
            total_funding_range[max] to set a monetary range for all of the
            company's funding rounds. Do not enter currency symbols, commas, or
            decimal points in the figure. Examples: 50000000; 350000000
        - name: total_funding_range[max]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The maximum amount the company received during all of its funding
            rounds combined. Use this parameter in combination with
            total_funding_range[min] to set a monetary range for all of the
            company's funding rounds. Do not enter currency symbols, commas, or
            decimal points in the figure. Examples: 50000000; 350000000
        - name: latest_funding_date_range[min]
          in: query
          required: false
          schema:
            type: string
          description: >-
            The earliest date when the company received its most recent funding
            round. Use this parameter in combination with
            latest_funding_date_range[max] to set a date range for when the
            company received its most recent funding round. Example: 2025-07-25
        - name: latest_funding_date_range[max]
          in: query
          required: false
          schema:
            type: string
          description: >-
            The latest date when the company received its most recent funding
            round. Use this parameter in combination with
            latest_funding_date_range[min] to set a date range for when the
            company received its most recent funding round. Example: 2025-09-25
        - name: q_organization_job_titles[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The job titles that are listed in active job postings at the
            company. Examples: sales manager; research analyst
        - name: organization_job_locations[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The locations of the jobs being actively recruited by the company.
            Examples: atlanta; japan
        - name: organization_num_jobs_range[min]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The minimum number of job postings active at the company. Use this
            parameter in combination with organization_num_jobs_range[max] to
            set a job postings range. Examples: 50; 500
        - name: organization_num_jobs_range[max]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The maximum number of job postings active at the company. Use this
            parameter in combination with organization_num_jobs_range[min] to
            set a job postings range. Examples: 50; 500
        - name: organization_job_posted_at_range[min]
          in: query
          required: false
          schema:
            type: string
          description: >-
            The earliest date when jobs were posted by the company. Use this
            parameter in combination with organization_job_posted_at_range[max]
            to set a date range for when jobs posted. Example: 2025-07-25
        - name: organization_job_posted_at_range[max]
          in: query
          required: false
          schema:
            type: string
          description: >-
            The latest date when jobs were posted by the company. Use this
            parameter in combination with organization_job_posted_at_range[min]
            to set a date range for when jobs posted. Example: 2025-09-25
        - name: page
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The page number of the Apollo data that you want to retrieve. Use
            this parameter in combination with the per_page parameter to make
            search results for navigable and improve the performance of the
            endpoint. Example: 4
        - name: per_page
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The number of search results that should be returned for each page.
            Limiting the number of results per page improves the endpoint's
            performance. Use the page parameter to search the different pages of
            data. Example: 10
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  breadcrumbs:
                    type: array
                    items:
                      type: string
                    description: Response array
                  partial_results_only:
                    type: boolean
                    description: Response field
                  has_join:
                    type: boolean
                    description: Response field
                  disable_eu_prospecting:
                    type: boolean
                    description: Response field
                  partial_results_limit:
                    type: integer
                    description: Response field
                  pagination:
                    type: object
                    description: Response object
                  accounts:
                    type: array
                    items:
                      type: string
                    description: Response array
                  organizations:
                    type: array
                    items:
                      type: string
                    description: Response array
                  model_ids:
                    type: array
                    items:
                      type: string
                    description: Response array
                  num_fetch_result:
                    type: string
                    description: Response field
                  derived_params:
                    type: string
                    description: Response field
        '400':
          description: Bad request
        '401':
          description: Unauthorized
        '429':
          description: Rate limit exceeded
        '500':
          description: Internal server error
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer

````