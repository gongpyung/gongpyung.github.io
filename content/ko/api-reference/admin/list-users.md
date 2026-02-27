---
title: "사용자 목록 조회"
description: "등록된 모든 사용자 목록을 조회합니다."
weight: 20
api_method: "GET"
api_endpoint: "/rest/admin/users"
---

## GET /rest/admin/users

등록된 모든 사용자 목록을 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "users": [
    {
      "usrId": "admin",
      "usrNm": "Administrator",
      "roles": ["ADMIN"]
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
curl "https://{{manager-host}}:{{port}}/rest/admin/users?key=YOUR_API_KEY"
```
