# 静态源码一致性检查器

`src_consistency.py` 仅凭 `AIsa-team/docs` 源仓库文件判定确凿的文档硬伤,不发任何 live 网络请求,对同一仓库多次运行结果稳定。**零误报是红线**:凡标为 BLOCKER 的结论,都能被人工仅凭源仓库文件复核证伪。

## 用法

```bash
python3 checks/src_consistency.py --repo ~/files/aisa-team-docs            # 同时输出 md + json
python3 checks/src_consistency.py --repo <path> --format md               # 仅 markdown
python3 checks/src_consistency.py --repo <path> --out-json r.json --out-md r.md
python3 checks/src_consistency.py --repo <path> --ci                       # 有 BLOCKER 则退出码 1
```

依赖 PyYAML(源仓库自带的 `consolidate_openapi.py` 同样依赖)。

## 真值从哪来

| 真值 | 来源 | 取法 |
| --- | --- | --- |
| spec 路径 / 操作 / schema / 分类数 | 已提交的 `openapi.yaml` | `yaml.safe_load` 后直接计数 |
| 承载操作的分类(tag) | `openapi.yaml` | 遍历 paths 下各操作的 `tags`,只计真正出现的 tag |
| agent-skills 页数、总 mdx、中文页 | 目录扫描 | `os.walk`,裁剪隐藏目录 |

选 `openapi.yaml` 而非现跑 `consolidate_openapi.py`,是因为它是仓库已提交、线上参考正文内联渲染所依据的同一份产物——文档描述的就是它,拿它比对无歧义,且不引入脚本执行的不确定性。

## 三条规则与判定逻辑

### 规则 1 · spec 形态断言一致性(`rule_spec_stat_claims`)

扫描 `guides/*.mdx`,抽取关于 spec 的可量化断言(schema 数、路径/端点数、分类数),与 `openapi.yaml` 真值比对。

- **只在「整份 spec」语境下定罪**:行内须命中全量 spec 标记(`openapi.yaml`、`consolidated OpenAPI`、`OpenAPI spec`、`the spec`、`machine-readable specification/contract`)才参与比对。否则可能是某个子服务的局部计数,跳过。
- **精确数字**(无 `+`)与真值不等 → BLOCKER。
- **限定数字**(`N+`)且真值 ≥ 2N → INFO(陈旧低估,字面仍为真)。

为何零误报:精确数字 `121 schemas` 写在描述 `openapi.yaml` 的同一行,而 spec 实有 321,二者直接矛盾,人工 `grep` + 一行 python 即可复核。`changelog.mdx` 的「CoinGecko API (23 Endpoints)」因行内无全量 spec 标记被排除——它指单个集成(coingecko.json 实有 21 路径),不是对全量 spec 的断言。这正是早期一版检查器的误报点,已用「全量 spec 标记」闸门堵死。

### 规则 2 · API 分类表完整性(`rule_category_table_coverage`)

定位 `agent-discovery.mdx` 的「### API Categories」表,抽取第一列分类名,与 spec 中真正承载操作的 tag 集合比对。表自称「spec 把端点组织为以下分类组」却遗漏了承载真实操作的分类 → BLOCKER。

- 名称做空白归一化比较(spec 用 `Twitter / X`,散文用 `Twitter/X`)。
- **只把「承载操作的 tag」算作分类**:空 tag 不会被当成遗漏,杜绝把无操作的声明性 tag 误判为缺口。
- 报告附每个遗漏分类的操作数,佐证它确实存在。

### 规则 3 · 本地化覆盖率(`rule_localization_coverage`)

统计文件名含 `zh`/`chinese`/`cn` 的页占比。这是内容缺口而非源码可证伪的「错误」,**恒为 INFO**,绝不阻断。

## 严重度铁律

- **BLOCKER**:能仅凭源仓库文件证伪的不一致。每条带 `file`、`line`、`reproduce`。
- **INFO**:统计性事实、内容缺口、带 `+` 的陈旧低估。

凡无法仅凭源码定罪的项,绝不标 BLOCKER。检查器宁可漏报,不可误报。

## 零误报自检记录(2026-06-26)

逐条手工复核首轮全部 BLOCKER:

- **B1** `agent-discovery.mdx:16` 写 `121 schemas`;`openapi.yaml` 实有 321。`sed -n '16p'` + 一行 python 复核,矛盾成立。
- **B2** `agent-discovery.mdx:127` 写 `10 categories`;承载操作的 tag 实有 14。复核成立。
- **B3** 该页「API Categories」表列 10 类,遗漏 Agent Email(46)、Reddit(5)、SEO & Search Data(445)、Sales Intelligence(54)——四者均承载真实操作,复核成立。

复核中剔除两类潜在误报:

- `changelog.mdx` 的 `23 Endpoints` 是 CoinGecko 局部计数(非全量 spec),已被规则 1 的全量标记闸门排除。
- 前序基线的「13 vs 43 skills」:agent card 的 13 个广播 skill 与 `agent-skills/` 的 43 个可安装技能页是不同概念,且文档「13」与其自身 13 行表内部自洽,无法仅凭源码证伪,不列入(见 `project/DECISIONS.md` D-006)。
