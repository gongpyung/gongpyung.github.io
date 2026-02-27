---
title: "노드 수정"
description: "노드 정보를 수정합니다."
weight: 40
api_method: "PUT"
api_endpoint: "/rest/nodes/{nodeId}/systems/{systemName}"
---

## PUT /rest/nodes/{nodeId}/systems/{systemName}

노드 정보를 수정합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `nodeId` | `string` | **Yes** | 노드 ID (Path) |
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
curl -X PUT "https://{{manager-host}}:{{port}}/rest/nodes/{nodeId}/systems/{systemName}?key=YOUR_API_KEY"
```
