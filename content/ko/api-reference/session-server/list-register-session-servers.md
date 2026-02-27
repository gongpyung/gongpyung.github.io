---
title: "등록 가능 세션 서버 목록 조회"
description: "특정 노드에 등록 가능한 세션 서버 목록을 조회합니다."
weight: 55
api_method: "GET"
api_endpoint: "/rest/session/servers/register/nodes/{nodeName}/systems/{systemName}"
---

## GET /rest/session/servers/register/nodes/{nodeName}/systems/{systemName}

특정 노드에 등록 가능한 세션 서버 목록을 조회합니다.

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
  "servers": [
    {
      "serverId": "session-02",
      "serverHome": "/usr/local/lena/servers/session-02",
      "status": "available"
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
curl "https://{{manager-host}}:{{port}}/rest/session/servers/register/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
