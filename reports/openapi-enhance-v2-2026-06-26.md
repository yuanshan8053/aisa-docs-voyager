# OpenAPI 内容加强 · 阶段三全量执行报告（v2 双字段路线）

> 受众：AIsa 产品负责人。读完要能判断一件事——把 31 份 OpenAPI spec 做「双字段加强」这条路，全量铺开后到底改了什么、改好还是改坏、能不能放心交付。
>
> 执行范围：`openapi/` 下全部 **31 份 spec / 667 个 operation / 18,290 个对外字段**。路线：D-015 确定的 v2 本地双字段方案（加强英文 `desc_en` → 中文本地化 `title_zh`，不产渲染 md，三栏对照表为权威呈现）。技能：`skill-local/aisa-doc-enhance/`（standalone python3，零包外依赖）。日期：2026-06-26。

## 一、结论先行：全量 31 份 spec 双闸门全绿，源头零改动

线上 API 参考页的正文不是手写 Markdown，而是 OpenAPI spec 内联渲染出来的。所以「把文档写好」的真正杠杆，是**把 spec 本身写好**——在不动任何原生结构的前提下，给每个字段补上「这是干什么的、怎么用、有什么坑」，且让中英两层一眼可对照。

本阶段把试点验证过的双字段路线全量铺到了 31 份 spec。中央验收（trust-but-verify：不信任已落盘产物，从每份 `content.json` 在 pinned 源 spec `16863d3` 上**现场重算** `enhanced.json`，再过两道闸门）的成绩单是：

| 指标 | 数值 |
| --- | --- |
| spec 总数 | **31 / 31 全绿** |
| operation 总数 | 667 |
| 对外字段/参数总数 | 18,290 |
| 主动批注（待研发确认）总数 | 109 |
| 原生保全闸门 `check_native_preserved.py` | **31/31 exit 0**（零篡改） |
| 完整性闸门 `make_review.py --require both` | **31/31 missing=0**（每个对外字段都齐备 `desc_en`+`title_zh`） |
| 落盘 `enhanced.json` 与现场重算 | **31/31 字节一致**（产物可独立复现） |
| 源保护跳过 `protected_skipped` | 0（本轮无人工内容被触碰） |

两个数字是这次全量的底气：**原生保全闸门 31 份全 exit 0**——所有改动都是新增的 `x-doc` 子树，原生的 `paths` / 类型 / `$ref` / `required` / 枚举一个字符都没动；**完整性闸门 31 份全 missing=0**——18,290 个对外字段无一漏写，杜绝偷懒留空。第三道交叉验证（落盘产物 = 现场重算，字节一致）则坐实了「任何人拿 `content.json` + 源 spec 都能复现出同一份 `enhanced.json`」，产物不是一次性手工拼装的黑箱。

## 二、加强能力：双字段 + 主动批注，每层各有落点

把「加强」拆开，做的是三类性质不同、对应三种「机器结构说不清」问题的活：

- **接口级定位（operation）**：补 `heading_zh`（中文动作 + Action 名）、`description_zh`（能力 + 场景 + 鉴权）、必要时补 `errors` 错误码表。667 个 operation **全部齐备** `heading_zh` + `description_zh` + `desc_en`，零缺漏。源 spec 的 `summary` 往往只有一句英文，定位信息几乎为零。
- **字段级双字段释义（property / parameter）**：给每个对外字段写两层——**加强英文 `desc_en`**（在源英文基础上补「传什么值、为什么传、不传会怎样」）+ **中文本地化 `title_zh`**（据加强英文做地道中文，语义一致）。覆盖请求体、响应体（按状态码）、operation 参数三处，自动穿透数组 `items` / `oneOf` / `anyOf` / `allOf` / `$ref` 的深层内联结构。
- **边界与坑（主动批注，绝对红线）**：spec 没声明清楚的硬事实——哈希算法取值范围、内部标志的业务含义、运算符全集、单位/上限——**一律不编**，转成 `\n[⚠️批注:...待研发确认]`（中文）/ `\n[⚠️Note:...]`（英文）双语内联，显式标注「这里待研发确认」。全量共留下 **109 条批注**，集中在 `openapi-financial`（30）、`dataforseo`（22）、`apollo`（20）三份信息密度最高的 spec。

三类加强共同守住边界：**只增不改**（不动原生 `description`）、**不复制原生元数据进 `x-doc`**（字段名/类型/`required`/枚举字面/默认值不抄，但枚举的业务含义可写）、**不捏造**（不确定即批注）、**自适应深度**（ID/布尔/时间戳等自解释字段一句话，带单位/区间/跨字段依赖/默认行为的复杂字段才展开，不注水）。

