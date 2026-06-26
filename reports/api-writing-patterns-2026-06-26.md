# API 文档专业写作实践：从源 spec 到加强描述的九个模式

> 受众：要写或评审 API 文档的人（研发、技术写作、文档负责人）。读完你能拿走一套可复用的「字段/接口描述怎么写才对读者有用」的判断标准，每条都配真实改写案例。
>
> 素材来源：AIsa 文档加强工程对 31 份 OpenAPI spec、667 个接口、18,290 个对外字段做的英文描述加强。下文每个「改前 / 改后」都是真实实例，改前取自源 spec 原生 `description`/`summary`，改后取自加强后的 `desc_en`。复现见 `ws-v2/dump_pairs.py`。

## 一、一条主线：好的字段描述回答的是「我该怎么用」，不是「它叫什么」

API 文档最常见的病，是把字段名换个说法重抄一遍——`category` 写成 "Category"，`revenue` 写成 "The estimated revenue"。读者本来就看得见字段名，这种描述等于没写。

真正有用的描述站在调用者一侧，回答四个问题里至少一个：**这个值传什么 / 为什么传 / 不传会怎样 / 拿到后能干什么**。本文把加强工程里反复出现的写法归纳成九个模式，前四个是「补什么信息」，中间三个是「写复杂字段的纪律」，最后两个是「克制与诚实」——后两条决定一份文档是专业还是注水。

下面每个模式给出定义、至少两个真实案例、以及为什么这么改（rationale）。

## 二、补信息的四个模式

### 模式 1 · 从无到有：源字段空白，补一句「它是什么、归属谁」

源 spec 里大量字段的 `description` 是空的，读者只能靠字段名猜。第一优先级是把空白填成一句确定的事实——说清这个值代表什么、隶属哪个实体。

| 改前 | 改后 |
| --- | --- |
| `pod_id` ——（空） | Identifier of the pod the resource belongs to. |
| `content_id` ——（空） | Content-ID used to reference an inline attachment from the HTML body (cid: links). |

**rationale**：空描述是最大的可用性缺口。补全时只写能从 schema 与上下文确证的事实（归属关系、ID 指向），不臆测业务规则。这是「有则搬、无则查、查不到则留批注」的第一步，也是覆盖面最大的一类改写（本工程约 1,300 个字段属此类）。

### 模式 2 · 标签扩写：把一两个词的「伪描述」展开成完整释义

比空白更隐蔽的是「标签式描述」——`Category` / `Bearer authentication` 这种把字段名原样复述的词。它看似有内容，实则零增量。

| 改前 | 改后 |
| --- | --- |
| `Authorization` —— "Bearer authentication" | Bearer token granting access to the inbox. Send as `Bearer <api_key>`; keep it secret and never log it in clear text. |
| `genesis_date` —— "coin genesis date" | Genesis (launch) date of the coin as an ISO 8601 timestamp; null when unknown. |

**rationale**：标签式描述骗过了「非空」检查却骗不过读者。扩写时补上调用者真正缺的信息——鉴权字段补「怎么传、注意保密」，日期字段补「什么格式、空值含义」。判断标准很简单：如果一句描述去掉后读者理解力没有任何损失，它就还没写完。

### 模式 3 · 补默认行为与省略后果：可选字段必须说「不传会怎样」

可选参数最该写、却最常漏的，是省略时的行为。读者决定「要不要传这个字段」，靠的正是这条信息。

| 改前 | 改后 |
| --- | --- |
| `username` —— "Username of address. Randomly generated if not specified." | Local part of the new inbox's address; a random value is generated when omitted. |
| `next_page_token` ——（空） | Cursor for the next page; pass it back as `page_token`. Absent or null when there are no more pages. |

**rationale**：「不传会怎样」是可选字段的决策依据。源里偶有提及（如 username 的 randomly generated）就保留并理顺；源里没有但能从分页语义确证的（token 用尽返回 null），补上;确证不了的绝不编默认值。注意 `next_page_token` 同时讲清了「拿它干什么（回传翻页）」和「边界（无下一页时为空）」——一个字段把用法和边界一次说全。

### 模式 4 · 补用途与下游：说清这个值「接下来喂给谁」

ID 类、token 类字段的价值在于它的「去向」——能拼成什么、传给哪个接口、驱动哪步操作。只说「它是个标识符」远不够。

| 改前 | 改后 |
| --- | --- |
| `attachment_id` ——（空） | Identifier of the attachment; pass it to get-attachment to obtain a download URL. |
| `video_id` ——（空） | YouTube's unique identifier for the video. Use it to build a watch URL or as the input to downstream video APIs. |

**rationale**：API 是接口的网络，字段往往是接口间的「接力棒」。点明下游用法，读者就能把单个接口串成工作流，而不必反复试错。改写只描述 spec 中确实存在的下游接口/用途，不虚构不存在的端点。

## 三、写复杂字段的三条纪律

### 模式 5 · 枚举写业务含义，不抄字面值

带固定取值的字段，描述的价值不是把枚举值再列一遍（那 schema 里已有），而是解释每个值意味着什么业务状态。

| 改前 | 改后 |
| --- | --- |
| `include_unauthenticated` ——（空） | When true, include items that failed sender authentication (e.g. SPF/DKIM/DMARC). |
| `period` ——（空） | Bucket size used to group metrics within the window (e.g. by day or hour). |

