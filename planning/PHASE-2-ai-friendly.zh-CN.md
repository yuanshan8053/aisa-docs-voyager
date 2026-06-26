# 阶段二 · AI-friendly 质检

**阶段目标**：用 `ai-friendly-doc-check-multiagent-v10` 技能，对 AIsa 文档中真正可读的散文页做系统性 AI 友好度质检，产出零漏报、零误报的质检报告，先试点再铺开。

**为什么是这些页**：664 个 API 参考页是桩页（正文由 spec 渲染生成，非手写），不是散文质检对象。真正该查的是 `guides/`（30 页）+ `agent-skills/`（43 页）= 73 页人写散文——这才是「Agent 拿去办事会不会栽跟头」的判定对象。

---

## 输入边界

- **质检对象**：源仓库 `~/files/aisa-team-docs` 下 `guides/**/*.mdx`（30 页）+ `agent-skills/*.mdx`（43 页）。
- **排除**：664 个含 `openapi:` frontmatter 的 API 参考桩页一律排除。
- **试点优先**：先跑 `guides/`（30 页，含 `agent-discovery.mdx`、`chinese-llms/*`），验收通过再加 `agent-skills/`（共 ~73 页）。

## 验收产物（缺一不可）

1. 试点质检报告 `reports/ai-friendly-guides-<日期>.md`（+ 技能产出的 JSON/findings）。
2. 全量质检报告 `reports/ai-friendly-prose-<日期>.md`（73 页）。
3. `reports/ai-friendly-method.zh-CN.md` — 记录调用方式、分片/规模档位、零误报复核机制，便于复跑。
4. 回写 `project/STATE.md`、`project/DECISIONS.md`（若有新决策）。

## 验收标准

- 每条问题都经技能的「逐字复核」环节确认，零误报；高召回、零漏报。
- 报告按问题严重度与规范点号归类，每条带源文件定位。
- 报告遵循 `WRITING-STANDARD.zh-CN.md`。

---

## 自包含委派提示词（复制给新 session agent）

> 你接手 AIsa 文档质量工程的「阶段二：AI-friendly 质检」。你之前没有本项目上下文，请严格按下文执行。
>
> **背景**：AIsa 是 OpenAI 兼容的 AI 能力网关。它的文档既给人看也给 AI Agent 读。我们要查清这些文档里「会害 AI Agent 查资料/调工具/判结果/排障栽跟头」的硬缺口，零漏报零误报，结果交产品负责人。
>
> **第一步 · 读权威信息源**：依次读 `~/files/aisa-docs-voyager/project/CHARTER.md`、`project/STATE.md`、`project/DECISIONS.md`、`project/baselines/FACTS.zh-CN.md`、`~/files/aisa-docs-voyager/WRITING-STANDARD.zh-CN.md`。
>
> **第二步 · 确认输入与边界**：质检对象是 `~/files/aisa-team-docs` 下的 `guides/**/*.mdx`（30 页）+ `agent-skills/*.mdx`（43 页）。**必须排除**所有 frontmatter 含 `openapi:` 的 API 参考桩页（664 个）——它们正文由 OpenAPI spec 渲染生成，不是手写散文，不在本阶段范围。若源仓库不在，用项目指令里的 PAT 克隆（PAT 永不明文打印）。
>
> **第三步 · 调用质检技能**：使用 `ai-friendly-doc-check-multiagent-v10` 技能（在 `/data/plugins/custom/skills/` 下）。**先试点 `guides/`（30 页）**：把 30 个 .mdx 路径作为输入交给技能，按它的 Map-Reduce 编排跑（自由探查 + 规范核对 + 汇总归类 + 逐字复核）。30 页属轻量档，按技能的规模门控自适应，不必强开跨会话续跑台账。
>
> **第四步 · 验收试点**：检查技能产出，确认每条问题都经逐字复核、带源文件定位、按规范点号归类。生成 `reports/ai-friendly-guides-<今天日期>.md`，遵循 `WRITING-STANDARD.zh-CN.md`（2.5 维叙事：先全局结论、再按问题类型拆解、后下钻一条最典型的硬缺口）。
>
> **第五步 · 铺开全量**：试点结果合理后，把 `agent-skills/*.mdx`（43 页）并入，对全部 73 页跑一遍，产出 `reports/ai-friendly-prose-<今天日期>.md`。
>
> **第六步 · 沉淀方法 + 回写**：写 `reports/ai-friendly-method.zh-CN.md` 记录调用方式、规模档位判定、零误报复核机制；更新 `project/STATE.md`，新决策追加 `project/DECISIONS.md`。
>
> **约束**：不换仓库、不提 PR、不撤销凭证、PAT 永不明文打印、占位符 `[ph_..._ph]` 逐字节保留。零误报是红线——拿不准的问题宁可不报。完成后用一句话汇报验收产物清单。
