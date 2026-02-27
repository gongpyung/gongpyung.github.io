# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows a date-based update style.

## [2026-02-27]

### Added
- **API Reference** section (`/api-reference/`) with full LENA REST API documentation.
  - 12 categories, 81 endpoints covering all user-facing APIs.
  - Dedicated layouts: method badges, endpoint paths, parameter tables, response examples.
  - API-specific sidebar navigation with method indicators (GET/POST/PUT/DELETE).
  - Dark mode support with per-method color theming.
  - Mobile-responsive design.
- Generation tooling (`tools/api-reference/generate_pages.py`) for endpoint page creation.
- API inventory document (`tools/api-reference/API_INVENTORY.md`) mapping all 100 controller endpoints (81 public + 19 internal).

## [Unreleased]

### Added
- Added `README.md` with project overview, development, and deployment notes.
- Added `CHANGELOG.md` for tracking project changes.

### Changed
- Updated right-side TOC header from text (`On this page`) to icon.
- Improved sidebar collapse/expand button UX:
  - moved collapse button to top area
  - adjusted button size and placement
  - aligned collapse/expand trigger position near header

### Fixed
- Improved sidebar top spacing and visual alignment around release selector.
