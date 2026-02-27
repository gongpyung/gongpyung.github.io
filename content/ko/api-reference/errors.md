---
title: "에러 처리"
description: "LENA REST API의 공통 에러 코드와 처리 방법을 설명합니다."
weight: 3
---

## 에러 응답 형식

API 요청이 실패하면 다음과 같은 JSON 형식의 에러 응답이 반환됩니다:

```json
{
  "error": "에러에 대한 설명 메시지",
  "code": "ERROR_CODE"
}
```

## HTTP 상태 코드

| 상태 코드 | 설명 | 일반적인 원인 |
|----------|------|-------------|
| `400` | Bad Request | 필수 파라미터 누락, 잘못된 파라미터 형식 |
| `401` | Unauthorized | API Key 누락 또는 유효하지 않은 API Key |
| `403` | Forbidden | 해당 리소스에 대한 접근 권한 없음 |
| `404` | Not Found | 요청한 리소스가 존재하지 않음 |
| `409` | Conflict | 중복된 리소스 (예: 동일한 시스템명 생성 시도) |
| `500` | Internal Server Error | 서버 내부 오류 |

## 주요 에러 시나리오

### 400 Bad Request

필수 파라미터가 누락되었거나 유효성 검사에 실패한 경우:

```bash
# 시스템명 없이 생성 요청
curl -X POST "https://{manager-host}:{port}/rest/systems?key=YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

```json
{
  "error": "systemName is required",
  "code": "BAD_REQUEST"
}
```

### 401 Unauthorized

API Key가 누락되거나 유효하지 않은 경우:

```bash
# API Key 없이 요청
curl -X GET "https://{manager-host}:{port}/rest/systems"
```

```json
{
  "error": "Unauthorized",
  "code": "UNAUTHORIZED"
}
```

### 404 Not Found

존재하지 않는 리소스를 조회한 경우:

```bash
curl -X GET "https://{manager-host}:{port}/rest/systems/NonExistentSystem?key=YOUR_API_KEY"
```

```json
{
  "error": "System not found: NonExistentSystem",
  "code": "NOT_FOUND"
}
```

### 409 Conflict

이미 존재하는 리소스를 생성하려는 경우:

```bash
curl -X POST "https://{manager-host}:{port}/rest/systems?key=YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"systemName": "Production"}'
```

```json
{
  "error": "System already exists: Production",
  "code": "CONFLICT"
}
```

## 작업 결과 확인

서버 생성, 수정, 삭제 등의 작업은 `ActionResult` 형식으로 결과를 반환합니다:

```json
{
  "actionResult": "Y"
}
```

| 값 | 설명 |
|----|------|
| `Y` | 작업 성공 |
| `N` | 작업 실패 |

작업 실패 시 에러 메시지가 함께 반환될 수 있습니다.

## 에러 처리 권장사항

- 모든 API 응답의 HTTP 상태 코드를 확인하십시오.
- `4xx` 에러는 요청을 수정하여 재시도하십시오.
- `5xx` 에러는 잠시 후 재시도하거나 관리자에게 문의하십시오.
- `actionResult`가 `N`인 경우 요청 파라미터와 서버 상태를 확인하십시오.
