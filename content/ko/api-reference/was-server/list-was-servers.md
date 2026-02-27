---
title: "모든 WAS 서버 조회"
description: "등록된 모든 WAS 서버 목록을 조회합니다."
weight: 10
api_method: "GET"
api_endpoint: "/rest/was/servers"
---

## GET /rest/was/servers

등록된 모든 WAS 서버 목록을 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "servers": [
    {
      "serverId": "was-01",
      "nodeName": "node-01",
      "systemName": "Production",
      "httpPort": 8080,
      "serverType": "S",
      "status": "running"
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
curl "https://{{manager-host}}:{{port}}/rest/was/servers?key=YOUR_API_KEY"
```
