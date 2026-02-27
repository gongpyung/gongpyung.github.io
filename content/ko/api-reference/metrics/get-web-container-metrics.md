---
title: "웹 컨테이너 메트릭 조회"
description: "웹 컨테이너의 메트릭을 호스트명 기준으로 조회합니다."
weight: 80
api_method: "GET"
api_endpoint: "/meters/web/container/{hostName}"
---

## GET /meters/web/container/{hostName}

웹 컨테이너의 메트릭을 호스트명 기준으로 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `hostName` | `string` | **Yes** | 호스트명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "hostName": "web-container-01",
  "connections": 85,
  "requestsPerSec": 120.5,
  "bytesIn": 20480,
  "bytesOut": 102400
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
curl "https://{{manager-host}}:{{port}}/meters/web/container/{hostName}?key=YOUR_API_KEY"
```
