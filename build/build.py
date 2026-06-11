# -*- coding: utf-8 -*-
"""Static site generator for Medad Advertising (bilingual EN/AR)."""
import os, json, datetime
from data import SITE, COMPANY, PRODUCTS, ARTICLES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------- SVG icon library ----------------
def _svg(p): return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % p
ICONS = {
 "layers": _svg('<path d="M12 2l9 5-9 5-9-5 9-5z"/><path d="M3 12l9 5 9-5"/><path d="M3 17l9 5 9-5"/>'),
 "frame": _svg('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 3v18"/>'),
 "flag": _svg('<path d="M4 22V4s2-1 5-1 5 2 8 2 3-1 3-1v10s-1 1-3 1-5-2-8-2-5 1-5 1"/>'),
 "signpost": _svg('<path d="M12 2v20"/><path d="M5 6h11l3 3-3 3H5z"/>'),
 "home": _svg('<path d="M3 10l9-7 9 7v9a2 2 0 0 1-2 2h-4v-6H9v6H5a2 2 0 0 1-2-2z"/>'),
 "tag": _svg('<path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0l-7.8-7.8V3h9.8l8 8a2 2 0 0 1 0 2.4z"/><circle cx="7.5" cy="7.5" r="1.4"/>'),
 "zap": _svg('<path d="M13 2L3 14h8l-1 8 10-12h-8l1-8z"/>'),
 "box": _svg('<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8"/><path d="M12 13v8"/>'),
 "rollup": _svg('<rect x="6" y="2" width="12" height="15" rx="1"/><path d="M9 21h6M12 17v4"/>'),
 "signboard": _svg('<rect x="3" y="4" width="18" height="11" rx="2"/><path d="M12 15v5M8 20h8"/>'),
 "activity": _svg('<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>'),
 "kiosk": _svg('<path d="M4 9h16v11H4zM3 5h18l-1 4H4z"/><path d="M10 20v-5h4v5"/>'),
 "sticker": _svg('<path d="M15.5 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h8l6-6V5a2 2 0 0 0-2-2z"/><path d="M14 21v-5a1 1 0 0 1 1-1h5"/>'),
 "award": _svg('<circle cx="12" cy="9" r="6"/><path d="M9 14.5L8 22l4-2 4 2-1-7.5"/>'),
 "truck": _svg('<path d="M1 5h13v11H1zM14 8h4l3 3v5h-7"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>'),
 "sparkles": _svg('<path d="M12 3l1.8 4.7L18 9.5l-4.2 1.8L12 16l-1.8-4.7L6 9.5l4.2-1.8z"/><path d="M19 14l.7 1.8L21.5 16.5l-1.8.7L19 19l-.7-1.8L16.5 16.5l1.8-.7z"/>'),
 "phone": _svg('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>'),
 "mobile": _svg('<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>'),
 "mail": _svg('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 6l10 7L22 6"/>'),
 "pin": _svg('<path d="M21 10c0 6-9 12-9 12s-9-6-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>'),
 "clock": _svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "arrow": _svg('<path d="M5 12h14M13 6l6 6-6 6"/>'),
 "check": _svg('<path d="M20 6L9 17l-5-5"/>'),
 "star": _svg('<path d="M12 2l3 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.9 21l1.2-6.8-5-4.9 6.9-1z"/>'),
 "shield": _svg('<path d="M12 2l8 4v6c0 5-3.4 8.5-8 10-4.6-1.5-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/>'),
 "rocket": _svg('<path d="M5 13c-2 1-3 5-3 5s4-1 5-3M15 9a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/><path d="M9 15l-3-3c2-7 7-9 12-9 0 5-2 10-9 12z"/>'),
 "users": _svg('<path d="M17 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9"/>'),
 "palette": _svg('<path d="M12 2a10 10 0 1 0 0 20c1.1 0 2-.9 2-2 0-.5-.2-1-.5-1.3-.3-.4-.5-.8-.5-1.2 0-1 .8-1.8 1.8-1.8H17a5 5 0 0 0 5-5c0-4.4-4.5-8-10-8z"/><circle cx="7.5" cy="10.5" r="1"/><circle cx="12" cy="7.5" r="1"/><circle cx="16.5" cy="10.5" r="1"/>'),
 "headset": _svg('<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="2" y="14" width="4" height="6" rx="1"/><rect x="18" y="14" width="4" height="6" rx="1"/><path d="M20 20a4 4 0 0 1-4 3h-2"/>'),
 "menu": _svg('<path d="M3 6h18M3 12h18M3 18h18"/>'),
 "close": _svg('<path d="M18 6L6 18M6 6l12 12"/>'),
 "globe": _svg('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18z"/>'),
 "wa": _svg('<path d="M20 12a8 8 0 0 1-11.7 7L4 20l1-4.2A8 8 0 1 1 20 12z"/><path d="M9 9c0 4 2 6 6 6 .5 0 1-.5 1-1l-1.5-1-1 .8c-1-.4-1.9-1.3-2.3-2.3l.8-1L11 9c0-.5-.5-1-1-1S9 8.5 9 9z" fill="currentColor" stroke="none"/>'),
 "insta": _svg('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/>'),
 "fb": _svg('<path d="M14 9h3V6h-3a4 4 0 0 0-4 4v2H8v3h2v6h3v-6h2.5l.5-3H13v-2a1 1 0 0 1 1-1z"/>'),
 "linkedin": _svg('<rect x="2" y="2" width="20" height="20" rx="3"/><path d="M7 10v7M7 7v.01M11 17v-4a2 2 0 0 1 4 0v4M11 17v-7" />'),
}
def icon(name): return ICONS.get(name, ICONS["star"])

PRODUCT_ICON = {p["slug"]: p["icon"] for p in PRODUCTS}

# ---------------- real images from the live WordPress site ----------------
IMG = "https://medadadv.ae/wp-content/uploads/2023/11/"
PRODUCT_IMG = {
    "acrylic-designs": IMG+"Acrylic.jpeg",
    "art-decor": IMG+"art-decor.jpeg",
    "banner-designs": IMG+"banner-designs.jpeg",
    "directory-sign": IMG+"directory-signs.jpeg",
    "indoor-designs": IMG+"indoor.jpeg",
    "label-and-tags": IMG+"labels-tags.jpeg",
    "laser-cutout": IMG+"laser.jpeg",
    "packaging": IMG+"packaging.jpeg",
    "promotional-design": IMG+"promotional.jpeg",
    "signages": IMG+"singages.jpeg",
    "sports-design": IMG+"sports.jpeg",
    "stand-designs": IMG+"stands.jpeg",
    "stikers-designing": IMG+"stickers.jpeg",
    "trophy-designs": IMG+"trophy.jpeg",
    "vehicle-printing-designs": IMG+"vehicle.jpeg",
}
ARTICLE_IMG = {
    "new-dtf-uv-printing-machine": IMG+"stickers.jpeg",
    "choosing-the-right-signage-in-dubai": IMG+"singages.jpeg",
    "acrylic-signage-why-it-stands-out": IMG+"Acrylic.jpeg",
    "vehicle-wrapping-guide": IMG+"vehicle.jpeg",
    "roll-up-banners-for-events": IMG+"promotional.jpeg",
    "large-format-printing-trends-2026": IMG+"banner-designs.jpeg",
}
def pimg(slug): return PRODUCT_IMG.get(slug, "")
def aimg(slug): return ARTICLE_IMG.get(slug, "")

