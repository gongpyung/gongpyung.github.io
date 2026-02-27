---
title: "노드 관리"
description: "노드의 등록, 조회, 수정, 삭제(Scale-out/in)를 관리합니다."
weight: 20
---

노드의 등록, 조회, 수정, 삭제(Scale-out/in)를 관리합니다.

## 엔드포인트

- **GET** `/rest/nodes` — 모든 노드 조회
- **GET** `/rest/nodes/{nodeName}/systems/{systemName}` — 노드 상세 조회
- **POST** `/rest/nodes` — 노드 등록 (Scale-out)
- **PUT** `/rest/nodes/{nodeId}/systems/{systemName}` — 노드 수정
- **DELETE** `/rest/nodes/{nodeId}/systems/{systemName}` — 노드 삭제 (Scale-in)
- **GET** `/rest/public/nodes` — [Public] 노드 목록 조회

