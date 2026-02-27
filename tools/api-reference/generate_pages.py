#!/usr/bin/env python3
"""
LENA API Reference Markdown Generator
Generates all endpoint documentation from embedded API inventory data.
"""

import os
import shutil
import json

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "content", "ko", "api-reference")

# ──────────────────────────────────────────────
# API Inventory Data (extracted from Java source)
# ──────────────────────────────────────────────

CATEGORIES = [
    {
        "slug": "system",
        "title": "시스템 관리",
        "description": "시스템의 생성, 조회, 수정, 삭제를 관리합니다.",
        "weight": 10,
        "controller": "RestSystemController",
        "endpoints": [
            {"slug": "list-systems", "title": "모든 시스템 조회", "desc": "사용자가 접근 가능한 모든 시스템 목록을 조회합니다.", "method": "GET", "path": "/rest/systems", "weight": 10,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_fields": [
                 {"name": "systemId", "type": "string", "desc": "시스템 고유 ID"},
                 {"name": "systemName", "type": "string", "desc": "시스템명"},
                 {"name": "nodeCount", "type": "integer", "desc": "소속 노드 수"},
                 {"name": "webCount", "type": "integer", "desc": "웹 서버 수"},
                 {"name": "appCount", "type": "integer", "desc": "WAS 서버 수"},
                 {"name": "sessionCount", "type": "integer", "desc": "세션 서버 수"},
             ],
             "response_example": '{\n  "systems": [\n    {\n      "systemId": "sys001",\n      "systemName": "Production",\n      "nodeCount": 5,\n      "webCount": 2,\n      "appCount": 10,\n      "sessionCount": 2\n    }\n  ]\n}'},
            {"slug": "get-system", "title": "시스템 상세 조회", "desc": "특정 시스템의 상세 정보를 조회합니다.", "method": "GET", "path": "/rest/systems/{systemName}", "weight": 20,
             "params": [
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_fields": [
                 {"name": "systemId", "type": "string", "desc": "시스템 고유 ID"},
                 {"name": "systemName", "type": "string", "desc": "시스템명"},
                 {"name": "nodes", "type": "array", "desc": "소속 노드 목록"},
             ],
             "response_example": '{\n  "systemId": "sys001",\n  "systemName": "Production",\n  "nodes": [\n    {\n      "nodeName": "node-01",\n      "hostIp": "10.0.1.10",\n      "status": "running"\n    }\n  ]\n}'},
            {"slug": "create-system", "title": "시스템 생성", "desc": "새로운 시스템을 생성합니다.", "method": "POST", "path": "/rest/systems", "weight": 30,
             "params": [
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (영숫자, -, _ / 최대 20자)"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "modify-system", "title": "시스템 수정", "desc": "시스템 정보를 수정합니다.", "method": "PUT", "path": "/rest/systems/{systemName}", "weight": 40,
             "params": [
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [
                 {"name": "systemName", "type": "string", "required": False, "desc": "변경할 시스템명"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "delete-system", "title": "시스템 삭제", "desc": "시스템을 삭제합니다. 하위 노드가 없어야 삭제 가능합니다.", "method": "DELETE", "path": "/rest/systems/{systemName}", "weight": 50,
             "params": [
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
        ],
    },
    {
        "slug": "node",
        "title": "노드 관리",
        "description": "노드의 등록, 조회, 수정, 삭제(Scale-out/in)를 관리합니다.",
        "weight": 20,
        "controller": "RestNodeController",
        "endpoints": [
            {"slug": "list-nodes", "title": "모든 노드 조회", "desc": "등록된 모든 노드 목록을 조회합니다.", "method": "GET", "path": "/rest/nodes", "weight": 10,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_example": '{\n  "nodes": [\n    {\n      "nodeName": "node-01",\n      "systemName": "Production",\n      "hostIp": "10.0.1.10",\n      "agentPort": 7700,\n      "status": "running"\n    }\n  ]\n}'},
            {"slug": "get-node", "title": "노드 상세 조회", "desc": "특정 노드의 상세 정보를 조회합니다.", "method": "GET", "path": "/rest/nodes/{nodeName}/systems/{systemName}", "weight": 20,
             "params": [
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "nodeName": "node-01",\n  "systemName": "Production",\n  "hostIp": "10.0.1.10",\n  "agentPort": 7700,\n  "status": "running",\n  "servers": [\n    {"serverId": "was-01", "serverType": "WAS", "status": "running"}\n  ]\n}'},
            {"slug": "create-node", "title": "노드 등록 (Scale-out)", "desc": "새로운 노드를 등록합니다.", "method": "POST", "path": "/rest/nodes", "weight": 30,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "body_params": [
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명"},
                 {"name": "hostIp", "type": "string", "required": True, "desc": "호스트 IP"},
                 {"name": "agentPort", "type": "integer", "required": True, "desc": "에이전트 포트"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "modify-node", "title": "노드 수정", "desc": "노드 정보를 수정합니다.", "method": "PUT", "path": "/rest/nodes/{nodeId}/systems/{systemName}", "weight": 40,
             "params": [
                 {"name": "nodeId", "type": "string", "required": True, "desc": "노드 ID (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "delete-node", "title": "노드 삭제 (Scale-in)", "desc": "노드를 삭제합니다.", "method": "DELETE", "path": "/rest/nodes/{nodeId}/systems/{systemName}", "weight": 50,
             "params": [
                 {"name": "nodeId", "type": "string", "required": True, "desc": "노드 ID (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "list-nodes-public", "title": "[Public] 노드 목록 조회", "desc": "인증 없이 노드 목록을 조회합니다. 테스트 목적으로 더미 데이터를 반환하며, 실제 운영 환경에서는 사용하지 마세요.", "method": "GET", "path": "/rest/public/nodes", "weight": 60,
             "params": [],
             "response_fields": [
                 {"name": "nodeId", "type": "string", "desc": "노드 고유 ID"},
                 {"name": "nodeName", "type": "string", "desc": "노드명"},
                 {"name": "systemName", "type": "string", "desc": "시스템명"},
                 {"name": "connectionStatus", "type": "string", "desc": "연결 상태 (connected/disconnected)"},
                 {"name": "ipAddress", "type": "string", "desc": "IP 주소"},
             ],
             "response_example": '{\n  "nodeList": [\n    {\n      "nodeId": "demo-node-1",\n      "nodeName": "Demo Node 1",\n      "systemName": "Demo System",\n      "connectionStatus": "connected",\n      "ipAddress": "192.168.1.100"\n    }\n  ]\n}'},
        ],
    },
    {
        "slug": "was-server",
        "title": "WAS 서버 관리",
        "description": "WAS(Web Application Server) 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다.",
        "weight": 30,
        "controller": "RestApplicationServerController",
        "endpoints": [
            {"slug": "list-was-servers", "title": "모든 WAS 서버 조회", "desc": "등록된 모든 WAS 서버 목록을 조회합니다.", "method": "GET", "path": "/rest/was/servers", "weight": 10,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_example": '{\n  "servers": [\n    {\n      "serverId": "was-01",\n      "nodeName": "node-01",\n      "systemName": "Production",\n      "httpPort": 8080,\n      "serverType": "S",\n      "status": "running"\n    }\n  ]\n}'},
            {"slug": "get-was-server", "title": "WAS 서버 상세 조회", "desc": "특정 WAS 서버의 상세 정보를 조회합니다.", "method": "GET", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 20,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "serverId": "was-01",\n  "nodeName": "node-01",\n  "systemName": "Production",\n  "httpPort": 8080,\n  "ajpPort": 8009,\n  "serverType": "S",\n  "status": "running",\n  "javaHome": "/usr/lib/jvm/java-8",\n  "installRootPath": "/app/lena/servers/was-01"\n}'},
            {"slug": "create-was-server", "title": "WAS 서버 설치/등록", "desc": "WAS 서버를 설치하거나 기존 서버를 등록합니다.", "method": "POST", "path": "/rest/was/servers", "weight": 30,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "body_params": [
                 {"name": "type", "type": "string", "required": True, "desc": "작업 유형 (`install` 또는 `register`)"},
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명"},
                 {"name": "httpPort", "type": "integer", "required": True, "desc": "HTTP 포트"},
                 {"name": "ajpPort", "type": "integer", "required": False, "desc": "AJP 포트"},
                 {"name": "serverType", "type": "string", "required": False, "desc": "서버 타입 (`S`: Standard, `E`: Enterprise)"},
                 {"name": "installRootPath", "type": "string", "required": False, "desc": "설치 경로 (install 타입 시)"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "modify-was-server", "title": "WAS 서버 수정", "desc": "WAS 서버 설정을 수정합니다.", "method": "PUT", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 40,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "delete-was-server", "title": "WAS 서버 삭제/해제", "desc": "WAS 서버를 삭제(uninstall)하거나 등록 해제(deregister)합니다.", "method": "DELETE", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 50,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "type", "type": "string", "required": True, "desc": "작업 유형 (`uninstall` 또는 `deregister`)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "control-was-server", "title": "WAS 서버 제어 (시작/중지)", "desc": "WAS 서버를 시작하거나 중지합니다.", "method": "POST", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action", "weight": 60,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [
                 {"name": "action", "type": "string", "required": True, "desc": "액션 (`start` 또는 `stop`)"},
                 {"name": "force", "type": "boolean", "required": False, "desc": "강제 중지 여부"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "setup-session-clustering", "title": "세션 클러스터링 설정", "desc": "WAS 서버에 세션 클러스터링을 설정합니다.", "method": "POST", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/session", "weight": 70,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "remove-session-clustering", "title": "세션 클러스터링 해제", "desc": "WAS 서버의 세션 클러스터링을 해제합니다.", "method": "DELETE", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/session", "weight": 80,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "attach-datasource", "title": "데이터소스 연결", "desc": "WAS 서버에 데이터소스를 연결합니다.", "method": "POST", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource", "weight": 90,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [
                 {"name": "resourceName", "type": "string", "required": True, "desc": "데이터소스 리소스명"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "detach-datasource", "title": "데이터소스 해제", "desc": "WAS 서버에서 데이터소스를 해제합니다.", "method": "DELETE", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/datasource", "weight": 100,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "resourceName", "type": "string", "required": True, "desc": "데이터소스 리소스명"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "deploy-application", "title": "애플리케이션 배포", "desc": "WAS 서버에 애플리케이션을 배포합니다.", "method": "POST", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application", "weight": 110,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "undeploy-application", "title": "애플리케이션 배포 해제", "desc": "WAS 서버에서 애플리케이션을 배포 해제합니다.", "method": "DELETE", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/application", "weight": 120,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "get-application-status", "title": "애플리케이션 상태 조회", "desc": "WAS 서버에 배포된 애플리케이션의 상태를 조회합니다.", "method": "GET", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/applications/status", "weight": 130,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "applications": [\n    {\n      "contextPath": "/myapp",\n      "status": "running",\n      "sessions": 42\n    }\n  ]\n}'},
            {"slug": "list-was-container-servers", "title": "컨테이너 WAS 서버 목록 조회", "desc": "컨테이너 그룹에 속한 WAS 서버 목록을 조회합니다. 컨테이너 IP, HTTP 포트 정보를 포함합니다.", "method": "GET", "path": "/rest/was/container/servers", "weight": 140,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_fields": [
                 {"name": "serverId", "type": "string", "desc": "서버 ID"},
                 {"name": "serverName", "type": "string", "desc": "서버명"},
                 {"name": "containerIp", "type": "string", "desc": "컨테이너 IP"},
                 {"name": "httpPort", "type": "integer", "desc": "HTTP 포트"},
             ],
             "response_example": '{\n  "containerList": [\n    {\n      "serverId": "was-01",\n      "serverName": "WAS Server 01",\n      "containerIp": "172.17.0.2",\n      "httpPort": 8080\n    }\n  ]\n}'},
            {"slug": "list-was-registerable", "title": "등록 가능 WAS 서버 목록 조회", "desc": "지정된 시스템의 노드에서 등록 가능한 WAS 서버 목록을 조회합니다. 아직 LENA에 등록되지 않은 서버들을 반환합니다.", "method": "GET", "path": "/rest/was/servers/register/nodes/{nodeName}/systems/{systemName}", "weight": 150,
             "params": [
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_fields": [
                 {"name": "systemName", "type": "string", "desc": "시스템명"},
                 {"name": "nodeName", "type": "string", "desc": "노드명"},
                 {"name": "serverId", "type": "string", "desc": "서버 ID"},
                 {"name": "serverIp", "type": "string", "desc": "서버 IP"},
                 {"name": "serverType", "type": "string", "desc": "서버 타입 (Standard/Enterprise)"},
                 {"name": "httpPort", "type": "integer", "desc": "HTTP 포트"},
                 {"name": "ajpPort", "type": "integer", "desc": "AJP 포트"},
             ],
             "response_example": '{\n  "noRegisterdServers": [\n    {\n      "systemName": "Production",\n      "nodeName": "node-01",\n      "serverId": "was-03",\n      "serverIp": "10.0.1.10",\n      "serverType": "Standard",\n      "httpPort": 8082,\n      "ajpPort": 8011\n    }\n  ]\n}'},
            {"slug": "import-resource", "title": "WAS 리소스 가져오기", "desc": "LENA에 등록된 리소스를 WAS 서버로 가져옵니다. 데이터소스, 애플리케이션, JMS, JTA 리소스를 지원합니다.", "method": "POST", "path": "/rest/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/resource", "weight": 160,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [
                 {"name": "resourceType", "type": "string", "required": True, "desc": "리소스 타입 (`datasource`, `application`, `jms`, `jta`)"},
                 {"name": "resourceName", "type": "string", "required": True, "desc": "리소스명"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
        ],
    },
    {
        "slug": "web-server",
        "title": "웹 서버 관리",
        "description": "웹 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다.",
        "weight": 40,
        "controller": "RestWebServerController",
        "endpoints": [
            {"slug": "list-web-servers", "title": "모든 웹 서버 조회", "desc": "등록된 모든 웹 서버 목록을 조회합니다.", "method": "GET", "path": "/rest/web/servers", "weight": 10,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_example": '{\n  "servers": [\n    {\n      "serverId": "web-01",\n      "nodeName": "node-01",\n      "systemName": "Production",\n      "httpPort": 80,\n      "status": "running"\n    }\n  ]\n}'},
            {"slug": "get-web-server", "title": "웹 서버 상세 조회", "desc": "특정 웹 서버의 상세 정보를 조회합니다.", "method": "GET", "path": "/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 20,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "serverId": "web-01",\n  "nodeName": "node-01",\n  "systemName": "Production",\n  "httpPort": 80,\n  "httpsPort": 443,\n  "status": "running",\n  "installRootPath": "/app/lena/servers/web-01"\n}'},
            {"slug": "create-web-server", "title": "웹 서버 설치/등록", "desc": "웹 서버를 설치하거나 기존 서버를 등록합니다.", "method": "POST", "path": "/rest/web/servers", "weight": 30,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "body_params": [
                 {"name": "type", "type": "string", "required": True, "desc": "작업 유형 (`install` 또는 `register`)"},
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명"},
                 {"name": "httpPort", "type": "integer", "required": True, "desc": "HTTP 포트"},
                 {"name": "httpsPort", "type": "integer", "required": False, "desc": "HTTPS 포트"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "modify-web-server", "title": "웹 서버 수정", "desc": "웹 서버 설정을 수정합니다.", "method": "PUT", "path": "/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 40,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "delete-web-server", "title": "웹 서버 삭제/해제", "desc": "웹 서버를 삭제(uninstall)하거나 등록 해제(deregister)합니다.", "method": "DELETE", "path": "/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 50,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "type", "type": "string", "required": True, "desc": "작업 유형 (`uninstall` 또는 `deregister`)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "control-web-server", "title": "웹 서버 제어 (시작/중지)", "desc": "웹 서버를 시작하거나 중지합니다.", "method": "POST", "path": "/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action", "weight": 60,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [{"name": "action", "type": "string", "required": True, "desc": "액션 (`start` 또는 `stop`)"}],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "setup-workers", "title": "로드밸런서 워커 설정", "desc": "웹 서버의 로드밸런서 워커를 설정합니다.", "method": "PUT", "path": "/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/worker", "weight": 70,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "setup-ssl", "title": "SSL 설정", "desc": "웹 서버에 SSL을 설정합니다.", "method": "POST", "path": "/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/ssl", "weight": 80,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "list-web-container-servers", "title": "컨테이너 웹 서버 목록 조회", "desc": "컨테이너 그룹에 속한 웹 서버 목록을 조회합니다. 컨테이너 IP, HTTP 포트 정보를 포함합니다.", "method": "GET", "path": "/rest/web/container/servers", "weight": 90,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_fields": [
                 {"name": "serverId", "type": "string", "desc": "서버 ID"},
                 {"name": "serverName", "type": "string", "desc": "서버명"},
                 {"name": "containerIp", "type": "string", "desc": "컨테이너 IP"},
                 {"name": "httpPort", "type": "integer", "desc": "HTTP 포트"},
             ],
             "response_example": '{\n  "containerList": [\n    {\n      "serverId": "web-01",\n      "serverName": "Web Server 01",\n      "containerIp": "172.17.0.3",\n      "httpPort": 80\n    }\n  ]\n}'},
            {"slug": "list-web-registerable", "title": "등록 가능 웹 서버 목록 조회", "desc": "지정된 시스템의 노드에서 등록 가능한 웹 서버 목록을 조회합니다. 아직 LENA에 등록되지 않은 서버들을 반환합니다.", "method": "GET", "path": "/rest/web/servers/register/nodes/{nodeName}/systems/{systemName}", "weight": 100,
             "params": [
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_fields": [
                 {"name": "systemName", "type": "string", "desc": "시스템명"},
                 {"name": "nodeName", "type": "string", "desc": "노드명"},
                 {"name": "serverId", "type": "string", "desc": "서버 ID"},
                 {"name": "serverIp", "type": "string", "desc": "서버 IP"},
                 {"name": "httpPort", "type": "integer", "desc": "HTTP 포트"},
                 {"name": "httpsPort", "type": "integer", "desc": "HTTPS 포트"},
             ],
             "response_example": '{\n  "noRegisterdServers": [\n    {\n      "systemName": "Production",\n      "nodeName": "node-01",\n      "serverId": "web-03",\n      "serverIp": "10.0.1.10",\n      "httpPort": 8080,\n      "httpsPort": 8443\n    }\n  ]\n}'},
            {"slug": "modify-uris", "title": "URI/Rewrite 설정 수정", "desc": "웹 서버의 URI 패턴 및 Rewrite 설정을 추가하거나 삭제합니다.", "method": "PUT", "path": "/rest/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/uri", "weight": 110,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "type", "type": "string", "required": True, "desc": "작업 유형 (`create` 또는 `delete`)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [
                 {"name": "uris", "type": "array", "required": True, "desc": "URI 패턴 목록 (예: `[\"/api/*\", \"/app/*\"]`)"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
        ],
    },
    {
        "slug": "session-server",
        "title": "세션 서버 관리",
        "description": "세션 서버의 설치, 조회, 수정, 삭제 및 제어를 관리합니다.",
        "weight": 50,
        "controller": "RestSessionServerController",
        "endpoints": [
            {"slug": "list-session-servers", "title": "모든 세션 서버 조회", "desc": "등록된 모든 세션 서버 목록을 조회합니다.", "method": "GET", "path": "/rest/session/servers", "weight": 10,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_example": '{\n  "servers": [\n    {\n      "serverId": "session-01",\n      "nodeName": "node-01",\n      "systemName": "Production",\n      "serverPort": 6100,\n      "status": "running"\n    }\n  ]\n}'},
            {"slug": "get-session-server", "title": "세션 서버 상세 조회", "desc": "특정 세션 서버의 상세 정보를 조회합니다.", "method": "GET", "path": "/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 20,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "serverId": "session-01",\n  "nodeName": "node-01",\n  "systemName": "Production",\n  "serverPort": 6100,\n  "status": "running"\n}'},
            {"slug": "create-session-server", "title": "세션 서버 설치/등록", "desc": "세션 서버를 설치하거나 기존 서버를 등록합니다.", "method": "POST", "path": "/rest/session/servers", "weight": 30,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "body_params": [
                 {"name": "type", "type": "string", "required": True, "desc": "작업 유형 (`install` 또는 `register`)"},
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명"},
                 {"name": "serverPort", "type": "integer", "required": True, "desc": "서버 포트"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "delete-session-server", "title": "세션 서버 삭제/해제", "desc": "세션 서버를 삭제(uninstall)하거나 등록 해제(deregister)합니다.", "method": "DELETE", "path": "/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 40,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "type", "type": "string", "required": True, "desc": "작업 유형 (`uninstall` 또는 `deregister`)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "control-session-server", "title": "세션 서버 제어 (시작/중지)", "desc": "세션 서버를 시작하거나 중지합니다.", "method": "POST", "path": "/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}/action", "weight": 50,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [{"name": "action", "type": "string", "required": True, "desc": "액션 (`start` 또는 `stop`)"}],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "list-register-session-servers", "title": "등록 가능 세션 서버 목록 조회", "desc": "특정 노드에 등록 가능한 세션 서버 목록을 조회합니다.", "method": "GET", "path": "/rest/session/servers/register/nodes/{nodeName}/systems/{systemName}", "weight": 55,
             "params": [
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "servers": [\n    {\n      "serverId": "session-02",\n      "serverHome": "/usr/local/lena/servers/session-02",\n      "status": "available"\n    }\n  ]\n}'},
            {"slug": "update-session-server", "title": "세션 서버 수정", "desc": "세션 서버의 설정을 수정합니다.", "method": "PUT", "path": "/rest/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 56,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
        ],
    },
    {
        "slug": "metrics",
        "title": "메트릭 조회",
        "description": "노드 및 서버의 실시간 메트릭(CPU, Memory, JVM, Thread 등)을 조회합니다.",
        "weight": 60,
        "controller": "RestMetersController",
        "endpoints": [
            {"slug": "list-all-node-metrics", "title": "모든 노드 메트릭 조회", "desc": "모든 노드의 메트릭 정보를 일괄 조회합니다.", "method": "GET", "path": "/meters/nodes", "weight": 10,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_example": '{\n  "nodes": [\n    {\n      "nodeName": "node-01",\n      "cpu": 45.2,\n      "memoryUsed": 4096,\n      "memoryTotal": 8192,\n      "diskUsage": 62.5\n    }\n  ]\n}'},
            {"slug": "get-node-metrics", "title": "특정 노드 메트릭 조회", "desc": "특정 노드의 상세 메트릭 정보를 조회합니다.", "method": "GET", "path": "/meters/nodes/{nodeName}/systems/{systemName}", "weight": 20,
             "params": [
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "nodeName": "node-01",\n  "cpu": 45.2,\n  "memoryUsed": 4096,\n  "memoryTotal": 8192,\n  "diskUsage": 62.5,\n  "networkIn": 1024,\n  "networkOut": 2048\n}'},
            {"slug": "get-node-all-metrics", "title": "노드 전체 메트릭 조회 (서버 포함)", "desc": "노드와 소속 서버의 전체 메트릭을 일괄 조회합니다.", "method": "GET", "path": "/meters/nodes/{nodeName}/systems/{systemName}/all", "weight": 30,
             "params": [
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "node": {"cpu": 45.2, "memoryUsed": 4096},\n  "wasServers": [\n    {"serverId": "was-01", "heapUsed": 512, "heapMax": 1024, "threadActive": 25}\n  ],\n  "webServers": [\n    {"serverId": "web-01", "connections": 150}\n  ]\n}'},
            {"slug": "get-was-server-metrics", "title": "WAS 서버 메트릭 조회", "desc": "특정 WAS 서버의 메트릭(JVM Heap, Thread, GC 등)을 조회합니다.", "method": "GET", "path": "/meters/was/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 40,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "serverId": "was-01",\n  "heapUsed": 512,\n  "heapMax": 1024,\n  "threadActive": 25,\n  "threadMax": 200,\n  "gcCount": 142,\n  "gcTime": 1250\n}'},
            {"slug": "get-web-server-metrics", "title": "웹 서버 메트릭 조회", "desc": "특정 웹 서버의 메트릭(연결 수, 요청 수 등)을 조회합니다.", "method": "GET", "path": "/meters/web/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 50,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "serverId": "web-01",\n  "connections": 150,\n  "requestsPerSec": 42.5,\n  "bytesIn": 10240,\n  "bytesOut": 51200\n}'},
            {"slug": "get-session-server-metrics", "title": "세션 서버 메트릭 조회", "desc": "특정 세션 서버의 메트릭을 조회합니다.", "method": "GET", "path": "/meters/session/servers/{serverId}/nodes/{nodeName}/systems/{systemName}", "weight": 60,
             "params": [
                 {"name": "serverId", "type": "string", "required": True, "desc": "서버 ID (Path)"},
                 {"name": "nodeName", "type": "string", "required": True, "desc": "노드명 (Path)"},
                 {"name": "systemName", "type": "string", "required": True, "desc": "시스템명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "serverId": "session-01",\n  "activeSessions": 1250,\n  "memoryUsed": 256,\n  "memoryMax": 512\n}'},
            {"slug": "get-was-container-metrics", "title": "WAS 컨테이너 메트릭 조회", "desc": "WAS 컨테이너의 메트릭을 호스트명 기준으로 조회합니다.", "method": "GET", "path": "/meters/was/container/{hostName}", "weight": 70,
             "params": [
                 {"name": "hostName", "type": "string", "required": True, "desc": "호스트명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "hostName": "was-container-01",\n  "cpu": 35.2,\n  "memoryUsed": 2048,\n  "memoryMax": 4096,\n  "threadCount": 150\n}'},
            {"slug": "get-web-container-metrics", "title": "웹 컨테이너 메트릭 조회", "desc": "웹 컨테이너의 메트릭을 호스트명 기준으로 조회합니다.", "method": "GET", "path": "/meters/web/container/{hostName}", "weight": 80,
             "params": [
                 {"name": "hostName", "type": "string", "required": True, "desc": "호스트명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "hostName": "web-container-01",\n  "connections": 85,\n  "requestsPerSec": 120.5,\n  "bytesIn": 20480,\n  "bytesOut": 102400\n}'},
        ],
    },
    {
        "slug": "notification",
        "title": "알림 관리",
        "description": "시스템 이벤트 알림을 조회합니다.",
        "weight": 70,
        "controller": "RestNotificationController",
        "endpoints": [
            {"slug": "list-notifications", "title": "알림 목록 조회", "desc": "시스템 이벤트 알림 목록을 조회합니다. interval 또는 dateTime 기반 필터를 지원합니다.", "method": "GET", "path": "/rest/notification", "weight": 10,
             "params": [
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
                 {"name": "interval", "type": "integer", "required": False, "desc": "조회 범위 (분 단위)"},
                 {"name": "dateTime", "type": "string", "required": False, "desc": "기준 시각 (yyyyMMddHHmmss)"},
                 {"name": "limit", "type": "integer", "required": False, "desc": "최대 조회 건수"},
             ],
             "response_example": '{\n  "notifications": [\n    {\n      "id": 1001,\n      "type": "WARNING",\n      "message": "High CPU usage on node-01",\n      "targetName": "node-01",\n      "createdAt": "20260227120000"\n    }\n  ]\n}'},
        ],
    },
    {
        "slug": "resource",
        "title": "리소스 관리",
        "description": "데이터베이스 및 데이터소스 리소스를 관리합니다.",
        "weight": 80,
        "controller": "RestResourceController",
        "endpoints": [
            {"slug": "list-databases", "title": "데이터베이스 목록 조회", "desc": "등록된 모든 데이터베이스 목록을 조회합니다.", "method": "GET", "path": "/rest/resource/databases", "weight": 10,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_example": '{\n  "databases": [\n    {\n      "resourceName": "mydb",\n      "databaseType": "MySQL",\n      "host": "10.0.1.100",\n      "port": 3306,\n      "databaseName": "lena_db"\n    }\n  ]\n}'},
            {"slug": "get-database", "title": "데이터베이스 상세 조회", "desc": "특정 데이터베이스의 상세 정보를 조회합니다.", "method": "GET", "path": "/rest/resource/databases/{resourceName}", "weight": 20,
             "params": [
                 {"name": "resourceName", "type": "string", "required": True, "desc": "리소스명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "resourceName": "mydb",\n  "databaseType": "MySQL",\n  "host": "10.0.1.100",\n  "port": 3306,\n  "databaseName": "lena_db",\n  "userName": "lena_user"\n}'},
            {"slug": "create-database", "title": "데이터베이스 생성", "desc": "새로운 데이터베이스 리소스를 생성합니다.", "method": "POST", "path": "/rest/resource/databases", "weight": 30,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "body_params": [
                 {"name": "resourceName", "type": "string", "required": True, "desc": "리소스명"},
                 {"name": "databaseType", "type": "string", "required": True, "desc": "DB 타입 (MySQL, Oracle, PostgreSQL 등)"},
                 {"name": "host", "type": "string", "required": True, "desc": "호스트"},
                 {"name": "port", "type": "integer", "required": True, "desc": "포트"},
                 {"name": "databaseName", "type": "string", "required": True, "desc": "데이터베이스명"},
                 {"name": "userName", "type": "string", "required": True, "desc": "사용자명"},
                 {"name": "password", "type": "string", "required": True, "desc": "비밀번호"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "delete-database", "title": "데이터베이스 삭제", "desc": "데이터베이스 리소스를 삭제합니다.", "method": "DELETE", "path": "/rest/resource/databases/{resourceName}", "weight": 40,
             "params": [
                 {"name": "resourceName", "type": "string", "required": True, "desc": "리소스명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "list-datasources", "title": "데이터소스 목록 조회", "desc": "등록된 모든 데이터소스 목록을 조회합니다.", "method": "GET", "path": "/rest/resource/datasources", "weight": 50,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_example": '{\n  "datasources": [\n    {\n      "resourceName": "myds",\n      "databaseResourceName": "mydb",\n      "minPoolSize": 5,\n      "maxPoolSize": 20\n    }\n  ]\n}'},
            {"slug": "create-datasource", "title": "데이터소스 생성", "desc": "새로운 데이터소스를 생성합니다.", "method": "POST", "path": "/rest/resource/datasources", "weight": 60,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "body_params": [
                 {"name": "resourceName", "type": "string", "required": True, "desc": "데이터소스 리소스명"},
                 {"name": "databaseResourceName", "type": "string", "required": True, "desc": "연결할 데이터베이스 리소스명"},
                 {"name": "minPoolSize", "type": "integer", "required": False, "desc": "최소 커넥션 풀 크기"},
                 {"name": "maxPoolSize", "type": "integer", "required": False, "desc": "최대 커넥션 풀 크기"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "get-datasource", "title": "데이터소스 상세 조회", "desc": "특정 데이터소스의 상세 정보를 조회합니다.", "method": "GET", "path": "/rest/resource/datasources/{resourceName}", "weight": 55,
             "params": [
                 {"name": "resourceName", "type": "string", "required": True, "desc": "리소스명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "resourceName": "myds",\n  "databaseResourceName": "mydb",\n  "minPoolSize": 5,\n  "maxPoolSize": 20,\n  "initialPoolSize": 5,\n  "maxWait": 30000\n}'},
            {"slug": "update-datasource", "title": "데이터소스 수정", "desc": "데이터소스의 설정을 수정합니다.", "method": "PUT", "path": "/rest/resource/datasource/{resourceName}", "weight": 65,
             "params": [
                 {"name": "resourceName", "type": "string", "required": True, "desc": "리소스명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [
                 {"name": "minPoolSize", "type": "integer", "required": False, "desc": "최소 커넥션 풀 크기"},
                 {"name": "maxPoolSize", "type": "integer", "required": False, "desc": "최대 커넥션 풀 크기"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "delete-datasource", "title": "데이터소스 삭제", "desc": "데이터소스를 삭제합니다.", "method": "DELETE", "path": "/rest/resource/datasources/{resourceName}", "weight": 70,
             "params": [
                 {"name": "resourceName", "type": "string", "required": True, "desc": "리소스명 (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
        ],
    },
    {
        "slug": "admin",
        "title": "관리자 기능",
        "description": "사용자 계정, 권한(Role), 액션 추적 로그를 관리합니다.",
        "weight": 90,
        "controller": "RestAdminController",
        "endpoints": [
            {"slug": "list-action-logs", "title": "액션 추적 로그 조회", "desc": "관리 액션 추적 로그를 조회합니다.", "method": "GET", "path": "/rest/admin/actionTraceLogList", "weight": 10,
             "params": [
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
                 {"name": "startDate", "type": "string", "required": False, "desc": "시작일 (yyyyMMdd)"},
                 {"name": "endDate", "type": "string", "required": False, "desc": "종료일 (yyyyMMdd)"},
             ],
             "response_example": '{\n  "logs": [\n    {\n      "logId": 1,\n      "userId": "admin",\n      "action": "CREATE_SYSTEM",\n      "targetName": "Production",\n      "result": "SUCCESS",\n      "createdAt": "2026-02-27 12:00:00"\n    }\n  ]\n}'},
            {"slug": "list-users", "title": "사용자 목록 조회", "desc": "등록된 모든 사용자 목록을 조회합니다.", "method": "GET", "path": "/rest/admin/users", "weight": 20,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_example": '{\n  "users": [\n    {\n      "usrId": "admin",\n      "usrNm": "Administrator",\n      "roles": ["ADMIN"]\n    }\n  ]\n}'},
            {"slug": "get-user", "title": "사용자 상세 조회", "desc": "특정 사용자의 상세 정보를 조회합니다.", "method": "GET", "path": "/rest/admin/user/{usrId}", "weight": 30,
             "params": [
                 {"name": "usrId", "type": "string", "required": True, "desc": "사용자 ID (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "usrId": "admin",\n  "usrNm": "Administrator",\n  "roles": ["ADMIN"],\n  "createdAt": "2026-01-01"\n}'},
            {"slug": "create-user", "title": "사용자 생성", "desc": "새로운 사용자를 생성합니다. 비밀번호는 8자 이상, 영문+숫자+특수문자를 포함해야 합니다.", "method": "POST", "path": "/rest/admin/user", "weight": 40,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "body_params": [
                 {"name": "usrId", "type": "string", "required": True, "desc": "사용자 ID"},
                 {"name": "usrNm", "type": "string", "required": True, "desc": "사용자명"},
                 {"name": "usrPw", "type": "string", "required": True, "desc": "비밀번호 (8자 이상, 영문+숫자+특수문자)"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "update-user", "title": "사용자 수정", "desc": "사용자 정보를 수정합니다.", "method": "PUT", "path": "/rest/admin/user/{usrId}", "weight": 50,
             "params": [
                 {"name": "usrId", "type": "string", "required": True, "desc": "사용자 ID (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "delete-user", "title": "사용자 삭제", "desc": "사용자를 삭제합니다.", "method": "DELETE", "path": "/rest/admin/user/{usrId}", "weight": 60,
             "params": [
                 {"name": "usrId", "type": "string", "required": True, "desc": "사용자 ID (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "grant-user-role", "title": "사용자 역할 부여", "desc": "사용자에게 역할을 부여합니다.", "method": "POST", "path": "/rest/admin/user/{usrId}/auth/grant", "weight": 70,
             "params": [
                 {"name": "usrId", "type": "string", "required": True, "desc": "사용자 ID (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [{"name": "authId", "type": "string", "required": True, "desc": "권한 ID"}],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "revoke-user-role", "title": "사용자 역할 취소", "desc": "사용자의 역할을 취소합니다.", "method": "POST", "path": "/rest/admin/user/{usrId}/auth/revoke", "weight": 80,
             "params": [
                 {"name": "usrId", "type": "string", "required": True, "desc": "사용자 ID (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [{"name": "authId", "type": "string", "required": True, "desc": "권한 ID"}],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "list-roles", "title": "권한 목록 조회", "desc": "등록된 모든 권한(Role) 목록을 조회합니다.", "method": "GET", "path": "/rest/admin/auth", "weight": 90,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_example": '{\n  "auths": [\n    {\n      "authId": "ADMIN",\n      "authNm": "Administrator",\n      "actionTypes": ["READ", "WRITE", "EXECUTE"]\n    }\n  ]\n}'},
            {"slug": "create-role", "title": "권한 생성", "desc": "새로운 권한을 생성합니다.", "method": "POST", "path": "/rest/admin/auth", "weight": 100,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "body_params": [
                 {"name": "authId", "type": "string", "required": True, "desc": "권한 ID"},
                 {"name": "authNm", "type": "string", "required": True, "desc": "권한명"},
                 {"name": "actionTypes", "type": "array", "required": True, "desc": "액션 타입 (READ, WRITE, EXECUTE)"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "list-user-roles", "title": "사용자 역할 목록 조회", "desc": "특정 사용자에게 부여된 역할 목록을 조회합니다.", "method": "GET", "path": "/rest/admin/user/{usrId}/auth", "weight": 65,
             "params": [
                 {"name": "usrId", "type": "string", "required": True, "desc": "사용자 ID (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "auths": [\n    {\n      "authId": "ADMIN",\n      "authNm": "Administrator"\n    }\n  ]\n}'},
            {"slug": "get-role", "title": "권한 상세 조회", "desc": "특정 권한의 상세 정보를 조회합니다.", "method": "GET", "path": "/rest/admin/auth/{authId}", "weight": 95,
             "params": [
                 {"name": "authId", "type": "string", "required": True, "desc": "권한 ID (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "authId": "ADMIN",\n  "authNm": "Administrator",\n  "actionTypes": ["READ", "WRITE", "EXECUTE"],\n  "description": "Full system administrator"\n}'},
            {"slug": "update-role", "title": "권한 수정", "desc": "권한 정보를 수정합니다.", "method": "PUT", "path": "/rest/admin/auth/{authId}", "weight": 105,
             "params": [
                 {"name": "authId", "type": "string", "required": True, "desc": "권한 ID (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "body_params": [
                 {"name": "authNm", "type": "string", "required": False, "desc": "권한명"},
                 {"name": "actionTypes", "type": "array", "required": False, "desc": "액션 타입 (READ, WRITE, EXECUTE)"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
            {"slug": "delete-role", "title": "권한 삭제", "desc": "권한을 삭제합니다.", "method": "DELETE", "path": "/rest/admin/auth/{authId}", "weight": 110,
             "params": [
                 {"name": "authId", "type": "string", "required": True, "desc": "권한 ID (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "actionResult": "Y"\n}'},
        ],
    },
    {
        "slug": "event-analysis",
        "title": "이벤트 분석",
        "description": "Stuck Thread, OOM, Full GC 등 서버 이벤트를 분석합니다.",
        "weight": 100,
        "controller": "RestAnlysisEventController",
        "endpoints": [
            {"slug": "list-events", "title": "분석 이벤트 조회", "desc": "서버 분석 이벤트 목록을 조회합니다.", "method": "GET", "path": "/rest/analysis/event", "weight": 10,
             "params": [
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
                 {"name": "systemName", "type": "string", "required": False, "desc": "시스템명 필터"},
                 {"name": "eventType", "type": "string", "required": False, "desc": "이벤트 타입 (stuckthread, oom, fullgc, error)"},
                 {"name": "startDate", "type": "string", "required": False, "desc": "시작일 (yyyyMMdd)"},
                 {"name": "endDate", "type": "string", "required": False, "desc": "종료일 (yyyyMMdd)"},
             ],
             "response_example": '{\n  "events": [\n    {\n      "eventId": 1001,\n      "eventType": "stuckthread",\n      "systemName": "Production",\n      "serverName": "was-01",\n      "message": "Thread stuck for 300s",\n      "createdAt": "2026-02-27 12:00:00"\n    }\n  ]\n}'},
            {"slug": "get-event", "title": "이벤트 상세 조회", "desc": "특정 이벤트의 상세 정보(스택 트레이스 포함)를 조회합니다.", "method": "GET", "path": "/rest/analysis/event/{eventId}", "weight": 20,
             "params": [
                 {"name": "eventId", "type": "integer", "required": True, "desc": "이벤트 ID (Path)"},
                 {"name": "key", "type": "string", "required": True, "desc": "API 인증 키"},
             ],
             "response_example": '{\n  "eventId": 1001,\n  "eventType": "stuckthread",\n  "systemName": "Production",\n  "serverName": "was-01",\n  "message": "Thread stuck for 300s",\n  "stackTrace": "java.lang.Thread.sleep(Native Method)\\n...",\n  "createdAt": "2026-02-27 12:00:00"\n}'},
        ],
    },
    {
        "slug": "license",
        "title": "라이선스 관리",
        "description": "LENA 라이선스 정보를 조회합니다.",
        "weight": 110,
        "controller": "RestLicenseController",
        "endpoints": [
            {"slug": "list-licenses", "title": "라이선스 목록 조회", "desc": "모든 노드의 라이선스 정보를 조회합니다.", "method": "GET", "path": "/rest/licenses", "weight": 10,
             "params": [{"name": "key", "type": "string", "required": True, "desc": "API 인증 키"}],
             "response_example": '{\n  "licenses": [\n    {\n      "nodeName": "node-01",\n      "licenseType": "Enterprise",\n      "expireDate": "2027-12-31",\n      "maxCpu": 16\n    }\n  ]\n}'},
        ],
    },
    {
        "slug": "public",
        "title": "공개 API",
        "description": "인증 없이 접근 가능한 공개 API입니다.",
        "weight": 120,
        "controller": "RestPublicController",
        "endpoints": [
            {"slug": "get-manager-info", "title": "매니저 정보 조회", "desc": "LENA Manager의 버전 및 상태 정보를 조회합니다. 인증이 필요하지 않습니다.", "method": "GET", "path": "/rest/public/managerInfo", "weight": 10,
             "params": [],
             "response_example": '{\n  "version": "1.3.4.4",\n  "patchVersion": "20260201",\n  "status": "running",\n  "haMode": false\n}'},
        ],
    },
]

# ──────────────────────────────────────────────
# Markdown Generator
# ──────────────────────────────────────────────

def render_params_table(params, header="Query Parameters"):
    if not params:
        return ""
    lines = [f"#### {header}\n"]
    lines.append("| Parameter | Type | Required | Description |")
    lines.append("|-----------|------|----------|-------------|")
    for p in params:
        req = "**Yes**" if p.get("required") else "No"
        lines.append(f"| `{p['name']}` | `{p['type']}` | {req} | {p['desc']} |")
    return "\n".join(lines) + "\n"


def render_endpoint(ep, category_slug):
    method = ep["method"]
    path = ep["path"]
    fm = f"""---
title: "{ep['title']}"
description: "{ep['desc']}"
weight: {ep['weight']}
api_method: "{method}"
api_endpoint: "{path}"
---

## {method} {path}

{ep['desc']}

### Request
"""
    sections = []

    # Query / Path params
    params = ep.get("params", [])
    if params:
        sections.append(render_params_table(params))

    # Body params
    body_params = ep.get("body_params", [])
    if body_params:
        sections.append(render_params_table(body_params, "Request Body"))

    if not params and not body_params:
        sections.append("이 엔드포인트는 추가 파라미터가 필요하지 않습니다.\n")

    # Response
    response = f"""### Response

#### 200 OK

```json
{ep.get('response_example', '{}')}
```
"""

    # Response fields
    response_fields = ep.get("response_fields", [])
    if response_fields:
        response += "\n#### Response Fields\n\n"
        response += "| Field | Type | Description |\n"
        response += "|-------|------|-------------|\n"
        for f in response_fields:
            response += f"| `{f['name']}` | `{f['type']}` | {f['desc']} |\n"

    # Error response
    response += """
#### 401 Unauthorized

```json
{
  "error": "Unauthorized",
  "code": "UNAUTHORIZED"
}
```
"""

    # Example
    key_param = "?key=YOUR_API_KEY" if any(p["name"] == "key" for p in params) else ""
    example_path = path.replace("{", "${").replace("}", "}")
    curl_method = f"-X {method} " if method != "GET" else ""
    example = f"""### Example

```bash
curl {curl_method}"https://{{{{manager-host}}}}:{{{{port}}}}{path}{key_param}"
```
"""

    content = fm + "\n".join(sections) + "\n" + response + "\n" + example
    return content


def render_category_index(cat):
    endpoints_list = ""
    for ep in cat["endpoints"]:
        endpoints_list += f"- **{ep['method']}** `{ep['path']}` — {ep['title']}\n"

    return f"""---
title: "{cat['title']}"
description: "{cat['description']}"
weight: {cat['weight']}
---

{cat['description']}

## 엔드포인트

{endpoints_list}
"""


def render_landing():
    cat_table = ""
    for cat in CATEGORIES:
        count = len(cat["endpoints"])
        cat_table += f"| [{cat['title']}](/api-reference/{cat['slug']}/) | {cat['description']} | {count} |\n"

    return f"""---
title: "API Reference"
description: "LENA REST API 레퍼런스 문서"
weight: 30
---

LENA Manager는 시스템, 노드, 서버를 관리하고 모니터링하기 위한 REST API를 제공합니다. 이 문서에서는 사용 가능한 모든 API 엔드포인트와 요청/응답 형식을 설명합니다.

## Base URL

모든 API 요청의 기본 URL은 다음과 같습니다:

```
https://{{{{manager-host}}}}:{{{{port}}}}
```

`{{{{manager-host}}}}`와 `{{{{port}}}}`는 LENA Manager가 설치된 서버의 호스트명과 포트 번호로 대체합니다.

## 인증

모든 API 요청에는 API Key를 쿼리 파라미터로 포함해야 합니다 (공개 API 제외).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `key` | `string` | **Yes** | API 인증 키 |

```bash
# 예시: API Key를 쿼리 파라미터로 전달
curl -X GET "https://{{{{manager-host}}}}:{{{{port}}}}/rest/systems?key=YOUR_API_KEY"
```

## 공통 응답 형식

### 성공 응답 (ActionResult)

작업 수행 결과는 `ActionResult` 형식으로 반환됩니다:

```json
{{{{
  "actionResult": "Y"
}}}}
```

| 값 | 설명 |
|----|------|
| `Y` | 작업 성공 |
| `N` | 작업 실패 |

### 에러 응답

```json
{{{{
  "error": "에러 메시지",
  "code": "ERROR_CODE"
}}}}
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
{cat_table}
"""


def main():
    # Remove old MVP directories
    old_dirs = ["server-management", "monitoring", "configuration"]
    for d in old_dirs:
        dirpath = os.path.join(BASE_DIR, d)
        if os.path.exists(dirpath):
            shutil.rmtree(dirpath)
            print(f"Removed old directory: {d}/")

    # Write landing page
    landing_path = os.path.join(BASE_DIR, "_index.md")
    with open(landing_path, "w", encoding="utf-8") as f:
        f.write(render_landing())
    print(f"Generated: _index.md")

    # Keep guide pages (getting-started, authentication, errors)
    # They were already created by MVP and are still valid

    total_endpoints = 0

    for cat in CATEGORIES:
        cat_dir = os.path.join(BASE_DIR, cat["slug"])
        os.makedirs(cat_dir, exist_ok=True)

        # Category index
        index_path = os.path.join(cat_dir, "_index.md")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(render_category_index(cat))
        print(f"Generated: {cat['slug']}/_index.md")

        # Endpoint pages
        for ep in cat["endpoints"]:
            ep_path = os.path.join(cat_dir, f"{ep['slug']}.md")
            with open(ep_path, "w", encoding="utf-8") as f:
                f.write(render_endpoint(ep, cat["slug"]))
            total_endpoints += 1

        print(f"Generated: {cat['slug']}/ ({len(cat['endpoints'])} endpoints)")

    print(f"\nTotal: {len(CATEGORIES)} categories, {total_endpoints} endpoints")


if __name__ == "__main__":
    main()
