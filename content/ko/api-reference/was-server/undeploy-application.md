---
title: "애플리케이션 배포 해제"
description: "WAS 서버에서 애플리케이션을 배포 해제합니다."
weight: 120
api_method: "DELETE"
api_endpoint: "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application"
---

## DELETE /rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application

WAS 서버에서 애플리케이션을 배포 해제합니다.

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
curl -X DELETE "https://{{manager-host}}:{{port}}/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application?key=YOUR_API_KEY"
```
