---
title: "알림 목록 조회"
description: "시스템 이벤트 알림 목록을 조회합니다. interval 또는 dateTime 기반 필터를 지원합니다."
weight: 10
api_method: "GET"
api_endpoint: "/rest/notification"
---

## GET /rest/notification

시스템 이벤트 알림 목록을 조회합니다. interval 또는 dateTime 기반 필터를 지원합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |
| `interval` | `integer` | No | 조회 범위 (분 단위) |
| `dateTime` | `string` | No | 기준 시각 (yyyyMMddHHmmss) |
| `limit` | `integer` | No | 최대 조회 건수 |

### Response

#### 200 OK

```json
{
  "notifications": [
    {
      "id": 1001,
      "type": "WARNING",
      "message": "High CPU usage on node-01",
      "targetName": "node-01",
      "createdAt": "20260227120000"
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
curl "https://{{manager-host}}:{{port}}/rest/notification?key=YOUR_API_KEY"
```
