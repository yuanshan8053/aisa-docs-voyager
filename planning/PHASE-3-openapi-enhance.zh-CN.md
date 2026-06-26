# 阶段三 · OpenAPI 内容加强（v2 · LLM 推理双字段加强）

**阶段目标**：用本地改造版技能 `aisa-doc-enhance`，由 **LLM 推理逐参数**把 AIsa 的 OpenAPI spec 加强成专业、好懂、人话的参考内容。产出**双字段加强**（加强英文 `desc_en` + 中文本地化 `title_zh`）并以 `x-doc` 命名空间只增不改地回写原 spec，配套**三栏对照表**让「改了什么、改好还是改坏」一眼可查。

**为什么 v2 推翻 v1**（见 D-012）：v1 试点用原 `api-doc-agent` 重型三引擎链路，交付物是渲染后的 md，而 `direct`（火山）渲染器按 `Action`/`Version` 信封模板生成、**不渲染** AIsa 真实 REST 参数——加强价值在最终产物里隐形，产品负责人无法确认改动是否更好。v2 砍掉渲染器/spectral/引擎依赖，**只吸收写作内核（一句方法论）**，由 LLM 逐字段加强，并用三栏对照表（源英文→加强英文→中文）直接呈现每个字段的改动。

---

## 输入边界

- **输入 spec**：源仓库 `~/files/aisa-team-docs/openapi/*.json`（31 个，共 667 个 operation、约 16.5k 个 schema 字段，其中 92% 自带英文 `description` 可作为加强基准）。
- **规模分层**（先小后大，逐档验收）：
  - **试点档（1 op）**：`youte-search.json`（GET，5 query 参数 + 内联响应）、`openai-chat.json`（POST，深层内联请求体 + oneOf）。
  - **中档（≤10 op）**：如 `perplexity-openapi.json`（具名 `$ref`）、`twitter-*`、`reddit.json`、`coingecko.json`。
  - **大档（数十～数百 op）**：`apollo.json`(54)、`agentmail.json`(46)、`dataforseo.json`(445) —— 子 agent 分片并发撰写，主 agent 汇总核验。
- **内容必须由 LLM 逐字段撰写**：注入器是确定性的，只做装配；`desc_en`/`title_zh` 必须由接手 agent 站在使用者视角按 `METHODOLOGY.md` 亲自写进 `content.json`。**严禁脚本批量套模板**——机械直译等于没写。

## 本地改造版技能（派遣 agent 只读此处）

`~/files/aisa-docs-voyager/skill-local/aisa-doc-enhance/`，已就绪、已自测通过：
- `SKILL.md` — 工作流与铁律。
- `METHODOLOGY.md` — 唯一写作内核（从原 skill 蒸馏，去平台化/去引擎化）。
- `tools/inject_xdoc.py` — 双字段 x-doc 加性注入器（standalone，纯 python3）。
- `tools/check_native_preserved.py` — 原生保全闸门。
- `tools/make_review.py` — 三栏对照表 + 完整性闸门。

**不读** `/data/plugins/.../api-doc-agent`，不装 spectral，不依赖任何包外引擎。

## 验收产物（每个 spec，缺一不可）

1. `content.json` — LLM 逐字段撰写的双字段增强内容。
2. `enhanced.json` — 含 `x-doc` 的增强 spec，原生零改动。
3. `review_table.md` — 三栏对照表（源英文 → 加强英文 → 中文），逐字段可判好坏。
4. `inject_review.json` — 注入审计（源保护跳过 / dotpath 未命中）。
5. `reports/openapi-enhance-v2-<日期>.md` — 小结：加强了哪些接口/字段、双字段如何对账、两道闸门状态、与 v1 的差异与改进。
6. 回写 `project/STATE.md`、`project/DECISIONS.md`。

## 验收标准

- **真正提升可用性**：补全字段用途、取值业务含义、依赖、坑、错误码；不是机械翻译、不注水。
- **双字段语义一致**：`desc_en` 与 `title_zh` 说同一件事。
- **完整性闸门 exit 0**：每个对外字段都齐备 `desc_en` + `title_zh`（缺漏即非零）。
- **原生保全闸门 exit 0**：原生 `paths/$ref/类型/枚举/必选/description` 零改动，无双源漂移。
- **可查可判**：`review_table.md` 让审阅者逐字段确认「改了什么、改好还是改坏」。

