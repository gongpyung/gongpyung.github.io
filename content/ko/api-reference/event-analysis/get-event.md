---
title: "이벤트 상세 조회"
description: "특정 이벤트의 상세 정보(스택 트레이스 포함)를 조회합니다."
weight: 20
api_method: "GET"
api_endpoint: "/rest/analysis/event/{eventId}"
---

## GET /rest/analysis/event/{eventId}

특정 이벤트의 상세 정보(스택 트레이스 포함)를 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `eventId` | `integer` | **Yes** | 이벤트 ID (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "eventId": 1001,
  "eventType": "stuckthread",
  "systemName": "Production",
  "serverName": "was-01",
  "message": "Thread stuck for 300s",
  "stackTrace": "java.lang.Thread.sleep(Native Method)\n...",
  "createdAt": "2026-02-27 12:00:00"
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
curl "https://{{manager-host}}:{{port}}/rest/analysis/event/{eventId}?key=YOUR_API_KEY"
```
