# 基线事实（静态可证）

> 本文件记录全部已从源码核实、可独立复现的事实。每条都附**源码定位**，任何人不依赖任何线上请求即可验证。
> 复现前提：`AIsa-team/docs` 仓库已克隆到本地（本项目工作副本在 `~/files/aisa-team-docs`）。
> 核实时间：2026-06-26。核实对象 commit 见仓库 `git log` 顶端。

---

## 一、文档面规模

| 指标 | 数值 | 复现命令（在源仓库根执行） |
| --- | --- | --- |
| 总页面（`.mdx`） | 743 | `find . -name '*.mdx' \| wc -l` |
| 其中 API 参考桩页（frontmatter 含 `openapi:`） | 664 | `grep -rl '^openapi:' --include='*.mdx' . \| wc -l` |
| `guides/` 散文页 | 30 | `find guides -name '*.mdx' \| wc -l` |
| `agent-skills/` 页 | 43 | `find agent-skills -name '*.mdx' \| wc -l` |
| OpenAPI spec 文件 | 31 | `ls openapi/*.json \| wc -l` |
| 中文页面（文件名含 zh / chinese / cn） | 11 | `find . -name '*.mdx' \| grep -iE 'zh\|chinese\|/cn' \| wc -l` |

**散文 vs 桩页之分**：664 个 API 参考页是单行桩——frontmatter 用 `openapi: "openapi/xxx.json METHOD /path"` 指向 spec，正文由渲染层从 spec 内联生成，并非手写内容。真正可做 AI-friendly 散文质检的对象是 `guides/`（30）+ `agent-skills/`（43）= 73 页可读散文。

---

## 二、已确证的硬伤（静态、零误报）

每条结论的判定**完全来自源仓库文件**，不依赖任何 live 请求；线上探测仅作旁证，绝不作为唯一定罪依据。

### 硬伤 1 · 发现契约不对称

- **现象**：`guides/agent-discovery.mdx` 与插件清单引导 Agent 去取的发现端点（如聚合 `openapi.yaml`），与源仓库实际产出的 spec 形态不一致——源仓库是 `openapi/` 下 31 个分服务 spec，经 `scripts/consolidate_openapi.py` 处理（跳过 `openapi.json`）后对外是 30 个。
- **源码定位**：`scripts/consolidate_openapi.py:43` → `SKIP_FILES = {"openapi.json"}`；`scripts/consolidate_openapi.py:321` 处据此过滤。31 → 30 是**有意为之**，非漂移。
- **判定**：spec 数量差异本身不是 bug；bug 在于散文里对发现入口形态的描述与产物不一致。

### 硬伤 2 · 技能计数漂移（13 vs 43）

- **现象**：`guides/agent-discovery.mdx` 正文硬编码「advertises 13 skills」「AIsa currently advertises 13 skills」，而源仓库 `agent-skills/` 目录实际有 43 个技能页。
- **源码定位**：
  - `guides/agent-discovery.mdx:14` → `... advertises 13 skills with metadata ...`
  - `guides/agent-discovery.mdx:97` → `AIsa currently advertises 13 skills through the agent card:`
  - `find agent-skills -name '*.mdx' | wc -l` → 43
- **判定**：手写数字 13 与目录真实页数 43 强不一致，是确凿硬伤。（注：agent card 广播的 skill 数与目录页数口径可能不同，但「文档写死一个会过期的数字」这一缺陷成立，且 13 既不等于 43 也不等于早期记录的 45。）

### 硬伤 3 · 中文覆盖率极低

- **现象**：743 页中仅 11 页为中文，覆盖率约 1.5%。
- **源码定位**：`find . -name '*.mdx' | grep -iE 'zh|chinese|/cn' | wc -l` → 11；11 / 743 ≈ 1.5%。
- **判定**：对主打中国模型供给的网关而言，这是离收入/留存最近的内容缺口。属内容缺口（非「错误」），列为高价值改进而非阻断硬伤。

---

## 三、口径与边界

- **零误报原则**：凡列为「阻断硬伤」的，必须能仅凭源仓库文件证伪；live 探测的 `http_status:0` 之类只能作 INFO，不能单独定罪（无法区分「文档真坏」与「本地网络被挡」）。
- **数字会变**：上表数值随上游提交变动，复现命令是不变的真相来源。任何引用本基线的报告须重跑命令取当时值。
- **历史出入说明**：早期 live-probe 阶段记录过「13 vs 45」「773 页」「1.3%」等数字，与本次静态核实的「13 vs 43」「743 页」「1.5%」存在口径差异，以本静态基线为准。
