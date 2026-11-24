/* وتواصوا بالحق · shared page behaviour */
(function () {
  const $ = (s, r) => (r || document).querySelector(s);
  const $$ = (s, r) => Array.from((r || document).querySelectorAll(s));
  const AR = document.documentElement.lang === 'ar';
  const num = n => AR ? String(n).replace(/\d/g, d => '٠١٢٣٤٥٦٧٨٩'[d]) : String(n);
  const T = AR ? {
    show: 'أظهر الجواب', hide: 'أخفِ الجواب', all: 'أظهر كل الأجوبة', none: 'أخفِ كل الأجوبة',
    soon: 'فيديو هذا الدرس يُضاف قريبًا',
    qOf: (i, n) => 'السؤال ' + i + ' من ' + n
  } : {
    show: 'Cevabı göster', hide: 'Cevabı gizle', all: 'Bütün cevapları göster', none: 'Bütün cevapları gizle',
    soon: 'Bu dersin videosu yakında eklenecek',
    qOf: (i, n) => 'Soru ' + i + ' / ' + n
  };

  /* ---- progress, kept on this device only ---- */
  const PKEY = 'wt.progress.v1', TOOLS = ['text', 'slides', 'map', 'qa', 'quiz'];
  const P = {
    get() { try { return JSON.parse(localStorage.getItem(PKEY)) || {}; } catch (e) { return {}; } },
    set(o) { try { localStorage.setItem(PKEY, JSON.stringify(o)); } catch (e) {} },
    mark(n, k, extra) { const o = P.get(), l = o[n] = o[n] || {}; if (k) l[k] = 1; if (extra) Object.assign(l, extra); P.set(o); },
    unmark(n, k) { const o = P.get(); if (o[n]) { delete o[n][k]; P.set(o); } }
  };
  const TP = AR ? {
    done: (c, n) => 'أنجزت ' + num(c) + ' من ' + num(n) + ' أدوات في هذا الدرس',
    short: (c, n) => 'أنجزت ' + num(c) + ' من ' + num(n),
    complete: '✓ أتممتَ هذا الدرس',
    best: (s, t) => 'أفضل نتيجة: ' + num(s) + ' من ' + num(t),
    resetQ: 'هل تريد مسح تقدّمك المحفوظ على هذا الجهاز؟'
  } : {
    done: (c, n) => 'Bu derste ' + n + ' araçtan ' + c + ' tanesi tamamlandı',
    short: (c, n) => c + '/' + n + ' tamamlandı',
    complete: '✓ Bu dersi tamamladınız',
    best: (s, t) => 'En iyi sonuç: ' + s + '/' + t,
    resetQ: 'Bu cihazda kayıtlı ilerlemeniz silinsin mi?'
  };
  const toolOf = a => {
    const u = new URL(a.getAttribute('href'), location.href);
    let m = /\/l(\d+)\/(text|slides|qa|quiz)\.html$/.exec(u.pathname); if (m) return [m[1], m[2]];
    m = /map\.html$/.test(u.pathname) && /^#l(\d+)$/.exec(u.hash); return m ? [m[1], 'map'] : null;
  };
  function paint() {
    const o = P.get();
    $$('a.chip, a.tool').forEach(a => {
      const k = toolOf(a); if (!k) return;
      const l = o[k[0]] || {};
      a.classList.toggle('done', !!l[k[1]]);
      if (k[1] === 'quiz' && a.classList.contains('tool')) {
        let b = a.querySelector('.best');
        if (l.best) { if (!b) { b = document.createElement('span'); b.className = 'best'; a.lastElementChild.appendChild(b); } b.textContent = TP.best(l.best[0], l.best[1]); }
        else if (b) b.remove();
      }
    });
    $$('.lprog[data-lesson], .prog[data-lesson]').forEach(e => {
      const l = o[e.dataset.lesson] || {}, c = TOOLS.filter(k => l[k]).length;
      e.hidden = !c && !l.lesson;
      e.innerHTML = (l.lesson ? `<span class="lesson-ok">${TP.complete}</span>` : '') +
        (c ? `<span class="pbar"><i style="width:${100 * c / TOOLS.length}%"></i></span><span>${(e.classList.contains('lprog') ? TP.short : TP.done)(c, TOOLS.length)}</span>` : '');
    });
    $$('.donebtn[data-done]').forEach(b => {
      const [n, k] = b.dataset.done.split(':'), on = !!(o[n] || {})[k];
      b.classList.toggle('on', on); b.setAttribute('aria-pressed', on); b.textContent = on ? b.dataset.on : b.dataset.off;
    });
    $$('.lrow').forEach(r => { const p = r.querySelector('.lprog'); r.classList.toggle('complete', !!(p && (o[p.dataset.lesson] || {}).lesson)); });
    const r = $('#progReset'); if (r) r.hidden = !Object.keys(o).length;
  }
  /* the student presses «I finished» themselves; pressing again undoes it */
  $$('.donebtn[data-done]').forEach(b => b.addEventListener('click', () => {
    const [n, k] = b.dataset.done.split(':');
    if ((P.get()[n] || {})[k]) P.unmark(n, k); else P.mark(n, k);
    paint();
  }));
  paint();
  addEventListener('pageshow', paint);
  const rb = $('#progReset');
  if (rb) rb.addEventListener('click', () => { if (confirm(TP.resetQ)) { try { localStorage.removeItem(PKEY); } catch (e) {} paint(); } });

  /* ---- font size for reading, remembered ---- */
  const FS = [.9, 1, 1.12, 1.25, 1.4];
  if ($('.fs-ctl')) {
    let i = 1; try { const v = localStorage.getItem('wt.fs'); if (v !== null && FS[+v]) i = +v; } catch (e) {}
    const apply = () => {
      document.documentElement.style.setProperty('--fs', FS[i]);
      $$('.fs-ctl [data-fs]').forEach(b => { b.disabled = +b.dataset.fs < 0 ? i === 0 : i === FS.length - 1; });
    };
    apply();
    $$('.fs-ctl').forEach(c => c.addEventListener('click', e => {
      const b = e.target.closest('[data-fs]'); if (!b) return;
      i = Math.max(0, Math.min(FS.length - 1, i + +b.dataset.fs));
      try { localStorage.setItem('wt.fs', i); } catch (err) {}
      apply();
    }));
  }

  /* ---- install as an app ---- */
  const cta = $('#appCta');
  const standalone = matchMedia('(display-mode: standalone)').matches || navigator.standalone;
  if (cta && !standalone) {
    let ev = null;
    addEventListener('beforeinstallprompt', e => { e.preventDefault(); ev = e; cta.hidden = false; $('#installBtn').hidden = false; });
    $('#installBtn').addEventListener('click', async () => { if (!ev) return; ev.prompt(); try { await ev.userChoice; } catch (e) {} ev = null; cta.hidden = true; });
    addEventListener('appinstalled', () => { cta.hidden = true; });
    if (/iphone|ipad|ipod/i.test(navigator.userAgent) && !/crios|fxios/i.test(navigator.userAgent)) { cta.hidden = false; $('#iosHint').hidden = false; }
  }

  /* ---- video: show a calm placeholder when the file is not uploaded yet ---- */
  $$('.player video').forEach(v => {
    const fail = () => {
      const box = v.closest('.player'); if (!box || box.querySelector('.soon')) return;
      const s = document.createElement('div'); s.className = 'soon';
      const poster = v.getAttribute('poster');
      if (poster) {
        s.classList.add('has-poster');
        s.style.backgroundImage = 'linear-gradient(rgba(15,46,42,0) 55%, rgba(15,46,42,.9)), url("' + poster + '")';
        s.innerHTML = '<span class="cap">' + (box.dataset.soon || T.soon) + '</span>';
      } else s.innerHTML = '<div>' + (box.dataset.logo ? '<img src="' + box.dataset.logo + '" alt="">' : '') + (box.dataset.soon || T.soon) + '</div>';
      box.appendChild(s); v.hidden = true;
    };
    v.addEventListener('error', fail, true);
    const src = v.querySelector('source'); if (src) src.addEventListener('error', fail);
    if (v.dataset.check !== undefined) fetch(v.currentSrc || v.getAttribute('src') || (src && src.getAttribute('src')), { method: 'HEAD' }).then(r => { if (!r.ok) fail(); }).catch(() => {});
  });

  /* ---- summary image dialog ---- */
  const dlg = $('#dlg');
  if (dlg) {
    $$('[data-img]').forEach(b => b.addEventListener('click', e => {
      e.preventDefault();
      $('#dlgImg').src = b.dataset.img; $('#dlgImg').alt = b.dataset.title || ''; $('#dlgT').textContent = b.dataset.title || '';
      const dl = $('#dlgDl'); if (dl) dl.href = b.dataset.img;
      try { dlg.showModal(); } catch (err) { dlg.setAttribute('open', ''); }
    }));
    $('#dlgX').addEventListener('click', () => dlg.close ? dlg.close() : dlg.removeAttribute('open'));
    dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });
  }

  /* ---- Q & A: reveal answers ---- */
  const qcards = $$('.qcard');
  if (qcards.length) {
    const setOne = (c, open) => {
      const a = c.querySelector('.qa-a'), b = c.querySelector('.rev');
      a.hidden = !open; b.textContent = open ? T.hide : T.show; b.setAttribute('aria-expanded', open);
    };
    qcards.forEach(c => { setOne(c, false); c.querySelector('.rev').addEventListener('click', () => setOne(c, c.querySelector('.qa-a').hidden)); });
    const all = $('#qaAll');
    if (all) all.addEventListener('click', () => {
      const open = qcards.some(c => c.querySelector('.qa-a').hidden);
      qcards.forEach(c => setOne(c, open)); all.textContent = open ? T.none : T.all;
    });
  }

  /* ---- table of contents: highlight the section in view ---- */
  const toc = $$('.toc a[href^="#"]');
  if (toc.length && 'IntersectionObserver' in window) {
    const map = new Map(toc.map(a => [decodeURIComponent(a.getAttribute('href').slice(1)), a]));
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return;
      toc.forEach(a => a.classList.remove('on'));
      const a = map.get(e.target.id); if (a) a.classList.add('on');
    }), { rootMargin: '-20% 0px -70% 0px' });
    map.forEach((a, id) => { const h = document.getElementById(id); if (h) io.observe(h); });
    $$('.toc details a').forEach(a => a.addEventListener('click', () => { const d = a.closest('details'); if (d && innerWidth < 960) d.open = false; }));
  }

  /* ---- standalone quiz ---- */
  const qz = $('#quiz');
  if (qz && window.LESSONS) {
    const L = window.LESSONS[+qz.dataset.lesson - 1], U = L.ui, Q = L.quiz, LET = U.letters || ['A', 'B', 'C', 'D'];
    let qi = 0, score = 0, wrong = [], done = false;
    const card = $('#qcard'), res = $('#qres');
    function render() {
      done = false;
      const it = Q[qi];
      $('#qprog').textContent = U.qOf(U.digits(qi + 1), U.digits(Q.length));
      $('#qscoreNow').textContent = AR ? ('الصحيح: ' + num(score)) : ('Doğru: ' + score);
      $('#qbar').style.width = (100 * qi / Q.length) + '%';
      $('#qtext').textContent = it.q;
      $('#qopts').innerHTML = it.o.map((t, i) => `<button class="qopt" data-i="${i}"><span class="ql">${LET[i]}</span><span>${t}</span></button>`).join('');
      $$('#qopts .qopt').forEach(b => b.onclick = () => answer(+b.dataset.i));
      $('#qfb').innerHTML = ''; $('#qnext').hidden = true; card.hidden = false; res.hidden = true;
    }
    function answer(i) {
      if (done) return; done = true;
      const it = Q[qi], ok = i === it.a; if (ok) score++; else wrong.push(qi);
      $$('#qopts .qopt').forEach((b, k) => { b.disabled = true; if (k === it.a) b.classList.add('right'); else if (k === i) b.classList.add('bad'); });
      $('#qfb').innerHTML = `<p class="${ok ? 'ok' : 'no'}">${ok ? U.correct : U.wrong}</p><p>${it.x}</p>`;
      const n = $('#qnext'); n.textContent = qi + 1 < Q.length ? U.next : U.finish; n.hidden = false; n.focus();
    }
    $('#qnext').onclick = () => { if (qi + 1 < Q.length) { qi++; render(); qz.scrollIntoView({ block: 'start' }); } else finish(); };
    function finish() {
      card.hidden = true; res.hidden = false;
      $('#qbar').style.width = '100%';
      const pct = score / Q.length, r = 52, c = 2 * Math.PI * r;
      $('#qring').innerHTML = `<circle cx="60" cy="60" r="${r}" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="12"/><circle cx="60" cy="60" r="${r}" fill="none" stroke="#D9B26A" stroke-width="12" stroke-linecap="round" stroke-dasharray="${c * pct} ${c}" transform="rotate(-90 60 60)"/><text x="60" y="68" text-anchor="middle" font-size="26" font-weight="700" fill="#F7F3EA" font-family="sans-serif">${AR ? num(Math.round(pct * 100)) + '٪' : '%' + Math.round(pct * 100)}</text>`;
      $('#qscore').textContent = U.score(U.digits(score), U.digits(Q.length));
      $('#qmsg').textContent = score === Q.length ? U.great : score >= Q.length - 2 ? U.good : U.review;
      $('#qwrong').innerHTML = wrong.map(k => `<li><b>${U.digits(k + 1)}.</b> ${Q[k].q}<br><span class="ans">✓ ${Q[k].o[Q[k].a]}</span></li>`).join('');
      $('#qwrongT').hidden = !wrong.length;
      const n = qz.dataset.lesson, prev = (P.get()[n] || {}).best;
      if (!prev || score / Q.length >= prev[0] / prev[1]) P.mark(n, null, { best: [score, Q.length] });
      paint();
      res.querySelector('button, a').focus();
    }
    $('#qretry').onclick = () => { qi = 0; score = 0; wrong = []; render(); };
    render();
  }
})();

