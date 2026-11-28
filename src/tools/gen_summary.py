"""Renders the printable summaries (lN/summary.html) to A4 PDF and JPG in src/media/,
and checks that each QR code reads the right address.

Usage: build the site, serve it, then run this, then build again so the files are copied:
  python3 src/build.py
  python3 -m http.server 8765 --directory docs &
  python3 src/tools/gen_summary.py http://localhost:8765/
  python3 src/build.py
Needs: playwright (with Chrome), opencv-python.
"""
import asyncio, os, sys
import cv2
from playwright.async_api import async_playwright
MEDIA = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'media') + '/'
BASE = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8765/'
PAGES = [('l1', 'ar'), ('l2', 'ar'), ('l3', 'ar'), ('f1', 'ar'), ('f2', 'ar'), ('f3', 'ar'), ('f4', 'ar'), ('f5', 'ar'), ('f6', 'ar'), ('f7', 'ar'), ('l1', 'tr'), ('l2', 'tr'), ('l3', 'tr'), ('f1', 'tr'), ('f2', 'tr'), ('f3', 'tr'), ('f4', 'tr'), ('f5', 'tr'), ('f6', 'tr'), ('f7', 'tr')]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(**({'executable_path': '/usr/bin/google-chrome'} if os.path.exists('/usr/bin/google-chrome') else {}))
        ctx = await b.new_context(viewport={'width': 1000, 'height': 1300}, device_scale_factor=2)
        pg = await ctx.new_page()
        for l, lang in PAGES:
            url = BASE + ('' if lang == 'ar' else 'tr/') + f'{l}/summary.html'
            await pg.goto(url, wait_until='networkidle'); await pg.wait_for_timeout(500)
            name = f'summary-{l}-{lang}'
            el = await pg.query_selector('#sheet')
            await el.screenshot(path=MEDIA + name + '.png')
            await pg.emulate_media(media='print')
            await pg.pdf(path=MEDIA + name + '.pdf', format='A4', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'}, prefer_css_page_size=True)
            await pg.emulate_media(media='screen')
            im = cv2.imread(MEDIA + name + '.png')
            cv2.imwrite(MEDIA + name + '.jpg', im, [cv2.IMWRITE_JPEG_QUALITY, 88]); os.remove(MEDIA + name + '.png')
            v, _, _ = cv2.QRCodeDetector().detectAndDecode(im)
            print(name, im.shape, 'QR =', v)
        await b.close()
asyncio.run(main())
