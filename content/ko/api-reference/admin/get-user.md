---
title: "사용자 상세 조회"
description: "특정 사용자의 상세 정보를 조회합니다."
weight: 30
api_method: "GET"
api_endpoint: "/rest/admin/user/{usrId}"
---

## GET /rest/admin/user/{usrId}

특정 사용자의 상세 정보를 조회합니다.

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
  "usrId": "admin",
  "usrNm": "Administrator",
  "roles": ["ADMIN"],
  "createdAt": "2026-01-01"
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
curl "https://{{manager-host}}:{{port}}/rest/admin/user/{usrId}?key=YOUR_API_KEY"
```
