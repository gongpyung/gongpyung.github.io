# AGENTS.md

Guidance for coding agents working in this repository.

## Rule precedence
1. Explicit user instruction
2. This `AGENTS.md`
3. `CLAUDE.md`
4. Existing repository patterns

## Project facts (latest)
- SSG: Hugo
- Theme: `themes/lena-docs` (custom)
- Languages: Korean default (`ko`), English (`en`)
- URL case preserved: `disablePathToLower = true`
- Raw HTML in Markdown allowed: `markup.goldmark.renderer.unsafe = true`
- Deploy pipeline copies `resources/` into `public/`

## Build / validation commands

### Core
- Dev server: `hugo server`
- Dev server (draft/future): `hugo server -D -F`
- Production build: `hugo --minify`
- Deploy-equivalent local build: `hugo --minify && cp -r ./resources ./public`

### Validation
- No unit/integration test framework configured.
- Minimum validation = Hugo build success + target page smoke check.
- Example smoke check:
  - `curl -fI http://localhost:1313/docs/1.3.4/1.3.4.4/`
  - `curl -fI http://localhost:1313/en/docs/1.3.4/1.3.4.2/`

## Repository structure
- Docs pages: `content/{lang}/docs/{major}/{minor}/`
- Download pages: `content/{lang}/download/{major}/{minor}/_index.md`
- Include HTML: `static/{lang}/_includes/{version}/`
- External assets: `resources/{version}/pdf/`, `resources/{version}/static/`
- Theme source: `themes/lena-docs/`
- Project overrides: `layouts/`, `static/custom.css`, `static/js/`

## Editing policy
- Prefer minimal, targeted edits.
- Do not introduce new framework/toolchain unless requested.
- Do not rename/move versioned paths casually.
- Keep `ko`/`en` structure consistent when adding shared features.

## Current workflow policy (important)
- Small tasks (quick CSS/text/simple tweaks): execute directly.
- Medium/Large tasks:
  1. Create improvement plan with Codex
  2. Implement via Claude Code `/team` style parallel execution

## New version workflow
1. Create docs pages under `content/{lang}/docs/{major}/{minor}/`
2. Add include HTML under `static/{lang}/_includes/{version}/`
3. Adjust include asset paths to `/resources/{version}/static`
4. Add static assets to `resources/{version}/static/`
5. Add PDFs to `resources/{version}/pdf/`
6. Add download entries under `content/{lang}/download/{major}/{minor}/`
7. Build and smoke-check

## Deployment notes
- Workflow: `.github/workflows/gh-pages.yml`
- Trigger: push to `master`
- CI flow: build → copy resources → publish `public/` to `gh-pages`
