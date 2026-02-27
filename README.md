# LENA Documentation Site

Static documentation site for LENA, built with **Hugo** and deployed via **GitHub Pages**.

## Stack

- Hugo (extended)
- Custom theme: `themes/lena-docs`
- Deployment target: GitHub Pages

## Local Development

```bash
hugo server
```

Open: `http://localhost:1313`

## Build

```bash
hugo
```

Generated output is in `public/`.

## API Reference

`/api-reference/` 경로에서 LENA REST API 문서를 제공합니다.

- **12 카테고리, 81 엔드포인트** (시스템, 노드, WAS/웹/세션 서버, 메트릭, 리소스, 관리자 등)
- 엔드포인트별 메서드 배지, 경로, 파라미터 테이블, 응답 예시 제공
- API 전용 사이드바 네비게이션

### 페이지 생성

```bash
python tools/api-reference/generate_pages.py
```

엔드포인트 정의는 스크립트 내 `CATEGORIES` 데이터에 관리됩니다. 전체 API 목록은 `tools/api-reference/API_INVENTORY.md`를 참고하세요.

## Repository Structure

- `content/` — docs and pages
- `themes/lena-docs/` — theme layouts, styles, scripts
- `static/` — static assets copied as-is
- `layouts/` — project-level layout overrides
- `tools/` — documentation generation scripts

## Deployment (GitHub Pages)

1. Commit and push to the configured branch
2. GitHub Pages publishes the site
3. (Optional) Custom domain via `CNAME`

## Notes

- Keep theme-level changes inside `themes/lena-docs/`
- Prefer small, focused commits for UI tweaks
