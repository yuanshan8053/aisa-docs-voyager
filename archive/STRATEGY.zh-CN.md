# AIsa 技术文档作品集 · 策略简报

**投递岗位：** Developer Advocate / Developer Relations Engineer（面向中国开发者市场）
**作品定位：** 不是「我能写文档」，而是「我能把文档变成一个由 AI Agent 自动运转的系统」。

---

## 一、为什么是这份作品

AIsa 的定位是「Agent 经济的能力层」——它的文档不只是给人看的，**更是给 Agent 读的契约**(`llms.txt`、`agent-card.json`、`ai-plugin.json`、`mcp.json`)。文档同时具备三个特征：

1. **体量大**：`llms.txt` 索引了 773 个页面；
2. **机器可发现**：Agent 被明确引导去 fetch 这些 well-known 端点；
3. **自动生成**：技能/模型目录由线上网关同步，而非手写。

这三点叠加，产生一类**必然反复发生的系统性故障：文档（给人的 prose）和线上契约（给机器的 contract）会漂移(drift)**。一个相信文档的 Agent，会拿到一条坏掉的指令。

普通技术作者会去「改错别字、补一页文档」。而文档负责人要解决的是：**让这类漂移再也无法悄悄发生**。这正是本作品做的事。

---

## 二、我挖到的真实缺口（全部可复现、附线上证据）

下表每一项都由作品中的 `aisa-doc-reality-auditor` 工具**实时抓取线上源**自动判定，不是人工臆测。审计运行时间：2026-06-26(UTC)。

| 严重度 | 缺口 | 证据（线上，可复现） |
| --- | --- | --- |
| 🔴 阻断 | **发现端点已失效** | `ai-plugin.json` 的 `api.url` 与 agent-discovery 指南都让 Agent 去取 `https://aisa.one/openapi.yaml`，实际返回 **404**。真实的 spec 是 `/docs/openapi/` 下的 30 个分散文件。 |
| 🔴 阻断 | **文档与现实计数漂移** | agent-discovery 指南写「advertises **13** skills」，而线上 `agent-card.json` 实际广播 **45** 个 skill。 |
| 🔴 阻断 | **中文覆盖率仅 1.3%** | `llms.txt` 中 773 个页面只有 10 个是中文；`chinese-llms.md` 讲国产模型却是全英文；**没有中文快速开始**。而中国是这个网关主打的模型供给市场。 |
| 🟡 警告 | **契约形态自相矛盾** | 指南承诺「一个聚合 spec、111+ 路径」，线上却是 30 个分服务 spec、且聚合文件不存在。 |

> 复现方式：`python -m aisa_doc_auditor.auditor`（无需 API Key，审计对象全为公开资源）。

**为什么 (3) 是对这个岗位「最优价值」的场景：** 岗位的核心是「面向中国开发者市场」「打磨 first success experience」。而现状是——一个中国开发者想用 AIsa 调用 DeepSeek/Qwen,**第一步就没有中文路径可走**。这是离收入和留存最近的缺口，也是这个岗位能立刻产生影响的地方。

---

## 三、我做出的改变（作品三件套）

### 1. `aisa-doc-reality-auditor` —— 把 Agent 放进文档系统里

一个无需鉴权、可独立运行的漂移检测 Agent。每次运行都**实时抓取线上权威源**，对四类缺陷给出带证据、带修复建议的结论：

- 失效的发现端点（prose/manifest 让 Agent 去取、实际取不到的 URL）;
- 计数漂移（指南里手写的数字 vs 线上真实数量）;
- 本地化覆盖率（中文页面占比）;
- 时效性（指南里 "last refreshed" 时间戳的陈旧程度）。

输出人类可读的 Markdown + 机器可读的 JSON，并支持 `--ci` 模式（发现阻断项即 `exit 1`）。

### 2. `doc-reality-check.yml` —— 让它自动运转

GitHub Actions 工作流，把审计 Agent 嵌入文档开发业务系统：

- **每个 docs PR**：阻断会引入漂移的合并，并把报告作为 PR 评论贴出，作者立刻看到「哪句话和线上契约对不上」;
- **每 6 小时定时**：捕捉上游网关自动同步带来的、没有任何 PR 的漂移，自动开/更新一个 `doc-drift` Issue，交给本地化与修复 Agent 接力。

**人类不再充当 prose 与 live contract 之间的 diff 引擎——这件事交给 Agent 自动做。**

### 3. `quickstart.zh-CN.md` —— 补上最贵的那一页

面向中国开发者的中文快速开始：三步跑通（注册领额度 → 改两行 → 发第一个请求），含 cURL / Python / TypeScript 三种可直接复制的代码，以及国产模型（Qwen/DeepSeek/Kimi/GLM/MiniMax/豆包 Seed）型号速查表与高频 FAQ。

代码已对着**真实网关验证**：`POST https://api.aisa.one/v1/chat/completions` 返回 `401 invalid api key`（路由存在、契约正确），而非 404。页面头部带 `last_synced` 与 `source_of_truth`，本身就是可被审计 Agent 检查的对象。

---

## 四、这套东西如何对应岗位职责

| 岗位职责 | 本作品如何回应 |
| --- | --- |
| 高质量中文开发者文档、快速上手、first success | `quickstart.zh-CN.md`:把中国开发者的「第一次成功」从「无路可走」变成「5 分钟跑通」。 |
| 可运行示例、SDK 示例 | 快速开始内三语言示例，全部经真实端点验证。 |
| 反馈闭环，驱动 API/文档/DX 迭代 | 定时审计自动把线上漂移转成 `doc-drift` Issue，形成「检测→工单→修复」闭环。 |
| 技术验证，以外部开发者视角发现接入坑 | 我以外部开发者身份跑通时发现的 `openapi.yaml` 404、13 vs 45 漂移，已固化成可回归的自动检查。 |
| 系统层面解决问题、让 Agent 自动运转 | 审计 Agent + CI 工作流，把「防止文档腐烂」从一次性人工劳动变成持续自动机制。 |

---

## 五、随时获取最新版本

作品不依赖任何快照。所有判断都来自每次运行时实时抓取的：

- `https://aisa.one/docs/llms.txt` —— 文档总索引
- `https://aisa.one/.well-known/agent-card.json` —— 技能广播（权威）
- `https://aisa.one/.well-known/ai-plugin.json` —— 插件清单
- `https://aisa.one/docs/guides/agent-discovery.md` —— 被审计的 prose

这意味着：**今天的结论，明天再跑会自动更新**。文档若被修好，审计会自动转绿；若上游又引入新漂移，审计会自动抓到。这正是「让 AI Agent 融入文档开发业务系统、自动运转」的含义。
