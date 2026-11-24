"""Opens every page at phone (390px) and desktop (1366px) width and reports console errors,
missing files, horizontal overflow and broken internal links. Screenshots go to /tmp/shots.

Usage: python3 -m http.server 8765 --directory docs &  then  python3 src/tools/test.py http://localhost:8765/
"""
import asyncio, sys, os, re, urllib.parse
from playwright.async_api import async_playwright

BASE = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8765/'
PAGES = ['index.html', 'la-ilaha.html', 'tr/la-ilaha.html', 'tasks.html', 'tr/tasks.html', 'map.html', 'l1/index.html', 'l1/text.html', 'l1/slides.html', 'l1/qa.html', 'l1/quiz.html', 'l1/summary.html',
         'l2/index.html', 'l2/text.html', 'l2/slides.html', 'l2/qa.html', 'l2/quiz.html', 'l2/summary.html',
         'tr/index.html', 'tr/map.html', 'tr/l1/index.html', 'tr/l1/text.html', 'tr/l1/slides.html', 'tr/l1/qa.html', 'tr/l1/quiz.html', 'tr/l1/summary.html',
         'tr/l2/index.html', 'tr/l2/text.html', 'tr/l2/slides.html', 'tr/l2/qa.html', 'tr/l2/quiz.html', 'tr/l2/summary.html']
SHOT = '/tmp/shots'
os.makedirs(SHOT, exist_ok=True)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(**({'executable_path': '/usr/bin/google-chrome'} if os.path.exists('/usr/bin/google-chrome') else {}))
        links = set(); problems = []
        for w, h, tag in ((390, 844, 'm'), (1366, 900, 'd')):
            ctx = await b.new_context(viewport={'width': w, 'height': h}, device_scale_factor=1, is_mobile=(w < 500), has_touch=(w < 500))
            for path in PAGES:
                pg = await ctx.new_page()
                errs = []
                pg.on('console', lambda m, errs=errs: errs.append(m.text) if m.type == 'error' else None)
                pg.on('pageerror', lambda e, errs=errs: errs.append('PAGEERR ' + str(e)))
                failed = []
                pg.on('requestfailed', lambda r, failed=failed: failed.append(r.url))
                pg.on('response', lambda r, failed=failed: failed.append(f'{r.status} {r.url}') if r.status >= 400 and 'localhost' in r.url else None)
                await pg.goto(BASE + path, wait_until='networkidle')
                await pg.wait_for_timeout(400)
                ov = await pg.evaluate('document.documentElement.scrollWidth - innerWidth')
                hrefs = await pg.evaluate('[...document.querySelectorAll("a[href]")].map(a=>a.href)')
                for hh in hrefs:
                    if hh.startswith(BASE): links.add(hh.split('#')[0])
                errs = [e for e in errs if 'mp4' not in e and 'Failed to load resource' not in e]
                failed = [f for f in failed if '.mp4' not in f and 'fonts.g' not in f]
                if ov > 1 or errs or failed:
                    problems.append((tag, path, f'overflow={ov}', errs[:3], failed[:3]))
                await pg.screenshot(path=f'{SHOT}/{tag}_{path.replace("/", "_")}.png', full_page=(path.endswith('index.html') or 'qa' in path or 'text' in path) and 'map' not in path)
                await pg.close()
            await ctx.close()
        # link check
        import urllib.request
        bad = []
        for l in sorted(links):
            try:
                urllib.request.urlopen(l)
            except Exception as e:
                bad.append((l, str(e)))
        print('PROBLEMS', *problems, sep='\n')
        print('LINKS', len(links), 'BAD', bad)
        await b.close()

asyncio.run(main())
