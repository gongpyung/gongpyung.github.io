---
title: "데이터소스 목록 조회"
description: "등록된 모든 데이터소스 목록을 조회합니다."
weight: 50
api_method: "GET"
api_endpoint: "/rest/resource/datasources"
---

## GET /rest/resource/datasources

등록된 모든 데이터소스 목록을 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "datasources": [
    {
      "resourceName": "myds",
      "databaseResourceName": "mydb",
      "minPoolSize": 5,
      "maxPoolSize": 20
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
curl "https://{{manager-host}}:{{port}}/rest/resource/datasources?key=YOUR_API_KEY"
```
