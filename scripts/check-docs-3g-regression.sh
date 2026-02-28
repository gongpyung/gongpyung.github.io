#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BASE_URL="${BASE_URL:-http://127.0.0.1:1313}"
HUGO_HOST="${HUGO_HOST:-127.0.0.1}"
HUGO_PORT="${HUGO_PORT:-1313}"
HUGO_LOG="${HUGO_LOG:-/tmp/lena-docs-hugo-3g.log}"

cd "$ROOT_DIR"

cleanup() {
  if [[ -n "${HUGO_PID:-}" ]] && kill -0 "$HUGO_PID" 2>/dev/null; then
    kill "$HUGO_PID" >/dev/null 2>&1 || true
    wait "$HUGO_PID" 2>/dev/null || true
  fi
}
trap cleanup EXIT

echo "[3g-check] Starting Hugo server on ${HUGO_HOST}:${HUGO_PORT} ..."
hugo server --bind "$HUGO_HOST" --port "$HUGO_PORT" >"$HUGO_LOG" 2>&1 &
HUGO_PID=$!

READY=0
for _ in $(seq 1 60); do
  if curl -fsS "$BASE_URL/" >/dev/null 2>&1; then
    READY=1
    break
  fi
  sleep 1
done

if [[ "$READY" -ne 1 ]]; then
  echo "[3g-check] Hugo server failed to start. Last logs:" >&2
  tail -n 80 "$HUGO_LOG" >&2 || true
  exit 1
fi

echo "[3g-check] Hugo server is ready. Running Playwright 3G regression check..."

# Ensure Playwright package exists in npx cache, then expose it via NODE_PATH for the script runtime.
npx --yes playwright --version >/dev/null
PLAYWRIGHT_PKG="$(find "$HOME/.npm/_npx" -path '*/node_modules/playwright/package.json' 2>/dev/null | sort | tail -n1)"
if [[ -z "${PLAYWRIGHT_PKG}" ]]; then
  echo "[3g-check] Failed to locate playwright package in npx cache" >&2
  exit 1
fi

NODE_PATH="$(dirname "$(dirname "$PLAYWRIGHT_PKG")")"   node "$ROOT_DIR/scripts/playwright/check-docs-3g-regression.cjs" --base-url "$BASE_URL" "$@"

echo "[3g-check] Done"
