# 阶段一 · 硬伤质检（静态源码一致性检查器）

**阶段目标**：构建一个零依赖、确定性、零误报的静态检查器 `checks/src_consistency.py`，仅凭 `AIsa-team/docs` 源仓库文件就能判定确凿硬伤，并产出首份硬伤报告。

**为什么先做它**：不依赖任何外部技能、不依赖 live 网络，确定性最高，能最快产出可交给产品负责人的硬证据。它也为后续阶段确立「静态为主、零误报」的工程基线。

---

## 输入边界

- **唯一输入**：`AIsa-team/docs` 源仓库工作副本（本地 `~/files/aisa-team-docs`）。若不存在，用项目指令中的 PAT 克隆 `AIsa-team/docs`（PAT 永不明文打印）。
- **不读 live**：本阶段一律不发网络请求。live 探测属旁证，不在本阶段范围。
- **基线参照**：`project/baselines/FACTS.zh-CN.md`，但所有数字以检查器实跑为准。

## 验收产物（缺一不可）

1. `checks/src_consistency.py` — 静态检查器，可 `python checks/src_consistency.py --repo ~/files/aisa-team-docs` 运行，输出 JSON + Markdown 双格式，支持 `--ci`（发现 BLOCKER 退出码 1）。
2. `checks/README.md` — 说明每条检查规则的判定逻辑、源码定位方式、为什么零误报。
3. `reports/hard-defects-<日期>.md` 与 `.json` — 首份硬伤报告，每条结论附源码文件 + 行号 + 复现命令。
4. 回写 `project/STATE.md`、`project/baselines/FACTS.zh-CN.md`（更新实跑数字）、`project/DECISIONS.md`（若有新决策）。

## 验收标准

- 每条 BLOCKER 都能被人工仅凭源仓库文件复核证伪，零误报。
- 检查器对同一仓库多次运行结果稳定（确定性）。
- 报告遵循 `WRITING-STANDARD.zh-CN.md`。

---

## 自包含委派提示词（复制给新 session agent）

> 你接手 AIsa 文档质量工程的「阶段一：硬伤质检」。你之前没有本项目上下文，请严格按下文执行。
>
> **背景**：AIsa 是 OpenAI 兼容的 AI 能力网关，文档源仓库是 GitHub 上的 `AIsa-team/docs`（.mdx 散文 + openapi/*.json + scripts/）。我们要建一个静态检查器，仅凭源仓库文件就能发现确凿的文档硬伤，零误报，结果要交给产品负责人。
>
> **第一步 · 读权威信息源**：依次读 `~/files/aisa-docs-voyager/project/CHARTER.md`、`project/STATE.md`、`project/DECISIONS.md`、`project/baselines/FACTS.zh-CN.md`、`~/files/aisa-docs-voyager/WRITING-STANDARD.zh-CN.md`。这些是项目的真相来源。
>
> **第二步 · 确认输入**：确认 `~/files/aisa-team-docs` 存在且是 `AIsa-team/docs` 的工作副本（`git -C ~/files/aisa-team-docs remote -v`）。若不存在，用项目指令里的 GitHub PAT 克隆（PAT 绝不能明文出现在任何输出、日志、文件里）。
>
> **第三步 · 实现 `checks/src_consistency.py`**，至少覆盖以下三类确定性检查，每条都必须能仅凭源仓库文件判定：
>   1. **计数漂移检查**：扫描 `guides/*.mdx` 中硬编码的数字断言（如「advertises N skills」「N paths」），与源仓库目录实际计数（如 `agent-skills/*.mdx` 文件数）比对。已知样本：`guides/agent-discovery.mdx:14,97` 写死「13 skills」，而 `agent-skills/` 实有 43 页。规则要可配置「散文断言 → 真值来源」映射，便于扩展。
>   2. **发现契约一致性检查**：核对 `guides/` 中对发现端点 / spec 形态的描述，与 `scripts/consolidate_openapi.py` 的实际产物形态（注意 `SKIP_FILES = {"openapi.json"}`，31 个 spec → 对外 30 个，这是有意为之，不要误报为 bug）。报告描述与产物的不一致。
>   3. **本地化覆盖率统计**：统计中文页占比（文件名含 zh/chinese/cn），当前约 11/743 ≈ 1.5%。列为 INFO/内容缺口，不是 BLOCKER。
>   - **严重度分级**：能仅凭源码证伪的不一致 = BLOCKER；统计性/内容缺口 = INFO。绝不把无法仅凭源码定罪的项标成 BLOCKER。
>   - 输出 JSON + Markdown 双格式；每条结论带 `file`、`line`、`reproduce`（复现命令）字段；支持 `--ci`。
>
> **第四步 · 自检零误报**：对每条 BLOCKER，手工打开对应源文件行号复核一遍，确认确实不一致。把复核过程写进 `checks/README.md`。
>
> **第五步 · 产出报告**：跑检查器，生成 `reports/hard-defects-<今天日期>.md` 和 `.json`。报告遵循 `WRITING-STANDARD.zh-CN.md`：需求视角优先、2.5 维叙事（先全局结论、再分类拆解、后单点下钻一条最严重的）、中文标点、中英文间空格、一次成型、控篇幅。
>
> **第六步 · 回写**：更新 `project/STATE.md`（标记阶段一完成、写下一步）、`project/baselines/FACTS.zh-CN.md`（更新实跑数字）；若产生新决策，追加到 `project/DECISIONS.md`。
>
> **约束**：不换仓库、不提 PR、不撤销凭证、不发 live 请求作为定罪依据、PAT 永不明文打印、占位符 `[ph_..._ph]` 逐字节保留。完成后用一句话向我汇报验收产物清单。
