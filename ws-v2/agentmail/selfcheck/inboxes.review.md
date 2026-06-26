# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 33 个接口，684 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## get

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:drafts get --inbox-id <inbox_id> --draft-id <draft_id><br>``` | Retrieve a single AgentMail resource by its path identifiers. The exact resource returned depends on the route: an inbox, a draft, a message, a thread, or a single allow/block list entry. The full object (including bodies, attachments and timestamps) is returned, so this is the canonical way to fetch the complete state of one item after listing. | 按路径标识获取单个 AgentMail 资源。返回对象的类型取决于路由：收件箱、草稿、消息、会话或单条 allow/block 名单条目。返回完整对象（含正文、附件与时间戳），是在列表查询后获取某一项完整状态的标准方式。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource. Obtain it from create (POST /agentmail/inboxes) or list (GET /agentmail/inboxes). | 拥有该资源的收件箱标识。可经 create (POST /agentmail/inboxes) 或 list (GET /agentmail/inboxes) 获取。 |
| `param:draft_id` |  | Identifier of the draft to retrieve, as returned when the draft was created. | 要获取的草稿标识，由创建草稿时返回。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox. Send as `Bearer <api_key>`; keep it secret and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌。以 `Bearer <api_key>` 形式发送；务必保密，切勿明文记录。 |
| `resp.200.inbox_id` |  | Identifier of the inbox the created resource belongs to. | 所创建资源所属的收件箱标识。 |
| `resp.200.draft_id` |  | Unique identifier of the created draft. | 所创建草稿的唯一标识。 |
| `resp.200.client_id` |  | Caller-supplied identifier echoed back on the created resource. | 回显在所创建资源上的调用方自定义标识。 |
| `resp.200.labels` |  | Labels applied to the created draft. | 应用于所创建草稿的标签。 |
| `resp.200.reply_to` |  | Reply-to addresses of the draft. | 草稿的回复至地址。 |
| `resp.200.to` |  | Primary recipient addresses of the draft. | 草稿的主要收件人地址。 |
| `resp.200.cc` |  | Carbon-copy recipient addresses of the draft. | 草稿的抄送（CC）收件人地址。 |
| `resp.200.bcc` |  | Blind carbon-copy recipient addresses of the draft. | 草稿的密送（BCC）收件人地址。 |
| `resp.200.subject` |  | Subject line of the draft. | 草稿主题。 |
| `resp.200.preview` |  | Short plain-text snippet of the draft body. | 草稿正文的简短纯文本片段。 |
| `resp.200.text` |  | Plain-text body of the draft. | 草稿的纯文本正文。 |
| `resp.200.html` |  | HTML body of the draft. | 草稿的 HTML 正文。 |
| `resp.200.attachments` |  | Attachments stored on the draft. | 草稿上保存的附件。 |
| `resp.200.attachments.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.attachments.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.attachments.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.attachments.content_disposition` |  | `inline` renders within the body; `attachment` is a downloadable file. | `inline` 在正文内联渲染；`attachment` 为可下载文件。 |
| `resp.200.attachments.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.in_reply_to` |  | Identifier of the message this draft replies to, if any. | 该草稿所回复的消息标识（如有）。 |
| `resp.200.references` | IDs of previous messages in thread. | Identifiers of earlier messages in the thread. | 会话中较早消息的标识。 |
| `resp.200.send_status` |  | Schedule status: `scheduled` queued for future send, `sending` in progress, `failed` send did not complete. | 定时状态：`scheduled` 已排队待发，`sending` 发送中，`failed` 发送未完成。 |
| `resp.200.send_at` |  | Scheduled send time of the draft. | 草稿的计划发送时间。 |
| `resp.200.updated_at` |  | Time the draft was last updated. | 草稿最后更新时间。 |
| `resp.200.created_at` | Time at which draft was created. | Time the resource was created. | 资源创建时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## delete

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:drafts delete --inbox-id <inbox_id> --draft-id <draft_id><br>``` | Delete a resource identified by its path (inbox, draft, message, thread, or list entry). Returns an empty success response with no body. For threads, deletion moves the thread to trash unless the `permanent` query flag forces hard deletion. | 按路径删除资源（收件箱、草稿、消息、会话或名单条目）。成功时返回空响应、无响应体。对会话而言，默认移入回收站，除非通过 `permanent` 查询参数强制彻底删除。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource being deleted. | 被删除资源所属的收件箱标识。 |
| `param:draft_id` |  | Identifier of the draft to delete. | 要删除的草稿标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## update

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:drafts update --inbox-id <inbox_id> --draft-id <draft_id> --subject "Updated subject"<br>``` | Partially update an existing resource identified by its path. Only the fields present in the request body are changed; omitted fields keep their current values. Applies to inboxes, drafts, messages (label changes) and threads (label changes); the response shape mirrors the resource being updated. | 按路径标识对已有资源做部分更新。仅修改请求体中出现的字段，未提供的字段保持原值。适用于收件箱、草稿、消息（改标签）与会话（改标签）；响应结构与被更新资源对应。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource being updated. | 被更新资源所属的收件箱标识。 |
| `param:draft_id` |  | Identifier of the draft to update. | 要更新的草稿标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.reply_to` |  | Replacement reply-to addresses for the draft. | 草稿的回复至（reply-to）地址，替换原值。 |
| `req.to` |  | Replacement primary recipient addresses for the draft. | 草稿的主要收件人地址，替换原值。 |
| `req.cc` |  | Replacement carbon-copy addresses for the draft. | 草稿的抄送（CC）地址，替换原值。 |
| `req.bcc` |  | Replacement blind carbon-copy addresses for the draft. | 草稿的密送（BCC）地址，替换原值。 |
| `req.subject` |  | New subject line for the draft. | 草稿的新主题。 |
| `req.text` |  | New plain-text body for the draft. | 草稿的新纯文本正文。 |
| `req.html` |  | New HTML body for the draft. | 草稿的新 HTML 正文。 |
| `req.send_at` |  | New scheduled send time for the draft; set it to schedule delayed delivery. | 草稿新的计划发送时间；设置后即可定时延迟发送。 |
| `resp.200.inbox_id` |  | Identifier of the inbox the created resource belongs to. | 所创建资源所属的收件箱标识。 |
| `resp.200.draft_id` |  | Unique identifier of the created draft. | 所创建草稿的唯一标识。 |
| `resp.200.client_id` |  | Caller-supplied identifier echoed back on the created resource. | 回显在所创建资源上的调用方自定义标识。 |
| `resp.200.labels` |  | Labels applied to the created draft. | 应用于所创建草稿的标签。 |
| `resp.200.reply_to` |  | Reply-to addresses of the draft. | 草稿的回复至地址。 |
| `resp.200.to` |  | Primary recipient addresses of the draft. | 草稿的主要收件人地址。 |
| `resp.200.cc` |  | Carbon-copy recipient addresses of the draft. | 草稿的抄送（CC）收件人地址。 |
| `resp.200.bcc` |  | Blind carbon-copy recipient addresses of the draft. | 草稿的密送（BCC）收件人地址。 |
| `resp.200.subject` |  | Subject line of the draft. | 草稿主题。 |
| `resp.200.preview` |  | Short plain-text snippet of the draft body. | 草稿正文的简短纯文本片段。 |
| `resp.200.text` |  | Plain-text body of the draft. | 草稿的纯文本正文。 |
| `resp.200.html` |  | HTML body of the draft. | 草稿的 HTML 正文。 |
| `resp.200.attachments` |  | Attachments stored on the draft. | 草稿上保存的附件。 |
| `resp.200.attachments.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.attachments.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.attachments.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.attachments.content_disposition` |  | `inline` renders within the body; `attachment` is a downloadable file. | `inline` 在正文内联渲染；`attachment` 为可下载文件。 |
| `resp.200.attachments.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.in_reply_to` |  | Identifier of the message this draft replies to, if any. | 该草稿所回复的消息标识（如有）。 |
| `resp.200.references` | IDs of previous messages in thread. | Identifiers of earlier messages in the thread. | 会话中较早消息的标识。 |
| `resp.200.send_status` |  | Schedule status: `scheduled` queued for future send, `sending` in progress, `failed` send did not complete. | 定时状态：`scheduled` 已排队待发，`sending` 发送中，`failed` 发送未完成。 |
| `resp.200.send_at` |  | Scheduled send time of the draft. | 草稿的计划发送时间。 |
| `resp.200.updated_at` |  | Time the draft was last updated. | 草稿最后更新时间。 |
| `resp.200.created_at` | Time at which draft was created. | Time the resource was created. | 资源创建时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes get --inbox-id <inbox_id><br>``` | Retrieve a single AgentMail resource by its path identifiers. The exact resource returned depends on the route: an inbox, a draft, a message, a thread, or a single allow/block list entry. The full object (including bodies, attachments and timestamps) is returned, so this is the canonical way to fetch the complete state of one item after listing. | 按路径标识获取单个 AgentMail 资源。返回对象的类型取决于路由：收件箱、草稿、消息、会话或单条 allow/block 名单条目。返回完整对象（含正文、附件与时间戳），是在列表查询后获取某一项完整状态的标准方式。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource. Obtain it from create (POST /agentmail/inboxes) or list (GET /agentmail/inboxes). | 拥有该资源的收件箱标识。可经 create (POST /agentmail/inboxes) 或 list (GET /agentmail/inboxes) 获取。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox. Send as `Bearer <api_key>`; keep it secret and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌。以 `Bearer <api_key>` 形式发送；务必保密，切勿明文记录。 |
| `resp.200.pod_id` |  | Identifier of the pod the resource belongs to. | 资源所属 pod 的标识。 |
| `resp.200.inbox_id` |  | Identifier of the inbox the created resource belongs to. | 所创建资源所属的收件箱标识。 |
| `resp.200.email` |  | Full email address of the created inbox. | 所创建收件箱的完整邮箱地址。 |
| `resp.200.display_name` |  | Display name of the created inbox. | 所创建收件箱的显示名。 |
| `resp.200.client_id` |  | Caller-supplied identifier echoed back on the created resource. | 回显在所创建资源上的调用方自定义标识。 |
| `resp.200.metadata` | Custom metadata attached to the inbox. | Custom metadata attached to the created inbox. | 附加在所创建收件箱上的自定义元数据。 |
| `resp.200.updated_at` | Time at which inbox was last updated. | Time the draft was last updated. | 草稿最后更新时间。 |
| `resp.200.created_at` | Time at which inbox was created. | Time the resource was created. | 资源创建时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## delete

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes delete --inbox-id <inbox_id><br>``` | Delete a resource identified by its path (inbox, draft, message, thread, or list entry). Returns an empty success response with no body. For threads, deletion moves the thread to trash unless the `permanent` query flag forces hard deletion. | 按路径删除资源（收件箱、草稿、消息、会话或名单条目）。成功时返回空响应、无响应体。对会话而言，默认移入回收站，除非通过 `permanent` 查询参数强制彻底删除。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource being deleted. | 被删除资源所属的收件箱标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## update

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes update --inbox-id <inbox_id> --display-name "Updated Name"<br>``` | Partially update an existing resource identified by its path. Only the fields present in the request body are changed; omitted fields keep their current values. Applies to inboxes, drafts, messages (label changes) and threads (label changes); the response shape mirrors the resource being updated. | 按路径标识对已有资源做部分更新。仅修改请求体中出现的字段，未提供的字段保持原值。适用于收件箱、草稿、消息（改标签）与会话（改标签）；响应结构与被更新资源对应。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource being updated. | 被更新资源所属的收件箱标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.display_name` |  | New display name shown on outgoing mail from the inbox. | 收件箱发件时展示的新显示名。 |
| `req.metadata` | Metadata to merge into the inbox's existing metadata. Keys you include<br>are added or overwritten; keys you omit are left unchanged. To remove a<br>single key, send it with a null value. To clear all metadata, send<br>`metadata` as null. Sending an empty object is rejected; use null to<br>clear. Each update must include at least one of `display_name` or<br>`metadata`. | Key/value pairs merged into the inbox's existing metadata; include only the keys you want to change. | 合并进收件箱现有元数据的键值对；仅需包含想修改的键。 |
| `resp.200.pod_id` |  | Identifier of the pod the resource belongs to. | 资源所属 pod 的标识。 |
| `resp.200.inbox_id` |  | Identifier of the inbox the created resource belongs to. | 所创建资源所属的收件箱标识。 |
| `resp.200.email` |  | Full email address of the created inbox. | 所创建收件箱的完整邮箱地址。 |
| `resp.200.display_name` |  | Display name of the created inbox. | 所创建收件箱的显示名。 |
| `resp.200.client_id` |  | Caller-supplied identifier echoed back on the created resource. | 回显在所创建资源上的调用方自定义标识。 |
| `resp.200.metadata` | Custom metadata attached to the inbox. | Custom metadata attached to the created inbox. | 附加在所创建收件箱上的自定义元数据。 |
| `resp.200.updated_at` | Time at which inbox was last updated. | Time the draft was last updated. | 草稿最后更新时间。 |
| `resp.200.created_at` | Time at which inbox was created. | Time the resource was created. | 资源创建时间。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## reply-all

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:messages reply-all --inbox-id <inbox_id> --message-id <message_id> --text "Reply text"<br>``` | Send a reply to all participants of a message (original sender plus all To/Cc recipients), quoting and threading onto the original. Recipients are derived automatically from the source message, so you only supply the new body, optional attachments and headers. | 向某条消息的全部参与者（原发件人及全部 To/Cc 收件人）发送回复，自动引用并接续到原会话。收件人由源消息自动推导，因此只需提供新正文、可选附件与头部。 |
| `param:inbox_id` |  | Identifier of the inbox sending the reply-all. | 发送回复全部的收件箱标识。 |
| `param:message_id` |  | Identifier of the message being replied to; its recipients become the reply-all audience. | 被回复的消息标识，其收件人即回复全部的对象。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.labels` |  | Labels to apply to the reply-all message. | 为回复全部消息应用的标签。 |
| `req.reply_to` |  | Reply-to addresses for the reply-all message. | 回复全部消息的回复至地址。 |
| `req.text` |  | Plain-text body of the reply-all. | 回复全部的纯文本正文。 |
| `req.html` |  | HTML body of the reply-all. | 回复全部的 HTML 正文。 |
| `req.attachments` |  | Files to attach; provide each as base64 `content` or a fetchable `url`. | 随消息附带的文件；每个以 base64 `content` 或可拉取 `url` 提供。 |
| `req.attachments.filename` |  | Filename to give the attachment. | 为附件指定的文件名。 |
| `req.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `req.attachments.content_disposition` |  | `inline` to render within the body, `attachment` to offer as a download. | `inline` 在正文内联渲染，`attachment` 作为下载提供。 |
| `req.attachments.content_id` |  | Content-ID used to reference an inline attachment from the HTML body. | Content-ID，用于在 HTML 正文中引用内联附件。 |
| `req.attachments.content` | Base64 encoded content of attachment. | The attachment bytes, base64-encoded. Use this or `url`, not both. | 附件字节内容，base64 编码。与 `url` 二选一。 |
| `req.attachments.url` | URL to the attachment. | A URL the service fetches the attachment from. Use this or `content`, not both. | 服务据以拉取附件的 URL。与 `content` 二选一。 |
| `req.headers` |  | Additional raw email headers to set on the reply-all message. | 为回复全部消息设置的额外原始邮件头。 |
| `resp.200.message_id` |  | Identifier of the reply message that was sent. | 已发送的回复消息标识。 |
| `resp.200.thread_id` |  | Identifier of the thread the reply was added to. | 回复加入的会话标识。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |
| `resp.403.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.403.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## send

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:messages send --inbox-id <inbox_id> --to recipient@example.com --subject "Hello" --text "Body"<br>``` | Send an email message. Two routes share this operation: composing and sending a brand-new message from the inbox, or sending a previously saved draft by its `draft_id`. The response returns the resulting message and thread identifiers. | 发送邮件消息。两个路由共用此操作：从收件箱新建并发送全新消息，或按 `draft_id` 发送此前保存的草稿。响应返回生成的消息与会话标识。 |
| `param:inbox_id` |  | Identifier of the inbox sending the message. | 发送消息的收件箱标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.labels` |  | Labels to apply to the forwarded message. | 为转发消息应用的标签。 |
| `req.reply_to` |  | Reply-to addresses for the forwarded message. | 转发消息的回复至地址。 |
| `req.to` |  | Recipients to forward the message to. | 转发消息的目标收件人。 |
| `req.cc` |  | Carbon-copy recipients of the forward. | 转发的抄送（CC）收件人。 |
| `req.bcc` |  | Blind carbon-copy recipients of the forward. | 转发的密送（BCC）收件人。 |
| `req.subject` |  | Subject line of the forwarded message. | 转发消息的主题。 |
| `req.text` |  | Additional plain-text body to prepend to the forward. | 转发时附加在前的纯文本正文。 |
| `req.html` |  | Additional HTML body to prepend to the forward. | 转发时附加在前的 HTML 正文。 |
| `req.attachments` |  | Extra files to attach to the forward; provide each as base64 `content` or a fetchable `url`. | 转发时附带的额外文件；每个以 base64 `content` 或可拉取 `url` 提供。 |
| `req.attachments.filename` |  | Filename to give the attachment. | 为附件指定的文件名。 |
| `req.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `req.attachments.content_disposition` |  | `inline` to render within the body, `attachment` to offer as a download. | `inline` 在正文内联渲染，`attachment` 作为下载提供。 |
| `req.attachments.content_id` |  | Content-ID used to reference an inline attachment from the HTML body. | Content-ID，用于在 HTML 正文中引用内联附件。 |
| `req.attachments.content` | Base64 encoded content of attachment. | The attachment bytes, base64-encoded. Use this or `url`, not both. | 附件字节内容，base64 编码。与 `url` 二选一。 |
| `req.attachments.url` | URL to the attachment. | A URL the service fetches the attachment from. Use this or `content`, not both. | 服务据以拉取附件的 URL。与 `content` 二选一。 |
| `req.headers` |  | Additional raw email headers to set on the forwarded message. | 为转发消息设置的额外原始邮件头。 |
| `resp.200.message_id` |  | Identifier of the reply message that was sent. | 已发送的回复消息标识。 |
| `resp.200.thread_id` |  | Identifier of the thread the reply was added to. | 回复加入的会话标识。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |
| `resp.403.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.403.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:threads get --inbox-id <inbox_id> --thread-id <thread_id><br>``` | Retrieve a single AgentMail resource by its path identifiers. The exact resource returned depends on the route: an inbox, a draft, a message, a thread, or a single allow/block list entry. The full object (including bodies, attachments and timestamps) is returned, so this is the canonical way to fetch the complete state of one item after listing. | 按路径标识获取单个 AgentMail 资源。返回对象的类型取决于路由：收件箱、草稿、消息、会话或单条 allow/block 名单条目。返回完整对象（含正文、附件与时间戳），是在列表查询后获取某一项完整状态的标准方式。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource. Obtain it from create (POST /agentmail/inboxes) or list (GET /agentmail/inboxes). | 拥有该资源的收件箱标识。可经 create (POST /agentmail/inboxes) 或 list (GET /agentmail/inboxes) 获取。 |
| `param:thread_id` |  | Identifier of the thread to retrieve. Returned by the threads list and present on every message. | 要获取的会话标识。由会话列表返回，也出现在每条消息上。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox. Send as `Bearer <api_key>`; keep it secret and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌。以 `Bearer <api_key>` 形式发送；务必保密，切勿明文记录。 |
| `resp.200.inbox_id` |  | Identifier of the inbox that contains this thread. | 包含该会话的收件箱标识。 |
| `resp.200.thread_id` |  | Unique identifier of the thread, used to fetch, update or delete it. | 会话的唯一标识，用于获取、更新或删除会话。 |
| `resp.200.labels` |  | Labels currently applied to the thread, including system labels and any custom labels. | 当前应用于该会话的标签，含系统标签与自定义标签。 |
| `resp.200.timestamp` |  | Time of the most recent activity (last sent or received message) in the thread; use it to sort threads by recency. | 会话中最近一次活动（最后发送或接收消息）的时间，可据此按新鲜度排序。 |
| `resp.200.received_timestamp` |  | Time the thread last received an inbound message; null if it has never received one. | 会话最后一次收到入站消息的时间；从未收到则为空。 |
| `resp.200.sent_timestamp` |  | Time the thread last sent an outbound message; null if nothing has been sent. | 会话最后一次发出出站消息的时间；从未发送则为空。 |
| `resp.200.senders` |  | Distinct sender addresses that have appeared in the thread. | 在会话中出现过的不同发件人地址。 |
| `resp.200.recipients` |  | Distinct recipient addresses that have appeared in the thread. | 在会话中出现过的不同收件人地址。 |
| `resp.200.subject` |  | Subject line of the thread, typically taken from its first message. | 会话主题，通常取自首条消息。 |
| `resp.200.preview` |  | Short plain-text snippet of the latest message, for showing a thread summary without loading full bodies. | 最新消息的简短纯文本片段，便于在不加载完整正文时展示会话摘要。 |
| `resp.200.attachments` |  | All attachments accumulated across the thread's messages. | 会话内各消息累计的全部附件。 |
| `resp.200.attachments.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.attachments.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.attachments.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.attachments.content_disposition` |  | `inline` renders within the body; `attachment` is a downloadable file. | `inline` 在正文内联渲染；`attachment` 为可下载文件。 |
| `resp.200.attachments.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.last_message_id` |  | Identifier of the most recent message in the thread. | 会话中最新消息的标识。 |
| `resp.200.message_count` |  | Number of messages currently in the thread. | 会话当前包含的消息数。 |
| `resp.200.size` |  | Total size of the thread in bytes. | 会话总大小，单位字节。 |
| `resp.200.updated_at` |  | Time the thread record was last updated. | 会话记录最后更新时间。 |
| `resp.200.created_at` |  | Time the thread was created. | 会话创建时间。 |
| `resp.200.messages` | Messages in thread. Ordered by `timestamp` ascending. | Full messages in the thread, ordered oldest-first by timestamp. | 会话内的完整消息列表，按 timestamp 升序（最早在前）排列。 |
| `resp.200.messages.inbox_id` |  | Identifier of the inbox that contains this thread. | 包含该会话的收件箱标识。 |
| `resp.200.messages.thread_id` |  | Unique identifier of the thread, used to fetch, update or delete it. | 会话的唯一标识，用于获取、更新或删除会话。 |
| `resp.200.messages.message_id` |  | Unique identifier of the message. | 消息的唯一标识。 |
| `resp.200.messages.labels` |  | Labels currently applied to the thread, including system labels and any custom labels. | 当前应用于该会话的标签，含系统标签与自定义标签。 |
| `resp.200.messages.timestamp` |  | Time of the most recent activity (last sent or received message) in the thread; use it to sort threads by recency. | 会话中最近一次活动（最后发送或接收消息）的时间，可据此按新鲜度排序。 |
| `resp.200.messages.from` |  | Sender address of the message. | 消息的发件人地址。 |
| `resp.200.messages.reply_to` | Reply-to addresses. In format `username@domain.com` or `Display Name <username@domain.com>`. | Addresses replies should be directed to, when different from the sender. | 回复应发往的地址（当与发件人不同时）。 |
| `resp.200.messages.to` |  | Primary recipient addresses of the message. | 消息的主要收件人地址。 |
| `resp.200.messages.cc` |  | Carbon-copy recipient addresses. | 抄送（CC）收件人地址。 |
| `resp.200.messages.bcc` |  | Blind carbon-copy recipient addresses. | 密送（BCC）收件人地址。 |
| `resp.200.messages.subject` |  | Subject line of the thread, typically taken from its first message. | 会话主题，通常取自首条消息。 |
| `resp.200.messages.preview` |  | Short plain-text snippet of the latest message, for showing a thread summary without loading full bodies. | 最新消息的简短纯文本片段，便于在不加载完整正文时展示会话摘要。 |
| `resp.200.messages.text` |  | Plain-text body of the message. | 消息的纯文本正文。 |
| `resp.200.messages.html` |  | HTML body of the message. | 消息的 HTML 正文。 |
| `resp.200.messages.extracted_text` | Extracted new text content. | Just the newly written plain text, with quoted/replied history stripped out. | 仅新撰写的纯文本，已剔除引用/回复的历史内容。 |
| `resp.200.messages.extracted_html` | Extracted new HTML content. | Just the newly written HTML, with quoted/replied history stripped out. | 仅新撰写的 HTML，已剔除引用/回复的历史内容。 |
| `resp.200.messages.attachments` |  | All attachments accumulated across the thread's messages. | 会话内各消息累计的全部附件。 |
| `resp.200.messages.attachments.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.messages.attachments.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.messages.attachments.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.messages.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.messages.attachments.content_disposition` |  | `inline` renders within the body; `attachment` is a downloadable file. | `inline` 在正文内联渲染；`attachment` 为可下载文件。 |
| `resp.200.messages.attachments.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.messages.in_reply_to` |  | Identifier of the message this one is replying to, if any. | 该消息所回复的消息标识（如有）。 |
| `resp.200.messages.references` |  | Identifiers of earlier messages in the thread, forming the reply chain. | 会话中较早消息的标识，构成回复链。 |
| `resp.200.messages.headers` |  | Raw email headers of the message as key/value pairs. | 消息的原始邮件头，以键值对形式给出。 |
| `resp.200.messages.size` |  | Total size of the thread in bytes. | 会话总大小，单位字节。 |
| `resp.200.messages.updated_at` |  | Time the thread record was last updated. | 会话记录最后更新时间。 |
| `resp.200.messages.created_at` |  | Time the thread was created. | 会话创建时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## delete

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Moves the thread to trash by adding a trash label to all messages. If the thread is already in trash, it will be permanently deleted. Use `permanent=true` to force permanent deletion.<br><br>**CLI:**<br>```bash<br>agentmail inboxes:threads delete --inbox-id <inbox_id> --thread-id <thread_id><br>``` | Delete a resource identified by its path (inbox, draft, message, thread, or list entry). Returns an empty success response with no body. For threads, deletion moves the thread to trash unless the `permanent` query flag forces hard deletion. | 按路径删除资源（收件箱、草稿、消息、会话或名单条目）。成功时返回空响应、无响应体。对会话而言，默认移入回收站，除非通过 `permanent` 查询参数强制彻底删除。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource being deleted. | 被删除资源所属的收件箱标识。 |
| `param:thread_id` |  | Identifier of the thread to delete. | 要删除的会话标识。 |
| `param:permanent` | If true, permanently delete the thread instead of moving to trash. | When true, hard-delete the thread immediately instead of moving it to trash. | 为真时立即彻底删除会话，而非移入回收站。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## update

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Updates thread labels. Cannot add or remove system labels (sent, received, bounced, etc.). Rejects requests with a `422` for threads with 100 or more messages. | Partially update an existing resource identified by its path. Only the fields present in the request body are changed; omitted fields keep their current values. Applies to inboxes, drafts, messages (label changes) and threads (label changes); the response shape mirrors the resource being updated. | 按路径标识对已有资源做部分更新。仅修改请求体中出现的字段，未提供的字段保持原值。适用于收件箱、草稿、消息（改标签）与会话（改标签）；响应结构与被更新资源对应。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource being updated. | 被更新资源所属的收件箱标识。 |
| `param:thread_id` |  | Identifier of the thread to update. | 要更新的会话标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.add_labels` | Labels to add to thread. Cannot be system labels. | Labels to attach. For threads, system labels are not allowed. | 要添加的标签。会话不允许使用系统标签。 |
| `req.remove_labels` | Labels to remove from thread. Cannot be system labels. Takes priority over `add_labels` (in the event of duplicate labels passed in). | Labels to detach. For threads, system labels are not allowed and removal takes priority over additions of the same label. | 要移除的标签。会话不允许系统标签，且同名标签的移除优先于添加。 |
| `resp.200.thread_id` |  | Identifier of the updated thread. | 被更新会话的标识。 |
| `resp.200.labels` |  | The message's labels after the update is applied. | 更新生效后该消息的标签。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.422.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.422.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## list

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:threads list --inbox-id <inbox_id><br>``` | List a collection of resources within an inbox (threads, messages, drafts, events, list entries) or all inboxes. Results are paginated via `limit` + `page_token` and returned newest-first by default. Use the various `include_*` flags to widen the result set to spam/blocked/trash items. | 列出收件箱内的某类资源（会话、消息、草稿、事件、名单条目）或全部收件箱。通过 `limit` + `page_token` 分页，默认按时间倒序返回。可用各 `include_*` 开关把垃圾邮件/被拦截/回收站项纳入结果。 |
| `param:inbox_id` |  | Identifier of the inbox whose resources are being listed. Omit only on the route that lists all inboxes. | 被列举资源所属的收件箱标识。仅在列出全部收件箱的路由上可不传。 |
| `param:limit` |  | Maximum number of items to return in one page. | 单页返回的最大条目数。 |
| `param:page_token` |  | Opaque cursor for the next page; pass back the `next_page_token` from the previous response to continue. | 下一页的不透明游标；把上次响应的 `next_page_token` 回传即可翻页。 |
| `param:labels` |  | Restrict results to items carrying all of the given labels. | 仅返回带有全部所给标签的条目。 |
| `param:before` |  | Return only items dated before this time, for time-window filtering. | 仅返回此时间之前的条目，用于时间窗筛选。 |
| `param:after` |  | Return only items dated after this time, for time-window filtering. | 仅返回此时间之后的条目，用于时间窗筛选。 |
| `param:ascending` |  | When true, return results oldest-first instead of the default newest-first. | 为真时按最早在前返回，覆盖默认的最新在前。 |
| `param:include_spam` |  | When true, include items classified as spam in the results. | 为真时把判定为垃圾邮件的条目纳入结果。 |
| `param:include_blocked` |  | When true, include items from blocked senders in the results. | 为真时把来自被拦截发件人的条目纳入结果。 |
| `param:include_unauthenticated` |  | When true, include items that failed sender authentication (e.g. SPF/DKIM/DMARC). | 为真时把未通过发件人认证（如 SPF/DKIM/DMARC）的条目纳入结果。 |
| `param:include_trash` |  | When true, include items currently in trash. | 为真时把当前在回收站中的条目纳入结果。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.200.count` |  | Number of items returned in this page. | 本页返回的条目数。 |
| `resp.200.limit` |  | The page-size limit that was applied to this response. | 本响应实际应用的分页大小上限。 |
| `resp.200.next_page_token` |  | Cursor for the next page; pass it back as `page_token`. Absent or null when there are no more pages. | 下一页游标；作为 `page_token` 回传。无更多页时缺省或为空。 |
| `resp.200.threads` | Ordered by `timestamp` descending. | The page of threads, ordered by `timestamp` descending. | 本页会话，按 `timestamp` 倒序排列。 |
| `resp.200.threads.inbox_id` |  | Identifier of the inbox that contains the thread. | 包含该会话的收件箱标识。 |
| `resp.200.threads.thread_id` |  | Unique identifier of the thread. | 会话的唯一标识。 |
| `resp.200.threads.labels` |  | Labels applied to the thread. | 应用于该会话的标签。 |
| `resp.200.threads.timestamp` |  | Time of the latest activity in the thread. | 会话最近一次活动的时间。 |
| `resp.200.threads.received_timestamp` |  | Time the thread last received an inbound message. | 会话最后一次收到入站消息的时间。 |
| `resp.200.threads.sent_timestamp` |  | Time the thread last sent an outbound message. | 会话最后一次发出出站消息的时间。 |
| `resp.200.threads.senders` |  | Distinct sender addresses in the thread. | 会话中出现过的不同发件人地址。 |
| `resp.200.threads.recipients` |  | Distinct recipient addresses in the thread. | 会话中出现过的不同收件人地址。 |
| `resp.200.threads.subject` |  | Subject line of the thread. | 会话主题。 |
| `resp.200.threads.preview` |  | Short plain-text snippet of the latest message in the thread. | 会话最新消息的简短纯文本片段。 |
| `resp.200.threads.attachments` |  | Attachments accumulated across the thread. | 会话累计的附件。 |
| `resp.200.threads.attachments.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.threads.attachments.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.threads.attachments.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.threads.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.threads.attachments.content_disposition` |  | `inline` renders within the body; `attachment` is a downloadable file. | `inline` 在正文内联渲染；`attachment` 为可下载文件。 |
| `resp.200.threads.attachments.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.threads.last_message_id` |  | Identifier of the most recent message in the thread. | 会话中最新消息的标识。 |
| `resp.200.threads.message_count` |  | Number of messages in the thread. | 会话包含的消息数。 |
| `resp.200.threads.size` |  | Total size of the thread in bytes. | 会话总大小，单位字节。 |
| `resp.200.threads.updated_at` |  | Time the thread was last updated. | 会话最后更新时间。 |
| `resp.200.threads.created_at` |  | Time the thread was created. | 会话创建时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## list

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | List label change events for an inbox. Returns events in reverse chronological order by default. Use for IMAP UID projection or audit logging.<br><br>**CLI:**<br>```bash<br>agentmail inboxes:events list --inbox-id <inbox_id><br>``` | List a collection of resources within an inbox (threads, messages, drafts, events, list entries) or all inboxes. Results are paginated via `limit` + `page_token` and returned newest-first by default. Use the various `include_*` flags to widen the result set to spam/blocked/trash items. | 列出收件箱内的某类资源（会话、消息、草稿、事件、名单条目）或全部收件箱。通过 `limit` + `page_token` 分页，默认按时间倒序返回。可用各 `include_*` 开关把垃圾邮件/被拦截/回收站项纳入结果。 |
| `param:inbox_id` |  | Identifier of the inbox whose resources are being listed. Omit only on the route that lists all inboxes. | 被列举资源所属的收件箱标识。仅在列出全部收件箱的路由上可不传。 |
| `param:limit` |  | Maximum number of items to return in one page. | 单页返回的最大条目数。 |
| `param:page_token` |  | Opaque cursor for the next page; pass back the `next_page_token` from the previous response to continue. | 下一页的不透明游标；把上次响应的 `next_page_token` 回传即可翻页。 |
| `param:ascending` |  | When true, return results oldest-first instead of the default newest-first. | 为真时按最早在前返回，覆盖默认的最新在前。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.200.count` |  | Number of items returned in this page. | 本页返回的条目数。 |
| `resp.200.limit` |  | The page-size limit that was applied to this response. | 本响应实际应用的分页大小上限。 |
| `resp.200.next_page_token` |  | Cursor for the next page; pass it back as `page_token`. Absent or null when there are no more pages. | 下一页游标；作为 `page_token` 回传。无更多页时缺省或为空。 |
| `resp.200.events` | Ordered by `event_id` descending. | The page of inbox events, ordered by `event_id` descending. | 本页收件箱事件，按 `event_id` 倒序排列。 |
| `resp.200.events.organization_id` |  | Identifier of the organization that owns the event. | 拥有该事件的组织标识。 |
| `resp.200.events.pod_id` | ID of pod. | Identifier of the pod the event belongs to. | 事件所属 pod 的标识。 |
| `resp.200.events.inbox_id` |  | Identifier of the inbox the event occurred in. | 事件发生所在的收件箱标识。 |
| `resp.200.events.event_id` |  | Unique identifier of the event; also drives the descending sort order. | 事件的唯一标识，同时决定倒序排序。 |
| `resp.200.events.event_type` |  | What happened: `label.added` when a label was attached, `label.removed` when one was detached. | 发生了什么：`label.added` 表示加上了标签，`label.removed` 表示移除了标签。 |
| `resp.200.events.message_id` | ID of message. | Identifier of the message the event relates to. | 该事件关联的消息标识。 |
| `resp.200.events.label` | Label added or removed. | The label that was added or removed. | 被添加或移除的标签。 |
| `resp.200.events.event_at` | Time at which the event occurred. | Time the event actually occurred. | 事件实际发生的时间。 |
| `resp.200.events.created_at` | Time at which the event was recorded. | Time the event record was written. | 事件记录写入的时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:messages get --inbox-id <inbox_id> --message-id <message_id><br>``` | Retrieve a single AgentMail resource by its path identifiers. The exact resource returned depends on the route: an inbox, a draft, a message, a thread, or a single allow/block list entry. The full object (including bodies, attachments and timestamps) is returned, so this is the canonical way to fetch the complete state of one item after listing. | 按路径标识获取单个 AgentMail 资源。返回对象的类型取决于路由：收件箱、草稿、消息、会话或单条 allow/block 名单条目。返回完整对象（含正文、附件与时间戳），是在列表查询后获取某一项完整状态的标准方式。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource. Obtain it from create (POST /agentmail/inboxes) or list (GET /agentmail/inboxes). | 拥有该资源的收件箱标识。可经 create (POST /agentmail/inboxes) 或 list (GET /agentmail/inboxes) 获取。 |
| `param:message_id` |  | Identifier of the message to retrieve, as returned by the messages list. | 要获取的消息标识，由消息列表返回。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox. Send as `Bearer <api_key>`; keep it secret and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌。以 `Bearer <api_key>` 形式发送；务必保密，切勿明文记录。 |
| `resp.200.inbox_id` |  | Identifier of the inbox that contains this thread. | 包含该会话的收件箱标识。 |
| `resp.200.thread_id` |  | Unique identifier of the thread, used to fetch, update or delete it. | 会话的唯一标识，用于获取、更新或删除会话。 |
| `resp.200.message_id` |  | Unique identifier of the message. | 消息的唯一标识。 |
| `resp.200.labels` |  | Labels currently applied to the thread, including system labels and any custom labels. | 当前应用于该会话的标签，含系统标签与自定义标签。 |
| `resp.200.timestamp` |  | Time of the most recent activity (last sent or received message) in the thread; use it to sort threads by recency. | 会话中最近一次活动（最后发送或接收消息）的时间，可据此按新鲜度排序。 |
| `resp.200.from` |  | Sender address of the message. | 消息的发件人地址。 |
| `resp.200.reply_to` | Reply-to addresses. In format `username@domain.com` or `Display Name <username@domain.com>`. | Addresses replies should be directed to, when different from the sender. | 回复应发往的地址（当与发件人不同时）。 |
| `resp.200.to` |  | Primary recipient addresses of the message. | 消息的主要收件人地址。 |
| `resp.200.cc` |  | Carbon-copy recipient addresses. | 抄送（CC）收件人地址。 |
| `resp.200.bcc` |  | Blind carbon-copy recipient addresses. | 密送（BCC）收件人地址。 |
| `resp.200.subject` |  | Subject line of the thread, typically taken from its first message. | 会话主题，通常取自首条消息。 |
| `resp.200.preview` |  | Short plain-text snippet of the latest message, for showing a thread summary without loading full bodies. | 最新消息的简短纯文本片段，便于在不加载完整正文时展示会话摘要。 |
| `resp.200.text` |  | Plain-text body of the message. | 消息的纯文本正文。 |
| `resp.200.html` |  | HTML body of the message. | 消息的 HTML 正文。 |
| `resp.200.extracted_text` | Extracted new text content. | Just the newly written plain text, with quoted/replied history stripped out. | 仅新撰写的纯文本，已剔除引用/回复的历史内容。 |
| `resp.200.extracted_html` | Extracted new HTML content. | Just the newly written HTML, with quoted/replied history stripped out. | 仅新撰写的 HTML，已剔除引用/回复的历史内容。 |
| `resp.200.attachments` |  | All attachments accumulated across the thread's messages. | 会话内各消息累计的全部附件。 |
| `resp.200.attachments.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.attachments.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.attachments.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.attachments.content_disposition` |  | `inline` renders within the body; `attachment` is a downloadable file. | `inline` 在正文内联渲染；`attachment` 为可下载文件。 |
| `resp.200.attachments.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.in_reply_to` |  | Identifier of the message this one is replying to, if any. | 该消息所回复的消息标识（如有）。 |
| `resp.200.references` |  | Identifiers of earlier messages in the thread, forming the reply chain. | 会话中较早消息的标识，构成回复链。 |
| `resp.200.headers` |  | Raw email headers of the message as key/value pairs. | 消息的原始邮件头，以键值对形式给出。 |
| `resp.200.size` |  | Total size of the thread in bytes. | 会话总大小，单位字节。 |
| `resp.200.updated_at` |  | Time the thread record was last updated. | 会话记录最后更新时间。 |
| `resp.200.created_at` |  | Time the thread was created. | 会话创建时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## delete

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Permanently deletes a message.<br><br>**CLI:**<br>```bash<br>agentmail inboxes:messages delete --inbox-id <inbox_id> --message-id <message_id><br>``` | Delete a resource identified by its path (inbox, draft, message, thread, or list entry). Returns an empty success response with no body. For threads, deletion moves the thread to trash unless the `permanent` query flag forces hard deletion. | 按路径删除资源（收件箱、草稿、消息、会话或名单条目）。成功时返回空响应、无响应体。对会话而言，默认移入回收站，除非通过 `permanent` 查询参数强制彻底删除。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource being deleted. | 被删除资源所属的收件箱标识。 |
| `param:message_id` |  | Identifier of the message to delete. | 要删除的消息标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## update

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:messages update --inbox-id <inbox_id> --message-id <message_id> --add-label read --remove-label unread<br>``` | Partially update an existing resource identified by its path. Only the fields present in the request body are changed; omitted fields keep their current values. Applies to inboxes, drafts, messages (label changes) and threads (label changes); the response shape mirrors the resource being updated. | 按路径标识对已有资源做部分更新。仅修改请求体中出现的字段，未提供的字段保持原值。适用于收件箱、草稿、消息（改标签）与会话（改标签）；响应结构与被更新资源对应。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource being updated. | 被更新资源所属的收件箱标识。 |
| `param:message_id` |  | Identifier of the message to update. | 要更新的消息标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.add_labels` | Label or labels to add to message. | Labels to attach. For threads, system labels are not allowed. | 要添加的标签。会话不允许使用系统标签。 |
| `req.remove_labels` | Label or labels to remove from message. | Labels to detach. For threads, system labels are not allowed and removal takes priority over additions of the same label. | 要移除的标签。会话不允许系统标签，且同名标签的移除优先于添加。 |
| `resp.200.message_id` |  | Identifier of the updated message. | 被更新消息的标识。 |
| `resp.200.labels` |  | The message's labels after the update is applied. | 更新生效后该消息的标签。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## list

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:drafts list --inbox-id <inbox_id><br>``` | List a collection of resources within an inbox (threads, messages, drafts, events, list entries) or all inboxes. Results are paginated via `limit` + `page_token` and returned newest-first by default. Use the various `include_*` flags to widen the result set to spam/blocked/trash items. | 列出收件箱内的某类资源（会话、消息、草稿、事件、名单条目）或全部收件箱。通过 `limit` + `page_token` 分页，默认按时间倒序返回。可用各 `include_*` 开关把垃圾邮件/被拦截/回收站项纳入结果。 |
| `param:inbox_id` |  | Identifier of the inbox whose resources are being listed. Omit only on the route that lists all inboxes. | 被列举资源所属的收件箱标识。仅在列出全部收件箱的路由上可不传。 |
| `param:limit` |  | Maximum number of items to return in one page. | 单页返回的最大条目数。 |
| `param:page_token` |  | Opaque cursor for the next page; pass back the `next_page_token` from the previous response to continue. | 下一页的不透明游标；把上次响应的 `next_page_token` 回传即可翻页。 |
| `param:labels` |  | Restrict results to items carrying all of the given labels. | 仅返回带有全部所给标签的条目。 |
| `param:before` |  | Return only items dated before this time, for time-window filtering. | 仅返回此时间之前的条目，用于时间窗筛选。 |
| `param:after` |  | Return only items dated after this time, for time-window filtering. | 仅返回此时间之后的条目，用于时间窗筛选。 |
| `param:ascending` |  | When true, return results oldest-first instead of the default newest-first. | 为真时按最早在前返回，覆盖默认的最新在前。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.200.count` |  | Number of items returned in this page. | 本页返回的条目数。 |
| `resp.200.limit` |  | The page-size limit that was applied to this response. | 本响应实际应用的分页大小上限。 |
| `resp.200.next_page_token` |  | Cursor for the next page; pass it back as `page_token`. Absent or null when there are no more pages. | 下一页游标；作为 `page_token` 回传。无更多页时缺省或为空。 |
| `resp.200.drafts` | Ordered by `updated_at` descending. | The page of drafts, ordered by `updated_at` descending. | 本页草稿，按 `updated_at` 倒序排列。 |
| `resp.200.drafts.inbox_id` |  | Identifier of the inbox that owns the draft. | 拥有该草稿的收件箱标识。 |
| `resp.200.drafts.draft_id` |  | Unique identifier of the draft. | 草稿的唯一标识。 |
| `resp.200.drafts.labels` |  | Labels applied to the draft. | 应用于该草稿的标签。 |
| `resp.200.drafts.to` |  | Primary recipient addresses of the draft. | 草稿的主要收件人地址。 |
| `resp.200.drafts.cc` |  | Carbon-copy recipient addresses of the draft. | 草稿的抄送（CC）收件人地址。 |
| `resp.200.drafts.bcc` |  | Blind carbon-copy recipient addresses of the draft. | 草稿的密送（BCC）收件人地址。 |
| `resp.200.drafts.subject` |  | Subject line of the draft. | 草稿主题。 |
| `resp.200.drafts.preview` |  | Short plain-text snippet of the draft body. | 草稿正文的简短纯文本片段。 |
| `resp.200.drafts.attachments` |  | Attachments included in the draft. | 草稿中包含的附件。 |
| `resp.200.drafts.attachments.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.drafts.attachments.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.drafts.attachments.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.drafts.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.drafts.attachments.content_disposition` |  | `inline` renders within the body; `attachment` is a downloadable file. | `inline` 在正文内联渲染；`attachment` 为可下载文件。 |
| `resp.200.drafts.attachments.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.drafts.in_reply_to` |  | Identifier of the message this draft replies to, if any. | 该草稿所回复的消息标识（如有）。 |
| `resp.200.drafts.send_status` |  | Schedule status of the draft: `scheduled` is queued for a future send, `sending` is in progress, `failed` means the scheduled send did not complete. | 草稿的定时发送状态：`scheduled` 已排队待发，`sending` 发送中，`failed` 定时发送未完成。 |
| `resp.200.drafts.send_at` |  | Scheduled send time of the draft. | 草稿的计划发送时间。 |
| `resp.200.drafts.updated_at` |  | Time the draft was last updated. | 草稿最后更新时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## create

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:drafts create --inbox-id <inbox_id> --to recipient@example.com --subject "Draft subject" --text "Draft body"<br>``` | Create a new resource: an inbox, a draft, or an allow/block list entry, depending on the route. The created object is returned in full, including server-assigned identifiers and timestamps. | 创建新资源：按路由创建收件箱、草稿或 allow/block 名单条目。返回创建后的完整对象，含服务端分配的标识与时间戳。 |
| `param:inbox_id` |  | Identifier of the inbox under which the resource is created (drafts and list entries). Omit on the route that creates a top-level inbox. | 在其下创建资源的收件箱标识（草稿与名单条目）。创建顶层收件箱的路由可不传。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.labels` |  | Labels to apply to the new draft. | 为新草稿应用的标签。 |
| `req.reply_to` |  | Reply-to addresses for the draft, when replies should go somewhere other than the sender. | 草稿的回复至地址（当回复应发往非发件人处时）。 |
| `req.to` |  | Primary recipient addresses for the draft. | 草稿的主要收件人地址。 |
| `req.cc` |  | Carbon-copy recipient addresses for the draft. | 草稿的抄送（CC）收件人地址。 |
| `req.bcc` |  | Blind carbon-copy recipient addresses for the draft. | 草稿的密送（BCC）收件人地址。 |
| `req.subject` |  | Subject line for the draft. | 草稿主题。 |
| `req.text` |  | Plain-text body of the draft. | 草稿的纯文本正文。 |
| `req.html` |  | HTML body of the draft. | 草稿的 HTML 正文。 |
| `req.attachments` | Attachments to include in draft. | Files to attach to the draft; provide each either inline as base64 `content` or as a fetchable `url`. | 随草稿附带的文件；每个附件以 base64 `content` 内联提供，或以可拉取的 `url` 提供。 |
| `req.attachments.filename` |  | Filename to give the attachment. | 为附件指定的文件名。 |
| `req.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `req.attachments.content_disposition` |  | `inline` to render within the body, `attachment` to offer as a download. | `inline` 在正文内联渲染，`attachment` 作为下载提供。 |
| `req.attachments.content_id` |  | Content-ID used to reference an inline attachment from the HTML body. | Content-ID，用于在 HTML 正文中引用内联附件。 |
| `req.attachments.content` | Base64 encoded content of attachment. | The attachment bytes, base64-encoded. Use this or `url`, not both. | 附件字节内容，base64 编码。与 `url` 二选一。 |
| `req.attachments.url` | URL to the attachment. | A URL the service fetches the attachment from. Use this or `content`, not both. | 服务据以拉取附件的 URL。与 `content` 二选一。 |
| `req.in_reply_to` |  | Identifier of a message this draft replies to, to keep it in the same thread. | 该草稿所回复的消息标识，用于保持同一会话。 |
| `req.send_at` |  | Time to schedule the draft for delayed sending. | 为草稿安排的定时延迟发送时间。 |
| `req.client_id` |  | Caller-supplied identifier for idempotency and your own correlation of the created resource. | 调用方自定义标识，用于幂等及对所创建资源的自有关联。 |
| `resp.200.inbox_id` |  | Identifier of the inbox the created resource belongs to. | 所创建资源所属的收件箱标识。 |
| `resp.200.draft_id` |  | Unique identifier of the created draft. | 所创建草稿的唯一标识。 |
| `resp.200.client_id` |  | Caller-supplied identifier echoed back on the created resource. | 回显在所创建资源上的调用方自定义标识。 |
| `resp.200.labels` |  | Labels applied to the created draft. | 应用于所创建草稿的标签。 |
| `resp.200.reply_to` |  | Reply-to addresses of the draft. | 草稿的回复至地址。 |
| `resp.200.to` |  | Primary recipient addresses of the draft. | 草稿的主要收件人地址。 |
| `resp.200.cc` |  | Carbon-copy recipient addresses of the draft. | 草稿的抄送（CC）收件人地址。 |
| `resp.200.bcc` |  | Blind carbon-copy recipient addresses of the draft. | 草稿的密送（BCC）收件人地址。 |
| `resp.200.subject` |  | Subject line of the draft. | 草稿主题。 |
| `resp.200.preview` |  | Short plain-text snippet of the draft body. | 草稿正文的简短纯文本片段。 |
| `resp.200.text` |  | Plain-text body of the draft. | 草稿的纯文本正文。 |
| `resp.200.html` |  | HTML body of the draft. | 草稿的 HTML 正文。 |
| `resp.200.attachments` |  | Attachments stored on the draft. | 草稿上保存的附件。 |
| `resp.200.attachments.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.attachments.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.attachments.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.attachments.content_disposition` |  | `inline` renders within the body; `attachment` is a downloadable file. | `inline` 在正文内联渲染；`attachment` 为可下载文件。 |
| `resp.200.attachments.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.in_reply_to` |  | Identifier of the message this draft replies to, if any. | 该草稿所回复的消息标识（如有）。 |
| `resp.200.references` | IDs of previous messages in thread. | Identifiers of earlier messages in the thread. | 会话中较早消息的标识。 |
| `resp.200.send_status` |  | Schedule status: `scheduled` queued for future send, `sending` in progress, `failed` send did not complete. | 定时状态：`scheduled` 已排队待发，`sending` 发送中，`failed` 发送未完成。 |
| `resp.200.send_at` |  | Scheduled send time of the draft. | 草稿的计划发送时间。 |
| `resp.200.updated_at` |  | Time the draft was last updated. | 草稿最后更新时间。 |
| `resp.200.created_at` | Time at which draft was created. | Time the resource was created. | 资源创建时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## list

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:messages list --inbox-id <inbox_id><br>``` | List a collection of resources within an inbox (threads, messages, drafts, events, list entries) or all inboxes. Results are paginated via `limit` + `page_token` and returned newest-first by default. Use the various `include_*` flags to widen the result set to spam/blocked/trash items. | 列出收件箱内的某类资源（会话、消息、草稿、事件、名单条目）或全部收件箱。通过 `limit` + `page_token` 分页，默认按时间倒序返回。可用各 `include_*` 开关把垃圾邮件/被拦截/回收站项纳入结果。 |
| `param:inbox_id` |  | Identifier of the inbox whose resources are being listed. Omit only on the route that lists all inboxes. | 被列举资源所属的收件箱标识。仅在列出全部收件箱的路由上可不传。 |
| `param:limit` |  | Maximum number of items to return in one page. | 单页返回的最大条目数。 |
| `param:page_token` |  | Opaque cursor for the next page; pass back the `next_page_token` from the previous response to continue. | 下一页的不透明游标；把上次响应的 `next_page_token` 回传即可翻页。 |
| `param:labels` |  | Restrict results to items carrying all of the given labels. | 仅返回带有全部所给标签的条目。 |
| `param:before` |  | Return only items dated before this time, for time-window filtering. | 仅返回此时间之前的条目，用于时间窗筛选。 |
| `param:after` |  | Return only items dated after this time, for time-window filtering. | 仅返回此时间之后的条目，用于时间窗筛选。 |
| `param:ascending` |  | When true, return results oldest-first instead of the default newest-first. | 为真时按最早在前返回，覆盖默认的最新在前。 |
| `param:include_spam` |  | When true, include items classified as spam in the results. | 为真时把判定为垃圾邮件的条目纳入结果。 |
| `param:include_blocked` |  | When true, include items from blocked senders in the results. | 为真时把来自被拦截发件人的条目纳入结果。 |
| `param:include_unauthenticated` |  | When true, include items that failed sender authentication (e.g. SPF/DKIM/DMARC). | 为真时把未通过发件人认证（如 SPF/DKIM/DMARC）的条目纳入结果。 |
| `param:include_trash` |  | When true, include items currently in trash. | 为真时把当前在回收站中的条目纳入结果。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.200.count` |  | Number of items returned in this page. | 本页返回的条目数。 |
| `resp.200.limit` |  | The page-size limit that was applied to this response. | 本响应实际应用的分页大小上限。 |
| `resp.200.next_page_token` |  | Cursor for the next page; pass it back as `page_token`. Absent or null when there are no more pages. | 下一页游标；作为 `page_token` 回传。无更多页时缺省或为空。 |
| `resp.200.messages` | Ordered by `timestamp` descending. | The page of messages, ordered by `timestamp` descending. | 本页消息，按 `timestamp` 倒序排列。 |
| `resp.200.messages.inbox_id` |  | Identifier of the inbox that owns the message. | 拥有该消息的收件箱标识。 |
| `resp.200.messages.thread_id` |  | Identifier of the thread the message belongs to. | 该消息所属会话的标识。 |
| `resp.200.messages.message_id` |  | Unique identifier of the message. | 消息的唯一标识。 |
| `resp.200.messages.labels` |  | Labels applied to the message. | 应用于该消息的标签。 |
| `resp.200.messages.timestamp` |  | Time the message was sent or drafted. | 消息发送或起草的时间。 |
| `resp.200.messages.from` |  | Sender address of the message. | 消息的发件人地址。 |
| `resp.200.messages.to` |  | Primary recipient addresses of the message. | 消息的主要收件人地址。 |
| `resp.200.messages.cc` |  | Carbon-copy recipient addresses. | 抄送（CC）收件人地址。 |
| `resp.200.messages.bcc` |  | Blind carbon-copy recipient addresses. | 密送（BCC）收件人地址。 |
| `resp.200.messages.subject` |  | Subject line of the message. | 消息主题。 |
| `resp.200.messages.preview` |  | Short plain-text snippet of the message body. | 消息正文的简短纯文本片段。 |
| `resp.200.messages.attachments` |  | Attachments carried by the message. | 消息携带的附件。 |
| `resp.200.messages.attachments.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.messages.attachments.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.messages.attachments.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.messages.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.messages.attachments.content_disposition` |  | `inline` renders within the body; `attachment` is a downloadable file. | `inline` 在正文内联渲染；`attachment` 为可下载文件。 |
| `resp.200.messages.attachments.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.messages.in_reply_to` |  | Identifier of the message this one replies to, if any. | 该消息所回复的消息标识（如有）。 |
| `resp.200.messages.references` |  | Identifiers of earlier messages in the thread, forming the reply chain. | 会话中较早消息的标识，构成回复链。 |
| `resp.200.messages.headers` |  | Raw email headers of the message as key/value pairs. | 消息的原始邮件头，以键值对形式给出。 |
| `resp.200.messages.size` |  | Size of the message in bytes. | 消息大小，单位字节。 |
| `resp.200.messages.updated_at` |  | Time the message was last updated. | 消息最后更新时间。 |
| `resp.200.messages.created_at` |  | Time the message was created. | 消息创建时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:lists get --inbox-id <inbox_id> --direction <direction> --type <type> --entry <entry><br>``` | Retrieve a single AgentMail resource by its path identifiers. The exact resource returned depends on the route: an inbox, a draft, a message, a thread, or a single allow/block list entry. The full object (including bodies, attachments and timestamps) is returned, so this is the canonical way to fetch the complete state of one item after listing. | 按路径标识获取单个 AgentMail 资源。返回对象的类型取决于路由：收件箱、草稿、消息、会话或单条 allow/block 名单条目。返回完整对象（含正文、附件与时间戳），是在列表查询后获取某一项完整状态的标准方式。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource. Obtain it from create (POST /agentmail/inboxes) or list (GET /agentmail/inboxes). | 拥有该资源的收件箱标识。可经 create (POST /agentmail/inboxes) 或 list (GET /agentmail/inboxes) 获取。 |
| `param:direction` |  | Which traffic direction the list entry governs: `send` filters outbound, `receive` filters inbound, `reply` filters replies. | 名单条目作用的流量方向：`send` 管出站，`receive` 管入站，`reply` 管回复。 |
| `param:type` |  | Whether the entry belongs to the allow list or the block list. | 条目属于 allow（放行）名单还是 block（拦截）名单。 |
| `param:entry` | Email address or domain. | The email address or domain that identifies the list entry to fetch. | 标识要获取的名单条目的邮箱地址或域名。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox. Send as `Bearer <api_key>`; keep it secret and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌。以 `Bearer <api_key>` 形式发送；务必保密，切勿明文记录。 |
| `resp.200.entry` | Email address or domain of list entry. | The email address or domain captured by the created list entry. | 所创建名单条目覆盖的邮箱地址或域名。 |
| `resp.200.organization_id` |  | Identifier of the organization that owns the list entry. | 拥有该名单条目的组织标识。 |
| `resp.200.reason` | Reason for adding the entry. | Reason recorded when the list entry was created. | 创建名单条目时记录的理由。 |
| `resp.200.direction` |  | Traffic direction the list entry governs: `send`, `receive`, or `reply`. | 名单条目作用的流量方向：`send`、`receive` 或 `reply`。 |
| `resp.200.list_type` |  | Whether the entry is on the `allow` or `block` list. | 条目位于 `allow` 还是 `block` 名单。 |
| `resp.200.entry_type` |  | Whether `entry` is an `email` address or a `domain`. | `entry` 是 `email` 地址还是 `domain` 域名。 |
| `resp.200.created_at` | Time at which entry was created. | Time the resource was created. | 资源创建时间。 |
| `resp.200.read_only` | Whether the entry is read-only and cannot be deleted via the API. | When true, the entry is platform-managed and cannot be deleted via the API. | 为真时条目由平台管理，无法通过 API 删除。 |
| `resp.200.pod_id` | ID of pod. | Identifier of the pod the resource belongs to. | 资源所属 pod 的标识。 |
| `resp.200.inbox_id` | ID of inbox, if entry is inbox-scoped. | Identifier of the inbox the created resource belongs to. | 所创建资源所属的收件箱标识。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## delete

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:lists delete --inbox-id <inbox_id> --direction <direction> --type <type> --entry <entry><br>``` | Delete a resource identified by its path (inbox, draft, message, thread, or list entry). Returns an empty success response with no body. For threads, deletion moves the thread to trash unless the `permanent` query flag forces hard deletion. | 按路径删除资源（收件箱、草稿、消息、会话或名单条目）。成功时返回空响应、无响应体。对会话而言，默认移入回收站，除非通过 `permanent` 查询参数强制彻底删除。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the resource being deleted. | 被删除资源所属的收件箱标识。 |
| `param:direction` |  | Traffic direction of the list entry to delete: `send`, `receive`, or `reply`. | 要删除的名单条目的流量方向：`send`、`receive` 或 `reply`。 |
| `param:type` |  | Whether the entry to delete is on the allow list or block list. | 要删除的条目位于 allow 名单还是 block 名单。 |
| `param:entry` | Email address or domain. | The email address or domain identifying the list entry to delete. | 标识要删除的名单条目的邮箱地址或域名。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## send

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:drafts send --inbox-id <inbox_id> --draft-id <draft_id><br>``` | Send an email message. Two routes share this operation: composing and sending a brand-new message from the inbox, or sending a previously saved draft by its `draft_id`. The response returns the resulting message and thread identifiers. | 发送邮件消息。两个路由共用此操作：从收件箱新建并发送全新消息，或按 `draft_id` 发送此前保存的草稿。响应返回生成的消息与会话标识。 |
| `param:inbox_id` |  | Identifier of the inbox sending the message. | 发送消息的收件箱标识。 |
| `param:draft_id` |  | Identifier of the draft to send, on the route that sends a saved draft. | 要发送的草稿标识（用于发送已保存草稿的路由）。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.add_labels` | Label or labels to add to message. | Labels to attach. For threads, system labels are not allowed. | 要添加的标签。会话不允许使用系统标签。 |
| `req.remove_labels` | Label or labels to remove from message. | Labels to detach. For threads, system labels are not allowed and removal takes priority over additions of the same label. | 要移除的标签。会话不允许系统标签，且同名标签的移除优先于添加。 |
| `resp.200.message_id` |  | Identifier of the reply message that was sent. | 已发送的回复消息标识。 |
| `resp.200.thread_id` |  | Identifier of the thread the reply was added to. | 回复加入的会话标识。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |
| `resp.403.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.403.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## query

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:metrics query --inbox-id <inbox_id><br>``` | Query aggregated activity metrics for an inbox over a time window, optionally bucketed by period and filtered by event type. Useful for dashboards and monitoring inbox throughput. | 在给定时间窗内查询某收件箱的聚合活动指标，可按周期分桶并按事件类型筛选。适用于看板与收件箱吞吐监控。 |
| `param:inbox_id` |  | Identifier of the inbox whose metrics are queried. | 被查询指标的收件箱标识。 |
| `param:event_types` |  | Restrict the metrics to these event types only. | 仅按这些事件类型统计指标。 |
| `param:start` |  | Start of the time window to aggregate over. | 聚合统计的时间窗起点。 |
| `param:end` |  | End of the time window to aggregate over. | 聚合统计的时间窗终点。 |
| `param:period` |  | Bucket size used to group metrics within the window (e.g. by day or hour). | 窗口内对指标分桶的粒度（如按天或按小时）。 |
| `param:limit` |  | Maximum number of metric buckets to return. | 返回的指标分桶数上限。 |
| `param:descending` |  | When true, return buckets newest-first. | 为真时按最新在前返回分桶。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |

## forward

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:messages forward --inbox-id <inbox_id> --message-id <message_id> --to recipient@example.com<br>``` | Forward an existing message to new recipients, preserving the original content and attachments. You supply the destination addresses and any additional body; the original message is referenced by its path `message_id`. | 将已有消息转发给新收件人，保留原始内容与附件。你提供目标地址及附加正文，原消息通过路径中的 `message_id` 引用。 |
| `param:inbox_id` |  | Identifier of the inbox forwarding the message. | 转发消息的收件箱标识。 |
| `param:message_id` |  | Identifier of the message to forward. | 要转发的消息标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.labels` |  | Labels to apply to the forwarded message. | 为转发消息应用的标签。 |
| `req.reply_to` |  | Reply-to addresses for the forwarded message. | 转发消息的回复至地址。 |
| `req.to` |  | Recipients to forward the message to. | 转发消息的目标收件人。 |
| `req.cc` |  | Carbon-copy recipients of the forward. | 转发的抄送（CC）收件人。 |
| `req.bcc` |  | Blind carbon-copy recipients of the forward. | 转发的密送（BCC）收件人。 |
| `req.subject` |  | Subject line of the forwarded message. | 转发消息的主题。 |
| `req.text` |  | Additional plain-text body to prepend to the forward. | 转发时附加在前的纯文本正文。 |
| `req.html` |  | Additional HTML body to prepend to the forward. | 转发时附加在前的 HTML 正文。 |
| `req.attachments` |  | Extra files to attach to the forward; provide each as base64 `content` or a fetchable `url`. | 转发时附带的额外文件；每个以 base64 `content` 或可拉取 `url` 提供。 |
| `req.attachments.filename` |  | Filename to give the attachment. | 为附件指定的文件名。 |
| `req.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `req.attachments.content_disposition` |  | `inline` to render within the body, `attachment` to offer as a download. | `inline` 在正文内联渲染，`attachment` 作为下载提供。 |
| `req.attachments.content_id` |  | Content-ID used to reference an inline attachment from the HTML body. | Content-ID，用于在 HTML 正文中引用内联附件。 |
| `req.attachments.content` | Base64 encoded content of attachment. | The attachment bytes, base64-encoded. Use this or `url`, not both. | 附件字节内容，base64 编码。与 `url` 二选一。 |
| `req.attachments.url` | URL to the attachment. | A URL the service fetches the attachment from. Use this or `content`, not both. | 服务据以拉取附件的 URL。与 `content` 二选一。 |
| `req.headers` |  | Additional raw email headers to set on the forwarded message. | 为转发消息设置的额外原始邮件头。 |
| `resp.200.message_id` |  | Identifier of the reply message that was sent. | 已发送的回复消息标识。 |
| `resp.200.thread_id` |  | Identifier of the thread the reply was added to. | 回复加入的会话标识。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |
| `resp.403.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.403.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get-raw

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:messages get-raw --inbox-id <inbox_id> --message-id <message_id><br>``` | Get a download link for the raw RFC 822 / MIME source of a message. The response is metadata plus a short-lived presigned URL pointing to the full raw bytes in object storage. | 获取某消息原始 RFC 822 / MIME 源的下载链接。响应包含元数据及一个指向对象存储中完整原始字节的短时效预签名 URL。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the message. | 拥有该消息的收件箱标识。 |
| `param:message_id` |  | Identifier of the message whose raw source is requested. | 请求原始源的消息标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.200.message_id` | ID of the message. | Identifier of the message the raw source belongs to. | 原始源所属的消息标识。 |
| `resp.200.size` | Size of the raw message in bytes. | Size of the raw message in bytes. | 原始邮件大小，单位字节。 |
| `resp.200.download_url` | S3 presigned URL to download the raw message. Expires at expires_at. | Presigned URL to download the raw RFC 822 source from object storage; it is short-lived and expires at `expires_at`. | 从对象存储下载原始 RFC 822 源的预签名 URL；时效短，于 `expires_at` 过期。 |
| `resp.200.expires_at` | Time at which the download URL expires. | Time after which the download URL stops working. | 下载 URL 失效的时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get-attachment

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:messages get-attachment --inbox-id <inbox_id> --message-id <message_id> --attachment-id <attachment_id><br>``` | Get a single attachment's metadata and a download URL. The attachment can be addressed through its parent message, thread, or draft; all three routes return the same attachment payload. | 获取单个附件的元数据与下载 URL。附件可经其所属消息、会话或草稿寻址，三种路由返回相同的附件结构。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the attachment. | 拥有该附件的收件箱标识。 |
| `param:message_id` |  | Identifier of the message the attachment belongs to, when addressing it via a message. | 经消息寻址时，附件所属的消息标识。 |
| `param:attachment_id` |  | Identifier of the attachment to fetch, as found on the parent message/thread/draft. | 要获取的附件标识，取自其所属消息/会话/草稿。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.200.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.content_disposition` |  | `inline` if the attachment is meant to render within the body, `attachment` if it is a standalone download. | `inline` 表示应在正文内联渲染，`attachment` 表示为独立下载。 |
| `resp.200.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.download_url` | URL to download the attachment. | Presigned URL to download the attachment bytes; short-lived, expiring at `expires_at`. | 下载附件字节的预签名 URL；时效短，于 `expires_at` 过期。 |
| `resp.200.expires_at` | Time at which the download URL expires. | Time after which the download URL stops working. | 下载 URL 失效的时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## list

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes list<br>``` | List a collection of resources within an inbox (threads, messages, drafts, events, list entries) or all inboxes. Results are paginated via `limit` + `page_token` and returned newest-first by default. Use the various `include_*` flags to widen the result set to spam/blocked/trash items. | 列出收件箱内的某类资源（会话、消息、草稿、事件、名单条目）或全部收件箱。通过 `limit` + `page_token` 分页，默认按时间倒序返回。可用各 `include_*` 开关把垃圾邮件/被拦截/回收站项纳入结果。 |
| `param:limit` |  | Maximum number of items to return in one page. | 单页返回的最大条目数。 |
| `param:page_token` |  | Opaque cursor for the next page; pass back the `next_page_token` from the previous response to continue. | 下一页的不透明游标；把上次响应的 `next_page_token` 回传即可翻页。 |
| `param:ascending` |  | When true, return results oldest-first instead of the default newest-first. | 为真时按最早在前返回，覆盖默认的最新在前。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.200.count` |  | Number of items returned in this page. | 本页返回的条目数。 |
| `resp.200.limit` |  | The page-size limit that was applied to this response. | 本响应实际应用的分页大小上限。 |
| `resp.200.next_page_token` |  | Cursor for the next page; pass it back as `page_token`. Absent or null when there are no more pages. | 下一页游标；作为 `page_token` 回传。无更多页时缺省或为空。 |
| `resp.200.inboxes` | Ordered by `created_at` descending. | The page of inboxes, ordered by `created_at` descending. | 本页收件箱，按 `created_at` 倒序排列。 |
| `resp.200.inboxes.pod_id` |  | Identifier of the pod the resource belongs to. | 资源所属 pod 的标识。 |
| `resp.200.inboxes.inbox_id` |  | Identifier of the inbox the created resource belongs to. | 所创建资源所属的收件箱标识。 |
| `resp.200.inboxes.email` |  | Full email address of the created inbox. | 所创建收件箱的完整邮箱地址。 |
| `resp.200.inboxes.display_name` |  | Display name of the created inbox. | 所创建收件箱的显示名。 |
| `resp.200.inboxes.client_id` |  | Caller-supplied identifier echoed back on the created resource. | 回显在所创建资源上的调用方自定义标识。 |
| `resp.200.inboxes.metadata` | Custom metadata attached to the inbox. | Custom metadata attached to the created inbox. | 附加在所创建收件箱上的自定义元数据。 |
| `resp.200.inboxes.updated_at` | Time at which inbox was last updated. | Time the draft was last updated. | 草稿最后更新时间。 |
| `resp.200.inboxes.created_at` | Time at which inbox was created. | Time the resource was created. | 资源创建时间。 |

## create

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes create --display-name "My Agent" --username myagent --domain agentmail.to<br>``` | Create a new resource: an inbox, a draft, or an allow/block list entry, depending on the route. The created object is returned in full, including server-assigned identifiers and timestamps. | 创建新资源：按路由创建收件箱、草稿或 allow/block 名单条目。返回创建后的完整对象，含服务端分配的标识与时间戳。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.username` | Username of address. Randomly generated if not specified. | Local part of the new inbox's address; a random value is generated when omitted. | 新收件箱地址的用户名部分；不传时随机生成。 |
| `req.domain` | Domain of address. Must be verified domain. Defaults to `agentmail.to`. | Domain for the new inbox's address; must be a verified domain, otherwise the platform default is used. | 新收件箱地址的域名；必须是已验证域名，否则使用平台默认域名。 |
| `req.display_name` |  | Display name shown on mail sent from the new inbox. | 新收件箱发件时展示的显示名。 |
| `req.client_id` |  | Caller-supplied identifier for idempotency and your own correlation of the created resource. | 调用方自定义标识，用于幂等及对所创建资源的自有关联。 |
| `req.metadata` | Custom metadata to attach to the inbox. | Custom key/value metadata to attach to the new inbox. | 附加在新收件箱上的自定义键值元数据。 |
| `resp.200.pod_id` |  | Identifier of the pod the resource belongs to. | 资源所属 pod 的标识。 |
| `resp.200.inbox_id` |  | Identifier of the inbox the created resource belongs to. | 所创建资源所属的收件箱标识。 |
| `resp.200.email` |  | Full email address of the created inbox. | 所创建收件箱的完整邮箱地址。 |
| `resp.200.display_name` |  | Display name of the created inbox. | 所创建收件箱的显示名。 |
| `resp.200.client_id` |  | Caller-supplied identifier echoed back on the created resource. | 回显在所创建资源上的调用方自定义标识。 |
| `resp.200.metadata` | Custom metadata attached to the inbox. | Custom metadata attached to the created inbox. | 附加在所创建收件箱上的自定义元数据。 |
| `resp.200.updated_at` | Time at which inbox was last updated. | Time the draft was last updated. | 草稿最后更新时间。 |
| `resp.200.created_at` | Time at which inbox was created. | Time the resource was created. | 资源创建时间。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |

## reply

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:messages reply --inbox-id <inbox_id> --message-id <message_id> --text "Reply text"<br>``` | Reply to a message, threading onto the original conversation. By default the reply goes to the original sender; set the request's `reply_all` flag to include all original recipients instead. | 回复某条消息并接续到原会话。默认仅回复原发件人；将请求中的 `reply_all` 置为真则改为回复全部原收件人。 |
| `param:inbox_id` |  | Identifier of the inbox sending the reply. | 发送回复的收件箱标识。 |
| `param:message_id` |  | Identifier of the message being replied to. | 被回复的消息标识。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.labels` |  | Labels to apply to the reply message. | 为回复消息应用的标签。 |
| `req.reply_to` |  | Reply-to addresses for the reply message. | 回复消息的回复至地址。 |
| `req.to` |  | Override the recipient addresses for the reply, instead of deriving them from the original message. | 覆盖回复的收件人地址，而非从原消息推导。 |
| `req.cc` |  | Override the carbon-copy addresses for the reply. | 覆盖回复的抄送（CC）地址。 |
| `req.bcc` |  | Override the blind carbon-copy addresses for the reply. | 覆盖回复的密送（BCC）地址。 |
| `req.reply_all` |  | When true, address the reply to all original recipients (To/Cc) instead of only the original sender. | 为真时把回复发给全部原收件人（To/Cc），而非仅原发件人。 |
| `req.text` |  | Plain-text body of the reply. | 回复的纯文本正文。 |
| `req.html` |  | HTML body of the reply. | 回复的 HTML 正文。 |
| `req.attachments` |  | Files to attach to the reply; provide each as base64 `content` or a fetchable `url`. | 随回复附带的文件；每个以 base64 `content` 或可拉取 `url` 提供。 |
| `req.attachments.filename` |  | Filename to give the attachment. | 为附件指定的文件名。 |
| `req.attachments.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `req.attachments.content_disposition` |  | `inline` to render within the body, `attachment` to offer as a download. | `inline` 在正文内联渲染，`attachment` 作为下载提供。 |
| `req.attachments.content_id` |  | Content-ID used to reference an inline attachment from the HTML body. | Content-ID，用于在 HTML 正文中引用内联附件。 |
| `req.attachments.content` | Base64 encoded content of attachment. | The attachment bytes, base64-encoded. Use this or `url`, not both. | 附件字节内容，base64 编码。与 `url` 二选一。 |
| `req.attachments.url` | URL to the attachment. | A URL the service fetches the attachment from. Use this or `content`, not both. | 服务据以拉取附件的 URL。与 `content` 二选一。 |
| `req.headers` |  | Additional raw email headers to set on the reply. | 为回复设置的额外原始邮件头。 |
| `resp.200.message_id` |  | Identifier of the reply message that was sent. | 已发送的回复消息标识。 |
| `resp.200.thread_id` |  | Identifier of the thread the reply was added to. | 回复加入的会话标识。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |
| `resp.403.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.403.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## get-attachment

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:threads get-attachment --inbox-id <inbox_id> --thread-id <thread_id> --attachment-id <attachment_id><br>``` | Get a single attachment's metadata and a download URL. The attachment can be addressed through its parent message, thread, or draft; all three routes return the same attachment payload. | 获取单个附件的元数据与下载 URL。附件可经其所属消息、会话或草稿寻址，三种路由返回相同的附件结构。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the attachment. | 拥有该附件的收件箱标识。 |
| `param:thread_id` |  | Identifier of the thread the attachment belongs to, when addressing it via a thread. | 经会话寻址时，附件所属的会话标识。 |
| `param:attachment_id` |  | Identifier of the attachment to fetch, as found on the parent message/thread/draft. | 要获取的附件标识，取自其所属消息/会话/草稿。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.200.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.content_disposition` |  | `inline` if the attachment is meant to render within the body, `attachment` if it is a standalone download. | `inline` 表示应在正文内联渲染，`attachment` 表示为独立下载。 |
| `resp.200.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.download_url` | URL to download the attachment. | Presigned URL to download the attachment bytes; short-lived, expiring at `expires_at`. | 下载附件字节的预签名 URL；时效短，于 `expires_at` 过期。 |
| `resp.200.expires_at` | Time at which the download URL expires. | Time after which the download URL stops working. | 下载 URL 失效的时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

## list

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:lists list --inbox-id <inbox_id> --direction <direction> --type <type><br>``` | List a collection of resources within an inbox (threads, messages, drafts, events, list entries) or all inboxes. Results are paginated via `limit` + `page_token` and returned newest-first by default. Use the various `include_*` flags to widen the result set to spam/blocked/trash items. | 列出收件箱内的某类资源（会话、消息、草稿、事件、名单条目）或全部收件箱。通过 `limit` + `page_token` 分页，默认按时间倒序返回。可用各 `include_*` 开关把垃圾邮件/被拦截/回收站项纳入结果。 |
| `param:inbox_id` |  | Identifier of the inbox whose resources are being listed. Omit only on the route that lists all inboxes. | 被列举资源所属的收件箱标识。仅在列出全部收件箱的路由上可不传。 |
| `param:direction` |  | When listing list entries, restrict to this traffic direction: `send`, `receive`, or `reply`. | 列举名单条目时，限定此流量方向：`send`、`receive` 或 `reply`。 |
| `param:type` |  | When listing list entries, restrict to the allow list or block list. | 列举名单条目时，限定 allow 名单或 block 名单。 |
| `param:limit` |  | Maximum number of items to return in one page. | 单页返回的最大条目数。 |
| `param:page_token` |  | Opaque cursor for the next page; pass back the `next_page_token` from the previous response to continue. | 下一页的不透明游标；把上次响应的 `next_page_token` 回传即可翻页。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.200.count` |  | Number of items returned in this page. | 本页返回的条目数。 |
| `resp.200.limit` |  | The page-size limit that was applied to this response. | 本响应实际应用的分页大小上限。 |
| `resp.200.next_page_token` |  | Cursor for the next page; pass it back as `page_token`. Absent or null when there are no more pages. | 下一页游标；作为 `page_token` 回传。无更多页时缺省或为空。 |
| `resp.200.entries` | Ordered by entry ascending. | The page of list entries, ordered by entry value ascending. | 本页名单条目，按条目值升序排列。 |
| `resp.200.entries.entry` | Email address or domain of list entry. | The email address or domain captured by the created list entry. | 所创建名单条目覆盖的邮箱地址或域名。 |
| `resp.200.entries.organization_id` |  | Identifier of the organization that owns the list entry. | 拥有该名单条目的组织标识。 |
| `resp.200.entries.reason` | Reason for adding the entry. | Reason recorded when the list entry was created. | 创建名单条目时记录的理由。 |
| `resp.200.entries.direction` |  | Traffic direction the list entry governs: `send`, `receive`, or `reply`. | 名单条目作用的流量方向：`send`、`receive` 或 `reply`。 |
| `resp.200.entries.list_type` |  | Whether the entry is on the `allow` or `block` list. | 条目位于 `allow` 还是 `block` 名单。 |
| `resp.200.entries.entry_type` |  | Whether `entry` is an `email` address or a `domain`. | `entry` 是 `email` 地址还是 `domain` 域名。 |
| `resp.200.entries.created_at` | Time at which entry was created. | Time the resource was created. | 资源创建时间。 |
| `resp.200.entries.read_only` | Whether the entry is read-only and cannot be deleted via the API. | When true, the entry is platform-managed and cannot be deleted via the API. | 为真时条目由平台管理，无法通过 API 删除。 |
| `resp.200.entries.pod_id` | ID of pod. | Identifier of the pod the resource belongs to. | 资源所属 pod 的标识。 |
| `resp.200.entries.inbox_id` | ID of inbox, if entry is inbox-scoped. | Identifier of the inbox the created resource belongs to. | 所创建资源所属的收件箱标识。 |

## create

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:lists create --inbox-id <inbox_id> --direction <direction> --type <type> --entry user@example.com<br>``` | Create a new resource: an inbox, a draft, or an allow/block list entry, depending on the route. The created object is returned in full, including server-assigned identifiers and timestamps. | 创建新资源：按路由创建收件箱、草稿或 allow/block 名单条目。返回创建后的完整对象，含服务端分配的标识与时间戳。 |
| `param:inbox_id` |  | Identifier of the inbox under which the resource is created (drafts and list entries). Omit on the route that creates a top-level inbox. | 在其下创建资源的收件箱标识（草稿与名单条目）。创建顶层收件箱的路由可不传。 |
| `param:direction` |  | When creating a list entry, the traffic direction it should govern: `send`, `receive`, or `reply`. | 创建名单条目时，其作用的流量方向：`send`、`receive` 或 `reply`。 |
| `param:type` |  | When creating a list entry, whether it goes on the allow list or block list. | 创建名单条目时，加入 allow 名单还是 block 名单。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `req.entry` | Email address or domain to add. | The email address or domain to add to the allow/block list. | 要加入 allow/block 名单的邮箱地址或域名。 |
| `req.reason` | Reason for adding the entry. | Free-text reason recorded with the list entry. | 随名单条目记录的文字理由。 |
| `resp.200.entry` | Email address or domain of list entry. | The email address or domain captured by the created list entry. | 所创建名单条目覆盖的邮箱地址或域名。 |
| `resp.200.organization_id` |  | Identifier of the organization that owns the list entry. | 拥有该名单条目的组织标识。 |
| `resp.200.reason` | Reason for adding the entry. | Reason recorded when the list entry was created. | 创建名单条目时记录的理由。 |
| `resp.200.direction` |  | Traffic direction the list entry governs: `send`, `receive`, or `reply`. | 名单条目作用的流量方向：`send`、`receive` 或 `reply`。 |
| `resp.200.list_type` |  | Whether the entry is on the `allow` or `block` list. | 条目位于 `allow` 还是 `block` 名单。 |
| `resp.200.entry_type` |  | Whether `entry` is an `email` address or a `domain`. | `entry` 是 `email` 地址还是 `domain` 域名。 |
| `resp.200.created_at` | Time at which entry was created. | Time the resource was created. | 资源创建时间。 |
| `resp.200.read_only` | Whether the entry is read-only and cannot be deleted via the API. | When true, the entry is platform-managed and cannot be deleted via the API. | 为真时条目由平台管理，无法通过 API 删除。 |
| `resp.200.pod_id` | ID of pod. | Identifier of the pod the resource belongs to. | 资源所属 pod 的标识。 |
| `resp.200.inbox_id` | ID of inbox, if entry is inbox-scoped. | Identifier of the inbox the created resource belongs to. | 所创建资源所属的收件箱标识。 |
| `resp.400.name` |  | Machine-readable name of the validation error. | 机器可读的校验错误名。 |
| `resp.400.errors` | Validation errors. | Per-field validation problems describing which inputs were rejected and why. | 逐字段的校验问题，说明哪些输入被拒及原因。 |

