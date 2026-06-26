# 报告甲 · AIsa 存量文档内容审计

> 受众：AIsa 产品负责人　·　审计日期：2026-06-26
> 审计对象：`AIsa-team/docs` 源仓库（工作副本 `~/files/aisa-team-docs`）
> 源仓库 pinned commit：`16863d3`（审计时 HEAD，本报告全部 git 行号永久钉在此 commit）
> 范围：743 页 `.mdx` = 664 桩页（spec 内联渲染，非手写）+ 73 页人写散文（`guides/` 30 + `agent-skills/` 43）+ 31 份 OpenAPI spec
> 方法一句话：阶段一确定性静态检查（零依赖、可证伪）+ 阶段二 Map-Reduce 多 agent 散文质检（三层隔离防确认偏误）
> 判定红线：零误报——凡定罪结论必须仅凭源仓库文件即可 Ctrl+F 复现，live 探测只作旁证

---

## 一、执行摘要：文档在「发现入口」与「跨页事实」两处系统性失真，根因是缺单一权威事实源

AIsa 的文档同时面向人和 Agent，Agent 靠它判断「AIsa 能干什么、怎么调、调完怎么对账」。这本是文档的核心价值，过去也确实在维护——`guides/` 下有一套 June 4 刷新、内部逐行自洽的权威目录（`models.mdx` + 定价页）。

但本轮审计发现：**真正决定 Agent 行为的两个位置正在失真。** 一是面向 Agent 的能力总览页 `guides/agent-discovery.mdx`，把一份 645 路径、321 schema、14 分类的 spec 描述成了 121 schema、10 分类的样子，还漏列 4 个真实分类——其中一个多达 445 操作。二是 43 页 `agent-skills/` 操作手册，每页各自手抄了一份模型价、上下文窗口、端点路径、家族计数，谁都没去引用那套权威目录。

由此自然引出产品负责人该问的那一问：**Agent 会不会因此被带偏，根子在哪？** 答案是会，而且根子只有一个——**文档缺一个被全站强制引用的单一权威事实源，关键数字与名称是各页各自手写、各自固化的离群快照。**

支撑这一主结论的，是四条互不重叠的发现：

1. **发现入口失真是阻断级的。** 3 项 BLOCKER 全部集中在 `agent-discovery.mdx`：schema 写 121（实 321）、分类写 10（实 14）、分类表漏列 4 类。只读这页的 Agent 会拿到一张错误的能力地图。
2. **被漏掉的不是边角，是主力。** 漏列的 `SEO & Search Data` 一类独占 445 操作，占全 spec 663 操作的约三分之二，却在能力总览里完全隐身——这是核心能力的发现性缺失。
3. **跨页事实打架的规模更大。** 73 页散文经全量质检确认 20 条会坑到 Agent 的硬缺口（7 高 / 8 中高 / 5 中），其中 14 条命中同一规范点 6.1（跨文档同对象取值不一致），全部是 agent-skills 页与权威目录对不上账。
4. **最隐蔽的一类不报错只喂错值。** 同一个模型 `qwen-plus-2025-12-01` 在三页给出三套单价，输出价 `$0.84`（权威）vs `$0.90` vs `$12.60`——cn-llm 那份高出 15 倍，每个数字单独看都「格式正确、量级合理」，Agent 没有任何信号判断该信哪个。

**单一根因**：agent-skills 与 agent-discovery 都在「手抄事实」而非「引用权威」——前者抄一次就固化一个离群快照，后者是某次手写后固化、未随 spec 演进的快照。

**最高优先级建议**：为 agent-skills 建立对 `guides/models.mdx` + 定价页的单一引用，删除各页自维护的离群价格 / 计数 / 端点 / 旧型号——14 条 6.1 缺口随之一次性消解；同步让 `agent-discovery.mdx` 的数字与分类表由 `openapi.yaml` 自动派生，3 项 BLOCKER 从源头杜绝再漂移。

---

## 二、关键发现

### 2.1 生产模式：线上 API 参考正文是 spec 内联渲染产物，不是手写 Markdown

文档生产链路已查清：

```
AIsa-team/docs            源仓库：.mdx 散文 + openapi/*.json + scripts/consolidate_openapi.py
      │  .github/workflows/sync-openapi.yml
      ▼
AIsa-team/new-style-landing-page   部署层
      ▼
https://aisa.one          线上：HTML 给人，.md 孪生页 + 发现契约给 Agent
```

这条链路决定了审计该往哪看。664 个 API 参考页是**桩页**——frontmatter 用 `openapi: "openapi/xxx.json METHOD /path"` 指向 spec，正文由渲染层从 OpenAPI spec 内联生成，并非手写。换言之，线上 API 参考正文的真值就是仓库里那份 consolidated `openapi.yaml`，拿文档对它的描述与它本身比对即可无歧义定罪。真正可做 AI 友好度散文质检的，是 `guides/`（30）+ `agent-skills/`（43）= 73 页人写散文。两类对象、两套方法，由此分工。

