#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const DEFAULT_PATHS = [
  '/docs/1.3.4/1.3.4.2/installation/',
  '/docs/1.3.4/1.3.4.2/userguide/'
];

const MAX_WIDTH_DELTA_PX = Number(process.env.MAX_WIDTH_DELTA_PX || 24);
const MAX_INITIAL_FINAL_DELTA_PX = Number(process.env.MAX_INITIAL_FINAL_DELTA_PX || 24);
const MAX_CLS = Number(process.env.MAX_CLS || 0.1);
const SAMPLE_MS = Number(process.env.SAMPLE_MS || 3000);
const SAMPLE_INTERVAL_MS = Number(process.env.SAMPLE_INTERVAL_MS || 100);

function parseArgs(argv) {
  const args = {
    baseUrl: 'http://127.0.0.1:1313',
    paths: [],
  };

  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (token === '--base-url') {
      args.baseUrl = argv[i + 1];
      i += 1;
      continue;
    }
    if (token === '--path') {
      args.paths.push(argv[i + 1]);
      i += 1;
      continue;
    }
    if (token === '--help' || token === '-h') {
      args.help = true;
      continue;
    }
  }

  if (!args.paths.length) args.paths = DEFAULT_PATHS.slice();
  return args;
}

function printHelp() {
  console.log(`\nUsage:\n  node scripts/playwright/check-docs-3g-regression.cjs [--base-url URL] [--path /docs/... --path /docs/...]\n\nExamples:\n  node scripts/playwright/check-docs-3g-regression.cjs\n  node scripts/playwright/check-docs-3g-regression.cjs --base-url http://127.0.0.1:1313 --path /docs/1.3.4/1.3.4.2/installation/\n\nThreshold env vars:\n  MAX_WIDTH_DELTA_PX (default: 24)\n  MAX_INITIAL_FINAL_DELTA_PX (default: 24)\n  MAX_CLS (default: 0.1)\n  SAMPLE_MS (default: 3000)\n  SAMPLE_INTERVAL_MS (default: 100)\n`);
}

async function emulateSlow3G(context, page) {
  const client = await context.newCDPSession(page);
  await client.send('Network.enable');
  await client.send('Network.emulateNetworkConditions', {
    offline: false,
    latency: 400,
    downloadThroughput: 50000,
    uploadThroughput: 50000,
    connectionType: 'cellular3g',
  });
}

