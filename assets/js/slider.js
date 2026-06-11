/* ============================================================
   MEDAD — hero slider (autoplay, arrows, dots, swipe, a11y)
   ============================================================ */
(function () {
  'use strict';
  var root = document.querySelector('.hero-slider');
  if (!root) return;

  var slides = Array.prototype.slice.call(root.querySelectorAll('.hs-slide'));
  var dotsWrap = root.querySelector('.hs-dots');
  var i = 0, timer = null;
  var DELAY = 6000;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // build dots
  slides.forEach(function (_, idx) {
    var b = document.createElement('button');
    b.className = 'hs-dot' + (idx === 0 ? ' active' : '');
    b.setAttribute('aria-label', 'Go to slide ' + (idx + 1));
    b.addEventListener('click', function () { go(idx); restart(); });
    dotsWrap.appendChild(b);
  });
  var dots = Array.prototype.slice.call(dotsWrap.children);

  function go(n) {
    slides[i].classList.remove('active'); dots[i].classList.remove('active');
    i = (n + slides.length) % slides.length;
    slides[i].classList.add('active'); dots[i].classList.add('active');
  }
  function next() { go(i + 1); }
  function prev() { go(i - 1); }

  function start() { if (!reduce) timer = setInterval(next, DELAY); }
  function stop() { if (timer) { clearInterval(timer); timer = null; } }
  function restart() { stop(); start(); }

  var nextBtn = root.querySelector('.hs-next'), prevBtn = root.querySelector('.hs-prev');
  if (nextBtn) nextBtn.addEventListener('click', function () { next(); restart(); });
  if (prevBtn) prevBtn.addEventListener('click', function () { prev(); restart(); });

  // pause on hover
  root.addEventListener('mouseenter', stop);
  root.addEventListener('mouseleave', start);

  // pause when tab hidden
  document.addEventListener('visibilitychange', function () { document.hidden ? stop() : restart(); });

  // swipe (touch)
  var x0 = null;
  root.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; stop(); }, { passive: true });
  root.addEventListener('touchend', function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    var rtl = document.documentElement.getAttribute('dir') === 'rtl';
    if (Math.abs(dx) > 45) { (dx < 0) !== rtl ? next() : prev(); }
    x0 = null; restart();
  }, { passive: true });

  start();
})();
