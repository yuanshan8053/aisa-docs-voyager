# 决策日志

> 只追加，不删改。每条决策记录：编号、日期、决策、理由、影响。

---

### D-001 · 不换仓库，旧内容归档
- **日期**：2026-06-26
- **决策**：项目资产继续留在 `aisa-docs-voyager`，早期求职作品集阶段的文件移入 `archive/`，不新建仓库。
- **理由**：保留 git 历史与已有镜像、工具；早期叙事失效但有参考价值。
- **影响**：`STRATEGY.zh-CN.md`、`planning/ROADMAP.zh-CN.md`、`localized/`、`reports/` 已移入 `archive/`。

### D-002 · OpenAPI 加强 = 独立增强页 + 回写能力，放弃「直出 md」交付
- **日期**：2026-06-26
- **决策**：工作线 ③ 产出独立的增强版参考页，并新增「把增强内容回写原 spec」的能力。原工作线 ④「直出 md」关闭，折叠进 ③。
- **理由**：经核实，线上渲染后的 API 参考正文是 OpenAPI spec 内联（body 为 ```yaml openapi/xxx.json METHOD /path），并非手写 Markdown；独立交付物本就是 `openapi/*.json`。单独产 md 与线上形态不符，冗余。
- **影响**：任务 #10 关闭；阶段三的验收产物改为 `enhanced.yaml`（增强 spec）+ 独立增强参考页，外加回写校验。

### D-003 · 无写权限，暂不提 PR，最终汇总成报告
- **日期**：2026-06-26
- **决策**：对 `AIsa-team/docs` 无写权限，各阶段产物全部落本地，不提 PR。项目收尾时把全部证据与改进汇总成一份报告交产品负责人。
- **理由**：用户明确无写权限，且当前阶段目标是拿出证据确凿的真实结果，而非直接改上游。
- **影响**：所有阶段验收产物为本地文件 + 最终报告；不设 PR 类验收项。

### D-004 · 项目重定位：从求职作品集到文档质量工程
- **日期**：2026-06-26
- **决策**：废弃「作品集 / 岗位映射」叙事，项目唯一受众是 AIsa 产品负责人，唯一标准是真实、可复现、可交付。
- **理由**：文档负责人已正式入局。
- **影响**：README 与全部权威文档重写为工程视角；`project/` 层作为新的权威信息源。

### D-005 · 静态为主、探索为辅，零误报为红线
- **日期**：2026-06-26
- **决策**：凡列为「阻断硬伤」的结论，必须能仅凭 `AIsa-team/docs` 源仓库文件证伪；live 探测结果只作 INFO 旁证，绝不单独定罪。
- **理由**：纯网络探测的 `http_status:0` 无法区分「文档真坏」与「本地网络被挡」，会产生误报。
- **影响**：阶段一静态检查器是确定性引擎；live-probe 审计器（`aisa_doc_auditor`）降级为旁证工具。

### D-006 · 撤下「技能计数漂移 13 vs 43」这条硬伤
- **日期**：2026-06-26
- **决策**：阶段一实跑复核后，从硬伤清单中移除前序基线的「`guides/agent-discovery.mdx` 写死 13 skills，而 `agent-skills/` 实有 43」。它不再列为 BLOCKER，也不进首份报告的定罪项。
- **理由**：A2A agent card 广播的 13 个 skill 与 `agent-skills/` 目录下 43 个可安装技能页是两个不同概念（一个是发现协议里的能力条目，一个是面向用户的安装页）。文档正文「advertises 13 skills」与其紧随的 13 行技能表内部自洽，无法仅凭源仓库文件证伪。按 D-005 零误报红线，不能定罪。
- **影响**：FACTS「硬伤 2」改写为「经复核撤下」。阶段一改以三项**全量 spec 形态**矛盾立案（schema 121→321、分类 10→14、分类表漏列 4 项），均可仅凭 `openapi.yaml` 证伪。

### D-007 · 阶段一真值取已提交的 openapi.yaml，定罪只限「整份 spec」语境
- **日期**：2026-06-26
- **决策**：静态检查器的 spec 真值取仓库已提交的 `openapi.yaml`（而非现跑 consolidate 脚本）；对散文数字定罪时，仅当该行处于「整份 spec」语境（命中 `openapi.yaml`/`consolidated`/`the spec`/`machine-readable` 等标记）才比对全量真值。
- **理由**：`openapi.yaml` 是线上参考正文内联渲染所依据的同一份产物，无歧义且不引入脚本执行的不确定性。语境闸门用于排除局部计数误报——例如 `changelog.mdx` 的「CoinGecko API (23 Endpoints)」是单集成局部数（coingecko.json 实有 21 路径），曾被一版检查器误判为「23≠645」，加闸门后排除。
- **影响**：确立后续阶段「真值绑定 + 语境约束」的零误报范式。

### D-008 · 阶段三对内联 schema 用「加性注入扩展」，绝不 hoist 改原生结构
- **日期**：2026-06-26
- **决策**：`api-doc-agent` 的确定性内核 `doc_engine.py` 只遍历 operation 级与 `components.schemas` 注入 `x-doc`；而 AIsa 的 spec 普遍用内联请求/响应 schema 与 operation 级 `parameters`（无 `$ref` 具名组件），引擎默认不触达。对此**新增加性扩展 `inline_inject.py`**：`import doc_engine` 后复用其逐节点函数（`_process_schema`/`assemble_property_xdoc`/`merge_node`），在内联 schema 根与 `parameters` 上再跑同一套确定性逻辑。**明确否决**「把内联 schema 提升（hoist）为具名 `$ref`」这一让引擎顺手的做法。
- **理由**：hoist 会把原本内联的结构搬进 `components.schemas`、在 `paths` 里平添 `$ref` 指针，**篡改原生骨架**，直接违反「只增不改」红线并使 `check_native_preserved.py` 失败。正确姿态是顺着工具接缝加性扩展，而非掰弯数据迁就工具。复用引擎自身函数则 R1–R10 源保护、`src_hash`、`source=ai` 治理戳全部原样继承，不另起一套逻辑。
- **影响**：`openai-chat.json` 与 `youte-search.json` 两份试点用同一未改动的注入器跑通，均 Gate 2 零 error、`check_native_preserved.py` exit 0、回写 diff 零删除。该扩展确立为阶段三全量化的注入入口。附带发现一处渲染层缺口（`direct` 平台不渲染真实 REST query 参数，仅渲染火山 `Action`/`Version` 信封），记为渲染器待办，不阻断增强与回写。

### D-009 · 阶段二散文质检用 Map-Reduce 多 agent，三层隔离防确认偏误
- **日期**：2026-06-26
- **决策**：散文 AI 友好度质检改用 `ai-friendly-doc-check-multiagent-v10` 的 Map-Reduce 范式——三路探查 agent（方法 A 全库精读 / 方法 B 流式三遍 / 规范核对固定清单）并行 Map，单汇总 agent Reduce。**三层隔离**：探查 agent 永远看不到分类体系（只凭五问标尺找会坑 Agent 的地方），规范核对 agent 只拿固定清单 1.1–6.3，唯有汇总 agent 看得到 `categories.md` 做回贴归类。
- **理由**：散文的坑是语义级的（同模型几套价、同 registry 两个地址、列名与说明串题），静态规则抓不到，须靠读懂语义 + 跨页对账。若让探查端预先知道分类框架，会按框架找证据、制造确认偏误并漏掉框架外的坑。隔离后探查端只对「会不会坑到 Agent」负责，召回更高。
- **影响**：阶段二（30 页试点 + 73 页全量）均按此跑。方法沉淀见 `reports/ai-friendly-method.zh-CN.md`。

### D-010 · 散文零误报沿用 D-005/D-007 范式：两条硬线撤回 + 去向台账可对账
- **日期**：2026-06-26
- **决策**：散文质检的零误报红线落地为四道机制：①**两条硬线撤回律**——一条线索只有「源文件 Ctrl+F 搜得到原文证据」才可能保留，只要满足「证据搜不到」或「存在消歧原文（两处指不同对象 / 上下文已说明差异）」立即撤回；②逐字复核每条保留项；③**去向台账可对账**（原始 = 保留 + 并入 + 撤回，三者相加须等于原始数）；④跨页事实一律以 June-4 刷新、内部自洽的权威集（`models.mdx`+定价页+`chinese-llms/*`）为真值，agent-skills 离群快照才是被告，权威集内部一致值绝不报。
- **理由**：延续阶段一「真值绑定 + 语境约束」范式（D-005/D-007）到语义层。散文里「概数 50+ vs 精确 57」「100+ 端点 vs 111+ 路径」这类相容项极易被误判为冲突，须用作用域/概数判别挡住；Kimi `temperature` 约束与 cn-llm 通用参数描述指不同模型，也须经逐字核对才能判「非同一对象 → 不报」。
- **影响**：73 页全量 **47 原始线索 → 20 保留 + 21 并入 + 6 撤回**，账平，零误报。撤回的 6 条（如 `AIsa-skills` 组织名在 agent-skills 任何页搜不到）与 5 处「待人工确认」均在报告 `四、零误报口径` 留痕。

### D-011 · 阶段二主病灶定性：agent-skills 缺单一权威事实源，14 条 6.1 同根
- **日期**：2026-06-26
- **决策**：把全量 73 页 20 条缺口的根因定性为单一病灶——**agent-skills 这 43 页缺一个被全站引用的权威事实源**：模型价、上下文窗口、家族计数、API 端点路径全是各页作者各自手抄的离群快照，谁也没去引用 `guides/` 那套 June-4 刷新、内部自洽的权威目录（`models.mdx`+定价页）。修法收口为一条：agent-skills 各页改为**引用**权威源，删除自维护的离群价格/计数/端点/旧型号。
- **理由**：20 条里 14 条命中 6.1（跨文档同对象取值不一致），且全部是 agent-skills 页与权威源对不上账（同模型几套价 P1–P4/P10、同能力两套路径 P5、一份清单几个数 P7/P11–P14/P17、挂旧型号 P8/P9）。试点 30 页只 10 条、且 guides 内部权威目录自洽——并入 43 页后缺口翻倍且新增几乎全来自 agent-skills，根因清晰指向「手抄而非引用」。
- **影响**：交付建议以「建立单一引用、删除离群快照」为最高优先级；该结论是阶段二报告的核心结论，也是后续若推动上游修复的纲领。

### D-012 · 阶段三 v2：推翻重型渲染链路，改「只吸收写作内核 + LLM 推理双字段加强 + 三栏对照表」
- **日期**：2026-06-26
- **决策**：废弃 v1 用原 `api-doc-agent` 重型三引擎（Spec Engine → doc_engine 装配 → Renderer + spectral 三闸门）产渲染 md 的做法。v2 只吸收写作内核（蒸馏成一份 `METHODOLOGY.md`），由 **LLM 推理逐参数**加强，交付从「中文单字段 `title_zh`」升级为**双字段**——加强英文 `desc_en`（保留并加强源英文）+ 中文本地化 `title_zh`（据加强英文做地道中文）；并以原生 `description`（只读）+ `desc_en` + `title_zh` **三栏并存可对账**。新建本地改造版技能 `skill-local/aisa-doc-enhance/`（standalone 纯 python3，不依赖任何包外引擎），派遣 agent **只读本地版**。
- **理由**：v1 试点交付物是渲染后 md，而 `direct`（火山）渲染器按 `Action`/`Version` 信封模板生成、**不渲染** AIsa 真实 REST 参数，加强价值在最终产物里隐形，产品负责人无法确认「改了什么、改好还是改坏」（用户原话痛点）。根因是「拿渲染器当交付」叠加渲染器平台缺口。砍掉渲染层、改用 `make_review.py` 三栏对照表直接呈现每个字段的「源→加强→本地化」三态，痛点即解。重型引擎对「把 spec 写好」这一目标是冗余依赖。
- **影响**：阶段三验收产物改为 `content.json`+`enhanced.json`+`review_table.md`+`inject_review.json`+报告；两道确定性闸门替代 spectral——`check_native_preserved.py`（原生保全，exit 0）+ `make_review.py`（对外字段完整性，缺漏即非零，杜绝偷懒漏写）。本地技能与三工具已自测通过（youte-search 11 字段注入、原生保全 exit 0、完整性 exit 0；缺字段触发 exit 1；坏 dotpath 记 unresolved；具名 `$ref` spec 解引用正常）。继承 D-008「只增不改、不 hoist」红线。v1 试点产物 `phase3-pilot/` 保留作对照，不删。

### D-013 · 阶段三回采 api-doc-agent x-doc 路线：spectral 已可装，双闸门收口为「真 lint green + 原生保全 exit 0」
- **日期**：2026-06-26
- **决策**：按用户本轮明确指令，阶段三回采 `api-doc-agent` 确定性管线 + `x-doc` 命名空间这条路线（D-002 的原始形态：增强 spec + 独立增强页 + 回写），不走 D-012 的 v2 本地三栏方案。交付物为 `content.json`（人工撰写增强内容）→ `enhanced.yaml`（注入 `x-doc` 后的增强 spec）→ `enhanced-page.md`（独立增强页）→ `writeback.diff`（回写 diff）+ `review_list.json`。Gate 2 用已装到 `$HOME` 的 `spectral 6.16.0` 对 `doc-engine-output.spectral.yaml` 真 lint，配 `check_native_preserved.py` 构成双确定性闸门。
- **理由**：D-012 当时推翻 v1 的两条理由——①渲染器隐形、②spectral 装不上只能跳过当 yellow——本轮均已变化：spectral 6.16.0 已成功装到 `$HOME`，Gate 2 可做**真正 lint 过的 green**（7 规则全启用、error 0），不再是「未装跳过」；且本轮交付物**不以渲染 md 为准**（按 D-002，权威产物是回写后的 `enhanced.yaml`，渲染页仅作旁证），渲染器隐形缺口降级为不阻断的待办（§4 已留痕）。用户本轮指令是最高优先级，明确要求 x-doc / enhanced.yaml / spectral 路线。
- **影响**：两份试点 `openai-chat.json`（内联请求体）、`youte-search.json`（query 参数 + 内联响应体）均跑通：Gate 2 error 0、`check_native_preserved.py` exit 0、回写 diff 零删除（+80/−0、+70/−0）。新增 source=human 保护演示：人工改写 operation 的 `description_zh` 并标 `source: human`，AI 版重跑注入后人工内容原样保留、AI 不同建议分流进 `review_merged.json`（reason R3/R5），机器级坐实「AI 永不静默覆盖人工」。产物落 `ws/openai-chat/`、`ws/youte-search/`，报告 `reports/openapi-enhance-pilot-2026-06-26.md`。继承 D-008「只增不改、不 hoist」、复用 `phase3-pilot/inline_inject.py` 作全量注入入口。与 D-012 并存：v2 本地技能 `skill-local/aisa-doc-enhance/` 不删，作为备选路线保留；本阶段全量化以本路线（D-013）为准。



### D-014 · 设报告汇总环节（阶段四）+ 报告契约：两份对外报告，咨询体例，证据可四步闭环
- **日期**：2026-06-26
- **决策**：在三阶段工程产物之上新增独立的「报告汇总环节」，把散落的过程产物重组成两份对外报告交产品负责人。阶段一（硬伤）+ 阶段二（散文 AI 友好度）合成《报告甲：存量文档内容审计》；阶段三单出《报告乙：API 内容加强》。形态由新建的权威文件 `project/REPORT-CONTRACT.zh-CN.md`（报告契约）规定，汇总流程与两份自包含委派提示词落 `planning/PHASE-4-report-aggregation.zh-CN.md`。两次独立派遣专业咨询专家 agent：派遣 A（报告甲，现在即可）、派遣 B（报告乙，须等阶段三全量执行）。
- **理由**：阶段产物是工程视角的过程稿，受众（产品负责人）要的是好查证、好理解的对外交付物。调研世界级咨询公司（麦肯锡/BCG/Bain）的研究报告呈现法，提炼五条规则落进契约：结论先行（金字塔原理）、SCQA 开场、结论式章节标题、发现必答「so what」、靠透明（交代撤回/待确认）建立可信。与项目自身「找根因比找问题更重要」同源——两份报告重心都压在根因与建议。用户痛点「不好查证不好理解」落地为硬性证据字段：线上文档 URL + git permalink（钉 pinned commit `16863d3`，不用 `main`）+ 行号 + 问题描述 + 可 Ctrl+F 的原文引用 + 可独立跑的复现命令，每条须「点 URL→跳 git 行→Ctrl+F→跑命令」四步闭环。
- **影响**：新增 `project/REPORT-CONTRACT.zh-CN.md`（形态权威，与 `WRITING-STANDARD.zh-CN.md` 文风权威并列）、`planning/PHASE-4-report-aggregation.zh-CN.md`（汇总流程 + 提示词）。报告乙的产物口径对齐 D-013（`enhanced.yaml`/`enhanced-page.md`/`writeback.diff`/`review_list.json` + spectral 双闸门），不再引用 D-012 的 v2 三栏方案。汇总 agent 铁律：不产出新事实、不改已定结论，疑似遗漏只进「待负责人决断」。报告甲现在即可派；报告乙待阶段三全量执行后派（或先出仅覆盖 2 份试点的试点版并标注范围）。

### D-015 · 阶段三回到 D-012 v2 双字段路线：英文加强→中文本地化，弃 md，三栏对照表为权威呈现
- **日期**：2026-06-26
- **决策**：按用户本轮明确反馈，阶段三**推翻 D-013 的 api-doc-agent x-doc 单字段（`title_zh`）+ `enhanced-page.md` 路线**，回到 D-012 的 v2 本地双字段方案：① 加强分两层——先**加强英文 `desc_en`**（在源英文上加强），再据其做**中文本地化 `title_zh`**，二者语义一致；② **不产任何渲染 md**（`enhanced-page.md` 取消）;③ 权威呈现是 `make_review.py` 抽取的**三栏对照表**「源英文（原生只读）→ 加强英文 desc_en → 中文 title_zh」，覆盖**接口级描述 + 参数 + 请求/响应字段**（不限参数）;④ 写作严格按 `skill-local/aisa-doc-enhance/METHODOLOGY.md`，禁止脚本套模板、禁止注水、禁止复制原生元数据。派遣 agent **只读** `skill-local/aisa-doc-enhance/`，不依赖 spectral / 渲染器 / doc_engine。
- **理由**：用户验收两份 D-013 试点后明确指出三处偏离：(1) 加强方向错了——应是「英文加强 + 中文本地化」双字段，而非单中文字段；(2) 仍然产出了不需要的渲染 md;(3) 价值呈现应能从增强 spec 抽取「原文 en / 加强 en / 本地化 cn」做表格对比，且不限于参数、含操作描述。这三点恰是 v2(D-012)的设计立意，本地技能 `aisa-doc-enhance` 与三工具已就绪。用户指令为最高优先级，故回采 v2。
- **影响**：阶段三验收产物改回 v2 五件套——`content.json`（双字段）+ `enhanced.json`（含 `x-doc`，原生零改动）+ `review_table.md`/`.json`（三栏对照表 + 完整性闸门）+ `inject_review.json`（注入审计）,**无 md**。两道确定性闸门：`check_native_preserved.py`（原生保全 exit 0）+ `make_review.py` 完整性（每个对外字段须齐备 `desc_en`+`title_zh`，缺漏即非零）。两份试点 `youte-search`（11 字段）、`openai-chat`（16 字段，含 `oneOf` 深层内联）已在 v2 路线重跑通过，产物落 `ws-v2/youte-search/`、`ws-v2/openai-chat/`，均双闸门 exit 0、原生零改动。**修复一处工具 bug**：`make_review.py` 原 `walk_schema` 不穿透 `oneOf/anyOf/allOf` 分支，导致注入进 `oneOf` 的 4 个字段（`messages.content.type/text/image_url`、`function_call.name`）在对照表中隐形、完整性闸门「假绿」（injector 写 16、review 仅列 12）；已对齐 `inject_xdoc.descend_object` 的穿透逻辑，现 review 列全 16 字段，闸门为真绿。D-013 的 `ws/`、`phase3-pilot/` 旧试点产物保留作对照不删；全量化以本决策（D-015，即 v2）为准。`planning/PHASE-3-openapi-enhance.zh-CN.md` 本就是 v2 文档，无需改；`REPORT-CONTRACT.zh-CN.md` 报告乙骨架与 `PHASE-4` 派遣 B 提示词须从 D-013 口径改回 v2 口径。

### D-016 · 阶段三 v2 全量执行收口：31 档全绿 + 工具链第 4 次一致性修复 + agentmail dup-operationId 认定
- **日期**：2026-06-26
- **决策**：按 D-015 的 v2 双字段路线**全量执行完阶段三**——31 份 spec / 667 operation / 18,290 对外字段 / 109 主动批注。中央验收以 trust-but-verify 为准：不信任已落盘 `enhanced.json`，从每份 `content.json` 在 pinned 源 `16863d3` 上现场重算，再过两道闸门。结果 **31/31 双闸门全绿**：`check_native_preserved.py` 31 份 exit 0（原生零改动）、`make_review.py --require both` 31 份 missing=0（每对外字段齐备 `desc_en`+`title_zh`）、落盘产物与现场重算 31 份字节一致。超大档 `dataforseo`（445 op）切 13 个互斥 path 分片、`agentmail`（46 op）切 2 个分片，由并发子 agent 各写分片 `content.json`，合并后在全档上一次性重注入 + 双闸门复验。报告落 `reports/openapi-enhance-v2-2026-06-26.md`。
- **理由**：D-015 已定 v2 为全量路线，本决策记录其执行结果与三处工程实情，以便后续可审计、可复现。①**大档分片**：用 `slice_spec.py` 按 path 段切片（保留全量 `components` 保 `$ref`），opKey（operationId 或 "METHOD /path"）与全档一致，故分片 content 可无缝合并；dataforseo 13 分片 opKey 全档唯一，用 `merge_content.py` 严格合并（同 key 即冲突退出，杜绝重复认领）。②**agentmail dup-operationId**：源 spec 把 46 个 operation 复用成仅 12 个 operationId（`get`/`list`/`delete` 等在多条 path 上同名），`merge_content.py` 的严格去重会误判为冲突，故新建专用 `union_merge.py` 按 opKey + dotpath 深合并；注入后 `unresolved=1347` 是「一份 content 块被应用到该 operationId 下全部同名 path、非匹配兄弟 path 记 harmless unresolved」的源结构属性，**非缺陷**——判定依据是两道绑定闸门（原生 exit 0、missing=0，944 实际字段全齐备），operationId 是不可改的原生结构，故认定为**可接受工程产物**。③**工具链第 4 次一致性修复**：dataforseo/apollo 响应 schema 把深层字段存成字面量含点号/方括号的扁平 property key（如 `properties["tasks.result.items.keyword"]`、`properties["account_stages[].category"]`，容器自身仅占位），原 `inject_xdoc.resolve_property` 按 `.` 逐段下钻永远命不中，而 `make_review` 按字面枚举又要求其齐备——首批子 agent 据此正确报告 unresolved==missing 并**拒绝杜撰/私改工具**（守红线）；我亲眼核实 schema 形态后，在权威 `inject_xdoc.resolve_property` 加「最长字面量整键优先匹配」（纯嵌套 schema 行为不变，扁平点号整键一次命中，与 make_review 口径对齐），validated 覆盖 apollo + 全部 13 个 dataforseo 分片，无需任何 per-slice workaround（试点期临时绕行脚本 `inject_flatkeys.py` 已删）。这是 descend/resolve 一致性 bug 类的第 4 个实例（前三个均在试点期修过）。
- **影响**：阶段三全量交付定案，产物落 `ws-v2/<spec名>/` 五件套（无 md）+ 中央验收脚本 `ws-v2/central_accept.py`（exit 0 = 31 份全绿，可一键复跑）+ agentmail 专用合并器 `ws-v2/agentmail/union_merge.py`。**阶段四报告乙前置条件已满足**——可直接派全量版报告乙（覆盖 31 份 spec，而非 D-014/PHASE-4 原写的「仅 2 份试点版」）。`inject_xdoc.py` 的 `resolve_property` 现为最新修复版，子 agent 沿用不再触此 bug。109 条批注建议整理成「待研发补全清单」反馈上游。绝对红线（不杜撰、主动批注、PAT 不明文、占位符逐字节保留、不换仓库/不提 PR、不直连 LLM Gateway、不启网络监听）全程无违反。

### D-017 · 阶段五呈现走路线 A 投影法：改 spec 适配 Scalar，不 fork 渲染器；三闸对账 60/60 绿
- **决策**：阶段五把已加强的 31 份 spec 渲染成两个静态 API 站点（英文 + 中文），呈现层路线定为**路线 A · 投影法**——写纯 Python 投影器 `project_spec.py`，按语言把 `x-doc` 投影进原生 `summary`/`description`、剥掉 `x-doc`，产出干净标准 OpenAPI 派生档 `ws-site/{en,zh}/<name>.json`；Scalar 用官方 CDN standalone 模式（`@scalar/api-reference` v1.61.0，MIT）零改动加载。配套投影闸门 `check_projection.py`（三闸：闸①无遗漏·无串语言、闸②无篡改·双树字节比对、闸③无杜撰·错误内容 token 溯源），对 60 份投影档 exit 0。**否决路线 B（fork Scalar 改其渲染逻辑读 `x-doc`）**。按用户决断：排除 Plant Store 样例（31→30）；在线 Test Request 默认关闭；提供 GitHub Pages + Actions 部署 workflow（`.github/workflows/deploy-api-site.yml`，默认不自动跑，启用交负责人）。
- **理由**：加强成果挂在 `x-doc`，而 Scalar/Redoc/Swagger 只认原生字段，直接喂源档显示的还是未加强英文。投影法 renderer 无关（换 Redoc/Swagger 也能用）、可写确定性闸门、可复现、可逆、不碰渲染器源码，与项目「只增不改、可复算」气质一致——投影本身又是一层加性可逆派生产物。路线 B 耦合 Scalar 内部实现、脆弱、难写闸门、不可迁移、维护成本高，否决。用户三点确认：①不保留样例；②先验证 Scalar 真可用再决定保留（已验：CDN HTTP 200、3.6 MB bundle 暴露 `createApiReference`）；③要上线，找可用方式如 GitHub。
- **影响**：阶段五交付定案，产物——投影 spec 60 份（`ws-site/en/` 30 + `ws-site/zh/` 30）+ 两个 Scalar standalone 入口 `ws-site/{en,zh}/index.html`（多 spec 侧边栏，由 `build_index.py` 从磁盘 `*.json` 派生，7 份 twitter-* 加 "Twitter · " 前缀聚簇，`openai-chat` 置顶 default）+ 三工具（`project_spec.py`/`check_projection.py`/`build_index.py`）+ 可选部署 workflow。**三闸 60/60 绿**：投影后 664 操作描述 + 16,876 字段描述 + 9 张错误表全由 `x-doc` 搬运，109 条 `[⚠️批注]` 一字不改进 description，原生骨架与源 `enhanced.json` 逐字节一致，`x-doc` 残留为 0。原始 `enhanced.json` 永不改动，投影器复用 `inject_xdoc.HTTP_METHODS` 与同款穿透逻辑、不改原工具。报告 `reports/scalar-api-site-2026-06-26.md`。**未竟（如实留痕）**：浏览器 file:// 截图可视化核对受沙箱三重限制（本地 harness 拒 file://、远程拒 file://+data:+内部 URL、Scalar 相对 fetch 在 file:// 受 CORS——上线 http(s) 即解）未能完成；但站点实质正确性已由三闸逐字节证明，未验仅剩 Scalar 视觉呈现，建议负责人启用 GitHub Pages 后线上目视终验。绝对红线（不杜撰、批注一字不改、PAT 不明文、占位符逐字节保留、不换仓库/不提 PR、不直连 LLM Gateway、不启网络监听）全程无违反。

### D-018 · 撤回 D-017 的样例档排除：按负责人要求站点凑齐 31/31 份 spec
- **决策**：按负责人本轮要求，把此前 D-017 排除的 Plant Store 示例档 `openapi`（title="OpenAPI Plant Store"，2 path / 3 op）补回站点，使英文站与中文站各覆盖 **31 份 spec**（与源 `ws-v2/` 全量一致），不再排除任何档。
- **理由**：D-017 当初排除样例档是延续阶段一/二「疑似遗留样例」的审计判断（A.5.4）；本轮负责人明确「希望部署所有 31 个 spec」，用户指令为最高优先级，故撤回该排除。补档走与其余 30 份完全一致的确定性管线——投影器 `project_spec.py` 投影（ops=3 / fields=7 / error_tables=3）+ `check_projection.py` 三闸 en/zh 均 exit 0，无任何特例处理。
- **影响**：新增 `ws-site/{en,zh}/openapi.json` 两份投影档 + `build_index.py` 自动重建两入口（每站 31 source，`openapi` 入侧边栏）。全量闸门复跑 **62/62 全绿**。GitHub Pages 重新部署成功（commit `6056d86`），线上 `en/zh/openapi.json` 与两入口均 HTTP 200。报告 `reports/scalar-api-site-2026-06-26.md` §5 决断一（样例档去留）据此更新为「按负责人要求纳入」。

### D-019 · 撤回 D-018：站点只部署 30 份 AIsa 真实 spec，剔除玩具示例 openapi(Plant Store)
- **决策**：撤回 D-018，站点恢复为 **30 份 AIsa 真实 spec**，移除 `openapi`（"OpenAPI Plant Store"，OpenAPI 官方卖植物玩具示例，与 AIsa 网关无关）。最终口径与 `baselines/FACTS.zh-CN.md` 的「31→30 spec」一致：源 `ws-v2/` 31 份含 1 份玩具，AIsa 真实 spec 恰为 30 份。
- **理由**：D-018 把「部署所有 spec」误解为「凑齐 31 份」从而补进玩具；负责人本轮澄清真实意图是「部署 AIsa 所有 spec，而非玩具示例」。AIsa 真实 spec 全集本就是 30 份，故移除玩具即满足「全部 AIsa spec」。这印证 D-017 当初排除样例档的判断是对的——D-018 是一次基于数字误读的临时往返，D-019 回到正确口径。
- **影响**：删 `ws-site/{en,zh}/openapi.json`，`build_index.py` 重建两入口（每站 30 source）。全量闸门复跑 **60/60 全绿**。GitHub Pages 重新部署成功（commit `bbb4f9d`）：线上 `en/openapi.json` 返回 404（玩具已下线）、`en/openai-chat.json` 等 AIsa 档与两入口均 200。报告 `reports/scalar-api-site-2026-06-26.md` §0 元信息与 §5 决断一据此回正为「30 份 AIsa 真实 spec，剔除玩具」。

### D-020 · 收尾整理：删除 archive/、清理求职作品集叙事、试点收拢到 pilots/
- **决策**：按负责人要求做三件文件治理：① 删除 `archive/` 整个目录（早期求职作品集阶段产物，与文档质量工程无关）；② 清除散落在 `README.md`/`CHARTER.md`/`HANDOVER.md`/`ASSETS.zh-CN.md` 等当前文档中指向求职作品集、指向 `archive/` 的前向表述；③ 把根目录散落的两份试点目录 `ws/`、`phase3-pilot/` 统一收拢到 `pilots/ws/`、`pilots/phase3-pilot/`。
- **理由**：负责人明确「archive 内容完全无关，可移除；别的地方也一律删除求职作品引用」「试点测试文件可以统一收到一个文件夹」。本决策日志只追加不删改，故 D-001/D-004/D-013 等历史条目里对 `archive/`、求职作品集、`ws/`、`phase3-pilot/` 的**历史记述保持原样**（它们记录的是当时为什么这么做），仅治理当前生效文档中的前向引用与物理路径。
- **影响**：`archive/`（6 文件）删除；`ws/`、`phase3-pilot/` → `pilots/` 下；`ASSETS.zh-CN.md` 分类由五大类回到四大类（删「归档」类）、第六节「归档」整节删除并重编节号、读图与盘点动作同步更新；`CHARTER.md`/`HANDOVER.md`/`README.md` 求职作品集与 archive 表述删除。试点旧产物按 D-013/D-015 仍保留作对照，只是改了存放路径；引用 `pilots/ws/`、`pilots/phase3-pilot/` 的旧复现命令需相应加 `pilots/` 前缀。

### D-021 · 站点重设计上线 + 一键机器验收 accept_all.py
- **日期**：2026-06-28
- **决策**：把成果落地页换成专业重设计版并新增独立的质检报告叙事页，二者共用双主题。① 落地页 `site/index.html` 重设计为**双主题**（`data-theme="A"` 沉浸体验暗色 / `data-theme="B"` 阅读模式暖纸白），顶栏按钮 + 键盘 1/2 切换、`localStorage` 键 `aisa-docs:theme` 跨页持久化；保留全部真实事实（8 块规模指标、四步历程、四块产物卡、五阶段表、四条质量纪律），新增终端块展示一键验收命令。② 新增 `site/ai-friendly.html`——可读版质检报告《从一个连字符看 Agent 的文档体验》的网页化叙事页，忠于 `reports/ai-friendly-prose-readable-2026-06-26.md`，5 章 + 目录锚点 + 28 条 GitHub permalink（pinned `16863d3`）+ aisa.one 链接，落地页「质检报告」入口经 `./ai-friendly.html` 进入。③ 新增一键机器验收 `accept_all.py`（`--baseline 16863d3` → `ws-v2/central_accept.py` 双闸门 31/31 + `check_projection.py` 投影三闸 60/60，exit 0），配 `tests/test_accept_all.py`、`tests/test_central_accept_paths.py`。
- **理由**：D-017/D-020 的落地页是纯静态最小实现，负责人希望站点风格再专业打磨一轮，且想基于可读版质检报告单出一个对外页面、并提供多主题供决策——故委派专业设计 Agent 产出，本轮做验收接线与上线。`accept_all.py` 把此前分散的两套门禁（OpenAPI 双闸门、站点投影三闸）收成一条可复跑命令，且诚实地**不**把「漏报/误报 0/0」写成机器门禁（那是人工/多 Agent 报告复核结论，非单脚本可重判），守零杜撰红线。
- **影响**：①**修复设计交付的文件名前缀坑**——设计 Agent 把两页交付为 `site/site_index.html` / `site/site_ai-friendly.html`，但页内链接与部署 workflow 均按无前缀的 `./index.html` / `./ai-friendly.html`，原样部署会让站点根 `/` 仍是旧版、质检 tab 404；`git rm` 旧 `index.html` + `git mv` 去前缀对齐，部署 workflow「Assemble site root」步增 `cp site/ai-friendly.html _site/ai-friendly.html`（否则报告页 404）。②上线前逐项验收：跨页链接全部 resolve、`accept_all.py --baseline 16863d3` exit 0、中文正文无半角标点。③commit `10cf6ec` 推送后线上 `/`、`/ai-friendly.html`、`/en/`、`/zh/`、`/en/openai-chat.json`、`/zh/openai-chat.json` 均 HTTP 200，双主题落地页与叙事页已生效。④文档层改动（`project/**`）不触发 Pages workflow（仅 `site/**`/`ws-site/**`/workflow 自身路径触发），故本轮 doc 更新无需重新部署。绝对红线（不杜撰、批注一字不改、PAT 不明文、占位符逐字节保留、不换仓库/不提 PR、不直连 LLM Gateway、不启网络监听）全程无违反。

### D-022 · 外部审计校正：permalink 数笔误（28→17）+ 展示产物打磨去黑话/去过程/去受众表述
- **日期**：2026-06-28
- **决策**：以「不信任任何既有结论」的外部审计视角全量复核后，做两类校正。①**事实笔误校正**：`site/ai-friendly.html` 与源报告 `reports/ai-friendly-prose-readable-2026-06-26.md` 实有 **17 条** GitHub permalink（按 href 计数、全文计数、去重计数三法一致，全 pinned `16863d3`、行号准确），而 D-021 正文及 `STATE.md`/`ASSETS.zh-CN.md` 误记为「28 条」。产物正确、文档数字错——已把 `STATE.md`（2 处）、`ASSETS.zh-CN.md`（1 处）改为 17；D-021 因本日志「只追加不删改」铁律不在原地改，以本条为准。②**展示产物打磨**（`site/index.html`、`site/ai-friendly.html`）：去黑话（「人写散文」「OpenAPI」首次出现加角标脚注、「双字段/五件套」改为「英文加强 + 中文本地化」「加强产物」自解释）、去过程表述（删「一字不可改」）、去受众表述（删落地页 footer 与叙事页 meta 的「受众：产品负责人」，并删 `README.md`/`CHARTER.md`/`STATE.md`/`REPORT-CONTRACT.zh-CN.md`/`HANDOVER.md` 中「唯一受众是 AIsa 产品负责人」前向表述）、去「参考文/参考文档」自指（叙事页 2 处改为直述原则）、规避中英混杂（「单一可信源（Single Source of Truth）」统一为中文「单一可信源」、「rationale」改「取舍理由」）、消解口径（「账平」改「零误报」、「17,550 对改前改后」改为「18,290 个加强字段的改写实例」对齐加强口径、「投影三闸·无杜撰」补一句实现说明）。
- **理由**：负责人要求展示产物面向「只知大概的同事」也能一次读懂、被追问能自圆、规范写作；外部审计同时发现 permalink 数文档笔误。两类都属「修复已发现问题」，合并记一条。展示产物的术语自解释与去过程化不改任何事实数字，仅改表述；事实笔误校正以产物与源报告的可复算计数为准。
- **影响**：`site/index.html` 8 处文案 + `site/ai-friendly.html` 5 处文案改写;`README.md`/`CHARTER.md`/`STATE.md`/`REPORT-CONTRACT.zh-CN.md`/`HANDOVER.md` 各 1 处「唯一受众」删除;`STATE.md`/`ASSETS.zh-CN.md` permalink 数校为 17。`DECISIONS.md` 历史条目（D-004「唯一受众」、D-021「28 条」）按只追加规则保持原样，本条为现行口径。展示产物改动落 `site/**`，推送后触发 Pages 重新部署并线上目视复验。绝对红线全程无违反。
