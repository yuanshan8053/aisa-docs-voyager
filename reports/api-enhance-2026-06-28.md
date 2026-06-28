# 报告乙：AIsa API 内容加强

> 读完这份报告要能决断一件事——把 31 份 OpenAPI spec 走「双字段加强 + 只增不改」这条路，到底改了什么、改好还是改坏、能不能放心铺开上线。
>
> 元信息：日期 2026-06-28 ｜ 源仓库 `AIsa-team/docs`，pinned commit `16863d3` ｜ 路线 v2 双字段（加强英文 `desc_en` + 中文本地化 `title_zh`，见决策 D-015/D-016）｜ 覆盖 **31 份 spec / 667 个 operation / 18,290 个对外字段 / 109 条主动批注** ｜ 两道确定性闸门：原生保全 `check_native_preserved.py`（exit 0）+ 对照表完整性 `make_review.py --require both`（missing 0）｜ 一键复现：`python3 ws-v2/central_accept.py`（exit 0 = 31/31 全绿）。

---

## 一、执行摘要:线上 API 正文是 spec 渲染产物,我们在这条管线上只增不改地把它写好,且每一处改动都可机器对账

**情境**：AIsa 是 OpenAI 兼容的 AI 能力网关，它的线上 API 参考页同时服务人和 Agent。**冲突**：这些参考页的正文不是手写文档，而是由 OpenAPI spec 自动渲染——spec 里的字段描述贫瘠、大量字段干脆没有描述，且全程无中文，渲染出来的页面也就跟着贫瘠。**问题**：能不能在不改动源 spec 原生结构的前提下，把这些描述系统性补好、补上中文，并且让产品负责人一眼看清「改了什么、改好还是改坏」？**答案**：能，而且已全量做完并通过机器验收。

本阶段在已查清的生产管线上提供一种**可对账的双字段加强能力**：逐字段撰写「加强英文 `desc_en` + 中文本地化 `title_zh`」，经确定性工具以 `x-doc` 命名空间**加性注入**进 spec（原生字段一个字符不动），产出增强 spec `enhanced.json`，再抽取成「源英文 → 加强英文 → 中文」三栏对照表供逐字段核对。

全量 31 份 spec 给出一致结论：

- **规模真实、覆盖完整**：667 个 operation、18,290 个对外字段全部补齐双字段描述，给每个接口补上「解决什么问题、何时用、怎么鉴权」，给每个字段补上「传什么值、为什么传、不传会怎样」。
- **改动只增不改,且可证**：31 份 spec 的原生 `paths` / 类型 / `$ref` / `required` / 枚举一个字符未动；原生保全闸门 31/31 exit 0，落盘产物与从源 spec 现场重算逐字节一致。
- **两道确定性闸门全绿**：原生保全 31/31 exit 0、对照表完整性 31/31 missing 0（每个对外字段都齐备 `desc_en`+`title_zh`，杜绝偷懒漏写），构成可一键复跑的验收证据。
- **拒绝杜撰,硬事实缺口显式留痕**：源 spec 没声明的事（比率是百分数还是小数、内部标志含义、哈希取值范围等）一律转成 **109 条批注**交研发确认，绝不编造。

**单一主张**：这条管线让 API 文档从源头变好、且让「改了什么、改好还是改坏」逐字段可对账、可一键复算。**最高优先级建议**：把这套加强从一次性产物升级为常态能力——让 spec 的描述成为发布门禁的一部分，并把 109 条批注交研发补全后去批注、升级为确定描述。

---

## 二、发现的 API 生产管线:正文由 spec 自动渲染,故加强的落点必须是 spec 本身

线上 API 参考正文的生成链路是：源仓库 `openapi/*.json` → 部署层自动渲染 → `aisa.one` 参考页。页面正文的主体即 spec 本身（664 个参考页是桩页，frontmatter 指向 spec、正文由渲染层从 OpenAPI 内联生成，非手写）。这意味着「把文档写好」的真正杠杆是**把 spec 本身写好**，而不是去改某一张渲染页。

由此定下加强的落点与判读铁律：**加强内容必须落在 spec 里、可被任何正确的渲染器消费**。本路线刻意不以「渲染出来的页面」为交付物——权威呈现是可从增强 spec 直接抽取的三栏对照表（源英文 → 加强英文 → 中文本地化），它与渲染器解耦，换任何渲染器都能复用同一份加强成果。后续阶段五用投影法把这份成果投影进原生字段、产出干净标准的派生 spec 喂给 Scalar 渲染上线，正是这条判读铁律的兑现。

---

## 三、管线上提供的加强能力:x-doc 加性注入,双字段产出,两道闸门把关

加强能力由「写 → 注入 → 验」三步构成，每一步都守「只增不改」红线：

