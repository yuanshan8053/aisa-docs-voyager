# 当前状态

> 每次 session 结束前必更。记录：项目处于哪个阶段、已完成什么、阻塞是什么、下一步是什么。

**最后更新**：2026-06-26
**当前阶段**：阶段零（重定位与规划）已完成，阶段一（硬伤质检）就绪待启动。

---

## 已完成

- [x] 查清文档生产链路（源仓库 → 部署层 → 线上），见 `CHARTER.md` 第二节。
- [x] 从源码核实全部基线事实（743 页 / 664 桩页 / 73 散文页 / 31→30 spec / 11 中文页），见 `baselines/FACTS.zh-CN.md`。
- [x] 确证 3 条硬伤：发现契约不对称、技能计数漂移（13 vs 43）、中文覆盖率 ~1.5%。
- [x] 项目重定位、旧资产归档至 `archive/`。
- [x] 建立权威信息源层 `project/`（CHARTER / STATE / DECISIONS / baselines）。
- [x] 产出三阶段实施计划，每阶段含自包含提示词。

## 进行中

- 无（等待委派阶段一）。

## 阻塞

- 无。

## 下一步

1. **启动阶段一**：把 `planning/PHASE-1-hard-defects.zh-CN.md` 的自包含提示词委派给一个新 session agent，产出 `checks/src_consistency.py` 静态检查器 + 首份硬伤报告。
2. 阶段一验收通过后，并行委派阶段二、阶段三（二者相互独立，依赖不同技能）。

## 给接手 agent 的提醒

- 先读 `CHARTER.md` → 本文件 → `DECISIONS.md`。
- 干活前确认输入源仓库 `~/files/aisa-team-docs` 仍在；不在则用项目指令中的 PAT 重新克隆 `AIsa-team/docs`（PAT 永不明文打印）。
- 完成后回写本文件 + `DECISIONS.md` + `baselines/FACTS.zh-CN.md`。
