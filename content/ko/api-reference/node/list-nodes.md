---
title: "모든 노드 조회"
description: "등록된 모든 노드 목록을 조회합니다."
weight: 10
api_method: "GET"
api_endpoint: "/rest/nodes"
---

## GET /rest/nodes

등록된 모든 노드 목록을 조회합니다.

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
      "systemName": "Production",
      "hostIp": "10.0.1.10",
      "agentPort": 7700,
      "status": "running"
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
curl "https://{{manager-host}}:{{port}}/rest/nodes?key=YOUR_API_KEY"
```