# ---------------- helpers ----------------
def bil(en, ar):
    """element text holder with both languages; default renders EN."""
    return 'data-en="%s" data-ar="%s"' % (en.replace('"','&quot;'), ar.replace('"','&quot;'))

def t(tag, en, ar, cls=""):
    c = ' class="%s"' % cls if cls else ""
    return '<%s%s %s>%s</%s>' % (tag, c, bil(en, ar), en, tag)

def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)

# ---------------- head ----------------
def head(title_en, title_ar, desc_en, desc_ar, slug, jsonld=None, og_type="website"):
    url = SITE + "/" + (slug + "/" if slug else "")
    ld = ""
    if jsonld:
        ld = "\n".join('<script type="application/ld+json">%s</script>' % json.dumps(j, ensure_ascii=False) for j in jsonld)
    return '''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-en="{te}" data-ar="{ta}">{te}</title>
<meta name="description" data-en="{de}" data-ar="{da}" content="{de}">
<meta name="keywords" content="Medad, advertising Dubai, printing Dubai, signage UAE, acrylic, banner, vehicle branding, DTF, UV printing, stickers, roll up, مداد, طباعة دبي, لوحات اعلانية, دعاية واعلان">
<meta name="author" content="Medad Advertising Requisites L.L.C">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{ot}">
<meta property="og:site_name" content="Medad Advertising">
<meta property="og:title" content="{te}">
<meta property="og:description" content="{de}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}/assets/img/og-image.svg">
<meta property="og:locale" content="en_AE">
<meta property="og:locale:alternate" content="ar_AE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{te}">
<meta name="twitter:description" content="{de}">
<meta name="theme-color" content="#383E8F">
<link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg">
<link rel="apple-touch-icon" href="/assets/img/favicon.svg">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="ar" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Noto+Kufi+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/styles.css">
{ld}
</head>
<body>
'''.format(te=title_en, ta=title_ar, de=desc_en, da=desc_ar, url=url, ot=og_type,
           site=SITE, ld=ld)

# ---------------- header ----------------
def nav_dropdown():
    items = ""
    for p in PRODUCTS:
        items += '<a href="/{s}/">{ic}<span {b}>{en}</span></a>'.format(
            s=p["slug"], ic=icon(p["icon"]), b=bil(p["en"], p["ar"]), en=p["en"])
    return items

def header(active=""):
    def a(href, en, ar, key):
        cls = ' class="active"' if key == active else ''
        return '<li><a href="%s"%s %s>%s</a></li>' % (href, cls, bil(en, ar), en)
    drop = nav_dropdown()
    # mobile product links
    mprods = "".join('<a href="/{s}/" {b}>{en}</a>'.format(s=p["slug"], b=bil(p["en"],p["ar"]), en=p["en"]) for p in PRODUCTS)
    return '''<header class="site-header">
<div class="container nav">
  <a class="brand" href="/" aria-label="Medad Advertising home"><img src="/assets/img/logo.svg" alt="Medad Advertising Requisites L.L.C"></a>
  <ul class="nav-links">
    {home}
    {about}
    <li class="has-drop"><button class="nav-item-btn" {bprod}>Products {arrow}</button>
      <div class="dropdown">{drop}</div></li>
    {blog}
    {contact}
  </ul>
  <div class="nav-actions">
    <button class="lang-toggle lang-desktop" data-toggle-lang aria-label="Switch language">{globe}<span data-langlabel>عربي</span></button>
    <a class="btn btn-primary lang-desktop" href="/contact/" {bquote}>Get a Quote</a>
    <button class="lang-toggle" data-toggle-lang aria-label="Switch language" style="display:none">{globe}<span data-langlabel>عربي</span></button>
    <button class="nav-toggle" data-open-menu aria-label="Open menu">{menu}</button>
  </div>
</div>
</header>
<div class="mobile-menu" data-close-menu>
  <div class="mobile-panel">
    <div class="m-head"><img src="/assets/img/logo.svg" alt="Medad" style="height:34px"><button data-close-menu aria-label="Close">{close}</button></div>
    <a href="/" {bhome}>Home</a>
    <a href="/about-us/" {babout}>About Us</a>
    <div style="padding:13px 6px;border-bottom:1px solid var(--line);font-weight:600" {bprod2}>Products</div>
    <div class="sub">{mprods}</div>
    <a href="/blog/" {bblog}>Articles</a>
    <a href="/contact/" {bcontact}>Contact</a>
    <button class="lang-toggle" data-toggle-lang style="margin-top:16px">{globe}<span data-langlabel>عربي</span></button>
  </div>
</div>'''.format(
        home=a("/", "Home", "الرئيسية", "home"),
        about=a("/about-us/", "About Us", "من نحن", "about"),
        blog=a("/blog/", "Articles", "المقالات", "blog"),
        contact=a("/contact/", "Contact", "تواصل معنا", "contact"),
        drop=drop, arrow=icon("arrow"), globe=icon("globe"), menu=icon("menu"), close=icon("close"),
        bprod=bil("Products","المنتجات"), bprod2=bil("Products","المنتجات"),
        bquote=bil("Get a Quote","اطلب عرض سعر"),
        bhome=bil("Home","الرئيسية"), babout=bil("About Us","من نحن"),
        bblog=bil("Articles","المقالات"), bcontact=bil("Contact","تواصل معنا"),
        mprods=mprods)

