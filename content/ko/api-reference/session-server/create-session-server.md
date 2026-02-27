---
title: "세션 서버 설치/등록"
description: "세션 서버를 설치하거나 기존 서버를 등록합니다."
weight: 30
api_method: "POST"
api_endpoint: "/rest/session/servers"
---

## POST /rest/session/servers

세션 서버를 설치하거나 기존 서버를 등록합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | `string` | **Yes** | 작업 유형 (`install` 또는 `register`) |
| `serverId` | `string` | **Yes** | 서버 ID |
| `nodeName` | `string` | **Yes** | 노드명 |
| `systemName` | `string` | **Yes** | 시스템명 |
| `serverPort` | `integer` | **Yes** | 서버 포트 |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/session/servers?key=YOUR_API_KEY"
```
