# 交接报告（Handover）

> 本文件供新 session 接管 agent 阅读，实现无缝衔接。读完本文件 + `CHARTER.md` + `STATE.md` + `DECISIONS.md` + `baselines/FACTS.zh-CN.md`，即可直接领工开干。
> 交接时间：2026-06-28。

---

## 一、项目一句话

AIsa 是 OpenAI 兼容的 AI 能力网关（法律实体 AIPay, Inc.），文档同时面向人和 Agent。本项目把「防止文档腐烂、主动提升文档质量」做成一套可分阶段实施、可独立验收、证据确凿的文档质量工程。源仓库 `AIsa-team/docs`（本地副本 `~/files/aisa-team-docs`，pinned `16863d3`），项目仓库 `aisa-docs-voyager`（远端 `github.com/yuanshan8053/aisa-docs-voyager`），线上站点 `https://yuanshan8053.github.io/aisa-docs-voyager/`。

---

## 二、五个阶段全景（截至 2026-06-28）

| 阶段 | 内容 | 状态 | 关键产物 |
| --- | --- | --- | --- |
| 一 | 硬伤质检（静态一致性检查器） | ✅ 完成 | `checks/src_consistency.py` + `reports/hard-defects-2026-06-26.md` |
| 二 | AI 友好度质检（73 页散文） | ✅ 完成 | `reports/ai-friendly-prose-2026-06-26.md`（技术版）+ readable 叙事版 |
| 三 | OpenAPI 内容加强（31 spec 双字段） | ✅ 全量完成 | `ws-v2/<spec>/` 五件套 + `reports/openapi-enhance-v2-2026-06-26.md` |
| 四 | 对外报告汇总 | ⏳ 可派 | 报告甲（A）现可派、报告乙（B）前置已满足 |
| 五 | 双语 Scalar API 站点 + 成果落地页 | ✅ 上线 | `ws-site/{en,zh}/` + `site/index.html` + `site/ai-friendly.html` |

**唯一剩余主线工作 = 阶段四对外报告汇总**（见 `planning/PHASE-4-report-aggregation.zh-CN.md`），其余均已交付并上线。

---

## 三、我做了什么（工作述职）

按时间线，本项目从「对文档一无所知」走到「两条治理线全量完成 + 呈现上线」：

1. **摸清生产链路与基线**：查清 `AIsa-team/docs`（源）→ `new-style-landing-page`（部署）→ `aisa.one`（线上），确认线上 API 参考正文是 OpenAPI spec 内联渲染、非手写 md。核实全部静态可证基线：743 页 / 664 API 参考桩页 / 73 可读散文页（guides 30 + agent-skills 43）/ 源仓库 31 份 spec（含 1 份玩具示例，30 份 AIsa 真实 spec）/ 11 中文页。见 `baselines/FACTS.zh-CN.md`。

2. **阶段一 · 硬伤质检**：自建零依赖确定性检查器 `checks/src_consistency.py`，定案 3 项 BLOCKER（全在 `guides/agent-discovery.mdx`：schema 121→321、分类 10→14、分类表漏列 4 项），均仅凭 `openapi.yaml` 可证伪。复核撤下前序「13 vs 43 skills」误报（D-006），确立「真值绑定 + 语境约束」零误报范式（D-005/D-007）。

3. **阶段二 · AI 友好度质检**：用 `ai-friendly-doc-check-multiagent-v10` 的 Map-Reduce + 三层隔离（D-009）对全部 73 页跑质检，确认 **20 条硬缺口**（7 高/8 中高/5 中），47 原始线索 → 20 保留 + 21 并入 + 6 撤回，账平零误报（D-010）。主病灶定性：agent-skills 43 页各自手抄模型价/上下文/计数/端点，缺单一权威事实源，14 条命中「跨文档同对象取值不一致」（D-011）。

4. **阶段三 · OpenAPI 内容加强（v2 双字段，全量）**：经 D-012→D-013→D-015 三次路线校正，最终走 v2 本地双字段路线——逐字段产 `desc_en`（加强英文）+ `title_zh`（中文本地化）写进 `content.json`，`inject_xdoc.py` 加性注入 `x-doc`（不 hoist、原生零改动，D-008），两道确定性闸门 `check_native_preserved.py`（exit 0）+ `make_review.py --require both`（完整性 exit 0），不产 md。全量 31 spec / 667 op / 18,290 字段 / 109 主动批注，超大档 dataforseo（445 op，13 分片）、agentmail（46 op，2 分片）切片并发撰写 + 合并 + 全档复验，**中央验收 31/31 双闸门全绿**（D-016）。

