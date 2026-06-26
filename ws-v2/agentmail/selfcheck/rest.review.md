# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 13 个接口，260 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## get

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail threads get --thread-id <thread_id><br>``` | Fetch a single resource by its ID. This operationId is shared by three endpoints: get a thread (with its full message list) by `thread_id`, get a draft by `draft_id`, and get one allow/block list entry by `direction`/`type`/`entry`. The path determines which resource and response shape you receive. | 按 ID 获取单个资源。该 operationId 由三个端点共用：按 `thread_id` 获取对话（含完整消息列表）、按 `draft_id` 获取草稿、按 `direction`/`type`/`entry` 获取单条允许/拦截名单条目。具体取哪种资源及返回结构由请求路径决定。 |
| `param:thread_id` |  | ID of the thread to fetch. Obtain it from the `thread_id` field of a list-threads result or a send/reply response. | 要获取的对话 ID。可从列出对话的结果或发送/回复响应的 `thread_id` 字段获得。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret; never log it in plaintext. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密，切勿明文记录。 |
| `resp.200.inbox_id` |  | ID of the inbox that owns this resource. | 拥有该资源的收件箱 ID。 |
| `resp.200.thread_id` |  | ID of the thread, usable as the path parameter for thread operations. | 对话 ID，可用作对话相关操作的路径参数。 |
| `resp.200.labels` |  | Labels currently applied, including both system labels and your custom labels. | 当前应用的标签，含系统标签与自定义标签。 |
| `resp.200.timestamp` |  | When the last message was sent or received in the thread. | 对话中最近一次发送或接收消息的时间。 |
| `resp.200.received_timestamp` |  | When the last message was received in the thread. | 对话中最近一次接收消息的时间。 |
| `resp.200.sent_timestamp` |  | When the last message was sent in the thread. | 对话中最近一次发送消息的时间。 |
| `resp.200.senders` |  | Distinct sender addresses appearing in the thread. | 对话中出现过的不同发件人地址。 |
| `resp.200.recipients` |  | Distinct recipient addresses appearing in the thread. | 对话中出现过的不同收件人地址。 |
| `resp.200.subject` |  | Subject line. | 主题。 |
| `resp.200.preview` |  | Short plain-text snippet of the content, for list-style display. | 内容的纯文本短摘要，用于列表展示。 |
| `resp.200.attachments` |  | Attachments belonging to this resource. | 该资源包含的附件。 |
| `resp.200.attachments.attachment_id` |  | ID of the attachment, used as the path parameter for the get-attachment endpoint. | 附件 ID，作为获取附件端点的路径参数。 |
| `resp.200.attachments.filename` |  | Original filename of the attachment. | 附件的原始文件名。 |
| `resp.200.attachments.size` |  | Attachment size in bytes. | 附件大小（字节）。 |
| `resp.200.attachments.content_type` |  | MIME content type of the attachment (e.g. `application/pdf`). | 附件的 MIME 内容类型（如 `application/pdf`）。 |
| `resp.200.attachments.content_disposition` |  | How the attachment is presented: `inline` (rendered within the body, e.g. an embedded image) or `attachment` (a downloadable file). | 附件呈现方式：`inline`（随正文内嵌，如内嵌图片）或 `attachment`（可下载的文件）。 |
| `resp.200.attachments.content_id` |  | Content-ID used to reference an inline attachment from within the HTML body (via `cid:`). | Content-ID，用于在 HTML 正文中以 `cid:` 引用内嵌附件。 |
| `resp.200.last_message_id` |  | ID of the most recent message in the thread. | 对话中最新一条消息的 ID。 |
| `resp.200.message_count` |  | Number of messages in the thread. | 对话中的消息数量。 |
| `resp.200.size` |  | Total size of the thread in bytes. | 对话的总大小（字节）。 |
| `resp.200.updated_at` |  | When the resource was last updated. | 资源最后更新时间。 |
| `resp.200.created_at` |  | When the resource was created. | 资源创建时间。 |
| `resp.200.messages` | Messages in thread. Ordered by `timestamp` ascending. | Full messages of the thread in chronological order, each with bodies and attachments. | 对话内的完整消息，按时间先后排列，每条含正文与附件。 |
| `resp.200.messages.inbox_id` |  | ID of the inbox that owns this message. | 拥有该消息的收件箱 ID。 |
| `resp.200.messages.thread_id` |  | ID of the thread this message belongs to. | 该消息所属的对话 ID。 |
| `resp.200.messages.message_id` |  | ID of the message. | 消息 ID。 |
| `resp.200.messages.labels` |  | Labels applied to this message. | 应用于该消息的标签。 |
| `resp.200.messages.timestamp` |  | When the message was sent or drafted. | 消息发送或起草的时间。 |
| `resp.200.messages.from` |  | Sender address of the message. | 消息发件人地址。 |
| `resp.200.messages.reply_to` | Reply-to addresses. In format `username@domain.com` or `Display Name <username@domain.com>`. | Reply-To addresses for this message. | 该消息的回复目标地址。 |
| `resp.200.messages.to` |  | Primary recipient addresses of the message. | 消息的主要收件人地址。 |
| `resp.200.messages.cc` |  | CC recipient addresses of the message. | 消息的抄送收件人地址。 |
| `resp.200.messages.bcc` |  | BCC recipient addresses of the message. | 消息的密送收件人地址。 |
| `resp.200.messages.subject` |  | Subject of the message. | 消息主题。 |
| `resp.200.messages.preview` |  | Short plain-text snippet of the message. | 消息的纯文本短摘要。 |
| `resp.200.messages.text` |  | Plain-text body of the message, including any quoted history. | 消息的纯文本正文，含引用的历史内容。 |
| `resp.200.messages.html` |  | HTML body of the message, including any quoted history. | 消息的 HTML 正文，含引用的历史内容。 |
| `resp.200.messages.extracted_text` | Extracted new text content. | Just the newly written plain text of the message, with quoted reply history stripped out. | 仅该消息新写入的纯文本，已剔除引用的回复历史。 |
| `resp.200.messages.extracted_html` | Extracted new HTML content. | Just the newly written HTML of the message, with quoted reply history stripped out. | 仅该消息新写入的 HTML，已剔除引用的回复历史。 |
| `resp.200.messages.attachments` |  | Attachments of this message. | 该消息的附件。 |
| `resp.200.messages.attachments.attachment_id` |  | ID of the attachment, used as the path parameter for the get-attachment endpoint. | 附件 ID，作为获取附件端点的路径参数。 |
| `resp.200.messages.attachments.filename` |  | Original filename of the attachment. | 附件的原始文件名。 |
| `resp.200.messages.attachments.size` |  | Attachment size in bytes. | 附件大小（字节）。 |
| `resp.200.messages.attachments.content_type` |  | MIME content type of the attachment (e.g. `application/pdf`). | 附件的 MIME 内容类型（如 `application/pdf`）。 |
| `resp.200.messages.attachments.content_disposition` |  | How the attachment is presented: `inline` (rendered within the body, e.g. an embedded image) or `attachment` (a downloadable file). | 附件呈现方式：`inline`（随正文内嵌，如内嵌图片）或 `attachment`（可下载的文件）。 |
| `resp.200.messages.attachments.content_id` |  | Content-ID used to reference an inline attachment from within the HTML body (via `cid:`). | Content-ID，用于在 HTML 正文中以 `cid:` 引用内嵌附件。 |
| `resp.200.messages.in_reply_to` |  | ID of the message this one replies to. | 该消息所回复的目标消息 ID。 |
| `resp.200.messages.references` |  | IDs of earlier messages in the thread, forming the reply chain. | 对话中较早消息的 ID，构成回复链。 |
| `resp.200.messages.headers` |  | Raw email headers of the message as key-value pairs. | 消息的原始邮件头，以键值对表示。 |
| `resp.200.messages.size` |  | Message size in bytes. | 消息大小（字节）。 |
| `resp.200.messages.updated_at` |  | When the message was last updated. | 消息最后更新时间。 |
| `resp.200.messages.created_at` |  | When the message was created. | 消息创建时间。 |
| `resp.404.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.404.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |

