# OpenAPI 内容加强 · 阶段三试点报告

> 受众：AIsa 产品负责人。读完要能判断一件事——把 31 份 OpenAPI spec 做「增强 + 回写」这条路，到底改了什么、改好还是改坏、能不能放心铺开。
>
> 试点对象：`openapi/openai-chat.json`（POST `/chat/completions`，内联请求体）与 `openapi/youte-search.json`（GET `/youtube/search`，query 参数 + 内联响应体）两份真实 spec。技能：`api-doc-agent` 确定性管线 + `@stoplight/spectral-cli@6.16.0`。日期：2026-06-26。

## 一、主线：源头变好，且可证「只增不改」

线上 API 参考页的正文不是手写 Markdown，而是 OpenAPI spec 内联渲染出来的。所以「把文档写好」的真正杠杆，是**把 spec 本身写好**——在不动任何原生结构的前提下，给每个字段补上「这是干什么的、怎么用、有什么坑」。

本阶段交付的，正是这条链路的一次完整跑通：人工撰写中文增强内容 → 确定性管线注入 `x-doc` 命名空间 → 两道闸门校验 → 回写原 spec → 渲染独立增强页。两份试点 spec 的成绩单一致：

| 试点 spec | 增强字段数 | Gate 2（spectral 6.16.0） | 原生保全闸门 | 回写 diff |
| --- | --- | --- | --- | --- |
| openai-chat | 12 个 `title_zh` + operation 级 5 项 | error 0，通过 | exit 0，零篡改 | +80 / −0 |
| youte-search | 11 个 `title_zh` + operation 级 4 项 | error 0，通过 | exit 0，零篡改 | +70 / −0 |

两个数字是这次试点的底气：**回写 diff 的删除行恒为 0**——所有改动都是新增的 `x-doc` 子树，原生的 `paths` / 类型 / `$ref` / `required` / 枚举一个字符都没动；`check_native_preserved.py` 以输入 spec 为基线做关系比对，两份均 exit 0，从机器层面坐实了「只增不改」。spectral 6.16.0 已装到 `$HOME`，Gate 2 是**真正 lint 过的 green**（7 条规则全启用、error 数为 0），不是「未安装跳过当通过」。

## 二、归因：加强分四类，价值各有落点

把「增强」这件事拆开，做的其实是四类性质不同的活，对应解决四种「机器结构说不清」的问题：

- **接口级定位（operation）**：补 `heading_zh`（中文 H1，如「创建对话补全 createChatCompletion」）、`description_zh`（能力 + 场景 + 鉴权）、`profile`。让读者一眼知道这个接口解决什么问题、什么时候用它。源 spec 的 `summary` 只有一句 "Create chat completion"，定位信息几乎为零。
- **字段级释义（property / parameter）**：给每个对外字段写 `title_zh`，从「字段叫什么」补到「传什么值、为什么传、不传会怎样」。openai-chat 覆盖到 `messages` → `role` / `content`、`functions` → `name` / `description` / `parameters` 等嵌套层；youte-search 覆盖 5 个 query 参数 + 响应体 `search_results` → 视频四字段。这是字段最多、最吃理解的一类，也是文档好不好用的分水岭。
- **边界与坑（批注）**：spec 没说清的硬事实——可用模型清单、`top_logprobs` 上限、多模态数组格式、`sp` 令牌编码——一律转成 `\n[⚠️批注:...]`，显式标注「这里待研发确认」，而不是编一个看似合理的数值蒙混过去。
- **错误与响应补全（章节扩展）**：补 `errors` 错误码表与响应说明，并诚实标注来源（openai-chat 的错误码源于 OpenAI 兼容约定推断、youte-search 的 400 / 401 源于 spec 已声明）。

四类加强共同守住六条红线：平台中立（不产 `x-apihub-*`）、只增不改、不复制原生元数据进 `x-doc`、不捏造、AI 不覆盖人工、中文 H1 归 `heading_zh`。其中「AI 不覆盖人工」这条本轮专门做了验证：把 operation 的 `x-doc` 标成 `source: human` 并人工改写 `description_zh`，再用 AI 版 content 重跑注入——结果人工内容原样保留，AI 的不同建议被分流进 `review_list.json`（reason 标 R3/R5），**AI 永不静默覆盖人工**得到机器级证明。

## 三、下钻：`top_logprobs` 从「一个 integer」到「一句人话」

