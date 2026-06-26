# AIsa Docs Voyager 🧭

> **Foresight** — 在人类发现之前,先看见文档与现实的漂移。

[![Doc Reality Check](https://github.com/yuanshan8053/aisa-docs-voyager/actions/workflows/doc-reality-check.yml/badge.svg)](https://github.com/yuanshan8053/aisa-docs-voyager/actions/workflows/doc-reality-check.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

一个用于 AIsa 开发者文档的**漂移检测 Agent**,以及让它在文档开发系统中自动运转所需的全部配套。

它要证明的不是「会写文档」,而是「能把文档变成由 AI Agent 自动维护的系统」——这正是一名 Developer Advocate / 文档负责人应当解决的系统层面问题。完整思路见 [`STRATEGY.zh-CN.md`](./STRATEGY.zh-CN.md)。

## 为什么需要它

AIsa 的文档同时是给人看的、也是给 Agent 读的契约(`llms.txt` / `agent-card.json` / `ai-plugin.json` / `mcp.json`),且大部分由线上网关自动生成。这必然产生一类反复发生的故障:**prose 文档与 live 契约会悄悄漂移**,相信文档的 Agent 就会拿到坏指令。Voyager 把"防止文档腐烂"从一次性人工劳动,变成持续自动的机制。

## 目录结构

```
aisa-docs-voyager/
├── STRATEGY.zh-CN.md                  # 策略简报:缺口、证据、方案、岗位映射
├── WRITING-STANDARD.zh-CN.md          # 长期生效的写作规范
├── planning/
│   └── ROADMAP.zh-CN.md               # 工作规划:三步走、四条工作线、里程碑
├── aisa_doc_auditor/
│   ├── __init__.py
│   └── auditor.py                     # 核心:实时抓取线上源、检测漂移
├── tools/
│   └── docs_mirror.py                 # 全量文档镜像:把整个文档面拉到本地
├── .github/workflows/
│   └── doc-reality-check.yml          # 把审计 Agent 嵌入 PR + 定时 CI
├── localized/
│   └── quickstart.zh-CN.md            # 补齐的最高价值资产:中文快速开始
├── reports/
│   ├── sample-audit.json              # 示例审计结果(机器可读)
│   └── sample-audit.md                # 示例审计结果(人类可读)
├── pyproject.toml
└── LICENSE
```

## 快速运行(无需 API Key)

```bash
# 人类可读报告
python -m aisa_doc_auditor.auditor

# 同时产出 JSON + Markdown
python -m aisa_doc_auditor.auditor --json reports/audit.json --md reports/audit.md

# CI 模式:发现阻断项即退出码 1
python -m aisa_doc_auditor.auditor --ci
```

安装后也可用入口命令 `aisa-docs-voyager`(见 `pyproject.toml`)。审计对象全部是 AIsa 的公开资源,任何人都能复现下面的结论。

## 把全部文档拉到本地

如果你无法直接访问 AIsa 站点,`tools/docs_mirror.py` 能把整个文档面拉成本地镜像——不止 `llms.txt` 索引,而是把它指向的每一页 `.md` 正文与每个 OpenAPI spec 都抓下来,按 URL 路径还原成目录树,并写一份记录每个文件 SHA-256 与抓取时间的 `manifest.json`。

```bash
# 全量拉取到 ./docs-mirror
python tools/docs_mirror.py

# 只重抓内容有变化的页面
python tools/docs_mirror.py --incremental

# 打印与上次相比新增/删除/变更了哪些页
python tools/docs_mirror.py --incremental --diff

# 额外存一份人类页面的原始 HTML 外壳
python tools/docs_mirror.py --keep-html
```

> 关于人类页面:`/docs/<path>` 的 HTML 是 Next.js 应用,正文被序列化进 RSC 负载里,需 JS 渲染才能干净提取;每页的 `.md` 孪生版以无损形式承载同样内容,所以镜像默认抓 `.md` 集合,`--keep-html` 仅用于归档原始外壳。

## 它检测什么

1. **失效的发现端点** —— 文档/manifest 让 Agent 去 fetch、实际却取不到的 URL(例:`/openapi.yaml` 返回 404)。
2. **计数漂移** —— 指南里手写的数字 vs 线上真实数量(例:指南「13 skills」vs 线上 `agent-card.json` 45 个)。
3. **本地化覆盖率** —— 中文文档在全部页面中的占比(当前 1.3%)。
4. **时效性** —— 指南 "last refreshed" 时间戳的陈旧程度。

## 示例审计结论(2026-06-26)

| 严重度 | 检查 | 结论 |
| --- | --- | --- |
| 🔴 | `discovery_endpoint` | `/openapi.yaml` 返回 404,但 `ai-plugin.json` 与指南都让 Agent 去取它 |
| 🔴 | `count_drift_skills` | 指南写 13 skills,线上 agent card 广播 45 |
| 🔴 | `localization_zh` | 中文覆盖率 1.3%(773 页中仅 10 页) |
| 🟡 | `count_drift_paths` | 指南承诺聚合 spec,线上是 30 个分散文件且聚合文件不存在 |

> 这些不是快照——每次运行都会对着线上重新判定。文档修好后审计自动转绿;上游再引入新漂移,审计自动抓到。

## License

[MIT](./LICENSE)
