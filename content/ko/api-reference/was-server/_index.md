---
title: "WAS 서버 관리"
description: "WAS(Web Application Server) 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다."
weight: 30
---

WAS(Web Application Server) 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다.

## 엔드포인트

- **GET** `/rest/was/servers` — 모든 WAS 서버 조회
- **GET** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — WAS 서버 상세 조회
- **POST** `/rest/was/servers` — WAS 서버 설치/등록
- **PUT** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — WAS 서버 수정
- **DELETE** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — WAS 서버 삭제/해제
- **POST** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action` — WAS 서버 제어 (시작/중지)
- **POST** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/session` — 세션 클러스터링 설정
- **DELETE** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/session` — 세션 클러스터링 해제
- **POST** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource` — 데이터소스 연결
- **DELETE** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource` — 데이터소스 해제
- **POST** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application` — 애플리케이션 배포
- **DELETE** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application` — 애플리케이션 배포 해제
- **GET** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/applications/status` — 애플리케이션 상태 조회
- **GET** `/rest/was/container/servers` — 컨테이너 WAS 서버 목록 조회
- **GET** `/rest/was/servers/register/nodes/{nodeName}/systems/{systemName}` — 등록 가능 WAS 서버 목록 조회
- **POST** `/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/resource` — WAS 리소스 가져오기