### 2.2 审计统计：3 项 BLOCKER + 20 条散文缺口，去向台账账平

规模盘与缺口分布（全部静态可证，复现命令见附录）：

| 维度 | 数值 |
| --- | --- |
| 总页面 `.mdx` | 743 |
| API 参考桩页（含 `openapi:`） | 664 |
| 人写散文（质检对象） | 73 = `guides/` 30 + `agent-skills/` 43 |
| OpenAPI spec 文件 | 31 |
| 中文页面 | 11（覆盖率约 1.5%） |
| 阶段一 BLOCKER | 3（B1–B3，集中在 `agent-discovery.mdx`） |
| 阶段二散文缺口 | 20（P1–P20，7 高 / 8 中高 / 5 中） |

阶段二去向台账可对账：**47 条原始线索 = 20 保留 + 21 并入 + 6 撤回**，三者相加等于原始数，无悬空线索（明细见附录三）。

### 2.3 问题模式与根因：20 条散文缺口归为一层四类病灶，14 条同根

按「会坑到 Agent 的什么」拆一层，20 条缺口落到四类病灶：

| 病灶类型 | 条目 | 规范点 | 说明 |
| --- | --- | --- | --- |
| 同对象几套值 | P1–P5、P7–P14、P17 | 6.1 | agent-skills 页与权威目录对不上账：同模型几套价、同能力两套端点、一份清单几个数、挂旧型号 |
| 同参数两种事实 | P6 | 6.1 | 一篇把 `gl=cn` 当可用示例，另一篇明说 `cn` 不支持会报错 |
| 中英双版结论不一 | P15 | 6.3 | 同组套利价，中文算「5.3% 利润」，英文标「0.05 edge」（=5%） |
| 单篇内算不平 / 表述瑕疵 | P16、P18、P19、P20 | 1.6 / 1.4 / 4.1 | 8 维权重合计 130%、折扣阶梯并列 5%、代号 Terminus 未释、注释 last 30 days 实为 31 天 |

第一类 14 条是绝对主病灶，根因同一：**agent-skills 各页各自手抄事实、不引用权威目录。** `guides/` 那套 `models.mdx` + 定价页 June 4 刷新、内部自洽；agent-skills 抄一次就固化一个快照，快照之间、快照与权威源之间于是系统性打架。BLOCKER 同根的另一面：`agent-discovery.mdx` 对 spec 形态的描述也是某次手写后固化的快照，schema 从 121 长到 321、分类从 10 长到 14，文档原地不动。

**两处失真，同一个病：该引用的没引用，手抄的快照在腐烂。**

---

## 三、我们如何做的：确定性静态检查 + 三层隔离多 agent，靠透明建立可信

**取数。** 真值取自 pinned commit `16863d3` 已提交的源仓库文件，尤其是 consolidated `openapi.yaml`——它正是线上 API 参考正文内联渲染所依据的同一份产物。数字会随上游提交变动，所以**复现命令才是不变的真相来源**：本报告每条结论都附一条可在源仓库根独立跑、确定性输出、零 live 依赖的命令。

**工具。** 阶段一用自建确定性静态检查器 `checks/src_consistency.py`（零依赖、可 `--ci`），只抓机械可证伪的结构错——schema 计数、分类条数这类能被 `openapi.yaml` 一键比对的硬伤。阶段二的坑是语义级的（同模型三套价、列名与说明串题），静态规则抓不到，改用 `ai-friendly-doc-check-multiagent-v10` 的 Map-Reduce 多 agent 质检：三路探查 agent（全库精读 / 流式三遍 / 规范核对固定清单）并行 Map，单汇总 agent Reduce。**三层隔离**是关键设计——探查 agent 永远看不到分类体系，只凭「会不会坑到 Agent」找证据，避免分类框架污染探查、制造确认偏误。

**可信度口径（透明即权威）。** 守零误报的四道机制：① 两条硬线撤回律——只有「源文件 Ctrl+F 搜得到原文」才可能保留，凡「证据搜不到」或「存在消歧原文（两处指不同对象）」立即撤回；② 每条保留项逐字回源复核，不凭转述定罪；③ 去向台账可对账（原始 = 保留 + 并入 + 撤回）；④ 权威源单一化，权威集内部一致的值绝不报。据此本轮如实撤回 6 条、标 5 处待人工确认，并撤下了前序基线的「技能计数 13 vs 43」（A2A 广播 13 skill 与 43 个安装页是两个概念，无法仅凭源码证伪，见附录三）。

---

## 四、具体审计报告

