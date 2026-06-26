# AIsa 文档质量工程

AIsa 是一个 OpenAI 兼容的 AI 能力网关(法律实体 AIPay, Inc.),文档同时面向人和 Agent。本仓库把「防止文档腐烂、并主动提升文档质量」从一次性人工劳动,做成一套可分阶段实施、可独立验收、证据确凿的文档质量工程。

> 唯一受众是 AIsa 产品负责人,唯一标准是真实、可复现、可交付。早期求职作品集阶段的产物已归档至 [`archive/`](./archive/)。

---

## 一、项目从哪来:一条完整脉络

项目起点是对 AIsa 文档一无所知。整个推进按「先看清、再分流、各个击破、最后呈现」展开:

**① 看清文档怎么生产的。** 先摸清 AIsa 文档的生产模式——源仓库 `AIsa-team/docs`(`.mdx` 散文 + `openapi/*.json` + 整合脚本)经部署层渲染成线上 `aisa.one`,给人看 HTML、给 Agent 看 `.md` 孪生页与发现契约。把 GitHub 源与线上渲染两份内容都抓到本地(`docs-mirror/` 全量镜像),逐一比对,推断出完整生产链路,并从源码核实全部基线事实(见 [`project/CHARTER.md`](./project/CHARTER.md) 第二节、[`project/baselines/FACTS.zh-CN.md`](./project/baselines/FACTS.zh-CN.md))。

**② 按现状分流。** 现状统计落地了一个关键事实:743 页 `.mdx` 里,**664 页是 API 参考桩页**(frontmatter 指向 spec,正文由渲染层从 OpenAPI 内联生成,非手写),真正可做散文质检的只有 **73 页人写散文**(`guides/` 30 + `agent-skills/` 43)。两类对象状态与风格迥异,于是分两条线做不同的事:

- **手写散文 → 质检**(尤其 AI 友好度):它们是人写的,问题在表达与一致性。
- **API 文档 → 内容加强 + 翻译 + 上线**:它们是 spec 驱动的,问题在描述贫瘠、无中文、线上呈现不出加强。

**③ 各阶段各有沉淀。** 五个阶段每个都有独立验收产物与复现命令,详见下文「高价值产物」。

**④ 最后呈现与交付。** 加强后的 API 以双语 Scalar 站点上线,质检结论汇总成对外报告。

```
AIsa-team/docs          源仓库:.mdx 散文 + openapi/*.json
      │  渲染/部署
      ▼
https://aisa.one        线上:HTML 给人,.md 孪生页 + 发现契约给 Agent
      │  本地抓取比对
      ▼
docs-mirror/  +  ~/files/aisa-team-docs(源仓库副本,pinned 16863d3)
      │  现状统计 → 分流
      ├── 73 页人写散文 ──→ 阶段一硬伤质检 + 阶段二 AI 友好度质检
      └── 664 桩页 / 31 spec ──→ 阶段三内容加强 ──→ 阶段五双语站点上线
```

---

## 二、最终沉淀的高价值产物(及如何消费)

这是项目的核心交付。按「质检 / API 加强 / 反馈 / 方法」四块组织。

### 1. 质检结果与洞察(手写文档)

| 产物 | 是什么 | 怎么消费 |
| --- | --- | --- |
| [`reports/hard-defects-2026-06-26.md`](./reports/hard-defects-2026-06-26.md) | 阶段一硬伤质检:3 项 BLOCKER,均集中在 `guides/agent-discovery.mdx`,全部仅凭 `openapi.yaml` 可证伪(schema 121→321、分类 10→14、分类表漏列 4 项) | 直接给研发改;`.json` 同源可进 CI |
| [`reports/ai-friendly-prose-readable-2026-06-26.md`](./reports/ai-friendly-prose-readable-2026-06-26.md) | 阶段二全量 73 页 AI 友好度质检的**可读版**(《从一个连字符看 Agent 的文档体验》),20 条硬缺口 | 给产品负责人通读;要查证看技术版 |
| [`reports/ai-friendly-prose-2026-06-26.md`](./reports/ai-friendly-prose-2026-06-26.md) | 同上**技术版**:含规范点号、置信度、逐条对账台账 | 逐条核实/复现 |
| [`reports/content-audit-2026-06-26.md`](./reports/content-audit-2026-06-26.md) | 报告甲:阶段一+二合并的对外内容审计稿 | 对外交付主稿 |

**核心洞察**:73 页 20 条缺口收口到一个根因——`agent-skills` 这 43 页缺一个被全站引用的权威事实源,模型价、上下文窗口、家族计数、API 端点全是各页作者各自手抄的离群快照,没人引用 `guides/` 那套内部自洽的权威目录。修法一句话:建立单一引用,删除离群快照。

### 2. 双语 API 参考站点(改造后部署)

| 站点 | 内容 | 入口 |
| --- | --- | --- |
| 英文站(改造后部署) | 30 份 AIsa spec 的**加强英文**描述,Scalar 渲染 | `ws-site/en/index.html` → 线上 `/en/` |
| 中文站(翻译后部署) | 同 30 份的**中文本地化**描述 | `ws-site/zh/index.html` → 线上 `/zh/` |

线上地址(GitHub Pages,已部署):

- 英文:https://yuanshan8053.github.io/aisa-docs-voyager/en/
- 中文:https://yuanshan8053.github.io/aisa-docs-voyager/zh/

