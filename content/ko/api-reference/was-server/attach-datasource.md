---
title: "데이터소스 연결"
description: "WAS 서버에 데이터소스를 연결합니다."
weight: 90
api_method: "POST"
api_endpoint: "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource"
---

## POST /rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource

WAS 서버에 데이터소스를 연결합니다.

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
| `resourceName` | `string` | **Yes** | 데이터소스 리소스명 |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource?key=YOUR_API_KEY"
```
