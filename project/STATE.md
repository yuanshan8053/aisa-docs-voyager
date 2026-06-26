# 当前状态

> 每次 session 结束前必更。记录：项目处于哪个阶段、已完成什么、阻塞是什么、下一步是什么。

**最后更新**：2026-06-26
**当前阶段**：阶段一（硬伤质检）已完成。阶段二（散文 AI 友好度质检）**全量 73 页已完成**。阶段三（OpenAPI 内容加强，v2 双字段路线，D-015）**全量执行已完成并通过中央验收**（31/31 双闸门全绿，ops=667 / fields=18,290 / annotations=109，见 D-016）。**阶段五（Scalar API 站点呈现，路线 A 投影法，D-017）已完成**：写投影器 `project_spec.py` 把 `x-doc` 按语言投影进原生字段、剥 `x-doc`，产干净标准 OpenAPI 派生档 `ws-site/{en,zh}/<name>.json`（各 30 份，排除 Plant Store 样例 31→30）；Scalar 官方 CDN standalone（v1.61.0，MIT）零改动加载，两入口 `ws-site/{en,zh}/index.html`（多 spec 侧边栏）。投影闸门 `check_projection.py` 三闸（无遗漏 / 无篡改 / 无杜撰·无串语言）对 **60 份投影档 exit 0**；投影后 664 操作描述 + 16,876 字段描述 + 9 张错误表全由 `x-doc` 搬运，原生骨架逐字节一致，`x-doc` 残留为 0。报告 `reports/scalar-api-site-2026-06-26.md`。**阶段四报告乙（API 加强对外报告）现在即可派。**

---

## 已完成

- [x] 查清文档生产链路（源仓库 → 部署层 → 线上），见 `CHARTER.md` 第二节。
- [x] 从源码核实全部基线事实（743 页 / 664 桩页 / 73 散文页 / 31→30 spec / 11 中文页），见 `baselines/FACTS.zh-CN.md`。
- [x] 项目重定位、旧资产归档至 `archive/`。
- [x] 建立权威信息源层 `project/`（CHARTER / STATE / DECISIONS / baselines）。
- [x] 产出三阶段实施计划，每阶段含自包含提示词。
- [x] **阶段一交付**：`checks/src_consistency.py` 静态检查器（零依赖、确定性、零误报，支持 `--repo`/`--format`/`--ci`）+ `checks/README.md` + 首份报告 `reports/hard-defects-2026-06-26.md` 与 `.json`。
- [x] 阶段一定案 3 项 BLOCKER（全在 `guides/agent-discovery.mdx`：schema 121→321、分类 10→14、分类表漏列 4 项），均仅凭 `openapi.yaml` 可证伪；复核撤下前序「13 vs 43 skills」误报（D-006）。
- [x] **阶段三试点交付**：在 `openai-chat.json`（内联请求体 schema）与 `youte-search.json`（query 参数 + 内联响应 schema）两份真实 spec 上跑通「撰写 → 注入 → Gate 2 → 回写校验 → 渲染」全链路。产物：`content.json`/`enhanced.yaml`/`enhanced-page.md`/`writeback.diff`/`review_list.json`（会话工作区 `ws/pilot`、`ws/pilot2`）+ 报告 `reports/openapi-enhance-pilot-2026-06-26.md`。两份均 Gate 2 零 error、`check_native_preserved.py` exit 0、diff 零删除。关键工程产出：加性注入扩展 `inline_inject.py`（复用引擎逐节点函数，不 hoist、不改原生结构，见 D-008）。
- [x] **阶段二试点交付**：用 `ai-friendly-doc-check-multiagent-v10` 对 `guides/**/*.mdx` 30 页跑通 Map-Reduce，确认 10 条硬缺口（4 高/3 中高/3 中弱）+ 1 条撤回，零漏报零误报。报告 `reports/ai-friendly-guides-2026-06-26.md`。
- [x] **阶段二全量交付**：并入 `agent-skills/*.mdx` 43 页，对全部 73 页重跑（轻量档、shard_count=1、SINGLE 汇总 factor=0.18）。确认 **20 条硬缺口（7 高/8 中高/5 中）**，47 原始线索 → 20 保留 + 21 并入 + 6 撤回，账平。主病灶：agent-skills 各页各自手抄模型价/context/家族总数/端点路径，不引用 June-4 权威目录，14 条命中 6.1。报告 `reports/ai-friendly-prose-2026-06-26.md` + 方法沉淀 `reports/ai-friendly-method.zh-CN.md`。
- [x] **报告汇总环节设计交付（阶段四规划）**：建立报告契约 `project/REPORT-CONTRACT.zh-CN.md`（调研麦肯锡/BCG/Bain 呈现法，定两份报告骨架 + 证据四步闭环字段）+ 汇总流程与两份自包含委派提示词 `planning/PHASE-4-report-aggregation.zh-CN.md`，见 D-014。**报告甲（阶段一+二内容审计）现在即可派咨询专家整理；报告乙（阶段三 API 加强）待全量执行后派。**
- [x] **阶段三全量执行交付（v2 双字段，D-016）**：31 份 spec / 667 op / 18,290 字段 / 109 批注全量加强完成，产物落 `ws-v2/<spec名>/` 五件套（`content.json` + `enhanced.json` + `review_table.md`/`.json` + `inject_review.json`，**无 md**）。超大档 `dataforseo`（445 op，13 分片）、`agentmail`（46 op，2 分片）经 `slice_spec.py` 切片 + 并发子 agent 撰写 + 合并（`merge_content.py` / agentmail 专用 `union_merge.py`）+ 全档中央复验。**中央验收 31/31 双闸门全绿**（`ws-v2/central_accept.py` exit 0）。工具链第 4 次一致性修复：`inject_xdoc.resolve_property` 加「最长字面量整键优先」以解 dataforseo/apollo 的扁平点号 property key。报告 `reports/openapi-enhance-v2-2026-06-26.md`。
- [x] **阶段五交付（Scalar API 站点呈现，路线 A 投影法，D-017）**：写投影器 `project_spec.py`（复用 `inject_xdoc.HTTP_METHODS` 与同款穿透逻辑，不改原工具）把 `x-doc` 按语言投影进原生 `summary`/`description`、剥 `x-doc`，产干净标准 OpenAPI 派生档；投影闸门 `check_projection.py` 三闸（无遗漏 / 无篡改·双树字节比对 / 无杜撰·错误内容 token 溯源）对 **60 份投影档 exit 0**。产物：`ws-site/en/` + `ws-site/zh/` 各 30 份投影 spec（排除 Plant Store 样例 31→30）+ 两入口 `ws-site/{en,zh}/index.html`（Scalar 官方 CDN v1.61.0 MIT，多 spec 侧边栏，由 `build_index.py` 从磁盘派生、7 份 twitter-* 加 "Twitter · " 前缀聚簇、`openai-chat` 置顶 default）+ 可选部署方案 `.github/workflows/deploy-api-site.yml`（GitHub Pages，默认不自动跑）。投影规模 664 操作描述 + 16,876 字段描述 + 9 张错误表，109 条批注一字不改进 description，`x-doc` 残留为 0，原生 `enhanced.json` 永不改动。Scalar 真可用性已验（CDN HTTP 200、3.6 MB bundle 暴露 `createApiReference`）。**未竟**：浏览器 file:// 截图可视化核对受沙箱三重限制未完成（实质正确性已由三闸逐字节证明，未验仅 Scalar 视觉呈现，建议上线后线上目视终验）。报告 `reports/scalar-api-site-2026-06-26.md`。

