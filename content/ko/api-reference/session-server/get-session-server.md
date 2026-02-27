---
title: "세션 서버 상세 조회"
description: "특정 세션 서버의 상세 정보를 조회합니다."
weight: 20
api_method: "GET"
api_endpoint: "/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}"
---

## GET /rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}

특정 세션 서버의 상세 정보를 조회합니다.

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
  "nodeName": "node-01",
  "systemName": "Production",
  "serverPort": 6100,
  "status": "running"
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
curl "https://{{manager-host}}:{{port}}/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