async function checkPage(context, baseUrl, pagePath, index) {
  const page = await context.newPage();
  const fullUrl = new URL(pagePath, baseUrl).toString();

  await emulateSlow3G(context, page);

  await page.addInitScript(() => {
    window.__docCls = 0;
    try {
      const observer = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          if (!entry.hadRecentInput) window.__docCls += entry.value;
        }
      });
      observer.observe({ type: 'layout-shift', buffered: true });
    } catch (_) {
      // ignore when not supported
    }
  });

  await page.goto(fullUrl, { waitUntil: 'domcontentloaded', timeout: 120000 });

  const metrics = await page.evaluate(async ({ sampleMs, intervalMs }) => {
    const target =
      document.querySelector('.doc-include #content') ||
      document.querySelector('.doc-include') ||
      document.querySelector('.doc-content__body');

    const getState = () => {
      const r = target
        ? target.getBoundingClientRect()
        : { width: 0, height: 0, top: 0, left: 0 };
      return {
        width: Number(r.width.toFixed(2)),
        height: Number(r.height.toFixed(2)),
      };
    };

    const samples = [];
    const start = performance.now();

    while (performance.now() - start < sampleMs) {
      samples.push({
        t: Math.round(performance.now() - start),
        ...getState(),
      });
      // eslint-disable-next-line no-await-in-loop
      await new Promise((resolve) => setTimeout(resolve, intervalMs));
    }

    const widths = samples.map((s) => s.width);
    const minWidth = Math.min(...widths);
    const maxWidth = Math.max(...widths);
    const firstWidth = widths[0] ?? 0;
    const finalWidth = widths[widths.length - 1] ?? 0;

    return {
      sampleCount: samples.length,
      minWidth,
      maxWidth,
      widthDelta: Number((maxWidth - minWidth).toFixed(2)),
      initialFinalWidthDelta: Number(Math.abs(firstWidth - finalWidth).toFixed(2)),
      firstWidth,
      finalWidth,
      cls: Number((window.__docCls || 0).toFixed(4)),
      nestedHeadInInclude: document.querySelectorAll('.doc-include head').length,
      nestedHtmlInInclude: document.querySelectorAll('.doc-include html').length,
      styleTagsInInclude: document.querySelectorAll('.doc-include style').length,
      scriptTagsInInclude: document.querySelectorAll('.doc-include script').length,
      targetFound: Boolean(target),
    };
  }, { sampleMs: SAMPLE_MS, intervalMs: SAMPLE_INTERVAL_MS });

  const failures = [];
  if (!metrics.targetFound) failures.push('doc target not found');
  if (metrics.styleTagsInInclude > 0) failures.push(`style tags in include: ${metrics.styleTagsInInclude}`);
  if (metrics.scriptTagsInInclude > 0) failures.push(`script tags in include: ${metrics.scriptTagsInInclude}`);
  if (metrics.nestedHeadInInclude > 0) failures.push(`nested head tags in include: ${metrics.nestedHeadInInclude}`);
  if (metrics.nestedHtmlInInclude > 0) failures.push(`nested html tags in include: ${metrics.nestedHtmlInInclude}`);
  if (metrics.widthDelta > MAX_WIDTH_DELTA_PX) failures.push(`width delta too high: ${metrics.widthDelta}px > ${MAX_WIDTH_DELTA_PX}px`);
  if (metrics.initialFinalWidthDelta > MAX_INITIAL_FINAL_DELTA_PX) failures.push(`initial-final width delta too high: ${metrics.initialFinalWidthDelta}px > ${MAX_INITIAL_FINAL_DELTA_PX}px`);
  if (metrics.cls > MAX_CLS) failures.push(`CLS too high: ${metrics.cls} > ${MAX_CLS}`);

  const screenshotDir = path.join(process.cwd(), 'test-results', 'playwright-3g');
  fs.mkdirSync(screenshotDir, { recursive: true });
  const safeName = pagePath.replace(/[^a-zA-Z0-9]+/g, '_').replace(/^_+|_+$/g, '');
  const screenshotPath = path.join(screenshotDir, `${String(index + 1).padStart(2, '0')}_${safeName}.png`);
  await page.screenshot({ path: screenshotPath, fullPage: false });

  await page.close();

  return {
    url: fullUrl,
    pagePath,
    pass: failures.length === 0,
    failures,
    metrics,
    screenshotPath,
  };
}

(async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    printHelp();
    process.exit(0);
  }

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });

  const results = [];
  try {
    for (let i = 0; i < args.paths.length; i += 1) {
      // eslint-disable-next-line no-await-in-loop
      const res = await checkPage(context, args.baseUrl, args.paths[i], i);
      results.push(res);
    }
  } finally {
    await context.close();
    await browser.close();
  }

  const failed = results.filter((r) => !r.pass);
  const report = {
    generatedAt: new Date().toISOString(),
    baseUrl: args.baseUrl,
    thresholds: {
      MAX_WIDTH_DELTA_PX,
      MAX_INITIAL_FINAL_DELTA_PX,
      MAX_CLS,
      SAMPLE_MS,
      SAMPLE_INTERVAL_MS,
    },
    results,
    pass: failed.length === 0,
  };

  const reportDir = path.join(process.cwd(), 'test-results', 'playwright-3g');
  fs.mkdirSync(reportDir, { recursive: true });
  const reportPath = path.join(reportDir, 'report.json');
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 2), 'utf-8');

  for (const item of results) {
    const icon = item.pass ? '✅' : '❌';
    console.log(`${icon} ${item.pagePath}`);
    console.log(`   widthDelta=${item.metrics.widthDelta}px, initialFinalWidthDelta=${item.metrics.initialFinalWidthDelta}px, cls=${item.metrics.cls}`);
    if (!item.pass) {
      for (const reason of item.failures) console.log(`   - ${reason}`);
    }
  }

  console.log(`\nReport: ${reportPath}`);

  if (failed.length > 0) {
    process.exit(1);
  }
})();
