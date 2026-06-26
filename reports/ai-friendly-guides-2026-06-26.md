# AIsa guides/ 散文 AI 友好度质检报告（试点）

> 生成日期：2026-06-26　·　技能：`ai-friendly-doc-check-multiagent-v10`
> 质检对象：`AIsa-team/docs`（工作副本 `~/files/aisa-team-docs`，HEAD `16863d3`）下 `guides/**/*.mdx`，共 30 页人写散文
> 排除：664 个含 `openapi:` frontmatter 的 API 参考桩页（正文由 spec 渲染，非手写）
> 判定口径：每条结论仅凭源仓库文件可 Ctrl+F 复现；拿不准的不报（零误报红线）

## 一、结论先行

这 30 页是 Agent 接入 AIsa 的第一落点——它读这里判断「能调什么、怎么调、调完怎么算对」。本轮系统质检后，**确认 10 条会坑到 Agent 的硬缺口，零漏报、零误报**，外加 1 条经复核排除的疑似项。

10 条里没有一条是错别字或排版瑕疵，全部是**会让 Agent 拿错值、找错地方、或对不上账**的语义缺口。按严重度：4 条「高」（直接误导，Agent 必栽），3 条「中高」，3 条「中/弱」。它们高度集中在两类病灶：**同一事实跨文档（或同页内）口径打架**，以及**列名/说明指向两个不同对象**。

一句话定性：**这批散文的事实层没有单一权威源，数字与名称各写各的，Agent 无从判断该信哪一个。**

## 二、归因拆解：10 条缺口按「病灶」归为三类

| 编号 | 病灶类型 | 位置 | 文档写了什么 | 真值 / 冲突项 | 置信度 | 规范点 |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | 列名与说明串题 | `dashboard/usage-logs.mdx` | `Tokens` 列说明为「The API key used for the request」 | 列名是数量类，说明却描述 API key，自相矛盾 | 高 | 1.6 / 6.3 |
| P2 | 同物异址 | `learn/agent-skills-vs-tools.mdx` | 首段链 `github.com/AIsa-skills` | 表格/文末为 `github.com/AIsa-team/agent-skills` | 高 | 6.1 / 6.2 |
| P3 | 同物异名 | `learn/agent-skills-vs-tools.mdx` | 决策树称「OpenClaw registry」 | 全文其余称「agent-skills registry」，无消歧 | 中高 | 1.3 / 6.1 |
| P4 | 数值口径冲突 | `tutorials/use-aisa-in-hermes-agent.mdx` | CLI 示例「167 model(s) visible / [1-167]」 | `models.mdx` 目录合计 57，多页统一口径「50+」 | 高 | 6.1 |
| P5 | 阶梯非单调 | `pricing/wallet.mdx` | $50 → 5%、$100 → 5% 折扣相同 | 折扣随金额单调递增的常理被打破 | 中/弱 | 1.1 |
| P6 | 同页计费单位冲突 | `pricing/ai-model-pricing-llm-inference.mdx` | `gpt-image-2` 按 per-token 列价 | 同页页尾称「image-generation routes 按 per request 计费」 | 中高 | 6.1 |
| P7 | 已发布但不可寻址 | `changelog.mdx` / `agent-discovery.mdx` | 列出 4 个 Wan 视频模型 ID（t2v/i2v） | `models.mdx`、定价页无任何对应条目 | 中 | 6.1 / 6.2 |
| P8 | 引用源已迁移 | `pricing.mdx` / `per-call-api-pricing.mdx` | 让用户「以 Marketplace 为准查价」 | changelog 声明 `marketplace.aisa.one` 已被 `console.aisa.one` 取代 | 中/弱 | 6.1 |
| P9 | 端点总数口径不一 | `authentication.mdx` vs `agent-discovery.mdx` / `changelog.mdx` | 一处「100+ endpoints」 | 另两处「111+ API paths/endpoints」 | 中高 | 6.1 / 6.2 |
| P10 | 站内链接形态不一 | `pricing/wallet.mdx` | Usage Logs 用绝对 URL `aisa.one/docs/...` | 他页统一用相对路径 `/guides/...` | 中/弱 | 6.2 |

