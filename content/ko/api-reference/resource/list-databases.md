---
title: "데이터베이스 목록 조회"
description: "등록된 모든 데이터베이스 목록을 조회합니다."
weight: 10
api_method: "GET"
api_endpoint: "/rest/resource/databases"
---

## GET /rest/resource/databases

등록된 모든 데이터베이스 목록을 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "databases": [
    {
      "resourceName": "mydb",
      "databaseType": "MySQL",
      "host": "10.0.1.100",
      "port": 3306,
      "databaseName": "lena_db"
    }
  ]
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
curl "https://{{manager-host}}:{{port}}/rest/resource/databases?key=YOUR_API_KEY"
```
