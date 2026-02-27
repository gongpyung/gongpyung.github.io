---
title: "WAS 서버 수정"
description: "WAS 서버 설정을 수정합니다."
weight: 40
api_method: "PUT"
api_endpoint: "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}"
---

## PUT /rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}

WAS 서버 설정을 수정합니다.

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
curl -X PUT "https://{{manager-host}}:{{port}}/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
