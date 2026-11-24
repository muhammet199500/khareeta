/* وتواصوا بالحق · offline support.
   Pages, styles and scripts: network first (so every edit reaches students when they are online),
   falling back to the saved copy when there is no connection.
   Fonts and pictures: saved copy first. Videos are never saved (too large). */
const VERSION = 'f8ea7647b475';
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
 "data.js",
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
 "manifest.webmanifest",
 "map.html",
 "media/apple-touch-icon.png",
 "media/icon-192.png",
 "media/logo.webp",
 "media/poster-teaser.jpg",
 "media/poster1-tr.jpg",
 "media/poster1.jpg",
 "tr/data_tr.js",
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
 "tr/manifest.webmanifest",
 "tr/map.html",
 "l1/index.html",
 "l2/index.html",
 "tr/index.html",
 "tr/l1/index.html",
 "tr/l2/index.html"
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

  e.respondWith(fetch(req).then(res => {
    if (res.ok && res.type === 'basic') { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
    return res;
  }).catch(() => caches.match(req, { ignoreSearch: true }).then(hit => hit ||
    (req.mode === 'navigate' ? caches.match(new URL('index.html', self.registration.scope).href) : Response.error()))));
});
