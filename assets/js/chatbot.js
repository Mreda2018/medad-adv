/* ============================================================
   MEDAD Assistant — offline bilingual chatbot (no API needed)
   Knowledge base built from Medad's site content & services.
   ============================================================ */
(function () {
  'use strict';

  var L = function () { return (window.MEDAD_getLang && window.MEDAD_getLang()) || 'en'; };

  // ---- knowledge base: intents with keywords (en+ar) and bilingual answers ----
  var KB = [
    {
      id: 'greet',
      kw: ['hi', 'hello', 'hey', 'salam', 'salaam', 'مرحبا', 'السلام', 'هاي', 'اهلا', 'أهلا'],
      en: "Hello! 👋 I'm Medad's assistant. I can help with our printing & signage services, prices, working hours, or location. What do you need?",
      ar: "أهلاً بك! 👋 أنا مساعد مداد. أقدر أساعدك في خدمات الطباعة واللوحات الإعلانية، الأسعار، مواعيد العمل، أو الموقع. محتاج إيه؟"
    },
    {
      id: 'services',
      kw: ['service', 'services', 'offer', 'do you', 'product', 'products', 'خدمات', 'خدمة', 'منتجات', 'بتعملوا', 'تقدمو'],
      en: "Medad offers a full range of advertising & printing solutions:<br>• 3D Signages & Signboards<br>• Acrylic works & laser cutting<br>• UV / DTF, indoor & outdoor printing<br>• Stickers, Roll-ups & Pop-ups<br>• Banners, Flex & Canvas<br>• Vehicle branding, Stands, Trophies & more.<br>Which one interests you?",
      ar: "مداد بتقدّم حلول إعلان وطباعة متكاملة:<br>• لوحات ثلاثية الأبعاد ولوحات إعلانية<br>• أعمال أكريليك وقص ليزر<br>• طباعة UV / DTF داخلية وخارجية<br>• ملصقات، رول أب وبوب أب<br>• بنرات، فليكس وكانفس<br>• تغليف مركبات، ستاندات، دروع وأكتر.<br>أي خدمة تهمّك؟"
    },
    {
      id: 'dtf',
      kw: ['dtf', 'uv', 'new machine', 'ماكينة', 'يو في', 'دي تي اف', 'الجديدة'],
      en: "Great choice! We've added a new DTF & UV printing machine. ✨ It prints sharp, durable, full-colour graphics directly onto almost any surface — acrylic, wood, glass, metal, leather and fabric — with white ink and 3D embossed effects. Perfect for custom signage, gifts, packaging and short runs. Want a quote?",
      ar: "اختيار ممتاز! أضفنا ماكينة DTF و UV جديدة. ✨ بتطبع ألوان حادة وثابتة مباشرة على أي سطح تقريبًا — أكريليك، خشب، زجاج، معدن، جلد وقماش — مع حبر أبيض وتأثيرات بارزة 3D. مثالية للوحات المخصّصة، الهدايا، التغليف والكميات الصغيرة. تحب عرض سعر؟"
    },
    {
      id: 'quote',
      kw: ['price', 'cost', 'quote', 'how much', 'quotation', 'سعر', 'اسعار', 'أسعار', 'عرض سعر', 'بكام', 'تكلفة'],
      en: "Pricing depends on material, size and quantity. Share your project details and we'll send a fast, competitive quote. 📞 Call/WhatsApp +971 50 8050150 or email info@medadadv.ae.",
      ar: "السعر بيعتمد على الخامة والمقاس والكمية. ابعتلنا تفاصيل مشروعك وهنرسل عرض سعر سريع ومنافس. 📞 اتصل/واتساب +971 50 8050150 أو إيميل info@medadadv.ae."
    },
    {
      id: 'contact',
      kw: ['contact', 'phone', 'call', 'whatsapp', 'email', 'reach', 'تواصل', 'اتصال', 'رقم', 'تليفون', 'ايميل', 'واتس'],
      en: "You can reach Medad here:<br>📞 Tel: +971 4 2638380<br>📱 Mobile/WhatsApp: +971 50 8050150<br>✉️ info@medadadv.ae<br>🌐 www.medadadv.ae",
      ar: "تقدر تتواصل مع مداد من هنا:<br>📞 هاتف: +971 4 2638380<br>📱 موبايل/واتساب: +971 50 8050150<br>✉️ info@medadadv.ae<br>🌐 www.medadadv.ae"
    },
    {
      id: 'location',
      kw: ['location', 'address', 'where', 'map', 'office', 'موقع', 'عنوان', 'فين', 'مكان', 'خريطة'],
      en: "📍 We're in Dubai — Al Habtoor Complex, Office No. 57, Al Qusais 3rd Industrial Zone, P.O. Box 237358, Dubai, U.A.E. Open the Contact page for the map & directions.",
      ar: "📍 موجودين في دبي — مجمع الحبتور، مكتب رقم 57، القصيص الصناعية الثالثة، ص.ب 237358، دبي، الإمارات. افتح صفحة التواصل للخريطة والاتجاهات."
    },
    {
      id: 'hours',
      kw: ['hours', 'open', 'timing', 'time', 'working', 'مواعيد', 'ساعات', 'مفتوح', 'وقت', 'دوام'],
      en: "🕘 Working hours:<br>• Mon–Fri: 9:00am – 5:00pm<br>• Saturday: 10:00am – 2:00pm<br>• Sunday: Closed<br>Support hotline available 24h.",
      ar: "🕘 مواعيد العمل:<br>• الإثنين–الجمعة: 9:00 ص – 5:00 م<br>• السبت: 10:00 ص – 2:00 م<br>• الأحد: مغلق<br>خط الدعم متاح 24 ساعة."
    },
    {
      id: 'about',
      kw: ['about', 'who are', 'company', 'experience', 'من انتم', 'عن', 'الشركة', 'خبرة', 'مين'],
      en: "Medad Advertising Requisites L.L.C is a Dubai-based digital printing & signage company. We turn ideas into vibrant, precise prints with state-of-the-art technology, customization, on-time delivery and strict quality control. See the About page for more.",
      ar: "مداد للوسائل الإعلانية ذ.م.م شركة طباعة رقمية ولوحات إعلانية مقرّها دبي. بنحوّل الأفكار إلى مطبوعات دقيقة وزاهية بأحدث التقنيات، مع تخصيص كامل، تسليم في الموعد، ورقابة جودة صارمة. شوف صفحة من نحن للمزيد."
    },
    {
      id: 'vehicle',
      kw: ['vehicle', 'car', 'wrap', 'branding', 'مركبات', 'سيارة', 'تغليف', 'عربية'],
      en: "Vehicle branding & wraps: we design, print and install durable, weather-resistant graphics for cars, vans and fleets — full or partial wraps. Want to brand your vehicle?",
      ar: "تغليف وبراندينج المركبات: بنصمّم ونطبع ونركّب جرافيك متين مقاوم للعوامل الجوية للسيارات والشاحنات والأساطيل — تغليف كامل أو جزئي. تحب تعمل براندينج لعربيتك؟"
    },
    {
      id: 'thanks',
      kw: ['thanks', 'thank', 'شكرا', 'شكراً', 'تسلم'],
      en: "You're welcome! 😊 Anything else I can help with?",
      ar: "العفو! 😊 في حاجة تانية أقدر أساعدك فيها؟"
    }
  ];

  var FALLBACK = {
    en: "I'm not 100% sure about that, but our team can help right away. 📞 Call/WhatsApp +971 50 8050150 or email info@medadadv.ae. You can also ask me about our services, prices, hours or location.",
    ar: "مش متأكد 100% من دي، بس فريقنا يقدر يساعدك فورًا. 📞 اتصل/واتساب +971 50 8050150 أو إيميل info@medadadv.ae. كمان تقدر تسألني عن خدماتنا، الأسعار، المواعيد أو الموقع."
  };

  var CHIPS = {
    en: [['Our services', 'services'], ['New DTF/UV', 'dtf'], ['Get a quote', 'quote'], ['Working hours', 'hours'], ['Location', 'location']],
    ar: [['خدماتنا', 'services'], ['DTF/UV الجديدة', 'dtf'], ['عرض سعر', 'quote'], ['المواعيد', 'hours'], ['الموقع', 'location']]
  };

  function match(text) {
    var q = ' ' + text.toLowerCase().replace(/[؟?.,!]/g, ' ') + ' ';
    var best = null, bestScore = 0;
    KB.forEach(function (intent) {
      var score = 0;
      intent.kw.forEach(function (k) { if (q.indexOf(k.toLowerCase()) !== -1) score += k.length > 3 ? 2 : 1; });
      if (score > bestScore) { bestScore = score; best = intent; }
    });
    return bestScore > 0 ? best : null;
  }

  // ---- build UI ----
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }

  var ICON = {
    chat: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>',
    bot: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4M8 16h.01M16 16h.01"/></svg>',
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>',
    send: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>'
  };

  var panel, body, chipsWrap, input;

  function addMsg(html, who) {
    var m = el('div', 'msg ' + who, html);
    body.appendChild(m); body.scrollTop = body.scrollHeight;
    return m;
  }
  function typing() {
    var t = el('div', 'msg bot typing', '<span></span><span></span><span></span>');
    body.appendChild(t); body.scrollTop = body.scrollHeight; return t;
  }
  function respond(text) {
    var lang = L();
    var t = typing();
    setTimeout(function () {
      t.remove();
      var hit = match(text);
      addMsg(hit ? hit[lang] : FALLBACK[lang], 'bot');
    }, 500 + Math.random() * 350);
  }
  function answerIntent(id) {
    var lang = L(), intent = KB.filter(function (k) { return k.id === id; })[0];
    if (intent) { var t = typing(); setTimeout(function () { t.remove(); addMsg(intent[lang], 'bot'); }, 450); }
  }
  function renderChips() {
    var lang = L(); chipsWrap.innerHTML = '';
    CHIPS[lang].forEach(function (c) {
      var b = el('button', null, c[0]);
      b.addEventListener('click', function () { addMsg(c[0], 'user'); answerIntent(c[1]); });
      chipsWrap.appendChild(b);
    });
  }
  function greet() {
    body.innerHTML = '';
    addMsg(KB[0][L()], 'bot');
    renderChips();
  }

  function build() {
    var fab = el('button', 'chat-fab', ICON.chat + '<span class="dot"></span>');
    fab.setAttribute('aria-label', 'Chat');
    panel = el('div', 'chat-panel');
    panel.innerHTML =
      '<div class="chat-head"><div class="av">' + ICON.bot + '</div>' +
      '<div><b data-en="Medad Assistant" data-ar="مساعد مداد">Medad Assistant</b>' +
      '<span data-en="Online · replies instantly" data-ar="متصل · يرد فورًا">Online · replies instantly</span></div>' +
      '<button class="chat-close" aria-label="Close">' + ICON.close + '</button></div>' +
      '<div class="chat-body"></div><div class="chat-chips"></div>' +
      '<div class="chat-input"><input type="text" data-en-ph="Type your message…" data-ar-ph="اكتب رسالتك…" placeholder="Type your message…"/>' +
      '<button class="chat-send" aria-label="Send">' + ICON.send + '</button></div>';
    document.body.appendChild(fab);
    document.body.appendChild(panel);

    body = panel.querySelector('.chat-body');
    chipsWrap = panel.querySelector('.chat-chips');
    input = panel.querySelector('input');

    var opened = false;
    function open() { panel.classList.add('open'); if (!opened) { greet(); opened = true; } input.focus(); }
    function close() { panel.classList.remove('open'); }
    fab.addEventListener('click', function () { panel.classList.contains('open') ? close() : open(); });
    panel.querySelector('.chat-close').addEventListener('click', close);

    function send() {
      var v = input.value.trim(); if (!v) return;
      addMsg(v.replace(/</g, '&lt;'), 'user'); input.value = ''; respond(v);
    }
    panel.querySelector('.chat-send').addEventListener('click', send);
    input.addEventListener('keydown', function (e) { if (e.key === 'Enter') send(); });

    // re-render greeting/chips on language change
    document.addEventListener('langchange', function () { if (opened) renderChips(); });
  }

  if (document.readyState !== 'loading') build();
  else document.addEventListener('DOMContentLoaded', build);
})();
