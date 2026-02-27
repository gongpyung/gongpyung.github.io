---
title: "WAS 컨테이너 메트릭 조회"
description: "WAS 컨테이너의 메트릭을 호스트명 기준으로 조회합니다."
weight: 70
api_method: "GET"
api_endpoint: "/meters/was/container/{hostName}"
---

## GET /meters/was/container/{hostName}

WAS 컨테이너의 메트릭을 호스트명 기준으로 조회합니다.

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
  "hostName": "was-container-01",
  "cpu": 35.2,
  "memoryUsed": 2048,
  "memoryMax": 4096,
  "threadCount": 150
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
curl "https://{{manager-host}}:{{port}}/meters/was/container/{hostName}?key=YOUR_API_KEY"
```
