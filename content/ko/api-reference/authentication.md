---
title: "인증"
description: "LENA REST API의 인증 방식을 설명합니다."
weight: 2
---

## 인증 방식

LENA REST API는 **API Key** 기반 인증을 사용합니다. 모든 API 요청에 유효한 API Key를 포함해야 합니다.

### API Key 전달 방법

API Key는 쿼리 파라미터 `key`로 전달합니다:

```
https://{manager-host}:{port}/rest/systems?key=YOUR_API_KEY
```

### 요청 예시

```bash
# 시스템 목록 조회
curl -X GET "https://{manager-host}:{port}/rest/systems?key=YOUR_API_KEY"

# 다른 쿼리 파라미터와 함께 사용
curl -X GET "https://{manager-host}:{port}/rest/notification?interval=30&key=YOUR_API_KEY"
```

### 인증 실패 응답

API Key가 누락되거나 유효하지 않은 경우 `401 Unauthorized` 응답이 반환됩니다:

```json
{
  "error": "Unauthorized",
  "code": "UNAUTHORIZED"
}
```

### 권한 부족 응답

유효한 API Key이지만 해당 리소스에 대한 접근 권한이 없는 경우 `403 Forbidden` 응답이 반환됩니다:

```json
{
  "error": "Access denied",
  "code": "FORBIDDEN"
}
```

### 공개 API

일부 API는 인증 없이 접근할 수 있습니다. 공개 API의 Base Path는 `/rest/public`입니다.

```bash
# 인증 없이 매니저 정보 조회
curl -X GET "https://{manager-host}:{port}/rest/public/managerInfo"
```

### 보안 권장사항

- API Key를 코드에 직접 하드코딩하지 마십시오. 환경 변수를 사용하십시오.
- HTTPS를 통해 통신하여 API Key가 네트워크상에서 노출되지 않도록 하십시오.
- 사용하지 않는 API Key는 즉시 폐기하십시오.