## delete

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Moves the thread to trash by adding a trash label to all messages. If the thread is already in trash, it will be permanently deleted. Use `permanent=true` to force permanent deletion.<br><br>**CLI:**<br>```bash<br>agentmail threads delete --thread-id <thread_id><br>``` | Delete a resource by its ID. Shared by two endpoints: delete a thread (moves it to trash, or permanently removes it when already trashed or when `permanent=true`) and delete one allow/block list entry. Read-only system entries cannot be deleted. | 按 ID 删除资源。由两个端点共用：删除对话（移入回收站；若已在回收站或 `permanent=true` 则永久删除）、删除单条允许/拦截名单条目。只读的系统条目无法删除。 |
| `param:thread_id` |  | ID of the thread to delete (trash, or permanently delete if already trashed or `permanent=true`). | 要删除的对话 ID（移入回收站；若已在回收站或 `permanent=true` 则永久删除）。 |
| `param:permanent` | If true, permanently delete the thread instead of moving to trash. | When true, permanently delete the thread immediately instead of moving it to trash. | 为 true 时立即永久删除对话，而非移入回收站。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密。 |
| `resp.404.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.404.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |

## update

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Updates thread labels. Cannot add or remove system labels (sent, received, bounced, etc.). Rejects requests with a `422` for threads with 100 or more messages. | Update a thread's labels by adding and/or removing custom labels. System labels (sent, received, bounced, etc.) cannot be changed, and threads with 100 or more messages are rejected with 422. | 更新对话标签：增加和/或移除自定义标签。系统标签（sent、received、bounced 等）不可改动；消息数达 100 条及以上的对话会以 422 拒绝。 |
| `param:thread_id` |  | ID of the thread whose labels are being updated. | 要更新标签的对话 ID。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密。 |
| `req.add_labels` | Labels to add to thread. Cannot be system labels. | Custom labels to apply to the thread. System labels are not allowed. | 要为对话添加的自定义标签。不允许使用系统标签。 |
| `req.remove_labels` | Labels to remove from thread. Cannot be system labels. Takes priority over `add_labels` (in the event of duplicate labels passed in). | Custom labels to remove from the thread. System labels are not allowed. If the same label appears in both lists, removal wins. | 要从对话移除的自定义标签。不允许使用系统标签。若同一标签同时出现在两个列表，以移除为准。 |
| `resp.200.thread_id` |  | ID of the updated thread. | 已更新对话的 ID。 |
| `resp.200.labels` |  | The thread's complete label set after the update. | 更新后对话的完整标签集合。 |
| `resp.400.name` |  | Machine-readable error name identifying the validation failure. | 标识本次校验失败的机器可读错误名。 |
| `resp.400.errors` | Validation errors. | Details of the validation problems with the query parameters. | 查询参数校验问题的明细。 |
| `resp.404.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.404.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |
| `resp.422.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.422.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |

## list

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail lists list --direction <direction> --type <type><br>``` | List resources with cursor pagination. This operationId is shared by three endpoints: list threads, list drafts, and list allow/block list entries. Supports time/label filters where applicable; iterate with `next_page_token` to walk all pages. | 分页列出资源（基于游标）。该 operationId 由三个端点共用：列出对话、列出草稿、列出允许/拦截名单条目。在适用处支持时间与标签筛选；通过 `next_page_token` 翻页可遍历全部结果。 |
| `param:direction` |  | Traffic direction of the list to read: `send`, `receive`, or `reply`. (List-entries endpoint only.) | 要读取的名单流量方向：`send`、`receive` 或 `reply`。（仅名单条目端点） |
| `param:type` |  | Whether to read the `allow` or `block` list. (List-entries endpoint only.) | 读取 `allow` 还是 `block` 名单。（仅名单条目端点） |
| `param:limit` |  | Maximum number of items to return in this page. | 本页返回的最大条目数。 |
| `param:page_token` |  | Pagination cursor. Pass the `next_page_token` from the previous response to fetch the next page; omit for the first page. | 分页游标。传入上一次响应的 `next_page_token` 以取下一页；首页可不传。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密。 |
| `resp.200.count` |  | Number of items returned in this page. | 本页返回的条目数。 |
| `resp.200.limit` |  | The limit that was applied to this page. | 本页实际生效的数量上限。 |
| `resp.200.next_page_token` |  | Cursor for the next page; pass it back as `page_token`. Absent or empty when there are no more pages. | 下一页的游标；作为 `page_token` 回传。无更多页时缺省或为空。 |
| `resp.200.entries` | Ordered by entry ascending. | The page of allow/block list entries, ordered by entry ascending. | 本页允许/拦截名单条目，按条目升序排列。 |
| `resp.200.entries.entry` | Email address or domain of list entry. | The email address or domain of the list entry. | 名单条目的邮箱地址或域名。 |
| `resp.200.entries.organization_id` |  | ID of the organization the list entry belongs to. | 名单条目所属的组织 ID。 |
| `resp.200.entries.reason` | Reason for adding the entry. | Free-text reason recorded when the entry was added. | 添加该条目时记录的自由文本原因。 |
| `resp.200.entries.direction` |  | Traffic direction the entry governs: `send`, `receive`, or `reply`. | 条目作用的流量方向：`send`、`receive` 或 `reply`。 |
| `resp.200.entries.list_type` |  | Whether this is an `allow` or `block` list entry. | 该条目属于 `allow` 还是 `block` 名单。 |
| `resp.200.entries.entry_type` |  | Whether the entry matches a single `email` address or an entire `domain`. | 条目匹配单个 `email` 地址还是整个 `domain`。 |
| `resp.200.entries.created_at` | Time at which entry was created. | When the resource was created. | 资源创建时间。 |
| `resp.200.entries.read_only` | Whether the entry is read-only and cannot be deleted via the API. | When true, the entry is system-managed and cannot be deleted through the API. | 为 true 时，条目由系统管理，不能通过 API 删除。 |