---

## 自包含委派提示词（复制给新 session agent）

> 你接手 AIsa 文档质量工程的「阶段三 v2：OpenAPI 内容加强」。你之前没有本项目上下文，请严格按下文执行。
>
> **背景**：AIsa 是 OpenAI 兼容的 AI 能力网关，文档源仓库 `AIsa-team/docs`（本地工作副本 `~/files/aisa-team-docs`）里有 31 个 OpenAPI spec（`openapi/*.json`）。线上 API 参考页正文由这些 spec 渲染内联生成，不是手写 md。目标：由你（LLM 推理）站在 API 使用者视角，把每个字段/参数加强成专业好懂的内容，产出**双字段**——加强英文 `desc_en` + 中文本地化 `title_zh`——并以 `x-doc` 只增不改地写进 spec。结果交产品负责人。**上一版（v1）失败的教训：用了重型渲染链路，最终 md 被火山 Action/Version 信封模板覆盖，看不清真实参数的加强；本版砍掉渲染，用三栏对照表直接呈现改动。**
>
> **第一步 · 读权威信息源**：依次读 `~/files/aisa-docs-voyager/project/CHARTER.md`、`project/STATE.md`、`project/DECISIONS.md`（特别是 D-012）、`project/baselines/FACTS.zh-CN.md`、`~/files/aisa-docs-voyager/WRITING-STANDARD.zh-CN.md`。
>
> **第二步 · 读本地技能（只读这里，不读 /data/plugins）**：`~/files/aisa-docs-voyager/skill-local/aisa-doc-enhance/`。先读 `SKILL.md`，再**精读 `METHODOLOGY.md`**（写作内核，双字段模型 + 自适应深度 + 两条边界 + 不捏造转批注）。工具在 `tools/`，纯 python3、无外部依赖。
>
> **第三步 · 试点（先 1 个接口跑通全链）**：选 `~/files/aisa-team-docs/openapi/youte-search.json`。
>   1. 逐字段按 `METHODOLOGY.md` 撰写 `content.json`（格式见 `tools/inject_xdoc.py` 顶部 docstring：`operations{}` 接口级 + `fields{}` 用 dotpath 寻址）。每个对外字段产 `desc_en` **和** `title_zh`，二者语义一致；简单字段一句话、复杂才展开；拿不准转 `annotation`；绝不复制原生元数据、绝不机械套模板。
>   2. 注入：`python3 tools/inject_xdoc.py --spec <spec> --content content.json --out enhanced.json --review-out inject_review.json --doc-version 2.0.0`
>   3. 原生保全闸门（须 exit 0）：`python3 tools/check_native_preserved.py <spec> enhanced.json`
>   4. 三栏对照 + 完整性闸门（须 exit 0）：`python3 tools/make_review.py --spec enhanced.json --out review_table --require both`
>   5. 打开 `review_table.md` 自查：每个字段「源英文 → 加强英文 → 中文」是否都改得更好、无注水、无原生元数据复制。
>   再用 `openai-chat.json`（深层内联 + oneOf）跑一遍，确认对深层嵌套也成立。
>
> **第四步 · 推广**：按 输入边界 的规模分层，从中档到大档逐 spec 跑同一四步。大档（`apollo`/`agentmail`/`dataforseo`）按接口切分派遣子 agent 并发撰写 `content.json`，主 agent 汇总后逐接口核验（抽查注水/留空/批注/双字段一致），再统一跑两道闸门。如实汇报每批：`接口数 / 已写字段数 / 转批注数 / 跳过数及原因`，不得谎报。
>
> **第五步 · 报告 + 回写**：写 `reports/openapi-enhance-v2-<今天日期>.md`（遵循 `WRITING-STANDARD.zh-CN.md` 2.5 维叙事：先讲清双字段加强 + 可对账的整体价值、再拆解做了哪几类加强、后下钻一个字段从「源英文 → 加强英文 → 中文」三态对比）。更新 `project/STATE.md`，新决策追加 `project/DECISIONS.md`。
>
> **约束**：不换仓库、不提 PR、不撤销凭证、不直连 LLM Gateway、不在沙箱启网络监听、PAT 永不明文打印、占位符 `[ph_..._ph]` 逐字节保留。x-doc 只增不改、绝不捏造、绝不脚本套模板。完成后用一句话汇报验收产物清单。
