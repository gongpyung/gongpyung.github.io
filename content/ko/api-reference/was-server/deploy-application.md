---
title: "애플리케이션 배포"
description: "WAS 서버에 애플리케이션을 배포합니다."
weight: 110
api_method: "POST"
api_endpoint: "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application"
---

## POST /rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application

WAS 서버에 애플리케이션을 배포합니다.

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
  "actionResult": "Y"
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
curl -X POST "https://{{manager-host}}:{{port}}/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application?key=YOUR_API_KEY"
```