## create

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail lists create --direction <direction> --type <type> --entry user@example.com<br>``` | Add an email address or domain to an allow/block list, scoped by the `direction` and `type` path parameters. Returns the created entry. | 向允许/拦截名单新增一个邮箱地址或域名，作用范围由路径参数 `direction` 与 `type` 决定。返回新建的条目。 |
| `param:direction` |  | Traffic direction the new entry should govern: `send`, `receive`, or `reply`. | 新条目作用的流量方向：`send`、`receive` 或 `reply`。 |
| `param:type` |  | Whether to add the entry to the `allow` or `block` list. | 将条目加入 `allow` 还是 `block` 名单。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密。 |
| `req.entry` | Email address or domain to add. | Email address or domain to add to the list. | 要加入名单的邮箱地址或域名。 |
| `req.reason` | Reason for adding the entry. | Optional free-text note recording why the entry was added. | 可选的自由文本备注，记录添加该条目的原因。 |
| `resp.200.entry` | Email address or domain of list entry. | The email address or domain of the list entry. | 名单条目的邮箱地址或域名。 |
| `resp.200.organization_id` |  | ID of the organization the list entry belongs to. | 名单条目所属的组织 ID。 |
| `resp.200.reason` | Reason for adding the entry. | Free-text reason recorded when the entry was added. | 添加该条目时记录的自由文本原因。 |
| `resp.200.direction` |  | Traffic direction the entry governs: `send`, `receive`, or `reply`. | 条目作用的流量方向：`send`、`receive` 或 `reply`。 |
| `resp.200.list_type` |  | Whether this is an `allow` or `block` list entry. | 该条目属于 `allow` 还是 `block` 名单。 |
| `resp.200.entry_type` |  | Whether the entry matches a single `email` address or an entire `domain`. | 条目匹配单个 `email` 地址还是整个 `domain`。 |
| `resp.200.created_at` | Time at which entry was created. | When the resource was created. | 资源创建时间。 |
| `resp.200.read_only` | Whether the entry is read-only and cannot be deleted via the API. | When true, the entry is system-managed and cannot be deleted through the API. | 为 true 时，条目由系统管理，不能通过 API 删除。 |
| `resp.400.name` |  | Machine-readable error name identifying the validation failure. | 标识本次校验失败的机器可读错误名。 |
| `resp.400.errors` | Validation errors. | Details of the validation problems with the query parameters. | 查询参数校验问题的明细。 |

## list

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail threads list<br>``` | List resources with cursor pagination. This operationId is shared by three endpoints: list threads, list drafts, and list allow/block list entries. Supports time/label filters where applicable; iterate with `next_page_token` to walk all pages. | 分页列出资源（基于游标）。该 operationId 由三个端点共用：列出对话、列出草稿、列出允许/拦截名单条目。在适用处支持时间与标签筛选；通过 `next_page_token` 翻页可遍历全部结果。 |
| `param:limit` |  | Maximum number of items to return in this page. | 本页返回的最大条目数。 |
| `param:page_token` |  | Pagination cursor. Pass the `next_page_token` from the previous response to fetch the next page; omit for the first page. | 分页游标。传入上一次响应的 `next_page_token` 以取下一页；首页可不传。 |
| `param:labels` |  | Restrict results to items carrying all of these labels. | 仅返回带有全部这些标签的条目。 |
| `param:before` |  | Only return items with a timestamp before this moment. | 仅返回时间戳早于该时刻的条目。 |
| `param:after` |  | Only return items with a timestamp after this moment. | 仅返回时间戳晚于该时刻的条目。 |
| `param:ascending` |  | When true, return items in ascending time order instead of the default newest-first. | 为 true 时按时间升序返回，而非默认的最新优先。 |
| `param:include_spam` |  | When true, include items labeled spam in the results. | 为 true 时在结果中包含被标记为垃圾邮件（spam）的条目。 |
| `param:include_blocked` |  | When true, include items labeled blocked in the results. | 为 true 时在结果中包含被标记为拦截（blocked）的条目。 |
| `param:include_unauthenticated` |  | When true, include items from unauthenticated senders in the results. | 为 true 时在结果中包含来自未通过认证发件人的条目。 |
| `param:include_trash` |  | When true, include items in trash in the results. | 为 true 时在结果中包含回收站（trash）内的条目。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密。 |
| `resp.200.count` |  | Number of items returned in this page. | 本页返回的条目数。 |
| `resp.200.limit` |  | The limit that was applied to this page. | 本页实际生效的数量上限。 |
| `resp.200.next_page_token` |  | Cursor for the next page; pass it back as `page_token`. Absent or empty when there are no more pages. | 下一页的游标；作为 `page_token` 回传。无更多页时缺省或为空。 |
| `resp.200.threads` | Ordered by `timestamp` descending. | The page of threads, newest first. | 本页对话列表，最新优先。 |
| `resp.200.threads.inbox_id` |  | ID of the inbox that owns the thread. | 拥有该对话的收件箱 ID。 |
| `resp.200.threads.thread_id` |  | ID of the thread, usable as the path parameter for thread operations. | 对话 ID，可用作对话相关操作的路径参数。 |
| `resp.200.threads.labels` |  | Labels applied to the thread. | 应用于该对话的标签。 |
| `resp.200.threads.timestamp` |  | When the last message was sent or received. | 最近一次发送或接收消息的时间。 |
| `resp.200.threads.received_timestamp` |  | When the last message was received. | 最近一次接收消息的时间。 |
| `resp.200.threads.sent_timestamp` |  | When the last message was sent. | 最近一次发送消息的时间。 |
| `resp.200.threads.senders` |  | Distinct sender addresses in the thread. | 对话中出现过的不同发件人地址。 |
| `resp.200.threads.recipients` |  | Distinct recipient addresses in the thread. | 对话中出现过的不同收件人地址。 |
| `resp.200.threads.subject` |  | Subject of the thread. | 对话主题。 |
| `resp.200.threads.preview` |  | Plain-text snippet of the last message. | 最后一条消息的纯文本短摘要。 |
| `resp.200.threads.attachments` |  | Attachments present in the thread. | 对话中包含的附件。 |
| `resp.200.threads.attachments.attachment_id` |  | ID of the attachment, used as the path parameter for the get-attachment endpoint. | 附件 ID，作为获取附件端点的路径参数。 |
| `resp.200.threads.attachments.filename` |  | Original filename of the attachment. | 附件的原始文件名。 |
| `resp.200.threads.attachments.size` |  | Attachment size in bytes. | 附件大小（字节）。 |
| `resp.200.threads.attachments.content_type` |  | MIME content type of the attachment (e.g. `application/pdf`). | 附件的 MIME 内容类型（如 `application/pdf`）。 |
| `resp.200.threads.attachments.content_disposition` |  | How the attachment is presented: `inline` (rendered within the body, e.g. an embedded image) or `attachment` (a downloadable file). | 附件呈现方式：`inline`（随正文内嵌，如内嵌图片）或 `attachment`（可下载的文件）。 |
| `resp.200.threads.attachments.content_id` |  | Content-ID used to reference an inline attachment from within the HTML body (via `cid:`). | Content-ID，用于在 HTML 正文中以 `cid:` 引用内嵌附件。 |
| `resp.200.threads.last_message_id` |  | ID of the most recent message in the thread. | 对话中最新一条消息的 ID。 |
| `resp.200.threads.message_count` |  | Number of messages in the thread. | 对话中的消息数量。 |
| `resp.200.threads.size` |  | Total size of the thread in bytes. | 对话的总大小（字节）。 |
| `resp.200.threads.updated_at` |  | When the thread was last updated. | 对话最后更新时间。 |
| `resp.200.threads.created_at` |  | When the thread was created. | 对话创建时间。 |
| `resp.404.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.404.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |

## get-attachment

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail drafts get-attachment --draft-id <draft_id> --attachment-id <attachment_id><br>``` | Get attachment metadata together with a time-limited presigned download URL. Shared by two endpoints: fetch an attachment from a draft (`draft_id`) or from a thread (`thread_id`), in both cases by `attachment_id`. | 获取附件元数据及一个限时的预签名下载链接。由两个端点共用：从草稿（`draft_id`）或从对话（`thread_id`）按 `attachment_id` 获取附件。 |
| `param:draft_id` |  | ID of the draft that contains the attachment. (Draft attachment endpoint only.) | 包含该附件的草稿 ID。（仅草稿附件端点） |
| `param:attachment_id` |  | ID of the attachment to fetch. Obtain it from the `attachment_id` field of a message/thread/draft attachment. | 要获取的附件 ID。可从消息/对话/草稿附件的 `attachment_id` 字段获得。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密。 |
| `resp.200.attachment_id` |  | ID of the attachment. | 附件 ID。 |
| `resp.200.filename` |  | Original filename of the attachment. | 附件的原始文件名。 |
| `resp.200.size` |  | Attachment size in bytes. | 附件大小（字节）。 |
| `resp.200.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.content_disposition` |  | How the attachment is presented: `inline` or `attachment`. | 附件呈现方式：`inline` 或 `attachment`。 |
| `resp.200.content_id` |  | Content-ID for referencing an inline attachment from the HTML body. | Content-ID，用于在 HTML 正文中引用内嵌附件。 |
| `resp.200.download_url` | URL to download the attachment. | Time-limited presigned URL to download the attachment binary. Fetch the file before `expires_at`. | 限时预签名下载链接，用于下载附件二进制内容。请在 `expires_at` 之前完成下载。 |
| `resp.200.expires_at` | Time at which the download URL expires. | When the download URL expires and stops working. | 下载链接失效的时间。 |
| `resp.404.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.404.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |

## get-attachment

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail threads get-attachment --thread-id <thread_id> --attachment-id <attachment_id><br>``` | Get attachment metadata together with a time-limited presigned download URL. Shared by two endpoints: fetch an attachment from a draft (`draft_id`) or from a thread (`thread_id`), in both cases by `attachment_id`. | 获取附件元数据及一个限时的预签名下载链接。由两个端点共用：从草稿（`draft_id`）或从对话（`thread_id`）按 `attachment_id` 获取附件。 |
| `param:thread_id` |  | ID of the thread that contains the attachment. (Thread attachment endpoint only.) | 包含该附件的对话 ID。（仅对话附件端点） |
| `param:attachment_id` |  | ID of the attachment to fetch. Obtain it from the `attachment_id` field of a message/thread/draft attachment. | 要获取的附件 ID。可从消息/对话/草稿附件的 `attachment_id` 字段获得。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密。 |
| `resp.200.attachment_id` |  | ID of the attachment. | 附件 ID。 |
| `resp.200.filename` |  | Original filename of the attachment. | 附件的原始文件名。 |
| `resp.200.size` |  | Attachment size in bytes. | 附件大小（字节）。 |
| `resp.200.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.content_disposition` |  | How the attachment is presented: `inline` or `attachment`. | 附件呈现方式：`inline` 或 `attachment`。 |
| `resp.200.content_id` |  | Content-ID for referencing an inline attachment from the HTML body. | Content-ID，用于在 HTML 正文中引用内嵌附件。 |
| `resp.200.download_url` | URL to download the attachment. | Time-limited presigned URL to download the attachment binary. Fetch the file before `expires_at`. | 限时预签名下载链接，用于下载附件二进制内容。请在 `expires_at` 之前完成下载。 |
| `resp.200.expires_at` | Time at which the download URL expires. | When the download URL expires and stops working. | 下载链接失效的时间。 |
| `resp.404.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.404.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |

## query

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail metrics list<br>``` | Query email delivery metrics aggregated into time buckets. Results are grouped by event type (sent, delivered, bounced, etc.) over the requested time window and bucket period. | 查询邮件投递指标，按时间桶聚合。结果按事件类型（sent、delivered、bounced 等）分组，覆盖请求指定的时间窗口与桶周期。 |
| `param:event_types` |  | Which metric event types to include, e.g. `message.sent`, `message.delivered`, `message.bounced`. Omit to query the default set. | 要纳入统计的指标事件类型，如 `message.sent`、`message.delivered`、`message.bounced`。不传则查询默认集合。 |
| `param:start` |  | Start of the time window to query (inclusive). | 查询时间窗口的起点（含）。 |
| `param:end` |  | End of the time window to query (exclusive). | 查询时间窗口的终点（不含）。 |
| `param:period` |  | Width of each time bucket, expressed as a number of seconds. Determines the granularity of the aggregation. | 每个时间桶的宽度，以秒数表示，决定聚合的粒度。 |
| `param:limit` |  | Maximum number of time buckets to return. | 返回的时间桶最大数量。 |
| `param:descending` |  | When true, return buckets in descending time order (newest first). | 为 true 时按时间降序返回桶（最新优先）。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密。 |
| `resp.400.name` |  | Machine-readable error name identifying the validation failure. | 标识本次校验失败的机器可读错误名。 |
| `resp.400.errors` | Validation errors. | Details of the validation problems with the query parameters. | 查询参数校验问题的明细。 |

