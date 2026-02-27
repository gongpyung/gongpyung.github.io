---
title: "노드 삭제 (Scale-in)"
description: "노드를 삭제합니다."
weight: 50
api_method: "DELETE"
api_endpoint: "/rest/nodes/{nodeId}/systems/{systemName}"
---

## DELETE /rest/nodes/{nodeId}/systems/{systemName}

노드를 삭제합니다.

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
curl -X DELETE "https://{{manager-host}}:{{port}}/rest/nodes/{nodeId}/systems/{systemName}?key=YOUR_API_KEY"
```
