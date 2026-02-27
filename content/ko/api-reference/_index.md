---
title: "API Reference"
description: "LENA REST API 레퍼런스 문서"
weight: 30
---

LENA Manager는 시스템, 노드, 서버를 관리하고 모니터링하기 위한 REST API를 제공합니다. 이 문서에서는 사용 가능한 모든 API 엔드포인트와 요청/응답 형식을 설명합니다.

## Base URL

모든 API 요청의 기본 URL은 다음과 같습니다:

```
https://{{manager-host}}:{{port}}
```

`{{manager-host}}`와 `{{port}}`는 LENA Manager가 설치된 서버의 호스트명과 포트 번호로 대체합니다.

## 인증

모든 API 요청에는 API Key를 쿼리 파라미터로 포함해야 합니다 (공개 API 제외).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

```bash
# 예시: API Key를 쿼리 파라미터로 전달
curl -X GET "https://{{manager-host}}:{{port}}/rest/systems?key=YOUR_API_KEY"
```

## 공통 응답 형식

### 성공 응답 (ActionResult)

작업 수행 결과는 `ActionResult` 형식으로 반환됩니다:

```json
{{
  "actionResult": "Y"
}}
```

| 값 | 설명 |
|----|------|
| `Y` | 작업 성공 |
| `N` | 작업 실패 |

### 에러 응답

```json
{{
  "error": "에러 메시지",
  "code": "ERROR_CODE"
}}
```

## HTTP 상태 코드

| 코드 | 설명 |
|------|------|
| `200` | 성공 |
| `201` | 생성 성공 |
| `400` | 잘못된 요청 (파라미터 오류) |
| `401` | 인증 실패 (유효하지 않은 API Key) |
| `403` | 권한 없음 |
| `404` | 리소스를 찾을 수 없음 |
| `409` | 충돌 (중복된 리소스) |
| `500` | 서버 내부 오류 |

## API 카테고리

| 카테고리 | 설명 | 엔드포인트 수 |
|---------|------|:----------:|
| [시스템 관리](/api-reference/system/) | 시스템의 생성, 조회, 수정, 삭제를 관리합니다. | 5 |
| [노드 관리](/api-reference/node/) | 노드의 등록, 조회, 수정, 삭제(Scale-out/in)를 관리합니다. | 6 |
| [WAS 서버 관리](/api-reference/was-server/) | WAS(Web Application Server) 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다. | 16 |
| [웹 서버 관리](/api-reference/web-server/) | 웹 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다. | 11 |
| [세션 서버 관리](/api-reference/session-server/) | 세션 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다. | 7 |
| [메트릭 조회](/api-reference/metrics/) | 노드 및 서버의 실시간 메트릭(CPU, Memory, JVM, Thread 등)을 조회합니다. | 8 |
| [알림 관리](/api-reference/notification/) | 시스템 이벤트 알림을 조회합니다. | 1 |
| [리소스 관리](/api-reference/resource/) | 데이터베이스 및 데이터소스 리소스를 관리합니다. | 9 |
| [관리자 기능](/api-reference/admin/) | 사용자 계정, 권한(Role), 액션 추적 로그를 관리합니다. | 14 |
| [이벤트 분석](/api-reference/event-analysis/) | Stuck Thread, OOM, Full GC 등 서버 이벤트를 분석합니다. | 2 |
| [라이선스 관리](/api-reference/license/) | LENA 라이선스 정보를 조회합니다. | 1 |
| [공개 API](/api-reference/public/) | 인증 없이 접근 가능한 공개 API입니다. | 1 |

