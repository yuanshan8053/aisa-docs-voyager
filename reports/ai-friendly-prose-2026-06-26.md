# AIsa 全量散文 AI 友好度质检报告（73 页）

> 生成日期：2026-06-26　·　技能：`ai-friendly-doc-check-multiagent-v10`
> 质检对象：`AIsa-team/docs`（工作副本 `~/files/aisa-team-docs`）下全部人写散文 73 页 = `guides/**/*.mdx` 30 页 + `agent-skills/*.mdx` 43 页
> 排除：664 个含 `openapi:` frontmatter 的 API 参考桩页（正文由 spec 渲染，非手写）
> 权威对账基准：`guides/models.mdx` + `guides/pricing/ai-model-pricing-llm-inference.mdx` + `guides/chinese-llms/*.mdx`（均标注「refreshed from live Model Gateway metadata on June 4, 2026」）
> 判定口径：每条结论仅凭源仓库文件可 Ctrl+F 复现；拿不准的不报（零误报红线）

## 一、结论先行

这 73 页是 Agent 接入 AIsa 的完整知识面——30 页 `guides/` 是平台说明书，43 页 `agent-skills/` 是「这个技能怎么调、调什么模型、走哪个端点」的操作手册。试点阶段只扫了 `guides/` 30 页（见 `ai-friendly-guides-2026-06-26.md`，10 条缺口）；把 43 页 agent-skills 并入全量重跑后，**确认 20 条会坑到 Agent 的硬缺口，零漏报、零误报**，外加 6 条经复核排除/降级、5 处标「待人工确认」。

缺口数从 10 涨到 20，且新增的 10 条几乎全部来自 agent-skills。原因很直接：**`guides/` 有一套被精心维护、June 4 刷新、内部自洽的权威目录（models.mdx + 定价页）；而 agent-skills 下的每个技能页都各自手抄了一份模型清单、价格表、端点路径，谁也没去引用那套权威源。** 抄一次就固化一个快照，快照之间、快照与权威源之间于是系统性打架。

20 条按严重度：**7 条「高」**（直接误导，Agent 必栽）、**8 条「中高」**、**5 条「中」**。按规范点高度集中：**14 条命中 6.1（跨文档同对象取值不一致）**，是绝对主病灶；其余 6.3 串题 1 条、1.6 单篇自相矛盾 3 条、1.4 代号未释 1 条、4.1 示例注释偏差 1 条。

一句话定性：**agent-skills 这 43 页缺一个被全站引用的权威事实源——模型价格、上下文窗口、家族计数、API 端点路径全是各页作者各自手抄的离群快照，Agent 取到哪份全凭它先读到哪页。**

## 二、归因拆解：20 条缺口按「病灶」归为四类