## 三、下钻一：一个 `oneOf` 深层内联字段，从「空」到「一句人话」

挑最能说明穿透能力的字段放大看。`openai-chat` 的多模态消息体里，`content` 是一个 `oneOf`——既可以是纯文本字符串，也可以是「文本块 + 图像块」的数组。`image_url` 字段藏在 `oneOf[1] → items → properties → image_url` 这条深层内联路径里，源 spec 对它的描述是**空的**：

```
content/oneOf[1]/items/properties/image_url   →   description: (无)
```

一个开发者读到这里只知道「有这么个字段」，填什么、模型拿它干嘛，全靠猜。加强后的双字段是：

> **desc_en**：Location of the image for an image-type content part; the model fetches and analyzes it alongside the text part.
> **title_zh**：图像类型分块的图片地址；模型会拉取它并与文本分块一同分析。

价值不在翻译，而在**穿透**：`oneOf` 分支里的深层字段，普通遍历会漏掉、完整性闸门会「假绿」。本路线的注入器与对照表共用同一套 `descend_object` 穿透逻辑（试点阶段专门修过一次「`oneOf/anyOf/allOf` 不穿透致字段隐形」的假绿 bug），保证「注入器写了几个字段，对照表就核几个字段」，两者口径恒等——这是 18,290 个字段 missing=0 可信的根基。

## 四、下钻二：批注红线如何挡住一次「编一个看似合理的值」

`apollo` 的 `people/match` 接口有个 `hashed_email` 参数。源 spec 只说它是「用于匹配的邮箱哈希」，但**没声明支持哪些哈希算法**。一个想把文档写「完整」的人，很容易顺手补一句「支持 MD5 / SHA-256」——这正是要挡住的捏造。本轮的实际产出是：

> **desc_en**：Hashed email used to match without sending the plaintext address.
> `[⚠️Note: 源码未声明 MD5 与 SHA-256 之外的取值，详细哈希规范待研发确认。]`
> **title_zh**：邮箱哈希值，用于在不传明文邮箱的情况下匹配。
> `[⚠️批注: 源码未声明 MD5 与 SHA-256 之外的取值，详细哈希规范待研发确认。]`

同样地，`apollo` 的 `has_join` 是个内部标志、源码无业务说明，加强时如实写「内部标志，表示查询进行了 join」并批注「业务含义待研发确认」，没有硬编一个臆想的语义。109 条批注每一条都是「宁可标注待确认，绝不杜撰」的落地——这是用户定的绝对红线，全量执行无一处违反。

## 五、完整产物清单：每份 spec 五件套 + 双闸门状态

每份 spec 落盘五件套（**无任何渲染 md**，权威呈现是可抽取的三栏对照表 `review_table.md`）：`content.json`（双字段源稿）+ `enhanced.json`（注入 `x-doc` 后的增强 spec，原生零改动）+ `review_table.md` / `.json`（三栏对照表「源英文 → 加强英文 → 中文」+ 完整性闸门）+ `inject_review.json`（注入审计）。全部落 `ws-v2/<spec名>/`。

| spec | ops | 字段 | 批注 | 双闸门 |
| --- | --- | --- | --- | --- |
| dataforseo | 445 | 13,816 | 22 | ✅ |
| agentmail | 46 | 864 | 0 | ✅ |
| apollo | 54 | 506 | 20 | ✅ |
| openapi-financial | 19 | 498 | 30 | ✅ |
| twitter-communities | 5 | 376 | 4 | ✅ |
| polymarket-openapi | 10 | 267 | 3 | ✅ |
| coingecko | 21 | 260 | 1 | ✅ |
| twitter-tweet-batch_01 | 4 | 245 | 6 | ✅ |
| twitter-user-batch_01 | 6 | 192 | 7 | ✅ |
| twitter-tweet-batch_02 | 3 | 184 | 4 | ✅ |
| twitter-user-batch_02 | 5 | 181 | 0 | ✅ |
| twitter-list | 3 | 169 | 0 | ✅ |
| perplexity-openapi | 4 | 148 | 4 | ✅ |
| tavily | 4 | 95 | 1 | ✅ |
| kalshi-openapi | 4 | 79 | 1 | ✅ |
| twitter-trend | 2 | 61 | 2 | ✅ |
| platform-txyz-openapi | 4 | 50 | 0 | ✅ |
| twitter-actions | 6 | 46 | 0 | ✅ |
| claude-messages | 1 | 39 | 0 | ✅ |
| aliyun-video | 2 | 38 | 0 | ✅ |
| twitter-tweet-replies-v2 | 1 | 27 | 0 | ✅ |
| chat-image-generation | 1 | 25 | 0 | ✅ |
| reddit | 5 | 20 | 0 | ✅ |
| gemini-openapi | 1 | 16 | 1 | ✅ |
| openai-chat | 1 | 16 | 0 | ✅ |
| macro_snapshot | 2 | 14 | 2 | ✅ |
| matching-markets-openapi | 2 | 13 | 0 | ✅ |
| openai-images-generations | 1 | 13 | 0 | ✅ |
| openapi | 3 | 13 | 0 | ✅ |
| youte-search | 1 | 11 | 0 | ✅ |
| analyst-estimates | 1 | 8 | 1 | ✅ |
| **合计** | **667** | **18,290** | **109** | **31/31 ✅** |

