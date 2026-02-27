---
title: "시작하기"
description: "LENA REST API를 빠르게 시작하는 방법을 안내합니다."
weight: 1
---

## 시작하기

LENA REST API를 사용하면 LENA Manager의 모든 기능을 프로그래밍 방식으로 제어할 수 있습니다. 이 가이드에서는 첫 번째 API 호출을 수행하는 방법을 안내합니다.

### 사전 요구사항

- LENA Manager가 설치 및 실행 중이어야 합니다
- API Key가 발급되어 있어야 합니다
- LENA Manager의 호스트 주소와 포트 번호를 알고 있어야 합니다

### 첫 번째 API 호출

시스템 목록을 조회하여 API가 정상 작동하는지 확인합니다:

```bash
curl -X GET "https://{manager-host}:{port}/rest/systems?key=YOUR_API_KEY"
```

정상 응답 예시:

```json
{
  "systems": [
    {
      "systemId": "sys001",
      "systemName": "Production",
      "nodeCount": 5,
      "webCount": 2,
      "appCount": 10,
      "sessionCount": 2,
      "cacheCount": 0
    }
  ]
}
```

### 인증 확인

API Key가 유효하지 않으면 `401 Unauthorized` 응답이 반환됩니다:

```json
{
  "error": "Unauthorized",
  "code": "UNAUTHORIZED"
}
```

### 주요 워크플로우

#### 서버 생성 및 시작

1. **시스템 조회**: `GET /rest/systems` -- 대상 시스템 확인
2. **노드 조회**: `GET /rest/nodes` -- 서버를 설치할 노드 확인
3. **서버 설치**: `POST /rest/was/servers` -- WAS 서버 설치
4. **서버 시작**: `POST /rest/was/servers/{serverId}/.../action` -- 서버 시작

#### 모니터링

1. **노드 메트릭 조회**: `GET /meters/nodes` -- 전체 노드 상태 확인
2. **서버 메트릭 조회**: `GET /meters/was/servers/{serverId}/...` -- 개별 서버 상태 확인
3. **알림 조회**: `GET /rest/notification` -- 시스템 알림 확인

### 다음 단계

- [인증 방식 상세](/ko/api-reference/authentication/) -- API Key 인증에 대한 자세한 설명
- [에러 처리](/ko/api-reference/errors/) -- 공통 에러 코드 및 처리 방법
- [서버 관리 API](/ko/api-reference/server-management/) -- 시스템, 노드, 서버 관리
