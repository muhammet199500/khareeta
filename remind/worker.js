/* وتواصوا بالحق · daily-task reminders (Cloudflare Worker)
 *
 * The site (GitHub Pages) asks the student's permission, then sends the browser's push subscription here.
 * Every hour, for every subscribed device, the worker looks at the device's own clock: at 10, 12, 14 … 22
 * (local time) it sends a reminder if today has a task and the student has not pressed «I finished» yet.
 *
 * No names, no accounts: a device is known only by a random id. Nothing else about the student is kept.
 * The push carries no text; the site's service worker reads today's task from tasks.json and shows it.
 *
 * Storage (KV, binding REMIND):
 *   vapid           → the key pair used to sign pushes (made once, never leaves Cloudflare)
 *   s:<id>          → value: the push subscription; metadata: { tz, lang, done: 'YYYY-MM-DD' | '' }
 * The cron runs once an hour, so each device gets at most one reminder per listed hour.
 */
const SITE = 'https://tevhidim.com/';
const ORIGINS = ['https://tevhidim.com', 'https://www.tevhidim.com', 'https://muhammet199500.github.io'];
const HOURS = [10, 12, 14, 16, 18, 20, 22];          // reminder hours, on the student's clock

const cors = origin => ({
  'Access-Control-Allow-Origin': ORIGINS.includes(origin) || /^http:\/\/localhost(:\d+)?$/.test(origin || '') ? origin : ORIGINS[0],
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Max-Age': '86400',
});
const json = (obj, origin, status = 200) => new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json', ...cors(origin) } });

const b64u = buf => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const b64uText = s => b64u(new TextEncoder().encode(s));

