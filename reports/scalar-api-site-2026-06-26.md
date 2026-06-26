# 阶段五 · Scalar API 站点呈现报告

> 受众：AIsa 产品负责人。一句话结论先给，证据与待决断项随后。
> 口径权威：`project/REPORT-CONTRACT.zh-CN.md`（形态）+ `WRITING-STANDARD.zh-CN.md`（文风）。

## 0. 元信息

| 项 | 值 |
| --- | --- |
| 交付对象 | 已加强的 31 份 OpenAPI spec → 两个静态 API 站点（英文 + 中文） |
| 纳入站点 | 30 份（排除 Plant Store 样例 `openapi.json`，见 §5 决断一） |
| 源 | `ws-v2/<spec>/enhanced.json`（原生 spec + 加性 `x-doc` 加强层），源仓库 `AIsa-team/docs` pinned `16863d3` |
| 路线 | **路线 A · 投影法**（改 spec 适配 Scalar，不 fork 渲染器），见 D-017 |
| 闸门 | `check_projection.py` 三闸（无遗漏 / 无篡改 / 无杜撰·无串语言），60/60 投影档 exit 0 |
| 日期 | 2026-06-26 |

## 1. 执行摘要

**现状**：阶段三把 31 份 spec 的加强成果（加强英文 `desc_en` + 中文本地化 `title_zh`）刻意挂在每个节点的 `x-doc` 子树里，原生 `description`/`summary` 保持未加强的英文基线零改动。**冲突**：Scalar（与 Redoc / Swagger UI 同类）是标准 OpenAPI 渲染器，只认原生字段，看不见 `x-doc`——直接喂源档，站点显示的还是未加强的英文。**问题**：怎么让渲染器看到加强文案，又不破坏「原生零改动、只增不改、不杜撰」这条贯穿全项目的红线？**答案**：写一个确定性「投影器」，按语言把 `x-doc` 投影进原生字段、剥掉 `x-doc`，产出干净标准 OpenAPI 派生档；Scalar 用官方 CDN standalone 模式零改动加载。投影本身又是一层加性、可逆、可逐字节对账的派生产物，与项目气质一致。

**主结论**：两个站点已产出并通过闸门——英文站 `ws-site/en/`、中文站 `ws-site/zh/`，各覆盖 30 份 spec，由各自的 `index.html`（Scalar 多 spec 侧边栏）统一入口。三道确定性闸门对 60 份投影档全绿，机器级坐实「无遗漏、无篡改、无杜撰、无串语言、双站结构对称」。

**支撑论点（MECE）**：
1. **路线选对了**：投影法 renderer 无关、可写闸门、确定性可复现、不碰渲染器源码；fork Scalar 会耦合其内部实现、脆弱、不可迁移（D-017）。
2. **加强真投影到位**：投影后 664 操作描述、16,876 字段描述、9 张错误表全部由 `x-doc` 搬运而来；109 条 `[⚠️批注]` 随文案一字不改进入 description（16 份 zh / 16 份 en 命中批注）。
3. **红线零破坏**：闸②双树清洗 + 字节比对证明原生骨架（paths/类型/`$ref`/required/枚举/servers）与源 `enhanced.json` 逐字节一致；投影档无任何 `x-doc` 残留。
4. **Scalar 真可用**：官方 CDN `@scalar/api-reference` v1.61.0（MIT）HTTP 200、3.6 MB standalone bundle 暴露 `createApiReference`，确认是官方支持的纯静态模式。
5. **上线有路**：提供 GitHub Pages + Actions 部署 workflow（默认不自动跑，启用交负责人），http(s) 托管天然解掉本地 `file://` 的 fetch CORS 限制。

**单一待负责人决断**：①样例档已按指示排除；②在线「Test Request」开关（servers 指向真网关 `api.aisa.one`、涉鉴权，**默认关闭**）；③是否启用 GitHub Pages 部署及用哪个域名。

## 2. 关键发现：加强在 `x-doc`，渲染器只认原生字段

阶段三的「双字段加强」是加性的——`x-doc` 子树挂在每个节点上，原生字段原封不动（这是阶段三两道闸门保下来的「原生零改动」）。Scalar 读的是 `summary` / `description` / `parameters[].description` / `schema.description`，**不读 `x-doc`**。所以「适配」的实质只有两条路：

