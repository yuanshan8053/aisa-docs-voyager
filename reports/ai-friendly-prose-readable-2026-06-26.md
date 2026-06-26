# 从一个连字符看 Agent 的文档体验

> 走查对象：AIsa 官方文档中 73 页人工撰写的说明文（30 页平台指南 + 43 页技能手册）
> 源仓库：`github.com/AIsa-team/docs`，定位锚定提交 `16863d3`　·　线上：`aisa.one/docs`
> 配套技术版：`ai-friendly-prose-2026-06-26.md`（含规范点号、置信度、对账台账）

## 一、一次按文档调用的失败旅程

设想一个 AI 助手（Agent）要拉取某只美股的分析师预测。它打开技能手册 `us-stock-analyst`，照着示例发出请求：

```
GET https://api.aisa.one/apis/v1/financial/analyst/eps?ticker=AAPL
```

请求返回 404。Agent 没有理由怀疑文档，于是反复检查自己的鉴权、参数、网络——而真正的原因是文档里的端点路径写错了一个字符：真实路径是 `/financial/analyst-estimates`，用的是连字符 `-`，文档却写成了 `/financial/analyst/eps`，用的是斜杠 `/`。同一套接口，相邻的 `marketpulse`、`trend-forecast` 两页写的都是对的。

这类「一个字符之差」的事故并不新鲜：开发者照着示例代码多写或漏写一个符号，签名失效、请求报错，往往要耗上大半天才在另一篇文档里找到正确写法。区别只在于：那时的受害者是人，会换思路、会翻别的页面、会提工单；而 Agent 不会。**它读到哪一页就信哪一页，错得没有任何异常信号，也没有自我怀疑的能力。** 文档对人的"不友好"是体验折损，对 Agent 的"不友好"往往是任务直接失败。

## 二、一个系统性结论

我们系统走查了这 73 页，**确认 23 处会让 Agent 拿错值、调错接口、或对不上账的硬缺口**——其中 3 处是面向 Agent 的发现入口失真（阻断级），20 处是说明文中的事实冲突。每一处都能在源文件里逐字检索复现，守住了零误报的红线。

把这些缺口归到一处，根因只有一句话：**这套文档缺少"单一可信源"（Single Source of Truth）**。

- 平台指南那 30 页其实维护得相当好——有一份 6 月 4 日刷新、内部逐行自洽的权威模型清单（`guides/models.mdx`）和定价页，价格、上下文长度、厂商计数在多页之间完全一致，我们一条都没误报。
- 问题集中在技能手册那 43 页：**每一页都自行手抄了一份模型清单、价目表、接口地址，没有一页去引用那份权威源。** 抄一次就冻结一个快照，快照之间、快照与权威源之间随时间推移系统性地漂移开来。

这正印证了参考文中那条原则的反面：信息一旦缺少单一真实源、靠各处重复叙述维持，冗余处迟早各说各话。**哪里有权威源，哪里就干净；哪里各抄各的，哪里就打架。** 这不是作者是否认真的问题，而是缺少一个强制"引用而非重写"的机制。

## 三、走查方法（简述）

走查由三组相互隔离的探查并行完成：第一组通读全库并做跨页对账，第二组用"逐页精读—跨页拉通—复核"三遍法，第三组按固定规范清单逐页核对。前两组刻意不知道分类框架的存在，以免照框架找证据、漏掉框架外的问题。三组产出由一名汇总者去重、逐字回核、归类，**拿不准的一律不报**：本轮 47 条原始线索，最终保留 20 条说明文缺口，撤回 6 条（证据检索不到，或经核对实为不同对象），并入 21 条重复项；另有 3 条阻断级缺口来自配套的纯静态检查器，可仅凭 `openapi.yaml` 证伪。

## 四、问题清单与精确定位

> **如何快速核验每一处。** 我们原本计划用"页面截图 + 红框标注"来定位，但线上站点 `aisa.one/docs` 启用了 Cloudflare 防护，自动截图会被拦截，且页面重排后框选位置会失效。对于文字类缺陷，更可靠的定位方式是 **GitHub 行级永久链接**——下表每条都给出两个入口：**线上页**（Agent/用户实际读到的内容）与**源文件**（锚定提交 `16863d3`，点击直达那一行，永不漂移）。需要时也可在源仓库根目录用所附命令一键复现。

