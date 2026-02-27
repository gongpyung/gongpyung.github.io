---
title: "시스템 생성"
description: "새로운 시스템을 생성합니다."
weight: 30
api_method: "POST"
api_endpoint: "/rest/systems"
---

## POST /rest/systems

새로운 시스템을 생성합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `systemName` | `string` | **Yes** | 시스템명 (영숫자, -, _ / 최대 20자) |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/systems?key=YOUR_API_KEY"
```