拆到一层就够清楚了：**P1/P3 是「一个对象两套描述」，P2 是「一个资源两个地址」，P4/P6/P9 是「一个数字几处不一」，P7/P8/P10 是「引用指向已失效或不存在的目标」。**根因同一——这批散文缺一个被全站引用的权威事实源，数字和名称是各页作者各自手写、各自固化的快照。修法也同一：把模型数、端点数、注册表名/址、计费单位这些跨页复用的事实，收口到单一来源再引用，而非每页重抄。

## 三、单点下钻：P1 是最危险的一类——它不报错，只悄悄喂错值

10 条里，跨页数字打架的（P4/P9）Agent 至少能察觉「两处对不上」从而起疑。**P1 不会——它在单页内、单列上，把语义彻底调包，且不留任何异常信号。**

`dashboard/usage-logs.mdx` 的日志列说明表里：

```
**Tokens**

The API key used for the request. This field may be empty for system events.
```

列名叫 `Tokens`，任何 Agent（和人）都会期望这一列是 token 计数。可它的说明文字描述的却是「用于该请求的 API key」。同一页里，真正承载 token 数的是另一列 `Input / Output`（"Number of input and output tokens consumed"），而过滤器里另有一项 `Token Name`（指 API key 名）——几乎可以断定是 `Token Name` 列的说明被复制串位到了 `Tokens` 列。

为什么这条最该先修：一个 Agent 拿 Usage Logs 做用量统计或对账时，会按列名 `Tokens` 去取 token 数，实际取到的是一串 API key 文本。它不会报错、不会抛异常，只会在下游算出一笔彻底错位的用量——而且因为列名「看起来对」，连排查时都不会怀疑到这一列。这正是「Agent 判结果」环节最隐蔽的陷阱：错得理直气壮。

复现：

```bash
grep -nA2 '^\*\*Tokens\*\*' guides/dashboard/usage-logs.mdx
```

## 四、零误报口径：撤回了什么，为什么

本轮唯一撤回项：`dashboard/playground.mdx` 的「Playground can be used **without generating an API key**」与「All requests … count toward usage and billing」一度被疑为矛盾。复核认定**二者相容**——免 API key 进 Playground 与照常计入用量计费是两件事（用注册赠送的 free credit 扣费即可），原文无歧义，按红线不报。

同时，下列疑似项经逐字复核判为「不构成问题」，未计入：

- 「50+ AI models」（overview / playground / pricing / security / what-is-an-llm-gateway 五处）是概数，与目录精确值 57 同量级，相容不报；与 P4 的「167」性质不同——167 是同量级之外的硬冲突。
- faq / openrouter 的「100+ non-LLM data APIs」是「非 LLM 数据 API」作用域，与 P9 的「API 端点总数」不是同一本体，不并入。
- 全部 token 单价、per-request 价、context window、各 provider 分项计数（OpenAI 8 / Anthropic 7 / Alibaba 16 …合计 57）在 `models.mdx`、定价页、各 provider 子页逐行一致，`compare-models.mdx` 的成本算例（6.5x / 9.7x）数学自洽，均不报。

## 五、本轮运行健康度

| 探查方法 | 覆盖 | 产出 | 状态 |
| --- | --- | --- | --- |
| 方法 A（精读 + 片内抽键） | 30/30 | 5 条问题 + 检索键 | 正常，完整标记齐 |
| 方法 B（流式三遍法） | 30/30 | 7 条问题 + 检索键 | 正常，完整标记齐 |
| 规范核对（固定清单） | 30/30 | 7 处命中，逐篇回执 30/30 | 正常 |

三路独立探查交叉覆盖，汇总去重台账可对账（保留 10 + 并入 9 + 撤回 1 = 20 条原始线索），每条保留项均带源文件定位、按规范点号归类、经逐字复核。试点验收通过，可铺开至全量 73 页。
