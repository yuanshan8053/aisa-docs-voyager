# AIsa 文档硬伤报告

> 生成日期：2026-06-26　·　检查器：`checks/src_consistency.py`
> 源仓库：`AIsa-team/docs`（工作副本 `~/files/aisa-team-docs`，HEAD `16863d3`）
> 判定方式：纯静态，仅凭源仓库文件，零 live 请求。每条均可独立复现。

## 一、结论先行

本轮检出 **3 项阻断硬伤（BLOCKER）**，全部集中在面向 Agent 的核心文档 `guides/agent-discovery.mdx`：它对外宣称的 OpenAPI spec 形态，与仓库实际产出的 `openapi.yaml` 对不上。Agent 正是靠这页决定「AIsa 能干什么、怎么调」，所以这页失真，等于发现入口给出了错误的能力地图。

一句话定性：**文档把一份 645 路径、321 schema、14 个分类的 spec，描述成了 121 schema、10 个分类的样子，并漏列了 4 个真实存在的能力分类——其中一个多达 445 个操作。**

另有 2 项提示（INFO）：路径数严重低估（写 `111+`，实为 645，字面不算错但显著陈旧）、中文覆盖率仅 1.5%（11/743）。这两项是内容缺口与陈旧,不是源码可证伪的「错误」,不阻断。

## 二、归因拆解：三项硬伤都指向同一个根因

| 编号 | 位置 | 文档写 | 真值 | 性质 |
| --- | --- | --- | --- | --- |
| B1 | `agent-discovery.mdx:16` | 121 schemas | 321 | 精确数字与产物矛盾 |
| B2 | `agent-discovery.mdx:127` | 10 categories | 14 | 精确数字与产物矛盾 |
| B3 | `agent-discovery.mdx:163` | 表列 10 类 | 实有 14 类 | 分类表漏列 4 项 |

三者不是三处独立笔误,而是**同一个根因的三个切面**:这页关于 spec 形态的描述是某次手写后固化的快照,而 `openapi/*.json` 与 `scripts/consolidate_openapi.py` 持续演进,文档没有跟着 spec 走。schema 从 121 长到 321、分类从 10 长到 14,文档原地不动,于是数字与表格同时失真。

根因明确,动作就明确:**让这些数字与表格由 `openapi.yaml` 自动派生,而非手写**。否则下次 spec 再长,同样的漂移会再次发生。

## 三、单点下钻:被漏掉的不是边角,是主力

最值得放大的是 B3。文档的「API Categories」表自称「spec 把端点组织为以下分类组」,却只列了 10 个,漏掉 4 个——而这 4 个不是空壳,全都承载真实操作:

| 漏列分类 | 承载操作数 |
| --- | --- |
| SEO & Search Data | 445 |
| Sales Intelligence | 54 |
| Agent Email | 46 |
| Reddit | 5 |

`SEO & Search Data` 一个分类就有 445 个操作,占全 spec 663 个操作的三分之二,却在面向 Agent 的能力总览里完全隐身。换句话说,一个只读这页发现文档的 Agent,会以为 AIsa 提供 10 类能力、最大的那块业务对它不存在。这不是「数字过期」的小瑕疵,而是**核心能力的发现性缺失**——离「Agent 找不到、用不上」最近的一类问题。

## 四、复现命令

在源仓库根目录执行,即可独立验证上述三条:

```bash
# B1 · schema 数
python3 -c "import yaml;d=yaml.safe_load(open('openapi.yaml'));print(len(d['components']['schemas']))"   # → 321

# B2 / B3 · 承载操作的分类数与名称
python3 -c "import yaml;d=yaml.safe_load(open('openapi.yaml'));t=set();[t.add(x) for p in d['paths'].values() for m,o in p.items() if m in ('get','post','put','patch','delete') and isinstance(o,dict) for x in o.get('tags',[])];print(len(t));print(sorted(t))"   # → 14

# 文档侧断言
grep -nE '121 schemas|10 categories' guides/agent-discovery.mdx
```

## 五、口径与边界（为什么零误报）

- **真值取自已提交的 `openapi.yaml`**,即线上 API 参考正文内联渲染所依据的同一份产物;文档对它的描述与它本身比对,无歧义。
- **只对「整份 spec」语境的数字定罪**。例如 `changelog.mdx` 的「CoinGecko API (23 Endpoints)」是单个集成的局部计数(coingecko.json 实有 21 路径),不是对全量 spec 的断言,检查器据此排除,不误报。
- **带 `+` 的限定数字(`111+ paths`、`100+ endpoints`)字面为真**(645 ≥ 111),仅作 INFO 标注陈旧,不计入 BLOCKER。
- **前序基线中的「13 vs 43 skills」经复核不成立,本轮不列入**:A2A agent card 广播的 13 个 skill 与 `agent-skills/` 目录下 43 个可安装技能页是两个不同概念,文档正文的「13」与其自身 13 行技能表内部自洽,无法仅凭源码证伪,故剔除。详见决策 D-006。
