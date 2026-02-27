---
title: "권한 목록 조회"
description: "등록된 모든 권한(Role) 목록을 조회합니다."
weight: 90
api_method: "GET"
api_endpoint: "/rest/admin/auth"
---

## GET /rest/admin/auth

등록된 모든 권한(Role) 목록을 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "auths": [
    {
      "authId": "ADMIN",
      "authNm": "Administrator",
      "actionTypes": ["READ", "WRITE", "EXECUTE"]
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
curl "https://{{manager-host}}:{{port}}/rest/admin/auth?key=YOUR_API_KEY"
```