挑全篇最能说明问题的一个字段放大看。源 spec 里 `top_logprobs` 的全部信息只有：

```json
"top_logprobs": {"type": "integer"}
```

一个开发者读到这里是懵的：这数填几？跟谁有关？填了有什么用？机器结构能告诉他的，只有「这是个整数」——而这恰恰是他**唯一不需要别人告诉**的事。加强后的 `title_zh` 是：

> 为每个输出位置额外返回概率最高的若干候选 token 及其对数概率。需在 `logprobs` 为 `true` 时配合使用，用于观察模型在该位置的备选分布。
> [⚠️批注:OpenAI 协议中该值通常限制在 0 至 20 之间，AIsa 网关的实际上限请研发确认。]

这一句补齐了机器结构永远给不出的三件事：**为什么传**（看模型备选分布）、**如何组合**（依赖 `logprobs` 开启，这是跨字段联动，类型签名里完全看不出来）、**边界在哪**（取值上限——但这是拿不准的硬事实，所以转批注让研发确认，而不是替它拍一个 `20`）。类型 `integer` 这个原生元数据，则一个字都没往 `title_zh` 里抄，渲染时由原生结构自己提供，杜绝双源漂移。

这就是整件事的缩影：**机器结构负责「是什么」，增强内容负责「怎么用、什么坑」，两者并存不打架**。把 667 个 operation 都这样过一遍，线上参考页就从「字段字典」变成了「能照着做的说明书」。

## 四、一个系统级缺口：渲染器吃不到真实 REST 参数

下钻还顺带暴露一个不在本阶段修复范围、但必须让产品负责人知道的系统问题（沿用 D-008 的发现）：youte-search 的 5 个真实 query 参数（`engine` / `q` / `sp` / `gl` / `hl`）的中文增强**确实写进了权威产物 `enhanced.yaml`**，但 `direct`（火山）渲染器按 `Action` / `Version` 信封模板出页面，最终只渲染出 `Action` 和 `Version` 两行，把真实参数的加强价值挡在了页面之外。

这不影响本阶段的核心交付——按 D-002，阶段三的权威交付物是 `enhanced.yaml`（回写后的增强 spec），不是渲染后的 md；增强内容确凿落在 spec 里、可被任何正确的渲染器消费。但它说明：**渲染层存在平台缺口，真正推上线前需要修渲染器或换渲染路径**，否则 REST 风格接口的增强在火山模板下会「隐形」。记为渲染器待办，不阻断增强与回写。

## 五、结论与铺开建议

试点结论：「人工撰写 → 确定性注入 → 双闸门 → 回写」这条链路在内联请求体、query 参数、内联响应体三种 spec 形态上均跑通，两道确定性闸门（Gate 2 真 lint green + 原生保全 exit 0）+ 回写 diff 零删除，构成可对账、可复现的验收证据。流程可复用。

铺开建议：

1. **按 spec 形态分层推广**至 31 份 spec / 667 个 operation，大档由子 Agent 按接口切分并发撰写、主 Agent 汇总核验（抽查注水 / 留空 / 批注）。
2. **撰写是灵魂、不可外包给脚本**：`title_zh` / `description_zh` 必须逐字段按使用者视角写，禁止套模板批量直译——那等于没写。
3. **先修渲染器再谈上线**：REST 参数在 `direct` 模板下隐形的缺口需在推上线前解决，否则增强价值在最终页面里看不见。

## 附：可验收产物清单

两份试点产物均落 `pilots/ws/`（会话工作区），可逐件复核：

- `pilots/ws/openai-chat/`：`content.json`（人工撰写的增强内容）、`enhanced.yaml`（回写后增强 spec）、`enhanced-page.md`（独立增强参考页）、`writeback.diff`（回写前后 diff，+80/−0）、`review_list.json`；外加 `existing-human.yaml` + `enhanced-merged.yaml` + `review_merged.json`（source=human 保护演示证据）。
- `pilots/ws/youte-search/`：`content.json`、`enhanced.yaml`、`enhanced-page.md`、`writeback.diff`（+70/−0）、`review_list.json`。

复现命令（在 `~/files/aisa-docs-voyager` 下）：用 `pilots/phase3-pilot/inline_inject.py` 注入，`spectral lint --ruleset <api-doc-agent>/contracts/rulesets/doc-engine-output.spectral.yaml enhanced.yaml` 过 Gate 2，`check_native_preserved.py <输入 spec> enhanced.yaml` 过原生保全闸门。
