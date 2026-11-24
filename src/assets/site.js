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
    $$('.donebtn').forEach(b => {
      const [n, k] = b.dataset.done.split(':'), on = !!(o[n] || {})[k];
      b.classList.toggle('on', on); b.setAttribute('aria-pressed', on); b.textContent = on ? b.dataset.on : b.dataset.off;
    });
    $$('.lrow').forEach(r => { const p = r.querySelector('.lprog'); r.classList.toggle('complete', !!(p && (o[p.dataset.lesson] || {}).lesson)); });
    const r = $('#progReset'); if (r) r.hidden = !Object.keys(o).length;
  }
  /* the student presses «I finished» themselves; pressing again undoes it */
  $$('.donebtn').forEach(b => b.addEventListener('click', () => {
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
