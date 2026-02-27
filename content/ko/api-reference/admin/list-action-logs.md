---
title: "액션 추적 로그 조회"
description: "관리 액션 추적 로그를 조회합니다."
weight: 10
api_method: "GET"
api_endpoint: "/rest/admin/actionTraceLogList"
---

## GET /rest/admin/actionTraceLogList

관리 액션 추적 로그를 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |
| `startDate` | `string` | No | 시작일 (yyyyMMdd) |
| `endDate` | `string` | No | 종료일 (yyyyMMdd) |

### Response

#### 200 OK

```json
{
  "logs": [
    {
      "logId": 1,
      "userId": "admin",
      "action": "CREATE_SYSTEM",
      "targetName": "Production",
      "result": "SUCCESS",
      "createdAt": "2026-02-27 12:00:00"
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
curl "https://{{manager-host}}:{{port}}/rest/admin/actionTraceLogList?key=YOUR_API_KEY"
```
