---
title: "등록 가능 웹 서버 목록 조회"
description: "지정된 시스템의 노드에서 등록 가능한 웹 서버 목록을 조회합니다. 아직 LENA에 등록되지 않은 서버들을 반환합니다."
weight: 100
api_method: "GET"
api_endpoint: "/rest/web/servers/register/nodes/{nodeName}/systems/{systemName}"
---

## GET /rest/web/servers/register/nodes/{nodeName}/systems/{systemName}

지정된 시스템의 노드에서 등록 가능한 웹 서버 목록을 조회합니다. 아직 LENA에 등록되지 않은 서버들을 반환합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `nodeName` | `string` | **Yes** | 노드명 (Path) |
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "noRegisterdServers": [
    {
      "systemName": "Production",
      "nodeName": "node-01",
      "serverId": "web-03",
      "serverIp": "10.0.1.10",
      "httpPort": 8080,
      "httpsPort": 8443
    }
  ]
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `systemName` | `string` | 시스템명 |
| `nodeName` | `string` | 노드명 |
| `serverId` | `string` | 서버 ID |
| `serverIp` | `string` | 서버 IP |
| `httpPort` | `integer` | HTTP 포트 |
| `httpsPort` | `integer` | HTTPS 포트 |

#### 401 Unauthorized

```json
{
  "error": "Unauthorized",
  "code": "UNAUTHORIZED"
}
```

### Example

```bash
curl "https://{{manager-host}}:{{port}}/rest/web/servers/register/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
