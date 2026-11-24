"""Makes a square share picture (1080 x 1080) for each lesson and language in src/media/share-lN-LANG.jpg:
logo, lesson title, its verse and a QR code that opens the lesson page.

Usage (the built site must be served, for the fonts and pictures):
  python3 -m http.server 8765 --directory docs &
  python3 src/tools/gen_share.py http://localhost:8765/
  python3 src/build.py
Needs: playwright (with Chrome), opencv-python, segno.
"""
import asyncio, html, os, sys
import cv2, segno
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import build as B  # noqa: E402

BASE = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8765/'
MEDIA = os.path.join(HERE, '..', 'media') + '/'
DOCS = os.path.join(HERE, '..', '..', 'docs')
E = html.escape

CSS = """
html, body { margin: 0; }
.card { width: 1080px; height: 1080px; position: relative; overflow: hidden; color: #F7F3EA; display: flex; flex-direction: column; align-items: center; text-align: center;
  background:
    url(assets/frieze.svg) center bottom 34px / 84px 42px repeat-x,
    radial-gradient(760px 460px at 50% 22%, rgba(217,178,106,.18), transparent 70%),
    radial-gradient(700px 420px at 10% 112%, rgba(63,143,106,.28), transparent 70%),
    radial-gradient(rgba(217,178,106,.18) 1.4px, transparent 1.9px) 0 0 / 30px 30px, #0F2E2A;
  box-shadow: inset 0 0 0 10px #0F2E2A, inset 0 0 0 12px rgba(217,178,106,.55); }
.arch { position: absolute; left: 50%; top: 40px; width: 380px; transform: translateX(-50%); opacity: .34;
  -webkit-mask-image: linear-gradient(#000 45%, transparent 85%); mask-image: linear-gradient(#000 45%, transparent 85%); }
.logo { position: relative; width: 250px; margin-top: 92px; filter: drop-shadow(0 18px 40px rgba(0,0,0,.5)); }
.eb { position: relative; margin: 26px 0 0; font: 600 30px/1.3 var(--uf); color: #D9B26A; }
h1 { position: relative; margin: 10px 60px 0; font: 600 76px/1.25 var(--hf); word-spacing: .16em; }
.vs { position: relative; margin: 30px 80px 0; font: 44px/1.75 'Amiri Quran', 'Amiri', serif; color: #F1E3C0; direction: rtl; }
.meal { position: relative; margin: 6px 100px 0; font: 500 30px/1.4 'EB Garamond', Georgia, serif; color: #D7E2DE; }
.foot { position: absolute; left: 70px; right: 70px; bottom: 118px; display: flex; align-items: center; gap: 26px; text-align: start; }
.qr { flex: none; width: 150px; height: 150px; background: #fff; border-radius: 14px; padding: 10px; box-sizing: border-box; }
.qr svg { width: 100%; height: 100%; display: block; }
.foot b { display: block; font: 600 32px/1.3 var(--hf); color: #D9B26A; word-spacing: .12em; }
.foot span { display: block; margin-top: 6px; font: 500 26px/1.4 var(--uf); color: #C6D6D0; }
.foot .url { direction: ltr; unicode-bidi: isolate; font: 600 24px/1.3 'Source Sans 3', sans-serif; color: #F7F3EA; }
html[lang=tr] h1 { font-size: 74px; line-height: 1.15; word-spacing: normal; }
"""

TXT = {
    'ar': dict(eb=lambda L: f"صفة الكفر بالطاغوت · الدرس {B.DIG('ar', L['n'])}", scan='امسح الرمز لتفتح الدرس',
               tools='فيديو · درس مكتوب · خريطة · أسئلة · اختبار'),
    'tr': dict(eb=lambda L: f"Tâğutu inkârın keyfiyeti · {L['n']}. ders", scan='Dersi açmak için kodu okutun',
               tools='Video · Yazılı ders · Harita · Soru-cevap · Test'),
}


def page(lang, L):
    t = TXT[lang]
    url = B.lesson_url(lang, L)
    qr = segno.make(url, error='m').svg_inline(dark='#0F2E2A', border=0, omitsize=True)
    meal = f'<p class="meal">{E(L["verseTr"])}</p>' if lang == 'tr' else ''
    return f'''<!DOCTYPE html><html lang="{lang}" dir="{'rtl' if lang == 'ar' else 'ltr'}"><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts.css"><link rel="stylesheet" href="assets/site.css"><style>{CSS}</style></head><body>
<div class="card" id="card">
  <img class="arch" src="assets/arch.svg" alt="">
  <img class="logo" src="media/logo.webp" alt="">
  <p class="eb">{E(t['eb'](L))}</p>
  <h1>{E(L[lang])}</h1>
  <p class="vs">{E(L["verse"])}</p>{meal}
  <div class="foot"><div class="qr">{qr}</div><div><b>{E(t['scan'])}</b><span>{E(t['tools'])}</span><span class="url">{E(url.replace('https://', ''))}</span></div></div>
</div></body></html>'''


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(**({'executable_path': '/usr/bin/google-chrome'} if os.path.exists('/usr/bin/google-chrome') else {}))
        pg = await b.new_page(viewport={'width': 1080, 'height': 1080})
        for L in B.LIVE:
            for lang in ('ar', 'tr'):
                tmp = os.path.join(DOCS, '_share_tmp.html')
                open(tmp, 'w', encoding='utf-8').write(page(lang, L))
                await pg.goto(BASE + '_share_tmp.html', wait_until='networkidle')
                os.remove(tmp)
                await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
                png = f'{MEDIA}share-l{L["n"]}-{lang}.png'
                await (await pg.query_selector('#card')).screenshot(path=png)
                im = cv2.imread(png); os.remove(png)
                out = f'{MEDIA}share-l{L["n"]}-{lang}.jpg'
                cv2.imwrite(out, im, [cv2.IMWRITE_JPEG_QUALITY, 88])
                print(os.path.basename(out), 'QR =', cv2.QRCodeDetector().detectAndDecode(im)[0])
        await b.close()

asyncio.run(main())
