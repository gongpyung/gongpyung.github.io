---
title: "컨테이너 웹 서버 목록 조회"
description: "컨테이너 그룹에 속한 웹 서버 목록을 조회합니다. 컨테이너 IP, HTTP 포트 정보를 포함합니다."
weight: 90
api_method: "GET"
api_endpoint: "/rest/web/container/servers"
---

## GET /rest/web/container/servers

컨테이너 그룹에 속한 웹 서버 목록을 조회합니다. 컨테이너 IP, HTTP 포트 정보를 포함합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "containerList": [
    {
      "serverId": "web-01",
      "serverName": "Web Server 01",
      "containerIp": "172.17.0.3",
      "httpPort": 80
    }
  ]
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `serverId` | `string` | 서버 ID |
| `serverName` | `string` | 서버명 |
| `containerIp` | `string` | 컨테이너 IP |
| `httpPort` | `integer` | HTTP 포트 |

#### 401 Unauthorized

```json
{
  "error": "Unauthorized",
  "code": "UNAUTHORIZED"
}
```

### Example

```bash
curl "https://{{manager-host}}:{{port}}/rest/web/container/servers?key=YOUR_API_KEY"
```