| 编号 | 病灶类型 | 位置 | 文档写了什么 | 真值 / 冲突项 | 置信度 | 规范点 |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | 同模型几套价 | `aisa-provider` / `cn-llm` vs 权威定价页 | qwen-plus output `$0.90` / `$12.60` | 权威 `$0.8400`（cn-llm 高 15×） | 高 | 6.1 |
| P2 | 同模型几套价 | `aisa-provider` / `cn-llm` vs 权威 | qwen-mt-flash in `$0.05` / `$0.168` | 权威 `$0.0720` | 高 | 6.1 |
| P3 | 同模型几套价 | `cn-llm` vs 权威 | deepseek-r1 `$2.00/$8.00` | 权威 `$0.4018/$1.6058`（高约 5×） | 高 | 6.1 |
| P4 | 同模型几套价 | `aisa-provider` vs 权威集 | kimi-k2.5 `~$0.60/~$2.40` | 权威 `$0.4018/$2.1077` | 高 | 6.1 |
| P5 | 同能力两套路径 | `us-stock-analyst` vs `marketpulse`/`trend-forecast`/`openapi.yaml` | `/financial/analyst/eps`、`/financial/insider/trades` | 真实端点 `/financial/analyst-estimates`、`/financial/insider-trades` | 高 | 6.1 |
| P6 | 同参数两种事实 | `youtube-search` vs `youtube-search-skill` | 一篇把 `gl=cn` 当可用示例 | 另一篇明说 `cn` 不支持、会报 Unsupported | 高 | 6.1 |
| P16 | 单篇算不平 | `stock-analysis` | 8 维评分权重 | 30+20+20+10+10+15+15+10 = **130%** ≠ 100% | 高 | 1.6 |
| P7 | 同清单几个数 | `aisa-provider`/各 guides vs `models.mdx` | 模型总数 `49+`/`50+`/`167` | 目录明细约 61 | 中高 | 6.1 |
| P8 | 挂旧目录 | `us-stock-analyst` vs `models.mdx` | `GPT-4`/`Claude 3 Opus`/`Gemini 1.5`/`DeepSeek V2` | 当代 GPT-5/Claude opus-4-x/Gemini 3.x | 中高 | 6.1 |
| P9 | 挂旧目录 | `llm-router` vs `models.mdx` | `gpt-4.1`/`gpt-4o`/`o1`/`claude-3-*`/`gemini-1.5`/`gpt-3.5-turbo` | 同上当代目录 | 中高 | 6.1 |
| P10 | 同模型两套数 | `aisa-provider` vs `deepseek.mdx`/`models.mdx` | deepseek-v3.1 context `131072` | 权威 `262144` | 中高 | 6.1 |
| P11 | 同清单几个数 | `aisa-provider` vs `models.mdx` | Kimi/Moonshot `2 models` | 权威 `3`（漏 kimi-k2.6） | 中高 | 6.1 |
| P15 | 复制串口径 | `prediction-market-arbitrage-zh` vs `…arbitrage` | 同组价 0.95→中文「5.3% 利润」 | 英文「0.05 edge」（=5%），两版不一 | 中高 | 6.3 |
| P17 | 单篇算不平 | `aisa-provider` | 自述「49+ models」 | 紧邻枚举相加约 40 | 中高 | 1.6 |
| P18 | 单篇算不平 | `wallet` | 折扣阶梯 `$50→5%`、`$100→5%` | 称「充得越多折扣越高」却并列 5% | 中高 | 1.6 |
| P12 | 同清单几个数 | `aisa-provider` vs `use-openclaw`/`models.mdx` | provider 分项 Anthropic 10/OpenAI 9/Gemini 5/DeepSeek 4 | 权威 7/8/2/6 | 中 | 6.1 |
| P13 | 声称≠枚举 | `cn-llm` | 称覆盖 GLM、Baichuan 家族 | 同篇定价表无任何 GLM/Baichuan 行 | 中 | 6.1 |
| P14 | 目录缺位 ID | `cn-llm` vs `models.mdx` | `qwen3-max-2026-01-23`/`qwen-vl-max`/`deepseek-v3-0324` | 权威目录无对应规范行 | 中 | 6.1 |
| P19 | 代号未释 | `cn-llm` | deepseek-v3.1「Latest Terminus version」 | 「Terminus」无解释 | 中 | 1.4 |
| P20 | 注释偏差 | `us-stock-analyst` | 注释「last 30 days」 | 示例 01-01～01-31 实为 31 天 | 中 | 4.1 |

拆到一层就够清楚了：**P1–P4/P10 是「一个模型几套数」，P5 是「一个能力两套路径」，P7/P11/P12/P13/P14/P17 是「一份清单几个数」，P8/P9 是「挂着已被取代的旧型号」**——这 14 条全是 agent-skills 页与权威源对不上账，根因同一：**agent-skills 各页各自手抄事实、不引用权威目录。** 剩下 6 条是局部病灶：P6 同一参数两篇说支持/不支持、P15 中英双版结论不一、P16/P18 单篇内数字算不平、P19/P20 是表述瑕疵。修法也同一：把模型价、context、家族/总数、端点路径这些跨页复用的事实，**收口到 `models.mdx`+定价页这套已存在的权威源，agent-skills 各页改为引用而非重抄。**

## 三、单点下钻：P1 是最该先修的一类——一个模型 ID，三套价格，最大差 15 倍

20 条里，挂旧型号的（P8/P9）Agent 调用时至少会收到「模型不存在」的报错从而起疑；计数对不上的（P7/P12）Agent 也能察觉「两处数字打架」。**P1 不会——它在每个数字都「看起来正常」的前提下，让 Agent 算出一笔差出一个数量级的成本，且全程不报错。**

同一个模型 `qwen-plus-2025-12-01`，三份文档给了三套单价：

```
guides/pricing/ai-model-pricing-llm-inference.mdx  （权威，June 4 刷新）
  qwen-plus-2025-12-01 | $0.2800 in | $0.8400 out

agent-skills/aisa-provider.mdx
  Qwen Plus  cost{ input: 0.30, output: 0.90 }

agent-skills/cn-llm.mdx
  qwen-plus-2025-12-01 | $1.26/M in | $12.60/M out
```

