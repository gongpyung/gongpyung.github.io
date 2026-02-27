---
title: "데이터베이스 상세 조회"
description: "특정 데이터베이스의 상세 정보를 조회합니다."
weight: 20
api_method: "GET"
api_endpoint: "/rest/resource/databases/{resourceName}"
---

## GET /rest/resource/databases/{resourceName}

특정 데이터베이스의 상세 정보를 조회합니다.

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
  "resourceName": "mydb",
  "databaseType": "MySQL",
  "host": "10.0.1.100",
  "port": 3306,
  "databaseName": "lena_db",
  "userName": "lena_user"
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
curl "https://{{manager-host}}:{{port}}/rest/resource/databases/{resourceName}?key=YOUR_API_KEY"
```
