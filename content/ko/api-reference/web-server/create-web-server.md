---
title: "웹 서버 설치/등록"
description: "웹 서버를 설치하거나 기존 서버를 등록합니다."
weight: 30
api_method: "POST"
api_endpoint: "/rest/web/servers"
---

## POST /rest/web/servers

웹 서버를 설치하거나 기존 서버를 등록합니다.

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
| `httpPort` | `integer` | **Yes** | HTTP 포트 |
| `httpsPort` | `integer` | No | HTTPS 포트 |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/web/servers?key=YOUR_API_KEY"
```
