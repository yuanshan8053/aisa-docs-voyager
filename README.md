# AIsa 文档质量工程

AIsa 是一个 OpenAI 兼容的 AI 能力网关（法律实体 AIPay, Inc.），文档同时面向人和 Agent。本仓库是 AIsa 文档质量工程的工作区：把「防止文档腐烂、并主动提升文档质量」做成一套可分阶段实施、可独立验收、证据确凿的工程。

> 唯一受众是 AIsa 产品负责人，唯一标准是真实、可复现、可交付。早期求职作品集阶段的产物已归档至 [`archive/`](./archive/)。

## 从哪读起

| 你想知道 | 看这里 |
| --- | --- |
| 项目是什么、四条工作线、硬约束 | [`project/CHARTER.md`](./project/CHARTER.md) |
| 现在进展到哪、下一步是什么 | [`project/STATE.md`](./project/STATE.md) |
| 做过哪些决策、为什么 | [`project/DECISIONS.md`](./project/DECISIONS.md) |
| 已核实的基线事实 + 复现命令 | [`project/baselines/FACTS.zh-CN.md`](./project/baselines/FACTS.zh-CN.md) |
| 各阶段怎么干（含委派提示词） | [`planning/`](./planning/) |
| 写作规范 | [`WRITING-STANDARD.zh-CN.md`](./WRITING-STANDARD.zh-CN.md) |

## 四条工作线

| 编号 | 工作线 | 目标 | 阶段 |
| --- | --- | --- | --- |
| ① | 硬伤质检 | 静态源码一致性检查器，零依赖零误报 | [阶段一](./planning/PHASE-1-hard-defects.zh-CN.md) |
| ② | AI-friendly 质检 | 对 73 页可读散文做 AI 友好度系统质检 | [阶段二](./planning/PHASE-2-ai-friendly.zh-CN.md) |
| ③ | OpenAPI 内容加强 | 独立增强参考页 + 回写原 spec | [阶段三](./planning/PHASE-3-openapi-enhance.zh-CN.md) |
| ④ | ~~直出 md~~ | 已折叠进 ③（线上参考页本就是 spec 内联） | 已关闭 |

## 跨 session 协作

本项目分阶段、跨 session 实施。任何接手的 agent：先读 `project/CHARTER.md` → `STATE.md` → `DECISIONS.md`，再打开对应 `planning/PHASE-N-*.zh-CN.md`（内含自包含委派提示词、输入边界、验收产物），干完回写三件套。详见 CHARTER 第六节。

## 现存工具

- `checks/`（阶段一交付）：静态源码一致性检查器。
- `aisa_doc_auditor/`：早期 live-probe 审计器，现降级为旁证工具（live 探测不单独定罪）。
- `tools/docs_mirror.py` + `docs-mirror/`：全量文档镜像工具与快照。

## License

[MIT](./LICENSE)