每条带齐证据字段，支持四步闭环：点线上 URL 看页 → 点 git 跳到行 → Ctrl+F 命中原文 → 跑命令验真值。线上 URL 形态经抽样自验——`https://aisa.one/docs/<路径>` 返回 200，裸 `https://aisa.one/<路径>` 返回 404，故全部采用 `/docs/` 前缀（自验记录见附录一）。git 行号永久钉在 `16863d3`。

### 4.1 阻断硬伤（BLOCKER）：发现入口的能力地图画错了

**B1 · spec schema 数：文档写 121，实为 321**　`BLOCKER`
- 文档位置：`guides/agent-discovery.mdx:16`
- 线上：https://aisa.one/docs/guides/agent-discovery　·　git：https://github.com/AIsa-team/docs/blob/16863d3/guides/agent-discovery.mdx#L16
- 坑到谁：Agent 读这页判断 spec 规模与可对接的数据结构数；少看 200 个 schema，会低估接口复杂度、漏接大量数据模型。
- 原文（可 Ctrl+F）：`Machine-readable specification covering 111+ API paths and 121 schemas`
- 真值 / 复现：`python3 -c "import yaml;print(len(yaml.safe_load(open('openapi.yaml'))['components']['schemas']))"` → `321`
- 根因归类：spec 形态固化快照，未随 `openapi.yaml` 演进
- 建议动作：见 §五·建议二（数字由 spec 自动派生）

**B2 · spec 分类数：文档写 10，实为 14**　`BLOCKER`
- 文档位置：`guides/agent-discovery.mdx:127`
- 线上：https://aisa.one/docs/guides/agent-discovery　·　git：https://github.com/AIsa-team/docs/blob/16863d3/guides/agent-discovery.mdx#L127
- 坑到谁：Agent 据此判断 AIsa 提供几大类能力；少算 4 类，会以为部分能力不存在。
- 原文（可 Ctrl+F）：`organized into 10 categories`
- 真值 / 复现：`python3 -c "import yaml;d=yaml.safe_load(open('openapi.yaml'));t=set();[t.add(x) for p in d['paths'].values() for m,o in p.items() if m in ('get','post','put','patch','delete') and isinstance(o,dict) for x in o.get('tags',[])];print(len(t))"` → `14`
- 根因归类：同上，spec 形态固化快照
- 建议动作：见 §五·建议二

**B3 · API 分类表漏列 4 个真实分类（其一独占 445 操作）**　`BLOCKER`
- 文档位置：`guides/agent-discovery.mdx:163`（表起始行）
- 线上：https://aisa.one/docs/guides/agent-discovery　·　git：https://github.com/AIsa-team/docs/blob/16863d3/guides/agent-discovery.mdx#L163
- 坑到谁：表自称「spec 把端点组织为以下分类组」却只列 10 类，漏掉 Agent Email（46 操作）、Reddit（5）、SEO & Search Data（445）、Sales Intelligence（54）。只读这页的 Agent 会认定最大的那块业务对它不存在——`SEO & Search Data` 一类即占全 spec 663 操作的约三分之二。
- 原文（可 Ctrl+F）：表内现存类目如 `| AI Models | ...`；缺失项可在 spec 侧证实
- 真值 / 复现：`python3 -c "import yaml;d=yaml.safe_load(open('openapi.yaml'));from collections import Counter;c=Counter();[c.update(o.get('tags',[])) for p in d['paths'].values() for m,o in p.items() if m in ('get','post','put','patch','delete') and isinstance(o,dict)];import json;print(json.dumps(dict(sorted(c.items())),ensure_ascii=False))"` → 14 类全名与操作数，含上述漏列 4 类
- 根因归类：同上，spec 形态固化快照
- 建议动作：见 §五·建议二（分类表由 spec 自动派生）

### 4.2 散文 AI 友好度缺口（20 条）：跨页事实各写各的

> 真值基准：`guides/models.mdx` + `guides/pricing/ai-model-pricing-llm-inference.mdx` + `guides/chinese-llms/*.mdx`（均标注 June 4 刷新、内部逐行自洽）。被告是 agent-skills 等页的离群快照。

**P1 · 同模型三套价，输出价差 15 倍**　`高`
- 文档位置：`agent-skills/cn-llm.mdx:83`（另：`agent-skills/aisa-provider.mdx:99`）
- 线上：https://aisa.one/docs/agent-skills/cn-llm　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/cn-llm.mdx#L83
- 坑到谁：Agent 做成本预算或多模型比价选型时，读到 cn-llm 会以为 `qwen-plus` 输出贵到不可用而排除它；读 aisa-provider 则估算偏 7%。三套数字每套单独看都合理，无信号判断该信哪个。
- 原文（可 Ctrl+F）：`| qwen-plus-2025-12-01 | $1.26/M | $12.60/M | Plus version |`
- 真值 / 复现：权威 `$0.2800 in / $0.8400 out`。`grep -rn 'qwen-plus-2025-12-01' guides/pricing/ai-model-pricing-llm-inference.mdx agent-skills/cn-llm.mdx` → 权威 `$0.8400` vs cn-llm `$12.60`
- 根因归类：同模型几套价 · 6.1
- 建议动作：见 §五·建议一

