> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# People API Search

> Use the People API Search endpoint to find net new people in the Apollo database.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/mixed_people/api_search
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
  /apollo/mixed_people/api_search:
    post:
      summary: People API Search
      description: >-
        Use the People API Search endpoint to find net new people in the Apollo
        database. Several filters are available to help narrow your search. This
        endpoint is optimized for API usage and does not consume credits. This
        endpoint is primarily designed for prospecting net new people. This
        endpoint does not return email addresses or phone numbers. Use the
        People Enrichment or Bulk People Enrichment endpoints to enrich data.
        This endpoint requires a master API key. Refer to Create API Keys to
        learn how to create a master API key. To protect Apollo's performance
        for all users, this endpoint has a display limit of 50,000 records (100
        records per page, up to 500 pages). Add more filters to narrow your
        search results as much as possible. This limitation does not restrict
        your access to Apollo's database; you just need to access the data in
        batches.
      operationId: post_apollo_mixed_people_api_search
      parameters:
        - name: person_titles[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            Job titles held by the people you want to find. For a person to be
            included in search results, they only need to match 1 of the job
            titles you add. Adding more job titles expands your search results.
            Results also include job titles with the same terms, even if they
            are not exact matches. For example, searching for marketing manager
            might return people with the job title content marketing manager.
            Use this parameter in combination with the person_seniorities[]
            parameter to find people based on specific job functions and
            seniority levels. Examples: sales development representative;
            marketing manager; research analyst
        - name: include_similar_titles
          in: query
          required: false
          schema:
            type: boolean
          description: >-
            This parameter determines whether people with job titles similar to
            the titles you define in the person_titles[] parameter are returned
            in the response. Set this parameter to false when using
            person_titles[] to return only strict matches for job titles.
        - name: q_keywords
          in: query
          required: false
          schema:
            type: string
          description: A string of words over which we want to filter the results.
        - name: person_locations[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The location where people live. You can search across cities, US
            states, and countries. To find people based on the headquarters
            locations of their current employer, use the organization_locations
            parameter. Examples: california; ireland; chicago
        - name: person_seniorities[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The job seniority that people hold within their current employer.
            This enables you to find people that currently hold positions at
            certain reporting levels, such as Director level or senior IC level.
            For a person to be included in search results, they only need to
            match 1 of the seniorities you add. Adding more seniorities expands
            your search results. Searches only return results based on their
            current job title, so searching for Director-level employees only
            returns people that currently hold a Director-level title. If
            someone was previously a Director, but is currently a VP, they would
            not be included in your search results. Use this parameter in
            combination with the person_titles[] parameter to find people based
            on specific job functions and seniority levels. The following
            options can be used for this parameter: owner founder c_suite
            partner vp head director manager senior entry intern
        - name: organization_locations[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The location of the company headquarters for a person's current
            employer. You can search across cities, US states, and countries. If
            a company has several office locations, results are still based on
            the headquarters location. For example, if you search chicago but a
            company's HQ location is in boston, people that work for the
            Boston-based company will not appear in your results, even if they
            match other parameters. To find people based on their personal
            location, use the person_locations parameter. Examples: texas;
            tokyo; spain
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
        - name: contact_email_status[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The email statuses for the people you want to find. You can add
            multiple statuses to expand your search. The statuses you can search
            include: verified unverified likely to engage unavailable
        - name: organization_ids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The Apollo IDs for the companies (employers) you want to include in
            your search results. Each company in the Apollo database is assigned
            a unique ID. To find IDs, call the Organization Search endpoint and
            identify the values for organization_id. Example:
            5e66b6381e05b4008c8331b8
        - name: organization_num_employees_ranges[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The number range of employees working for the person's current
            company. This enables you to find people based on the headcount of
            their employer. You can add multiple ranges to expand your search
            results. Each range you add needs to be a string, with the upper and
            lower numbers of the range separated only by a comma. Examples:
            1,10; 250,500; 10000,20000
        - name: revenue_range[min]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The minimum revenue the person's current employer generates. Use
            this parameter in combination with revenue_range[max] to set a
            revenue range. Do not enter currency symbols, commas, or decimal
            points in the figure. Examples: 500000; 1500000
        - name: revenue_range[max]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The maximum revenue the person's current employer generates. Use
            this parameter in combination with revenue_range[min] to set a
            revenue range. Do not enter currency symbols, commas, or decimal
            points in the figure. Examples: 500000; 1500000
        - name: currently_using_all_of_technology_uids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            Find people based on all of the technologies their current employer
            uses. Apollo supports filtering by 1,500+ technologies. Apollo
            calculates technologies data from multiple sources. This data is
            updated regularly. Check out the full list of supported technologies
            by downloading this CSV file . Use underscores (_) to replace spaces
            and periods for the technologies listed in the CSV file. Examples:
            salesforce; google_analytics; wordpress_org
        - name: currently_using_any_of_technology_uids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            Find people based on any of the technologies their current employer
            uses. Apollo supports filtering by 1,500+ technologies. Apollo
            calculates technologies data from multiple sources. This data is
            updated regularly. Check out the full list of supported technologies
            by downloading this CSV file . Use underscores (_) to replace spaces
            and periods for the technologies listed in the CSV file. Examples:
            salesforce; google_analytics; wordpress_org
        - name: currently_not_using_any_of_technology_uids[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            Exclude people from your search based on any of the technologies
            their current employer uses. Apollo supports filtering by 1,500+
            technologies. Apollo calculates technologies data from multiple
            sources. This data is updated regularly. Check out the full list of
            supported technologies by downloading this CSV file . Use
            underscores (_) to replace spaces and periods for the technologies
            listed in the CSV file. Examples: salesforce; google_analytics;
            wordpress_org
        - name: q_organization_job_titles[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The job titles that are listed in active job postings at the
            person's current employer. Examples: sales manager; research analyst
        - name: organization_job_locations[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            The locations of the jobs being actively recruited by the person's
            employer. Examples: atlanta; japan
        - name: organization_num_jobs_range[min]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The minimum number of job postings active at the person's current
            employer. Use this parameter in combination with
            organization_num_jobs_range[max] to set a job postings range.
            Examples: 50; 500
        - name: organization_num_jobs_range[max]
          in: query
          required: false
          schema:
            type: integer
          description: >-
            The maximum number of job postings active at the person's current
            employer. Use this parameter in combination with
            organization_num_jobs_range[min] to set a job postings range.
            Examples: 50; 500
        - name: organization_job_posted_at_range[min]
          in: query
          required: false
          schema:
            type: string
          description: >-
            The earliest date when jobs were posted by the person's current
            employer. Use this parameter in combination with
            organization_job_posted_at_range[max] to set a date range for when
            jobs posted. Example: 2025-07-25
        - name: organization_job_posted_at_range[max]
          in: query
          required: false
          schema:
            type: string
          description: >-
            The latest date when jobs were posted by the person's current
            employer. Use this parameter in combination with
            organization_job_posted_at_range[min] to set a date range for when
            jobs posted. Example: 2025-09-25
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
                  total_entries:
                    type: integer
                    description: Response field
                  people:
                    type: array
                    items:
                      type: string
                    description: Response array
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