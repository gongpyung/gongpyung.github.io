---
title: "모든 시스템 조회"
description: "사용자가 접근 가능한 모든 시스템 목록을 조회합니다."
weight: 10
api_method: "GET"
api_endpoint: "/rest/systems"
---

## GET /rest/systems

사용자가 접근 가능한 모든 시스템 목록을 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "systems": [
    {
      "systemId": "sys001",
      "systemName": "Production",
      "nodeCount": 5,
      "webCount": 2,
      "appCount": 10,
      "sessionCount": 2
    }
  ]
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `systemId` | `string` | 시스템 고유 ID |
| `systemName` | `string` | 시스템명 |
| `nodeCount` | `integer` | 소속 노드 수 |
| `webCount` | `integer` | 웹 서버 수 |
| `appCount` | `integer` | WAS 서버 수 |
| `sessionCount` | `integer` | 세션 서버 수 |

#### 401 Unauthorized

```json
{
  "error": "Unauthorized",
  "code": "UNAUTHORIZED"
}
```

### Example

```bash
curl "https://{{manager-host}}:{{port}}/rest/systems?key=YOUR_API_KEY"
```
