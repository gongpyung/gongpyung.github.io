---
title: "라이선스 목록 조회"
description: "모든 노드의 라이선스 정보를 조회합니다."
weight: 10
api_method: "GET"
api_endpoint: "/rest/licenses"
---

## GET /rest/licenses

모든 노드의 라이선스 정보를 조회합니다.

### Request
#### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

### Response

#### 200 OK

```json
{
  "licenses": [
    {
      "nodeName": "node-01",
      "licenseType": "Enterprise",
      "expireDate": "2027-12-31",
      "maxCpu": 16
    }
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
curl "https://{{manager-host}}:{{port}}/rest/licenses?key=YOUR_API_KEY"
```