| 路线 | 做法 | 评价 |
| --- | --- | --- |
| **A · 投影法** | Python 投影器按语言把 `x-doc` 投影进原生字段，产标准 OpenAPI，Scalar 零改动吃 | **✅ 采用**：renderer 无关、可写闸门、确定性可复现、可逆、不碰渲染器源码 |
| B · fork Scalar | 改 Scalar（JS/React）渲染逻辑去读 `x-doc` | ❌ 否决：耦合内部实现、脆弱、难写闸门、不可迁移、维护成本高 |

投影是「有则搬、无则空」，无任何兜底生成：没有 `x-doc` 的节点保留原生 `description`（有则保、无则空），严禁用原生英文顶替缺失加强文案。这把「留空、不杜撰」红线落到了本阶段。

## 3. 我们如何做的（方法 + 可信度）

**先验收输入**：跑 `python3 ws-v2/central_accept.py`，确认 31/31 双闸门全绿（ops=667 / fields=18,290 / annotations=109），源 pinned `16863d3`，确保投影输入可信。绿了才动手。

**两个工具（沿用项目「确定性 + 可复算闸门」范式）**：

1. **`project_spec.py`（投影器）**：入参 `--enhanced/--lang(en|zh)/--out`。逐节点把 `x-doc` 投影进原生字段、剥掉 `x-doc`：
   - 操作：en → `summary`=原生 summary（无 `heading_en`，回退原生；缺则留空不编）、`description`=`x-doc.desc_en`；zh → `summary`=`x-doc.heading_zh`、`description`=`x-doc.description_zh`。
   - 字段：en → `description`=`x-doc.desc_en`；zh → `description`=`x-doc.title_zh`。
   - 错误表：仅当 `x-doc.errors` 存在才渲染（zh 出「状态码 | 说明」表，en 源无英文错误文案故只列状态码、不编英文）；只有 `errors_source` 时不造表。
   - **穿透逻辑复用阶段三 `inject_xdoc.py` 的 `HTTP_METHODS` 与同款定位**（array items / oneOf|anyOf / allOf / `$ref` / 扁平点号整键），不另起炉灶。全树遍历是注入路径的超集，深层内联字段不漏投。

2. **`check_projection.py`（投影闸门 · trust-but-verify）**：
   - **闸①无遗漏·无串语言**：每个带 `x-doc.{desc_en|title_zh}` 的节点，投影后 `description` 恰等于对应语言字段（精确相等天然排除串语言）；操作 summary en 回退原生、zh 取 `heading_zh`。
   - **闸②无篡改**：双树并行清洗（剥 `x-doc` + 在 x-doc 节点排除被投影覆盖的 description/summary）后，投影档与源 `enhanced.json` 骨架逐字节一致；结构错位/越界改写都会暴露。
   - **闸③无杜撰**：所有被改写的 description/summary 必须落在带 `x-doc` 的节点上且可由其重建；错误表里每个状态码与 `message_zh` 必须能在 `x-doc.errors` 中溯源。

**可信度口径（透明即权威）**：投影器与闸门共用同一份 `render_errors` 函数（错误表格式唯一权威），闸③再对错误内容做独立 token 溯源——即便格式函数有 bug 也抓得住杜撰。原始 `enhanced.json` 永不改动，只产派生档。

## 4. 产物与闸门成绩

**站点产物**：

| 产物 | 数量 | 路径 |
| --- | --- | --- |
| 英文投影 spec | 30 | `ws-site/en/<name>.json` |
| 中文投影 spec | 30 | `ws-site/zh/<name>.json` |
| Scalar standalone 入口 | 2 | `ws-site/en/index.html`、`ws-site/zh/index.html` |
| 工具 | 3 | `project_spec.py`、`check_projection.py`、`build_index.py` |
| 部署方案（可选，未启用） | 1 | `.github/workflows/deploy-api-site.yml` |

**闸门成绩**：`check_projection.py` 对全部 60 份投影档 **exit 0（60/60 全绿）**；投影档 `x-doc` 残留为 0；均为合法标准 OpenAPI。

