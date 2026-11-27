"""نموذج تجريبي (غير منشور): ورقة حفظ من خريطة الموقع نفسها، صفحتان A4 بالعرض:
الصفحة ١ الخريطة بالأمور المهمة فقط، والصفحة ٢ الخريطة نفسها بمربعات فارغة («اختبر حفظك»).
المسائل تُكتب يدويًا في src/hifz/<slug>.json (ar و tr)، ولا تُؤخذ من بيانات الخريطة.
الاستعمال: ابنِ الموقع وشغّل الخادم، ثم:
  python3 src/tools/gen_hifz.py ar FIQH5 105 f5 [مجلد الإخراج]
يحتاج: playwright و segno و pdfunite. انظر guide/hifz-maps.md."""
import asyncio, sys, json, segno, subprocess, os
from playwright.async_api import async_playwright
lang, var, n, slug = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/'
OUT = (sys.argv[5] if len(sys.argv) > 5 else '.') + '/'
AR = lang == 'ar'
base = 'http://localhost:8765/' + ('' if AR else 'tr/')
s = open(SRC + 'maps/' + ('data.js' if AR else 'data_tr.js'), encoding='utf-8').read()
i = s.index(f'window.{var} = ') + len(f'window.{var} = '); obj, _ = json.JSONDecoder().raw_decode(s[i:])
url = f'https://tevhidim.com/{"" if AR else "tr/"}{slug}/'
qr = segno.make(url, error='m').svg_inline(scale=3, dark='#0F2E2A', border=0)
D = '٠١٢٣٤٥٦٧٨٩' if AR else '0123456789'
num = lambda k: ''.join(D[int(c)] for c in str(k))
T = dict(
 ar=dict(p1='الخريطة', p2='اختبر حفظك', hot='مسألة يكثر فيها الخطأ', cnt='عدد المسائل',
   how1='احفظ الفروع بأرقامها، ثم مسائل كل فرع بعددها.', how2='غطِّ الصفحة الأولى، واكتب كل مسألة في مكانها، ثم صحّح منها.',
   jam='العبارة الجامعة', jamw='اكتب العبارة الجامعة من حفظك', rev='راجعها', days=['اليوم', 'غدًا', 'بعد ٣ أيام', 'بعد أسبوع', 'بعد شهر'],
   scan='الخريطة التفاعلية والاختبار', score='صحيح: ____ من'),
 tr=dict(p1='Harita', p2='Ezberini sına', hot='Sık hata yapılan mesele', cnt='Mesele sayısı',
   how1='Önce dalları numaralarıyla, sonra her dalın meselelerini sayısıyla ezberle.', how2='İlk sayfayı kapat, her meseleyi yerine yaz, sonra ondan kontrol et.',
   jam='Ezberlenecek özet', jamw='Özeti ezberinden yaz', rev='Tekrar et', days=['Bugün', 'Yarın', '3 gün sonra', '1 hafta sonra', '1 ay sonra'],
   scan='Etkileşimli harita ve test', score='Doğru: ____ /'))[lang]
