---
title: "권한 상세 조회"
description: "특정 권한의 상세 정보를 조회합니다."
weight: 95
api_method: "GET"
api_endpoint: "/rest/admin/auth/{authId}"
---

## GET /rest/admin/auth/{authId}

특정 권한의 상세 정보를 조회합니다.

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
  "authId": "ADMIN",
  "authNm": "Administrator",
  "actionTypes": ["READ", "WRITE", "EXECUTE"],
  "description": "Full system administrator"
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
curl "https://{{manager-host}}:{{port}}/rest/admin/auth/{authId}?key=YOUR_API_KEY"
```