5. **阶段五 · 呈现与上线**：写投影器 `project_spec.py` 把 `x-doc` 按语言投影进原生字段产干净 OpenAPI 派生档（路线 A，D-017），投影闸门 `check_projection.py` 三闸对 60 份投影档 exit 0；Scalar 官方 CDN standalone（v1.61.0，MIT）零改动加载，两入口侧边栏多 spec。站点 spec 口径经 D-018→D-019 校正为 **30 份 AIsa 真实 spec**（剔除玩具）。GitHub Pages 部署上线。

6. **收尾与重设计**：资产盘点（`ASSETS.zh-CN.md`）+ README 重写 + 成果落地页（D-020 统一 31/30 口径、标点归正、删 archive、收拢 pilots）。**本轮（D-021）**把落地页 `site/index.html` 换成双主题（沉浸体验/阅读模式，键盘 1/2 切换、`localStorage` 持久化）重设计版，新增质检报告叙事页 `site/ai-friendly.html`，修复设计交付的 `site_` 文件名前缀坑并接通部署 workflow，新增一键机器验收 `accept_all.py`，commit `10cf6ec` 上线、6 个 URL 全 200。

最近 commit：`10cf6ec`（站点重设计上线）。

---

## 四、关键产物在哪、怎么验

| 想要什么 | 看哪里 |
| --- | --- |
| 质检洞察（人读） | `reports/ai-friendly-prose-readable-2026-06-26.md` 或线上 `/ai-friendly.html` |
| 质检对账（技术版） | `reports/ai-friendly-prose-2026-06-26.md` |
| 硬伤清单 | `reports/hard-defects-2026-06-26.md` / `.json` |
| API 加强成果 | `ws-v2/<spec>/` 五件套；报告 `reports/openapi-enhance-v2-2026-06-26.md` |
| 双语 API 站点 | 线上 `/en/` `/zh/`；源 `ws-site/{en,zh}/` |
| 109 条待研发批注 | `reports/annotations-for-dev-2026-06-26.{md,csv}` |
| 9 个写作模式 | `reports/api-writing-patterns-2026-06-26.md` |
| 一键复验全部门禁 | `python3 accept_all.py --baseline 16863d3`（双闸门 31/31 + 投影三闸 60/60，exit 0） |

---

## 五、给接手 agent 的开工步骤

1. 读 `CHARTER.md` → `STATE.md` → `DECISIONS.md`（D-001…D-021）→ `baselines/FACTS.zh-CN.md` → 本文件。
2. 确认源仓库副本 `~/files/aisa-team-docs` 在；不在则用项目指令里的 PAT 克隆 `AIsa-team/docs`（PAT 永不明文打印）。
3. 跑 `python3 accept_all.py --baseline 16863d3` 确认所有机器门禁仍绿，再动手。
4. 若做阶段四：打开 `planning/PHASE-4-report-aggregation.zh-CN.md`，按自包含派遣提示词执行（报告甲 A 现可派；报告乙 B 须对齐 v2 口径 D-015/D-016，五件套 + 双闸门，无 md）。
5. 阶段三若需补做：**只读** `skill-local/aisa-doc-enhance/`（先精读 `METHODOLOGY.md`），不读 `api-doc-agent`，不依赖 spectral / 渲染器 / doc_engine。
6. 干完回写 `STATE.md` + `DECISIONS.md`（只追加）+ `baselines/FACTS.zh-CN.md`。

---

## 六、硬约束（不可违背）

不换仓库 · 无写权限不提 PR（D-003）· 静态为主 live 仅旁证 · 零误报红线（D-005/D-007）· 严禁杜撰硬事实、缺口主动留批注 · 每阶段独立可验收 · 遵循 `../WRITING-STANDARD.zh-CN.md`（中文标点、中英文间空格、需求视角优先、一次成型、控篇幅）· PAT 保留不撤销且永不明文打印 · 占位符 `[ph_..._ph]` 逐字节保留 · 不直连 LLM Gateway · 不在沙箱启网络监听 · 根 `.py` 工具与被 import 的工具脚本不可移动（复现命令钉死路径，见 `ASSETS.zh-CN.md` 第六节）。

---

## 七、已知未竟与待决（如实留痕）

- **阶段五线上目视终验**：浏览器 file:// 截图受沙箱限制未做，站点实质正确性已由三闸逐字节 + `accept_all.py` 证明；建议负责人在线上目视终验 Scalar 视觉呈现、双主题切换、质检报告页链接。
- **109 条批注交研发**：源 spec 未声明、加强时拒绝杜撰而留痕的硬事实缺口（集中在 openapi-financial 30 / dataforseo 22 / apollo 20），建议整理成「待研发补全清单」反馈上游。
- **阶段二修复跟进**：为 agent-skills 建立对 `guides/models.mdx` + 定价页的单一引用，删离群价格/计数/端点/旧型号，14 条 6.1 缺口随之消解（交产品负责人）。
- **渲染层缺口（D-008，不阻断）**：火山 `direct` 渲染器不渲染真实 REST 参数；本路线刻意不以渲染 md 为交付，不影响价值落地。
