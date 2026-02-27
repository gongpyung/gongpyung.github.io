# LENA REST API Inventory

> Source: `lena-manager/src/main/java/argo/manager/rest/controller/`
> Generated: 2026-02-27
> Total: **14 controllers, 81 user-facing endpoints**
> Excluded: 14 HA-internal + 5 session-based = 19 internal endpoints

## 1. 시스템 관리 (RestSystemController) — 5 endpoints

| # | Method | Path | 설명 |
|---|--------|------|------|
| 1 | GET | `/rest/systems` | 모든 시스템 목록 조회 |
| 2 | GET | `/rest/systems/{systemName}` | 시스템 상세 조회 |
| 3 | POST | `/rest/systems` | 시스템 생성 |
| 4 | PUT | `/rest/systems/{systemName}` | 시스템 수정 |
| 5 | DELETE | `/rest/systems/{systemName}` | 시스템 삭제 |

## 2. 노드 관리 (RestNodeController) — 6 endpoints

| # | Method | Path | 설명 |
|---|--------|------|------|
| 6 | GET | `/rest/nodes` | 모든 노드 목록 조회 |
| 7 | GET | `/rest/nodes/{nodeName}/systems/{systemName}` | 노드 상세 조회 |
| 8 | POST | `/rest/nodes` | 노드 생성/등록 |
| 9 | PUT | `/rest/nodes/{nodeName}/systems/{systemName}` | 노드 수정 |
| 10 | DELETE | `/rest/nodes/{nodeId}/systems/{systemName}` | 노드 삭제/해제 |
| 11 | GET | `/rest/public/nodes` | 노드 목록 조회 (Public) |

## 3. WAS 서버 관리 (RestApplicationServerController) — 16 endpoints

| # | Method | Path | 설명 |
|---|--------|------|------|
| 12 | GET | `/rest/was/servers` | 모든 WAS 서버 목록 조회 |
| 13 | GET | `/rest/was/container/servers` | 컨테이너 WAS 서버 목록 조회 |
| 14 | GET | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | WAS 서버 상세 조회 |
| 15 | POST | `/rest/was/servers` | WAS 서버 생성/등록 |
| 16 | GET | `/rest/was/servers/register/nodes/{nodeName}/systems/{systemName}` | 등록 가능 WAS 서버 목록 조회 |
| 17 | PUT | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | WAS 서버 수정 |
| 18 | DELETE | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | WAS 서버 삭제/해제 |
| 19 | POST | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action` | WAS 서버 시작/중지 |
| 20 | POST | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/session` | 세션 클러스터링 설정 |
| 21 | DELETE | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/session` | 세션 클러스터링 해제 |
| 22 | POST | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource` | 데이터소스 연결 |
| 23 | DELETE | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource` | 데이터소스 해제 |
| 24 | POST | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application` | 애플리케이션 배포 |
| 25 | DELETE | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application` | 애플리케이션 제거 |
| 26 | GET | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/applications/status` | 애플리케이션 상태 조회 |
| 27 | POST | `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/resource` | 리소스 매핑 |

## 4. 웹 서버 관리 (RestWebServerController) — 11 endpoints

| # | Method | Path | 설명 |
|---|--------|------|------|
| 28 | GET | `/rest/web/servers` | 모든 웹 서버 목록 조회 |
| 29 | GET | `/rest/web/container/servers` | 컨테이너 웹 서버 목록 조회 |
| 30 | GET | `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | 웹 서버 상세 조회 |
| 31 | POST | `/rest/web/servers` | 웹 서버 생성/등록 |
| 32 | GET | `/rest/web/servers/register/nodes/{nodeName}/systems/{systemName}` | 등록 가능 웹 서버 목록 조회 |
| 33 | PUT | `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | 웹 서버 수정 |
| 34 | DELETE | `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | 웹 서버 삭제/해제 |
| 35 | POST | `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action` | 웹 서버 시작/중지 |
| 36 | PUT | `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/worker` | 워커 설정 수정 |
| 37 | PUT | `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/uri` | URI/Rewrite 설정 수정 |
| 38 | POST | `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/ssl` | SSL 인증서 설정 |

## 5. 세션 서버 관리 (RestSessionServerController) — 7 endpoints

| # | Method | Path | 설명 |
|---|--------|------|------|
| 39 | GET | `/rest/session/servers` | 모든 세션 서버 목록 조회 |
| 40 | GET | `/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | 세션 서버 상세 조회 |
| 41 | POST | `/rest/session/servers` | 세션 서버 생성/등록 |
| 42 | GET | `/rest/session/servers/register/nodes/{nodeName}/systems/{systemName}` | 등록 가능 세션 서버 목록 조회 |
| 43 | PUT | `/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | 세션 서버 수정 |
| 44 | DELETE | `/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | 세션 서버 삭제/해제 |
| 45 | POST | `/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action` | 세션 서버 시작/중지 |