## get

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail lists get --direction <direction> --type <type> --entry <entry><br>``` | Fetch a single resource by its ID. This operationId is shared by three endpoints: get a thread (with its full message list) by `thread_id`, get a draft by `draft_id`, and get one allow/block list entry by `direction`/`type`/`entry`. The path determines which resource and response shape you receive. | 按 ID 获取单个资源。该 operationId 由三个端点共用：按 `thread_id` 获取对话（含完整消息列表）、按 `draft_id` 获取草稿、按 `direction`/`type`/`entry` 获取单条允许/拦截名单条目。具体取哪种资源及返回结构由请求路径决定。 |
| `param:direction` |  | Which traffic direction the list entry governs: `send` (your outbound), `receive` (inbound to you), or `reply`. Combined with `type` it selects exactly one list. | 名单条目作用的流量方向：`send`（出站）、`receive`（入站）或 `reply`（回复）。与 `type` 组合可精确定位一份名单。 |
| `param:type` |  | Whether to address the allow list or the block list. `allow` permits the entry; `block` denies it. Combined with `direction` it selects exactly one list. | 操作允许名单还是拦截名单：`allow` 放行、`block` 拦截。与 `direction` 组合可精确定位一份名单。 |
| `param:entry` | Email address or domain. | The exact email address or domain identifying the list entry to fetch. | 标识要获取的名单条目的邮箱地址或域名（需精确匹配）。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret; never log it in plaintext. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密，切勿明文记录。 |
| `resp.200.entry` | Email address or domain of list entry. | The email address or domain of the list entry. | 名单条目的邮箱地址或域名。 |
| `resp.200.organization_id` |  | ID of the organization the list entry belongs to. | 名单条目所属的组织 ID。 |
| `resp.200.reason` | Reason for adding the entry. | Free-text reason recorded when the entry was added. | 添加该条目时记录的自由文本原因。 |
| `resp.200.direction` |  | Traffic direction the entry governs: `send`, `receive`, or `reply`. | 条目作用的流量方向：`send`、`receive` 或 `reply`。 |
| `resp.200.list_type` |  | Whether this is an `allow` or `block` list entry. | 该条目属于 `allow` 还是 `block` 名单。 |
| `resp.200.entry_type` |  | Whether the entry matches a single `email` address or an entire `domain`. | 条目匹配单个 `email` 地址还是整个 `domain`。 |
| `resp.200.created_at` | Time at which entry was created. | When the resource was created. | 资源创建时间。 |
| `resp.200.read_only` | Whether the entry is read-only and cannot be deleted via the API. | When true, the entry is system-managed and cannot be deleted through the API. | 为 true 时，条目由系统管理，不能通过 API 删除。 |
| `resp.404.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.404.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |

