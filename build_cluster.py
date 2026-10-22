#!/usr/bin/env python3
"""Build the qr.atlasbiznow.com BOFU cluster pages (abn-seo 11-point blueprint)."""
import json, pathlib

SITE = "https://qr.atlasbiznow.com"
UPDATED = "2026-10-22"
UPDATED_HUMAN = "October 22, 2026"

NAV = [
    ("index.html", "QR Code Generator"),
    ("best-free-qr-code-generators.html", "Best Free Generators"),
    ("canva-qr-code-alternatives.html", "Canva Alternatives"),
    ("bitly-qr-code-alternatives.html", "Bitly Alternatives"),
    ("restaurant-qr-code-generator.html", "Restaurant QR"),
    ("wifi-qr-code-generator.html", "WiFi QR"),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="AtlasBizNow">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="ABN Free QR Code Generator">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/og-image.png">
<script async src="https://www.googletagmanager.com/gtag/js?id=GT-KFTLV5WM"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','GT-KFTLV5WM',{{linker:{{domains:['atlasbiznow.com']}}}});</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>tailwind.config={{theme:{{extend:{{colors:{{brand:'#f97316',branddark:'#ea580c',ink:'#111111'}},fontFamily:{{sans:['Inter','ui-sans-serif','system-ui','sans-serif']}}}}}}}}</script>
<script type="application/ld+json">
{schema}
</script>
</head>
<body class="bg-gray-50 text-gray-800 font-sans antialiased">
<header class="bg-white border-b border-gray-100">
  <div class="max-w-5xl mx-auto px-4 py-4 flex items-center justify-between gap-4">
    <a href="index.html" class="flex items-center gap-2 font-extrabold text-ink text-lg">
      <span class="inline-flex w-8 h-8 rounded-lg bg-brand items-center justify-center text-white text-sm">ABN</span>
      <span class="hidden sm:inline">QR Code Generator</span>
    </a>
    <a href="index.html" class="bg-brand hover:bg-branddark text-white font-bold text-sm px-4 py-2 rounded-lg transition">Create a Free QR Code</a>
  </div>
</header>
<main class="max-w-3xl mx-auto px-4 py-10">
{article}
</main>
<footer class="bg-gradient-to-r from-gray-900 via-gray-800 to-gray-900 text-gray-300 mt-16" style="border-top:4px solid #f97316;">
  <div class="max-w-5xl mx-auto px-4 py-10 grid grid-cols-1 md:grid-cols-3 gap-8">
    <div>
      <h4 class="text-white font-semibold mb-3"><a href="https://atlasbiznow.com" class="hover:text-brand">ABN Free QR Code Generator</a></h4>
      <p class="text-sm">Free, permanent QR codes with your logo. No sign-up, no expiry.</p>
    </div>
    <div>
      <h4 class="text-white font-semibold mb-3">Guides</h4>
      <ul class="text-sm space-y-2">
        <li><a href="best-free-qr-code-generators.html" class="hover:text-brand">Best Free QR Code Generators</a></li>
        <li><a href="canva-qr-code-alternatives.html" class="hover:text-brand">Canva QR Code Alternatives</a></li>
        <li><a href="bitly-qr-code-alternatives.html" class="hover:text-brand">Bitly QR Code Alternatives</a></li>
        <li><a href="restaurant-qr-code-generator.html" class="hover:text-brand">Restaurant QR Codes</a></li>
        <li><a href="wifi-qr-code-generator.html" class="hover:text-brand">WiFi QR Codes</a></li>
      </ul>
    </div>
    <div>
      <h4 class="text-white font-semibold mb-3">Tool</h4>
      <ul class="text-sm space-y-2">
        <li><a href="index.html" class="hover:text-brand">QR Code Generator</a></li>
        <li><a href="privacy.html" class="hover:text-brand">Privacy</a></li>
        <li><a href="terms.html" class="hover:text-brand">Terms</a></li>
        <li><a href="https://atlasbiznow.com/atlasbiznow-sales-letter/" class="hover:text-brand">Grow Your Business</a></li>
      </ul>
    </div>
  </div>
  <div class="max-w-5xl mx-auto px-4 pb-8 text-xs text-gray-500">© 2026 AtlasBizNow. ‘QR Code’ is a registered trademark of DENSO WAVE INCORPORATED.</div>
</footer>
</body>
</html>
"""

ARTICLE = """<article>
<p class="text-xs font-semibold uppercase tracking-widest text-branddark mb-3">{kicker}</p>
<h1 class="text-3xl md:text-4xl font-extrabold text-ink leading-tight mb-3">{h1}</h1>
<p class="text-sm text-gray-500 mb-6">By the AtlasBizNow team · Published and last updated <time datetime="{date}">{date_h}</time> · Independent testing of free tiers</p>

<div class="bg-orange-50 border border-orange-200 rounded-xl p-5 mb-8">
  <h2 class="text-lg font-bold text-ink mb-2">Takeaways</h2>
  <ul class="space-y-2 text-sm text-gray-700">
    {takeaways}
  </ul>
</div>

<div class="prose-qr space-y-5 text-gray-700 leading-relaxed">
{body}
</div>

{cta}
</article>"""

CTA = """<div class="mt-10 bg-gradient-to-br from-gray-900 to-[#1a1a1a] text-white rounded-2xl p-6 md:p-8 text-center border-2 border-orange-500/30">
  <h2 class="text-xl md:text-2xl font-extrabold mb-2">Create a free, permanent QR code now</h2>
  <p class="text-gray-300 text-sm mb-5">Custom logo, colors, PNG and SVG — no account, no expiry, no watermark.</p>
  <a href="index.html" class="inline-block bg-brand hover:bg-branddark text-white font-bold px-6 py-3 rounded-lg transition">Open the free QR Code Generator →</a>
</div>"""

PAGES = [
{
 "slug": "best-free-qr-code-generators.html",
 "kicker": "Best Of · 2026",
 "title": "Best Free QR Code Generators in 2026 (Tested & Ranked)",
 "h1": "Best Free QR Code Generators in 2026",
 "desc": "We tested the free tiers of the most popular QR code generators. See what is actually free, what expires, and which generator to use for logos, SVG files and permanent codes.",
 "takeaways": [
   "<strong>Best overall free:</strong> ABN (this site) — no sign-up, custom logo, PNG and SVG, codes never expire.",
   "<strong>Best for advanced design:</strong> QRCode Monkey — genuinely 100% free with SVG, PDF and EPS export.",
   "<strong>Best if you already use Canva:</strong> Canva — free with an account, but tied to Canva's editor.",
   "<strong>Watch out:</strong> Bitly's free plan gives only 2 QR codes per month and shows ads.",
 ],
 "body": """<h2 class="text-2xl font-bold text-ink mt-2">How we tested</h2>
<p>For each generator we used the free tier exactly as a first-time visitor would, then checked six things: <strong>price, whether codes expire, custom logo support, SVG export, whether an account is required, and monthly limits.</strong> Everything below reflects the free tier as published by each provider on {date_h}; pricing changes, so confirm on the provider's site before buying.</p>
<h2 class="text-2xl font-bold text-ink mt-4">Quick comparison</h2>
<div class="overflow-x-auto"><table class="w-full text-left text-sm border-collapse mt-2">
<thead><tr class="border-b border-gray-200"><th class="py-3 pr-3 font-semibold">Generator</th><th class="py-3 px-3 font-semibold">Free tier</th><th class="py-3 px-3 font-semibold">Logo</th><th class="py-3 px-3 font-semibold">SVG</th><th class="py-3 pl-3 font-semibold">Sign-up</th></tr></thead>
<tbody class="text-gray-600">
<tr class="border-b border-gray-100 bg-orange-50"><td class="py-3 pr-3 font-semibold text-gray-900">ABN</td><td class="py-3 px-3">Unlimited, permanent</td><td class="py-3 px-3">Yes</td><td class="py-3 px-3">Yes</td><td class="py-3 pl-3">No</td></tr>
<tr class="border-b border-gray-100"><td class="py-3 pr-3">QRCode Monkey</td><td class="py-3 px-3">Unlimited, permanent</td><td class="py-3 px-3">Yes</td><td class="py-3 px-3">Yes (+PDF/EPS)</td><td class="py-3 pl-3">No</td></tr>
<tr class="border-b border-gray-100"><td class="py-3 pr-3">qr-code-generator.com</td><td class="py-3 px-3">Free static codes</td><td class="py-3 px-3">Paid tiers</td><td class="py-3 px-3">Varies</td><td class="py-3 pl-3">For dynamic</td></tr>
<tr class="border-b border-gray-100"><td class="py-3 pr-3">Canva</td><td class="py-3 px-3">Free with account</td><td class="py-3 px-3">Yes</td><td class="py-3 px-3">Limited</td><td class="py-3 pl-3">Yes</td></tr>
<tr><td class="py-3 pr-3">Bitly</td><td class="py-3 px-3">2 codes / month + ads</td><td class="py-3 px-3">No (free)</td><td class="py-3 px-3">No (free)</td><td class="py-3 pl-3">Yes</td></tr>
</tbody></table></div>
<h2 class="text-2xl font-bold text-ink mt-8">The best free QR code generators, reviewed</h2>
<h3 class="text-lg font-bold text-ink mt-4">1. ABN Free QR Code Generator — best for speed and permanence</h3>
<p class="inline-block text-xs font-semibold bg-orange-100 text-branddark px-2 py-1 rounded mb-2">Best for: small businesses that need one reliable code today</p>
<p>Open the page, pick a type (URL, WiFi, email, SMS, WhatsApp, phone, text or vCard), add a logo and colors, and download PNG or SVG. There is no account and no expiry — the code encodes your content directly, so it keeps working forever. The trade-off: because the codes are static, you cannot change the destination after printing (that is a feature of paid "dynamic" services).</p>
<h3 class="text-lg font-bold text-ink mt-6">2. QRCode Monkey — best for advanced design</h3>
<p class="inline-block text-xs font-semibold bg-gray-100 text-gray-700 px-2 py-1 rounded mb-2">Best for: designers who want maximum styling and vector export</p>
<p>QRCode Monkey is the strongest free alternative. It is genuinely free, requires no account, and exports PNG, SVG, PDF and EPS with custom logos, gradients and shape controls. If you need EPS or heavy design control, use it.</p>
<h3 class="text-lg font-bold text-ink mt-6">3. qr-code-generator.com — best if you need dynamic codes</h3>
<p class="inline-block text-xs font-semibold bg-gray-100 text-gray-700 px-2 py-1 rounded mb-2">Best for: marketers who need to change a link after printing</p>
<p>The free static codes work, but the real product is the paid dynamic system (scan tracking, editable destinations). It runs a 14-day trial and then requires a subscription — only worth it if you specifically need post-print editing and analytics.</p>
<h3 class="text-lg font-bold text-ink mt-6">4. Canva — best if you already design there</h3>
<p class="inline-block text-xs font-semibold bg-gray-100 text-gray-700 px-2 py-1 rounded mb-2">Best for: existing Canva users</p>
<p>Canva's QR app is convenient inside a design, but it requires an account and is tied to the editor. Downloading a clean, print-ready vector file takes extra steps compared with a dedicated generator.</p>
<h3 class="text-lg font-bold text-ink mt-6">5. Bitly — not recommended for free QR codes</h3>
<p>Bitly is a link platform, and its free plan allows just 2 QR codes per month with ads. Paid plans start around $10/month for 5 codes and climb steeply. Use it only if you are already paying for link management.</p>
<h2 class="text-2xl font-bold text-ink mt-8">Frequently asked questions</h2>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">Are free QR codes really permanent?</summary><p class="text-sm text-gray-600 mt-2">Static codes encode the content directly, so they do not expire. Dynamic codes point to a redirect that the provider can switch off if you stop paying — check which type you are creating.</p></details>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">Can I add my logo to a free QR code?</summary><p class="text-sm text-gray-600 mt-2">Yes. ABN and QRCode Monkey both allow logo uploads on the free tier. Keep the logo small and test-scan the result before printing.</p></details>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">Which generator gives an SVG file for free?</summary><p class="text-sm text-gray-600 mt-2">ABN and QRCode Monkey both export SVG at no cost, which is what you want for signs, menus and packaging.</p></details>
<details class="py-3"><summary class="font-semibold cursor-pointer">Do I need to sign up?</summary><p class="text-sm text-gray-600 mt-2">With ABN and QRCode Monkey, no. Canva and Bitly require an account.</p></details>""",
 "faqs": [
   ("Are free QR codes really permanent?", "Static codes encode the content directly, so they do not expire. Dynamic codes point to a redirect that the provider can switch off if you stop paying."),
   ("Can I add my logo to a free QR code?", "Yes. ABN and QRCode Monkey both allow logo uploads on the free tier. Keep the logo small and test-scan before printing."),
   ("Which generator gives an SVG file for free?", "ABN and QRCode Monkey both export SVG at no cost."),
   ("Do I need to sign up?", "With ABN and QRCode Monkey, no. Canva and Bitly require an account."),
 ],
},
{
 "slug": "canva-qr-code-alternatives.html",
 "kicker": "Alternatives · 2026",
 "title": "Best Canva QR Code Alternatives (Free, No Sign-Up) in 2026",
 "h1": "Best Canva QR Code Alternatives in 2026",
 "desc": "Looking for a Canva QR code alternative? Compare free generators that export print-ready PNG and SVG without an account, including options with logo support.",
 "takeaways": [
   "<strong>Best overall:</strong> ABN — free, permanent, logo + SVG, no account.",
   "<strong>Best for vector-heavy design:</strong> QRCode Monkey — free SVG, PDF and EPS.",
   "<strong>Why leave Canva:</strong> Canva needs an account and a workaround to get a clean vector file.",
   "<strong>Already have Canva Pro?</strong> Its QR app is fine — but a dedicated generator is faster for a single code.",
 ],
 "body": """<h2 class="text-2xl font-bold text-ink mt-2">Why look for a Canva alternative?</h2>
<p>Canva's QR app is handy when the code lives inside a poster or flyer you are already designing. But if you just need a QR code — for a menu, a WiFi sign or a business card — Canva adds friction: you need an account, you work inside the editor, and getting a clean, print-ready vector file takes extra steps. A dedicated generator is faster and gives you a file you can hand straight to a printer.</p>
<h2 class="text-2xl font-bold text-ink mt-4">The alternatives, compared</h2>
<div class="overflow-x-auto"><table class="w-full text-left text-sm border-collapse mt-2">
<thead><tr class="border-b border-gray-200"><th class="py-3 pr-3 font-semibold">Tool</th><th class="py-3 px-3 font-semibold">Account needed</th><th class="py-3 px-3 font-semibold">Logo</th><th class="py-3 px-3 font-semibold">Vector export</th><th class="py-3 pl-3 font-semibold">Cost</th></tr></thead>
<tbody class="text-gray-600">
<tr class="border-b border-gray-100 bg-orange-50"><td class="py-3 pr-3 font-semibold text-gray-900">ABN</td><td class="py-3 px-3">No</td><td class="py-3 px-3">Yes</td><td class="py-3 px-3">SVG</td><td class="py-3 pl-3">Free</td></tr>
<tr class="border-b border-gray-100"><td class="py-3 pr-3">QRCode Monkey</td><td class="py-3 px-3">No</td><td class="py-3 px-3">Yes</td><td class="py-3 px-3">SVG / PDF / EPS</td><td class="py-3 pl-3">Free</td></tr>
<tr class="border-b border-gray-100"><td class="py-3 pr-3">qr-code-generator.com</td><td class="py-3 px-3">No (static)</td><td class="py-3 px-3">Paid</td><td class="py-3 px-3">Varies</td><td class="py-3 pl-3">Free static</td></tr>
<tr><td class="py-3 pr-3">Canva</td><td class="py-3 px-3">Yes</td><td class="py-3 px-3">Yes</td><td class="py-3 px-3">Limited</td><td class="py-3 pl-3">Free / Pro</td></tr>
</tbody></table></div>
<h2 class="text-2xl font-bold text-ink mt-8">Our picks</h2>
<h3 class="text-lg font-bold text-ink mt-4">ABN — the fastest no-account option</h3>
<p class="inline-block text-xs font-semibold bg-orange-100 text-branddark px-2 py-1 rounded mb-2">Best for: a single print-ready code in under a minute</p>
<p>Choose the type, enter the content, upload a logo, download PNG or SVG. No login, no watermark, and the code never expires because it is static.</p>
<h3 class="text-lg font-bold text-ink mt-6">QRCode Monkey — the designer's alternative</h3>
<p class="inline-block text-xs font-semibold bg-gray-100 text-gray-700 px-2 py-1 rounded mb-2">Best for: EPS/PDF output and heavy styling</p>
<p>If your print vendor wants EPS, or you want gradients and custom shapes, QRCode Monkey is the strongest free replacement for a Canva workflow.</p>
<h3 class="text-lg font-bold text-ink mt-6">qr-code-generator.com — when you need dynamic codes</h3>
<p>Free static codes are available, but the paid dynamic product (editable links, scan analytics) is a different purchase. Only choose it if post-print editing matters.</p>
<h2 class="text-2xl font-bold text-ink mt-8">Frequently asked questions</h2>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">Is Canva's QR code generator free?</summary><p class="text-sm text-gray-600 mt-2">Yes, with a free Canva account. Some export formats and features require Canva Pro.</p></details>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">Can I get an SVG from Canva?</summary><p class="text-sm text-gray-600 mt-2">Not directly on the free plan for QR codes. A dedicated generator that exports SVG is simpler.</p></details>
<details class="py-3"><summary class="font-semibold cursor-pointer">Which alternative works without signing up?</summary><p class="text-sm text-gray-600 mt-2">ABN and QRCode Monkey both work with no account.</p></details>""",
 "faqs": [
   ("Is Canva's QR code generator free?", "Yes, with a free Canva account. Some export formats and features require Canva Pro."),
   ("Can I get an SVG from Canva?", "Not directly on the free plan for QR codes. A dedicated generator that exports SVG is simpler."),
   ("Which alternative works without signing up?", "ABN and QRCode Monkey both work with no account."),
 ],
},
{
 "slug": "bitly-qr-code-alternatives.html",
 "kicker": "Alternatives · 2026",
 "title": "Best Bitly QR Code Alternatives (Free, No Sign-Up) in 2026",
 "h1": "Best Bitly QR Code Alternatives in 2026",
 "desc": "Bitly's free plan allows only 2 QR codes per month. Compare free alternatives that give unlimited permanent QR codes with logos and SVG export, no subscription.",
 "takeaways": [
   "<strong>Bitly free = 2 QR codes/month</strong> with ads; paid plans start around $10/month.",
   "<strong>Best free replacement:</strong> ABN — unlimited, permanent, logo + SVG, no account.",
   "<strong>Best for design:</strong> QRCode Monkey — free SVG/PDF/EPS.",
   "<strong>Choose Bitly only if</strong> you need link management and scan analytics and will pay for it.",
 ],
 "body": """<h2 class="text-2xl font-bold text-ink mt-2">Why look past Bitly for QR codes?</h2>
<p>Bitly is excellent at link management. Its free plan, however, allows just <strong>2 QR codes per month</strong> with ads, and paid plans start around $10/month for 5 codes — rising steeply for higher volumes. If what you actually need is a handful of permanent, branded QR codes for print, a dedicated free generator is the better fit.</p>
<h2 class="text-2xl font-bold text-ink mt-4">Bitly vs the free alternatives</h2>
<div class="overflow-x-auto"><table class="w-full text-left text-sm border-collapse mt-2">
<thead><tr class="border-b border-gray-200"><th class="py-3 pr-3 font-semibold">Option</th><th class="py-3 px-3 font-semibold">Free QR limit</th><th class="py-3 px-3 font-semibold">Logo on free</th><th class="py-3 px-3 font-semibold">SVG on free</th><th class="py-3 pl-3 font-semibold">Paid from</th></tr></thead>
<tbody class="text-gray-600">
<tr class="border-b border-gray-100"><td class="py-3 pr-3">Bitly</td><td class="py-3 px-3">2 / month (ads)</td><td class="py-3 px-3">No</td><td class="py-3 px-3">No</td><td class="py-3 pl-3">~$10/mo (5 codes)</td></tr>
<tr class="border-b border-gray-100 bg-orange-50"><td class="py-3 pr-3 font-semibold text-gray-900">ABN</td><td class="py-3 px-3">Unlimited</td><td class="py-3 px-3">Yes</td><td class="py-3 px-3">Yes</td><td class="py-3 pl-3">$0</td></tr>
<tr><td class="py-3 pr-3">QRCode Monkey</td><td class="py-3 px-3">Unlimited</td><td class="py-3 px-3">Yes</td><td class="py-3 px-3">Yes</td><td class="py-3 pl-3">$0</td></tr>
</tbody></table></div>
<h2 class="text-2xl font-bold text-ink mt-8">The best Bitly alternatives</h2>
<h3 class="text-lg font-bold text-ink mt-4">ABN — best free replacement</h3>
<p class="inline-block text-xs font-semibold bg-orange-100 text-branddark px-2 py-1 rounded mb-2">Best for: unlimited permanent codes with a logo</p>
<p>Create as many codes as you like, with a logo and colors, and download PNG or SVG. No account, no ads, no expiry. The only thing you give up versus Bitly is dynamic redirects and scan analytics — which matter only for campaigns you need to edit after printing.</p>
<h3 class="text-lg font-bold text-ink mt-6">QRCode Monkey — best for vector design</h3>
<p class="inline-block text-xs font-semibold bg-gray-100 text-gray-700 px-2 py-1 rounded mb-2">Best for: EPS/PDF and advanced styling</p>
<p>Free, no account, and the deepest design options of the free tools, including SVG, PDF and EPS.</p>
<h2 class="text-2xl font-bold text-ink mt-8">When Bitly is still the right call</h2>
<p>If you run campaigns and need to <strong>change a destination after printing</strong>, or you need scan tracking across many codes, a paid dynamic platform is the correct tool. For static print codes, free generators do the job.</p>
<h2 class="text-2xl font-bold text-ink mt-8">Frequently asked questions</h2>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">Does Bitly have a free QR code generator?</summary><p class="text-sm text-gray-600 mt-2">Yes, but the free plan allows only 2 QR codes per month and shows ads.</p></details>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">Can I get unlimited free QR codes elsewhere?</summary><p class="text-sm text-gray-600 mt-2">Yes — ABN and QRCode Monkey both create unlimited static codes at no cost.</p></details>
<details class="py-3"><summary class="font-semibold cursor-pointer">What do I lose by leaving Bitly?</summary><p class="text-sm text-gray-600 mt-2">Dynamic redirects and scan analytics. Static codes cannot be edited after printing.</p></details>""",
 "faqs": [
   ("Does Bitly have a free QR code generator?", "Yes, but the free plan allows only 2 QR codes per month and shows ads."),
   ("Can I get unlimited free QR codes elsewhere?", "Yes — ABN and QRCode Monkey both create unlimited static codes at no cost."),
   ("What do I lose by leaving Bitly?", "Dynamic redirects and scan analytics. Static codes cannot be edited after printing."),
 ],
},
{
 "slug": "restaurant-qr-code-generator.html",
 "kicker": "Use Case · Restaurants",
 "title": "Free Restaurant QR Code Generator — Menu QR Codes That Never Expire",
 "h1": "Free Restaurant QR Code Generator",
 "desc": "Create a free, permanent QR code for your restaurant menu, table tents or window decals. No sign-up, no monthly fee, printable PNG and SVG with your logo.",
 "takeaways": [
   "<strong>Free and permanent:</strong> a static menu QR code costs nothing and never expires.",
   "<strong>Print-ready:</strong> download SVG for signage and table tents, PNG for social and receipts.",
   "<strong>No account:</strong> create and download in under a minute.",
   "<strong>Tip:</strong> put the menu on a stable page you control, and test-scan the code before you print 500 of them.",
 ],
 "body": """<h2 class="text-2xl font-bold text-ink mt-2">Why restaurants use QR menu codes</h2>
<p>A QR code on a table tent, window or receipt lets guests open your menu, order page or reservation form in one scan — no app, no typing. Done right, it replaces reprinting costs: put the menu on a page you control, and update prices there without touching the sign.</p>
<h2 class="text-2xl font-bold text-ink mt-4">Restaurant QR code checklist</h2>
<ul class="list-disc pl-5 space-y-2">
<li><strong>Use a static, permanent code.</strong> It encodes your URL directly, so it keeps working with no subscription.</li>
<li><strong>Link to a mobile-first page.</strong> Your menu should load fast and read well on a phone.</li>
<li><strong>Export SVG for print.</strong> Vector files stay sharp on table tents, window decals and large signage.</li>
<li><strong>Add a short call to action.</strong> “Scan for the menu” beats a naked code.</li>
<li><strong>Test-scan before printing.</strong> Check it on iOS and Android, in low light, at the final printed size.</li>
</ul>
<h2 class="text-2xl font-bold text-ink mt-8">Static vs dynamic menu codes</h2>
<div class="overflow-x-auto"><table class="w-full text-left text-sm border-collapse mt-2">
<thead><tr class="border-b border-gray-200"><th class="py-3 pr-3 font-semibold">Feature</th><th class="py-3 px-3 font-semibold">Static (free)</th><th class="py-3 pl-3 font-semibold">Dynamic (paid)</th></tr></thead>
<tbody class="text-gray-600">
<tr class="border-b border-gray-100"><td class="py-3 pr-3">Cost</td><td class="py-3 px-3">$0</td><td class="py-3 pl-3">Monthly subscription</td></tr>
<tr class="border-b border-gray-100"><td class="py-3 pr-3">Expiry</td><td class="py-3 px-3">Never</td><td class="py-3 pl-3">Stops if you cancel</td></tr>
<tr class="border-b border-gray-100"><td class="py-3 pr-3">Change the link later</td><td class="py-3 px-3">No</td><td class="py-3 pl-3">Yes</td></tr>
<tr><td class="py-3 pr-3">Scan analytics</td><td class="py-3 px-3">No</td><td class="py-3 pl-3">Yes</td></tr>
</tbody></table></div>
<p class="mt-4">For most restaurants a static code is the right choice: your menu page already lives at a stable URL you control, so you rarely need to change the code itself.</p>
<h2 class="text-2xl font-bold text-ink mt-8">Frequently asked questions</h2>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">How much does a restaurant QR code cost?</summary><p class="text-sm text-gray-600 mt-2">A static menu QR code can be created free here — no account and no monthly fee.</p></details>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">Will the code stop working if I change my menu?</summary><p class="text-sm text-gray-600 mt-2">No. The code points to your menu URL; update the page and the same code keeps working.</p></details>
<details class="py-3"><summary class="font-semibold cursor-pointer">What file should I give my printer?</summary><p class="text-sm text-gray-600 mt-2">An SVG file — it scales cleanly to any size. Use PNG for social posts and receipts.</p></details>""",
 "faqs": [
   ("How much does a restaurant QR code cost?", "A static menu QR code can be created free here — no account and no monthly fee."),
   ("Will the code stop working if I change my menu?", "No. The code points to your menu URL; update the page and the same code keeps working."),
   ("What file should I give my printer?", "An SVG file — it scales cleanly to any size. Use PNG for social posts and receipts."),
 ],
},
{
 "slug": "wifi-qr-code-generator.html",
 "kicker": "Use Case · WiFi",
 "title": "Free WiFi QR Code Generator — No Sign-Up, Permanent Code",
 "h1": "Free WiFi QR Code Generator",
 "desc": "Create a free WiFi QR code so guests join your network with one scan. No sign-up, no expiry, printable PNG and SVG. Works with WPA/WPA2, WEP and open networks.",
 "takeaways": [
   "<strong>One scan, no typing:</strong> guests join your WiFi without entering a password.",
   "<strong>Free and permanent:</strong> no account, no subscription, no expiry.",
   "<strong>Print-ready:</strong> SVG for signage, PNG for cards and stickers.",
   "<strong>Security:</strong> a WiFi QR reveals the password to anyone who scans it — treat it like a written password.",
 ],
 "body": """<h2 class="text-2xl font-bold text-ink mt-2">What a WiFi QR code does</h2>
<p>A WiFi QR code stores your network name (SSID), password and security type in a single scannable code. When a guest scans it with their phone camera, the device offers to join the network automatically — no spelling out a password at the counter.</p>
<h2 class="text-2xl font-bold text-ink mt-4">How to make one</h2>
<ol class="list-decimal pl-5 space-y-2">
<li>Open the <a href="index.html" class="text-branddark font-semibold underline">ABN QR code generator</a> and choose the <strong>WiFi</strong> tab.</li>
<li>Enter the network name (SSID), the password, and the encryption type (WPA/WPA2 is standard; choose “open” only for guest networks with no password).</li>
<li>Optionally add your logo and brand colors.</li>
<li>Download SVG for signage or PNG for cards, then test-scan it with a phone before printing.</li>
</ol>
<h2 class="text-2xl font-bold text-ink mt-8">Where to put it</h2>
<ul class="list-disc pl-5 space-y-2">
<li><strong>Cafés and restaurants:</strong> a small table card or a corner of the menu.</li>
<li><strong>Waiting rooms and salons:</strong> a framed sign at reception.</li>
<li><strong>Airbnb and rentals:</strong> inside the welcome book or on the router.</li>
<li><strong>Offices:</strong> a guest-network sign in the lobby.</li>
</ul>
<h2 class="text-2xl font-bold text-ink mt-8">Is a WiFi QR code safe?</h2>
<p>A WiFi QR code contains the password in readable form — anyone who scans it can join. Treat the printed code exactly like a written password: use a separate guest network for customers, and rotate the password if the code is shared publicly and you need to lock it down.</p>
<h2 class="text-2xl font-bold text-ink mt-8">Frequently asked questions</h2>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">Does a WiFi QR code work on iPhone and Android?</summary><p class="text-sm text-gray-600 mt-2">Yes. Modern iPhone and Android cameras recognise WiFi QR codes and offer to join the network.</p></details>
<details class="border-b border-gray-200 py-3"><summary class="font-semibold cursor-pointer">Can I change the WiFi password later?</summary><p class="text-sm text-gray-600 mt-2">The code is static, so a new password means generating a new code. Keep the sign editable or use a small printed insert.</p></details>
<details class="py-3"><summary class="font-semibold cursor-pointer">Is it free?</summary><p class="text-sm text-gray-600 mt-2">Yes — free, no account, and the code never expires.</p></details>""",
 "faqs": [
   ("Does a WiFi QR code work on iPhone and Android?", "Yes. Modern iPhone and Android cameras recognise WiFi QR codes and offer to join the network."),
   ("Can I change the WiFi password later?", "The code is static, so a new password means generating a new code. Keep the sign editable or use a small printed insert."),
   ("Is it free?", "Yes — free, no account, and the code never expires."),
 ],
},
]


def schema_for(p):
    url = f"{SITE}/{p['slug']}"
    graph = [
        {
            "@type": "Article",
            "headline": p["h1"],
            "description": p["desc"],
            "datePublished": UPDATED,
            "dateModified": UPDATED,
            "author": {"@type": "Organization", "name": "AtlasBizNow", "url": "https://atlasbiznow.com"},
            "publisher": {"@type": "Organization", "name": "AtlasBizNow", "url": "https://atlasbiznow.com"},
            "mainEntityOfPage": url,
            "image": f"{SITE}/og-image.png",
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "QR Code Generator", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in p["faqs"]
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2)


def build(p):
    url = f"{SITE}/{p['slug']}"
    takeaways = "\n    ".join(f"<li>{t}</li>" for t in p["takeaways"])
    article = ARTICLE.format(
        kicker=p["kicker"], h1=p["h1"], date=UPDATED, date_h=UPDATED_HUMAN,
        takeaways=takeaways, body=p["body"].replace("{date_h}", UPDATED_HUMAN), cta=CTA,
    )
    return HEAD.format(
        title=p["title"].replace('"', "&quot;"),
        desc=p["desc"].replace('"', "&quot;"),
        url=url, site=SITE, schema=schema_for(p), article=article,
    )


out = pathlib.Path(__file__).parent
for p in PAGES:
    (out / p["slug"]).write_text(build(p), encoding="utf-8")
    print("wrote", p["slug"], len(build(p)), "bytes")