# ---------------- footer ----------------
def footer():
    prod_links = "".join('<li><a href="/{s}/" {b}>{en}</a></li>'.format(s=p["slug"], b=bil(p["en"],p["ar"]), en=p["en"]) for p in PRODUCTS[:8])
    return '''<footer class="site-footer">
<div class="container">
  <div class="footer-grid">
    <div>
      <img src="/assets/img/logo-white.svg" alt="Medad Advertising">
      <p {babout}>Your trusted partner in Dubai for digital printing, signage and advertising solutions — turning ideas into vibrant, precise prints.</p>
      <div class="foot-social">
        <a href="https://wa.me/971508050150" aria-label="WhatsApp" target="_blank" rel="noopener">{wa}</a>
        <a href="https://www.instagram.com/" aria-label="Instagram" target="_blank" rel="noopener">{insta}</a>
        <a href="https://www.facebook.com/" aria-label="Facebook" target="_blank" rel="noopener">{fb}</a>
        <a href="https://www.linkedin.com/" aria-label="LinkedIn" target="_blank" rel="noopener">{linkedin}</a>
      </div>
    </div>
    <div>
      <h4 {bquick}>Quick Links</h4>
      <ul>
        <li><a href="/" {bhome}>Home</a></li>
        <li><a href="/about-us/" {babout2}>About Us</a></li>
        <li><a href="/blog/" {bblog}>Articles</a></li>
        <li><a href="/contact/" {bcontact}>Contact</a></li>
      </ul>
    </div>
    <div>
      <h4 {bserv}>Services</h4>
      <ul>{prod_links}</ul>
    </div>
    <div>
      <h4 {bget}>Get in Touch</h4>
      <ul class="foot-contact">
        <li>{pin}<span {baddr}>{addr_en}</span></li>
        <li>{phone}<a href="tel:{tel}">{tel_disp}</a></li>
        <li>{mobile}<a href="https://wa.me/971508050150" target="_blank" rel="noopener">{mobile_disp}</a></li>
        <li>{mail}<a href="mailto:{email}">{email}</a></li>
        <li>{clock}<span {bhours}>Sun–Thu: 9am–6pm</span></li>
      </ul>
    </div>
  </div>
  <div class="foot-bottom">
    <span>© <span id="year">2026</span> {cname} · <span {brights}>All rights reserved.</span> · TRN {trn}</span>
    <span class="dev" {bdev}>Designed &amp; developed by <b>Mohamed Reda</b></span>
  </div>
</div>
</footer>
<script src="/assets/js/main.js" defer></script>
<script src="/assets/js/slider.js" defer></script>
<script src="/assets/js/chatbot.js" defer></script>
</body>
</html>'''.format(
        wa=icon("wa"), insta=icon("insta"), fb=icon("fb"), linkedin=icon("linkedin"),
        pin=icon("pin"), phone=icon("phone"), mobile=icon("mobile"), mail=icon("mail"), clock=icon("clock"),
        prod_links=prod_links,
        babout=bil("Your trusted partner in Dubai for digital printing, signage and advertising solutions — turning ideas into vibrant, precise prints.",
                   "شريكك الموثوق في دبي لحلول الطباعة الرقمية واللوحات الإعلانية والدعاية — نحوّل الأفكار إلى مطبوعات دقيقة وزاهية."),
        babout2=bil("About Us","من نحن"),
        bquick=bil("Quick Links","روابط سريعة"), bserv=bil("Services","خدماتنا"),
        bget=bil("Get in Touch","تواصل معنا"), bhome=bil("Home","الرئيسية"),
        bblog=bil("Articles","المقالات"), bcontact=bil("Contact","تواصل معنا"),
        baddr=bil(COMPANY["addr_en"], COMPANY["addr_ar"]), addr_en=COMPANY["addr_en"],
        tel=COMPANY["tel"], tel_disp=COMPANY["tel_disp"], mobile_disp=COMPANY["mobile_disp"],
        email=COMPANY["email"], bhours=bil("Sun–Thu: 9am–6pm","الأحد–الخميس: 9ص–6م"),
        cname=COMPANY["name_en"], trn=COMPANY["trn"],
        brights=bil("All rights reserved.","جميع الحقوق محفوظة."),
        bdev=bil('Designed &amp; developed by <b>Mohamed Reda</b>','تصميم وتطوير <b>Mohamed Reda</b>'))

