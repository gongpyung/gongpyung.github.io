---
title: "WAS 리소스 가져오기"
description: "LENA에 등록된 리소스를 WAS 서버로 가져옵니다. 데이터소스, 애플리케이션, JMS, JTA 리소스를 지원합니다."
weight: 160
api_method: "POST"
api_endpoint: "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/resource"
---

## POST /rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/resource

LENA에 등록된 리소스를 WAS 서버로 가져옵니다. 데이터소스, 애플리케이션, JMS, JTA 리소스를 지원합니다.

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
| `resourceType` | `string` | **Yes** | 리소스 타입 (`datasource`, `application`, `jms`, `jta`) |
| `resourceName` | `string` | **Yes** | 리소스명 |

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
curl -X POST "https://{{manager-host}}:{{port}}/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/resource?key=YOUR_API_KEY"
```
