---
title: "WAS 서버 메트릭 조회"
description: "특정 WAS 서버의 메트릭(JVM Heap, Thread, GC 등)을 조회합니다."
weight: 40
api_method: "GET"
api_endpoint: "/meters/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}"
---

## GET /meters/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}

특정 WAS 서버의 메트릭(JVM Heap, Thread, GC 등)을 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `serverId` | `string` | **Yes** | 서버 ID (Path) |
| `nodeName` | `string` | **Yes** | 노드명 (Path) |
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "serverId": "was-01",
  "heapUsed": 512,
  "heapMax": 1024,
  "threadActive": 25,
  "threadMax": 200,
  "gcCount": 142,
  "gcTime": 1250
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
curl "https://{{manager-host}}:{{port}}/meters/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}?key=YOUR_API_KEY"
```
