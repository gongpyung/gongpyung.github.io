---
title: "시스템 삭제"
description: "시스템을 삭제합니다. 하위 노드가 없어야 삭제 가능합니다."
weight: 50
api_method: "DELETE"
api_endpoint: "/rest/systems/{systemName}"
---

## DELETE /rest/systems/{systemName}

시스템을 삭제합니다. 하위 노드가 없어야 삭제 가능합니다.

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
curl -X DELETE "https://{{manager-host}}:{{port}}/rest/systems/{systemName}?key=YOUR_API_KEY"
```