## get-attachment

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | **CLI:**<br>```bash<br>agentmail inboxes:drafts get-attachment --inbox-id <inbox_id> --draft-id <draft_id> --attachment-id <attachment_id><br>``` | Get a single attachment's metadata and a download URL. The attachment can be addressed through its parent message, thread, or draft; all three routes return the same attachment payload. | 获取单个附件的元数据与下载 URL。附件可经其所属消息、会话或草稿寻址，三种路由返回相同的附件结构。 |
| `param:inbox_id` |  | Identifier of the inbox that owns the attachment. | 拥有该附件的收件箱标识。 |
| `param:draft_id` |  | Identifier of the draft the attachment belongs to, when addressing it via a draft. | 经草稿寻址时，附件所属的草稿标识。 |
| `param:attachment_id` |  | Identifier of the attachment to fetch, as found on the parent message/thread/draft. | 要获取的附件标识，取自其所属消息/会话/草稿。 |
| `param:Authorization` | Bearer authentication | Bearer token granting access to the inbox; send as `Bearer <api_key>` and never log it in clear text. | 授予收件箱访问权限的 Bearer 令牌；以 `Bearer <api_key>` 发送，切勿明文记录。 |
| `resp.200.attachment_id` |  | Identifier of the attachment. | 附件标识。 |
| `resp.200.filename` |  | Original filename of the attachment. | 附件原始文件名。 |
| `resp.200.size` |  | Size of the attachment in bytes. | 附件大小，单位字节。 |
| `resp.200.content_type` |  | MIME content type of the attachment. | 附件的 MIME 内容类型。 |
| `resp.200.content_disposition` |  | `inline` if the attachment is meant to render within the body, `attachment` if it is a standalone download. | `inline` 表示应在正文内联渲染，`attachment` 表示为独立下载。 |
| `resp.200.content_id` |  | Content-ID for referencing an inline attachment from HTML. | Content-ID，用于从 HTML 引用内联附件。 |
| `resp.200.download_url` | URL to download the attachment. | Presigned URL to download the attachment bytes; short-lived, expiring at `expires_at`. | 下载附件字节的预签名 URL；时效短，于 `expires_at` 过期。 |
| `resp.200.expires_at` | Time at which the download URL expires. | Time after which the download URL stops working. | 下载 URL 失效的时间。 |
| `resp.404.name` |  | Machine-readable name of the error, identifying the failure category (e.g. resource not found). | 机器可读的错误名，标识失败类别（如资源不存在）。 |
| `resp.404.message` |  | Human-readable explanation of what went wrong. | 对错误原因的可读说明。 |

