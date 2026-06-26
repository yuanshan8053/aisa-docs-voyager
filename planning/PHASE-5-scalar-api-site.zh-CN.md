# 阶段五 · Scalar API 站点呈现（规划 + 自包含委派提示词）

> 受众：接手本阶段的新 session。读完要能独立判断「怎么把已加强的 31 份 spec 渲染成两个惊艳的 API 站点（英文 + 中文）」，并直接开工，不依赖任何上文对话。
>
> 本文件分两部分：**A. 规划与决策**（给负责人审阅，说清路线选型、边界、注意事项）+ **B. 自包含委派提示词**（直接复制给新 session 的工作指令）。

---

## A. 规划与决策

### A.0 一句话目标

把阶段三产出的 31 份 `enhanced.json`（原生 spec + 加性 `x-doc` 加强层）渲染成**两个静态 API 站点**：一个**英文站**（用加强英文 `desc_en`）、一个**中文站**（用中文本地化 `title_zh`）。要求呈现专业、惊艳，且**spec 里没有的内容一律留空，严禁杜撰**。

### A.1 核心难点的本质：加强内容在 `x-doc`，而 Scalar 只认原生字段

Scalar（与 Redoc / Swagger UI 同类）是标准 OpenAPI 渲染器，它读 `summary` / `description` / `parameters[].description` / `schema.description`。而我们的加强成果**刻意没写进原生字段**，而是加性挂在每个节点的 `x-doc` 子树里（操作级 `heading_zh`/`desc_en`/`description_zh`，字段级 `desc_en`/`title_zh`）。原生 `description` 仍是未加强的英文基线，原封不动（这是阶段三两道闸门保下来的「原生零改动」）。

所以「适配」的实质是：**让 Scalar 看到的 `description` 变成我们的加强文案**。有两条路：

| 路线 | 做法 | 评价 |
| --- | --- | --- |
| **A·改 spec 适配 Scalar（投影）** | 写一个纯 Python「投影器」，按语言把 `x-doc` 内容**投影进原生 `description`/`summary`**，产出**标准 OpenAPI 文件**（en 一份、zh 一份）。Scalar 零改动直接吃。 | **✅ 推荐**。renderer 无关（换 Redoc/Swagger 也能用）、可写完整性闸门、确定性可复现、不碰 Scalar 源码。与本项目「只增不改、可复算」气质一致——投影本身又是一层加性、可逆的派生产物。 |
| B·改 Scalar 适配 spec | fork Scalar（JS/React 组件），改其渲染逻辑去读 `x-doc`。 | ❌ 不推荐。耦合 Scalar 内部实现、脆弱、难写闸门、不可迁移到其他渲染器、维护成本高。 |

**决策：走路线 A（投影法）。** 原始 `enhanced.json` 永不改动，投影只产生 `ws-site/{en,zh}/<name>.json` 派生文件。Scalar 用官方 standalone HTML 模式加载这些标准 spec，零 fork。

### A.2 投影规则（这是「留空、不杜撰」红线在本阶段的落地）

投影器逐节点遍历，**只搬运 `x-doc` 里已存在的内容**，绝不生成新文本：

**操作级（operation 节点）**
- 英文站：`summary` ← 原生 `summary`（已是英文动作名，如 "Create chat completion"，是源事实不是杜撰；**注意：没有 `heading_en`，必须回退原生 summary**）；`description` ← `x-doc.desc_en`。
- 中文站：`summary` ← `x-doc.heading_zh`（中文动作 + Action 名）；`description` ← `x-doc.description_zh`。
- 错误码：仅当 `x-doc.errors` 存在才渲染错误表；只有 `errors_source`（说明「spec 未声明错误码」）时**不造错误表**。

**字段级（parameter / schema property 节点）**
- 英文站：`description` ← `x-doc.desc_en`。
- 中文站：`description` ← `x-doc.title_zh`。
- 批注已内联在上述字符串里（`[⚠️Note:...]` / `[⚠️批注:...]`），随文案一起进 `description`，**不得剥除**。

**留空规则（红线）**
- 节点**没有** `x-doc` 加强字段时（例如非对外字段的中间容器节点）：保留其原生 `description`（若有），否则**留空**。**严禁**用原生英文基线去顶替缺失的加强文案，**严禁**为留空处编造任何文字。
- 投影是「有则搬、无则空」，没有任何兜底生成逻辑。

### A.3 必须写的两个工具（沿用项目「确定性 + 可复算闸门」范式）

1. **`project_spec.py`（投影器）**：入参 `--enhanced <enhanced.json> --lang en|zh --out <out.json>`。逐节点把 `x-doc` 按上表投影进原生 `description`/`summary`，**剥掉 `x-doc` 子树**（产出干净标准 OpenAPI），原生骨架（paths/类型/`$ref`/required/枚举/servers）一字不动。
2. **`check_projection.py`（投影闸门）**：验证 ①每个带 `x-doc.{desc_en|title_zh}` 的节点，其投影后 `description` 恰等于对应语言字段（无遗漏、无串语言）；②原生骨架与源 `enhanced.json` 剥除 `x-doc` 后逐字节一致（无篡改）；③投影器没有写入任何 `x-doc` 之外的新文案（无杜撰）。exit 0 = 全绿。这是本阶段的「trust-but-verify」对账机制。

