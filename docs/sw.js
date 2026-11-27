/* وتواصوا بالحق · offline support.
   Pages, styles and scripts: network first (so every edit reaches students when they are online),
   falling back to the saved copy when there is no connection.
   Fonts and pictures: saved copy first. Videos are never saved (too large). */
const VERSION = '94c5c84f33e7';
const CACHE = 'wt-' + VERSION;
const PRECACHE = [
 "./",
 "assets/arch.svg",
 "assets/deck-ar.css",
 "assets/deck-tr.css",
 "assets/fonts.css",
 "assets/fonts/OFL.txt",
 "assets/fonts/amiri-arabic-400-normal.woff2",
 "assets/fonts/amiri-arabic-700-normal.woff2",
 "assets/fonts/amiri-latin-400-normal.woff2",
 "assets/fonts/amiri-latin-700-normal.woff2",
 "assets/fonts/amiri-latin-ext-400-normal.woff2",
 "assets/fonts/amiri-latin-ext-700-normal.woff2",
 "assets/fonts/amiri-quran-arabic-400-normal.woff2",
 "assets/fonts/eb-garamond-latin-ext-wght-normal.woff2",
 "assets/fonts/eb-garamond-latin-wght-normal.woff2",
 "assets/fonts/ibm-plex-sans-arabic-arabic-400-normal.woff2",
 "assets/fonts/ibm-plex-sans-arabic-arabic-600-normal.woff2",
 "assets/fonts/ibm-plex-sans-arabic-arabic-700-normal.woff2",
 "assets/fonts/ibm-plex-sans-arabic-latin-400-normal.woff2",
 "assets/fonts/ibm-plex-sans-arabic-latin-600-normal.woff2",
 "assets/fonts/ibm-plex-sans-arabic-latin-700-normal.woff2",
 "assets/fonts/ibm-plex-sans-arabic-latin-ext-400-normal.woff2",
 "assets/fonts/ibm-plex-sans-arabic-latin-ext-600-normal.woff2",
 "assets/fonts/ibm-plex-sans-arabic-latin-ext-700-normal.woff2",
 "assets/fonts/noto-naskh-arabic-arabic-wght-normal.woff2",
 "assets/fonts/noto-naskh-arabic-latin-ext-wght-normal.woff2",
 "assets/fonts/noto-naskh-arabic-latin-wght-normal.woff2",
 "assets/fonts/reem-kufi-arabic-wght-normal.woff2",
 "assets/fonts/reem-kufi-latin-ext-wght-normal.woff2",
 "assets/fonts/reem-kufi-latin-wght-normal.woff2",
 "assets/fonts/source-sans-3-latin-ext-wght-normal.woff2",
 "assets/fonts/source-sans-3-latin-wght-normal.woff2",
 "assets/frieze.svg",
 "assets/site.css",
 "assets/site.js",
 "assets/slides.css",
 "assets/slides.js",
 "assets/summary.css",
 "cards.html",
 "data.js",
 "f1/",
 "f1/qa.html",
 "f1/quiz.html",
 "f1/sharh.html",
 "f1/slides.html",
 "f1/summary.html",
 "f1/text.html",
 "fiqh-muyassar.html",
 "l1/",
 "l1/qa.html",
 "l1/quiz.html",
 "l1/slides.html",
 "l1/summary.html",
 "l1/text.html",
 "l2/",
 "l2/qa.html",
 "l2/quiz.html",
 "l2/slides.html",
 "l2/summary.html",
 "l2/text.html",
 "l3/",
 "l3/qa.html",
 "l3/quiz.html",
 "l3/slides.html",
 "l3/summary.html",
 "l3/text.html",
 "la-ilaha.html",
 "manifest.webmanifest",
 "map.html",
 "media/apple-touch-icon.png",
 "media/icon-192.png",
 "media/logo.webp",
 "media/poster-f1-tr.jpg",
 "media/poster-f1.jpg",
 "media/poster-teaser.jpg",
 "media/poster1-tr.jpg",
 "media/poster1.jpg",
 "privacy.html",
 "quiz-all.html",
 "search.json",
 "tasks.html",
 "tasks.json",
 "tr/cards.html",
 "tr/data_tr.js",
 "tr/f1/",
 "tr/f1/qa.html",
 "tr/f1/quiz.html",
 "tr/f1/sharh.html",
 "tr/f1/slides.html",
 "tr/f1/summary.html",
 "tr/f1/text.html",
 "tr/fiqh-muyassar.html",
 "tr/",
 "tr/l1/",
 "tr/l1/qa.html",
 "tr/l1/quiz.html",
 "tr/l1/slides.html",
 "tr/l1/summary.html",
 "tr/l1/text.html",
 "tr/l2/",
 "tr/l2/qa.html",
 "tr/l2/quiz.html",
 "tr/l2/slides.html",
 "tr/l2/summary.html",
 "tr/l2/text.html",
 "tr/l3/",
 "tr/l3/qa.html",
 "tr/l3/quiz.html",
 "tr/l3/slides.html",
 "tr/l3/summary.html",
 "tr/l3/text.html",
 "tr/la-ilaha.html",
 "tr/manifest.webmanifest",
 "tr/map.html",
 "tr/privacy.html",
 "tr/quiz-all.html",
 "tr/search.json",
 "tr/tasks.html",
 "f1/index.html",
 "l1/index.html",
 "l2/index.html",
 "l3/index.html",
 "tr/f1/index.html",
 "tr/index.html",
 "tr/l1/index.html",
 "tr/l2/index.html",
 "tr/l3/index.html"
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRECACHE.map(u => new Request(u, { cache: 'reload' })))).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith('wt-') && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

