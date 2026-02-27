---
title: "컨테이너 WAS 서버 목록 조회"
description: "컨테이너 그룹에 속한 WAS 서버 목록을 조회합니다. 컨테이너 IP, HTTP 포트 정보를 포함합니다."
weight: 140
api_method: "GET"
api_endpoint: "/rest/was/container/servers"
---

## GET /rest/was/container/servers

컨테이너 그룹에 속한 WAS 서버 목록을 조회합니다. 컨테이너 IP, HTTP 포트 정보를 포함합니다.

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
      "serverId": "was-01",
      "serverName": "WAS Server 01",
      "containerIp": "172.17.0.2",
      "httpPort": 8080
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
curl "https://{{manager-host}}:{{port}}/rest/was/container/servers?key=YOUR_API_KEY"
```
