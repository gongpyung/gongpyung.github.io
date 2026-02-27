---
title: "노드 전체 메트릭 조회 (서버 포함)"
description: "노드와 소속 서버의 전체 메트릭을 일괄 조회합니다."
weight: 30
api_method: "GET"
api_endpoint: "/meters/nodes/{nodeName}/systems/{systemName}/all"
---

## GET /meters/nodes/{nodeName}/systems/{systemName}/all

노드와 소속 서버의 전체 메트릭을 일괄 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `nodeName` | `string` | **Yes** | 노드명 (Path) |
| `systemName` | `string` | **Yes** | 시스템명 (Path) |
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "node": {"cpu": 45.2, "memoryUsed": 4096},
  "wasServers": [
    {"serverId": "was-01", "heapUsed": 512, "heapMax": 1024, "threadActive": 25}
  ],
  "webServers": [
    {"serverId": "web-01", "connections": 150}
  ]
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
curl "https://{{manager-host}}:{{port}}/meters/nodes/{nodeName}/systems/{systemName}/all?key=YOUR_API_KEY"
```