## delete

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail lists delete --direction <direction> --type <type> --entry <entry><br>``` | Delete a resource by its ID. Shared by two endpoints: delete a thread (moves it to trash, or permanently removes it when already trashed or when `permanent=true`) and delete one allow/block list entry. Read-only system entries cannot be deleted. | 按 ID 删除资源。由两个端点共用：删除对话（移入回收站；若已在回收站或 `permanent=true` 则永久删除）、删除单条允许/拦截名单条目。只读的系统条目无法删除。 |
| `param:direction` |  | Traffic direction of the list entry to delete: `send`, `receive`, or `reply`. | 要删除的名单条目的流量方向：`send`、`receive` 或 `reply`。 |
| `param:type` |  | Whether the entry is on the `allow` or `block` list. | 条目位于 `allow` 还是 `block` 名单。 |
| `param:entry` | Email address or domain. | The exact email address or domain of the list entry to delete. System (read-only) entries cannot be removed. | 要删除的名单条目的邮箱地址或域名（需精确匹配）。系统（只读）条目不可删除。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密。 |
| `resp.404.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.404.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |

## list

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail drafts list<br>``` | List resources with cursor pagination. This operationId is shared by three endpoints: list threads, list drafts, and list allow/block list entries. Supports time/label filters where applicable; iterate with `next_page_token` to walk all pages. | 分页列出资源（基于游标）。该 operationId 由三个端点共用：列出对话、列出草稿、列出允许/拦截名单条目。在适用处支持时间与标签筛选；通过 `next_page_token` 翻页可遍历全部结果。 |
| `param:limit` |  | Maximum number of items to return in this page. | 本页返回的最大条目数。 |
| `param:page_token` |  | Pagination cursor. Pass the `next_page_token` from the previous response to fetch the next page; omit for the first page. | 分页游标。传入上一次响应的 `next_page_token` 以取下一页；首页可不传。 |
| `param:labels` |  | Restrict results to items carrying all of these labels. | 仅返回带有全部这些标签的条目。 |
| `param:before` |  | Only return items with a timestamp before this moment. | 仅返回时间戳早于该时刻的条目。 |
| `param:after` |  | Only return items with a timestamp after this moment. | 仅返回时间戳晚于该时刻的条目。 |
| `param:ascending` |  | When true, return items in ascending time order instead of the default newest-first. | 为 true 时按时间升序返回，而非默认的最新优先。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密。 |
| `resp.200.count` |  | Number of items returned in this page. | 本页返回的条目数。 |
| `resp.200.limit` |  | The limit that was applied to this page. | 本页实际生效的数量上限。 |
| `resp.200.next_page_token` |  | Cursor for the next page; pass it back as `page_token`. Absent or empty when there are no more pages. | 下一页的游标；作为 `page_token` 回传。无更多页时缺省或为空。 |
| `resp.200.drafts` | Ordered by `updated_at` descending. | The page of drafts, most recently updated first. | 本页草稿列表，按最近更新优先。 |
| `resp.200.drafts.inbox_id` |  | ID of the inbox that owns the draft. | 拥有该草稿的收件箱 ID。 |
| `resp.200.drafts.draft_id` |  | ID of the draft, usable as the path parameter for draft operations. | 草稿 ID，可用作草稿相关操作的路径参数。 |
| `resp.200.drafts.labels` |  | Labels applied to the draft. | 应用于该草稿的标签。 |
| `resp.200.drafts.to` |  | Primary recipient addresses of the draft. | 草稿的主要收件人地址。 |
| `resp.200.drafts.cc` |  | CC recipient addresses of the draft. | 草稿的抄送收件人地址。 |
| `resp.200.drafts.bcc` |  | BCC recipient addresses of the draft. | 草稿的密送收件人地址。 |
| `resp.200.drafts.subject` |  | Subject of the draft. | 草稿主题。 |
| `resp.200.drafts.preview` |  | Plain-text snippet of the draft body. | 草稿正文的纯文本短摘要。 |
| `resp.200.drafts.attachments` |  | Attachments present in the draft. | 草稿中包含的附件。 |
| `resp.200.drafts.attachments.attachment_id` |  | ID of the attachment, used as the path parameter for the get-attachment endpoint. | 附件 ID，作为获取附件端点的路径参数。 |
| `resp.200.drafts.attachments.filename` |  | Original filename of the attachment. | 附件的原始文件名。 |
| `resp.200.drafts.attachments.size` |  | Attachment size in bytes. | 附件大小（字节）。 |
| `resp.200.drafts.attachments.content_type` |  | MIME content type of the attachment (e.g. `application/pdf`). | 附件的 MIME 内容类型（如 `application/pdf`）。 |
| `resp.200.drafts.attachments.content_disposition` |  | How the attachment is presented: `inline` (rendered within the body, e.g. an embedded image) or `attachment` (a downloadable file). | 附件呈现方式：`inline`（随正文内嵌，如内嵌图片）或 `attachment`（可下载的文件）。 |
| `resp.200.drafts.attachments.content_id` |  | Content-ID used to reference an inline attachment from within the HTML body (via `cid:`). | Content-ID，用于在 HTML 正文中以 `cid:` 引用内嵌附件。 |
| `resp.200.drafts.in_reply_to` |  | ID of the message the draft replies to, if any. | 草稿所回复的目标消息 ID（如有）。 |
| `resp.200.drafts.send_status` |  | Scheduled-send state of the draft: `scheduled`, `sending`, or `failed`. | 草稿的定时发送状态：`scheduled`、`sending` 或 `failed`。 |
| `resp.200.drafts.send_at` |  | When the draft is scheduled to be sent. | 草稿计划发送的时间。 |
| `resp.200.drafts.updated_at` |  | When the draft was last updated. | 草稿最后更新时间。 |
| `resp.404.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.404.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |

