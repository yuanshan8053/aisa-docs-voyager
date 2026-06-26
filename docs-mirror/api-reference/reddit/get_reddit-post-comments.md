> ## Documentation Index
> Fetch the complete documentation index at: https://aisa.one/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Post Comments

> Post Comments

Fetch the comment tree of a single Reddit post. Pass the full post URL.

## Example

```bash theme={null}
curl "https://api.aisa.one/apis/v1/reddit/post/comments?url=VALUE" \
  -H "Authorization: Bearer YOUR_API_KEY"
```


## OpenAPI

````yaml openapi/reddit.json GET /reddit/post/comments
openapi: 3.0.0
info:
  title: Reddit API
  description: >-
    Read public Reddit data — search posts, browse subreddits, and fetch
    comments.
  version: 1.0.0
servers:
  - url: https://api.aisa.one/apis/v1
security:
  - bearerAuth: []
paths:
  /reddit/post/comments:
    get:
      tags:
        - Reddit API
      summary: Post Comments
      description: >-
        Retrieves comments and post details from a Reddit post by URL. Returns
        the post with title, author, score, ups, upvote_ratio, num_comments, and
        created_utc, plus a comments array where each comment includes author,
        body, body_html, score, created_utc, parent_id, permalink, and nested
        replies. Supports cursor-based pagination for loading more comments and
        a trim parameter for lighter responses.
      operationId: get_reddit-post-comments
      parameters:
        - name: url
          in: query
          required: true
          description: Reddit post URL
          schema:
            type: string
          example: >-
            https://www.reddit.com/r/AskReddit/comments/ablzuq/people_who_havent_pooped_in_2019_yet_why_are_you/
        - name: cursor
          in: query
          required: false
          description: Cursor to get more comments, or replies.
          schema:
            type: string
          example: ed1lvsa,ed3fnpq,ed25l2w
        - name: trim
          in: query
          required: false
          description: Set to true for a trimmed down version of the response
          schema:
            type: boolean
          example: 'false'
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              example:
                comments:
                  - id: mymupxb
                    author: Background-Emu-2890
                    author_fullname: t2_efdlposp6
                    body: Black cat i have one and i love her so much !
                    name: t1_mymupxb
                    created_utc: 1750342221
                    created_at_iso: '2025-06-19T14:10:21.000Z'
                    parent_id: t3_1lfbo7u
                    url: >-
                      https://www.reddit.com/r/AskReddit/comments/1lfbo7u/what_is_a_thing_you_love_that_lots_of_people_hate/mymupxb/
                    replies:
                      items:
                        - url: >-
                            https://www.reddit.com/r/AskReddit/comments/1lfbo7u/what_is_a_thing_you_love_that_lots_of_people_hate/mymxwde/
                          created_utc: 1750343166
                          created_at_iso: '2025-06-19T14:26:06.000Z'
                          subreddit_id: t5_2qh1i
                          approved_at_utc: null
                          author_is_blocked: false
                          comment_type: null
                          awarders: []
                          mod_reason_by: null
                          banned_by: null
                          author_flair_type: text
                          total_awards_received: 0
                          subreddit: AskReddit
                          author_flair_template_id: null
                          likes: null
                          replies:
                            items: []
                            more:
                              has_more: false
                              next_cursor: null
                          user_reports: []
                          saved: false
                          id: mymxwde
                          banned_at_utc: null
                          mod_reason_title: null
                          gilded: 0
                          archived: false
                          collapsed_reason_code: null
                          no_follow: false
                          author: doublestitch
                          can_mod_post: false
                          send_replies: true
                          parent_id: t1_mymupxb
                          score: 19
                          author_fullname: t2_10py0g
                          removal_reason: null
                          approved_by: null
                          mod_note: null
                          all_awardings: []
                          body: House panthers for the win
                          edited: false
                          top_awarded_type: null
                          author_flair_css_class: null
                          name: t1_mymxwde
                          is_submitter: false
                          downs: 0
                          author_flair_richtext: []
                          author_patreon_flair: false
                          body_html: >-
                            &lt;div class="md"&gt;&lt;p&gt;House panthers for
                            the win&lt;/p&gt;

                            &lt;/div&gt;
                          gildings: {}
                          collapsed_reason: null
                          distinguished: null
                          associated_award: null
                          stickied: false
                          author_premium: false
                          can_gild: false
                          link_id: t3_1lfbo7u
                          unrepliable_reason: null
                          author_flair_text_color: null
                          score_hidden: false
                          permalink: >-
                            /r/AskReddit/comments/1lfbo7u/what_is_a_thing_you_love_that_lots_of_people_hate/mymxwde/
                          subreddit_type: public
                          locked: false
                          report_reasons: null
                          created: 1750343166
                          author_flair_text: null
                          treatment_tags: []
                          collapsed: false
                          subreddit_name_prefixed: r/AskReddit
                          controversiality: 0
                          depth: 1
                          author_flair_background_color: null
                          collapsed_because_crowd_control: null
                          mod_reports: []
                          num_reports: null
                          ups: 19
                      more:
                        has_more: true
                        cursor: myn970w
                    ups: 75
                    downs: 0
                    score: 75
                post:
                  id: 1lfbo7u
                  author: Vetro_Nodulare2
                  author_fullname: t2_16syu27ar1
                  subreddit: AskReddit
                  title: What is a thing you love that lots of people hate?
                  downs: 0
                  name: t3_1lfbo7u
                  upvote_ratio: 0.91
                  ups: 47
                  total_awards_received: 0
                  score: 47
                  created: 1750341959
                  num_comments: 353
                  url: >-
                    https://www.reddit.com/r/AskReddit/comments/1lfbo7u/what_is_a_thing_you_love_that_lots_of_people_hate/
                  subreddit_subscribers: 56146601
                  is_video: false
                  created_utc: 1750341959
                more:
                  has_more: true
                  cursor: myoaw2m,myob40l,myoeo9h
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: AIsa API key. Get yours at https://aisa.one

````