/* ---- library: remember the last lesson page opened, search, categories ---- */
(function () {
  const $ = s => document.querySelector(s), $$ = s => Array.from(document.querySelectorAll(s));
  const AR = document.documentElement.lang === 'ar', LKEY = 'wt.last.' + (AR ? 'ar' : 'tr');
  const num = n => AR ? String(n).replace(/\d/g, d => '٠١٢٣٤٥٦٧٨٩'[d]) : String(n);
  const get = k => { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } };
  /* on a lesson page (l1/…, tr/l1/…) note where the student is */
  const m = /\/l(\d+)\/([\w-]+\.html)?$/.exec(location.pathname);
  if (m) { try { localStorage.setItem(LKEY, JSON.stringify({ n: m[1], p: 'l' + m[1] + '/' + (m[2] || 'index.html') })); } catch (e) {} }
  const dataEl = $('#libData'); if (!dataEl) return;
  const D = JSON.parse(dataEl.textContent), prog = get('wt.progress.v1') || {};
  const TOOLS = ['text', 'slides', 'map', 'qa', 'quiz'];
  /* continue where you stopped */
  const last = get(LKEY);
  if (last && D[last.n]) {
    $('#contT').textContent = D[last.n].t; $('#contW').textContent = D[last.n].w;
    $('#contA').href = last.p; $('#contBand').hidden = false;
  }
  /* each series card: how many of its published lessons the student completed */
  $$('.sprog[data-lessons]').forEach(e => {
    const ls = e.dataset.lessons.split(','), c = ls.filter(n => (prog[n] || {}).lesson).length;
    if (!c) return;
    e.hidden = false;
    e.innerHTML = `<span class="pbar"><i style="width:${100 * c / ls.length}%"></i></span><span>${AR ? 'أتممتَ ' + num(c) + ' من ' + num(ls.length) : c + '/' + ls.length + ' tamamlandı'}</span>`;
  });
  /* search + categories */
  const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ًͯ-ٰٟـ’'ʿ‘]/g, '')
    .replace(/[أإآٱ]/g, 'ا').replace(/ى/g, 'ي').replace(/ة/g, 'ه').replace(/ı/g, 'i').replace(/\s+/g, ' ').trim();
  let cat = '';
  const q = $('#libQ');
  function apply() {
    const t = norm(q.value || '');
    let shown = 0;
    $$('.scard').forEach(c => { const ok = (!cat || c.dataset.cat === cat) && (!t || norm(c.dataset.q).includes(t)); c.hidden = !ok; if (ok) shown++; });
    let rowsShown = 0;
    $$('#latest .lrow').forEach(r => { const ok = !t || norm(r.dataset.q).includes(t); r.hidden = !ok; if (ok) rowsShown++; });
    $('#latest').hidden = !rowsShown;
    $('#noResult').hidden = !!(shown || rowsShown);
  }
  $$('.cats button').forEach(b => b.addEventListener('click', () => {
    cat = b.dataset.cat; $$('.cats button').forEach(x => x.classList.toggle('on', x === b)); apply();
  }));
  q.addEventListener('input', apply);
})();

