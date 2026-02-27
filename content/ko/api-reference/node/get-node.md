---
title: "노드 상세 조회"
description: "특정 노드의 상세 정보를 조회합니다."
weight: 20
api_method: "GET"
api_endpoint: "/rest/nodes/{nodeName}/systems/{systemName}"
---

## GET /rest/nodes/{nodeName}/systems/{systemName}

특정 노드의 상세 정보를 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `nodeName` | `string` | **Yes** | 노드명 (Path) |
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "nodeName": "node-01",
  "systemName": "Production",
  "hostIp": "10.0.1.10",
  "agentPort": 7700,
  "status": "running",
  "servers": [
    {"serverId": "was-01", "serverType": "WAS", "status": "running"}
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
curl "https://{{manager-host}}:{{port}}/rest/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
