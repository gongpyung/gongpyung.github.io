---
title: "SSL 설정"
description: "웹 서버에 SSL을 설정합니다."
weight: 80
api_method: "POST"
api_endpoint: "/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/ssl"
---

## POST /rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/ssl

웹 서버에 SSL을 설정합니다.

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/ssl?key=YOUR_API_KEY"
```
