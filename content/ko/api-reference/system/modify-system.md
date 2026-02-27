---
title: "시스템 수정"
description: "시스템 정보를 수정합니다."
weight: 40
api_method: "PUT"
api_endpoint: "/rest/systems/{systemName}"
---

## PUT /rest/systems/{systemName}

시스템 정보를 수정합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `systemName` | `string` | No | 변경할 시스템명 |

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
curl -X PUT "https://{{manager-host}}:{{port}}/rest/systems/{systemName}?key=YOUR_API_KEY"
```