## get

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail drafts get --draft-id <draft_id><br>``` | Fetch a single resource by its ID. This operationId is shared by three endpoints: get a thread (with its full message list) by `thread_id`, get a draft by `draft_id`, and get one allow/block list entry by `direction`/`type`/`entry`. The path determines which resource and response shape you receive. | 按 ID 获取单个资源。该 operationId 由三个端点共用：按 `thread_id` 获取对话（含完整消息列表）、按 `draft_id` 获取草稿、按 `direction`/`type`/`entry` 获取单条允许/拦截名单条目。具体取哪种资源及返回结构由请求路径决定。 |
| `param:draft_id` |  | ID of the draft to fetch. Obtain it from the `draft_id` field of a list-drafts result or a create-draft response. | 要获取的草稿 ID。可从列出草稿的结果或创建草稿响应的 `draft_id` 字段获得。 |
| `param:Authorization` | Bearer authentication | Bearer token for authentication, sent as `Bearer <api_key>`. Keep the key secret; never log it in plaintext. | 用于鉴权的 Bearer 令牌，格式为 `Bearer <api_key>`。请妥善保密，切勿明文记录。 |
| `resp.200.inbox_id` |  | ID of the inbox that owns this resource. | 拥有该资源的收件箱 ID。 |
| `resp.200.draft_id` |  | ID of the draft, usable as the path parameter for draft operations. | 草稿 ID，可用作草稿相关操作的路径参数。 |
| `resp.200.client_id` |  | Caller-supplied client ID echoed back, useful for correlating the draft with your own records. | 回显的调用方自定义 client ID，便于将草稿与你自己的记录关联。 |
| `resp.200.labels` |  | Labels currently applied, including both system labels and your custom labels. | 当前应用的标签，含系统标签与自定义标签。 |
| `resp.200.reply_to` |  | Reply-To addresses recipients should reply to instead of the From address. | 回复目标地址，收件人应回复到此处而非 From 地址。 |
| `resp.200.to` |  | Primary recipient addresses. | 主要收件人地址。 |
| `resp.200.cc` |  | CC (carbon copy) recipient addresses. | 抄送（CC）收件人地址。 |
| `resp.200.bcc` |  | BCC (blind carbon copy) recipient addresses, not visible to other recipients. | 密送（BCC）收件人地址，其他收件人不可见。 |
| `resp.200.subject` |  | Subject line. | 主题。 |
| `resp.200.preview` |  | Short plain-text snippet of the content, for list-style display. | 内容的纯文本短摘要，用于列表展示。 |
| `resp.200.text` |  | Plain-text body. | 纯文本正文。 |
| `resp.200.html` |  | HTML body. | HTML 正文。 |
| `resp.200.attachments` |  | Attachments belonging to this resource. | 该资源包含的附件。 |
| `resp.200.attachments.attachment_id` |  | ID of the attachment, used as the path parameter for the get-attachment endpoint. | 附件 ID，作为获取附件端点的路径参数。 |
| `resp.200.attachments.filename` |  | Original filename of the attachment. | 附件的原始文件名。 |
| `resp.200.attachments.size` |  | Attachment size in bytes. | 附件大小（字节）。 |
| `resp.200.attachments.content_type` |  | MIME content type of the attachment (e.g. `application/pdf`). | 附件的 MIME 内容类型（如 `application/pdf`）。 |
| `resp.200.attachments.content_disposition` |  | How the attachment is presented: `inline` (rendered within the body, e.g. an embedded image) or `attachment` (a downloadable file). | 附件呈现方式：`inline`（随正文内嵌，如内嵌图片）或 `attachment`（可下载的文件）。 |
| `resp.200.attachments.content_id` |  | Content-ID used to reference an inline attachment from within the HTML body (via `cid:`). | Content-ID，用于在 HTML 正文中以 `cid:` 引用内嵌附件。 |
| `resp.200.in_reply_to` |  | ID of the message this draft/thread is replying to, if any. | 本草稿/对话所回复的目标消息 ID（如有）。 |
| `resp.200.references` | IDs of previous messages in thread. | IDs of earlier messages in the thread, forming the reply chain. | 对话中较早消息的 ID 列表，构成回复链。 |
| `resp.200.send_status` |  | Scheduled-send state of the draft: `scheduled` (queued for `send_at`), `sending`, or `failed`. Absent for drafts with no scheduled send. | 草稿的定时发送状态：`scheduled`（已排期到 `send_at`）、`sending`、`failed`。未设定时发送的草稿无此字段。 |
| `resp.200.send_at` |  | When the draft is scheduled to be sent. | 草稿计划发送的时间。 |
| `resp.200.updated_at` |  | When the resource was last updated. | 资源最后更新时间。 |
| `resp.200.created_at` | Time at which draft was created. | When the resource was created. | 资源创建时间。 |
| `resp.404.name` |  | Machine-readable error name identifying the failure. | 标识此次失败的机器可读错误名。 |
| `resp.404.message` |  | Human-readable description of the error. | 面向人类的错误描述。 |

