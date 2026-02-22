# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

LENA 제품 기술 문서 사이트 (Hugo 기반 정적 사이트).

- Theme: `themes/lena-docs` (커스텀 테마)
- 배포: GitHub Pages
- 다국어: 한국어(`ko`, 기본), 영어(`en`)
- 버전 구조: `major/minor` (예: `1.3.4/1.3.4.2`)

## Build & Development

```bash
# local dev
hugo server

# production build
hugo --minify

# deploy-equivalent local build (resources 포함)
hugo --minify && cp -r ./resources ./public
```

## Deployment

`master` 브랜치 push 시 GitHub Actions(`.github/workflows/gh-pages.yml`)가 실행되어:
1. `hugo --minify` 빌드
2. `resources/`를 `public/`로 복사
3. `gh-pages` 브랜치 배포

## Current Architecture

### Core paths
- `content/` : 문서/페이지 원본
- `themes/lena-docs/` : 테마 레이아웃/CSS/JS
- `layouts/` : 프로젝트 레벨 오버라이드
- `static/` : 정적 리소스 (복사형)
- `resources/` : PDF/이미지 등 배포 시 `public/`로 복사 필요한 리소스

### Docs content pattern
버전 문서는 보통 아래 3파일 패턴 사용:

```
content/{lang}/docs/{major}/{minor}/
  _index.md
  installation.md
  userguide.md
```

필요 시 `include` shortcode로 `static/{lang}/_includes/{version}/` HTML을 포함.

### Download content pattern

```
content/{lang}/download/{major}/{minor}/_index.md
```

PDF 링크는 `resources/{version}/pdf/` 기준으로 관리.

## UI/Theme Notes (latest)

최근 변경사항(반영 기준):
- 우측 TOC 헤더 `On this page` → 아이콘으로 변경
- 좌측 사이드바 접기/펼치기 버튼 위치/크기 UX 조정
  - Header 바로 아래 정렬
  - 접기/펼치기 버튼 크기 통일
  - 버튼을 사이드바 바깥 우측에 붙여 명확한 affordance 제공

관련 파일:
- `themes/lena-docs/layouts/partials/toc.html`
- `themes/lena-docs/layouts/partials/sidebar.html`
- `themes/lena-docs/assets/css/sidebar.css`

## Conventions

- `disablePathToLower = true` (대소문자 URL 보존)
- `markup.goldmark.renderer.unsafe = true` (HTML 허용)
- 변경은 가능한 작고 명확한 단위로 수행
- UI 변경 후 반드시 `hugo` 빌드 확인
