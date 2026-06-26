# 散文 AI 友好度质检：方法沉淀

> 生成日期：2026-06-26　·　技能：`ai-friendly-doc-check-multiagent-v10`
> 适用：阶段二（散文 AI 友好度质检）。本文讲清三件事——**怎么调、规模档位怎么判、零误报怎么守**——供接手 agent 复跑或铺到其他仓库时照做。

## 一、这套方法在解决什么

阶段一的静态检查器（`checks/src_consistency.py`）只能抓「机械可证伪的硬伤」——schema 计数、分类条数这类能被 `openapi.yaml` 一键比对的结构错。但**散文里的坑是语义级的**：同一个模型在三页里写了三套价、同一个 registry 给了两个 GitHub 地址、列名叫 `Tokens` 而说明写的是 API key。这些错每一处单独看都「格式正确、量级合理」，静态规则抓不到，得靠「读懂语义 + 跨页对账」。

于是阶段二改用 `ai-friendly-doc-check-multiagent-v10` 这套 **Map-Reduce 多 agent 质检**：用多个互相隔离的探查 agent 并行精读（Map），再用单个汇总 agent 去重、复核、归类（Reduce）。判定红线只有一条——**会不会坑到 Agent**：查资料拿错值、调工具找错地方、判结果对不上账、排障查错方向。

## 二、怎么调（调用方式）

### 2.1 Map 阶段：三路独立探查，三层隔离

同一批文档，三个探查 agent 用**不同方法各扫一遍**，交叉覆盖以压低漏报：

| 探查方法 | agent | 干法 |
| --- | --- | --- |
| 方法 A | `finder_v2` | 全库精读 + 全库对账（`shard_count=1` 时按整库一次性读完、自己做跨库对账）|
| 方法 B | `finder_v3` | 流式三遍法：Pass A 单篇精读 → Pass B 跨篇穷举 → Pass C 合并复核 |
| 规范核对 | `floor` | 按固定清单（1.1–6.3）逐篇核对，产出逐篇覆盖回执 |

**三层隔离是这套方法的关键设计**，目的是防止「分类框架」污染探查、制造确认偏误：

1. **探查 agent（A/B）永远看不到分类体系**——它们只管「凭五问标尺找会坑到 Agent 的地方」，不知道有 1.1–6.3 这套编号。
2. **规范核对 agent（floor）只拿到固定清单**（`floor.md` 的 1.1–6.3 条目），不拿到汇总端的归类逻辑。
3. **只有汇总 agent 看得到 `categories.md`**（唯一权威分类源），由它把探查产出的「自然语言问题」回贴到规范点号。

每个探查 agent 完成后必须在文件末尾落标记 `=== FINDINGS_COMPLETE <id> docs=<N> ===`，N 必须等于应扫页数，否则视为未跑完。

### 2.2 Reduce 阶段：先聚类，再单汇总

探查全部 COMPLETE 后，按以下顺序收口（轻量档，无台账）：

1. `python3 scripts/group_keys.py <findings_dir> --json <out>/group_index.json`
   —— 把三个 findings 里的 `keys` 机器块按本体（obj+attr）确定性聚类，产出跨页对账底座。本轮 `total_keys=202`、`hit_count=47`、`parse_errors=[]`、`files_without_keys_block=[]`，聚类无召回打折。
2. `python3 scripts/plan_shards.py "$PWD" --files <list> --json /tmp/shard_plan.json`
   —— 产出规模计划（见第三节）。**务必带 `--json`**：不带时输出是给人看的渲染文本，下游 `aggregate-plan` 会 JSONDecodeError。
3. `python3 scripts/progress_ledger.py aggregate-plan --run-dir <dir> --plan /tmp/shard_plan.json`
   —— 算汇总 factor，判 SINGLE 还是 SPLIT。
4. factor≤1 → 派**一个**汇总 agent。汇总 agent 按 `aggregator.md` 流程（输入校验 → 合并去重 → 逐字复核 → 消费 group_index 做 0-漏报全库对账 → 回贴规范点号 → 置信度加权 → 扩库归纳），**以消息返回报告**，主 agent 负责落盘——汇总 agent 不能写文件。

### 2.3 报告体例

最终报告按 `WRITING-STANDARD` 的 **2.5 维叙事** 写：维度 1 结论先行（全局定性）→ 维度 2 归因拆解（**只拆一层**，按病灶类型列表）→ 维度 2.5 单点下钻（挑一条最典型的硬缺口讲透）。中文标点、中英文间空格、一次成稿、控制篇幅。

## 三、规模档位怎么判

`plan_shards.py` 按页数 N、总字节、各方法分片数三个维度算档位。本轮输入 73 页（30 guides + 43 agent-skills），`total_bytes=453235`：

| 字段 | 值 | 含义 |
| --- | --- | --- |
| `N` | 73 | 应扫页数 |
| `shard_count` | 1 | 方法 A 不分片 → 派为**全库 agent**，自己做全库对账 |
| `split_singles` | false | 不拆单篇 agent |
| `batches` | [3] | 三个探查 agent 一批并行 |
| 档位 | 轻量 | 单会话一口气跑完，**不建进度台账** |

汇总 factor 公式：`factor = max(findings_bytes/600000, hit_count/300, N/2000)`。本轮 `= max(0.18, 0.16, 0.04) = 0.18 ≤ 1 → SINGLE`，单汇总 agent。

判定逻辑一句话：**页数小、字节小、命中少 → 轻量档 → 单会话 + 单汇总 + 无台账**；只有当任一维度顶破阈值（factor>1 或 shard_count>1）才升级为分片探查 / 多汇总 / 带台账续跑。`shard_count==1` 是个要点——此时方法 A 不再被「别对整库下结论」约束，反而被指派为全库对账主力（`SKILL.md` 第 121 行）。

## 四、零误报怎么守

零误报是这套方法的红线——**拿不准的宁可不报**。机制有四道：

1. **两条硬线撤回律**：一条线索只有满足「源文件 Ctrl+F 搜得到原文证据」才可能保留；只要满足「证据搜不到」**或**「存在消歧原文（两处其实指不同对象 / 上下文已说明差异）」，立即撤回。本轮据此撤回 6 条（如 `AIsa-skills` 组织名在 agent-skills 任何页都搜不到 → 撤回；Kimi 的 `temperature` 约束与 cn-llm 的通用参数描述经核对指不同模型 → 非同一对象，转待人工确认）。
2. **逐字复核**：每条保留项的「文档写了什么 / 真值是什么」都必须回到源文件逐字核对，不凭探查 agent 的转述定罪。
3. **去向台账可对账**：原始线索总数 = 保留 + 并入 + 撤回，三者相加必须等于原始数，缺口即意味着有线索没交代去向。本轮 **47 原始 = 20 保留 + 21 并入 + 6 撤回**，账平。
4. **权威源单一化**：跨页复用的事实（模型价、context、家族/总数、端点路径）一律以 `guides/models.mdx` + `pricing/ai-model-pricing-llm-inference.mdx` + `chinese-llms/*.mdx`（均 June 4 刷新、内部逐行自洽）为真值；agent-skills 各页的离群快照才是被告，权威集内部一致的值绝不报。

四道合起来的效果：**主病灶（agent-skills 各页手抄事实、不引用权威目录）被 14 条 6.1 缺口精确指认，同时把「概数 50+ vs 精确 57」「100+ 端点 vs 111+ 路径作用域不同」这类相容项稳稳挡在报告外。**
