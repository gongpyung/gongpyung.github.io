---
title: "세션 서버 메트릭 조회"
description: "특정 세션 서버의 메트릭을 조회합니다."
weight: 60
api_method: "GET"
api_endpoint: "/meters/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}"
---

## GET /meters/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}

특정 세션 서버의 메트릭을 조회합니다.

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
  "serverId": "session-01",
  "activeSessions": 1250,
  "memoryUsed": 256,
  "memoryMax": 512
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
curl "https://{{manager-host}}:{{port}}/meters/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
