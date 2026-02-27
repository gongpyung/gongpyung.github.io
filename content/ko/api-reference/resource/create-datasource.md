---
title: "데이터소스 생성"
description: "새로운 데이터소스를 생성합니다."
weight: 60
api_method: "POST"
api_endpoint: "/rest/resource/datasources"
---

## POST /rest/resource/datasources

새로운 데이터소스를 생성합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resourceName` | `string` | **Yes** | 데이터소스 리소스명 |
| `databaseResourceName` | `string` | **Yes** | 연결할 데이터베이스 리소스명 |
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
curl -X POST "https://{{manager-host}}:{{port}}/rest/resource/datasources?key=YOUR_API_KEY"
```