# ---------------- structured data ----------------
def org_jsonld():
    return {
        "@context":"https://schema.org","@type":"LocalBusiness",
        "@id": SITE + "/#org",
        "name": COMPANY["name_en"], "alternateName": COMPANY["name_ar"],
        "url": SITE, "image": SITE+"/assets/img/logo.svg", "logo": SITE+"/assets/img/logo.svg",
        "description":"Dubai-based digital printing, signage and advertising company offering acrylic, banners, signboards, vehicle branding, stickers, DTF and UV printing.",
        "telephone": COMPANY["tel"], "email": COMPANY["email"],
        "address":{"@type":"PostalAddress","streetAddress":"Al Habtoor Complex, Office 57, Al Qusais 3rd Industrial Zone",
                   "addressLocality":"Dubai","addressCountry":"AE","postOfficeBoxNumber":"237358"},
        "geo":{"@type":"GeoCoordinates","latitude":COMPANY["lat"],"longitude":COMPANY["lng"]},
        "areaServed":"AE","priceRange":"$$",
        "openingHoursSpecification":[
            {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"17:00"},
            {"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"10:00","closes":"14:00"}],
        "sameAs":["https://wa.me/971508050150"]
    }

def breadcrumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList",
        "itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate(items)]}

# ---------------- shared blocks ----------------
def page_hero(en_title, ar_title, en_sub, ar_sub, crumb_en, crumb_ar):
    return '''<section class="page-hero"><div class="container">
  <div class="crumb"><a href="/" {bh}>Home</a>{arrow}<span {bc}>{ce}</span></div>
  <h1 {bt}>{te}</h1>
  <p style="color:var(--muted);max-width:680px;margin-top:10px" {bs}>{se}</p>
</div></section>'''.format(bh=bil("Home","الرئيسية"), arrow=icon("arrow"),
        bc=bil(crumb_en,crumb_ar), ce=crumb_en, bt=bil(en_title,ar_title), te=en_title,
        bs=bil(en_sub,ar_sub), se=en_sub)

def cta_band():
    return '''<section><div class="container"><div class="band reveal">
  <div class="grid grid-2" style="align-items:center;gap:30px">
    <div>
      <h2 style="color:#fff;font-size:1.9rem" {bt}>Ready to start your project?</h2>
      <p style="color:rgba(255,255,255,.9);margin-top:10px" {bp}>Tell us what you need printed — we'll reply fast with a competitive quote.</p>
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:flex-end">
      <a class="btn btn-light" href="tel:{tel}">{ph}<span {bcall}>Call Now</span></a>
      <a class="btn btn-ghost" href="/contact/" {bq}>Get a Quote</a>
    </div>
  </div></div></div></section>'''.format(
        bt=bil("Ready to start your project?","جاهز تبدأ مشروعك؟"),
        bp=bil("Tell us what you need printed — we'll reply fast with a competitive quote.",
               "قل لنا ما تحتاج طباعته — وسنردّ بسرعة بعرض سعر منافس."),
        tel=COMPANY["tel"], ph=icon("phone"), bcall=bil("Call Now","اتصل الآن"),
        bq=bil("Get a Quote","اطلب عرض سعر"))

# ---------------- HOME ----------------
def build_home():
    # service cards
    cards = ""
    for p in PRODUCTS:
        cards += '''<a class="card has-media reveal" href="/{s}/">
          <div class="card-media"><div class="media-img"><img src="{img}" alt="{en}" loading="lazy" decoding="async"></div><div class="ic">{ic}</div></div>
          <h3 {bt}>{en}</h3>
          <p {bd}>{de}</p>
          <span class="more" {bm}>Learn more {ar}</span>
        </a>'''.format(s=p["slug"], img=pimg(p["slug"]), ic=icon(p["icon"]), bt=bil(p["en"],p["ar"]), en=p["en"],
                       bd=bil(p["desc_en"],p["desc_ar"]), de=p["desc_en"],
                       bm=bil("Learn more","اعرف المزيد"), ar=icon("arrow"))
    whys = [
        ("rocket","State-of-the-Art Technology","أحدث التقنيات","Latest digital, UV and DTF printing for unmatched clarity and color.","أحدث طباعة رقمية وUV وDTF لوضوح وألوان لا تُضاهى."),
        ("palette","Full Customization","تخصيص كامل","Every print tailored to your brand, size and material.","كل مطبوعة مفصّلة على علامتك ومقاسك وخامتك."),
        ("clock","On-Time Delivery","تسليم في الموعد","Efficient processes that meet your deadlines, every time.","عمليات فعّالة تلتزم بمواعيدك في كل مرة."),
        ("shield","Quality Assurance","ضمان الجودة","Rigorous quality control on every single job.","رقابة جودة صارمة على كل عمل."),
    ]
    why_html = ""
    for ic,en,ar,de,da in whys:
        why_html += '<div class="feature reveal"><div class="ic">{ic}</div><div><h3 {bt}>{en}</h3><p {bd}>{de}</p></div></div>'.format(
            ic=icon(ic), bt=bil(en,ar), en=en, bd=bil(de,da), de=de)
    # latest articles
    posts = ""
    for art in ARTICLES[:3]:
        posts += article_card(art)
    clients = ["VOGUE","NIKE","DISNEY","COSTCO","FERRARI","SONY","TARGET","L'OCCITANE"]
    cl = "".join("<span>%s</span>" % c for c in clients*2)

    jl = [org_jsonld(),
          {"@context":"https://schema.org","@type":"WebSite","url":SITE,"name":COMPANY["name_en"],
           "inLanguage":["en","ar"]}]
    html = head("Medad Advertising Requisites L.L.C — Printing & Signage in Dubai, UAE",
                "مداد للوسائل الإعلانية ذ.م.م — طباعة ولوحات إعلانية في دبي",
                "Medad Advertising in Dubai: large-format & UV/DTF printing, signboards, acrylic, banners, stickers, vehicle branding, roll-ups and more. Fast, premium, competitive.",
                "مداد للإعلان في دبي: طباعة كبيرة المقاس وUV/DTF، لوحات إعلانية، أكريليك، بنرات، ستيكرات، تغليف مركبات ورول أب وأكثر. سريع وفاخر ومنافس.",
                "", jsonld=jl)
    html += header(active="home")
    # ---- hero slider (featured services) ----
    pmap = {p["slug"]: p for p in PRODUCTS}
    featured = ["signages","vehicle-printing-designs","acrylic-designs","stand-designs","stikers-designing","laser-cutout"]
    slides = ""
    for k, slug in enumerate(featured):
        p = pmap[slug]
        slides += '''<div class="hs-slide{act}">
      <img class="hs-bg" src="{img}" alt="{en}" {ld} decoding="async">
      <div class="hs-overlay"></div>
      <div class="hs-inner"><div class="container"><div class="hs-content">
        <span class="hs-eyebrow" {beb}>Our Services</span>
        <h1 class="hs-title" {bt}>{en}</h1>
        <p class="hs-desc" {bd}>{de}</p>
        <div class="hs-cta">
          <a class="btn btn-light" href="/{slug}/" {bv}>View details {ar}</a>
          <a class="btn btn-ghost" href="/contact/" {bq}>Get a Quote</a>
        </div>
      </div></div></div>
    </div>'''.format(act=" active" if k==0 else "", img=pimg(slug),
            ld='fetchpriority="high"' if k==0 else 'loading="lazy"',
            en=p["en"], beb=bil("Our Services","خدماتنا"),
            bt=bil(p["en"],p["ar"]), bd=bil(p["desc_en"],p["desc_ar"]), de=p["desc_en"],
            slug=slug, bv=bil("View details","عرض التفاصيل"), ar=icon("arrow"),
            bq=bil("Get a Quote","اطلب عرض سعر"))
    html += '''<section class="hero-slider" aria-label="Featured services">
  <div class="hs-slides">{slides}</div>
  <button class="hs-arrow hs-prev" aria-label="Previous slide">{prev}</button>
  <button class="hs-arrow hs-next" aria-label="Next slide">{next}</button>
  <div class="hs-dots" role="tablist"></div>
</section>'''.format(slides=slides,
        prev='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>',
        next='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg>')

    html += '''<section id="services"><div class="container">
  <div class="sec-head center reveal">
    <span class="eyebrow">{eb}</span>
    <h2 {bt}>Everything you need, under one roof</h2>
    <p {bp}>A complete range of advertising, printing and signage solutions for businesses across the UAE.</p>
  </div>
  <div class="grid grid-3">{cards}</div>
</div></section>'''.format(eb='<span data-en="What we do" data-ar="ما نقدّمه">What we do</span>',
        bt=bil("Everything you need, under one roof","كل ما تحتاجه تحت سقف واحد"),
        bp=bil("A complete range of advertising, printing and signage solutions for businesses across the UAE.",
               "مجموعة متكاملة من حلول الدعاية والطباعة واللوحات الإعلانية للشركات في كل الإمارات."),
        cards=cards)

    html += '''<section class="bg-alt"><div class="container">
  <div class="grid grid-2" style="gap:50px;align-items:center">
    <div class="reveal">
      <span class="eyebrow">{eb}</span>
      <h2 style="font-size:2.1rem" {bt}>Why brands choose Medad</h2>
      <p style="color:var(--muted);margin:14px 0 26px" {bp}>We're not just a printing company — we're a creative partner committed to quality, innovation and a seamless experience.</p>
      <div style="display:grid;gap:22px">{why}</div>
    </div>
    <div class="reveal">
      <div class="band">
        <div class="grid grid-2">
          <div class="stat"><b>15+</b><span {s1}>Service categories</span></div>
          <div class="stat"><b>100%</b><span {s2}>Quality checked</span></div>
          <div class="stat"><b>24h</b><span {s3}>Support hotline</span></div>
          <div class="stat"><b>UAE</b><span {s4}>Nationwide service</span></div>
        </div>
      </div>
    </div>
  </div>
</div></section>'''.format(eb='<span data-en="Why us" data-ar="لماذا نحن">Why us</span>',
        bt=bil("Why brands choose Medad","لماذا تختار العلامات مداد"),
        bp=bil("We're not just a printing company — we're a creative partner committed to quality, innovation and a seamless experience.",
               "نحن لسنا مجرد شركة طباعة — بل شريك إبداعي ملتزم بالجودة والابتكار وتجربة سلسة."),
        why=why_html, s1=bil("Service categories","فئات الخدمات"), s2=bil("Quality checked","فحص الجودة"),
        s3=bil("Support hotline","خط دعم"), s4=bil("Nationwide service","خدمة في كل الإمارات"))

    html += '''<section><div class="container">
  <div class="sec-head center reveal"><span class="eyebrow">{eb}</span>
  <h2 {bt}>Trusted by leading brands</h2></div>
  <div class="marquee"><div class="marquee-track">{cl}</div></div>
</div></section>'''.format(eb='<span data-en="Our clients" data-ar="عملاؤنا">Our clients</span>',
        bt=bil("Trusted by leading brands","موضع ثقة علامات رائدة"), cl=cl)

    html += '''<section class="bg-alt"><div class="container">
  <div class="sec-head reveal" style="display:flex;justify-content:space-between;align-items:flex-end;max-width:none;flex-wrap:wrap;gap:16px">
    <div><span class="eyebrow">{eb}</span><h2 {bt}>From our blog</h2></div>
    <a class="btn btn-ghost" href="/blog/" {ba}>View all articles {ar}</a>
  </div>
  <div class="grid grid-3">{posts}</div>
</div></section>'''.format(eb='<span data-en="Insights" data-ar="مقالات">Insights</span>',
        bt=bil("From our blog","من مدونتنا"), ba=bil("View all articles","كل المقالات"), ar=icon("arrow"), posts=posts)

    html += cta_band()
    html += footer()
    write("index.html", html)

# ---------------- ABOUT ----------------
def build_about():
    feats = [
        ("rocket","State-of-the-Art Technology","أحدث التقنيات","We invest in the latest digital, UV and DTF printing for unparalleled clarity, color accuracy and detail.","نستثمر في أحدث الطباعة الرقمية وUV وDTF لوضوح ودقة ألوان وتفاصيل لا تُضاهى."),
        ("palette","Customization","التخصيص","Your brand is unique — tailor every aspect of your prints to your exact requirements.","علامتك فريدة — خصّص كل تفصيلة في مطبوعاتك حسب متطلباتك بالضبط."),
        ("clock","Timely Delivery","التسليم في الوقت","Efficient processes and a dedicated team ensure on-time delivery without compromising quality.","عمليات فعّالة وفريق متخصّص يضمنون التسليم في الموعد دون المساس بالجودة."),
        ("shield","Quality Assurance","ضمان الجودة","Every print passes rigorous quality control to meet our high standards.","كل مطبوعة تمر برقابة جودة صارمة لتلبّي معاييرنا العالية."),
        ("users","Customer-Centric","التركيز على العميل","We work closely with you to understand your needs and exceed expectations.","نعمل معك عن قرب لفهم احتياجاتك وتجاوز توقّعاتك."),
        ("star","Affordability","أسعار في المتناول","High-quality printing at competitive prices — real value for your investment.","طباعة عالية الجودة بأسعار منافسة — قيمة حقيقية لاستثمارك."),
    ]
    fh = ""
    for ic,en,ar,de,da in feats:
        fh += '<div class="card reveal"><div class="ic">{ic}</div><h3 {bt}>{en}</h3><p {bd}>{de}</p></div>'.format(
            ic=icon(ic), bt=bil(en,ar), en=en, bd=bil(de,da), de=de)
    jl = [org_jsonld(), breadcrumb([("Home",SITE+"/"),("About Us",SITE+"/about-us/")])]
    html = head("About Us — Medad Advertising Requisites L.L.C, Dubai",
                "من نحن — مداد للوسائل الإعلانية ذ.م.م، دبي",
                "Learn about Medad Advertising: a Dubai-based digital printing and signage company built on technology, customization, quality and customer focus.",
                "تعرّف على مداد للإعلان: شركة طباعة رقمية ولوحات إعلانية في دبي قائمة على التقنية والتخصيص والجودة والاهتمام بالعميل.",
                "about-us", jsonld=jl)
    html += header(active="about")
    html += page_hero("About Medad Advertising","عن مداد للوسائل الإعلانية",
        "Your gateway to exceptional digital printing solutions in Dubai.",
        "بوابتك لحلول طباعة رقمية استثنائية في دبي.","About Us","من نحن")
    html += '''<section><div class="container prose reveal" style="max-width:880px">
  <h2 {bw}>Welcome to Medad Advertising</h2>
  <p {p1}>At Medad Advertising, we take pride in being your trusted partner for all your digital printing needs. Our commitment to excellence, cutting-edge technology and unwavering dedication to customer satisfaction set us apart as a premier player in the world of digital printing.</p>
  <p {p2}>Medad Advertising is not just a printing company; we are a creative hub where ideas come to life in vibrant colors and precision. Our team of skilled professionals is passionate about transforming your concepts into visually stunning prints that make a lasting impact.</p>
  <h3 {bm}>Our Mission</h3>
  <p {p3}>To empower businesses and individuals with top-notch digital printing solutions. We strive to be the go-to destination for those who demand quality, innovation and a seamless printing experience — a partnership that enhances your brand and communicates your message effectively.</p>
</div></section>'''.format(
        bw=bil("Welcome to Medad Advertising","أهلاً بك في مداد للإعلان"),
        p1=bil("At Medad Advertising, we take pride in being your trusted partner for all your digital printing needs. Our commitment to excellence, cutting-edge technology and unwavering dedication to customer satisfaction set us apart as a premier player in the world of digital printing.",
               "في مداد للإعلان، نفخر بأن نكون شريكك الموثوق لكل احتياجاتك من الطباعة الرقمية. التزامنا بالتميّز وأحدث التقنيات وتفانينا الدائم في رضا العميل يميّزنا كلاعب رائد في عالم الطباعة الرقمية."),
        p2=bil("Medad Advertising is not just a printing company; we are a creative hub where ideas come to life in vibrant colors and precision. Our team of skilled professionals is passionate about transforming your concepts into visually stunning prints that make a lasting impact.",
               "مداد ليست مجرد شركة طباعة؛ بل مركز إبداعي تتحوّل فيه الأفكار إلى ألوان زاهية ودقة عالية. فريقنا من المحترفين شغوف بتحويل تصوّراتك إلى مطبوعات مبهرة تترك أثرًا دائمًا."),
        bm=bil("Our Mission","مهمتنا"),
        p3=bil("To empower businesses and individuals with top-notch digital printing solutions. We strive to be the go-to destination for those who demand quality, innovation and a seamless printing experience — a partnership that enhances your brand and communicates your message effectively.",
               "تمكين الشركات والأفراد بحلول طباعة رقمية من الطراز الأول. نسعى لأن نكون الوجهة الأولى لمن يطلبون الجودة والابتكار وتجربة طباعة سلسة — شراكة تعزّز علامتك وتوصّل رسالتك بفعالية."))
    html += '''<section class="bg-alt"><div class="container">
  <div class="sec-head center reveal"><span class="eyebrow">{eb}</span>
  <h2 {bt}>What makes us stand out</h2></div>
  <div class="grid grid-3">{fh}</div>
</div></section>'''.format(eb='<span data-en="Our advantage" data-ar="ما يميّزنا">Our advantage</span>',
        bt=bil("What makes us stand out","ما الذي يميّزنا"), fh=fh)
    html += cta_band()
    html += footer()
    write("about-us/index.html", html)

# ---------------- PRODUCT ----------------
def build_product(p, idx):
    feats = ""
    fen = p["feats_en"]; far = p["feats_ar"]
    for i in range(len(fen)):
        feats += '<li {b}>{en}</li>'.format(b=bil(fen[i],far[i]), en=fen[i])
    # related (next 3)
    rel = [PRODUCTS[(idx+k+1) % len(PRODUCTS)] for k in range(3)]
    rel_html = ""
    for r in rel:
        rel_html += '''<a class="card has-media reveal" href="/{s}/">
          <div class="card-media"><div class="media-img"><img src="{img}" alt="{en}" loading="lazy" decoding="async"></div><div class="ic">{ic}</div></div>
          <h3 {bt}>{en}</h3><p {bd}>{de}</p>
          <span class="more" {bm}>Learn more {ar}</span></a>'''.format(
            s=r["slug"], img=pimg(r["slug"]), ic=icon(r["icon"]), bt=bil(r["en"],r["ar"]), en=r["en"],
            bd=bil(r["desc_en"],r["desc_ar"]), de=r["desc_en"], bm=bil("Learn more","اعرف المزيد"), ar=icon("arrow"))
    jl = [breadcrumb([("Home",SITE+"/"),(p["en"],SITE+"/"+p["slug"]+"/")]),
          {"@context":"https://schema.org","@type":"Service","name":p["en"],"description":p["desc_en"],
           "provider":{"@id":SITE+"/#org"},"areaServed":"AE","serviceType":p["en"]}]
    html = head("%s — Medad Advertising Dubai" % p["en"],
                "%s — مداد للإعلان دبي" % p["ar"],
                p["desc_en"], p["desc_ar"], p["slug"], jsonld=jl, og_type="article")
    html += header(active="")
    html += page_hero(p["en"], p["ar"], p["desc_en"], p["desc_ar"], p["en"], p["ar"])
    html += '''<section><div class="container">
  <div class="grid grid-2" style="gap:46px;align-items:start">
    <div class="prose reveal">
      <div class="ic" style="width:64px;height:64px;border-radius:18px;background:var(--grad);display:grid;place-items:center;margin-bottom:20px">
        <span style="color:#fff;display:grid;place-items:center">{bigic}</span></div>
      <h2 {bt}>{en}</h2>
      <p {bi}>{intro}</p>
      <h3 {bh}>Highlights</h3>
      <ul class="bullets">{feats}</ul>
      <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:24px">
        <a class="btn btn-primary" href="/contact/" {bq}>Request a Quote</a>
        <a class="btn btn-ghost" href="https://wa.me/971508050150" target="_blank" rel="noopener">{wa}<span {bw}>WhatsApp Us</span></a>
      </div>
    </div>
    <div class="reveal">
      <figure class="product-banner" style="margin-bottom:22px"><img src="{pbanner}" alt="{en} — Medad Advertising Dubai" loading="lazy" decoding="async"></figure>
      <div class="card" style="background:var(--grad-soft);border:none">
        <h3 style="margin-bottom:14px" {bn}>Why Medad for this</h3>
        <div style="display:grid;gap:16px">
          <div class="feature"><div class="ic">{i1}</div><div><h3 {f1}>Premium materials</h3><p {f1d}>We use durable, color-stable materials suited to the UAE climate.</p></div></div>
          <div class="feature"><div class="ic">{i2}</div><div><h3 {f2}>Design to install</h3><p {f2d}>One team handles design, production and professional installation.</p></div></div>
          <div class="feature"><div class="ic">{i3}</div><div><h3 {f3}>Fast turnaround</h3><p {f3d}>Efficient processes that respect your deadlines.</p></div></div>
        </div>
      </div>
    </div>
  </div>
</div></section>'''.format(
        bigic=icon(p["icon"]), bt=bil(p["en"],p["ar"]), en=p["en"], pbanner=pimg(p["slug"]),
        bi=bil(p["intro_en"],p["intro_ar"]), intro=p["intro_en"],
        bh=bil("Highlights","أبرز المزايا"), feats=feats,
        bq=bil("Request a Quote","اطلب عرض سعر"), wa=icon("wa"), bw=bil("WhatsApp Us","راسلنا واتساب"),
        bn=bil("Why Medad for this","لماذا مداد لهذا"),
        i1=icon("shield"), f1=bil("Premium materials","خامات فاخرة"),
        f1d=bil("We use durable, color-stable materials suited to the UAE climate.","نستخدم خامات متينة وثابتة اللون تناسب مناخ الإمارات."),
        i2=icon("palette"), f2=bil("Design to install","من التصميم للتركيب"),
        f2d=bil("One team handles design, production and professional installation.","فريق واحد يتولّى التصميم والإنتاج والتركيب الاحترافي."),
        i3=icon("rocket"), f3=bil("Fast turnaround","تنفيذ سريع"),
        f3d=bil("Efficient processes that respect your deadlines.","عمليات فعّالة تحترم مواعيدك."))
    html += '''<section class="bg-alt"><div class="container">
  <div class="sec-head reveal"><span class="eyebrow">{eb}</span><h2 {bt}>You may also need</h2></div>
  <div class="grid grid-3">{rel}</div>
</div></section>'''.format(eb='<span data-en="Related services" data-ar="خدمات ذات صلة">Related services</span>',
        bt=bil("You may also need","قد تحتاج أيضًا"), rel=rel_html)
    html += cta_band()
    html += footer()
    write("%s/index.html" % p["slug"], html)

# ---------------- BLOG ----------------
def article_card(art):
    return '''<a class="post-card reveal" href="/blog/{s}/">
      <div class="post-thumb"><img src="{img}" alt="{te}" loading="lazy" decoding="async"><span class="post-tag" {bc}>{ce}</span></div>
      <div class="post-body">
        <div class="meta"><span {bd}>{dd}</span></div>
        <h3 {bt}>{te}</h3>
        <p {bx}>{xe}</p>
        <span class="more" {bm}>Read article {ar}</span>
      </div>
    </a>'''.format(s=art["slug"], ic=icon(art["icon"]), img=aimg(art["slug"]),
        bc=bil(art["cat_en"],art["cat_ar"]), ce=art["cat_en"],
        bd=bil(fmt_date(art["date"],"en"),fmt_date(art["date"],"ar")), dd=fmt_date(art["date"],"en"),
        bt=bil(art["title_en"],art["title_ar"]), te=art["title_en"],
        bx=bil(art["excerpt_en"],art["excerpt_ar"]), xe=art["excerpt_en"],
        bm=bil("Read article","اقرأ المقال"), ar=icon("arrow"))

MONTHS_AR = ["يناير","فبراير","مارس","أبريل","مايو","يونيو","يوليو","أغسطس","سبتمبر","أكتوبر","نوفمبر","ديسمبر"]
def fmt_date(d, lang):
    y,m,day = d.split("-"); m=int(m)
    if lang=="ar": return "%s %s %s" % (int(day), MONTHS_AR[m-1], y)
    import calendar
    return "%s %s, %s" % (calendar.month_abbr[m], int(day), y)

def build_blog_index():
    cards = "".join(article_card(a) for a in ARTICLES)
    jl = [breadcrumb([("Home",SITE+"/"),("Articles",SITE+"/blog/")]),
          {"@context":"https://schema.org","@type":"Blog","url":SITE+"/blog/","name":"Medad Advertising Blog",
           "publisher":{"@id":SITE+"/#org"}}]
    html = head("Articles &amp; Insights — Medad Advertising Dubai",
                "المقالات والرؤى — مداد للإعلان دبي",
                "Guides and insights on printing, signage, UV & DTF technology, vehicle wraps and large-format trends from Medad Advertising in Dubai.",
                "أدلّة ورؤى حول الطباعة واللوحات الإعلانية وتقنية UV وDTF وتغليف المركبات واتجاهات الطباعة كبيرة المقاس من مداد في دبي.",
                "blog", jsonld=jl)
    html += header(active="blog")
    html += page_hero("Articles &amp; Insights","المقالات والرؤى",
        "Practical guides on printing, signage and the technology behind great brand visuals.",
        "أدلّة عملية حول الطباعة واللوحات والتقنية وراء أفضل هويات العلامات.","Articles","المقالات")
    html += '<section><div class="container"><div class="grid grid-3">%s</div></div></section>' % cards
    html += cta_band()
    html += footer()
    write("blog/index.html", html)

def build_article(art, idx):
    # body
    body = ""
    for typ, val in art["body_en"]:
        # find AR counterpart by index
        pass
    # build with parallel en/ar lists
    en_blocks = art["body_en"]; ar_blocks = art["body_ar"]
    for i,(typ,val) in enumerate(en_blocks):
        av = ar_blocks[i][1]
        if typ=="h2": body += t("h2", val, av)
        elif typ=="h3": body += t("h3", val, av)
        elif typ=="p": body += t("p", val, av)
        elif typ=="callout": body += '<div class="callout"><p style="margin:0" %s>%s</p></div>' % (bil(val,av), val)
        elif typ=="ul":
            lis=""
            for j,li in enumerate(val):
                lis += '<li %s>%s</li>' % (bil(li, av[j]), li)
            body += '<ul class="bullets">%s</ul>' % lis
    # related
    rel = [ARTICLES[(idx+k+1) % len(ARTICLES)] for k in range(3)]
    rel_html = "".join(article_card(r) for r in rel)
    jl = [breadcrumb([("Home",SITE+"/"),("Articles",SITE+"/blog/"),(art["title_en"],SITE+"/blog/"+art["slug"]+"/")]),
          {"@context":"https://schema.org","@type":"BlogPosting",
           "headline":art["title_en"],"description":art["excerpt_en"],
           "datePublished":art["date"],"dateModified":art["date"],
           "inLanguage":"en","image":SITE+"/assets/img/og-image.svg",
           "author":{"@type":"Organization","name":COMPANY["name_en"]},
           "publisher":{"@id":SITE+"/#org"},
           "mainEntityOfPage":SITE+"/blog/"+art["slug"]+"/"}]
    html = head("%s — Medad Advertising" % art["title_en"],
                "%s — مداد للإعلان" % art["title_ar"],
                art["excerpt_en"], art["excerpt_ar"], "blog/"+art["slug"], jsonld=jl, og_type="article")
    html += header(active="blog")
    html += '''<section class="page-hero"><div class="container">
  <div class="crumb"><a href="/" {bh}>Home</a>{a1}<a href="/blog/" {bb}>Articles</a>{a2}<span {bc}>{ce}</span></div>
  <span class="post-tag" style="position:static;display:inline-block;margin-bottom:12px" {bcat}>{cat}</span>
  <h1 {bt} style="max-width:840px">{te}</h1>
  <p style="color:var(--muted);margin-top:10px" {bd}>{dd}</p>
</div></section>'''.format(bh=bil("Home","الرئيسية"), a1=icon("arrow"), bb=bil("Articles","المقالات"),
        a2=icon("arrow"), bc=bil(art["cat_en"],art["cat_ar"]), ce=art["cat_en"],
        bcat=bil(art["cat_en"],art["cat_ar"]), cat=art["cat_en"],
        bt=bil(art["title_en"],art["title_ar"]), te=art["title_en"],
        bd=bil(fmt_date(art["date"],"en"),fmt_date(art["date"],"ar")), dd=fmt_date(art["date"],"en"))
    html += '<section><div class="container prose reveal" style="margin-inline:auto">'
    html += '<figure class="article-banner"><img src="%s" alt="%s" loading="lazy" decoding="async"></figure>' % (aimg(art["slug"]), art["title_en"].replace('"',"'"))
    html += body
    html += '''<div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:30px;padding-top:24px;border-top:1px solid var(--line)">
      <a class="btn btn-primary" href="/contact/" {bq}>Get a Quote</a>
      <a class="btn btn-ghost" href="/blog/" {bb}>{back} All Articles</a>
    </div></div></section>'''.format(bq=bil("Get a Quote","اطلب عرض سعر"),
        bb=bil("Back to all articles","العودة لكل المقالات"), back=icon("arrow"))
    html += '''<section class="bg-alt"><div class="container">
  <div class="sec-head reveal"><span class="eyebrow">{eb}</span><h2 {bt}>Keep reading</h2></div>
  <div class="grid grid-3">{rel}</div></div></section>'''.format(
        eb='<span data-en="More articles" data-ar="مقالات أخرى">More articles</span>',
        bt=bil("Keep reading","تابع القراءة"), rel=rel_html)
    html += footer()
    write("blog/%s/index.html" % art["slug"], html)

# ---------------- CONTACT ----------------
def build_contact():
    jl = [org_jsonld(), breadcrumb([("Home",SITE+"/"),("Contact",SITE+"/contact/")]),
          {"@context":"https://schema.org","@type":"ContactPage","url":SITE+"/contact/"}]
    html = head("Contact Medad Advertising — Dubai, UAE",
                "تواصل مع مداد للإعلان — دبي، الإمارات",
                "Contact Medad Advertising in Dubai. Call +971 4 2638380, WhatsApp +971 50 8050150 or email info@medadadv.ae for printing and signage quotes.",
                "تواصل مع مداد للإعلان في دبي. اتصل على +971 4 2638380 أو واتساب +971 50 8050150 أو إيميل info@medadadv.ae لعروض الطباعة واللوحات.",
                "contact", jsonld=jl)
    html += header(active="contact")
    html += page_hero("Contact Us","تواصل معنا",
        "Let's bring your project to life. Reach out for a fast, competitive quote.",
        "لنحقّق مشروعك معًا. تواصل معنا للحصول على عرض سعر سريع ومنافس.","Contact","تواصل معنا")
    cards = [
        ("phone","Phone","الهاتف",COMPANY["tel_disp"],"tel:"+COMPANY["tel"]),
        ("wa","WhatsApp / Mobile","واتساب / موبايل",COMPANY["mobile_disp"],"https://wa.me/971508050150"),
        ("mail","Email","البريد الإلكتروني",COMPANY["email"],"mailto:"+COMPANY["email"]),
    ]
    ic_cards = ""
    for ic,en,ar,val,href in cards:
        ic_cards += '''<div class="info-card reveal"><div class="ic">{ic}</div>
          <div><h4 {bt}>{en}</h4><a href="{href}">{val}</a></div></div>'''.format(
            ic=icon(ic), bt=bil(en,ar), en=en, href=href, val=val)
    html += '''<section><div class="container">
  <div class="grid grid-2" style="gap:40px;align-items:start">
    <div>
      <div style="display:grid;gap:16px;margin-bottom:24px">{cards}
        <div class="info-card reveal"><div class="ic">{pin}</div><div><h4 {bl}>Location</h4><p {ba}>{addr}</p></div></div>
        <div class="info-card reveal"><div class="ic">{clock}</div><div><h4 {bh}>Working Hours</h4>
          <p {h1}>Monday – Friday: 9:00am – 5:00pm</p><p {h2}>Saturday: 10:00am – 2:00pm</p><p {h3}>Sunday: Closed</p></div></div>
      </div>
    </div>
    <div class="reveal">
      <form class="card" onsubmit="return medadSubmit(event)">
        <h3 style="margin-bottom:18px" {bs}>Send us a message</h3>
        <div class="f-row">
          <div class="field"><label {bn}>Name</label><input required data-en-ph="Your name" data-ar-ph="اسمك" placeholder="Your name"></div>
          <div class="field"><label {bem}>Email</label><input type="email" required data-en-ph="you@email.com" data-ar-ph="بريدك الإلكتروني" placeholder="you@email.com"></div>
        </div>
        <div class="field"><label {bph}>Phone</label><input data-en-ph="+971 ..." data-ar-ph="+971 ..." placeholder="+971 ..."></div>
        <div class="field"><label {bse}>Service</label><select>{opts}</select></div>
        <div class="field"><label {bms}>Message</label><textarea rows="4" required data-en-ph="Tell us about your project…" data-ar-ph="احكِ لنا عن مشروعك…" placeholder="Tell us about your project…"></textarea></div>
        <button class="btn btn-primary" type="submit" style="width:100%;justify-content:center" {bsub}>Send Message</button>
        <p id="form-note" style="display:none;margin-top:12px;color:var(--sky-deep);font-weight:600" {bok}>Thank you! We'll get back to you shortly.</p>
      </form>
    </div>
  </div>
  <div class="map-wrap reveal" style="margin-top:40px;height:380px"><iframe src="{map}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Medad location"></iframe></div>
</div></section>'''.format(
        cards=ic_cards, pin=icon("pin"), clock=icon("clock"),
        bl=bil("Location","الموقع"), ba=bil(COMPANY["addr_en"],COMPANY["addr_ar"]), addr=COMPANY["addr_en"],
        bh=bil("Working Hours","مواعيد العمل"),
        h1=bil("Monday – Friday: 9:00am – 5:00pm","الإثنين – الجمعة: 9:00ص – 5:00م"),
        h2=bil("Saturday: 10:00am – 2:00pm","السبت: 10:00ص – 2:00م"),
        h3=bil("Sunday: Closed","الأحد: مغلق"),
        bs=bil("Send us a message","أرسل لنا رسالة"), bn=bil("Name","الاسم"), bem=bil("Email","البريد الإلكتروني"),
        bph=bil("Phone","الهاتف"), bse=bil("Service","الخدمة"), bms=bil("Message","الرسالة"),
        bsub=bil("Send Message","إرسال الرسالة"), bok=bil("Thank you! We'll get back to you shortly.","شكرًا لك! سنعاود التواصل معك قريبًا."),
        opts="".join('<option {b}>{en}</option>'.format(b=bil(p["en"],p["ar"]), en=p["en"]) for p in PRODUCTS),
        map=COMPANY["map_embed"])
    html += '''<script>function medadSubmit(e){e.preventDefault();var n=document.getElementById('form-note');var f=e.target;
      var lang=(window.MEDAD_getLang&&window.MEDAD_getLang())||'en';
      n.textContent=n.getAttribute('data-'+lang)||n.textContent;n.style.display='block';f.reset();return false;}</script>'''
    html += footer()
    write("contact/index.html", html)

# ---------------- sitemap + robots + manifest ----------------
def build_meta_files():
    urls = [("", "1.0"), ("about-us", "0.8"), ("contact", "0.8"), ("blog", "0.8")]
    for p in PRODUCTS: urls.append((p["slug"], "0.7"))
    for a in ARTICLES: urls.append(("blog/"+a["slug"], "0.6"))
    today = datetime.date.today().isoformat()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
    for slug, pr in urls:
        loc = SITE + "/" + (slug + "/" if slug else "")
        sm += '  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>%s</priority>\n' % (loc, today, pr)
        sm += '    <xhtml:link rel="alternate" hreflang="en" href="%s"/>\n' % loc
        sm += '    <xhtml:link rel="alternate" hreflang="ar" href="%s"/>\n' % loc
        sm += '    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>\n  </url>\n' % loc
    sm += '</urlset>\n'
    write("sitemap.xml", sm)

def main():
    build_home(); build_about(); build_contact(); build_blog_index()
    for i,p in enumerate(PRODUCTS): build_product(p, i)
    for i,a in enumerate(ARTICLES): build_article(a, i)
    build_meta_files()
    n = 4 + len(PRODUCTS) + len(ARTICLES)
    print("Generated %d HTML pages + sitemap." % n)

if __name__ == "__main__":
    main()
