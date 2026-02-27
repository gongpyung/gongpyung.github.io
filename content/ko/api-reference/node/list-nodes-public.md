---
title: "[Public] 노드 목록 조회"
description: "인증 없이 노드 목록을 조회합니다. 테스트 목적으로 더미 데이터를 반환하며, 실제 운영 환경에서는 사용하지 마세요."
weight: 60
api_method: "GET"
api_endpoint: "/rest/public/nodes"
---

## GET /rest/public/nodes

인증 없이 노드 목록을 조회합니다. 테스트 목적으로 더미 데이터를 반환하며, 실제 운영 환경에서는 사용하지 마세요.

### Request
이 엔드포인트는 추가 파라미터가 필요하지 않습니다.

### Response

#### 200 OK

```json
{
  "nodeList": [
    {
      "nodeId": "demo-node-1",
      "nodeName": "Demo Node 1",
      "systemName": "Demo System",
      "connectionStatus": "connected",
      "ipAddress": "192.168.1.100"
    }
  ]
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `nodeId` | `string` | 노드 고유 ID |
| `nodeName` | `string` | 노드명 |
| `systemName` | `string` | 시스템명 |
| `connectionStatus` | `string` | 연결 상태 (connected/disconnected) |
| `ipAddress` | `string` | IP 주소 |

#### 401 Unauthorized

```json
{
  "error": "Unauthorized",
  "code": "UNAUTHORIZED"
}
```

### Example

```bash
curl "https://{{manager-host}}:{{port}}/rest/public/nodes"
```