**1. 撰写双字段增强内容（`content.json`）。** 逐字段产出两个字段——加强英文 `desc_en`（在源英文基础上加强，源英文为空则从无到有写）+ 中文本地化 `title_zh`（据加强英文做地道中文，二者语义一致）。operation 级额外产 `heading_zh` + `description_zh` + `desc_en`。撰写严格遵循写作方法论：不套模板、不注水、不复制原生元数据、不确定的硬事实留批注。

**2. 加性注入 `x-doc` 命名空间（`enhanced.json`）。** 注入器把增强内容挂进每个节点的 `x-doc` 子树，**绝不改动**原生 `description` / `summary` / 类型 / 结构，也**不**把内联 schema 提升为具名 `$ref`（不 hoist）。原生骨架保持逐字节原样，加强是一层可逆的加性派生。

**3. 两道确定性闸门把关。**
- `check_native_preserved.py`：剥掉 `x-doc` 子树后与 pinned 源 spec 逐字段比对，原生零改动则 exit 0。
- `make_review.py --require both`：抽取三栏对照表，并强制每个对外字段都齐备 `desc_en`+`title_zh`，缺漏即非零退出，杜绝「假绿」漏写。

三栏对照表覆盖**接口级描述 + 参数 + 请求体字段 + 响应体字段**（不限于参数），逐字段并列「源英文（原生只读）→ 加强英文 → 中文」三态，让「改得更好还是更坏」一眼可判。

**人工内容永不被 AI 静默覆盖**：注入器内建 `source` 治理戳——凡标记 `source: human` 的字段，AI 重跑注入时原样保留、不同建议分流进审计而非覆盖。本次全量 31 份的加强内容均为本轮产出、无既有人工标记字段（`protected` 计数为 0），故没有任何人工内容被触及；该保护机制随工具内建，一旦未来引入人工撰写即自动生效。

---

## 四、能力的范畴与价值:31 份 spec 全覆盖,补的是机器结构说不清的业务语义

**覆盖范畴**：31 份 spec（30 份 AIsa 真实 spec + 1 份 OpenAPI 官方玩具示例 Plant Store）、667 个 operation、18,290 个对外字段，全部补齐双字段描述。超大档经确定性切片并发撰写后在全档上一次性重注入、复验——`dataforseo`（445 operation，切 13 片）、`agentmail`（46 operation，切 2 片），切片的字段键与全档一致、可无缝合并。

**加强了哪几类内容**：用途（这个接口/字段解决什么问题）、取值的业务含义（枚举值各代表什么、参数怎么取）、依赖关系（哪个字段要先开、谁约束谁）、易踩的坑（默认行为、边界）、以及源 spec 说不清的硬事实（转批注，不编造）。

**价值口径（可对账、不注水）**：
- **双字段语义一致**：加强英文与中文本地化一一对应、含义同步，不是把英文机翻成中文，而是据加强英文做地道中文。
- **只增不改、可逆**：原生 `description` / `summary` 只读零改动，三态（原生 / 加强英文 / 中文）并存可对账，加强随时可剥离还原。
- **完整性有机器门禁**：18,290 个对外字段无一漏写双字段，由 `make_review.py --require both` 强制。
- **拒绝杜撰有留痕**：109 条批注是「源码未声明、加强时拒绝编造」的硬事实缺口清单，可直接交研发。

---

## 五、典型实例效果展示:三态对比看「改得更好」,深层内联看「触达到位」,批注看「拒绝杜撰」

以下实例均为真实产物零改动摘录，可在对应 `ws-v2/<spec>/review_table.md` 逐字 Ctrl+F 命中。

**实例 1 · 从空白到讲清「为什么传」（`openai-chat` · `req.top_logprobs`）**

| 三态 | 内容 |
| --- | --- |
| 源英文（原生只读） | *（空）* |
| 加强英文 `desc_en` | How many of the most likely alternative tokens to report at each position, each with its log probability. Requires logprobs to be on. |
| 中文 `title_zh` | 每个位置上报多少个最可能的备选 token，并各带其对数概率。需先开启 logprobs。 |

源 spec 此字段无任何描述。加强不仅说清它是什么，还点出**跨字段依赖**（须先开 `logprobs`）——这正是 Agent 最容易踩、而机器结构表达不出的坑。

**实例 2 · 触达深层内联结构（`openai-chat` · `req.messages.content`,内联数组 + `oneOf` 分支）**

| 三态 | 内容 |
| --- | --- |
| 源英文（原生只读） | Can be a text string or an array (for image inputs). |
| 加强英文 `desc_en` | The payload of the turn. Pass a plain string for a text-only message, or an array of typed parts to mix text with image inputs for multimodal analysis. |
| 中文 `title_zh` | 本轮的内容载荷。纯文本消息传字符串；若要图文混排做多模态分析，则传一个带类型的分块数组。 |

