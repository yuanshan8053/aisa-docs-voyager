# 增强对照表（源英文 → 加强英文 → 中文本地化）

> spec 共 3 个接口，15 个对外字段/参数。逐字段对照「原文 → 加强 → 本地化」三态，判断改得更好还是更坏。

## GET /plants

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Returns all plants from the system that the user has access to | List the plants in the store that the caller is allowed to see. This is a read-only listing; cap the result size with `limit`. Typical use is browsing or populating a catalog view. | 列出当前调用方有权查看的店内植物。这是只读列表查询,可用 `limit` 限制返回数量。典型场景为浏览或填充目录视图。 |
| `param:limit` | The maximum number of results to return | Caps how many plants are returned in one response. Omit it to let the server apply its own default ceiling. | 限制单次响应返回的植物数量。留空则由服务端套用其默认上限。 |
| `resp.200.name` | The name of the plant | Display name of the created plant, echoing what was stored. | 新建植物的展示名称,回显入库内容。 |
| `resp.200.tag` | Tag to specify the type | Free-text tag of the created plant. | 新建植物的自由文本标签。 |
| `resp.400.error` |  | Numeric error code identifying the failure. | 标识本次失败的数字错误码。 |
| `resp.400.message` |  | Human-readable detail describing the error. | 对错误的可读详细说明。 |

## POST /plants

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Creates a new plant in the store | Create a new plant in the store from the supplied plant details and return the stored record. Typical use is adding inventory. | 用提交的植物信息在店内新建一条植物记录,并返回入库后的对象。典型场景为新增库存。 |
| `req.name` | The name of the plant | Display name of the created plant, echoing what was stored. | 新建植物的展示名称,回显入库内容。 |
| `req.tag` | Tag to specify the type | Free-text tag of the created plant. | 新建植物的自由文本标签。 |
| `req.id` | Identification number of the plant | Caller-assigned identification number for the new plant, distinguishing it from existing records. | 为新植物指定的标识编号,用于与现有记录区分。 |
| `resp.200.name` | The name of the plant | Display name of the created plant, echoing what was stored. | 新建植物的展示名称,回显入库内容。 |
| `resp.200.tag` | Tag to specify the type | Free-text tag of the created plant. | 新建植物的自由文本标签。 |
| `resp.400.error` |  | Numeric error code identifying the failure. | 标识本次失败的数字错误码。 |
| `resp.400.message` |  | Human-readable detail describing the error. | 对错误的可读详细说明。 |

## DELETE /plants/{id}

| 字段路径 | 源英文（原生，只读） | 加强英文 desc_en | 中文 title_zh |
| --- | --- | --- | --- |
| `(operation)` | Deletes a single plant based on the ID supplied | Delete a single plant identified by its path `id`. On success the store returns no body. Typical use is removing inventory. | 按路径中的 `id` 删除单条植物记录。成功时不返回响应体。典型场景为下架库存。 |
| `param:id` | ID of plant to delete | Identifier of the plant to delete. The plant with this ID is removed from the store. | 要删除的植物的标识。该 ID 对应的植物将从店内移除。 |
| `resp.400.error` |  | Numeric error code identifying the failure. | 标识本次失败的数字错误码。 |
| `resp.400.message` |  | Human-readable detail describing the error. | 对错误的可读详细说明。 |