H = json.load(open(SRC + f'hifz/{slug}.json', encoding='utf-8'))[lang]
obj['branches'] = H
total = sum(len(b['children']) for b in obj['branches'])
HF = "'Reem Kufi','IBM Plex Sans Arabic',sans-serif" if AR else "'EB Garamond',Georgia,serif"
UF = "'IBM Plex Sans Arabic',sans-serif" if AR else "'Source Sans 3',Arial,sans-serif"
AF = "'Amiri','Noto Naskh Arabic',serif" if AR else "'EB Garamond',Georgia,serif"
# before the page lays out the map: wider leaf boxes (room to write) and one font for all leaves
INIT = """(()=>{const H=__H__;let v;Object.defineProperty(window,"__V__",{configurable:true,get(){return v},set(x){x.branches=H;v=x}})})();
document.addEventListener('DOMContentLoaded',()=>{const st=document.createElement('style');st.textContent=`
.node.d1{font-family:${document.documentElement.lang==='ar'?"'IBM Plex Sans Arabic',sans-serif":"'EB Garamond',Georgia,serif"}!important;font-weight:700!important;font-size:44px!important} .node.d2{min-width:230px;font-family:${document.documentElement.lang==='ar'?"'IBM Plex Sans Arabic',sans-serif":"'Source Sans 3',Arial,sans-serif"}!important;font-weight:600!important;font-size:34px!important;line-height:1.35!important;padding:12px 26px!important} ${document.documentElement.lang==='ar'?"":""}`;document.head.appendChild(st)});"""
COMMON = f'''
#top,#card,#tools,#bar,#prog,.wm,#orn,.node .more,.node.hascard::after{{display:none!important}}
body,#stage{{background:#F7F3EA!important}} #stage::before,#stage::after{{display:none!important}}
#ph{{position:fixed;top:0;inset-inline:0;height:60px;background:#0F2E2A;color:#F7F3EA;display:flex;align-items:center;gap:12px;padding:0 24px;z-index:9;font-family:{UF}}}
#ph img{{width:42px}} #ph .eb{{color:#D9B26A;font-size:10px;font-weight:600;margin:0}}
#ph h1{{margin:0;font-family:{HF};font-size:22px;font-weight:600;line-height:1.2}}
#ph .pg{{background:#D9B26A;color:#0F2E2A;border-radius:20px;padding:3px 12px;font-weight:700;font-size:11.5px;margin-inline-start:6px}}
#ph .lg{{margin-inline-start:auto;display:flex;gap:14px;align-items:center;font-size:10.5px;color:#DCE6E2}}
#ph .lg span{{display:flex;align-items:center;gap:6px}}
#ph .sw{{width:20px;height:12px;border-radius:4px;background:#0F2E2A;border:1.5px solid #D9B26A;display:inline-block}}
#ph .how{{font-size:10px;color:#B9CBC4;max-width:330px;line-height:1.45}}
.cnt{{position:absolute;z-index:3;background:#D9B26A;color:#0F2E2A;font-family:{UF};font-weight:700;border-radius:50%;display:grid;place-items:center;border:2px solid #F7F3EA}}
#pf{{position:fixed;bottom:8px;inset-inline:20px;display:flex;gap:10px;z-index:9;font-family:{UF};height:80px}}
#pf .box{{background:#D9B26A;border-radius:12px;padding:6px 14px;color:#0F2E2A;flex:1;overflow:hidden}}
#pf h4{{margin:0;font-family:{HF};font-size:12px;font-weight:600}}
#pf p{{margin:0;font-family:{AF};font-size:{11.6 if AR else 12}px;line-height:{1.55 if AR else 1.35}}}
#pf .rev{{background:#fff;border:1px solid #E6DCC8;border-radius:12px;padding:6px 12px;color:#0F2E2A;font-size:10px}}
#pf .rev .ds{{display:grid;grid-template-columns:repeat(5,auto);gap:3px 10px;margin-top:4px}}
#pf .rev .ds span{{display:flex;flex-direction:column;align-items:center;gap:2px;white-space:nowrap}}
#pf .rev .ds i{{width:15px;height:15px;border:1.5px solid #85601C;border-radius:4px;display:block}}
#pf .qr{{display:flex;align-items:center;gap:8px;background:#0F2E2A;color:#B9CBC4;border-radius:12px;padding:6px 10px;font-size:9.4px}}
#pf .qr svg{{width:58px;height:58px;background:#fff;padding:4px;border-radius:6px}}
#pf .u{{direction:ltr;unicode-bidi:isolate;color:#F7F3EA;font-weight:600}}
#pf .lines{{background:#fff;border:1px solid #E6DCC8;border-radius:12px;padding:5px 14px;flex:1;color:#6B706B;font-size:10.5px}}
#pf .lines i{{display:block;border-bottom:1px dashed #C9AE7A;height:19px}}
#pf .score{{background:#0F2E2A;color:#F7F3EA;border-radius:12px;padding:6px 14px;display:flex;flex-direction:column;justify-content:center;font-size:12px;font-weight:700}}
'''
BLANK = '''
.node.d2{color:transparent!important;background:#fff!important;border:3px dashed #B99A5E!important;box-shadow:none!important}
.node.d2.hot{border:3.5px dashed #0F2E2A!important;background:#F1E8D5!important}
.node.d2 .ix{color:#B99A5E;position:absolute;inset-inline-start:10px;top:50%;transform:translateY(-50%);font-size:.8em;font-weight:700;font-family:sans-serif}
.node.d2.hot .ix{color:#0F2E2A}
'''
def header(page):
    pl = T['p1'] if page == 1 else T['p2']
    how = T['how1'] if page == 1 else T['how2']
    return (f'<div id="ph"><img src="/media/logo.webp"><div><p class="eb">{obj["eb"]}</p><h1>{obj["h1"]}<span class="pg">{num(page)} · {pl}</span></h1></div>'
            f'<div class="lg"><span class="how">{how}</span><span><i class="sw"></i>{T["hot"]}</span>'
            f'<span><i class="cnt" style="position:static;width:18px;height:18px;font-size:10px">{num(6)}</i>{T["cnt"]}</span></div></div>')
