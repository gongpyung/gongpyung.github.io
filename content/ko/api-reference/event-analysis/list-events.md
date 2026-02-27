---
title: "분석 이벤트 조회"
description: "서버 분석 이벤트 목록을 조회합니다."
weight: 10
api_method: "GET"
api_endpoint: "/rest/analysis/event"
---

## GET /rest/analysis/event

서버 분석 이벤트 목록을 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |
| `systemName` | `string` | No | 시스템명 필터 |
| `eventType` | `string` | No | 이벤트 타입 (stuckthread, oom, fullgc, error) |
| `startDate` | `string` | No | 시작일 (yyyyMMdd) |
| `endDate` | `string` | No | 종료일 (yyyyMMdd) |

### Response

#### 200 OK

```json
{
  "events": [
    {
      "eventId": 1001,
      "eventType": "stuckthread",
      "systemName": "Production",
      "serverName": "was-01",
      "message": "Thread stuck for 300s",
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
curl "https://{{manager-host}}:{{port}}/rest/analysis/event?key=YOUR_API_KEY"
```
