---
title: "권한 수정"
description: "권한 정보를 수정합니다."
weight: 105
api_method: "PUT"
api_endpoint: "/rest/admin/auth/{authId}"
---

## PUT /rest/admin/auth/{authId}

권한 정보를 수정합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `authId` | `string` | **Yes** | 권한 ID (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `authNm` | `string` | No | 권한명 |
| `actionTypes` | `array` | No | 액션 타입 (READ, WRITE, EXECUTE) |

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
curl -X PUT "https://{{manager-host}}:{{port}}/rest/admin/auth/{authId}?key=YOUR_API_KEY"
```
