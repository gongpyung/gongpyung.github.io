---
title: "메트릭 조회"
description: "노드 및 서버의 실시간 메트릭(CPU, Memory, JVM, Thread 등)을 조회합니다."
weight: 60
---

노드 및 서버의 실시간 메트릭(CPU, Memory, JVM, Thread 등)을 조회합니다.

## 엔드포인트

- **GET** `/meters/nodes` — 모든 노드 메트릭 조회
- **GET** `/meters/nodes/{nodeName}/systems/{systemName}` — 특정 노드 메트릭 조회
- **GET** `/meters/nodes/{nodeName}/systems/{systemName}/all` — 노드 전체 메트릭 조회 (서버 포함)
- **GET** `/meters/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — WAS 서버 메트릭 조회
- **GET** `/meters/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — 웹 서버 메트릭 조회
- **GET** `/meters/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}` — 세션 서버 메트릭 조회
- **GET** `/meters/was/container/{hostName}` — WAS 컨테이너 메트릭 조회
- **GET** `/meters/web/container/{hostName}` — 웹 컨테이너 메트릭 조회