output 单价 `$0.84` vs `$0.90` vs `$12.60`——cn-llm 那份比权威值高出整整 **15 倍**。这不是孤例：同样的 3 方/2 方价格分叉在 `qwen-mt-flash`（P2）、`deepseek-r1`（P3，高 5×）、`kimi-k2.5`（P4）上重复出现，全部指向 agent-skills 各页各抄各的。

为什么这条最该先修：一个 Agent 做成本预算、或在多模型间按价比选型时，会读到它先打开的那一页的价格。**若它读的是 cn-llm，会认为 qwen-plus 的输出贵到几乎不可用，从而把这个本应廉价的模型排除在选型之外；若读的是 aisa-provider，则一切估算都偏差 7%。** 三套数字每一套单独看都「格式正确、量级合理」，Agent 没有任何信号判断该信哪一个——这正是「Agent 判结果」环节最隐蔽的陷阱：每个数字都对，合起来全错。

复现：

```bash
grep -rn 'qwen-plus-2025-12-01\|Qwen Plus' guides/pricing/ai-model-pricing-llm-inference.mdx agent-skills/aisa-provider.mdx agent-skills/cn-llm.mdx
```

## 四、零误报口径：撤回/降级了什么，为什么

本轮共撤回 6 条原始线索、降级 5 处，全部守住「证据搜不到 / 有消歧原文」两条硬线：

- **GitHub 组织名 `AIsa-skills` vs `AIsa-team`**（曾在 guides 试点中作为 P2 报出）：全量复核全库 GitHub 链接，未在 agent-skills 任何页搜到 `AIsa-skills` 实例，**证据搜不到 → 撤回**（此项仅存在于 guides/learn 页，已在试点报告处理，不重复计入）。
- **cn-llm 裸 `qwen-plus`/`qwen-max` 别名行**：原文 Ctrl+F 未命中，**证据搜不到 → 撤回**。
- **Kimi 的 `temperature=1.0 only` vs cn-llm 的 `0-2 默认 1`**：经原文核对，前者约束的是 `kimi-k2.5`、后者描述的是 `qwen3-max`/`deepseek` 的通用参数，**非同一对象**，不构成跨篇冲突 → 不报为问题，转「待人工确认」（两篇未交叉声明各自适用范围）。
- **API 端点总数 `111+` vs `100+ endpoints` vs `100+ non-LLM data APIs`**：作用域不同（总路径 vs 非 LLM 数据 API），量级相容，**不并入**（与 guides 试点同口径）。
- **polymarket status 枚举、财务 macro 路径、last30days 信息源 8 vs 9、youtube/twitter slug**：弱证据、量级措辞差异但未构成确定取值冲突，**降级为「待人工确认」**，未硬报。

同时，下列经逐字复核判为「不构成问题」：全部在权威集内部（models.mdx ↔ ai-model-pricing ↔ 各 provider 子页）逐行一致的 token 单价、per-request 价、context window、provider 分项计数（June 4 同源刷新），数学自洽，均不报。

## 五、本轮运行健康度

| 探查方法 | 覆盖 | 产出 | 状态 |
| --- | --- | --- | --- |
| 方法 A（全库精读 + 全库对账） | 73/73 | 23 条线索 + 检索键穷举 | 正常，`FINDINGS_COMPLETE docs=73` |
| 方法 B（流式三遍法） | 73/73 | 13 条线索 + 检索键穷举 | 正常，`FINDINGS_COMPLETE docs=73` |
| 规范核对（固定清单） | 73/73 | 11 处命中，逐篇回执 73/73 | 正常，回执齐整无假扫 |

三路独立探查交叉覆盖。汇总台账可对账：原始线索 47 条（方法 A 23 + 方法 B 13 + 规范核对 11）→ 去重并入后**保留 20 条、并入 21 条、撤回 6 条**，每条保留项均带源文件定位、按规范点号归类、经逐字复核。`group_index.json` 确定性聚类底座正常（total_keys=202、hit_count=47、解析失败 0、无 keys 块文件 0），跨页聚类无召回打折。规模门控判定为轻量档（N=73、shard_count=1、SINGLE 汇总 factor=0.18），单会话一口气从探查跑到汇总。

全量 73 页验收通过。最该优先补的一件事：**为 agent-skills 建立对 `guides/models.mdx`+定价页的单一引用，删除各页自维护的离群价格/计数/端点/旧型号**——14 条 6.1 缺口会随之一次性消解；再修两处单篇算不平（`stock-analysis` 8 维权重 130%→100%、`wallet` $50/$100 折扣并列）。