**P2 · qwen-mt-flash 价格分叉**　`高`
- 文档位置：`agent-skills/cn-llm.mdx:84`（另：`agent-skills/aisa-provider.mdx:281`）
- 线上：https://aisa.one/docs/agent-skills/cn-llm　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/cn-llm.mdx#L84
- 坑到谁：同 P1，翻译类高频调用按错价预算，累积偏差显著。
- 原文（可 Ctrl+F）：`| qwen-mt-flash | $0.168/M | $0.514/M | Fast machine translation |`
- 真值 / 复现：权威 `$0.0720 in`。`grep -rn 'qwen-mt-flash' guides/pricing/ai-model-pricing-llm-inference.mdx agent-skills/cn-llm.mdx` → 权威 `$0.0720` vs cn-llm `$0.168`
- 根因归类：同模型几套价 · 6.1
- 建议动作：见 §五·建议一

**P3 · deepseek-r1 价格高约 5 倍**　`高`
- 文档位置：`agent-skills/cn-llm.mdx:91`
- 线上：https://aisa.one/docs/agent-skills/cn-llm　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/cn-llm.mdx#L91
- 坑到谁：Agent 把推理模型成本高估约 5 倍，可能误弃该模型。
- 原文（可 Ctrl+F）：`| deepseek-r1 | $2.00/M | $8.00/M | Reasoning model, supports Tools |`
- 真值 / 复现：权威 `$0.4018 in / $1.6058 out`。`grep -rn 'deepseek-r1' guides/pricing/ai-model-pricing-llm-inference.mdx agent-skills/cn-llm.mdx`
- 根因归类：同模型几套价 · 6.1
- 建议动作：见 §五·建议一

**P4 · kimi-k2.5 价格离群**　`高`
- 文档位置：`agent-skills/aisa-provider.mdx:143`
- 线上：https://aisa.one/docs/agent-skills/aisa-provider　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/aisa-provider.mdx#L143
- 坑到谁：Agent 按 `~$0.60/~$2.40` 预算，与权威 `$0.4018/$2.1077` 不一致，成本估算失真。
- 原文（可 Ctrl+F）：`"input": 0.60,` / `"output": 2.40,`（位于 `"id": "aisa/kimi-k2.5"` 的 cost 块）
- 真值 / 复现：权威 `$0.4018 in / $2.1077 out`。`grep -n 'kimi-k2.5' guides/pricing/ai-model-pricing-llm-inference.mdx` → line 98
- 根因归类：同模型几套价 · 6.1
- 建议动作：见 §五·建议一

**P5 · 同能力两套端点路径**　`高`
- 文档位置：`agent-skills/us-stock-analyst.mdx:113`、`:120`
- 线上：https://aisa.one/docs/agent-skills/us-stock-analyst　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/us-stock-analyst.mdx#L113
- 坑到谁：Agent 按 `/financial/analyst/eps`、`/financial/insider/trades` 拼 URL 会请求到不存在的端点而失败；真实端点是带连字符的 `/financial/analyst-estimates`、`/financial/insider-trades`（见 `marketpulse.mdx:216`、`:218`）。
- 原文（可 Ctrl+F）：`/financial/analyst/eps?ticker=AAPL` / `/financial/insider/trades?ticker=AAPL`
- 真值 / 复现：`grep -rn 'financial/analyst-estimates\|financial/insider-trades' agent-skills/marketpulse.mdx agent-skills/trend-forecast.mdx`
- 根因归类：同能力两套路径 · 6.1
- 建议动作：见 §五·建议一

**P6 · 同参数 `gl=cn` 一篇说可用、一篇说不支持**　`高`
- 文档位置：`agent-skills/youtube-search.mdx:110`
- 线上：https://aisa.one/docs/agent-skills/youtube-search　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/youtube-search.mdx#L110
- 坑到谁：Agent 照 youtube-search 用 `gl=cn` 会被服务端报 `Unsupported value`；youtube-search-skill 已明说 `cn` 不支持。
- 原文（可 Ctrl+F）：`gl` — country code (`us`, `jp`, `cn`, etc.)
- 真值 / 复现：`grep -n 'cn' agent-skills/youtube-search-skill.mdx` → line 385「`cn` (China) ... Unsupported value」
- 根因归类：同参数两种事实 · 6.1
- 建议动作：见 §五·建议一