**rationale**：枚举字面量是机器可读的，业务含义才是人需要的。写「true 代表纳入未通过发件人认证的邮件」，比罗列 `true/false` 有用得多。红线：只写能确证含义的取值；含义不明的枚举（如 apollo 的若干 `category`）一律留批注「取值集合待研发确认」，绝不硬编一个臆想的语义。

### 模式 6 · 接口定位写「能力 + 场景 + 组合价值」

接口级描述（operation）最忌只把接口名复述一遍。好的接口描述让读者 30 秒判断「这个接口是不是我要找的」，并知道怎么和别的接口配合。

| 改前 | 改后 |
| --- | --- |
| `Analyst Estimates` | Return consensus Wall Street analyst estimates — projected revenue and earnings per share — for a single US stock ticker, broken down by fiscal period. This is a read-only query: pick annual or quarterly granularity and cap how many periods come back. |
| `Coins List (ID Map)` | List every coin tracked by CoinGecko with its ID, symbol and name... Use it to map a ticker symbol to the CoinGecko coin ID that the other endpoints require. |

**rationale**：接口描述是读者的导航。三件套——**能力**（返回什么）、**场景**（只读查询、按财季拆分）、**组合价值**（这个接口产出的 ID 是别的接口的入参）——让接口从孤立端点变成工作流的一环。CoinGecko 那条点出「先用我拿到 ID 再去调别的接口」，直接消除了新手最常踩的「ID 从哪来」的坑。

### 模式 7 · 跨字段关系：说清「它和谁配对、和谁互斥」

参数很少孤立存在——有的成对出现（min/max），有的互斥（二选一），有的必须与另一字段对齐。这层关系不写出来，读者只能靠报错来学。

| 改前 | 改后 |
| --- | --- |
| `revenue_range[min]` —— "The minimum revenue the person's current employer generates. Use this parameter in combina..." | Minimum revenue of the current employer; pair with revenue_range[max]. |
| `polymarket_market_slug` —— "The Polymarket market slug(s)..." | One or more Polymarket market slugs to find cross-platform equivalents for. Repeat the query parameter to pass several at once. Cannot be combined with `kalshi_event_ticker` — choose one. |

**rationale**：跨字段约束是「读文档能避免、不读就踩」的典型。点明「与 max 配对」「与 X 互斥，二选一」，把运行时才会暴露的 400 错误提前到阅读期。改写只陈述 spec 里确有的约束（互斥关系、配对关系），不推断 spec 未声明的隐性规则。

## 四、克制与诚实：决定专业度的两条

### 模式 8 · 自适应深度：自解释字段一句话，绝不注水

不是每个字段都要长篇大论。ID、布尔标志、时间戳这类自解释字段，一句话讲清即可；硬要扩写只会稀释信息密度。

| 改前 | 改后 |
| --- | --- |
| `title` ——（空） | The video's display title. |
| `link` ——（空） | Direct, clickable watch URL for the video. |

**rationale**：篇幅要与字段复杂度匹配。带单位、区间、跨字段依赖、默认行为的字段才值得展开（见模式 3/5/7）；`title`、`link` 这种一眼明了的，一句话就是最优解。注水（把简单字段硬撑成一段）和偷懒（把复杂字段一笔带过）是同一种病的两面——都没有站在读者需要多少信息的角度判断。

### 模式 9 · 不确定就留批注，绝不杜撰（绝对红线）

写文档最大的诱惑，是把「看起来合理」的内容补全成「看起来权威」。这恰恰是必须挡住的。源 spec 没声明清楚的硬事实——哈希算法取值、内部标志含义、运算符全集、金额单位——一律不编，转成显式批注。

| 字段 | 改后描述 + 批注 |
| --- | --- |
| `apollo` / `hashed_email` | Hashed email used to match without sending the plaintext address. `[⚠️Note: 源码未声明 MD5 与 SHA-256 之外的取值，详细哈希规范待研发确认。]` |
| `apollo` / `has_join` | Internal flag indicating a join was applied to the query. `[⚠️Note: 源码未声明该字段的业务含义，待研发确认。]` |

**rationale**：`hashed_email` 那条，一个想把文档写「完整」的人很容易顺手补一句「支持 MD5/SHA-256」——但 spec 没这么声明，这就是杜撰。改写的做法是：能确证的部分照写（用途是「不传明文匹配」），不能确证的部分显式标「待研发确认」。本工程 31 份 spec 共留下 109 条这样的批注（集中在 financial 30、dataforseo 22、apollo 20），每一条都是「宁可标注待确认，绝不编一个看似合理的值」的落地。诚实的留白比自信的错误对读者更有价值——错误会被当成事实传播，留白会驱动补全。

## 五、一句话收口

九个模式归到一条：**描述的受众是调用者，不是字段本身**。补空白、扩标签、讲默认、指下游，是在补调用者缺的信息；写枚举含义、接口定位、跨字段关系，是在帮调用者把接口串成工作流；自适应深度和留批注，是在守住「不浪费读者时间、不误导读者」的底线。对照这九条改写任意一份 API 文档，可用性都会有肉眼可见的提升。

---

> 复现：`python3 ws-v2/dump_pairs.py` 导出全部 17,550 对「原生 → 加强」对照到 `/tmp/pairs.jsonl`；`python3 ws-v2/find_examples.py` 按模式分桶捞取候选案例。本文案例均从中挑选，未做任何文字改动。
