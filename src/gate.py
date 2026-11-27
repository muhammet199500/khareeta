# -*- coding: utf-8 -*-
"""Temporary entry gate: the site (and the app, which shows the site) asks for a code.
One code per person. gate.json holds only salted SHA-256 hashes, never the codes themselves.

- Turn off:      set "on": false in gate.json, then build.
- Revoke a code: delete its key (k01, k02…) from gate.json, then build. That person is asked again.
- New codes:     python3 src/tools/gate_keys.py N  (prints the codes once; keep them outside the repo).

This only keeps ordinary visitors out. The site files stay public on GitHub, so it is not real
protection; that needs a server-side gate (planned: Cloudflare + a private repository).
"""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
_P = os.path.join(ROOT, 'gate.json')
GATE = json.load(open(_P, encoding='utf-8')) if os.path.exists(_P) else {'on': False}
FREE = ('privacy.html', '404.html')   # stay public: the store listing links to the privacy policy
START, END = '<!--gate-->', '<!--/gate-->'

T = dict(
    ar=dict(t='الدخول برمز', n='الموقع الآن في مرحلة تجريبية لعدد محدود من الأشخاص. اكتب الرمز الذي أُعطيته.',
            p='مثال: AB12-CD34', b='دخول', e='الرمز غير صحيح. تأكد منه وأعد المحاولة.'),
    tr=dict(t='Kodla giriş', n='Site şu an sınırlı sayıda kişi için deneme aşamasındadır. Size verilen kodu yazın.',
            p='Örnek: AB12-CD34', b='Giriş', e='Kod geçersiz. Kontrol edip tekrar deneyin.'),
)

CSS = """<style>html.gated body>*:not(#gate){display:none!important}
#gate{position:fixed;inset:0;z-index:99;display:grid;place-items:center;padding:24px;background:#0F2E2A;color:#F7F3EA}
#gate .gbox{width:min(380px,100%);text-align:center}
#gate img{width:96px;height:96px;margin:0 auto 14px;display:block}
#gate h1{font-family:var(--hf,serif);color:#D9B26A;font-size:1.6em;margin:0 0 8px}
#gate p{margin:0 0 18px;line-height:1.8;opacity:.9}
#gate input{width:100%;box-sizing:border-box;font:600 1.25em/1 var(--uf,sans-serif);letter-spacing:.12em;text-align:center;direction:ltr;text-transform:uppercase;padding:14px;border-radius:12px;border:1px solid #D9B26A;background:#F7F3EA;color:#0F2E2A}
#gate button{margin-top:12px;width:100%;padding:13px;border:0;border-radius:12px;background:#D9B26A;color:#0F2E2A;font:700 1.05em var(--uf,sans-serif);cursor:pointer}
#gate .gerr{color:#F2B8A8;min-height:1.6em;margin:10px 0 0}
#gate input::placeholder{text-transform:none;letter-spacing:.04em}</style>"""

JS = """<script>(function(){var K=%(keys)s,S=%(salt)s,L='tvh_key',d=document.documentElement,h=null;
try{h=localStorage.getItem(L)}catch(e){}
if(h&&K.indexOf(h)>-1)return;d.classList.add('gated');
function hx(b){return Array.prototype.map.call(new Uint8Array(b),function(x){return('0'+x.toString(16)).slice(-2)}).join('')}
document.addEventListener('DOMContentLoaded',function(){var g=document.createElement('div');g.id='gate';g.setAttribute('role','dialog');g.setAttribute('aria-modal','true');
g.innerHTML=%(form)s;document.body.appendChild(g);var f=g.querySelector('form'),i=f.elements.c,er=g.querySelector('.gerr');i.focus();
f.addEventListener('submit',function(e){e.preventDefault();var c=(i.value||'').toUpperCase().replace(/[^A-Z0-9]/g,'');
crypto.subtle.digest('SHA-256',new TextEncoder().encode(S+':'+c)).then(function(b){var x=hx(b);
if(K.indexOf(x)>-1){try{localStorage.setItem(L,x)}catch(e){}d.classList.remove('gated');g.remove()}else{er.textContent=%(err)s;i.select()}})})})})();</script>"""


def tags(lang, u):
    """Head tags for a page; u = path from the page up to the site root of this language's media."""
    if not GATE.get('on'):
        return ''
    t = T[lang]
    form = (f'<form class="gbox"><img src="{u}media/logo.webp" alt=""><h1>{t["t"]}</h1><p>{t["n"]}</p>'
            f'<input name="c" autocomplete="off" autocapitalize="characters" spellcheck="false" placeholder="{t["p"]}" aria-label="{t["t"]}">'
            f'<button type="submit">{t["b"]}</button><p class="gerr" aria-live="polite"></p></form>')
    js = JS % dict(keys=json.dumps(sorted(GATE['keys'].values())), salt=json.dumps(GATE['salt']),
                   form=json.dumps(form, ensure_ascii=False), err=json.dumps(t['e'], ensure_ascii=False))
    return START + CSS + js + END


def strip_if_free(path, html):
    """Pages that must stay public lose the gate."""
    if path.endswith(FREE) and START in html:
        a, b = html.index(START), html.index(END) + len(END)
        return html[:a] + html[b:]
    return html