const isMedia = url => /\.(mp4|webm|mov|m4a|mp3)$/i.test(url.pathname);
const isStatic = url => /\.(woff2|png|jpe?g|webp|svg|ico)$/i.test(url.pathname);

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin || isMedia(url) || req.headers.has('range')) return;

  if (isStatic(url)) {
    e.respondWith(caches.match(req, { ignoreSearch: true }).then(hit => hit || fetch(req).then(res => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
      return res;
    })));
    return;
  }

  const nav = req.mode === 'navigate';
  const fallback = () => caches.match(req, { ignoreSearch: true }).then(hit => hit ||
      (nav ? caches.match(new URL('index.html', self.registration.scope).href) : null))
    .catch(() => null)
    .then(hit => hit || (nav ? offlinePage(url) : Response.error()));
  const net = fetch(req).then(res => {
    if (res.ok && res.type === 'basic') { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
    // a page reached through a redirect cannot be handed back as is: the browser would show an error
    if (nav && res.redirected) return res.blob().then(b => new Response(b, { status: res.status, statusText: res.statusText, headers: res.headers }));
    return res;
  });
  e.waitUntil(net.catch(() => {}));   // let the saved copy be refreshed even when it was not waited for
  // Network first, but on a slow connection do not keep the student waiting:
  // after WAIT ms the saved copy is shown, and the fresh one is saved for next time.
  e.respondWith(new Promise(resolve => {
    let done = false;
    const finish = r => { if (!done) { done = true; resolve(r); } };
    const timer = setTimeout(() => caches.match(req, { ignoreSearch: true }).then(hit => { if (hit) finish(hit); }).catch(() => {}), WAIT);
    net.then(r => { clearTimeout(timer); finish(r); }, () => { clearTimeout(timer); fallback().then(finish); });
  }));
});
const WAIT = 2500;

