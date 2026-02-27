---
title: "로드밸런서 워커 설정"
description: "웹 서버의 로드밸런서 워커를 설정합니다."
weight: 70
api_method: "PUT"
api_endpoint: "/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/worker"
---

## PUT /rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/worker

웹 서버의 로드밸런서 워커를 설정합니다.

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
  "actionResult": "Y"
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
curl -X PUT "https://{{manager-host}}:{{port}}/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/worker?key=YOUR_API_KEY"
```