- [x] **批注待研发确认清单交付**：`ws-v2/extract_annotations.py` 从 31 份 `content.json` 提取全部 **109 条批注**（驱动源为 `content.json` 的 `annotation` 字段，确保不漏 agentmail 重名 operationId 等未内联到 enhanced 的边界条目），并在源 spec（pinned `16863d3`）上按 opKey+dotpath 解析回 native 上下文（109/109 全解析到类型与原描述）。输出 `reports/annotations-for-dev-2026-06-26.{md,csv}`，列含 spec/接口/位置/字段/类型/原描述 en/改后描述 en/批注，可直接交研发逐条确认。一键复现 `python3 ws-v2/extract_annotations.py`。
- [x] **API 文档专业写作实践集交付**：`ws-v2/dump_pairs.py` 导出全部 17,550 对「原生英文 → 加强英文」对照（`/tmp/pairs.jsonl`），`ws-v2/find_examples.py` 按模式分桶捞候选；从中提炼 **9 个写作模式**（从无到有 / 标签扩写 / 补默认行为 / 补用途下游 / 枚举写业务含义 / 接口定位 / 跨字段关系 / 自适应深度 / 不确定留批注），每模式 ≥2 真实改前改后案例 + rationale，汇总成 `reports/api-writing-patterns-2026-06-26.md`。案例均为真实实例零改动。
- [x] **项目收尾交付（资产盘点 + README + 成果落地页 + 部署）**：①**资产盘点**——全量文件分五类（产物/规划/过程/参考/归档）落 `project/ASSETS.zh-CN.md`，清理全部 `__pycache__`/`*.pyc`（本就 gitignored），记录「根 `.py` 与被 import 的工具脚本因被决策日志/报告以原路径钉死复现命令而不可移动」的约束（第七节）。②**README 重写**——`README.md` 改为完整历程（一无所知→摸清生产链路→现状分流→两条线治理→呈现交付）+ 高价值产物消费指南（质检洞察、双语 API 站、109 条批注清单、9 模式写作实践）+ 复现命令。③**成果落地页**——`site/index.html`（纯静态内联 CSS、无构建、文档负责人能力证明倾向：历程四步 + 四块产物卡 + 五阶段表 + 四条质量纪律 + 四个规模指标），相对链接 `./en/ ./zh/` 接双语 API 站。④**部署**——复用同一 GitHub Pages workflow（`.github/workflows/deploy-api-site.yml`，触发路径加 `site/**`），落地页置站点根 `/`、双语站为同级 `/en /zh`；commit `e2c831f` 推送后线上 `/`、`/en/`、`/zh/`、`/en/openai-chat.json`、`/zh/openai-chat.json` 均 HTTP 200，落地页新内容已生效。站点根 https://yuanshan8053.github.io/aisa-docs-voyager/ 。

