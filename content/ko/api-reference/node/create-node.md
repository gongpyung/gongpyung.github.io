---
title: "노드 등록 (Scale-out)"
description: "새로운 노드를 등록합니다."
weight: 30
api_method: "POST"
api_endpoint: "/rest/nodes"
---

## POST /rest/nodes

새로운 노드를 등록합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `nodeName` | `string` | **Yes** | 노드명 |
| `systemName` | `string` | **Yes** | 시스템명 |
| `hostIp` | `string` | **Yes** | 호스트 IP |
| `agentPort` | `integer` | **Yes** | 에이전트 포트 |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/nodes?key=YOUR_API_KEY"
```