## 6. 메트릭 조회 (RestMetersController) — 8 endpoints

| # | Method | Path | 설명 |
|---|--------|------|------|
| 46 | GET | `/meters/nodes` | 노드 메트릭 목록 조회 |
| 47 | GET | `/meters/nodes/{nodeName}/systems/{systemName}` | 노드 메트릭 상세 조회 |
| 48 | GET | `/meters/nodes/{nodeName}/systems/{systemName}/all` | 노드 전체 메트릭 조회 (서버 포함) |
| 49 | GET | `/meters/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | 세션 서버 메트릭 조회 |
| 50 | GET | `/meters/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | WAS 서버 메트릭 조회 |
| 51 | GET | `/meters/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` | 웹 서버 메트릭 조회 |
| 52 | GET | `/meters/was/container/{hostName}` | WAS 컨테이너 메트릭 조회 |
| 53 | GET | `/meters/web/container/{hostName}` | 웹 컨테이너 메트릭 조회 |

## 7. 알림 관리 (RestNotificationController) — 1 endpoint

| # | Method | Path | 설명 |
|---|--------|------|------|
| 54 | GET | `/rest/notification` | 알림 목록 조회 |

## 8. 리소스 관리 (RestResourceController) — 9 endpoints

| # | Method | Path | 설명 |
|---|--------|------|------|
| 55 | GET | `/rest/resource/databases` | 데이터베이스 목록 조회 |
| 56 | GET | `/rest/resource/databases/{resourceName}` | 데이터베이스 상세 조회 |
| 57 | POST | `/rest/resource/databases` | 데이터베이스 생성 |
| 58 | DELETE | `/rest/resource/databases/{resourceName}` | 데이터베이스 삭제 |
| 59 | GET | `/rest/resource/datasources` | 데이터소스 목록 조회 |
| 60 | GET | `/rest/resource/datasources/{resourceName}` | 데이터소스 상세 조회 |
| 61 | POST | `/rest/resource/datasources` | 데이터소스 생성 |
| 62 | PUT | `/rest/resource/datasource/{resourceName}` | 데이터소스 업데이트 |
| 63 | DELETE | `/rest/resource/datasources/{resourceName}` | 데이터소스 삭제 |

## 9. 관리자 기능 (RestAdminController) — 14 endpoints

| # | Method | Path | 설명 |
|---|--------|------|------|
| 64 | GET | `/rest/admin/actionTraceLogList` | 액션 추적 로그 조회 |
| 65 | GET | `/rest/admin/users` | 사용자 목록 조회 |
| 66 | GET | `/rest/admin/user/{usrId}` | 사용자 상세 조회 |
| 67 | POST | `/rest/admin/user` | 사용자 생성 |
| 68 | PUT | `/rest/admin/user/{usrId}` | 사용자 수정 |
| 69 | DELETE | `/rest/admin/user/{usrId}` | 사용자 삭제 |
| 70 | GET | `/rest/admin/user/{usrId}/auth` | 사용자 역할 목록 조회 |
| 71 | POST | `/rest/admin/user/{usrId}/auth/grant` | 사용자 역할 부여 |
| 72 | POST | `/rest/admin/user/{usrId}/auth/revoke` | 사용자 역할 취소 |
| 73 | GET | `/rest/admin/auth` | 권한 목록 조회 |
| 74 | GET | `/rest/admin/auth/{authId}` | 권한 상세 조회 |
| 75 | POST | `/rest/admin/auth` | 권한 생성 |
| 76 | PUT | `/rest/admin/auth/{authId}` | 권한 수정 |
| 77 | DELETE | `/rest/admin/auth/{authId}` | 권한 삭제 |

## 10. 이벤트 분석 (RestAnlysisEventController) — 2 endpoints

| # | Method | Path | 설명 |
|---|--------|------|------|
| 78 | GET | `/rest/analysis/event` | 분석 이벤트 목록 조회 |
| 79 | GET | `/rest/analysis/event/{eventId}` | 분석 이벤트 상세 조회 |

## 11. 라이선스 관리 (RestLicenseController) — 1 endpoint

| # | Method | Path | 설명 |
|---|--------|------|------|
| 80 | GET | `/rest/licenses` | 라이선스 정보 목록 조회 |

## 12. 공개 API (RestPublicController) — 1 endpoint

| # | Method | Path | 설명 |
|---|--------|------|------|
| 81 | GET | `/rest/public/managerInfo` | 매니저 정보 조회 (인증 불필요) |

---

## 제외된 API (내부용)

### HA 동기화 (RestManagerHaSyncController) — 14 endpoints
- `@Profile({"ha-primary", "ha-secondary"})` 제한
- 매니저 간 내부 동기화 전용

### 서버 템플릿 (RestServerTemplateController) — 5 endpoints
- 세션 기반 인증 (API Key 미지원)
- 파일 다운로드 응답 (JSON 아님)
- 컨테이너 오케스트레이션 내부 전용
