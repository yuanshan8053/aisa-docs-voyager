> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# News Articles Search

> Use the News Articles Search endpoint to find news articles related to companies in the Apollo database.



## OpenAPI

````yaml openapi/apollo.json POST /apollo/news_articles/search
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
  /apollo/news_articles/search:
    post:
      summary: News Articles Search
      description: >-
        Use the News Articles Search endpoint to find news articles related to
        companies in the Apollo database. Several filters are available to help
        narrow your search. Calling this endpoint does consume credits as part
        of your Apollo pricing plan .
      operationId: post_apollo_news_articles_search
      parameters:
        - name: organization_ids[]
          in: query
          required: true
          schema:
            type: array
            items:
              type: string
          description: >-
            The Apollo IDs for the companies you want to include in your search
            results. Each company in the Apollo database is assigned a unique
            ID. To find IDs, call the Organization Search endpoint and identify
            the values for organization_id. Example: 5e66b6381e05b4008c8331b8
        - name: categories[]
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
          description: >-
            Filter your search to include only certain categories or
            sub-categories of news. Use the News search filter for companies
            within Apollo to uncover all possible categories and sub-categories.
            Examples: hires; investment; contract
        - name: published_at[min]
          in: query
          required: false
          schema:
            type: string
          description: >-
            Set the lower bound of the date range you want to search. Use this
            parameter in combination with the published_at[max] parameter. This
            date should fall before the published_at[max] date. The date should
            be formatted as YYYY-MM-DD. Example: 2025-02-15
        - name: published_at[max]
          in: query
          required: false
          schema:
            type: string
          description: >-
            Set the upper bound of the date range you want to search. Use this
            parameter in combination with the published_at[min] parameter. This
            date should fall after the published_at[min] date. The date should
            be formatted as YYYY-MM-DD. Example: 2025-05-15
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
                  pagination:
                    type: object
                    description: Response object
                  news_articles:
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