/* shown instead of the browser's grey error page when there is no connection and no saved copy */
function offlinePage(url) {
  const tr = /\/tr\//.test(url.pathname);
  const t = tr
    ? { lang: 'tr', dir: 'ltr', h: 'İnternet bağlantısı yok', p: 'Bu sayfa şu anda açılamadı. Bağlantınızı kontrol edip tekrar deneyin.', b: 'Tekrar dene', home: 'Ders Kütüphanesi', name: 'Ve Tevâsav bi’l-Hak' }
    : { lang: 'ar', dir: 'rtl', h: 'لا يوجد اتصال بالإنترنت', p: 'تعذّر فتح هذه الصفحة الآن. تأكّد من اتصالك ثم حاول مرة أخرى.', b: 'حاول مرة أخرى', home: 'مكتبة الدروس', name: 'وتواصوا بالحق' };
  const root = self.registration.scope + (tr ? 'tr/' : '');
  const html = `<!doctype html><html lang="${t.lang}" dir="${t.dir}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${t.name}</title>
<style>body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#0F2E2A;color:#C6D6D0;font-family:'IBM Plex Sans Arabic','Source Sans 3',Tahoma,sans-serif;text-align:center}
main{padding:32px 24px;max-width:420px}img{width:120px;height:auto;margin-bottom:12px}h1{color:#F3DFA8;font-size:24px;margin:0 0 10px}p{font-size:17px;line-height:1.7;margin:0 0 26px}
button{font:inherit;font-size:17px;font-weight:600;background:#D9B26A;color:#0F2E2A;border:0;border-radius:30px;padding:12px 30px;cursor:pointer}a{display:block;margin-top:18px;color:#D9B26A;font-size:15px}</style></head>
<body><main><img src="${self.registration.scope}media/logo.webp" alt=""><h1>${t.h}</h1><p>${t.p}</p><button onclick="location.reload()">${t.b}</button><a href="${root}index.html">${t.home}</a></main></body></html>`;
  return new Response(html, { status: 503, headers: { 'Content-Type': 'text/html; charset=utf-8' } });
}

/* ---- daily-task reminders: the push carries no text; today's task is read from tasks.json ---- */
const SETTINGS_URL = new URL('__wt_settings.json', self.registration.scope).href;
async function settings() { try { const c = await caches.open('wt-settings'); const r = await c.match(SETTINGS_URL); return r ? await r.json() : {}; } catch (e) { return {}; } }
async function saveSettings(v) { try { const c = await caches.open('wt-settings'); await c.put(SETTINGS_URL, new Response(JSON.stringify(v), { headers: { 'Content-Type': 'application/json' } })); } catch (e) {} }
const pad2 = n => String(n).padStart(2, '0');
const todayISO = () => { const d = new Date(); return d.getFullYear() + '-' + pad2(d.getMonth() + 1) + '-' + pad2(d.getDate()); };

self.addEventListener('push', e => {
  e.waitUntil((async () => {
    const s = await settings(), today = todayISO();
    let tasks = null;
    const url = new URL('tasks.json', self.registration.scope).href;
    try { const r = await fetch(url, { cache: 'no-cache' }); if (r.ok) { tasks = await r.clone().json(); caches.open(CACHE).then(c => c.put(url, r)); } } catch (err) {}
    if (!tasks) { const hit = await caches.match(url, { ignoreSearch: true }); if (hit) tasks = await hit.json(); }
    const day = tasks && (tasks.weeks || []).flatMap(w => w.days || []).find(d => d.date === today);
    const lang = s.lang || 'ar';
    if (day && (s.done || {})[today]) return;          // already finished on this device
    const pick = o => o ? (typeof o === 'string' ? o : (o[lang] || o.ar || '')) : '';
    const body = day ? [pick(day.segment), day[lang] || day.ar].filter(Boolean).join('\n') : (lang === 'tr' ? 'Bugünün ödevine göz atın.' : 'افتح واجب اليوم.');
    await self.registration.showNotification(s.title || 'واجب اليوم · وتواصوا بالحق', {
      body, tag: 'wt-task', renotify: true, requireInteraction: true,
      vibrate: [900, 300, 900, 300, 900], /* three long vibrations (Android; iPhone uses its own) */
      lang, dir: lang === 'ar' ? 'rtl' : 'ltr',
      icon: new URL('media/icon-192.png', self.registration.scope).href,
      badge: new URL('media/icon-192.png', self.registration.scope).href,
      data: { page: s.page || self.registration.scope, date: today },
      actions: [{ action: 'done', title: s.doneLabel || 'أنهيتُ' }],
    });
  })());
});

self.addEventListener('notificationclick', e => {
  e.notification.close();
  const { page, date } = e.notification.data || {};
  if (e.action === 'done') {
    e.waitUntil((async () => {
      const s = await settings(); s.done = Object.assign(s.done || {}, { [date]: 1 }); await saveSettings(s);
      if (s.api && s.id) await fetch(s.api + '/done', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ id: s.id, date }) }).catch(() => {});
    })());
    return;
  }
  e.waitUntil(self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then(list => {
    for (const c of list) if (c.url.startsWith(page) && 'focus' in c) return c.focus();
    return self.clients.openWindow(page);
  }));
});
