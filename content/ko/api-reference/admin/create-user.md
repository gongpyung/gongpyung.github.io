---
title: "사용자 생성"
description: "새로운 사용자를 생성합니다. 비밀번호는 8자 이상, 영문+숫자+특수문자를 포함해야 합니다."
weight: 40
api_method: "POST"
api_endpoint: "/rest/admin/user"
---

## POST /rest/admin/user

새로운 사용자를 생성합니다. 비밀번호는 8자 이상, 영문+숫자+특수문자를 포함해야 합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `usrId` | `string` | **Yes** | 사용자 ID |
| `usrNm` | `string` | **Yes** | 사용자명 |
| `usrPw` | `string` | **Yes** | 비밀번호 (8자 이상, 영문+숫자+특수문자) |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/admin/user?key=YOUR_API_KEY"
```
