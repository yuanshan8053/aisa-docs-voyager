<!--
Source: api.go (createChatCompletion)
Profile: rest-crud
Title: 创建对话补全 createChatCompletion
-->

# 创建对话补全 createChatCompletion

向指定模型发送一段对话消息，获取模型生成的补全回复，兼容 OpenAI Chat Completions 协议。支持纯文本对话、图文多模态输入、流式增量输出、函数调用（Function Calling）以及输出 token 的对数概率，适用于智能问答、多轮对话、智能体工具编排等场景。鉴权采用 HTTP Bearer，需在 `Authorization` 头携带 AIsa 平台签发的 API Key。
## 请求说明
- 请求方式：**POST**
- 请求地址：**https://api.aisa.one/v1?Action=createChatCompletion&Version=（待研发补充）**
[⚠️批注:源码未声明本接口的调用版本（Version），请由研发补充真实 Version 后再发布。]
## 请求参数
请求体为一个 JSON 对象。最小可用请求只需 `model` 与 `messages` 两个字段；其余字段按需开启流式输出、函数调用、对数概率等增强能力，不传即关闭对应能力。
### Query
```mixin-react
const columns = [
  {
    "title": "参数名称",
    "dataIndex": "name",
    "headerCellStyle": {
      "minWidth": "102px"
    }
  },
  {
    "title": "数据类型",
    "dataIndex": "type",
    "headerCellStyle": {
      "width": "170px"
    }
  },
  {
    "title": "是否必选",
    "dataIndex": "required",
    "headerCellStyle": {
      "width": "190px"
    }
  },
  {
    "title": "参数说明",
    "dataIndex": "description",
    "headerCellStyle": {
      "width": "505px"
    },
    "render": (val) => <span dangerouslySetInnerHTML={{ __html: val }} />
  }
];

const data = [
  {
    "name": "Action",
    "key": "Action",
    "description": "接口名称。当前 API 的名称为 <code>createChatCompletion</code>。",
    "required": "是",
    "type": "String"
  },
  {
    "name": "Version",
    "key": "Version",
    "description": "接口版本。当前 API 的版本为 <code>（待研发补充）</code>。",
    "required": "是",
    "type": "String"
  }
];

return (<Table
  defaultExpandAllRows={false}
  columns={columns}
  data={data}
  border={{ cell: true, wrapper: true }}
  pagination={false}
/>);
```
### Body
```mixin-react
const columns = [
  {
    "title": "参数名称",
    "dataIndex": "name",
    "headerCellStyle": {
      "minWidth": "100px"
    }
  },
  {
    "title": "数据类型",
    "dataIndex": "type",
    "headerCellStyle": {
      "width": "140px"
    }
  },
  {
    "title": "是否必选",
    "dataIndex": "required",
    "headerCellStyle": {
      "width": "100px"
    }
  },
  {
    "title": "参数说明",
    "dataIndex": "title",
    "headerCellStyle": {
      "width": "190px"
    },
    "render": (val) => <span dangerouslySetInnerHTML={{ __html: val }} />
  },
  {
    "title": "示例",
    "dataIndex": "example",
    "headerCellStyle": {
      "width": "437px"
    },
    "render": (val) => <span dangerouslySetInnerHTML={{ __html: val }} />
  }
];

const data = [
  {
    "name": "model",
    "key": "0-0",
    "title": "指定本次补全所用的模型。不同模型在推理能力、上下文窗口长度与计费上存在差异，需传入当前账号下已开通的模型名称（如 <code>gpt-4.1</code>）。\n<p>[⚠️批注:可用模型清单与各自上下文窗口随平台开通情况变化，请以控制台或模型目录为准。]</p>",
    "example": "<code>gpt-4.1</code>",
    "required": "否",
    "type": "String"
  },
  {
    "name": "messages",
    "key": "0-1",
    "title": "对话上下文消息列表，按时间先后顺序排列。模型基于整段历史生成下一条回复，因此多轮对话需把此前每一轮都回传。典型用法：先用一条 <code>system</code> 消息设定角色与规则，再以 <code>user</code> 与 <code>assistant</code> 交替承接多轮问答。",
    "example": "",
    "required": "否",
    "type": "Object[]",
    "children": [
      {
        "name": "role",
        "key": "0-1-0",
        "title": "该条消息的发言角色，告诉模型这句话由谁说出。常见取值：<code>system</code> 设定系统级指令与人设，通常置于列表首位；<code>user</code> 表示终端用户输入；<code>assistant</code> 表示模型在历史轮次中的回复，多轮对话时需把模型上一轮的输出按此角色回传。",
        "example": "<code>user</code>",
        "required": "否",
        "type": "String"
      },
      {
        "name": "content",
        "key": "0-1-1",
        "title": "消息正文。既可传纯文本字符串完成普通对话，也可传一个结构化数组，在同一条消息中混合文本块与图像块，实现图文多模态输入。\n<p>[⚠️批注:多模态数组中各元素 <code>type</code>、<code>text</code>、<code>image_url</code> 的取值约定与图像传入格式（URL 或 base64）spec 未明确，请研发补充。]</p>",
        "example": "",
        "required": "否",
        "type": "Object"
      }
    ]
  },
  {
    "name": "stream",
    "key": "0-2",
    "title": "是否以流式方式返回结果。取值：\n\n* <code>true</code>：服务端通过 SSE 分块持续推送增量内容，适合打字机式实时展示，可降低首字延迟。\n* <code>false</code>：在生成完毕后一次性返回完整回复。\n\n不传时按服务端默认行为处理（通常为 <code>false</code>）。",
    "example": "<code>false</code>",
    "required": "否",
    "type": "Boolean"
  },
  {
    "name": "logprobs",
    "key": "0-3",
    "title": "是否在返回中附带每个输出 token 的对数概率。开启后可用于分析模型对所选 token 的置信度，常见于结果可解释性、内容审核打分等场景。",
    "example": "",
    "required": "否",
    "type": "Boolean"
  },
  {
    "name": "top_logprobs",
    "key": "0-4",
    "title": "为每个输出位置额外返回概率最高的若干候选 token 及其对数概率。需在 <code>logprobs</code> 为 <code>true</code> 时配合使用，用于观察模型在该位置的备选分布。\n<p>[⚠️批注:OpenAI 协议中该值通常限制在 0 至 20 之间，AIsa 网关的实际上限请研发确认。]</p>",
    "example": "",
    "required": "否",
    "type": "Integer"
  },
  {
    "name": "functions",
    "key": "0-5",
    "title": "可供模型调用的函数声明列表（Function Calling）。模型会根据对话内容判断是否调用其中某个函数，并生成符合其参数定义的调用请求，从而把模型与外部工具或业务接口对接。模型本身不执行函数，调用动作由你的服务在收到返回后完成。",
    "example": "",
    "required": "否",
    "type": "Object[]",
    "children": [
      {
        "name": "name",
        "key": "0-5-0",
        "title": "函数名称。模型决定调用时以此作为标识返回，你的服务据此分发到对应实现。建议使用简洁、语义明确的英文名。",
        "example": "",
        "required": "否",
        "type": "String"
      },
      {
        "name": "description",
        "key": "0-5-1",
        "title": "函数用途说明。模型据此判断在何种对话情境下应当调用该函数，描述越清晰准确，触发时机越贴合预期。",
        "example": "",
        "required": "否",
        "type": "String"
      },
      {
        "name": "parameters",
        "key": "0-5-2",
        "title": "函数入参的结构定义，以 JSON Schema 描述。模型生成调用请求时会按此结构填充参数值，因此应在此声明每个参数的类型与约束。",
        "example": "",
        "required": "否",
        "type": "Object"
      }
    ]
  },
  {
    "name": "function_call",
    "key": "0-6",
    "title": "控制模型如何选择函数，需与 <code>functions</code> 配合使用。可传字符串策略：<code>auto</code> 由模型自行决定是否调用及调用哪个，<code>none</code> 则禁用函数调用、仅做普通文本回复；也可传对象 <code>{name}</code> 强制模型调用指定名称的函数。",
    "example": "",
    "required": "否",
    "type": "Object"
  }
];

return (<Table
  defaultExpandAllRows={false}
  columns={columns}
  data={data}
  border={{ cell: true, wrapper: true }}
  pagination={false}
/>);
```
## 返回参数
成功时（HTTP `200`）返回模型补全结果。响应体结构由所选模型与是否流式决定：非流式返回一个完整补全对象（含 `choices` 等字段），流式则经 SSE 以 `data:` 分块持续推送增量片段，并以 `data: [DONE]` 结束。
[⚠️批注:本 spec 仅声明 200 成功响应，未给出响应体字段结构与错误响应结构，上述响应形态依据 OpenAI 兼容协议通用约定整理，请研发补充真实响应 schema 后据实更新。]
## 错误码
| 错误码 | HTTP 状态码 | 说明 |
| --- | --- | --- |
| 400 |  | 请求体格式错误或字段不合法。常见于 `model` 名称未开通、`messages` 为空或结构不符、`top_logprobs` 取值越界等。 |
| 401 |  | 鉴权失败。`Authorization` 头缺失，或 Bearer API Key 错误、已失效。 |
| 429 |  | 请求频率或配额超限。需降低并发、稍后重试，或在控制台提升配额。 |
| 500 |  | 服务端内部错误或上游模型异常，可携带请求标识重试或联系平台支持。 |

<div data-source="api-doc-hub" style="display: none"></div>