**P7 · 模型总数三处不一（49+ / 50+ / 167）**　`中高`
- 文档位置：`guides/tutorials/use-aisa-in-hermes-agent.mdx:74`（另：`agent-skills/aisa-provider.mdx:221` 写 49+）
- 线上：https://aisa.one/docs/guides/tutorials/use-aisa-in-hermes-agent　·　git：https://github.com/AIsa-team/docs/blob/16863d3/guides/tutorials/use-aisa-in-hermes-agent.mdx#L74
- 坑到谁：Agent 据此判断可选模型规模，167 与目录明细（约 61）量级不符，选型范围被误导。
- 原文（可 Ctrl+F）：`167 model(s) visible`
- 真值 / 复现：目录明细约 61。`grep -rn '167\|49+ models\|50+ AI models' guides/tutorials/use-aisa-in-hermes-agent.mdx agent-skills/aisa-provider.mdx`
- 根因归类：同清单几个数 · 6.1
- 建议动作：见 §五·建议一

**P8 · us-stock-analyst 挂已被取代的旧型号**　`中高`
- 文档位置：`agent-skills/us-stock-analyst.mdx:207`
- 线上：https://aisa.one/docs/agent-skills/us-stock-analyst　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/us-stock-analyst.mdx#L207
- 坑到谁：Agent 调 `GPT-4`/`Claude 3 Opus`/`Gemini 1.5`/`DeepSeek V2` 会收「模型不存在」；当代目录是 GPT-5 / claude-opus-4-x / Gemini 3.x。
- 原文（可 Ctrl+F）：`GPT-4, GPT-4 Turbo (OpenAI)` / `Claude 3 Opus, Sonnet, Haiku (Anthropic)`
- 真值 / 复现：`grep -nE '^\| (OpenAI|Anthropic|Google Gemini|DeepSeek) ' guides/models.mdx`
- 根因归类：挂旧目录 · 6.1
- 建议动作：见 §五·建议一

**P9 · llm-router 挂旧型号清单**　`中高`
- 文档位置：`agent-skills/llm-router.mdx:83`
- 线上：https://aisa.one/docs/agent-skills/llm-router　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/llm-router.mdx#L83
- 坑到谁：路由示例通篇用 `gpt-4.1`/`gpt-4o`/`o1`/`claude-3-*`/`gemini-1.5`/`gpt-3.5-turbo`，Agent 照抄会路由到已下线型号。
- 原文（可 Ctrl+F）：`| GPT | OpenAI | gpt-4.1, gpt-4o, gpt-4o-mini, o1, o1-mini, o3-mini |`
- 真值 / 复现：`grep -nE '^\| (OpenAI|Anthropic|Google Gemini) ' guides/models.mdx`
- 根因归类：挂旧目录 · 6.1
- 建议动作：见 §五·建议一

**P10 · deepseek-v3.1 上下文窗口写小一半**　`中高`
- 文档位置：`agent-skills/aisa-provider.mdx:124`
- 线上：https://aisa.one/docs/agent-skills/aisa-provider　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/aisa-provider.mdx#L124
- 坑到谁：Agent 按 `131072` 截断输入，浪费一半可用上下文（权威 `262144`），长文任务被无谓拒绝或截断。
- 原文（可 Ctrl+F）：`"contextWindow": 131072,`（`"id": "aisa/deepseek-v3.1"` 块内）
- 真值 / 复现：`grep -n 'deepseek-v3.1' guides/chinese-llms/deepseek.mdx` → line 21「`262,144`」
- 根因归类：同模型两套数 · 6.1
- 建议动作：见 §五·建议一

**P11 · Kimi/Moonshot 家族计数漏一个**　`中高`
- 文档位置：`agent-skills/aisa-provider.mdx:231`
- 线上：https://aisa.one/docs/agent-skills/aisa-provider　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/aisa-provider.mdx#L231
- 坑到谁：写「2 models」漏掉 `kimi-k2.6`，Agent 以为该家族只有两个模型，错过最新型号。
- 原文（可 Ctrl+F）：`**Kimi / Moonshot (2 models):**`
- 真值 / 复现：权威 3。`grep -n 'Moonshot' guides/models.mdx` → line 63「`| Moonshot | 3 | ... | kimi-k2-thinking, kimi-k2.5, kimi-k2.6 |`」
- 根因归类：同清单几个数 · 6.1
- 建议动作：见 §五·建议一