**怎么来的**:加强成果以加性 `x-doc` 挂在 spec 上(原生零改动),`project_spec.py` 按语言把 `x-doc` 投影进原生 `summary`/`description`、剥掉 `x-doc`,产出干净标准 OpenAPI 派生档,Scalar 官方 CDN standalone 零改动加载。`check_projection.py` 三闸(无遗漏 / 无篡改·逐字节比对 / 无杜撰·无串语言)对 60 份投影档 exit 0。详见 [`reports/scalar-api-site-2026-06-26.md`](./reports/scalar-api-site-2026-06-26.md)。

### 3. API 文档批注反馈问题(交研发确认)

| 产物 | 是什么 | 怎么消费 |
| --- | --- | --- |
| [`reports/annotations-for-dev-2026-06-26.md`](./reports/annotations-for-dev-2026-06-26.md) / [`.csv`](./reports/annotations-for-dev-2026-06-26.csv) | **109 条**源 spec 未声明、加强时拒绝杜撰而显式留痕的硬事实缺口(哈希算法取值、内部标志含义、单位上限等),集中在 `openapi-financial`(30) / `dataforseo`(22) / `apollo`(20) | 研发逐条补全权威说明 → 去批注、升级为确定描述 |

每条含:spec / 接口 / 位置(参数·请求·返回) / 字段 / 类型 / 原描述 en / 改后描述 en / 批注。CSV 用 Excel 直接打开。一键复现:`python3 ws-v2/extract_annotations.py`。

### 4. API 文档专业写作实践(可复用方法)

| 产物 | 是什么 | 怎么消费 |
| --- | --- | --- |
| [`reports/api-writing-patterns-2026-06-26.md`](./reports/api-writing-patterns-2026-06-26.md) | 从 17,550 对改前改后实例提炼的 **9 个写作模式**(从无到有 / 标签扩写 / 补默认行为 / 补用途下游 / 枚举写业务含义 / 接口定位 / 跨字段关系 / 自适应深度 / 不确定留批注),每模式 ≥2 真实案例 + rationale | 写或评审 API 文档时当判断标准 |
| [`reports/ai-friendly-method.zh-CN.md`](./reports/ai-friendly-method.zh-CN.md) | AI 友好度质检方法论 | 复用到其他文档质检 |

---

## 三、加强工程的规模(静态可证)

| 指标 | 数值 | 复现 |
| --- | --- | --- |
| 加强的 spec | 31 | `ls -d ws-v2/*/` 含 `content.json` 者 |
| 加强的 operation | 667 | `python3 ws-v2/central_accept.py` |
| 加强的对外字段/参数 | 18,290 | 同上 |
| 主动批注(待研发确认) | 109 | 同上 / `python3 ws-v2/extract_annotations.py` |
| 双闸门验收 | 31/31 exit 0 | `python3 ws-v2/central_accept.py` |
| 站点投影闸门 | 60/60 exit 0 | `python3 check_projection.py …`(见下) |

**双字段模型**:每个对外字段齐备「加强英文 `desc_en` + 中文本地化 `title_zh`」;operation 级齐备 `heading_zh` + `description_zh` + `desc_en`。原生 `description`/`summary` 只读、零改动,三态可对账。

---

## 四、仓库导航

| 你想知道 | 看这里 |
| --- | --- |
| 项目是什么、四条工作线、硬约束 | [`project/CHARTER.md`](./project/CHARTER.md) |
| 现在进展到哪、下一步 | [`project/STATE.md`](./project/STATE.md) |
| 做过哪些决策、为什么 | [`project/DECISIONS.md`](./project/DECISIONS.md) |
| 已核实的基线事实 + 复现命令 | [`project/baselines/FACTS.zh-CN.md`](./project/baselines/FACTS.zh-CN.md) |
| **全部文件分了哪些类、能不能动** | [`project/ASSETS.zh-CN.md`](./project/ASSETS.zh-CN.md) |
| 各阶段怎么干(含委派提示词) | [`planning/`](./planning/) |
| 对外报告契约 | [`project/REPORT-CONTRACT.zh-CN.md`](./project/REPORT-CONTRACT.zh-CN.md) |
| 写作规范 | [`WRITING-STANDARD.zh-CN.md`](./WRITING-STANDARD.zh-CN.md) |

**五个阶段**:① 硬伤质检(`checks/src_consistency.py`)→ ② AI 友好度质检(73 页)→ ③ OpenAPI 内容加强(31 spec 双字段)→ ④ 报告汇总 → ⑤ 双语 API 站点呈现。

---

## 五、复现关键产物

```bash
# 阶段三:全量验收(31 spec 双闸门)
python3 ws-v2/central_accept.py                    # exit 0 = 31/31 全绿

# 批注清单(109 条)
python3 ws-v2/extract_annotations.py               # → reports/annotations-for-dev-*.{md,csv}

# 写作实践素材(17,550 对改前改后)
python3 ws-v2/dump_pairs.py                         # → /tmp/pairs.jsonl
python3 ws-v2/find_examples.py                      # 按模式分桶

# 阶段五:投影 + 闸门 + 站点入口(单 spec 示例)
python3 project_spec.py --enhanced ws-v2/openai-chat/enhanced.json --lang en --out ws-site/en/openai-chat.json
python3 check_projection.py --enhanced ws-v2/openai-chat/enhanced.json --lang en --projected ws-site/en/openai-chat.json  # exit 0
python3 build_index.py --lang en --dir ws-site/en  # 重建侧边栏入口
```

> 复现前提:源仓库副本在 `~/files/aisa-team-docs`(pinned `16863d3`)。根目录三个工具 `project_spec.py` / `check_projection.py` / `build_index.py` 与 `ws-v2/*.py` 被决策日志和报告以原路径钉死复现命令,**不要移动**(详见 [`project/ASSETS.zh-CN.md`](./project/ASSETS.zh-CN.md) 第七节)。

---

## License

[MIT](./LICENSE)
