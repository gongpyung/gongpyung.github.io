---
title: "특정 노드 메트릭 조회"
description: "특정 노드의 상세 메트릭 정보를 조회합니다."
weight: 20
api_method: "GET"
api_endpoint: "/meters/nodes/{nodeName}/systems/{systemName}"
---

## GET /meters/nodes/{nodeName}/systems/{systemName}

특정 노드의 상세 메트릭 정보를 조회합니다.

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
  "cpu": 45.2,
  "memoryUsed": 4096,
  "memoryTotal": 8192,
  "diskUsage": 62.5,
  "networkIn": 1024,
  "networkOut": 2048
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
curl "https://{{manager-host}}:{{port}}/meters/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
