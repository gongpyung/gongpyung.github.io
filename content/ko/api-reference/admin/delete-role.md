---
title: "권한 삭제"
description: "권한을 삭제합니다."
weight: 110
api_method: "DELETE"
api_endpoint: "/rest/admin/auth/{authId}"
---

## DELETE /rest/admin/auth/{authId}

권한을 삭제합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `authId` | `string` | **Yes** | 권한 ID (Path) |
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
curl -X DELETE "https://{{manager-host}}:{{port}}/rest/admin/auth/{authId}?key=YOUR_API_KEY"
```
