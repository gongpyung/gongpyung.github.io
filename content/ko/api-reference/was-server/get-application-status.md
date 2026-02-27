---
title: "애플리케이션 상태 조회"
description: "WAS 서버에 배포된 애플리케이션의 상태를 조회합니다."
weight: 130
api_method: "GET"
api_endpoint: "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/applications/status"
---

## GET /rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/applications/status

WAS 서버에 배포된 애플리케이션의 상태를 조회합니다.

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
  "applications": [
    {
      "contextPath": "/myapp",
      "status": "running",
      "sessions": 42
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
curl "https://{{manager-host}}:{{port}}/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/applications/status?key=YOUR_API_KEY"
```