async function vapid(env) {
  let v = await env.REMIND.get('vapid', 'json');
  if (!v) {
    const kp = await crypto.subtle.generateKey({ name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign', 'verify']);
    const jwk = await crypto.subtle.exportKey('jwk', kp.privateKey);
    const raw = await crypto.subtle.exportKey('raw', kp.publicKey);
    v = { jwk, pub: b64u(raw) };
    await env.REMIND.put('vapid', JSON.stringify(v));
  }
  return v;
}

async function vapidHeader(v, endpoint) {
  const aud = new URL(endpoint).origin;
  const head = b64uText(JSON.stringify({ typ: 'JWT', alg: 'ES256' }));
  const body = b64uText(JSON.stringify({ aud, exp: Math.floor(Date.now() / 1000) + 12 * 3600, sub: 'mailto:muhammet199500@users.noreply.github.com' }));
  const key = await crypto.subtle.importKey('jwk', v.jwk, { name: 'ECDSA', namedCurve: 'P-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign({ name: 'ECDSA', hash: 'SHA-256' }, key, new TextEncoder().encode(head + '.' + body));
  return `vapid t=${head}.${body}.${b64u(sig)}, k=${v.pub}`;
}

/* local date "YYYY-MM-DD" and hour (0–23) in a time zone */
function localNow(tz, now = new Date()) {
  let parts;
  try { parts = new Intl.DateTimeFormat('en-CA', { timeZone: tz, year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', hourCycle: 'h23' }).formatToParts(now); }
  catch (e) { parts = new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Istanbul', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', hourCycle: 'h23' }).formatToParts(now); }
  const g = t => parts.find(p => p.type === t).value;
  return { date: `${g('year')}-${g('month')}-${g('day')}`, hour: +g('hour') % 24 };
}

async function taskDates() {
  try {
    const r = await fetch(SITE + 'tasks.json', { cf: { cacheTtl: 300 } });
    const d = await r.json();
    return new Set((d.weeks || []).flatMap(w => (w.days || []).map(x => x.date)));
  } catch (e) { return new Set(); }
}

async function remindAll(env, now = new Date()) {
  const dates = await taskDates();
  if (!dates.size) return { sent: 0 };
  const v = await vapid(env);
  let cursor, sent = 0, removed = 0;
  do {
    const page = await env.REMIND.list({ prefix: 's:', cursor });
    cursor = page.list_complete ? null : page.cursor;
    for (const k of page.keys) {
      const m = k.metadata || {};
      const { date, hour } = localNow(m.tz, now);
      if (!HOURS.includes(hour) || !dates.has(date) || m.done === date) continue;
      const sub = await env.REMIND.get(k.name, 'json');
      if (!sub || !sub.endpoint) continue;
      const res = await fetch(sub.endpoint, { method: 'POST', headers: { TTL: '3600', Urgency: 'normal', 'Content-Length': '0', Authorization: await vapidHeader(v, sub.endpoint) } });
      if (res.status === 404 || res.status === 410) { await env.REMIND.delete(k.name); removed++; continue; }
      if (res.ok) sent++;   // no write here: the free plan allows 1,000 writes a day, kept for «I finished» presses
    }
  } while (cursor);
  return { sent, removed };
}

/* only the browsers' own push services: Google (Chrome, Edge on Android…), Mozilla, Apple, Microsoft */
const PUSH_HOSTS = [/^fcm\.googleapis\.com$/, /^android\.googleapis\.com$/, /(^|\.)push\.services\.mozilla\.com$/, /(^|\.)push\.apple\.com$/, /(^|\.)notify\.windows\.com$/];
const pushHost = e => { try { const u = new URL(e); return u.protocol === 'https:' && PUSH_HOSTS.some(r => r.test(u.hostname)); } catch (x) { return false; } };
const validId = id => typeof id === 'string' && /^[A-Za-z0-9_-]{16,64}$/.test(id);
const validDate = d => typeof d === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(d);

export default {
  async fetch(req, env) {
    const origin = req.headers.get('Origin');
    if (req.method === 'OPTIONS') return new Response(null, { headers: cors(origin) });
    const url = new URL(req.url);
    if (req.method === 'GET' && url.pathname === '/key') return json({ key: (await vapid(env)).pub }, origin);
    if (req.method === 'GET' && url.pathname === '/') return json({ ok: true, service: 'wt-remind' }, origin);
    if (req.method !== 'POST') return json({ error: 'not found' }, origin, 404);
    let b; try { b = await req.json(); } catch (e) { return json({ error: 'bad json' }, origin, 400); }

    if (url.pathname === '/subscribe') {
      const s = b.subscription;
      if (!s || typeof s.endpoint !== 'string' || !pushHost(s.endpoint) || JSON.stringify(s).length > 4000) return json({ error: 'bad subscription' }, origin, 400);
      const id = validId(b.id) ? b.id : b64u(crypto.getRandomValues(new Uint8Array(18)));
      const old = await env.REMIND.getWithMetadata('s:' + id, 'json');
      const meta = { tz: String(b.tz || 'Europe/Istanbul').slice(0, 64), lang: b.lang === 'tr' ? 'tr' : 'ar', done: (old.metadata || {}).done || '' };
      await env.REMIND.put('s:' + id, JSON.stringify({ endpoint: s.endpoint, keys: s.keys || {} }), { metadata: meta });
      return json({ id }, origin);
    }
    if (!validId(b.id)) return json({ error: 'bad id' }, origin, 400);
    const cur = await env.REMIND.getWithMetadata('s:' + b.id, 'json');
    if (url.pathname === '/unsubscribe') { if (cur.value) await env.REMIND.delete('s:' + b.id); return json({ ok: true }, origin); }
    if (!cur.value) return json({ error: 'unknown id' }, origin, 404);
    if (url.pathname === '/done' || url.pathname === '/undone') {
      if (!validDate(b.date)) return json({ error: 'bad date' }, origin, 400);
      const m = cur.metadata || {};
      const done = url.pathname === '/done' ? b.date : (m.done === b.date ? '' : m.done || '');
      if (done !== m.done) await env.REMIND.put('s:' + b.id, JSON.stringify(cur.value), { metadata: { ...m, done } });
      return json({ ok: true }, origin);
    }
    return json({ error: 'not found' }, origin, 404);
  },
  async scheduled(event, env, ctx) {
    ctx.waitUntil(remindAll(env, new Date(event.scheduledTime)));
  },
};
