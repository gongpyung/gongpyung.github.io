---
title: "모든 노드 메트릭 조회"
description: "모든 노드의 메트릭 정보를 일괄 조회합니다."
weight: 10
api_method: "GET"
api_endpoint: "/meters/nodes"
---

## GET /meters/nodes

모든 노드의 메트릭 정보를 일괄 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "nodes": [
    {
      "nodeName": "node-01",
      "cpu": 45.2,
      "memoryUsed": 4096,
      "memoryTotal": 8192,
      "diskUsage": 62.5
    }
  ]
}
```

#### 401 Unauthorized

```json
{
  "error": "Unauthorized",
  "code": "UNAUTHORIZED"
}
```

### Example

```bash
curl "https://{{manager-host}}:{{port}}/meters/nodes?key=YOUR_API_KEY"
```
