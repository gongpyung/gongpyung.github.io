---
title: "사용자 역할 취소"
description: "사용자의 역할을 취소합니다."
weight: 80
api_method: "POST"
api_endpoint: "/rest/admin/user/{usrId}/auth/revoke"
---

## POST /rest/admin/user/{usrId}/auth/revoke

사용자의 역할을 취소합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `usrId` | `string` | **Yes** | 사용자 ID (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `authId` | `string` | **Yes** | 권한 ID |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/admin/user/{usrId}/auth/revoke?key=YOUR_API_KEY"
```