**P15 · 套利示例中英双版利润口径不一**　`中高`
- 文档位置：`agent-skills/prediction-market-arbitrage-zh.mdx:122`
- 线上：https://aisa.one/docs/agent-skills/prediction-market-arbitrage-zh　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/prediction-market-arbitrage-zh.mdx#L122
- 坑到谁：同组价 0.95，中文写「5.3% 利润」，英文写「0.05 edge」（=5%），Agent 跨版对账时拿到两个数。
- 原文（可 Ctrl+F）：`成本 ``0.95``，保证回报 ``1.00`` -> 5.3% 利润`
- 真值 / 复现：`grep -n '0.95' agent-skills/prediction-market-arbitrage.mdx` → line 56「`0.05` edge」（=5%），与中文「5.3%」不一
- 根因归类：复制串口径 · 6.3
- 建议动作：见 §五·建议三（中英双版收口同一算例）

**P17 · aisa-provider 自述 49+ 与紧邻枚举相加约 40 不符**　`中高`
- 文档位置：`agent-skills/aisa-provider.mdx:221`
- 线上：https://aisa.one/docs/agent-skills/aisa-provider　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/aisa-provider.mdx#L221
- 坑到谁：同页自述总数与下方枚举对不上，Agent 无从判断哪个为准。
- 原文（可 Ctrl+F）：`The full catalog includes **49+ models**:`
- 真值 / 复现：紧邻枚举（Qwen 8 + DeepSeek 4 + Kimi 2 + Claude 10 + GPT 9 + Gemini 5 + Grok 2 …）相加约 40。`sed -n '221,235p' agent-skills/aisa-provider.mdx`
- 根因归类：单篇算不平 · 1.6
- 建议动作：见 §五·建议三（单篇自洽）

**P18 · wallet 折扣阶梯并列 5%**　`中高`
- 文档位置：`guides/pricing/wallet.mdx:43`–`:44`
- 线上：https://aisa.one/docs/guides/pricing/wallet　·　git：https://github.com/AIsa-team/docs/blob/16863d3/guides/pricing/wallet.mdx#L43
- 坑到谁：称「充得越多折扣越高」却把 $50 与 $100 并列 5%，Agent 算最优充值档时被误导。
- 原文（可 Ctrl+F）：`$50 → 5% discount` / `$100 → 5% discount`
- 真值 / 复现：`grep -n '5% discount\|10% discount' guides/pricing/wallet.mdx`（$50、$100 同列 5%）
- 根因归类：单篇算不平 · 1.6
- 建议动作：见 §五·建议三

**P12 · provider 分项计数与权威目录不符**　`中`
- 文档位置：`agent-skills/aisa-provider.mdx:234`（另：`:228`）
- 线上：https://aisa.one/docs/agent-skills/aisa-provider　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/aisa-provider.mdx#L234
- 坑到谁：写 Anthropic 10 / OpenAI 9 / Gemini 5 / DeepSeek 4，权威为 7 / 8 / 2 / 6；Agent 据此判断各家族规模会偏。
- 原文（可 Ctrl+F）：`**Also available:** Claude series (10), GPT series (9), Gemini series (5)` / `**DeepSeek (4 models):**`
- 真值 / 复现：`grep -nE '^\| (OpenAI|Anthropic|Google Gemini|DeepSeek) ' guides/models.mdx` → OpenAI 8 / Anthropic 7 / Gemini 2 / DeepSeek 6
- 根因归类：同清单几个数 · 6.1
- 建议动作：见 §五·建议一

**P13 · cn-llm 声称覆盖 GLM/Baichuan 但定价表无对应行**　`中`
- 文档位置：`agent-skills/cn-llm.mdx:31`（声称）；`:8`
- 线上：https://aisa.one/docs/agent-skills/cn-llm　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/cn-llm.mdx#L31
- 坑到谁：Agent 以为可调 GLM/Baichuan，但同篇定价表无任何对应行，照调会失败。
- 原文（可 Ctrl+F）：`Choose between Qwen, DeepSeek, GLM, Baichuan, and related models.`
- 真值 / 复现：`grep -n 'GLM\|Baichuan' agent-skills/cn-llm.mdx`（仅出现在声称段，定价表无行）
- 根因归类：声称≠枚举 · 6.1
- 建议动作：见 §五·建议一

**P14 · cn-llm 列出权威目录缺位的模型 ID**　`中`
- 文档位置：`agent-skills/cn-llm.mdx:75`（另：`:82`、`:93`）
- 线上：https://aisa.one/docs/agent-skills/cn-llm　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/cn-llm.mdx#L75
- 坑到谁：`qwen3-max-2026-01-23`/`qwen-vl-max`/`deepseek-v3-0324` 在权威目录无规范行，Agent 调用真伪难判。
- 原文（可 Ctrl+F）：`| qwen3-max-2026-01-23 | $1.37/M | $5.48/M | Latest version |`
- 真值 / 复现：`grep -n 'qwen3-max-2026-01-23\|qwen-vl-max\|deepseek-v3-0324' guides/models.mdx`（权威目录无对应规范行）
- 根因归类：目录缺位 ID · 6.1
- 建议动作：见 §五·建议一

