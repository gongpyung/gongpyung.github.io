---
title: "시스템 상세 조회"
description: "특정 시스템의 상세 정보를 조회합니다."
weight: 20
api_method: "GET"
api_endpoint: "/rest/systems/{systemName}"
---

## GET /rest/systems/{systemName}

특정 시스템의 상세 정보를 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "systemId": "sys001",
  "systemName": "Production",
  "nodes": [
    {
      "nodeName": "node-01",
      "hostIp": "10.0.1.10",
      "status": "running"
    }
  ]
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `systemId` | `string` | 시스템 고유 ID |
| `systemName` | `string` | 시스템명 |
| `nodes` | `array` | 소속 노드 목록 |

#### 401 Unauthorized

```json
{
  "error": "Unauthorized",
  "code": "UNAUTHORIZED"
}
```

### Example

```bash
curl "https://{{manager-host}}:{{port}}/rest/systems/{systemName}?key=YOUR_API_KEY"
```
