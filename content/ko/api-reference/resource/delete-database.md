---
title: "데이터베이스 삭제"
description: "데이터베이스 리소스를 삭제합니다."
weight: 40
api_method: "DELETE"
api_endpoint: "/rest/resource/databases/{resourceName}"
---

## DELETE /rest/resource/databases/{resourceName}

데이터베이스 리소스를 삭제합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resourceName` | `string` | **Yes** | 리소스명 (Path) |
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
curl -X DELETE "https://{{manager-host}}:{{port}}/rest/resource/databases/{resourceName}?key=YOUR_API_KEY"
```
