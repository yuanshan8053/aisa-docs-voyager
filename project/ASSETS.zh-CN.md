# 资产清单（项目全量盘点)

> 本文件是项目所有文件的权威分类索引。回答「这个文件是什么、属哪一类、能不能动」就看它。
> 盘点时间：2026-06-26。盘点口径：仓库根 `~/files/aisa-docs-voyager` 下全部纳管文件,不含 `.git/`。
> 分类五大类:**产物**(对外可交付的高价值成果)、**规划**(各阶段实施提示词)、**过程**(中间工作区与脚本)、**参考**(权威信息源与基线)、**归档**(早期废弃产物,仅历史留存)。

---

## 一、一句话读图

```
aisa-docs-voyager/
├── 参考  project/        权威信息源:章程/状态/决策/基线/契约/本清单
├── 规划  planning/       五个阶段的自包含实施提示词
├── 产物  reports/        13 份对外报告(质检结果、写作实践、批注清单……)
├── 产物  ws-site/        双语 Scalar API 站点(部署源)
├── 产物  checks/         阶段一静态检查器(可独立运行的工具)
├── 过程  ws-v2/          阶段三加强工作区(31 spec 五件套 + 复现脚本)
├── 过程  skill-local/    阶段三本地加强方法与工具链
├── 参考  docs-mirror/    线上文档全量镜像快照(对比基准)
├── 过程  tools/          镜像工具
├── 过程  aisa_doc_auditor/  早期 live-probe 审计器(降级为旁证)
├── 过程  ws/ phase3-pilot/   阶段三早期试点(保留作对照,见 D-013/D-015)
├── 归档  archive/        求职作品集阶段产物(已废弃)
└── 根    README/LICENSE/WRITING-STANDARD/pyproject/三个 Phase-5 工具
```

---

## 二、产物(对外可交付的高价值成果)

这一类是项目对产品负责人/研发/技术写作的最终交付物。

### 2.1 报告 `reports/`(13 份)

| 文件 | 它是什么 | 受众 |
| --- | --- | --- |
| `hard-defects-2026-06-26.md` / `.json` | 阶段一硬伤质检首报:3 项 BLOCKER,均仅凭 `openapi.yaml` 可证伪 | 产品负责人 |
| `ai-friendly-guides-2026-06-26.md` | 阶段二 30 页 guides 试点质检 | 产品负责人 |
| `ai-friendly-prose-2026-06-26.md` | 阶段二全量 73 页质检(技术版,含规范点号/置信度/对账台账) | 技术写作 |
| `ai-friendly-prose-readable-2026-06-26.md` | 同上的可读叙事版(《从一个连字符看 Agent 的文档体验》) | 产品负责人/对外 |
| `ai-friendly-method.zh-CN.md` | AI 友好度质检方法论沉淀 | 复用方 |
| `content-audit-2026-06-26.md` | 报告甲:存量文档内容审计(阶段一+二合并对外稿) | 产品负责人 |
| `openapi-enhance-pilot-2026-06-26.md` | 阶段三两 spec 试点报告 | 过程留痕 |
| `openapi-enhance-v2-2026-06-26.md` | 阶段三全量执行报告(31 spec / 667 op / 18,290 字段) | 产品负责人 |
| `scalar-api-site-2026-06-26.md` | 阶段五双语 API 站点呈现报告 | 产品负责人 |
| `annotations-for-dev-2026-06-26.md` / `.csv` | 批注待研发确认清单(109 条硬事实缺口) | AIsa 研发 |
| `api-writing-patterns-2026-06-26.md` | API 文档专业写作实践(9 模式,真实改前改后) | 技术写作/研发 |

### 2.2 双语 API 站点 `ws-site/`(部署源)

- `ws-site/en/` — 30 份英文投影 spec + `index.html`(Scalar 多 spec 入口)
- `ws-site/zh/` — 30 份中文投影 spec + `index.html`
- 由 `project_spec.py` 从 `ws-v2/*/enhanced.json` 投影派生,`check_projection.py` 三闸逐字节验收。
- 上线方式:`.github/workflows/deploy-api-site.yml` → GitHub Pages。

### 2.3 静态检查器 `checks/`

- `src_consistency.py` — 阶段一交付,零依赖确定性源码一致性检查器,可 CI 集成。
- `README.md` — 用法。`.gitkeep` 占位。

---

## 三、规划 `planning/`(五阶段实施提示词)

| 文件 | 阶段 |
| --- | --- |
| `PHASE-1-hard-defects.zh-CN.md` | 阶段一 硬伤质检 |
| `PHASE-2-ai-friendly.zh-CN.md` | 阶段二 AI 友好度质检 |
| `PHASE-3-openapi-enhance.zh-CN.md` | 阶段三 OpenAPI 内容加强 |
| `PHASE-4-report-aggregation.zh-CN.md` | 阶段四 报告汇总 |
| `PHASE-5-scalar-api-site.zh-CN.md` | 阶段五 API 站点呈现 |

每份含自包含委派提示词、输入边界、验收产物清单,供跨 session agent 领取实施。

---

## 四、参考(权威信息源与基线)

### 4.1 `project/`(跨 session 三件套 + 配套)

| 文件 | 作用 | 可变性 |
| --- | --- | --- |
| `CHARTER.md` | 项目章程:是什么、四条线、约束、资产地图 | 稳定 |
| `STATE.md` | 当前进度、阻塞、下一步 | 每 session 必更 |
| `DECISIONS.md` | 决策日志(D-001…D-019) | **只追加,不删改** |
| `baselines/FACTS.zh-CN.md` | 静态可证基线事实 + 复现命令 | 随上游更新 |
| `REPORT-CONTRACT.zh-CN.md` | 对外报告契约(骨架 + 证据闭环) | 稳定 |
| `HANDOVER.md` | 交接说明 | 稳定 |
| `ASSETS.zh-CN.md` | 本文件:资产分类索引 | 盘点时更新 |

