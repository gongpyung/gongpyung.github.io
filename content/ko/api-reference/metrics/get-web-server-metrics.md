---
title: "웹 서버 메트릭 조회"
description: "특정 웹 서버의 메트릭(연결 수, 요청 수 등)을 조회합니다."
weight: 50
api_method: "GET"
api_endpoint: "/meters/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}"
---

## GET /meters/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}

특정 웹 서버의 메트릭(연결 수, 요청 수 등)을 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `serverId` | `string` | **Yes** | 서버 ID (Path) |
| `nodeName` | `string` | **Yes** | 노드명 (Path) |
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "serverId": "web-01",
  "connections": 150,
  "requestsPerSec": 42.5,
  "bytesIn": 10240,
  "bytesOut": 51200
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
curl "https://{{manager-host}}:{{port}}/meters/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
