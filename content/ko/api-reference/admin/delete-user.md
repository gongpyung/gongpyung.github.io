---
title: "사용자 삭제"
description: "사용자를 삭제합니다."
weight: 60
api_method: "DELETE"
api_endpoint: "/rest/admin/user/{usrId}"
---

## DELETE /rest/admin/user/{usrId}

사용자를 삭제합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `usrId` | `string` | **Yes** | 사용자 ID (Path) |
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
curl -X DELETE "https://{{manager-host}}:{{port}}/rest/admin/user/{usrId}?key=YOUR_API_KEY"
```
