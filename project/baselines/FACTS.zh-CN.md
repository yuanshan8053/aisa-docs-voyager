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

**consolidated `openapi.yaml` 形态（线上参考正文内联渲染的同一份产物，全部静态可证）**：

| 指标 | 数值 | 复现命令（在源仓库根执行） |
| --- | --- | --- |
| 路径数 | 645 | `python3 -c "import yaml;print(len(yaml.safe_load(open('openapi.yaml'))['paths']))"` |
| 操作数 | 663 | 见 `checks/src_consistency.py` |
| schema 数 | 321 | `python3 -c "import yaml;print(len(yaml.safe_load(open('openapi.yaml'))['components']['schemas']))"` |
| 承载操作的分类（tag）数 | 14 | 见 `checks/src_consistency.py` 规则 2 复现命令 |

**散文 vs 桩页之分**：664 个 API 参考页是单行桩——frontmatter 用 `openapi: "openapi/xxx.json METHOD /path"` 指向 spec，正文由渲染层从 spec 内联生成，并非手写内容。真正可做 AI-friendly 散文质检的对象是 `guides/`（30）+ `agent-skills/`（43）= 73 页可读散文。

---

## 二、已确证的硬伤（静态、零误报）

> 阶段一（2026-06-26）实跑静态检查器后更新。每条结论的判定**完全来自源仓库文件**，不依赖任何 live 请求；线上探测仅作旁证，绝不作为唯一定罪依据。立案以 `checks/src_consistency.py` 实跑为准，首份报告见 `reports/hard-defects-2026-06-26.md`。

三项 BLOCKER 全部集中在 `guides/agent-discovery.mdx`，根因同一：该页对 spec 形态的描述是某次手写后固化的快照，未随 `openapi.yaml` 演进而更新。

### 硬伤 1 · schema 数断言矛盾（121 vs 321）

- **现象**：`guides/agent-discovery.mdx:16` 写 spec「covering 111+ API paths and 121 schemas」，而 `openapi.yaml` 实有 321 个 schema。
- **复现**：`python3 -c "import yaml;print(len(yaml.safe_load(open('openapi.yaml'))['components']['schemas']))"` → 321。
- **判定**：精确数字与产物直接矛盾，BLOCKER。

### 硬伤 2 · 分类数断言矛盾（10 vs 14）

- **现象**：`guides/agent-discovery.mdx:127` 写「organized into 10 categories」，spec 中真正承载操作的分类（tag）实有 14 个。
- **复现**：见上表「承载操作的分类数」复现命令 → 14。
- **判定**：精确数字与产物矛盾，BLOCKER。

### 硬伤 3 · API 分类表漏列 4 个真实分类

- **现象**：`agent-discovery.mdx:163` 的「API Categories」表自称「spec 把端点组织为以下分类组」却只列 10 个，漏掉 Agent Email（46 操作）、Reddit（5）、SEO & Search Data（445）、Sales Intelligence（54）——四者均承载真实操作。
- **判定**：spec 可直接证伪遗漏，BLOCKER。其中 SEO & Search Data 一类即占全 spec 663 个操作的约三分之二，属核心能力的发现性缺失。

### 已撤下 · 技能计数漂移（13 vs 43）

- 前序基线曾列此条。经阶段一复核：A2A agent card 广播的 13 个 skill 与 `agent-skills/` 目录 43 个可安装技能页是两个不同概念，文档「13」与其自身 13 行技能表内部自洽，无法仅凭源码证伪。按零误报红线撤下，不再计为 BLOCKER（见 `DECISIONS.md` D-006）。

### INFO · 中文覆盖率极低 & 路径数陈旧低估

- 743 页中仅 11 页中文，覆盖率约 1.5%：`find . -name '*.mdx' | grep -iE 'zh|chinese|/cn' | wc -l` → 11。属内容缺口，非阻断。
- `agent-discovery.mdx:16` 写「111+ paths」，实为 645：带 `+` 字面为真，仅标陈旧低估，非阻断。

---

## 三、阶段三 OpenAPI 内容加强覆盖（v2 双字段，静态可证）

> 阶段三（2026-06-26）全量执行后记录。所有数字可由 `ws-v2/central_accept.py` 一键复跑核实（exit 0 = 31 份 spec 双闸门全绿）。加强为加性注入 `x-doc`，原生 spec 零改动。

| 指标 | 数值 | 复现命令（在项目根 `~/files/aisa-docs-voyager` 执行） |
| --- | --- | --- |
| 加强的 spec 数 | 31 | `ls openapi/*.json` 于源仓库 → 31；`ls -d ws-v2/*/` 中含 `content.json` 者 → 31 |
| 加强的 operation 数 | 667 | `python3 ws-v2/central_accept.py`（totals.ops） |
| 加强的对外字段/参数数 | 18,290 | 同上（totals.fields） |
| 主动批注（待研发确认）数 | 109 | 同上（totals.annotations） |
| 原生保全闸门通过 | 31/31 exit 0 | `check_native_preserved.py <源 spec> <enhanced.json>` 逐档 |
| 完整性闸门通过 | 31/31 missing=0 | `make_review.py --spec <enhanced.json> --require both` 逐档 |
| 落盘产物可复现 | 31/31 字节一致 | 现场重注入与落盘 `enhanced.json` diff 为空 |

**口径说明**：每个对外字段都齐备「加强英文 `desc_en` + 中文本地化 `title_zh`」双字段；operation 级齐备 `heading_zh`+`description_zh`+`desc_en`。`agentmail` 的注入 `unresolved=1347` 是源 spec 把 46 operation 复用成 12 个 operationId 的结构属性（非匹配兄弟 path 记 harmless unresolved），两道绑定闸门均通过，属已认定的可接受工程产物（见 `DECISIONS.md` D-016）。109 条批注是源 spec 未声明、加强时拒绝杜撰而显式留痕的硬事实缺口，集中在 `openapi-financial`(30) / `dataforseo`(22) / `apollo`(20)。

---

## 四、口径与边界

- **零误报原则**：凡列为「阻断硬伤」的，必须能仅凭源仓库文件证伪；live 探测的 `http_status:0` 之类只能作 INFO，不能单独定罪（无法区分「文档真坏」与「本地网络被挡」）。
- **数字会变**：上表数值随上游提交变动，复现命令是不变的真相来源。任何引用本基线的报告须重跑命令取当时值。
- **历史出入说明**：早期 live-probe 阶段记录过「13 vs 45」「773 页」「1.3%」等数字；本次静态核实为「743 页」「1.5%」。其中「技能计数漂移」一条经阶段一复核撤下（见硬伤段「已撤下」与 `DECISIONS.md` D-006），现行硬伤以 `openapi.yaml` 形态矛盾为准。
