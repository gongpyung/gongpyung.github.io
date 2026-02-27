---
title: "데이터소스 수정"
description: "데이터소스의 설정을 수정합니다."
weight: 65
api_method: "PUT"
api_endpoint: "/rest/resource/datasource/{resourceName}"
---

## PUT /rest/resource/datasource/{resourceName}

데이터소스의 설정을 수정합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resourceName` | `string` | **Yes** | 리소스명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `minPoolSize` | `integer` | No | 최소 커넥션 풀 크기 |
| `maxPoolSize` | `integer` | No | 최대 커넥션 풀 크기 |

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
curl -X PUT "https://{{manager-host}}:{{port}}/rest/resource/datasource/{resourceName}?key=YOUR_API_KEY"
```
