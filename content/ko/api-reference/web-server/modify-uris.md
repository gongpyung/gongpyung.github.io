---
title: "URI/Rewrite 설정 수정"
description: "웹 서버의 URI 패턴 및 Rewrite 설정을 추가하거나 삭제합니다."
weight: 110
api_method: "PUT"
api_endpoint: "/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/uri"
---

## PUT /rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/uri

웹 서버의 URI 패턴 및 Rewrite 설정을 추가하거나 삭제합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `serverId` | `string` | **Yes** | 서버 ID (Path) |
| `nodeName` | `string` | **Yes** | 노드명 (Path) |
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `type` | `string` | **Yes** | 작업 유형 (`create` 또는 `delete`) |
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `uris` | `array` | **Yes** | URI 패턴 목록 (예: `["/api/*", "/app/*"]`) |

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
curl -X PUT "https://{{manager-host}}:{{port}}/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/uri?key=YOUR_API_KEY"
```
