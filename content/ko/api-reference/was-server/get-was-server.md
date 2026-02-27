---
title: "WAS 서버 상세 조회"
description: "특정 WAS 서버의 상세 정보를 조회합니다."
weight: 20
api_method: "GET"
api_endpoint: "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}"
---

## GET /rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}

특정 WAS 서버의 상세 정보를 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `serverId` | `string` | **Yes** | 서버 ID (Path) |
| `nodeName` | `string` | **Yes** | 노드명 (Path) |
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "serverId": "was-01",
  "nodeName": "node-01",
  "systemName": "Production",
  "httpPort": 8080,
  "ajpPort": 8009,
  "serverType": "S",
  "status": "running",
  "javaHome": "/usr/lib/jvm/java-8",
  "installRootPath": "/app/lena/servers/was-01"
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
curl "https://{{manager-host}}:{{port}}/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
