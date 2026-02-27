---
title: "세션 서버 관리"
description: "세션 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다."
weight: 50
---

세션 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다.

## 엔드포인트

- **GET** `/rest/session/servers` — 모든 세션 서버 조회
- **GET** `/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — 세션 서버 상세 조회
- **POST** `/rest/session/servers` — 세션 서버 설치/등록
- **DELETE** `/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — 세션 서버 삭제/해제
- **POST** `/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action` — 세션 서버 제어 (시작/중지)
- **GET** `/rest/session/servers/register/nodes/{nodeName}/systems/{systemName}` — 등록 가능 세션 서버 목록 조회
- **PUT** `/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — 세션 서버 수정

