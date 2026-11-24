/* وتواصوا بالحق · offline support.
   Pages, styles and scripts: network first (so every edit reaches students when they are online),
   falling back to the saved copy when there is no connection.
   Fonts and pictures: saved copy first. Videos are never saved (too large). */
const VERSION = '__VERSION__';
const CACHE = 'wt-' + VERSION;
const PRECACHE = __PRECACHE__;

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

  e.respondWith(fetch(req).then(res => {
    if (res.ok && res.type === 'basic') { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
    return res;
  }).catch(() => caches.match(req, { ignoreSearch: true }).then(hit => hit ||
    (req.mode === 'navigate' ? caches.match(new URL('index.html', self.registration.scope).href) : Response.error()))));
});

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
      vibrate: [900, 300, 900, 300, 900],   // three long vibrations (Android; iPhone uses its own) lang, dir: lang === 'ar' ? 'rtl' : 'ltr',
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
