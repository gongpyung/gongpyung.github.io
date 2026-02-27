---
title: "권한 생성"
description: "새로운 권한을 생성합니다."
weight: 100
api_method: "POST"
api_endpoint: "/rest/admin/auth"
---

## POST /rest/admin/auth

새로운 권한을 생성합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `authId` | `string` | **Yes** | 권한 ID |
| `authNm` | `string` | **Yes** | 권한명 |
| `actionTypes` | `array` | **Yes** | 액션 타입 (READ, WRITE, EXECUTE) |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/admin/auth?key=YOUR_API_KEY"
```