def footer(page):
    if page == 1:
        ds = ''.join(f'<span><i></i>{d}</span>' for d in T['days'])
        return (f'<div id="pf"><div class="box"><h4>{T["jam"]}</h4><p>{obj["jamia"]}</p></div>'
                f'<div class="rev"><b>{T["rev"]}</b><div class="ds">{ds}</div></div>'
                f'<div class="qr">{qr}<div>{T["scan"]}<br><span class="u">{url[8:]}</span></div></div></div>')
    return (f'<div id="pf"><div class="lines">{T["jamw"]}<i></i><i></i><i></i></div>'
            f'<div class="score">{T["score"]} {num(total)}</div></div>')
# count badges on branch nodes, and per-branch numbers inside blank boxes
BADGES = """(blank)=>{const W=document.getElementById('world');
 document.querySelectorAll('.node.d1').forEach(b=>{const k=b.dataset.k; });
}"""
async def render(pg, page, path):
    await pg.goto(base + f'map.html#l{n}', wait_until='networkidle'); await pg.wait_for_timeout(900)
    await pg.evaluate("document.getElementById('explore').click()"); await pg.wait_for_timeout(1800)
    await pg.add_style_tag(content=COMMON + (BLANK if page == 2 else ''))
    await pg.evaluate("h=>document.body.insertAdjacentHTML('beforeend',h)", header(page) + footer(page))
    counts = [len(b['children']) for b in obj['branches']]
    await pg.evaluate("""([counts,D,blank])=>{const nm=k=>String(k).split('').map(c=>D[+c]).join('');
      const nodes=[...document.querySelectorAll('#world .node')]; let bi=-1, li=0;
      nodes.forEach(e=>{ if(e.classList.contains('d1')){bi++;li=0;
          const c=document.createElement('i'); c.className='cnt'; c.textContent=nm(counts[bi]);
          c.style.cssText+=';width:44px;height:44px;font-size:22px;top:-22px;inset-inline-end:-22px'; e.appendChild(c);}
        else if(e.classList.contains('d2')){li++; if(blank){const x=document.createElement('span');x.className='ix';x.textContent=nm(li);e.appendChild(x);}}});
      document.getElementById('fitb').click();}""", [counts, D, page == 2])
    await pg.wait_for_timeout(1400)
    await pg.screenshot(path=path + '.png')
    await pg.pdf(path=path + '.pdf', width='297mm', height='210mm', print_background=True)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); ctx = await b.new_context(viewport={'width': 1123, 'height': 794}, device_scale_factor=2)
        await ctx.add_init_script(INIT.replace('__H__', json.dumps(H, ensure_ascii=False)).replace('__V__', var))
        for k in (1, 2):
            pg = await ctx.new_page(); await render(pg, k, OUT + f'_hifz-{slug}-{lang}-{k}'); await pg.close()
        await b.close()
    subprocess.run(['pdfunite', OUT + f'_hifz-{slug}-{lang}-1.pdf', OUT + f'_hifz-{slug}-{lang}-2.pdf', OUT + f'hifz-{slug}-{lang}.pdf'], check=True)
    print('ok', total)
asyncio.run(main())
