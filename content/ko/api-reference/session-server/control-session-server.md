---
title: "세션 서버 제어 (시작/중지)"
description: "세션 서버를 시작하거나 중지합니다."
weight: 50
api_method: "POST"
api_endpoint: "/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action"
---

## POST /rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action

세션 서버를 시작하거나 중지합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `serverId` | `string` | **Yes** | 서버 ID (Path) |
| `nodeName` | `string` | **Yes** | 노드명 (Path) |
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `action` | `string` | **Yes** | 액션 (`start` 또는 `stop`) |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action?key=YOUR_API_KEY"
```