## 六、两处工程实情：大档分片 + 工具链第 4 次修复（透明留痕）

全量执行中遇到两处需如实交代的工程细节，二者都不影响最终双闸门结论，但关系到产物可信度：

**(1) 超大档分片并发 + 中央复验**。`dataforseo`（445 op）与 `agentmail`（46 op）两份超大档，按互斥的 path 分组切片（`slice_spec.py`，保留全量 `components` 以保 `$ref` 解析），派多个子 agent 各写一份分片 `content.json`，再合并后**在全档上一次性重新注入 + 双闸门复验**。dataforseo 13 个分片用 `merge_content.py` 严格合并（opKey 全档唯一，零冲突）；agentmail 因源 spec 把 46 个 operation 复用成仅 **12 个 operationId**（`get`/`list`/`delete` 等在多条 path 上同名），用专用的 `union_merge.py` 按 opKey 深合并。两档全档复验均双闸门绿。

**(2) agentmail 的 `unresolved=1347` 是源结构属性，不是缺陷**。注入器以 operationId 为 opKey，一份 content 块会被应用到该 id 下的全部同名 path；agentmail 的同名 operationId 各自挂着结构不同的 schema，故非匹配的兄弟 path 上会记 harmless `unresolved`。判定依据是**两道绑定闸门**：原生保全 exit 0、完整性 missing=0（944 个实际字段全齐备）——operationId 是源 spec 的原生结构、不可改，故此为**已认定的可接受工程产物**，非待修项。

**(3) 工具链第 4 次一致性修复（flat-dotted-key）**。`dataforseo` / `apollo` 的响应 schema 把深层字段存成**字面量含点号/方括号的扁平 property key**（如 `properties["tasks.result.items.keyword"]`、`properties["account_stages[].category"]`，而容器 `tasks` 自身只是占位）。原注入器 `resolve_property` 按 `.` 切分逐段下钻，永远命不中这类整键，而对照表 `make_review` 按字面枚举又要求它们齐备——首批子 agent 据此正确报告「unresolved == missing」并**拒绝杜撰或私改工具**（遵守红线）。我亲眼核实 schema 形态后，认定这是 descend/resolve 一致性 bug 的第 4 个实例，在权威 `inject_xdoc.py` 的 `resolve_property` 加「最长字面量整键优先匹配」修复，validated 覆盖 apollo + 全部 13 个 dataforseo 分片，无需任何 per-slice workaround（试点期的临时绕行脚本已删除）。

## 七、待负责人决断

本阶段执行严格遵守「不产出新事实、不改已定结论」。两处需负责人知悉的事项：

1. **批注 109 条待研发确认**：这些是源 spec 未声明、加强时拒绝杜撰而显式留痕的硬事实缺口（哈希算法、内部标志语义、运算符全集等）。建议作为一份「待研发补全清单」反馈给上游，补全后可去掉批注、升级为确定描述。
2. **渲染层缺口仍在（沿用 D-008 发现，不阻断本交付）**：火山 `direct` 渲染器按 `Action`/`Version` 信封模板生成、不渲染 AIsa 真实 REST 参数。本路线**刻意不以渲染 md 为交付**，权威呈现是可抽取的三栏对照表 `review_table.md`，故此缺口不影响本阶段价值落地；但若要让加强在最终线上页面可见，仍需在推上线前修渲染器或换渲染路径。

---

> 复现：任取一份 spec，在项目根执行
> `python3 skill-local/aisa-doc-enhance/tools/inject_xdoc.py --spec ~/files/aisa-team-docs/openapi/<name>.json --content ws-v2/<name>/content.json --out /tmp/e.json --review-out /tmp/r.json`
> → `python3 skill-local/aisa-doc-enhance/tools/check_native_preserved.py ~/files/aisa-team-docs/openapi/<name>.json /tmp/e.json`（exit 0）
> → `python3 skill-local/aisa-doc-enhance/tools/make_review.py --spec /tmp/e.json --out /tmp/rev --require both`（missing=0）。
> 全量一次性复跑见 `ws-v2/central_accept.py`（exit 0 = 31 份全绿）。