**P16 · stock-analysis 8 维评分权重合计 130%**　`高`
- 文档位置：`agent-skills/stock-analysis.mdx:82`–`:89`
- 线上：https://aisa.one/docs/agent-skills/stock-analysis　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/stock-analysis.mdx#L82
- 坑到谁：8 项权重 30+20+20+10+10+15+15+10 = 130% ≠ 100%，Agent 复现评分模型会算出错误归一化结果。
- 原文（可 Ctrl+F）：`| 1 | Earnings Surprise | 30% |` … `| 8 | Sentiment (Fear/Greed, shorts, insiders) | 10% |`
- 真值 / 复现：`grep -nE '\| [0-9]+ \|.*\| [0-9]+% \|' agent-skills/stock-analysis.mdx | head -8`（八项相加 = 130）
- 根因归类：单篇算不平 · 1.6
- 建议动作：见 §五·建议三

**P19 · cn-llm 代号 Terminus 未释义**　`中`
- 文档位置：`agent-skills/cn-llm.mdx:94`
- 线上：https://aisa.one/docs/agent-skills/cn-llm　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/cn-llm.mdx#L94
- 坑到谁：「Latest Terminus version」中 Terminus 无任何解释，Agent 无法判断它是版本代号还是型号。
- 原文（可 Ctrl+F）：`| deepseek-v3.1 | $4.00/M | $12.00/M | Latest Terminus version |`
- 真值 / 复现：`grep -n 'Terminus' agent-skills/cn-llm.mdx`（全篇无释义）
- 根因归类：代号未释 · 1.4
- 建议动作：见 §五·建议三

**P20 · us-stock-analyst 注释 last 30 days 实为 31 天**　`中`
- 文档位置：`agent-skills/us-stock-analyst.mdx:94`
- 线上：https://aisa.one/docs/agent-skills/us-stock-analyst　·　git：https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/us-stock-analyst.mdx#L94
- 坑到谁：注释写「last 30 days」，示例区间 `2025-01-01`～`2025-01-31` 实为 31 天，Agent 照注释推断窗口长度会偏。
- 原文（可 Ctrl+F）：`# Daily prices for last 30 days`
- 真值 / 复现：`sed -n '94,95p' agent-skills/us-stock-analyst.mdx`（`start_date=2025-01-01&end_date=2025-01-31` = 31 天）
- 根因归类：注释偏差 · 4.1
- 建议动作：见 §五·建议三

---

## 五、我们的建议：建立单一引用 + spec 自动派生，14 条同根缺口一次消解

按优先级，每条写明根治效果。

**建议一（最高优先级）· 为 agent-skills 建立对 `guides/models.mdx` + 定价页的单一引用，删除离群快照。**
把模型价、上下文窗口、家族 / 总数、端点路径这些跨页复用的事实，收口到那套 June 4 刷新、内部自洽的权威目录，agent-skills 各页改为引用而非重抄；同步删除各页自维护的离群价格、计数、端点、旧型号。
- 根治效果：**14 条 6.1 缺口一次性消解**——P1–P5、P7–P14、P17 全部随权威源单一化而消失，且杜绝下次再抄出新快照。

**建议二（次优先级）· 让 `agent-discovery.mdx` 的数字与分类表由 `openapi.yaml` 自动派生。**
schema 数、分类数、分类表均改为构建时从 spec 生成，而非手写固化。
- 根治效果：**B1、B2、B3 三项 BLOCKER 从源头杜绝**——spec 再长，文档跟着长，漂移不再发生。

**建议三（收尾）· 修两处单篇算不平 + 三处表述瑕疵。**
- `stock-analysis` 8 维权重 130% → 校正为 100%（P16）；`wallet` $50/$100 折扣并列 5% → 按单调阶梯校正（P18）；`aisa-provider` 49+ 与枚举对齐（P17）；P15 中英双版收口同一算例；P19 补释 Terminus；P20 注释与示例区间对齐。
- 根治效果：消解 P15–P20 共 6 条局部缺口，单篇内自洽。

---

## 六、附录

### 附录一 · 全部复现命令清单（源仓库根可独立跑，零 live 依赖）

