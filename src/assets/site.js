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
    host.append(c);
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
        const a = $('#todayBand .go'); a.textContent = T('openWeek') + (AR ? ' ←' : ' →');
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
  }

  /* reminders: ask permission, subscribe, tell the reminder service */
  const ios = /iphone|ipad|ipod/i.test(navigator.userAgent), standalone = matchMedia('(display-mode: standalone)').matches || navigator.standalone;
  const can = 'serviceWorker' in navigator && 'PushManager' in window && 'Notification' in window;
  const rBtn = $('#rBtn'), rState = $('#rState');
  const b64 = s => { const p = '='.repeat((4 - s.length % 4) % 4), r = atob((s + p).replace(/-/g, '+').replace(/_/g, '/')); return Uint8Array.from(r, c => c.charCodeAt(0)); };
  async function current() { if (!can) return null; const reg = await navigator.serviceWorker.ready; return reg.pushManager.getSubscription(); }
  async function paintR() {
    if (!rBtn) return;
    if (!can) { rState.textContent = ios && !standalone ? T('rIos') : T('rNo'); rBtn.hidden = true; return; }
    if (Notification.permission === 'denied') { rState.textContent = T('rDenied'); rBtn.hidden = true; return; }
    const sub = await current(), on = !!(sub && ls.get(IDKEY, null));
    rBtn.hidden = false; rBtn.textContent = on ? T('rOff') : T('rOn'); rBtn.classList.toggle('line', on);
    rState.textContent = on ? T('rIsOn') + ' ' + T('rHelp') : T('rHelp');
  }
  async function enable() {
    if ((await Notification.requestPermission()) !== 'granted') return paintR();
    const reg = await navigator.serviceWorker.ready;
    const key = (await (await fetch(API + '/key')).json()).key;
    let sub = await reg.pushManager.getSubscription();
    if (!sub) sub = await reg.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: b64(key) });
    const r = await post('/subscribe', { subscription: sub.toJSON(), id: ls.get(IDKEY, null), tz: Intl.DateTimeFormat().resolvedOptions().timeZone, lang: LANG });
    if (!r.id) throw new Error('no id');
    ls.set(IDKEY, r.id);
    if (ls.get(DKEY, {})[TODAY]) post('/done', { id: r.id, date: TODAY }).catch(() => {});
    await writeSW();
  }
  async function disable() {
    const sub = await current(); if (sub) await sub.unsubscribe().catch(() => {});
    const id = ls.get(IDKEY, null); if (id) post('/unsubscribe', { id }).catch(() => {});
    try { localStorage.removeItem(IDKEY); } catch (e) {}
    await writeSW({ id: null });
  }
  if (rBtn) rBtn.addEventListener('click', async () => {
    rBtn.disabled = true;
    try { if ((await current()) && ls.get(IDKEY, null)) await disable(); else await enable(); }
    catch (e) { rState.textContent = T('rErr'); rBtn.disabled = false; return; }
    rBtn.disabled = false; paintR();
  });
  load(); paintR(); writeSW();
})();
