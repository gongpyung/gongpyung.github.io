---
title: "사용자 역할 목록 조회"
description: "특정 사용자에게 부여된 역할 목록을 조회합니다."
weight: 65
api_method: "GET"
api_endpoint: "/rest/admin/user/{usrId}/auth"
---

## GET /rest/admin/user/{usrId}/auth

특정 사용자에게 부여된 역할 목록을 조회합니다.

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
  "auths": [
    {
      "authId": "ADMIN",
      "authNm": "Administrator"
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
curl "https://{{manager-host}}:{{port}}/rest/admin/user/{usrId}/auth?key=YOUR_API_KEY"
```
