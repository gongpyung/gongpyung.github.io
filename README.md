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

## Repository Structure

- `content/` — docs and pages
- `themes/lena-docs/` — theme layouts, styles, scripts
- `static/` — static assets copied as-is
- `layouts/` — project-level layout overrides

## Deployment (GitHub Pages)

1. Commit and push to the configured branch
2. GitHub Pages publishes the site
3. (Optional) Custom domain via `CNAME`

## Notes

- Keep theme-level changes inside `themes/lena-docs/`
- Prefer small, focused commits for UI tweaks