```bash
# === 规模盘 ===
find . -name '*.mdx' | wc -l                                            # 743
grep -rl '^openapi:' --include='*.mdx' . | wc -l                        # 664 桩页
find guides -name '*.mdx' | wc -l                                       # 30 guides 散文
find agent-skills -name '*.mdx' | wc -l                                 # 43 agent-skills
ls openapi/*.json | wc -l                                               # 31 spec
find . -name '*.mdx' | grep -iE 'zh|chinese|/cn' | wc -l                # 11 中文页

# === BLOCKER 真值 ===
python3 -c "import yaml;print(len(yaml.safe_load(open('openapi.yaml'))['components']['schemas']))"   # 321 (B1)
python3 -c "import yaml;d=yaml.safe_load(open('openapi.yaml'));t=set();[t.add(x) for p in d['paths'].values() for m,o in p.items() if m in ('get','post','put','patch','delete') and isinstance(o,dict) for x in o.get('tags',[])];print(len(t))"   # 14 (B2)
python3 -c "import yaml;d=yaml.safe_load(open('openapi.yaml'));from collections import Counter;c=Counter();[c.update(o.get('tags',[])) for p in d['paths'].values() for m,o in p.items() if m in ('get','post','put','patch','delete') and isinstance(o,dict)];import json;print(json.dumps(dict(sorted(c.items())),ensure_ascii=False))"   # 14 类全名+操作数 (B3)
python3 -c "import yaml;print(len(yaml.safe_load(open('openapi.yaml'))['paths']))"   # 645 (INFO 路径数)
grep -nE '121 schemas|10 categories' guides/agent-discovery.mdx          # B1/B2 文档侧断言

# === 散文缺口（择要） ===
grep -rn 'qwen-plus-2025-12-01' guides/pricing/ai-model-pricing-llm-inference.mdx agent-skills/cn-llm.mdx   # P1
grep -rn 'qwen-mt-flash' guides/pricing/ai-model-pricing-llm-inference.mdx agent-skills/cn-llm.mdx          # P2
grep -rn 'deepseek-r1' guides/pricing/ai-model-pricing-llm-inference.mdx agent-skills/cn-llm.mdx            # P3
grep -rn 'financial/analyst-estimates\|financial/insider-trades' agent-skills/marketpulse.mdx               # P5 真实端点
grep -n 'cn' agent-skills/youtube-search-skill.mdx                                                          # P6
grep -n 'deepseek-v3.1' guides/chinese-llms/deepseek.mdx                                                    # P10 真值 262144
grep -n 'Moonshot' guides/models.mdx                                                                        # P11 真值 3
grep -nE '^\| (OpenAI|Anthropic|Google Gemini|DeepSeek) ' guides/models.mdx                                 # P8/P9/P12 权威目录
```

### 附录二 · 完整缺口明细

- **3 项 BLOCKER**（B1–B3）：详见 §4.1，逐项带证据字段。
- **20 条散文缺口**（P1–P20）：详见 §4.2，逐项带证据字段。
- 按严重度：高 7（P1–P6、P16）、中高 8（P7、P8、P9、P10、P11、P15、P17、P18）、中 5（P12、P13、P14、P19、P20）。
- 按规范点：6.1 共 14 条（主病灶）、6.3 一条（P15）、1.6 三条（P16/P17/P18）、1.4 一条（P19）、4.1 一条（P20）。

### 附录三 · 撤回 / 待人工确认台账（透明留痕）

阶段二去向台账：**47 原始线索 = 20 保留 + 21 并入 + 6 撤回**，账平。

撤回（守两条硬线：证据搜不到 / 有消歧原文）——具名留痕：
- GitHub 组织名 `AIsa-skills`：在 agent-skills 任一页 Ctrl+F 未命中，证据搜不到 → 撤回（仅存在于 guides/learn 页，已在试点处理，不重复计）。
- cn-llm 裸 `qwen-plus`/`qwen-max` 别名行：原文 Ctrl+F 未命中 → 撤回。
- 其余并入降级项见 `reports/ai-friendly-prose-2026-06-26.md` §四。

待人工确认（5 处，证据偏弱或作用域差异，未硬报）：
- Kimi `temperature=1.0 only` vs cn-llm `0-2 默认 1`：经核对约束的是不同模型，非同一对象 → 待两篇交叉声明各自适用范围。
- polymarket status 枚举、财务 macro 路径、last30days 信息源 8 vs 9、youtube/twitter slug：量级或措辞差异但未构成确定取值冲突。

阶段一撤下（D-006）：「技能计数 13 vs 43」——A2A agent card 广播的 13 个 skill 与 `agent-skills/` 43 个安装页是两个不同概念，文档「13」与其自身 13 行技能表内部自洽，无法仅凭源码证伪，按零误报红线撤下，不计 BLOCKER。

INFO（内容缺口 / 陈旧，非阻断）：
- 中文覆盖率约 1.5%（11/743）。
- `agent-discovery.mdx:16` 写「111+ paths」，实为 645——带 `+` 字面为真，仅标陈旧低估。

### 附录四 · 待负责人决断

本报告不产出新事实、不改已定结论。审计过程中无新发现的缺口或与已定结论的矛盾需提请决断；如后续推动上游修复，建议以 §五·建议一（建立单一引用）为纲领落地，并据本附录三的「待人工确认 5 处」安排一次人工复核以决定是否立案。
