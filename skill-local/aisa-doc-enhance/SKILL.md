# aisa-doc-enhance — AIsa OpenAPI 双字段加强（本地改造版，standalone）

> 本技能是 `api-doc-agent` 的**本地瘦身改造版**，专为 AIsa 文档质量工程阶段三定制。
> 派遣的 agent **只读本目录**，不读 `/data/plugins/.../api-doc-agent`，不依赖 spectral / 渲染器 / doc_engine 等任何包外引擎。

## 这版相比原 skill 改了什么（为什么改）

原 `api-doc-agent` 是「确定性三引擎流水线（Spec Engine → doc_engine 装配 → Renderer）+ spectral 三道闸门」的重型链路。阶段三试点暴露两个问题：
1. **看不清改了什么**：交付物是渲染后的 md，而 `direct`（火山）渲染器按 `Action`/`Version` 信封模板生成，**不渲染** AIsa 真实 REST 参数，加强价值在最终产物里隐形 → 无法判断「改好还是改坏」。
2. **链路过重**：spectral / 渲染器 / 引擎一整套，对「只想把 spec 写好」这个目标是冗余的。

本版按新策略**只吸收 doc 内核（一句写作方法论），由 LLM 推理逐字段加强**：

- **写作内核蒸馏成一份** `METHODOLOGY.md`（去平台化、去引擎化）。
- **交付从「双字段」立意**：每个字段产**加强英文 `desc_en`** +**中文本地化 `title_zh`**，与原生源英文 `description` 三栏并存、可逐字段对账。
- **新增 `make_review.py` 三栏对照表**：源英文 → 加强英文 → 中文，一眼看清每个字段改了什么、改好还是改坏（直接解决痛点 1）。它同时是**完整性闸门**，缺字段即非零退出，杜绝偷懒漏写。
- **工具全部 standalone**（纯 python3 标准库），不 import 任何包外引擎。
- **不渲染、不跑 spectral、不 hoist、不碰原生结构**——只做加性注入 + 关系型保全校验 + 对照表。

## 铁律（不可违背）

1. **写作是 LLM 的智力工作，不可外包给脚本。** 逐接口、逐字段亲自按 `METHODOLOGY.md` 撰写 `content.json`。**严禁写脚本批量套模板生成 `desc_en`/`title_zh`**——机械直译等于没写，是本技能最忌讳的偷懒。
2. **只增不改。** 只新增 `x-doc`，绝不删改任何 OpenAPI 原生结构（paths/method/type/enum/required/$ref/items/`description`）。`check_native_preserved.py` 把关（exit 0）。
3. **不复制原生元数据进 `x-doc`**（字段名/必选/类型/枚举字面量/范围/默认）。
4. **不捏造**：拿不准的硬事实转 `annotation`，注入器自动转 `[⚠️批注]`/`[⚠️Note]`。
5. **双字段语义一致**：`desc_en` 与 `title_zh` 必须说同一件事。
6. **源保护**：节点已有 `source∈{human,ai-reviewed}` 且内容不同 → 注入器不覆盖、记 review。
7. **安全**：PAT 仅从环境/参数读、永不明文打印；不直连 LLM Gateway；不在沙箱启网络监听；占位符 `[ph_..._ph]` 逐字节保留。

## 工作流（每个 spec 一遍）

```bash
cd <本技能目录>/tools

# 1.（智力工作）按 ../METHODOLOGY.md 逐字段撰写 content.json。
#    格式见 inject_xdoc.py 顶部 docstring：operations{} + fields{}（dotpath 寻址）。

# 2. 加性注入：把双字段 content 注入 spec 的 x-doc（standalone，不依赖引擎）
python3 inject_xdoc.py --spec <源spec.json> --content content.json \
  --out enhanced.json --review-out inject_review.json --doc-version 2.0.0

# 3. 原生保全闸门（必须 exit 0）
python3 check_native_preserved.py <源spec.json> enhanced.json

# 4. 三栏对照表 + 完整性闸门（必须 exit 0，缺字段即 1）
python3 make_review.py --spec enhanced.json --out review_table --require both
#    产物 review_table.md = 人读「改了什么」对照表；review_table.json = 机读统计
```

## 交付产物（每个 spec）

| 产物 | 说明 |
|---|---|
| `content.json` | LLM 逐字段撰写的双字段增强内容（本阶段之魂） |
| `enhanced.json` | 含 `x-doc` 的增强 spec，原生零改动 |
| `review_table.md` | 三栏对照表：源英文 → 加强英文 → 中文，逐字段判好坏 |
| `inject_review.json` | 注入审计：源保护跳过 / dotpath 未命中等 |

## tools/ 清单

- `inject_xdoc.py` — 双字段 x-doc 加性注入器（standalone）。dotpath 寻址，自动穿透 array items 与 `$ref`；源保护红线。
- `check_native_preserved.py` — 原生结构保全关系型 diff 闸门。
- `make_review.py` — 三栏对照表生成 + 对外字段完整性闸门。
