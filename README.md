# Medad Advertising — Website (Static, Bilingual)

A fast, lightweight, fully static redesign of **medadadv.ae** — bilingual (English / العربية), responsive, SEO/GEO/LLM‑optimized, with a built‑in offline chatbot. No backend, no database, no build step required to deploy.

Designed & developed by **Mohamed Reda**.

---

## What's inside

```
medad-website/
├── index.html              ← Home
├── about-us/               ← About
├── contact/                ← Contact (form + map)
├── blog/                   ← Articles index + 6 articles
│   ├── new-dtf-uv-printing-machine/   (the new DTF/UV machine)
│   └── ... 5 more
├── <15 product folders>/   ← acrylic-designs, signages, vehicle-printing-designs, ...
├── assets/
│   ├── css/styles.css      ← design system (logo colors)
│   ├── js/main.js          ← language toggle (AR/EN + RTL), nav, reveal
│   ├── js/chatbot.js       ← offline bilingual assistant
│   └── img/                ← logo.svg, logo-white.svg, favicon.svg, og-image.svg
├── robots.txt              ← search + AI/LLM crawlers (GPTBot, ClaudeBot, PerplexityBot...)
├── sitemap.xml             ← all 25 URLs with hreflang
├── site.webmanifest
├── vercel.json             ← clean URLs + caching + security headers
└── build/                  ← (optional) Python generator. NOT needed to deploy.
```

> **All original URL paths are preserved** (e.g. `/acrylic-designs/`, `/vehicle-printing-designs/`, `/about-us/`, `/contact/`) so no existing links or SEO break.

---

## Option A — Preview on Vercel (drag & drop, fastest)

1. Go to **vercel.com** → log in → **Add New… → Project**.
2. Choose **Deploy** / drag the **`medad-website` folder** onto the page (or use “Browse all templates → Other → upload”).
   - Or install the CLI: `npm i -g vercel`, then run `vercel` **inside this folder** and follow the prompts.
3. Vercel gives you a live `*.vercel.app` link to share with the client. Done — no settings needed (it's plain HTML).

## Option B — Push to GitHub

1. Create a new repo on GitHub (e.g. `medad-website`).
2. Inside this folder:
   ```bash
   git init
   git add .
   git commit -m "Medad website redesign"
   git branch -M main
   git remote add origin https://github.com/<you>/medad-website.git
   git push -u origin main
   ```
3. (Optional) On Vercel: **Add New → Project → Import** the GitHub repo → Deploy.

## Going live on medadadv.ae

In Vercel → Project → **Settings → Domains** → add `medadadv.ae`, then point the domain's DNS to Vercel (Vercel shows the exact A/CNAME record). Since the WordPress slugs are kept identical, the switch won't break links.

---

## Notes
- **Language:** click the **عربي / EN** button in the header. Choice is remembered and the layout flips to RTL with the **Noto Kufi Arabic** font.
- **Chatbot:** bottom‑right bubble. Works offline, answers in the active language about services, the new DTF/UV machine, quotes, hours and location.
- **Replace the logo:** drop your official files over `assets/img/logo.svg` (color) and `assets/img/logo-white.svg` (footer), keeping the same names. A PNG works too — update the `<img src>` if you change the extension.
- **Edit content later:** either edit the HTML directly, or edit `build/data.py` and re‑run `python3 build/build.py` to regenerate every page.
