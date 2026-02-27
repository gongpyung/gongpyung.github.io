---
title: "사용자 수정"
description: "사용자 정보를 수정합니다."
weight: 50
api_method: "PUT"
api_endpoint: "/rest/admin/user/{usrId}"
---

## PUT /rest/admin/user/{usrId}

사용자 정보를 수정합니다.

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
curl -X PUT "https://{{manager-host}}:{{port}}/rest/admin/user/{usrId}?key=YOUR_API_KEY"
```
