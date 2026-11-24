/* slide viewer: one slide at a time, step through answers, swipe, keys, full screen, grid of all slides */
(function () {
  const $ = s => document.querySelector(s);
  const AR = document.documentElement.lang === 'ar';
  const num = n => AR ? String(n).replace(/\d/g, d => '٠١٢٣٤٥٦٧٨٩'[d]) : String(n);
  const canvas = $('#svCanvas'), stage = $('#svStage');
  const slides = Array.from(canvas.children).filter(e => e.tagName === 'SECTION');
  const N = slides.length;
  slides.forEach((s, i) => { const pn = s.querySelector('.pn'); if (pn) pn.textContent = num(i + 1); });
  let cur = 0, step = 0;
  const frags = s => Array.from(s.querySelectorAll('.fragment'));

  function fit() {
    const r = stage.getBoundingClientRect(), pad = innerWidth < 700 ? 8 : 24;
    const z = Math.min((r.width - pad * 2) / 1920, (r.height - pad * 2) / 1080);
    canvas.style.transformOrigin = '0 0';
    canvas.style.left = (r.width / 2) + 'px'; canvas.style.top = (r.height / 2) + 'px';
    canvas.style.transform = `translate(-${960 * z}px, -${540 * z}px) scale(${z})`;
  }
  function show(i, st, fromBack) {
    i = Math.max(0, Math.min(N - 1, i));
    const changed = i !== cur || !slides[i].classList.contains('cur');
    slides.forEach((s, k) => s.classList.toggle('cur', k === i));
    if (changed) { slides[i].classList.remove('fade'); void slides[i].offsetWidth; slides[i].classList.add('fade'); }
    cur = i;
    const f = frags(slides[i]);
    step = st === undefined ? 0 : Math.max(0, Math.min(f.length, st));
    if (fromBack) step = f.length;
    f.forEach((e, k) => e.classList.toggle('visible', k < step));
    $('#svCnt').textContent = num(i + 1) + ' / ' + num(N);
    $('#svBar').style.width = (100 * (i + 1) / N) + '%';
    $('#svPrev').disabled = i === 0 && step === 0;
    $('#svNext').disabled = i === N - 1 && step >= f.length;
    const left = f.length - step, fb = $('#svFrag');
    fb.hidden = !left; if (left) fb.textContent = AR ? ('اضغط «التالي» لإظهار الجواب (' + num(left) + ')') : ('Cevap için «Sonraki»e basın (' + left + ')');
    try { history.replaceState(null, '', '#' + (i + 1)); } catch (e) {}
  }
  function next() { const f = frags(slides[cur]); if (step < f.length) { step++; f[step - 1].classList.add('visible'); show(cur, step); } else if (cur < N - 1) show(cur + 1, 0); }
  function prev() { if (step > 0) show(cur, step - 1); else if (cur > 0) show(cur - 1, 0, true); }

  $('#svNext').onclick = next; $('#svPrev').onclick = prev;
  stage.addEventListener('click', e => { if (grid.hidden && !e.target.closest('a,button')) { const r = stage.getBoundingClientRect(); const x = e.clientX - r.left; (AR ? x < r.width * .35 : x > r.width * .65) ? next() : (AR ? x > r.width * .65 : x < r.width * .35) ? prev() : next(); } });
  addEventListener('keydown', e => {
    if (!grid.hidden) { if (e.key === 'Escape') toggleGrid(false); return; }
    const fwd = AR ? ['ArrowLeft', 'ArrowDown', 'PageDown', ' ', 'Enter'] : ['ArrowRight', 'ArrowDown', 'PageDown', ' ', 'Enter'];
    const back = AR ? ['ArrowRight', 'ArrowUp', 'PageUp', 'Backspace'] : ['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace'];
    if (fwd.includes(e.key)) { e.preventDefault(); next(); }
    else if (back.includes(e.key)) { e.preventDefault(); prev(); }
    else if (e.key === 'Home') show(0); else if (e.key === 'End') show(N - 1);
    else if (e.key === 'f' || e.key === 'F') fs();
  });
  let tx = null, ty = null;
  stage.addEventListener('touchstart', e => { tx = e.touches[0].clientX; ty = e.touches[0].clientY; }, { passive: true });
  stage.addEventListener('touchend', e => {
    if (tx === null || !grid.hidden) return;
    const dx = e.changedTouches[0].clientX - tx, dy = e.changedTouches[0].clientY - ty; tx = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) { e.preventDefault(); (AR ? dx > 0 : dx < 0) ? next() : prev(); }
  });

  function fs() {
    const el = document.documentElement;
    if (document.fullscreenElement) document.exitFullscreen();
    else if (el.requestFullscreen) el.requestFullscreen().then(() => { try { screen.orientation.lock('landscape'); } catch (e) {} }).catch(() => {});
  }
  $('#svFs').onclick = fs;
  if (!document.documentElement.requestFullscreen) $('#svFs').hidden = true;

  /* grid of all slides */
  const grid = $('#svGrid');
  let built = false;
  function buildGrid() {
    built = true;
    grid.innerHTML = slides.map((s, i) => `<button data-i="${i}" aria-label="${num(i + 1)}"><div class="th">${s.outerHTML.replace(/class="([^"]*)\bcur\b([^"]*)"/, 'class="$1$2"')}</div><span class="n">${num(i + 1)}</span></button>`).join('');
    grid.querySelectorAll('.th').forEach(t => { const w = t.parentElement.clientWidth; t.style.transform = `scale(${w / 1920})`; });
    grid.querySelectorAll('button').forEach(b => b.onclick = () => { toggleGrid(false); show(+b.dataset.i); });
  }
  function toggleGrid(on) {
    grid.hidden = !on; $('#svGridBtn').setAttribute('aria-pressed', on);
    if (on) { if (!built) buildGrid(); grid.querySelectorAll('button').forEach((b, i) => b.classList.toggle('on', i === cur)); const b = grid.querySelector('.on'); if (b) b.scrollIntoView({ block: 'center' }); }
  }
  $('#svGridBtn').onclick = () => toggleGrid(grid.hidden);
  addEventListener('resize', () => { fit(); if (built) grid.querySelectorAll('.th').forEach(t => { t.style.transform = `scale(${t.parentElement.clientWidth / 1920})`; }); });

  const hint = $('#svHint');
  if (hint) { if (innerHeight > innerWidth && innerWidth < 700) setTimeout(() => { hint.style.opacity = 0; }, 4500); else hint.hidden = true; }

  addEventListener('hashchange', () => { const k = parseInt(location.hash.slice(1), 10); if (k > 0 && k - 1 !== cur) show(k - 1); });
  const h = parseInt(location.hash.slice(1), 10);
  fit(); show(h > 0 ? h - 1 : 0);
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(fit);
})();
