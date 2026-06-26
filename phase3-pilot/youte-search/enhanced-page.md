<!--
Source: api.go (youtubeSearch)
Profile: simple-query
Title: YouTube 视频搜索 youtubeSearch
-->

# YouTube 视频搜索 youtubeSearch

通过 SearchApi 聚合的 YouTube 搜索引擎,按关键词检索 YouTube 视频并返回结构化结果列表。属只读查询接口,支持按地区、界面语言以及 YouTube 过滤令牌进一步收窄结果,适用于内容发现、竞品监测、素材采集等场景。
## 请求说明
- 请求方式：**GET**
- 请求地址：**https://api.aisa.one/apis/v1?Action=youtubeSearch&Version=（待研发补充）**
[⚠️批注:源码未声明本接口的调用版本（Version），请由研发补充真实 Version 后再发布。]
## 请求参数
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
    "description": "接口名称。当前 API 的名称为 <code>youtubeSearch</code>。",
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
## 返回参数
成功时返回搜索结果载荷,包含本次检索的元信息与命中的视频列表。
```mixin-react
const columns = [
  {
    "title": "参数名称",
    "dataIndex": "name",
    "headerCellStyle": {
      "minWidth": "174px"
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
      "width": "433px"
    },
    "render": (val) => <span dangerouslySetInnerHTML={{ __html: val }} />
  }
];

const data = [
  {
    "name": "search_metadata",
    "key": "0-1-0",
    "title": "本次搜索的元信息,记录检索状态等查询维度的附加数据,便于排查与审计。",
    "example": "",
    "type": "Object"
  },
  {
    "name": "search_results",
    "key": "0-1-1",
    "title": "命中的视频结果列表,按引擎相关性排序;每个元素是一条视频记录。",
    "example": "",
    "type": "Object[]",
    "children": [
      {
        "name": "video_id",
        "key": "0-1-1-0",
        "title": "视频在 YouTube 上的唯一标识,可用于拼接播放地址或作为后续接口的入参。",
        "example": "",
        "type": "String"
      },
      {
        "name": "title",
        "key": "0-1-1-1",
        "title": "视频标题。",
        "example": "",
        "type": "String"
      },
      {
        "name": "link",
        "key": "0-1-1-2",
        "title": "视频的可点击播放链接。",
        "example": "",
        "type": "String"
      },
      {
        "name": "channel_name",
        "key": "0-1-1-3",
        "title": "发布该视频的频道名称。",
        "example": "",
        "type": "String"
      }
    ]
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
## 错误码
| 错误码 | HTTP 状态码 | 说明 |
| --- | --- | --- |
| 400 |  | 请求参数无效,例如缺少必填的 engine 或 q、参数取值不合法。 |
| 401 |  | 鉴权失败,Bearer API Key 缺失或无效。 |

<div data-source="api-doc-hub" style="display: none"></div>