/* ---- weekly tasks: today's task, daily check-in, «I finished», and reminders that repeat until the student presses it ---- */
(function () {
  const box = document.querySelector('[data-remind]'); if (!box) return;
  const $ = s => document.querySelector(s);
  const AR = document.documentElement.lang === 'ar', LANG = AR ? 'ar' : 'tr';
  const TS = JSON.parse(box.dataset.ts || '{}'), T = k => TS[k] || '';
  const API = box.dataset.remind, TASKS = new URL(box.dataset.tasks, location.href).href;
  const ROOT = TASKS.replace(/tasks\.json$/, ''), SETTINGS = ROOT + '__wt_settings.json';
  const DKEY = 'wt.tasks.v1', LKEY = 'wt.tasklog.v1', IDKEY = 'wt.remind.id';
  const pad = n => String(n).padStart(2, '0');
  const iso = d => d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate());
  const TODAY = iso(new Date());
  const num = n => AR ? String(n).replace(/\d/g, d => '٠١٢٣٤٥٦٧٨٩'[d]) : String(n);
  const L = o => o == null ? '' : typeof o === 'string' ? o : (o[LANG] || o.ar || '');
  const ls = { get(k, f) { try { const v = localStorage.getItem(k); return v === null ? f : JSON.parse(v); } catch (e) { return f; } },
               set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} } };
  const post = (path, body) => fetch(API + path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) }).then(r => r.json());
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };

  /* settings shared with the service worker (it cannot read localStorage) */
  async function readSW() { try { const c = await caches.open('wt-settings'); const r = await c.match(SETTINGS); return r ? await r.json() : {}; } catch (e) { return {}; } }
  async function writeSW(extra) {
    try {
      const v = Object.assign(await readSW(), { lang: LANG, api: API, page: ROOT + (AR ? '' : 'tr/') + 'tasks.html', title: T('nTitle'), doneLabel: T('nDone'), id: ls.get(IDKEY, null), done: ls.get(DKEY, {}) }, extra || {});
      const c = await caches.open('wt-settings'); await c.put(SETTINGS, new Response(JSON.stringify(v), { headers: { 'Content-Type': 'application/json' } }));
    } catch (e) {}
  }
  async function mergeFromSW() { const v = await readSW(); if (v.done) ls.set(DKEY, Object.assign(ls.get(DKEY, {}), v.done)); }

  function setDone(date, on) {
    const d = ls.get(DKEY, {}); if (on) d[date] = 1; else delete d[date]; ls.set(DKEY, d);
    const id = ls.get(IDKEY, null);
    if (id && date === TODAY) post(on ? '/done' : '/undone', { id, date }).catch(() => {});
    writeSW();
  }
  const log = { get: k => (ls.get(LKEY, {})[k] || {}), set(k, patch) { const all = ls.get(LKEY, {}); all[k] = Object.assign(all[k] || {}, patch); ls.set(LKEY, all); } };
  const fmt = new Intl.DateTimeFormat(AR ? 'ar-u-nu-arab' : 'tr-TR', { weekday: 'long', day: 'numeric', month: 'long' });
  const dayName = s => { const [y, m, d] = s.split('-').map(Number); return fmt.format(new Date(y, m - 1, d)); };
  function doneBtn(btn, date) {
    const paint = () => { const on = !!ls.get(DKEY, {})[date]; btn.classList.toggle('on', on); btn.setAttribute('aria-pressed', on); btn.textContent = on ? T('doneOn') : T('doneOff'); };
    btn.addEventListener('click', () => { setDone(date, !ls.get(DKEY, {})[date]); paint(); });
    paint();
  }
  const link = (href, label) => { const a = el('a', 'go', label + (AR ? ' ←' : ' →')); a.href = ROOT + (AR ? '' : 'tr/') + href; return a; };

  /* yes / no pair stored in the day's log */
  function yesNo(key, field, label, onChange) {
    const row = el('div', 'yn'), lab = el('span', 'ynl', label), g = el('div', 'yng'); g.setAttribute('role', 'group'); g.setAttribute('aria-label', label);
    const mk = (v, t) => { const b = el('button', 'ynb', t); b.type = 'button'; b.dataset.v = v; return b; };
    const by = mk(1, T('yes')), bn = mk(0, T('no'));
    const paint = () => { const v = log.get(key)[field]; [by, bn].forEach(b => { const on = v === +b.dataset.v; b.classList.toggle('on', on); b.setAttribute('aria-pressed', on); }); };
    [by, bn].forEach(b => b.addEventListener('click', () => { const cur = log.get(key)[field]; log.set(key, { [field]: cur === +b.dataset.v ? null : +b.dataset.v }); paint(); onChange && onChange(); }));
    g.append(by, bn); row.append(lab, g); paint(); return row;
  }
  function note(key, field, label, ph) {
    const w = el('label', 'tnote'); w.append(el('span', 'ynl', label));
    const ta = el('textarea'); ta.rows = 2; ta.placeholder = ph; ta.value = log.get(key)[field] || '';
    ta.addEventListener('input', () => log.set(key, { [field]: ta.value }));
    w.append(ta); return w;
  }

  function renderIntro(week) {
    const host = $('#wkIntro'); if (!host) return;
    const h = el('div', 'wkhead'); h.append(el('h2', null, L(week.title))); if (week.sub) h.append(el('p', 'wksub', L(week.sub)));
    (week.intro && week.intro[LANG] || []).forEach(t => h.append(el('p', 'wkp', t)));
    if (week.remember) h.append(el('p', 'wkrem', L(week.remember)));
    host.append(h);
    [['goal', 'goalT', 'ul'], ['steps', 'stepsT', 'ol']].forEach(([k, t, tag]) => {
      const items = week[k] && (week[k][LANG] || week[k].ar); if (!items) return;
      const d = el('details', 'wkdet'); d.append(el('summary', null, T(t)));
      const list = el(tag); items.forEach(x => list.append(el('li', null, x))); d.append(list); host.append(d);
    });
  }

  function renderDay(week, d, first, last) {
    const li = el('li', 'tday' + (d.date === TODAY ? ' now' : d.date > TODAY ? ' later' : ''));
    const top = el('p', 'tdate', dayName(d.date)); if (d.date === TODAY) top.append(el('span', 'ttag', T('todayTag'))); li.append(top);
    if (d.segment) li.append(el('p', 'tseg', L(d.segment)));
    li.append(el('p', 'ttext', L(d)));
    if (d.href) li.append(link(d.href, T('open')));
    if (week.track) {
      const k = d.date, f = el('div', 'track'); f.append(el('p', 'trackT', T('trackT')));
      const why = note(k, 'why', T('why'), T('whyPh'));
      const showWhy = () => { const v = log.get(k); why.hidden = !(v.seg === 0 || v.kept === 0 || (v.why || '').trim()); };
      f.append(yesNo(k, 'seg', T('tSeg'), showWhy), yesNo(k, 'kept', T('tKept'), showWhy), why);
      if (week.counter) {
        const row = el('div', 'yn cnt'), g = el('div', 'cntg'), n = el('output', 'cntn');
        const minus = el('button', 'ynb', '−'), plus = el('button', 'ynb', '+'); minus.type = plus.type = 'button';
        minus.setAttribute('aria-label', '−1'); plus.setAttribute('aria-label', '+1');
        const cmp = el('p', 'cmp');
        const paint = () => {
          const c = log.get(k).n || 0; n.textContent = num(c);
          if (last && first && first.date !== d.date) { const a = log.get(first.date).n; cmp.textContent = a == null ? '' : T('cmp').replace('{a}', num(a)).replace('{b}', num(c)); cmp.hidden = a == null; }
          else cmp.hidden = true;
        };
        minus.addEventListener('click', () => { log.set(k, { n: Math.max(0, (log.get(k).n || 0) - 1) }); paint(); });
        plus.addEventListener('click', () => { log.set(k, { n: (log.get(k).n || 0) + 1 }); paint(); });
        g.append(minus, n, plus); row.append(el('span', 'ynl', T('counterT')), g); f.append(row, cmp); paint();
      }
      showWhy(); li.append(f);
    }
    const b = el('button', 'donebtn'); b.type = 'button'; li.append(b); doneBtn(b, d.date);
    return li;
  }

  function renderFinal(week) {
    const F = week.final, host = $('#wkFinal'); if (!F || !host) return;
    const k = 'final:' + F.date, c = el('section', 'final'); c.append(el('h2', null, L(F.title)));
    if (F.q1) {
      const q = el('div', 'fq'); q.append(el('p', 'ynl', L(F.q1)));
      const g = el('div', 'yng'), opts = F.q1opts && (F.q1opts[LANG] || F.q1opts.ar) || [];
      const paint = () => [...g.children].forEach((b, i) => { const on = log.get(k).q1 === i; b.classList.toggle('on', on); b.setAttribute('aria-pressed', on); });
      opts.forEach((t, i) => { const b = el('button', 'ynb', t); b.type = 'button'; b.addEventListener('click', () => { log.set(k, { q1: log.get(k).q1 === i ? null : i }); paint(); }); g.append(b); });
      q.append(g); c.append(q); paint();
    }
    if (F.q2) c.append(note(k, 'q2', L(F.q2), T('notePh')));
    if (F.q3) c.append(note(k, 'q3', L(F.q3), T('notePh')));
    if (F.pledge) {
      const p = el('div', 'pledge'); p.append(el('p', 'ynl', T('pledgeT')), el('p', 'ptext', L(F.pledge)));
      const b = el('button', 'donebtn'); b.type = 'button';
      const paint = () => { const on = !!log.get(k).pledge; b.classList.toggle('on', on); b.setAttribute('aria-pressed', on); b.textContent = on ? T('pledgeOn') : T('pledgeOff'); };
      b.addEventListener('click', () => { log.set(k, { pledge: !log.get(k).pledge }); paint(); }); paint();
      p.append(b); c.append(p);
    }
    c.append(sendBox(week));   /* «send my task» lives only in the final review */
    host.append(c);
  }

  /* «send my task»: the whole week becomes one picture the student shares with the teacher */
  function sendBox(week) {
    const w = el('div', 'sendbox');
    w.append(el('h3', null, T('sendT')), el('p', 'sendhelp', T('sendHelp')));
    const lab = el('label', 'tnote'); lab.append(el('span', 'ynl', T('nameL')));
    const inp = el('input'); inp.type = 'text'; inp.placeholder = T('namePh'); inp.autocomplete = 'name'; inp.value = ls.get('wt.name', '');
    inp.addEventListener('input', () => ls.set('wt.name', inp.value));
    lab.append(inp); w.append(lab);
    const row = el('div', 'sendrow'), btn = el('button', 'btn', T('sendBtn')), msg = el('p', 'sendmsg'); btn.type = 'button';
    const save = el('a', 'btn line', T('saveBtn')); save.hidden = true;
    row.append(btn, save); w.append(row, msg);
    btn.addEventListener('click', async () => {
      const name = inp.value.trim(); if (!name) { msg.textContent = T('noName'); inp.focus(); return; }
      msg.textContent = ''; btn.disabled = true;
      try {
        const blob = await sheetPdf(await sheetImage(week, name));
        const file = new File([blob], T('imgFile') + '-' + name.replace(/\s+/g, '-') + '.pdf', { type: 'application/pdf' });
        const url = URL.createObjectURL(blob); save.href = url; save.download = file.name; save.hidden = false;
        if (navigator.canShare && navigator.canShare({ files: [file] })) { try { await navigator.share({ files: [file], title: L(week.title) }); } catch (e) {} }
        else save.click();
      } catch (e) { msg.textContent = T('rErr'); }
      btn.disabled = false;
    });
    return w;
  }

  async function sheetImage(week, name) {
    await document.fonts.ready;
    const W = 1080, M = 64, inner = W - 2 * M, R = AR;
    const HF = AR ? '"Reem Kufi", "IBM Plex Sans Arabic", sans-serif' : '"EB Garamond", Georgia, serif';
    const BF = AR ? '"Noto Naskh Arabic", "Amiri", serif' : '"Source Sans 3", Arial, sans-serif';
    const UF = AR ? '"IBM Plex Sans Arabic", Tahoma, sans-serif' : '"Source Sans 3", Arial, sans-serif';
    const logo = await new Promise(res => { const i = new Image(); i.onload = () => res(i); i.onerror = () => res(null); i.src = ROOT + 'media/logo.webp'; });
    const days = week.days.slice().sort((a, b) => a.date < b.date ? -1 : 1), dn = ls.get(DKEY, {});
    const fin = week.final, fk = fin ? log.get('final:' + fin.date) : {};
    /* two passes: measure, then draw */
    const run = (ctx, draw) => {
      let y = 0; ctx.direction = R ? 'rtl' : 'ltr'; ctx.textBaseline = 'top';
      const X = R ? W - M : M, align = R ? 'right' : 'left';
      const wrap = (text, font, size, lh, color, x = X, maxw = inner) => {
        ctx.font = `${font.w || 400} ${size}px ${font.f}`; ctx.textAlign = align; ctx.fillStyle = color;
        const words = String(text).split(/\s+/); let line = '';
        const out = [];
        for (const wd of words) { const t = line ? line + ' ' + wd : wd; if (ctx.measureText(t).width > maxw && line) { out.push(line); line = wd; } else line = t; }
        if (line) out.push(line);
        out.forEach(l => { if (draw) ctx.fillText(l, x, y); y += lh; });
      };
      const gap = h => { y += h; };
      const rule = (c = '#DCD0B6') => { if (draw) { ctx.fillStyle = c; ctx.fillRect(M, y, inner, 2); } y += 2; };
      /* header */
      if (draw) { ctx.fillStyle = '#0F2E2A'; ctx.fillRect(0, 0, W, 300); }
      y = 40;
      if (logo) { if (draw) ctx.drawImage(logo, W / 2 - 70, y, 140, 140 * logo.height / logo.width); y += 140 * logo.height / logo.width + 18; }
      ctx.textAlign = 'center';
      const center = (t, f, size, color) => { ctx.font = `${f.w || 400} ${size}px ${f.f}`; ctx.fillStyle = color; ctx.textAlign = 'center'; if (draw) ctx.fillText(t, W / 2, y); y += size * 1.45; };
      center(L(week.title), { f: HF, w: 700 }, 46, '#F7EBD0');
      if (week.sub) center(L(week.sub), { f: UF, w: 600 }, 24, '#D9B26A');
      y = Math.max(y, 300) + 34;
      const range = T('imgWeek').replace('{a}', dayName(days[0].date)).replace('{b}', dayName(days[days.length - 1].date));
      wrap(T('imgName') + ': ' + name, { f: UF, w: 700 }, 32, 46, '#0F2E2A');
      wrap(range, { f: UF }, 24, 36, '#6F6654'); gap(18); rule('#85601C'); gap(26);
      /* days */
      days.forEach(d => {
        const g = log.get(d.date), done = !!dn[d.date];
        wrap(dayName(d.date), { f: HF, w: 700 }, 34, 48, '#0F2E2A');
        if (d.segment) wrap(L(d.segment), { f: UF, w: 600 }, 24, 36, '#85601C');
        gap(6);
        const yn = (label, v) => {
          const mark = v === 1 ? '✓ ' + T('yes') : v === 0 ? '✗ ' + T('no') : T('imgNA');
          const col = v === 1 ? '#2E8B57' : v === 0 ? '#C0392B' : '#6F6654';
          ctx.font = `600 26px ${UF}`; const lw = ctx.measureText(label + '  ').width;
          if (draw) { ctx.fillStyle = '#34433F'; ctx.textAlign = align; ctx.fillText(label, R ? W - M : M, y);
            ctx.fillStyle = col; ctx.font = `700 26px ${UF}`; ctx.fillText(mark, R ? W - M - lw - 20 : M + lw + 20, y); }
          y += 40;
        };
        if (week.track) { yn(T('tSeg'), g.seg); yn(T('tKept'), g.kept); if ((g.why || '').trim()) wrap(T('why') + ': ' + g.why.trim(), { f: BF }, 24, 38, '#34433F'); }
        wrap(done ? '✓ ' + T('imgDone') : '○ ' + T('imgNot'), { f: UF, w: 700 }, 24, 38, done ? '#2E8B57' : '#9A8F7A');
        gap(16); rule(); gap(24);
      });
      /* final review */
      if (fin) {
        wrap(L(fin.title), { f: HF, w: 700 }, 36, 52, '#85601C'); gap(6);
        const opts = fin.q1opts && (fin.q1opts[LANG] || fin.q1opts.ar) || [];
        if (fin.q1) { wrap(L(fin.q1), { f: UF, w: 600 }, 25, 38, '#34433F'); wrap(fk.q1 != null ? '◉ ' + opts[fk.q1] : T('imgNA'), { f: UF, w: 700 }, 26, 42, '#0F2E2A'); gap(8); }
        [['q2', fin.q2], ['q3', fin.q3]].forEach(([k, q]) => { if (!q) return; wrap(L(q), { f: UF, w: 600 }, 25, 38, '#34433F'); wrap((fk[k] || '').trim() || T('imgNA'), { f: BF }, 26, 42, '#0F2E2A'); gap(8); });
        if (fin.pledge) { gap(6); wrap(T('pledgeT') + ': ' + L(fin.pledge), { f: BF, w: 600 }, 25, 42, '#0F2E2A'); wrap(fk.pledge ? T('pledgeOn') : T('imgNA'), { f: UF, w: 700 }, 25, 40, fk.pledge ? '#2E8B57' : '#9A8F7A'); }
      }
      gap(30);
      if (draw) { ctx.fillStyle = '#0F2E2A'; ctx.fillRect(0, y, W, 90); ctx.fillStyle = '#D9B26A'; ctx.font = `600 24px ${UF}`; ctx.textAlign = 'center'; ctx.fillText(AR ? 'وتواصوا بالحق' : 'Ve Tevâsav bi’l-Hak', W / 2, y + 32); }
      return y + 90;
    };
    const m = document.createElement('canvas').getContext('2d');
    const H = Math.ceil(run(m, false));
    const cv = document.createElement('canvas'); cv.width = W; cv.height = H;
    const ctx = cv.getContext('2d'); ctx.fillStyle = '#FCFAF4'; ctx.fillRect(0, 0, W, H);
    run(ctx, true);
    return new Promise(res => cv.toBlob(b => res({ blob: b, w: W, h: H }), 'image/jpeg', 0.9));
  }

  /* wrap the picture in a one-page PDF (A4 width, page as long as the sheet) */
  async function sheetPdf(img) {
    const jpg = new Uint8Array(await img.blob.arrayBuffer());
    const pw = 595.28, ph = +(pw * img.h / img.w).toFixed(2);
    const enc = new TextEncoder(), parts = [], offs = [];
    let len = 0; const push = x => { const b = typeof x === 'string' ? enc.encode(x) : x; parts.push(b); len += b.length; };
    const obj = (n, body) => { offs[n] = len; push(n + ' 0 obj\n'); body(); push('\nendobj\n'); };
    push('%PDF-1.4\n%\xE2\xE3\xCF\xD3\n');
    obj(1, () => push('<< /Type /Catalog /Pages 2 0 R >>'));
    obj(2, () => push('<< /Type /Pages /Kids [3 0 R] /Count 1 >>'));
    obj(3, () => push(`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${pw} ${ph}] /Resources << /XObject << /Im0 4 0 R >> >> /Contents 5 0 R >>`));
    obj(4, () => { push(`<< /Type /XObject /Subtype /Image /Width ${img.w} /Height ${img.h} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length ${jpg.length} >>\nstream\n`); push(jpg); push('\nendstream'); });
    const cs = `q ${pw} 0 0 ${ph} 0 0 cm /Im0 Do Q`;
    obj(5, () => push(`<< /Length ${cs.length} >>\nstream\n${cs}\nendstream`));
    const xref = len;
    push('xref\n0 6\n0000000000 65535 f \n' + [1, 2, 3, 4, 5].map(n => String(offs[n]).padStart(10, '0') + ' 00000 n \n').join(''));
    push(`trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`);
    return new Blob(parts, { type: 'application/pdf' });
  }

  async function load() {
    await mergeFromSW();
    let data; try { data = await (await fetch(TASKS, { cache: 'no-cache' })).json(); } catch (e) { data = { weeks: [] }; }
    const weeks = (data.weeks || []).filter(w => (w.days || []).length);
    const all = weeks.flatMap(w => w.days.map(d => Object.assign({ week: w }, d)));
    const today = all.find(d => d.date === TODAY);
    /* home: today's card */
    if ($('#todayBand') && today) {
      $('#todaySeg').textContent = L(today.segment); $('#todaySeg').hidden = !today.segment;
      $('#todayText').textContent = L(today);
      if (today.href) $('#todayText').after(link(today.href, T('open')));
      doneBtn($('#todayDone'), TODAY); $('#todayBand').hidden = false;
    } else if ($('#todayBand')) {
      /* no task today: point to this week's (or the coming week's) task */
      const next = weeks.find(w => w.days.some(d => d.date >= TODAY));
      if (next) {
        $('#todayWhere').textContent = T('week'); $('#todaySeg').textContent = L(next.title);
        $('#todayText').textContent = L(next.sub) || ''; $('#todayDone').hidden = true;
        const a = $('#todayBand .tgo'); a.textContent = T('openWeek') + (AR ? ' ←' : ' →');
        $('#todayBand').hidden = false;
      }
    }
    /* tasks page: the current week (holding today, else the latest started, else the next one) */
    const list = $('#taskList'); if (!list) return;
    const started = weeks.filter(w => w.days.some(d => d.date <= TODAY));
    const week = weeks.find(w => w.days.some(d => d.date === TODAY)) || started[started.length - 1] || weeks[0];
    if (!week) { $('#taskEmpty').hidden = false; return; }
    renderIntro(week);
    const days = week.days.slice().sort((a, b) => a.date < b.date ? -1 : 1);
    days.forEach((d, i) => list.append(renderDay(week, d, days[0], i === days.length - 1)));
    renderFinal(week);
    dayTabs(days, week);
    if (!week.final) $('#taskList').parentNode.insertBefore(sendBox(week), $('#wkFinal').nextSibling);
  }

  /* one day at a time: a row of day buttons above the list; opens on today */
  function dayTabs(days, week) {
    const items = [...document.querySelectorAll('#taskList > .tday')], fin = document.querySelector('#wkFinal .final');
    const panels = items.concat(fin ? [fin] : []); if (panels.length < 2) return;
    const wd = new Intl.DateTimeFormat(AR ? 'ar' : 'tr-TR', { weekday: 'long' });
    const dm = new Intl.DateTimeFormat(AR ? 'ar-u-nu-arab' : 'tr-TR', { day: 'numeric', month: 'long' });
    const bar = el('div', 'daytabs'); bar.setAttribute('role', 'tablist');
    const tabs = panels.map((p, i) => {
      const b = el('button'); b.type = 'button'; b.setAttribute('role', 'tab');
      if (i < days.length) {
        const [y, m, dd] = days[i].date.split('-').map(Number), dt = new Date(y, m - 1, dd);
        b.append(el('b', null, wd.format(dt)), el('span', null, dm.format(dt)));
        if (days[i].date === TODAY) b.classList.add('today');
        b.dataset.date = days[i].date;
      } else { b.append(el('b', null, L(week.final.title)), el('span', null, '✦')); b.classList.add('fin'); }
      b.addEventListener('click', () => show(i, true)); bar.append(b); return b;
    });
    const mark = () => { const dn = ls.get(DKEY, {}); tabs.forEach(b => { if (b.dataset.date) b.classList.toggle('done', !!dn[b.dataset.date]); }); };
    function show(i, focus) {
      panels.forEach((p, j) => { p.hidden = j !== i; });
      tabs.forEach((b, j) => { b.classList.toggle('on', j === i); b.setAttribute('aria-selected', j === i); });
      if (focus) tabs[i].scrollIntoView({ block: 'nearest', inline: 'nearest', behavior: 'smooth' });
    }
    const ti = days.findIndex(d => d.date === TODAY);
    const start = ti >= 0 ? ti : (TODAY < days[0].date ? 0 : (fin ? panels.length - 1 : days.length - 1));
    document.querySelector('#taskList').before(bar);
    document.querySelector('#taskList').addEventListener('click', e => { if (e.target.closest('.donebtn')) setTimeout(mark, 0); });
    mark(); show(start, false);
    setTimeout(() => tabs[start].scrollIntoView({ block: 'nearest', inline: 'center' }), 50);
  }

  /* reminders: ask permission, subscribe, tell the reminder service.
     Browsers never allow notifications without the student's own tap, so we make that tap easy:
     a card with one big button (home + task page) until it is on, and one offer after the first «I finished». */
  const ios = /iphone|ipad|ipod/i.test(navigator.userAgent), standalone = matchMedia('(display-mode: standalone)').matches || navigator.standalone;
  const can = 'serviceWorker' in navigator && 'PushManager' in window && 'Notification' in window;
  const b64 = s => { const p = '='.repeat((4 - s.length % 4) % 4), r = atob((s + p).replace(/-/g, '+').replace(/_/g, '/')); return Uint8Array.from(r, c => c.charCodeAt(0)); };
  async function current() { if (!can) return null; const reg = await navigator.serviceWorker.ready; return reg.pushManager.getSubscription(); }
  async function isOn() { return !!((await current()) && ls.get(IDKEY, null)); }
  async function enable() {
    if ((await Notification.requestPermission()) !== 'granted') return false;
    const reg = await navigator.serviceWorker.ready;
    const key = (await (await fetch(API + '/key')).json()).key;
    let sub = await reg.pushManager.getSubscription();
    if (!sub) sub = await reg.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: b64(key) });
    const r = await post('/subscribe', { subscription: sub.toJSON(), id: ls.get(IDKEY, null), tz: Intl.DateTimeFormat().resolvedOptions().timeZone, lang: LANG });
    if (!r.id) throw new Error('no id');
    ls.set(IDKEY, r.id);
    if (ls.get(DKEY, {})[TODAY]) post('/done', { id: r.id, date: TODAY }).catch(() => {});
    await writeSW(); return true;
  }
  async function disable() {
    const sub = await current(); if (sub) await sub.unsubscribe().catch(() => {});
    const id = ls.get(IDKEY, null); if (id) post('/unsubscribe', { id }).catch(() => {});
    try { localStorage.removeItem(IDKEY); } catch (e) {}
    await writeSW({ id: null });
  }
  const BELL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 8-3 8h18s-3-1-3-8"/><path d="M13.7 20a2 2 0 0 1-3.4 0"/></svg>';
  async function paintCards() {
    const on = await isOn().catch(() => false);
    document.querySelectorAll('[data-rcard]').forEach(card => {
      const home = card.dataset.rcard === 'home'; card.innerHTML = ''; card.className = 'rcard';
      if (on) {
        if (home) { card.hidden = true; return; }
        card.classList.add('on'); card.hidden = false;
        const p = el('p', 'ron', T('rIsOn')); const off = el('button', 'linkbtn', T('rOff')); off.type = 'button';
        off.addEventListener('click', async () => { off.disabled = true; await disable().catch(() => {}); paintCards(); });
        card.append(p, off); return;
      }
      if (!can) {
        if (!(ios && !standalone)) { card.hidden = home; if (!home) card.append(el('p', 'rmsg', T('rNo'))); return; }
        card.hidden = false; card.classList.add('hint');
        const ic = el('span', 'ric'); ic.innerHTML = BELL; card.append(ic, el('div', null)); card.lastChild.append(el('h3', null, T('rT')), el('p', 'rmsg', T('rIos'))); return;
      }
      if (Notification.permission === 'denied') { card.hidden = home; if (!home) card.append(el('p', 'rmsg', T('rDenied'))); return; }
      card.hidden = false;
      const ic = el('span', 'ric'); ic.innerHTML = BELL;
      const txt = el('div'); txt.append(el('h3', null, T('rT')), el('p', 'rmsg', T('rHelp')));
      const btn = el('button', 'btn rbig', T('rOn')); btn.type = 'button';
      btn.addEventListener('click', async () => {
        btn.disabled = true;
        try { await enable(); } catch (e) { txt.lastChild.textContent = T('rErr'); btn.disabled = false; return; }
        paintCards();
      });
      card.append(ic, txt, btn);
    });
  }
  /* one gentle offer after the first «I finished» */
  async function offerOnce() {
    if (!can || Notification.permission !== 'default' || ls.get('wt.remind.asked', false) || await isOn().catch(() => true)) return;
    ls.set('wt.remind.asked', true);
    const t = el('div', 'rtoast'); t.setAttribute('role', 'dialog');
    const ic = el('span', 'ric'); ic.innerHTML = BELL;
    const yes = el('button', 'btn', T('rOn')), no = el('button', 'linkbtn', T('askNo')); yes.type = no.type = 'button';
    const row = el('div', 'rtrow'); row.append(yes, no);
    const body = el('div'); body.append(el('p', 'rtq', T('askQ')), row);
    t.append(ic, body); document.body.append(t);
    requestAnimationFrame(() => t.classList.add('show'));
    const close = () => { t.classList.remove('show'); setTimeout(() => t.remove(), 300); };
    no.addEventListener('click', close);
    yes.addEventListener('click', async () => { yes.disabled = true; try { await enable(); } catch (e) {} close(); paintCards(); });
  }
  document.addEventListener('click', e => {
    const b = e.target.closest('#todayDone, .tday .donebtn');
    if (b) setTimeout(() => { if (b.classList.contains('on')) offerOnce(); }, 0);
  });
  load(); paintCards(); writeSW();
})();
