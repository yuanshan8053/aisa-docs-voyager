<!--
Source: api.go (createChatCompletion)
Profile: rest-crud
Title: 创建对话补全 createChatCompletion
-->

# 创建对话补全 createChatCompletion

向指定模型发送一段对话消息并获取模型生成的补全回复,兼容 OpenAI Chat Completions 协议。支持纯文本对话、图文多模态输入、流式增量输出、函数调用(Function Calling)以及输出 token 的对数概率,适用于问答、多轮对话、智能体工具编排等场景。
## 请求说明
- 请求方式：**POST**
- 请求地址：**https://api.aisa.one/v1?Action=createChatCompletion&Version=（待研发补充）**
[⚠️批注:源码未声明本接口的调用版本（Version），请由研发补充真实 Version 后再发布。]
## 请求参数
请求体为一个 JSON 对象。最小可用请求只需 `model` 与 `messages` 两个字段;其余字段用于开启流式、函数调用、对数概率等增强能力。
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
    "title": "指定生成本次补全所用的模型。不同模型在推理能力、上下文窗口和计费上存在差异,需传入当前账号下已开通的模型名称。",
    "example": "<code>gpt-4.1</code>",
    "required": "否",
    "type": "String"
  },
  {
    "name": "messages",
    "key": "0-1",
    "title": "对话上下文消息列表,按时间先后顺序排列。模型基于整段历史生成下一条回复;典型用法是先用 system 设定角色与规则,再以 user / assistant 交替承接多轮对话。",
    "example": "",
    "required": "否",
    "type": "Object[]",
    "children": [
      {
        "name": "role",
        "key": "0-1-0",
        "title": "该条消息的发言角色,告诉模型这句话由谁说出。常见取值:<code>system</code> 设定系统级指令与人设;<code>user</code> 表示终端用户输入;<code>assistant</code> 表示模型在历史轮次中的回复。",
        "example": "<code>user</code>",
        "required": "否",
        "type": "String"
      },
      {
        "name": "content",
        "key": "0-1-1",
        "title": "消息正文。既可传纯文本字符串完成普通对话,也可传结构化数组以在同一条消息中混合文本与图像,实现多模态输入。",
        "example": "",
        "required": "否",
        "type": "Object"
      }
    ]
  },
  {
    "name": "stream",
    "key": "0-2",
    "title": "是否以流式方式返回结果。开启后服务端通过 SSE 分块持续推送增量内容,适合打字机式实时展示;关闭则在生成完毕后一次性返回完整回复。",
    "example": "<code>false</code>",
    "required": "否",
    "type": "Boolean"
  },
  {
    "name": "logprobs",
    "key": "0-3",
    "title": "是否在返回中附带每个输出 token 的对数概率,可用于分析模型对所选 token 的置信度。",
    "example": "",
    "required": "否",
    "type": "Boolean"
  },
  {
    "name": "top_logprobs",
    "key": "0-4",
    "title": "为每个输出位置额外返回概率最高的若干候选 token 及其对数概率。需在 <code>logprobs</code> 开启时配合使用,用于观察模型在该位置的备选分布。",
    "example": "",
    "required": "否",
    "type": "Integer"
  },
  {
    "name": "functions",
    "key": "0-5",
    "title": "可供模型调用的函数声明列表(Function Calling)。模型会根据对话内容判断是否调用其中某个函数并生成符合其参数定义的调用请求,从而把模型与外部工具或接口对接。",
    "example": "",
    "required": "否",
    "type": "Object[]",
    "children": [
      {
        "name": "name",
        "key": "0-5-0",
        "title": "函数名称,模型决定调用时以此作为标识返回。建议使用简洁、语义明确的英文名。",
        "example": "",
        "required": "否",
        "type": "String"
      },
      {
        "name": "description",
        "key": "0-5-1",
        "title": "函数用途说明。模型据此判断何时应当调用该函数,描述越清晰,触发越准确。",
        "example": "",
        "required": "否",
        "type": "String"
      },
      {
        "name": "parameters",
        "key": "0-5-2",
        "title": "函数入参的结构定义,以 JSON Schema 描述。模型生成调用请求时会按此结构填充参数。",
        "example": "",
        "required": "否",
        "type": "Object"
      }
    ]
  },
  {
    "name": "function_call",
    "key": "0-6",
    "title": "控制模型如何选择函数。可传字符串策略(如 <code>auto</code> 由模型自行决定是否调用、<code>none</code> 禁用调用),也可传对象 <code>{name}</code> 强制模型调用指定函数。",
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
本接口 spec 仅声明 200 成功响应,响应体结构由所选模型与是否流式决定:非流式返回完整补全对象,流式经 SSE 分块推送增量。下列错误码依据 OpenAI 兼容网关通用约定整理,以服务端实际返回为准。
[⚠️批注: spec 未声明错误响应结构与错误码,此处错误码为 OpenAI 兼容约定推断,待研发确认。]
## 错误码
| 错误码 | HTTP 状态码 | 说明 |
| --- | --- | --- |
| 400 |  | 请求体格式错误或字段不合法,例如 model 未开通、messages 为空或结构不符。 |
| 401 |  | 鉴权失败,Bearer API Key 缺失、错误或已失效。 |
| 429 |  | 请求频率或配额超限,需降低并发或稍后重试。 |

<div data-source="api-doc-hub" style="display: none"></div>
