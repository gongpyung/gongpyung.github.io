---
title: "데이터베이스 생성"
description: "새로운 데이터베이스 리소스를 생성합니다."
weight: 30
api_method: "POST"
api_endpoint: "/rest/resource/databases"
---

## POST /rest/resource/databases

새로운 데이터베이스 리소스를 생성합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `resourceName` | `string` | **Yes** | 리소스명 |
| `databaseType` | `string` | **Yes** | DB 타입 (MySQL, Oracle, PostgreSQL 등) |
| `host` | `string` | **Yes** | 호스트 |
| `port` | `integer` | **Yes** | 포트 |
| `databaseName` | `string` | **Yes** | 데이터베이스명 |
| `userName` | `string` | **Yes** | 사용자명 |
| `password` | `string` | **Yes** | 비밀번호 |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/resource/databases?key=YOUR_API_KEY"
```
