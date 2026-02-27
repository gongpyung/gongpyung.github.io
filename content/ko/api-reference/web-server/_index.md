---
title: "웹 서버 관리"
description: "웹 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다."
weight: 40
---

웹 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다.

## 엔드포인트

- **GET** `/rest/web/servers` — 모든 웹 서버 조회
- **GET** `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — 웹 서버 상세 조회
- **POST** `/rest/web/servers` — 웹 서버 설치/등록
- **PUT** `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — 웹 서버 수정
- **DELETE** `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — 웹 서버 삭제/해제
- **POST** `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action` — 웹 서버 제어 (시작/중지)
- **PUT** `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/worker` — 로드밸런서 워커 설정
- **POST** `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/ssl` — SSL 설정
- **GET** `/rest/web/container/servers` — 컨테이너 웹 서버 목록 조회
- **GET** `/rest/web/servers/register/nodes/{nodeName}/systems/{systemName}` — 등록 가능 웹 서버 목록 조회
- **PUT** `/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/uri` — URI/Rewrite 설정 수정

