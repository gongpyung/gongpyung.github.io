---
title: "데이터소스 상세 조회"
description: "특정 데이터소스의 상세 정보를 조회합니다."
weight: 55
api_method: "GET"
api_endpoint: "/rest/resource/datasources/{resourceName}"
---

## GET /rest/resource/datasources/{resourceName}

특정 데이터소스의 상세 정보를 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resourceName` | `string` | **Yes** | 리소스명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "resourceName": "myds",
  "databaseResourceName": "mydb",
  "minPoolSize": 5,
  "maxPoolSize": 20,
  "initialPoolSize": 5,
  "maxWait": 30000
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
curl "https://{{manager-host}}:{{port}}/rest/resource/datasources/{resourceName}?key=YOUR_API_KEY"
```