### A.4 站点形态与托管（**硬约束：沙箱内严禁起任何网络监听**）

- **不得**运行 `scalar serve` / `vite dev` / `http.server` / 任何绑定端口的进程（项目硬红线 `<network_security>`）。
- 交付物是**纯静态文件**：每个站点一个 standalone `index.html`，通过 Scalar 官方 CDN 的 `@scalar/api-reference` 脚本加载本地投影后的 spec JSON（支持多 spec 下拉侧边栏，把 31 份归到一个站）。两站 = `ws-site/en/index.html` + `ws-site/zh/index.html`，各自引用同语言的投影 spec。
- **预览/验证**用浏览器工具打开 `file://.../index.html` 截图核对即可（浏览器不是监听进程，允许）；正式上线由负责人在沙箱外部署，本阶段不部署、不提 PR。

### A.5 其他必须注意的事项（交付前逐条核对）

1. **英文操作标题靠回退**：无 `heading_en`，英文站操作标题用原生 `summary`。若某操作连原生 `summary` 都没有，留空，别编。
2. **批注要看得见**：`[⚠️Note]`/`[⚠️批注]` 是给读者的「待研发确认」诚实标记，渲染时确保可见（建议在投影时把批注行包成 Markdown 引用块 `> ⚠️ ...` 以突出，但**不得改其文字**）。全项目 109 条，集中在 financial/dataforseo/apollo。
3. **信息架构（IA）分组**：7 份 twitter 分片（`twitter-*`、含 batch_01/02）在站点侧边栏归并到一个「Twitter」分组——这是**呈现层分组，不动 spec 内容**。其余按服务名分组。
4. **泛标题与样例档**：`openapi`（Plant Store 示例）疑为遗留样例，建议**向负责人确认是否排除**；`kalshi`/`matching-markets`/`polymarket` 等 `title="AIsa API proxy"` 的泛标题，侧边栏显示名可用文件名兜底，**不得编造营销式标题**。
5. **交互式「Test Request」要慎开**：所有 servers 指向 `api.aisa.one`，Scalar 的在线请求客户端会真打线上网关并涉及鉴权。建议**默认关闭** in-browser API client，或明确标注鉴权要求；静态文件里**严禁**写入任何密钥/token。
6. **先验收再投影**：开工第一步先跑 `python3 ws-v2/central_accept.py` 确认 31/31 仍全绿（源 pinned `16863d3`），确保投影输入可信。
7. **双站对称性**：同一接口在 en/zh 两站的结构（path/参数/字段树）必须完全一致，仅文案语言不同——这正是投影法天然保证的，闸门 ②会兜住。
8. **dataforseo 扁平点号 key / oneOf 深层内联字段**：投影器遍历必须复用阶段三 `inject_xdoc.py` 的 `descend_object` 同款穿透逻辑（array items / oneOf|anyOf / allOf / `$ref` / 扁平字面量整键），否则深层字段会「假绿」漏投。直接参照该文件实现，别另起炉灶。

### A.6 验收标准（Definition of Done）

- `ws-site/en/` 与 `ws-site/zh/` 各含一个可在浏览器 `file://` 打开的 Scalar 站点，覆盖全部纳入的 spec。
- `check_projection.py` 对全部投影档 exit 0（无遗漏、无篡改、无杜撰、无串语言）。
- 浏览器截图核对：操作描述/参数/嵌套字段/批注/错误表均按规则正确呈现；留空处确实为空。
- 一份阶段报告 `reports/scalar-api-site-2026-06-26.md`（口径对齐 `project/REPORT-CONTRACT.zh-CN.md`），含路线选型、产物清单、闸门成绩、待负责人决断项（样例档去留、上线部署、Test client 开关）。
- 回写 `STATE.md` + `DECISIONS.md`（新增一条记录路线 A 决策）+（如涉及事实）`baselines/FACTS.zh-CN.md`。

---

## B. 自包含委派提示词（复制给新 session）

> 把下面整段作为新 session 的首条指令。它假定接手者对本项目一无所知。