### 缺口一类 · 发现入口失真：能力地图本身是错的（阻断级，3 处）

`guides/agent-discovery.mdx` 是 Agent 接入 AIsa 的第一落点——它靠这页判断"平台能干什么、怎么调"。而这页对 OpenAPI spec 形态的描述，与仓库实际产出的 `openapi.yaml` 对不上：

| 编号 | 文档写 | 真值 | 定位 |
| --- | --- | --- | --- |
| B1 | `121 schemas` | 321 | [线上](https://aisa.one/docs/guides/agent-discovery) · [源文件 L16](https://github.com/AIsa-team/docs/blob/16863d3/guides/agent-discovery.mdx#L16) |
| B2 | `10 categories` | 14 | [源文件 L127](https://github.com/AIsa-team/docs/blob/16863d3/guides/agent-discovery.mdx#L127) |
| B3 | 分类表只列 10 类 | 实有 14 类，漏列 4 类 | [源文件 L163](https://github.com/AIsa-team/docs/blob/16863d3/guides/agent-discovery.mdx#L163) |

最值得放大的是 B3：被漏掉的 4 个分类不是空壳，全都承载真实操作，其中 `SEO & Search Data` 一个分类就有 445 个操作，约占全 spec 的三分之二。换言之，一个只读这页做能力发现的 Agent，会以为 AIsa 提供 10 类能力、而最大的那块业务对它根本不存在。这不是"数字过期"的小瑕疵，而是核心能力的发现性缺失。

> 复现（源仓库根目录）：
> ```bash
> python3 -c "import yaml;d=yaml.safe_load(open('openapi.yaml'));print(len(d['components']['schemas']))"   # → 321，非 121
> ```

### 缺口二类 · 同一模型，多套价格（高危，4 处）

价格冲突是最隐蔽的一类：挂了旧模型，Agent 调用时至少会收到"模型不存在"的报错从而起疑；但每个价格单独看都"格式正确、量级合理"，Agent 没有任何信号判断该信哪一个。以 `qwen-plus` 为例，三个页面给了三套输出价：

| 来源 | 输出价（每百万 token） | 定位 |
| --- | --- | --- |
| 权威定价页（真值） | **$0.84** | [线上](https://aisa.one/docs/guides/pricing/ai-model-pricing-llm-inference) · [源文件 L76](https://github.com/AIsa-team/docs/blob/16863d3/guides/pricing/ai-model-pricing-llm-inference.mdx#L76) |
| 技能手册 `aisa-provider` | $0.90（偏高约 7%） | [线上](https://aisa.one/docs/agent-skills/aisa-provider) · [源文件 L99](https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/aisa-provider.mdx#L99) |
| 技能手册 `cn-llm` | **$12.60（高约 15 倍）** | [线上](https://aisa.one/docs/agent-skills/cn-llm) · [源文件 L83](https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/cn-llm.mdx#L83) |

一个做成本预算或按价比选型的 Agent，若读到 `cn-llm` 那页，会判定这个本该廉价的模型贵到不可用而将其排除；若读到 `aisa-provider`，则整笔估算偏差约 7%。**全程不报错。** 同样的分叉在 `qwen-mt-flash`（权威 $0.072 vs `cn-llm` $0.168）、`deepseek-r1`（权威 $0.4018/$1.6058 vs `cn-llm` $2.00/$8.00，高约 5 倍）、`kimi-k2.5` 上重复出现。

| 模型 | 真值 | 离群快照 | 定位 |
| --- | --- | --- | --- |
| `qwen-mt-flash` | $0.072 | $0.168 | [真值 L74](https://github.com/AIsa-team/docs/blob/16863d3/guides/pricing/ai-model-pricing-llm-inference.mdx#L74) · [离群 L84](https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/cn-llm.mdx#L84) |
| `deepseek-r1` | $0.4018 / $1.6058 | $2.00 / $8.00 | [真值 L62](https://github.com/AIsa-team/docs/blob/16863d3/guides/pricing/ai-model-pricing-llm-inference.mdx#L62) · [离群 L91](https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/cn-llm.mdx#L91) |

### 缺口三类 · 同一接口，多个地址（高危，1 处含两条端点）

即第一节那个开篇案例。`us-stock-analyst` 把两个金融端点的路径写成了斜杠分隔，而真实路径（及相邻的 `marketpulse` 页）用的是连字符：

| 接口 | 文档错写 | 正确写法 | 定位 |
| --- | --- | --- | --- |
| 分析师预测 | `/financial/analyst/eps` | `/financial/analyst-estimates` | [错 · us-stock-analyst L113](https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/us-stock-analyst.mdx#L113) · [对 · marketpulse L216](https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/marketpulse.mdx#L216) |
| 内部人交易 | `/financial/insider/trades` | `/financial/insider-trades` | [错 · us-stock-analyst L120](https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/us-stock-analyst.mdx#L120) · [对 · marketpulse L121](https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/marketpulse.mdx#L121) |

### 缺口四类 · 同一参数，两种说法（高危，1 处）

`youtube-search` 把 `gl=cn`（中国）当作正常示例使用，而 `youtube-search-skill` 明确写着 `cn` 不受支持、会返回 `Unsupported value` 错误（[源文件 L385](https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/youtube-search-skill.mdx#L385)）。Agent 取哪一页，决定了它会不会构造出一个注定报错的请求。

### 缺口五类 · 单页内部就算不平（中危，举两例）

这类缺陷不依赖跨页对账，单页审阅即可发现：

- **评分表权重合计 130%**：`stock-analysis` 的八维评分为 30 + 20 + 20 + 10 + 10 + 15 + 15 + 10 = **130%**，凑不出 100%，Agent 无法据此做加权（[源文件 L82–89](https://github.com/AIsa-team/docs/blob/16863d3/agent-skills/stock-analysis.mdx#L82)）。
- **折扣阶梯不单调**：`wallet` 页声称"充得越多折扣越高"，却把 $50 与 $100 都标为 5%（[源文件 L43–44](https://github.com/AIsa-team/docs/blob/16863d3/guides/pricing/wallet.mdx#L43)）。

> 其余缺口（模型总数 49+/50+/167 各处不一、`us-stock-analyst` 与 `llm-router` 仍在推荐 GPT-4/Claude 3 Opus 等已被取代的旧型号、`cn-llm` 声称覆盖 GLM/Baichuan 而定价表无对应行等）见技术版完整清单，定位方式相同。

## 五、系统性改进建议

缺口有 23 处，但真正要做的事可以收敛为三件，且优先级清晰：

**第一件 · 建立单一可信源，让技能手册"引用而非重写"（治本，一次消解大半）。**
那份 6 月 4 日刷新、内部自洽的权威模型清单与定价页已经存在。把模型、价格、上下文长度、端点路径这类会被多页复用的事实，固化为一份机器可读的单一数据源，各技能手册在构建时自动注入、而非人工 copy。本轮 14 条"同对象跨页不一致"会随之同时消失，也从机制上杜绝复发。

**第二件 · 把单页可发现的硬错挡在合入前（治标，但必须做）。**
评分权重应合计 100%、折扣阶梯应单调递增、端点路径应统一为连字符——这些无需跨页对账，单页审阅就该拦下。建议在 CI 中加一道极简自检（数字加和校验 + 端点路径白名单），让这类机械错不再进入正文。同样的自检也能盯住第一类的发现入口：让 `agent-discovery` 的 schema 数、分类数、分类表由 `openapi.yaml` 自动派生，spec 再增长也不会漂移。

**第三件 · 立一条"同一事实只能有一个权威定义处"的引用规矩（防复发）。**
这正是参考文里"Single Source of Truth"原则的工程化：每条信息只在一处定义，其余位置一律引用，不重复叙述。规矩立住，今天修好的 23 处，半年后才不会重新长回来。

---

技术写作不只是修正语法与拼写，而是在为用户——无论是人还是 Agent——铺一段流畅、能成功走完的旅程。AIsa 文档的底子并不差，差的是一个让所有页面都去对齐同一个答案的机制。补上这个源、让技能手册引用它，缺口的大半会自动消失，剩下的几处用单页审阅加 CI 自检即可兜住。