### 4.2 `docs-mirror/`(线上文档全量镜像)

773 个文件,`guides/` + `agent-skills/` + `api-reference/` + `openapi/` 全量快照,作为「线上呈现 vs 源仓库」对比基准。配套工具 `tools/docs_mirror.py`(见过程类)。

---

## 五、过程(中间工作区与脚本)

这一类是产出产物的工作区与脚本,非最终交付,但承载复现能力,**不删**。

### 5.1 阶段三加强工作区 `ws-v2/`

- 31 个 spec 子目录,每个含五件套:`content.json`(语义字典源)、`enhanced.json`(加性注入 `x-doc` 后的 spec)、`review_table.md` / `.json`(三栏对照表)、`inject_review.json`(注入回执)。
- 超大档另含切片中间物:`dataforseo/{slices,parts,selfcheck}`、`agentmail/{slices,parts,selfcheck}` 及其专用 `union_merge.py`。
- 顶层复现脚本(产物报告依赖,**不可移动**,详见第七节):
  - `central_accept.py` — 31 spec 双闸门中央验收。
  - `extract_annotations.py` — 提取 109 条批注 → 产物报告。
  - `dump_pairs.py` — 导出 17,550 对改前改后 → 写作实践素材。
  - `find_examples.py` — 按模式分桶捞案例。

### 5.2 阶段三方法与工具链 `skill-local/aisa-doc-enhance/`

- `SKILL.md` / `METHODOLOGY.md` — 本地加强方法。
- `tools/` — `inject_xdoc.py`(加性注入引擎)、`check_native_preserved.py`(原生保全闸门)、`make_review.py`(对照表+完整性闸门)、`merge_content.py`、`slice_spec.py`。被多份产物脚本 `import`,**不可移动**。

### 5.3 镜像工具 `tools/docs_mirror.py`

抓取线上文档生成 `docs-mirror/` 快照。

### 5.4 早期试点(保留作对照,见 D-013/D-015)

- `ws/` — 阶段三最早试点(openai-chat、youte-search),含 `enhanced-page.md`/`writeback.diff` 等旧路线产物。
- `phase3-pilot/` — 试点定型版,含独立的 `inline_inject.py`。
- 两者已被 `ws-v2/` 全量路线取代,但 `DECISIONS.md` 明令「旧试点产物保留作对照,不删」。

### 5.5 早期 live-probe 审计器 `aisa_doc_auditor/`

`auditor.py` + `__init__.py`。阶段一后降级为旁证工具(live 探测不单独定罪)。`pyproject.toml` 的 `aisa-docs-voyager` 入口仍指向它。保留。

---

## 六、归档 `archive/`(早期废弃产物)

求职作品集阶段产物,已不代表当前方向,仅历史留存(详见 `archive/README.md`):

| 文件 | 原用途 |
| --- | --- |
| `STRATEGY.zh-CN.md` | 投递岗位策略简报(废弃) |
| `ROADMAP.zh-CN.md` | 三步走作品规划(被 `planning/` 取代) |
| `localized/quickstart.zh-CN.md` | 样例中文快速开始(留作本地化样张) |
| `reports/sample-audit.*` | 早期 live-probe 审计样例(留作格式参考) |

---

## 七、根目录文件与「不可移动」约束

| 文件 | 类 | 说明 |
| --- | --- | --- |
| `README.md` | 参考 | 项目门面 |
| `LICENSE` | 参考 | MIT |
| `WRITING-STANDARD.zh-CN.md` | 参考 | 写作规范(所有文字产出遵守) |
| `pyproject.toml` | 过程 | 打包配置,入口指向 `aisa_doc_auditor` |
| `.gitignore` / `.github/` | 过程 | 忽略规则 + 两个 workflow |
| `project_spec.py` | 过程(产物工具) | 阶段五投影器 |
| `check_projection.py` | 过程(产物工具) | 阶段五投影闸门 |
| `build_index.py` | 过程(产物工具) | 阶段五站点入口生成器 |

**为什么三个 Phase-5 工具留在根、不归进子目录**:`DECISIONS.md`(只追加不删改)与 `reports/scalar-api-site-2026-06-26.md`、`planning/PHASE-5-*.md`、`STATE.md` 均以根路径形式钉死了复现命令(如 `python3 project_spec.py …`、`python3 check_projection.py …`)。决策日志不可改写,移动这些文件会让已发布的复现命令失效。同理 `ws-v2/*.py` 与 `skill-local/.../tools/*.py` 被产物报告与脚本 `import`,亦不移动。**归整以「分类标注 + 清理 cruft」为限,不做破坏复现链的物理搬迁。**

---

## 八、本轮盘点动作(留痕)

1. **去重消歧**:核对无重复内容文件。`ai-friendly-prose` 技术版与 readable 版是同源不同受众的两份,非重复;`ws/` 与 `phase3-pilot/` 是两次试点快照,内容不同,均按 D-013/D-015 保留。
2. **清理 cruft**:删除全部 `__pycache__/` 与 `*.pyc`(本就 gitignored,5 处)。
3. **一致性**:本清单与 `CHARTER.md` 第五节资产地图、`STATE.md` 已完成项对齐。
4. **不动复现链**:根 `.py` 与被 import 的工具脚本一律原位保留(第七节)。