## 进行中

- 无。阶段一/二/三/五均已全量完成。剩余仅阶段四对外报告汇总（报告甲、报告乙均可派）。

## 阻塞

- 无。阶段五浏览器 file:// 可视化截图受沙箱限制未做，但站点实质正确性已由 `check_projection.py` 三闸逐字节证明，不阻断交付（详见 D-017 与 `reports/scalar-api-site-2026-06-26.md` §6）。

## 下一步

1. **阶段五待负责人决断（见 D-017 / `reports/scalar-api-site-2026-06-26.md` §5）**：①样例档已排除；②在线 Test Request 开关（默认关闭，servers 指真网关涉鉴权）；③是否启用 GitHub Pages 部署及域名（workflow 已备 `.github/workflows/deploy-api-site.yml`，默认不自动跑）。启用后建议做一次线上目视终验。
2. **阶段四报告汇总（见 D-014 / `planning/PHASE-4-report-aggregation.zh-CN.md`）**：派遣 A（报告甲：阶段一+二内容审计）现在即可派；**派遣 B（报告乙：阶段三 API 加强）前置条件已满足**——阶段三已全量执行，可直接派全量版报告乙（覆盖 31 份 spec，而非仅 2 份试点）。两份报告形态以 `project/REPORT-CONTRACT.zh-CN.md` 为准；报告乙骨架须对齐 v2 口径（D-015/D-016，五件套 + 双闸门，无 md）。
2. **批注清单交研发**：阶段三留下 109 条 `[⚠️批注:...待研发确认]`（集中在 openapi-financial 30 / dataforseo 22 / apollo 20），是源 spec 未声明、加强时拒绝杜撰而留痕的硬事实缺口。建议整理成「待研发补全清单」反馈上游，补全后去批注、升级为确定描述。
3. **渲染层缺口（沿用 D-008，不阻断本交付）**：火山 `direct` 渲染器不渲染真实 REST 参数。本路线刻意不以渲染 md 为交付（权威是三栏对照表），故不影响价值落地；若要让加强在最终线上页可见，仍需推上线前修渲染器或换渲染路径。
4. **阶段二修复跟进（交产品负责人）**：为 agent-skills 建立对 `guides/models.mdx`+定价页的单一引用，删除离群价格/计数/端点/旧型号，14 条 6.1 缺口随之消解。
5. 项目收尾时把三阶段证据与改进汇总成对外报告交产品负责人（不提 PR，见 D-003）。

## 给接手 agent 的提醒

- 先读 `CHARTER.md` → 本文件 → `DECISIONS.md`（阶段三务必读 **D-015**：已推翻 D-013，回到 D-012 v2 双字段路线；全量化以 v2 为准。D-013 的 `ws/`、`phase3-pilot/` 旧试点产物保留作对照，不删）。
- 阶段三走 **v2 本地双字段路线**：只读 `skill-local/aisa-doc-enhance/`（先精读 `METHODOLOGY.md`），**不读** `/data/plugins/.../api-doc-agent`，不依赖 spectral / 渲染器 / doc_engine。逐字段产 `desc_en`（加强英文）+ `title_zh`（中文本地化）写进 `content.json` → `inject_xdoc.py` 加性注入 `x-doc`（不 hoist、原生零改动）→ `check_native_preserved.py`（exit 0）+ `make_review.py --require both`（三栏对照表 + 完整性闸门 exit 0）。**不产 md**。
- 干活前确认输入源仓库 `~/files/aisa-team-docs` 仍在；不在则用项目指令中的 PAT 重新克隆 `AIsa-team/docs`（PAT 永不明文打印）。
- 零误报范式（D-005/D-007）后续阶段沿用；阶段三的对应机制是两道确定性闸门 + 三栏对照表可对账。
- 完成后回写本文件 + `DECISIONS.md` + `baselines/FACTS.zh-CN.md`。
