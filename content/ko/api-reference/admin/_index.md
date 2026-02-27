---
title: "관리자 기능"
description: "사용자 계정, 권한(Role), 액션 추적 로그를 관리합니다."
weight: 90
---

사용자 계정, 권한(Role), 액션 추적 로그를 관리합니다.

## 엔드포인트

- **GET** `/rest/admin/actionTraceLogList` — 액션 추적 로그 조회
- **GET** `/rest/admin/users` — 사용자 목록 조회
- **GET** `/rest/admin/user/{usrId}` — 사용자 상세 조회
- **POST** `/rest/admin/user` — 사용자 생성
- **PUT** `/rest/admin/user/{usrId}` — 사용자 수정
- **DELETE** `/rest/admin/user/{usrId}` — 사용자 삭제
- **POST** `/rest/admin/user/{usrId}/auth/grant` — 사용자 역할 부여
- **POST** `/rest/admin/user/{usrId}/auth/revoke` — 사용자 역할 취소
- **GET** `/rest/admin/auth` — 권한 목록 조회
- **POST** `/rest/admin/auth` — 권한 생성
- **GET** `/rest/admin/user/{usrId}/auth` — 사용자 역할 목록 조회
- **GET** `/rest/admin/auth/{authId}` — 권한 상세 조회
- **PUT** `/rest/admin/auth/{authId}` — 권한 수정
- **DELETE** `/rest/admin/auth/{authId}` — 권한 삭제

