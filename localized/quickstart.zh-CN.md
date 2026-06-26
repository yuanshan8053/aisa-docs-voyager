---
title: 快速开始 · 5 分钟跑通你的第一个 AIsa 请求
description: 面向中国开发者的 AIsa 上手指南。用一个 API Key,以 OpenAI 兼容的方式调用 Qwen、DeepSeek、Kimi、GLM、MiniMax、豆包 Seed 等国内主流大模型。
locale: zh-CN
source_of_truth:
  - https://aisa.one/docs/guides/getting-started-with-aisa.md
  - https://aisa.one/docs/guides/chinese-llms.md
  - https://aisa.one/.well-known/agent-card.json
last_synced: 2026-06-26
---

# 快速开始:5 分钟跑通你的第一个请求

> 本页是 [Getting Started with AIsa](https://aisa.one/docs/guides/getting-started-with-aisa.md) 的中文版,并针对国内开发者补齐了「用 AIsa 调用国产大模型」的最短路径。代码可直接复制运行。

AIsa 是面向 Agent 经济的能力层:**一个 API Key**,即可用 OpenAI 兼容的方式访问 100+ 大模型(含 Qwen、DeepSeek、Kimi、GLM、MiniMax、字节豆包 Seed/Seedream)、100+ 数据 API,以及面向 Agent 的机器支付。你无需为每家模型厂商单独注册、单独接入。

整个上手过程只有三步:**注册拿 Key → 改两行配置 → 发第一个请求**。

---

## 第一步:注册并领取免费额度

1. 打开注册入口 [console.aisa.one](https://console.aisa.one/),用邮箱注册(需邮箱验证),或用 Google / GitHub 账号一键登录(SSO)。
2. 所有**新注册账号自动获得 $2.00 免费额度**,可立即用于网页版 Model Playground 或直接调用 REST API,无需绑卡。
3. 在控制台创建一个 API Key,形如 `sk-...`。妥善保管,**不要提交到 Git 仓库**。

> 💡 国内网络访问 `console.aisa.one` 与 `api.aisa.one` 通常无需特殊配置;若公司网络有出口限制,把这两个域名加入白名单即可。

---

## 第二步:理解「只改两行」

AIsa 暴露**单一入口** `https://api.aisa.one/v1`,并根据你传入的 `model` 参数,动态路由到对应的模型厂商。

如果你已经在用 OpenAI 的 SDK,迁移成本几乎为零——只需要改两处:

| 配置项 | 改成 |
| --- | --- |
| `base_url` | `https://api.aisa.one/v1` |
| `api_key` | 你的 AIsa API Key |

模型名换成你想用的型号(见下方「国产模型一览」),其余代码原封不动。

---

## 第三步:发出第一个请求

### cURL

```bash
curl --url https://api.aisa.one/v1/chat/completions \
  --header 'Authorization: Bearer <你的_AIsa_API_Key>' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "deepseek-v3.2",
    "messages": [
      { "role": "user", "content": "用一句话解释什么是 Agent 经济" }
    ]
  }'
```

### Python(openai SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="<你的_AIsa_API_Key>",
    base_url="https://api.aisa.one/v1",  # ← 改这一行
)

resp = client.chat.completions.create(
    model="qwen3-max",   # 也可换成 deepseek-v3.2 / kimi-k2.6 / glm-5 等
    messages=[
        {"role": "user", "content": "用一句话解释什么是 Agent 经济"}
    ],
)
print(resp.choices[0].message.content)
```

### TypeScript / Node.js(openai SDK)

```ts
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AISA_API_KEY,
  baseURL: "https://api.aisa.one/v1", // ← 改这一行
});

const resp = await client.chat.completions.create({
  model: "kimi-k2.6",
  messages: [
    { role: "user", content: "用一句话解释什么是 Agent 经济" },
  ],
});
console.log(resp.choices[0].message.content);
```

跑通后,你应当能在终端看到模型返回的一句话——这就是你与 AIsa 的「第一次成功」。

---

## 国产模型一览(常用型号)

以下型号均可直接作为上面的 `model` 参数传入。完整列表与上下文窗口见 [Chinese LLMs 指南](https://aisa.one/docs/guides/chinese-llms.md)。

| 厂商 | 代表型号(model 值) | 适用场景 |
| --- | --- | --- |
| 阿里 Qwen | `qwen3-max`、`qwen-flash`、`qwen3-coder-plus` | 通用对话、代码、低延迟 |
| DeepSeek | `deepseek-v3.2`、`deepseek-v4-flash`、`deepseek-r1` | 通用、推理、高性价比 |
| 月之暗面 Kimi | `kimi-k2.6`、`kimi-k2-thinking` | 长上下文、推理 |
| 智谱 GLM | `glm-5` | 通用对话 |
| MiniMax | `MiniMax-M3` | 通用对话 |
| 字节豆包 Seed | `seed-2-0-pro-260328`、`seed-2-0-lite-260228` | 通用、轻量 |
| 字节 Seedream(图像)| `seedream-5-0-260128` | 文生图 |

> ⚠️ 模型型号会随网关更新而变化。**不要把型号写死在文档里背诵**——运行时以 [agent-card.json](https://aisa.one/.well-known/agent-card.json) 或 Chinese LLMs 指南为准。本页的 `last_synced` 字段标注了与线上对齐的日期。

---

## 常见问题(国内开发者高频)

**Q:报 401 / Invalid API key?**
确认请求头是 `Authorization: Bearer sk-...`,且 Key 来自 [console.aisa.one](https://console.aisa.one/) 而非其它平台。

**Q:能用 Anthropic / Gemini 的 SDK 吗?**
可以。除了 OpenAI 兼容的 `/v1/chat/completions`,AIsa 还提供 Anthropic Messages、OpenAI Responses、Gemini GenerateContent 等路由。先用本页的 OpenAI 方式跑通,再按需切换。

**Q:免费额度用完了怎么办?**
在控制台充值后按调用量计费(pay-per-call),无最低消费、无厂商锁定。

**Q:如何把这些模型接入 Cursor / Windsurf 等工具?**
把工具里的 OpenAI base_url 改成 `https://api.aisa.one/v1`、填入 AIsa Key 即可,模型名填上表中的型号。

---

## 下一步

- 浏览全部能力:让你的 Agent 读取 [`https://aisa.one/docs/llms.txt`](https://aisa.one/docs/llms.txt)(机器可读的文档总索引)。
- 给 Agent 装能力:`npm install -g @aisa-one/cli` 后 `aisa skills search` / `aisa skills install`。
- 国产模型详解:[Chinese LLMs 指南](https://aisa.one/docs/guides/chinese-llms.md)。

---

*本页由「AIsa 文档本地化 Agent」从英文源页面生成并定期对齐;若发现与线上行为不一致,即为一次需要修复的 drift——欢迎提交 Issue。*
