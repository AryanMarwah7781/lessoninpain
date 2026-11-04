// Records lesson-studio-demo.html to JPEG frames via a CDP screencast and writes an ffconcat list.
// usage: node record.mjs <html> <outDir> [speed] [shotEveryMs]
//   shotEveryMs > 0 = preview mode: plain screenshots at that interval, no screencast.
import { chromium } from 'playwright-core';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const [, , html, outDir, speed = '1', shotEvery = '0'] = process.argv;
fs.rmSync(outDir, { recursive: true, force: true });
fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch({ channel: 'chrome', headless: true, args: ['--hide-scrollbars', '--force-device-scale-factor=1'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.error('PAGE ERROR', e.message));
page.on('console', m => { if (m.type() === 'error') console.error('CONSOLE', m.text()); });

const url = pathToFileURL(path.resolve(html)).href + `?rec=1&speed=${speed}`;
await page.goto(url);
await page.waitForFunction(() => typeof window.__start === 'function');

const frames = [];
if (+shotEvery > 0) {
  await page.evaluate(() => window.__start());
  let i = 0;
  while (!(await page.evaluate(() => window.__demoDone === true))) {
    await page.waitForTimeout(+shotEvery);
    await page.screenshot({ path: path.join(outDir, `p${String(i++).padStart(3, '0')}.png`) });
  }
} else {
  const cdp = await page.context().newCDPSession(page);
  let n = 0;
  cdp.on('Page.screencastFrame', f => {
    const file = `f${String(n++).padStart(6, '0')}.jpg`;
    fs.writeFileSync(path.join(outDir, file), Buffer.from(f.data, 'base64'));
    frames.push({ file, t: f.metadata.timestamp });
    cdp.send('Page.screencastFrameAck', { sessionId: f.sessionId }).catch(() => {});
  });
  await cdp.send('Page.startScreencast', { format: 'jpeg', quality: 95, maxWidth: 1920, maxHeight: 1080, everyNthFrame: 1 });
  await page.waitForTimeout(400);
  await page.evaluate(() => window.__start());
  await page.waitForFunction(() => window.__demoDone === true, null, { timeout: 15 * 60 * 1000, polling: 250 });
  await page.waitForTimeout(300);
  await cdp.send('Page.stopScreencast');
  await new Promise(r => setTimeout(r, 500));

  // each frame lasts until the next one arrives; screencast only sends frames when pixels change
  let list = 'ffconcat version 1.0\n';
  frames.forEach((f, i) => {
    const next = frames[i + 1];
    // the closing card is static, so no frames arrive while it shows; hold the last frame for it
    const dur = next ? Math.max(0.001, next.t - f.t) : 4.0;
    list += `file '${f.file}'\nduration ${dur.toFixed(4)}\n`;
  });
  list += `file '${frames[frames.length - 1].file}'\n`;
  fs.writeFileSync(path.join(outDir, 'list.ffconcat'), list);
  const total = frames[frames.length - 1].t - frames[0].t;
  console.log(`frames=${frames.length} seconds=${total.toFixed(1)}`);
}
await browser.close();
