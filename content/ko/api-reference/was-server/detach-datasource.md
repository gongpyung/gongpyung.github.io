---
title: "데이터소스 해제"
description: "WAS 서버에서 데이터소스를 해제합니다."
weight: 100
api_method: "DELETE"
api_endpoint: "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource"
---

## DELETE /rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource

WAS 서버에서 데이터소스를 해제합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `serverId` | `string` | **Yes** | 서버 ID (Path) |
| `nodeName` | `string` | **Yes** | 노드명 (Path) |
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `resourceName` | `string` | **Yes** | 데이터소스 리소스명 |
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
curl -X DELETE "https://{{manager-host}}:{{port}}/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource?key=YOUR_API_KEY"
```