该字段下还有 `content.type` / `content.text` / `content.image_url` 三个深层内联子字段，均被注入加强——证明加强不止触达顶层参数，也穿透内联数组与 `oneOf` 分支，覆盖嵌套结构。

**实例 3 · 原生保全:加强了,但原生一个字符没动**

`openai-chat` 的接口级原生描述 `Generate chat responses with support for images, streaming, function calling, and logprobs.` 在 `enhanced.json` 中**原样保留**；加强后的更详尽英文写在 `x-doc.desc_en`、中文写在 `x-doc.title_zh`，三者并存。`check_native_preserved.py` 对 31 份 spec 全部 exit 0，机器级坐实「只增不改」。

**实例 4 · 拒绝杜撰,硬事实转批注（`openapi-financial` · `resp.200.free_cash_flow_yield`）**

| 三态 | 内容 |
| --- | --- |
| 源英文（原生只读） | Free cash flow yield. |
| 加强英文 `desc_en` | Free cash flow relative to market capitalization.<br>[⚠️Note：源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |
| 中文 `title_zh` | 自由现金流相对于市值的收益率。<br>[⚠️批注：源码未声明该比率/百分比字段是以百分数（如 25.3）还是小数（如 0.253）返回，待研发确认。] |

源 spec 没说这个比率字段返回百分数还是小数——这是会直接坑到 Agent 计算的硬事实。加强没有猜，而是显式留批注交研发。全量共 **109 条**这类批注，集中在 `openapi-financial`（30 条）、`dataforseo`（22 条）、`apollo`（20 条）。`apollo` 的 `param:hashed_email` 同理：源码只举了 MD5 与 SHA-256 两例、未声明是否支持其他取值，故留批注待确认。

---

## 六、完整产物附录:每份 spec 五件套 + 两道闸门状态总表 + 一键复现

**每份 spec 的产物（落 `ws-v2/<spec名>/`,无渲染 md）**：
- `content.json`——人工撰写的双字段增强内容（`desc_en` + `title_zh`）
- `enhanced.json`——注入 `x-doc` 后的增强 spec（原生零改动）
- `review_table.md` + `.json`——三栏对照表（源英文 → 加强英文 → 中文）
- `inject_review.json`——注入审计（解析/未解析/批注计数）

**两道闸门状态总表(31/31 全绿,`python3 ws-v2/central_accept.py` 一键复跑)**：

| 验收项 | 结果 |
| --- | --- |
| 原生保全 `check_native_preserved.py` | 31/31 exit 0 |
| 对照表完整性 `make_review.py --require both` | 31/31 missing 0 |
| 落盘产物 vs 源 spec 现场重算 | 31/31 逐字节一致 |
| 总 operation | 667 |
| 总对外字段 | 18,290 |
| 主动批注（待研发确认） | 109 |
| 被保护人工字段 / 误覆盖 | 0 / 0 |

**规模分布要点**：字段量集中在 `dataforseo`（13,816）、`agentmail`（864）、`apollo`（506）、`openapi-financial`（498）；operation 量集中在 `dataforseo`（445）、`apollo`（54）、`agentmail`（46）。

**工程实情留痕(透明即可信)**：
- `agentmail` 源 spec 把 46 个 operation 复用为仅 12 个 operationId（多条 path 同名），合并用专用 `union_merge.py` 按 opKey + dotpath 深合并；其 `unresolved` 计数是「一份 content 块应用到该 operationId 下全部同名 path、非匹配兄弟 path 记为无害未解析」的源结构属性，**非缺陷**——判据是两道绑定闸门均绿、944 个实际字段全齐备，且 operationId 是不可改的原生结构。
- 工具链 `inject_xdoc.resolve_property` 修过一处一致性问题，使 `dataforseo` / `apollo` 把深层字段存成「含点号/方括号的扁平 property key」也能正确命中（最长字面量整键优先匹配），与对照表口径对齐；纯嵌套 schema 行为不变。

**与早期试点的差异**：本报告为**全量版**，覆盖全部 31 份 spec；早期 D-013 试点仅 2 份 spec、走 `enhanced.yaml` + spectral 的旧路线，已按 D-015 推翻，全量化以本 v2 双字段路线为准（旧试点产物保留作对照，不删）。

**复现命令**：
```bash
python3 ws-v2/central_accept.py            # exit 0 = 31/31 双闸门全绿(原生保全 + 完整性)
python3 ws-v2/extract_annotations.py       # → reports/annotations-for-dev-*.{md,csv}(109 条批注)
```
> 复现前提：源仓库副本在 `~/files/aisa-team-docs`（pinned `16863d3`）。