```
你接手「AIsa 文档质量工程」的阶段五：把已加强的 OpenAPI spec 渲染成两个静态 API 站点
（英文 + 中文），让成果惊艳可展示。

【背景，30 秒理解现状】
- AIsa 是 OpenAI 兼容的 AI 网关。文档源仓库 AIsa-team/docs 已克隆到 ~/files/aisa-team-docs
  （pinned commit 16863d3）。本项目工作区在 ~/files/aisa-docs-voyager。
- 前序阶段一/二/三已全部完成。阶段三对 openapi/ 下 31 份 spec 做了「双字段加强」：
  在不动任何原生结构的前提下，给每个节点加性挂了一棵 x-doc 子树。产物在
  ws-v2/<spec名>/enhanced.json（共 31 份），是「原生 spec + x-doc 加强层」。
- x-doc 形态（务必先读一份真档确认，如 ws-v2/youte-search/enhanced.json）：
    · 操作节点: x-doc.heading_zh(中文动作+Action名) / desc_en(加强英文) /
      description_zh(中文) / 可选 errors / errors_source。注意没有 heading_en。
    · 参数与 schema 字段节点: x-doc.desc_en + x-doc.title_zh。
    · 批注已内联在上述字符串里: 英文 "\n[⚠️Note:...]"、中文 "\n[⚠️批注:...]"。
  原生 description/summary 仍在、是未加强的英文基线，原封不动。

【第一步：先验收输入】
跑 `python3 ws-v2/central_accept.py`，确认输出 all_green=True、31/31 双闸门全绿
（ops=667 / fields=18290 / annotations=109）。绿了才动手。

【你的任务（已定路线：改 spec 适配 Scalar，即投影法。理由见
 planning/PHASE-5-scalar-api-site.zh-CN.md 的 A.1，不要改 Scalar 源码）】
1. 写 project_spec.py（纯 Python，零包外依赖）：入参 --enhanced/--lang(en|zh)/--out。
   逐节点把 x-doc 投影进原生字段，剥掉 x-doc，产出干净标准 OpenAPI：
     · 操作: en → summary=原生summary, description=x-doc.desc_en;
             zh → summary=x-doc.heading_zh, description=x-doc.description_zh。
             仅当 x-doc.errors 存在才渲染错误表；只有 errors_source 时不造表。
     · 字段: en → description=x-doc.desc_en; zh → description=x-doc.title_zh。
   遍历必须复用 skill-local/aisa-doc-enhance/tools/inject_xdoc.py 的 descend_object
   同款穿透逻辑（array items / oneOf|anyOf / allOf / $ref / 扁平点号整键），否则深层
   字段会漏投。原生骨架(paths/类型/$ref/required/枚举/servers)一字不改。
2. 写 check_projection.py（投影闸门）：①每个带 x-doc.{desc_en|title_zh} 的节点投影后
   description 恰等于对应语言字段（无遗漏、无串语言）；②剥除 x-doc 后原生骨架与源
   enhanced.json 逐字节一致；③无任何 x-doc 之外的新文案。exit 0=全绿。对全部投影档跑绿。
3. 产物落 ws-site/en/<name>.json 与 ws-site/zh/<name>.json（各 31 份，或排除样例档后）。
4. 各语言出一个 Scalar standalone index.html：ws-site/en/index.html、ws-site/zh/index.html，
   用 Scalar 官方 CDN 的 @scalar/api-reference 加载本语言的投影 spec（多 spec 侧边栏）。
   IA：7 份 twitter-* 归并到一个 "Twitter" 分组（仅呈现层分组，不动内容）。
5. 用浏览器工具打开 file:// 的 index.html 截图核对呈现（操作描述/参数/嵌套字段/批注/
   错误表/留空处）。【严禁起任何网络监听进程：不许 scalar serve / vite / http.server /
   任何绑定端口的命令。浏览器开 file:// 截图是允许的。】
6. 出报告 reports/scalar-api-site-2026-06-26.md（口径对齐 project/REPORT-CONTRACT.zh-CN.md），
   回写 STATE.md + DECISIONS.md（新增决策记录路线 A）。

【绝对红线（违反即作废）】
- 严禁杜撰：spec/x-doc 里没有的内容一律留空。没有 x-doc 的节点保留原生 description（有则保、
  无则空），严禁用原生英文顶替缺失加强文案，严禁为空白处编任何字。批注文字一字不改、不剥除。
- 沙箱内严禁起网络监听（见上）。
- 不碰共享 .py 工具的语义（投影器是新文件；如需复用 inject_xdoc 的穿透逻辑，import 或抄函数，
  不要改原工具）。原始 enhanced.json 永不改动，只产派生文件。
- 项目指令里的 GitHub PAT 永不明文打印；不换仓库、不提 PR。
- 所有文字产出遵循 ~/files/aisa-docs-voyager/WRITING-STANDARD.zh-CN.md
  （需求视角优先、2.5 维叙事、中文用中文标点、中英文间留空格、一次成型、控篇幅、前后强一致）。

【需要向负责人确认的点（在报告里列出，不要自行臆断）】
- openapi.json（Plant Store 示例）是否为遗留样例、要不要从站点排除。
- Scalar 在线 "Test Request" 客户端是否开启（servers 指向 api.aisa.one 真网关、涉鉴权）。
- 上线部署方式（本阶段只产静态文件，不部署）。

【动手前必读】
planning/PHASE-5-scalar-api-site.zh-CN.md（本规划全文，A.2 投影规则与 A.5 注意事项是关键）、
CHARTER.md、project/STATE.md、project/DECISIONS.md（尤其 D-015/D-016 双字段路线）。
干活前确认 ~/files/aisa-team-docs 仍在；不在则用项目指令里的 PAT 重新克隆（PAT 永不明文打印）。
```
