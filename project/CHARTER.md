# AIsa 文档质量工程 · 项目章程

> 本文件是项目的权威信息源。任何跨 session 的 agent 接手前先读它，再读 `STATE.md`（当前进度）与 `DECISIONS.md`（已定决策）。三者冲突时，以 `DECISIONS.md` 的最新决策为准。

---

## 一、项目是什么

AIsa 是一个 OpenAI 兼容的 AI 能力网关（法律实体 AIPay, Inc.），文档同时面向人和 Agent。本项目把「防止文档腐烂、并主动提升文档质量」从一次性人工劳动，做成一套可分阶段实施、可独立验收、证据确凿的文档质量工程。

**负责人定位**：文档负责人已正式入局。早期求职作品集叙事已废弃（见 `../archive/`），现在的唯一受众是 AIsa 产品负责人，唯一标准是真实、可复现、可交付。

---

## 二、文档生产链路（已查清）

```
AIsa-team/docs            源仓库：.mdx 散文 + openapi/*.json + scripts/consolidate_openapi.py
      │  .github/workflows/sync-openapi.yml
      ▼
AIsa-team/new-style-landing-page   部署层
      ▼
https://aisa.one          线上：HTML 给人，.md 孪生页 + 发现契约给 Agent
```

- API 参考页（664 个）是桩页：frontmatter 指向 spec，正文由渲染层从 OpenAPI spec 内联生成。**线上渲染后的 API 参考正文是 spec 内联，不是手写 Markdown。**
- 发现契约：`/.well-known/agent-card.json`（A2A）、`ai-plugin.json`（OpenAI 插件）、`mcp.json`（MCP）、`/openapi.yaml`、`/docs/llms.txt`。

---

## 三、四条工作线

| 编号 | 工作线 | 一句话目标 | 依赖技能 | 阶段映射 |
| --- | --- | --- | --- | --- |
| ① | 硬伤质检 | 静态源码一致性检查器，零依赖零误报，发现确凿硬伤 | 无（自建 `src_consistency.py`） | 阶段一 |
| ② | AI-friendly 质检 | 对 73 页可读散文做 AI 友好度系统质检 | `ai-friendly-doc-check-multiagent-v10` | 阶段二 |
| ③ | OpenAPI 内容加强 | 产出独立增强版参考页 + 回写原 spec 的能力 | `api-doc-agent` | 阶段三 |
| ④ | ~~直出 md~~ | 已折叠进 ③（线上参考页本就是 spec 内联，非手写 md） | — | 已关闭 |

**为什么这样排**：① 零依赖、确定性最高、可立刻产出给产品负责人看的硬证据，先做。② 依赖外部技能但对象边界清晰（73 页散文），价值直接。③ 工程量最大、需人/LLM 撰写内容，且要新增回写能力，放最后并先用最小 spec 试点。

---

## 四、关键约束（不可违背）

1. **不换仓库**：项目资产留在 `aisa-docs-voyager`，早期内容已归档至 `archive/`。
2. **无写权限 + 暂不提 PR**：对 `AIsa-team/docs` 无写权限。所有阶段产物落本地，最终汇总成报告交产品负责人，不提 PR。
3. **静态为主、探索为辅**：阻断级结论必须能仅凭源仓库证伪；live 探测只作旁证。零误报是红线。
4. **每阶段独立**：独立实现、独立验收、有明确验收产物，并各自附自包含提示词供其他 session agent 实施。
5. **写作规范**：所有文字产出遵循 `../WRITING-STANDARD.zh-CN.md`（中文标点、中英文间空格、2.5 维叙事、一次成型、控篇幅）。
6. **安全**：GitHub PAT 在项目指令中，保留不撤销，永不明文打印。占位符 `[ph_..._ph]` 逐字节保留。

---

## 五、资产地图

```
aisa-docs-voyager/
├── project/                 ← 权威信息源（跨 session 共享）
│   ├── CHARTER.md           ← 本文件：项目是什么、四条线、约束
│   ├── STATE.md             ← 当前进度、阻塞、下一步（每次 session 必更）
│   ├── DECISIONS.md         ← 决策日志（只追加，不删改）
│   └── baselines/
│       └── FACTS.zh-CN.md   ← 静态可证基线事实 + 复现命令
├── planning/                ← 分阶段实施计划（每阶段一个自包含提示词）
│   ├── PHASE-1-hard-defects.zh-CN.md
│   ├── PHASE-2-ai-friendly.zh-CN.md
│   └── PHASE-3-openapi-enhance.zh-CN.md
├── checks/                  ← 阶段一交付：静态检查器（待建）
├── aisa_doc_auditor/        ← 早期 live-probe 审计器（旁证工具，保留）
├── tools/docs_mirror.py     ← 全量镜像工具（保留）
├── docs-mirror/             ← 本地镜像快照
├── archive/                 ← 早期求职作品集产物（已废弃）
└── WRITING-STANDARD.zh-CN.md
```

外部依赖（非本仓库）：
- `~/files/aisa-team-docs/` — `AIsa-team/docs` 源仓库工作副本，静态检查的输入。
- 专属技能：`/data/plugins/custom/skills/api-doc-agent`、`/data/plugins/custom/skills/ai-friendly-doc-check-multiagent-v10`。

---

## 六、跨 session 协作机制

接手任一阶段的 agent，按此流程工作：

1. **读三件套**：`CHARTER.md`（本文件）→ `STATE.md` → `DECISIONS.md`。
2. **领阶段**：打开 `planning/PHASE-N-*.zh-CN.md`，其中含自包含提示词、输入边界、验收产物清单。
3. **干活**：严格按提示词执行，产物落到该阶段指定目录。
4. **回写**：完成后更新 `STATE.md`（进度、阻塞、下一步），把新决策追加进 `DECISIONS.md`，把新核实的数字更新进 `baselines/FACTS.zh-CN.md`。
5. **不扩权**：不擅自改仓库结构、不提 PR、不撤销凭证。