**投影规模（30 份，en 口径）**：操作描述 664、字段描述 16,876、错误表 9。

> 复现命令（源仓库可独立跑、确定性、零 live 依赖）：
> ```
> python3 ws-v2/central_accept.py                    # 输入验收 31/31 绿
> python3 project_spec.py --enhanced ws-v2/<n>/enhanced.json --lang en --out ws-site/en/<n>.json
> python3 check_projection.py --enhanced ws-v2/<n>/enhanced.json --lang en --projected ws-site/en/<n>.json   # exit 0
> python3 build_index.py --lang en --dir ws-site/en  # 由磁盘 *.json 派生侧边栏，不手抄
> ```

**呈现层细节**（不动 spec 内容）：7 份 twitter 分片在侧边栏统一加 "Twitter · " 前缀聚成一簇（Scalar source 下拉是扁平结构，前缀聚簇是最忠实的近似）；`openai-chat`（OpenAI 兼容网关代表接口）置顶为 default；`title="AIsa API proxy"` 的泛标题用文件名兜底，不编营销标题。

## 5. 待负责人决断项

| # | 事项 | 现状 / 建议 |
| --- | --- | --- |
| 一 | Plant Store 样例 `openapi.json` 去留 | **已按负责人要求纳入**（D-018，撤回 D-017 的排除）：站点现覆盖 31/31 份 spec。补档走同款管线，闸门 en/zh 均 exit 0。 |
| 二 | 在线 "Test Request" 开关 | **默认关闭**（`hideTestRequestButton:true`，连带隐藏鉴权面板）。servers 指向真网关 `api.aisa.one`、涉鉴权，静态档内零密钥。开启与否交决断。 |
| 三 | 上线部署方式 | **建议 GitHub Pages**：已写 `deploy-api-site.yml`（手动触发或推 `ws-site/**` 才跑，默认不自动）。启用步骤见 workflow 顶部注释；http(s) 托管解掉 `file://` 的 fetch CORS。域名形如 `https://<owner>.github.io/<repo>/{en,zh}/`。 |

## 6. 边界与透明交代

**Scalar 可用性已验证**（回应「保留是否真正可用」）：官方 CDN `@scalar/api-reference@latest/dist/browser/standalone.js` 返回 HTTP 200、3,639,831 bytes，bundle 头标 `@scalar/api-reference 1.61.0 ... License: MIT`，暴露全局 `Scalar.createApiReference`。确系官方支持的纯静态 CDN 模式（spec 用相对 URL `./x.json` 拉取），可用，保留。

**浏览器可视化截图核对未能在沙箱内完成（如实交代）**：本阶段计划用浏览器开 `file://` 截图核对呈现，但沙箱环境三重受限——①本地浏览器 harness 拒绝 file:// 访问（"Cannot navigate to a file URL without local file access"）；②远程浏览器拒绝 file:// / data: / 内部 URL；③即便能开 file://，Scalar 的相对 `fetch('./x.json')` 在 `file://` 下受浏览器 CORS 拦截（这正是上线到 GitHub Pages 后由 http(s) 托管解决的问题）。

**为什么这不影响交付可信度**：站点的**实质正确性**——无遗漏、无篡改、无杜撰、无串语言、双站结构对称——已由 `check_projection.py` 对 60 份投影档**逐字节对账证明**（闸②双树字节比对、闸①③精确相等 + token 溯源），不依赖肉眼。未能验证的仅是 Scalar 把这些标准 spec **画成什么样的视觉呈现**，而 Scalar 是官方维护的成熟渲染器、吃的是合法标准 OpenAPI，渲染风险低。建议负责人在启用 GitHub Pages 后做一次线上目视终验。

## 7. 自查（对齐 REPORT-CONTRACT 验收清单）

- 结论先行、SCQA 开场、章节标题为结论句；发现均答「so what」并落到决断项。
- 路线选型有据（D-017），主动交代边界（截图未做的原因 + 为何不影响可信度）。
- 复现命令源仓库可独立跑、确定性、零 live 依赖；闸门 exit 0 可一键复跑。
- 不提 PR、PAT 永不明文、占位符逐字节保留；原生 `enhanced.json` 零改动。
