/* ============================================================
   MEDAD — core: language toggle (AR/EN + RTL), nav, reveal
   ============================================================ */
(function () {
  'use strict';
  var KEY = 'medad-lang';

  /* ---------- language ---------- */
  function applyLang(lang) {
    var html = document.documentElement;
    html.setAttribute('lang', lang);
    html.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

    document.querySelectorAll('[data-en]').forEach(function (el) {
      var val = el.getAttribute('data-' + lang);
      if (val !== null) el.innerHTML = val;
    });
    document.querySelectorAll('[data-en-ph]').forEach(function (el) {
      var val = el.getAttribute('data-' + lang + '-ph');
      if (val !== null) el.setAttribute('placeholder', val);
    });
    document.querySelectorAll('[data-en-title]').forEach(function (el) {
      var val = el.getAttribute('data-' + lang + '-title');
      if (val !== null) el.setAttribute('title', val);
    });
    // toggle button label shows the OTHER language
    document.querySelectorAll('[data-langlabel]').forEach(function (el) {
      el.textContent = lang === 'ar' ? 'EN' : 'عربي';
    });
    // update <title> + meta description if alternates provided
    var t = document.querySelector('title');
    if (t && t.getAttribute('data-' + lang)) document.title = t.getAttribute('data-' + lang);

    try { localStorage.setItem(KEY, lang); } catch (e) {}
    window.MEDAD_LANG = lang;
    document.dispatchEvent(new CustomEvent('langchange', { detail: lang }));
  }
  function getLang() {
    try { return localStorage.getItem(KEY) || 'en'; } catch (e) { return 'en'; }
  }
  window.MEDAD_setLang = applyLang;
  window.MEDAD_getLang = getLang;

  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-toggle-lang]');
    if (t) { e.preventDefault(); applyLang(getLang() === 'ar' ? 'en' : 'ar'); }
  });

  /* ---------- header scroll ---------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 12); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- mobile menu ---------- */
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-open-menu]')) document.querySelector('.mobile-menu').classList.add('open');
    if (e.target.closest('[data-close-menu]') || e.target.classList.contains('mobile-menu'))
      document.querySelector('.mobile-menu').classList.remove('open');
  });

  /* ---------- reveal on scroll ---------- */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { threshold: 0.12 });
  function bindReveal() { document.querySelectorAll('.reveal:not(.in)').forEach(function (el) { io.observe(el); }); }

  /* ---------- year ---------- */
  document.addEventListener('DOMContentLoaded', function () {
    var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
    bindReveal();
  });

  // apply saved language ASAP
  applyLang(getLang());
})();
