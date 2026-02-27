---
title: "WAS 서버 삭제/해제"
description: "WAS 서버를 삭제(uninstall)하거나 등록 해제(deregister)합니다."
weight: 50
api_method: "DELETE"
api_endpoint: "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}"
---

## DELETE /rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}

WAS 서버를 삭제(uninstall)하거나 등록 해제(deregister)합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `serverId` | `string` | **Yes** | 서버 ID (Path) |
| `nodeName` | `string` | **Yes** | 노드명 (Path) |
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `type` | `string` | **Yes** | 작업 유형 (`uninstall` 또는 `deregister`) |
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
curl -X DELETE "https://{{manager-host}}:{{port}}/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
