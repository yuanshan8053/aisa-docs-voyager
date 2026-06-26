# 阶段三 · OpenAPI 内容加强

**阶段目标**：用 `api-doc-agent` 技能，把 AIsa 的 OpenAPI spec 加强成专业、好懂、人话的参考内容——产出**独立的增强版参考页**，并实现**把增强内容回写原 spec**的能力（经 `x-doc` 命名空间只增不改，杜绝双源漂移）。先用最小单接口 spec 试点。

**为什么这样定**（见 D-002）：线上渲染后的 API 参考正文是 OpenAPI spec 内联，不是手写 Markdown，独立交付物本就是 `openapi/*.json`。所以本阶段不产「直出 md」，而是产增强 spec + 独立增强参考页，并把增强内容沉淀回 spec 的 `x-doc` 字段，让源头变好。

---

## 输入边界

- **输入 spec**：源仓库 `~/files/aisa-team-docs/openapi/*.json`（31 个）。
- **试点对象**（单接口、字节最小，便于快速验收）：`openai-chat.json`（POST /chat/completions，1 op，4.2KB）、`youte-search.json`（GET /youtube/search，1 op，3.6KB）。验收通过再扩到多接口 spec。
- **内容必须由 agent 撰写**：`api-doc-agent` 的 `doc_engine.py` 是不调 LLM 的确定性内核，只做装配；字段/接口的中文说明、用法、坑必须由接手 agent 站在 API 使用者视角亲自写进 `content.json`，再注入。空 content 只会产出空壳。

## 依赖准备

- 安装 spectral（真 lint 才得 green，否则闸门 skipped、verdict 降级 yellow）：`npm i -g @stoplight/spectral-cli@6.16.0`（需 node/npm，按 `<software_installation>` 装到 `$HOME`）。装不上则记录降级状态，不阻塞试点。

## 验收产物（缺一不可）

1. 试点的 `content.json`（agent 撰写的增强内容）。
2. 试点的 `enhanced.yaml` / 增强 spec（含 `x-doc` 命名空间，原生字段不复制）。
3. 试点的独立增强参考页（技能产出的 doc 产物）。
4. **回写验证**：证明增强内容能回写进原 spec 的 `x-doc` 而不破坏原生结构（`source=human` 受保护、AI 不静默覆盖），并附回写前后 diff。
5. `reports/openapi-enhance-pilot-<日期>.md` — 试点小结：做了什么、x-doc 加强了哪些字段、回写如何保证不漂移、闸门状态（green/yellow 及原因）。
6. 回写 `project/STATE.md`、`project/DECISIONS.md`（若有新决策）。

## 验收标准

- 增强内容真正提升可用性（字段说明、用法、错误码、边界条件），不是机械转换。
- 回写只走 `x-doc`「只增不改」，原生 `paths/$ref/类型/枚举/必选` 不被复制或篡改，无双源漂移。
- 报告遵循 `WRITING-STANDARD.zh-CN.md`。

---

## 自包含委派提示词（复制给新 session agent）

> 你接手 AIsa 文档质量工程的「阶段三：OpenAPI 内容加强」。你之前没有本项目上下文，请严格按下文执行。
>
> **背景**：AIsa 是 OpenAI 兼容的 AI 能力网关，文档源仓库 `AIsa-team/docs` 里有 31 个 OpenAPI spec（`openapi/*.json`）。线上 API 参考页的正文是由这些 spec 渲染内联生成的，不是手写 md。我们要把 spec 加强成专业好懂的参考内容：产出独立增强参考页，并把增强内容回写进原 spec（只增不改），让源头变好。结果交产品负责人。
>
> **第一步 · 读权威信息源**：依次读 `~/files/aisa-docs-voyager/project/CHARTER.md`、`project/STATE.md`、`project/DECISIONS.md`、`project/baselines/FACTS.zh-CN.md`、`~/files/aisa-docs-voyager/WRITING-STANDARD.zh-CN.md`。特别注意决策 D-002：本阶段不产「直出 md」，产增强 spec + 独立增强页 + 回写能力。
>
> **第二步 · 装依赖**：尝试安装 spectral（`npm i -g @stoplight/spectral-cli@6.16.0`，装到 $HOME）。装不上就记录降级（verdict 会是 yellow），不阻塞。
>
> **第三步 · 读技能方法论**：`api-doc-agent` 技能在 `/data/plugins/custom/skills/api-doc-agent/`。务必读它的 `SKILL.md` 和 `doc-engine/SKILL.md` + `doc-engine/core/`，掌握 x-doc 撰写方法论与 6 条红线（平台中立 / 只增不改 / 不复制原生元数据 / 不捏造 / AI 不覆盖人工 / 中文 H1 归 heading_zh）。
>
> **第四步 · 试点**：选 `~/files/aisa-team-docs/openapi/openai-chat.json`（POST /chat/completions，单接口）做试点。
>   1. 站在 API 使用者视角，为该接口的每个字段/参数撰写中文增强内容（干什么、怎么用、有什么坑、错误码、边界），写进 `content.json`。这是本阶段的灵魂，不可跳过、不可机械转换、不可捏造。
>   2. 用技能的确定性管线把 content 注入，产出 `enhanced.yaml`（含 x-doc）和独立增强参考页。
>   3. **验证回写**：把增强内容回写进原 spec 的 `x-doc` 命名空间，确认原生结构（paths/$ref/类型/枚举/必选）零改动、source=human 受保护、AI 不静默覆盖。生成回写前后 diff 留证。
>   4. 用 `youte-search.json` 再跑一遍，确认流程可复用。
>
> **第五步 · 产出报告 + 回写**：写 `reports/openapi-enhance-pilot-<今天日期>.md`，遵循 `WRITING-STANDARD.zh-CN.md`（2.5 维叙事：先讲清「增强 + 回写」整体价值、再拆解做了哪几类加强、后下钻一个字段从「机器结构」到「人话说明」的对比）。更新 `project/STATE.md`，新决策追加 `project/DECISIONS.md`。
>
> **约束**：不换仓库、不提 PR、不撤销凭证、不直连 LLM Gateway、不在沙箱启网络监听、PAT/base-token 永不明文打印、占位符 `[ph_..._ph]` 逐字节保留。x-doc 只增不改、绝不捏造。完成后用一句话汇报验收产物清单。
