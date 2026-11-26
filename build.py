#!/usr/bin/env python3
"""Static site generator for 62287.com (OCCUR). Run: python3 build.py  (writes HTML into repo root)."""
import json, os, datetime

SITE = "https://62287.com"
BRAND = "62287.com"
ADS = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
TODAY = datetime.date.today().isoformat()
OUT = os.path.dirname(os.path.abspath(__file__))
SEARCH = []

NAV = [("index.html", "Home"), ("plan.html", "Plan"), ("directory.html", "Vendors"),
       ("events.html", "Ideas & Calendar"), ("guides/index.html", "Guides"),
       ("videos.html", "Videos"), ("support.html", "Support")]


def head(title, desc, path, root, extra=""):
    canon = SITE + "/" + ("" if path == "index.html" else path)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#d9480f">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
{ADS}
{extra}
</head>"""


def header(path, root):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == path else ""
        items.append(f'<li><a href="{root}{href}"{cur}>{label}</a></li>')
    items.append(f'<li><a class="cta" href="{root}get-started.html">Get Free Quotes</a></li>')
    return f"""<body data-root="{root}">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="https://web.works/contact" rel="noopener" target="_blank">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership →</a></div>
<header class="site"><div class="wrap nav">
<a class="brand" href="{root}index.html"><span class="logo">62</span><span>62287 · OCCUR<small>Plan it. Book it. Make it happen.</small></span></a>
<nav aria-label="Main"><ul class="menu">{''.join(items)}</ul></nav>
<div style="display:flex;gap:8px"><button class="icon-btn" id="themeToggle" aria-label="Toggle dark mode">◐</button><button class="icon-btn burger" aria-label="Open menu" aria-expanded="false">☰</button></div>
</div></header>
<main id="main">"""


def footer(root):
    return f"""</main>
<div class="wrap ad-zone"><div class="ad-label">Advertisement</div></div>
<footer class="site"><div class="wrap">
<div class="fgrid">
<div><a class="brand" href="{root}index.html" style="color:#fff"><span class="logo">62</span><span>62287.com</span></a>
<p style="margin-top:14px;font-size:.92rem">OCCUR — 62287 on a phone keypad — is an independent hub for planning, budgeting and booking events: weddings, birthdays, corporate gatherings and fundraisers.</p>
<form data-fs="Newsletter signup" style="display:flex;gap:8px;margin-top:10px"><input type="email" name="email" placeholder="Your email" required aria-label="Email for newsletter"><button class="btn btn-primary btn-sm" type="submit">Join</button></form>
<p style="font-size:.75rem;margin-top:6px">Weekly planning tips &amp; vendor deals. Unsubscribe anytime.</p></div>
<div><h4>Explore</h4><ul><li><a href="{root}plan.html">Planning tools</a></li><li><a href="{root}directory.html">Vendor directory</a></li><li><a href="{root}events.html">Ideas &amp; seasonal calendar</a></li><li><a href="{root}guides/index.html">Guides</a></li><li><a href="{root}videos.html">Video hub</a></li></ul></div>
<div><h4>Get involved</h4><ul><li><a href="{root}get-started.html">Get free vendor quotes</a></li><li><a href="{root}advertise.html">Advertise &amp; sponsor</a></li><li><a href="{root}support.html#donate">Donate</a></li><li><a href="{root}support.html#contests">Contests &amp; prizes</a></li><li><a href="{root}support.html#careers">Careers &amp; talent</a></li><li><a href="{root}directory.html#list">List your business</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="{root}about.html">About</a></li><li><a href="{root}contact.html">Contact</a></li><li><a href="{root}privacy.html">Privacy policy</a></li><li><a href="{root}terms.html">Terms of use</a></li><li><a href="{root}disclosure.html">Trademark &amp; copyright disclosure</a></li><li><a href="https://web.works/contact" target="_blank" rel="noopener">Buy / partner on this domain</a></li></ul></div>
</div>
<div class="legal">© <span class="yr"></span> 62287.com. All rights reserved. Independent publication. Not affiliated with any company, product or organisation that uses the number 62287 or the word “occur”. Cost figures are planning estimates; prices vary by region, season and vendor — always confirm quotes in writing. <a href="{root}disclosure.html">Full disclosure</a>.</div>
</div></footer>
<div class="cookie" role="dialog" aria-label="Cookie notice"><b>Cookies &amp; ads.</b> We use cookies for analytics and to show ads (Google AdSense), which may be personalised. See our <a href="{root}privacy.html">privacy policy</a>.<div style="display:flex;gap:8px;margin-top:10px"><button class="btn btn-primary btn-sm" data-v="all">Accept</button><button class="btn btn-ghost btn-sm" data-v="essential">Essential only</button></div></div>
<div class="sticky-cta"><a href="{root}get-started.html">🎉 Free vendor quotes →</a></div>
<script src="{root}assets/js/main.js" defer></script>
</body></html>"""


def page(path, title, desc, body, keywords="", extra=""):
    root = "../" * path.count("/")
    html = head(title, desc, path, root, extra) + "\n" + header(path, root) + "\n" + body.replace("{R}", root) + "\n" + footer(root)
    fp = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(html)
    if path not in ("thank-you.html", "404.html"):
        SEARCH.append({"u": path, "t": title.split(" | ")[0], "d": desc, "k": keywords})


def pagehead(h1, sub, crumb):
    return f'<section class="pagehead"><div class="wrap"><div class="breadcrumb"><a href="{{R}}index.html">Home</a> / {crumb}</div><h1>{h1}</h1><p class="lead">{sub}</p></div></section>'


AD = '<div class="wrap ad-zone"><div class="ad-label">Advertisement</div></div>'

# ---------- reusable lead wizard ----------
def wizard(fs="Lead — Vendor quotes"):
    opts = [("venue", "🏛️ Venue"), ("catering", "🍽️ Catering & bar"), ("photo", "📸 Photo / video"), ("music", "🎧 DJ / band"),
            ("planner", "📋 Planner / coordinator"), ("decor", "💐 Flowers & décor"), ("rentals", "🪑 Rentals & tents"),
            ("corporate", "🏢 Corporate event"), ("advertise", "📣 Advertise to planners")]
    ch = "".join(f'<label class="choice"><input type="radio" name="need" value="{v}" required>{l}</label>' for v, l in opts)
    return f"""<form class="wizard" data-fs="{fs}" id="match">
<div class="steps"><i></i><i></i><i></i></div>
<div class="step active"><h3>What do you need for your event?</h3><p class="src">Pick one — 60 seconds, free, no obligation.</p><div class="choices">{ch}</div></div>
<div class="step"><h3>Tell us about the event</h3>
<div class="row"><div class="field"><label for="w_type">Event type</label><select id="w_type" name="event_type" required><option value="">Select…</option><option>Wedding</option><option>Engagement / shower</option><option>Birthday / anniversary</option><option>Corporate / conference</option><option>Fundraiser / gala</option><option>Festival / community</option><option>Other</option></select></div>
<div class="field"><label for="w_date">Event date (approx.)</label><input id="w_date" name="event_date" type="date"></div></div>
<div class="row"><div class="field"><label for="w_guests">Guests</label><select id="w_guests" name="guests"><option>Under 25</option><option>25–75</option><option>75–150</option><option>150–300</option><option>300+</option></select></div>
<div class="field"><label for="w_budget">Total budget</label><select id="w_budget" name="budget"><option>Under $2,500</option><option>$2,500–$10K</option><option>$10K–$30K</option><option>$30K–$75K</option><option>$75K+</option></select></div></div>
<div class="field"><label for="w_city">City / region</label><input id="w_city" name="location" required placeholder="e.g. Toronto, ON or Austin, TX"></div>
<div class="field"><label for="w_note">Anything specific? (optional)</label><textarea id="w_note" name="details" rows="3" placeholder="e.g. outdoor ceremony, vegetarian menu, live band"></textarea></div>
<div style="display:flex;gap:10px"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div></div>
<div class="step"><h3>Where should we send your quotes?</h3>
<div class="row"><div class="field"><label for="w_name">Full name</label><input id="w_name" name="name" required autocomplete="name"></div>
<div class="field"><label for="w_email">Email</label><input id="w_email" type="email" name="email" required autocomplete="email"></div></div>
<div class="row"><div class="field"><label for="w_phone">Phone (optional, faster)</label><input id="w_phone" type="tel" name="phone" autocomplete="tel"></div>
<div class="field"><label for="w_contact">Best way to reach you</label><select id="w_contact" name="preferred_contact"><option>Email</option><option>Phone call</option><option>Text</option></select></div></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my event by 62287.com and up to 3 matched vendors. No spam; consent isn't a condition of purchase. See <a href="{{R}}privacy.html">privacy</a>.</label>
<div style="display:flex;gap:10px;margin-top:14px"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="submit" class="btn btn-primary">Get my free quotes ✓</button></div></div>
<div class="trust"><span>🔒 Private &amp; secure</span><span>⚡ Reply within 1 business day</span><span>💸 Free for planners</span></div>
</form>"""


BUDGET = """<div class="tool" id="budget"><h3>💰 Event budget planner</h3>
<div class="row"><div class="field"><label for="b_total">Total budget ($)</label><input id="b_total" type="number" value="25000"></div><div class="field"><label for="b_guests">Guests</label><input id="b_guests" type="number" value="100"></div></div>
<div class="field"><label for="b_type">Event type</label><select id="b_type"><option value="wedding">Wedding</option><option value="corporate">Corporate event</option><option value="birthday">Birthday / private party</option><option value="fundraiser">Fundraiser / gala</option></select></div>
<div class="result" id="b_out"></div></div>"""
CATER = """<div class="tool" id="cater"><h3>🍽️ Catering &amp; bar estimator</h3>
<div class="row"><div class="field"><label for="k_guests">Guests</label><input id="k_guests" type="number" value="100"></div><div class="field"><label for="k_hours">Bar hours</label><input id="k_hours" type="number" value="4"></div></div>
<div class="row"><div class="field"><label for="k_food">Food $/guest</label><input id="k_food" type="number" value="55"></div><div class="field"><label for="k_drink">Bar $/guest</label><input id="k_drink" type="number" value="25"></div></div>
<div class="field"><label for="k_svc">Service charge + gratuity (%)</label><input id="k_svc" type="number" value="22"></div>
<div class="result" id="k_out"></div></div>"""
SEAT = """<div class="tool" id="seat"><h3>🪑 Seating &amp; space</h3>
<div class="row"><div class="field"><label for="s_guests">Guests</label><input id="s_guests" type="number" value="120"></div><div class="field"><label for="s_per">Seats per table</label><input id="s_per" type="number" value="8"></div></div>
<div class="field"><label for="s_style">Layout</label><select id="s_style"><option value="12">Banquet, round tables (~12 sq ft/guest)</option><option value="8">Cocktail, standing (~8 sq ft/guest)</option><option value="10">Theatre / ceremony rows (~10 sq ft/guest)</option><option value="15">Classroom / conference (~15 sq ft/guest)</option></select></div>
<div class="result" id="s_out"></div></div>"""
COUNT = """<div class="tool" id="countdown"><h3>⏳ Countdown &amp; planning checklist</h3>
<div class="field"><label for="t_date">Event date</label><input id="t_date" type="date"></div>
<div class="result" id="t_out"></div></div>"""

# ======================= HOME =======================
home = f"""
<section class="hero"><div class="wrap grid">
<div><span class="eyebrow">6-2-2-8-7 = O-C-C-U-R</span>
<h1>Make your event <span style="color:var(--bud)">occur</span> — on budget and on time.</h1>
<p class="lead">Free planning tools, honest budgets and vetted vendor quotes for weddings, birthdays, corporate events and fundraisers. Dial 62287 on any phone keypad and it spells OCCUR — that's what we help you do.</p>
<div class="actions"><a class="btn btn-primary" href="{{R}}get-started.html">Get free vendor quotes →</a><a class="btn btn-ghost" href="{{R}}plan.html">Open the planning tools</a></div>
<div class="searchbox" style="max-width:520px;margin-top:22px"><input id="siteSearch" type="search" placeholder="Search guides, tools, vendors… (try “budget”, “venue”, “wedding”)" aria-label="Search site"><div class="sresults" id="sResults"></div></div>
</div>
<div class="zipcard reveal"><div class="src">On your keypad</div><div class="zip">62287</div><div style="font-weight:700">O · C · C · U · R</div>
<div class="statgrid">
<div class="stat"><b>4</b><span>free planning calculators</span></div>
<div class="stat"><b>12</b><span>vendor categories</span></div>
<div class="stat"><b>3</b><span>matched quotes per request</span></div>
<div class="stat"><b>$0</b><span>cost to planners</span></div>
</div><p class="src" style="margin-top:10px">Every tool runs privately in your browser. <a href="{{R}}about.html">How we work</a></p></div>
</div></section>
{AD}
<section><div class="wrap">
<div class="sec-head reveal"><span class="eyebrow">Everything in one place</span><h2>From “someday” to “it's happening”</h2><p>Built for people planning an event — and the vendors who make events happen.</p></div>
<div class="cards">
<div class="card reveal"><div class="ic">🧮</div><h3>Planning tools</h3><p>Budget split, catering &amp; bar, seating &amp; space, and a countdown checklist that tells you what to book this week.</p><a class="more" href="{{R}}plan.html">Plan now →</a></div>
<div class="card reveal"><div class="ic">📇</div><h3>Vendor directory</h3><p>Venues, caterers, photographers, DJs, florists, rentals, planners and more — plus free listings for vendors.</p><a class="more" href="{{R}}directory.html">Find vendors →</a></div>
<div class="card reveal"><div class="ic">📨</div><h3>Free quotes</h3><p>One request, up to three matched vendors, reply within one business day. You compare and choose.</p><a class="more" href="{{R}}get-started.html">Get quotes →</a></div>
<div class="card reveal"><div class="ic">💡</div><h3>Ideas &amp; calendar</h3><p>Theme ideas by event type and a month-by-month calendar of what to plan and when to book.</p><a class="more" href="{{R}}events.html">Get inspired →</a></div>
<div class="card reveal"><div class="ic">📚</div><h3>Guides</h3><p>Long-form, numbers-first guides on budgets, venues, corporate events and fundraisers.</p><a class="more" href="{{R}}guides/index.html">Read →</a></div>
<div class="card reveal"><div class="ic">▶️</div><h3>Video hub</h3><p>Curated videos on planning timelines, décor, catering and running the day itself.</p><a class="more" href="{{R}}videos.html">Watch →</a></div>
</div></div></section>

<section class="alt" id="get-matched"><div class="wrap two">
<div class="reveal"><span class="eyebrow">Free vendor matching</span><h2>Tell us about your event. We'll find the vendors.</h2>
<p>One short form routes your request to up to three vendors who fit your date, guest count, budget and location. No bidding wars, no inbox flood.</p>
<ul class="prose"><li><b>Couples:</b> venues, photographers, caterers, florists and music.</li><li><b>Companies:</b> conference venues, AV, catering and team-building.</li><li><b>Non-profits:</b> gala venues, auction support and sponsorship-ready packages.</li></ul>
<p class="src">Vendors may pay us a referral fee. That never costs you anything and never changes who we recommend.</p></div>
<div class="reveal">{wizard()}</div>
</div></section>
{AD}
<section><div class="wrap two">
<div class="reveal">{COUNT}</div>
<div class="reveal"><div class="tool" id="fitquiz"><h3>🎯 What's your event style?</h3>
<div class="field"><label>Guest list</label><select><option value="">Select…</option><option value="3">150+ people</option><option value="2">50–150</option><option value="1">Under 50</option></select></div>
<div class="field"><label>Atmosphere</label><select><option value="">Select…</option><option value="3">Black-tie, wow factor</option><option value="2">Stylish but relaxed</option><option value="1">Cosy and personal</option></select></div>
<div class="field"><label>Time until the event</label><select><option value="">Select…</option><option value="3">10+ months</option><option value="2">3–9 months</option><option value="1">Under 3 months</option></select></div>
<div class="field"><label>Who's doing the work?</label><select><option value="">Select…</option><option value="3">Hire a full planner</option><option value="2">Day-of coordinator</option><option value="1">DIY with help</option></select></div>
<div class="result" id="fit_out">Answer all 4 questions to see your event style.</div></div></div>
</div></section>

<section class="alt"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Latest guides</span><h2>Read before you book</h2></div>
<div class="cards" id="guidecards"></div></div></section>

<section><div class="wrap">
<div class="sec-head"><span class="eyebrow">FAQ</span><h2>Quick answers</h2></div>
<details><summary>Why is the site called 62287 / OCCUR?</summary><p>On a standard phone keypad, 6-2-2-8-7 spells O-C-C-U-R. We help events occur — planned well, booked on time and kept on budget.</p></details>
<details><summary>Is the quote service really free?</summary><p>Yes. Vendors may pay a referral fee; you pay nothing and are never obligated to book.</p></details>
<details><summary>How far ahead should I book vendors?</summary><p>For large weddings and galas, book the venue 10–12 months out and photographers, caterers and bands 8–10 months out. Small parties can come together in 6–10 weeks. Use the countdown checklist for exact dates.</p></details>
<details><summary>How much of my budget should go to the venue and food?</summary><p>For most weddings and galas, venue plus catering and bar typically takes 50–60% of the total. Our budget planner shows a full split by event type.</p></details>
<details><summary>I'm a vendor. How do I get listed?</summary><p>Basic listings are free — see the <a href="{{R}}directory.html#list">vendor directory</a>. Featured listings and lead partnerships are on the <a href="{{R}}advertise.html">advertise page</a>.</p></details>
</div></section>
"""
faq_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "WebSite", "name": BRAND, "alternateName": "OCCUR", "url": SITE},
    {"@type": "Organization", "name": BRAND, "url": SITE, "logo": SITE + "/assets/img/favicon.svg"},
    {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "Why is the site called 62287 / OCCUR?", "acceptedAnswer": {"@type": "Answer", "text": "On a phone keypad, 6-2-2-8-7 spells O-C-C-U-R."}},
        {"@type": "Question", "name": "How far ahead should I book vendors?", "acceptedAnswer": {"@type": "Answer", "text": "For large weddings and galas, book the venue 10–12 months out; small parties can come together in 6–10 weeks."}}]}]}) + "</script>"

# ======================= PLAN =======================
plan = pagehead("Free event planning tools", "Budget, catering, seating and timeline — run the numbers before you sign a single contract.", "Plan") + f"""
<section><div class="wrap two">{BUDGET}{CATER}</div>
<div class="wrap two" style="margin-top:28px">{SEAT}{COUNT}</div></section>
{AD}
<section class="alt"><div class="wrap two">
<div class="prose"><h2>How to use these numbers</h2>
<ol><li><b>Start with the guest count.</b> It drives catering, space, rentals and staffing — cutting 20 guests saves more than any single negotiation.</li>
<li><b>Fix the budget, then split it.</b> Decide your total first, then allocate. Re-run the split if one category goes over.</li>
<li><b>Price per guest is your reality check.</b> If your per-guest number can't cover food and drink in your city, change the format (brunch, cocktail, weekday) before you change vendors.</li>
<li><b>Book in order of scarcity.</b> Venue first, then the vendors who only work one event a day (photographer, band, planner).</li>
<li><b>Keep 5–10% contingency.</b> Overtime, weather plans and last-minute guests always appear.</li></ol></div>
<div><p class="warn">Figures are planning estimates. Real prices vary widely by city, season, day of week and vendor. Always get itemised quotes in writing.</p>
<a class="btn btn-primary" href="{{R}}get-started.html">Turn these numbers into real quotes →</a></div>
</div></section>
"""
page("plan.html", "Free Event Planning Tools — Budget, Catering, Seating & Checklist | 62287.com",
     "Free event planning calculators: budget split by event type, catering and bar estimator, seating and space planner, and a countdown checklist with booking dates.", plan, "plan budget calculator catering bar seating tables checklist timeline countdown")

# ======================= DIRECTORY =======================
cats = [("venue", "Venues", ["Banquet & event halls", "Hotels & resorts", "Barns, farms & estates", "Restaurants & private dining", "Rooftops, lofts & galleries"]),
        ("food", "Food & drink", ["Full-service caterers", "Food trucks", "Mobile bars & bartenders", "Cakes & desserts", "Coffee & late-night snacks"]),
        ("media", "Photo, video & music", ["Photographers", "Videographers & drone", "DJs & MCs", "Live bands & musicians", "Photo booths"]),
        ("style", "Décor & style", ["Florists", "Lighting & draping", "Balloon artists", "Hair & makeup", "Attire & tailoring"]),
        ("ops", "Planning & logistics", ["Full-service planners", "Day-of coordinators", "Tent, table & chair rentals", "AV & staging", "Transportation & shuttles"]),
        ("fun", "Entertainment & extras", ["Officiants", "Kids' entertainers", "Games & team-building", "Stationery & invitations", "Favours & gifts"])]
cards = "".join(f'<div class="card" data-cat="{c}"><h3>{n}</h3><ul class="prose" style="font-size:.95rem">' + "".join(f"<li>{x}</li>" for x in items) +
                f'</ul><a class="more" href="{{R}}get-started.html">Request quotes →</a></div>' for c, n, items in cats)
chips = '<button class="chip on" data-cat="all">All</button>' + "".join(f'<button class="chip" data-cat="{c}">{n}</button>' for c, n, _ in cats)
directory = pagehead("Event vendor directory", "Find the people who make events happen — or list your business free.", "Vendors") + f"""
<section><div class="wrap">
<div class="filters" data-target="#dirgrid">{chips}</div>
<div class="cards" id="dirgrid">{cards}</div>
<p class="note" style="margin-top:20px">Vendor listings are being added and verified category by category. Need someone now? <a href="{{R}}get-started.html">Request up to 3 quotes</a> and we'll match you directly.</p>
</div></section>
{AD}
<section class="alt" id="list"><div class="wrap two">
<div class="prose"><h2>Vendors: list your business — free</h2><p>Planners search here when they're ready to book. A basic listing is free. Featured listings add photos, a priority position and lead routing from our quote form.</p>
<table><tr><th>Plan</th><th>Includes</th><th>Price</th></tr><tr><td>Basic</td><td>Name, category, service area, website</td><td>Free</td></tr><tr><td>Featured</td><td>Top placement, logo, gallery, lead routing</td><td>From $29/mo</td></tr><tr><td>Category sponsor</td><td>Exclusive category banner + Featured perks</td><td>From $99/mo</td></tr></table></div>
<form class="tool" data-fs="Vendor listing request"><h3>📇 Add / claim a listing</h3>
<div class="field"><label for="l_biz">Business name</label><input id="l_biz" name="business" required></div>
<div class="row"><div class="field"><label for="l_cat">Category</label><select id="l_cat" name="category">{''.join(f'<option>{n}</option>' for _, n, _ in cats)}</select></div><div class="field"><label for="l_plan">Plan</label><select id="l_plan" name="plan"><option>Basic (free)</option><option>Featured</option><option>Category sponsor</option></select></div></div>
<div class="row"><div class="field"><label for="l_area">Service area</label><input id="l_area" name="service_area" placeholder="City / region" required></div><div class="field"><label for="l_web">Website</label><input id="l_web" name="website" type="url" placeholder="https://"></div></div>
<div class="row"><div class="field"><label for="l_name">Your name</label><input id="l_name" name="name" required></div><div class="field"><label for="l_email">Email</label><input id="l_email" name="email" type="email" required></div></div>
<button class="btn btn-primary" type="submit">Submit listing →</button></form>
</div></section>
"""
page("directory.html", "Event Vendor Directory — Venues, Caterers, Photographers, DJs & More | 62287.com",
     "Browse event vendors by category — venues, catering, photo and video, music, décor, planners and rentals — or list your event business free.", directory, "vendors directory venue caterer photographer dj florist rentals planner listing")

# ======================= EVENTS (ideas & calendar) =======================
events = pagehead("Event ideas &amp; seasonal calendar", "What to plan, when to book, and ideas that make an event memorable.", "Ideas &amp; Calendar") + f"""
<section><div class="wrap two">
<div><h2>A year of events</h2><div class="timeline">
<div class="ev"><div class="month">January–February</div><h3>Engagement season &amp; Valentine's</h3><p>Peak time to tour venues for next year. Valentine's dinners and galentine's parties book restaurants early.</p></div>
<div class="ev"><div class="month">March–April</div><h3>Spring showers &amp; fundraisers</h3><p>Baby and bridal showers, spring galas and Easter brunches. Garden venues open their calendars.</p></div>
<div class="ev"><div class="month">May–June</div><h3>Graduations &amp; peak weddings</h3><p>The busiest stretch for photographers and caterers — book 9–12 months ahead for Saturdays.</p></div>
<div class="ev"><div class="month">July–August</div><h3>Reunions, festivals &amp; backyard parties</h3><p>Outdoor events need a weather plan: tents, fans, shade and a rain date.</p></div>
<div class="ev"><div class="month">September–October</div><h3>Fall weddings &amp; corporate offsites</h3><p>Golden light, cooler temperatures and strong demand. Halloween parties fill October weekends.</p></div>
<div class="ev"><div class="month">November–December</div><h3>Holiday parties</h3><p>Company holiday parties book venues 3–6 months out; Fridays in December go first.</p></div>
</div></div>
<div><h2>Ideas by event type</h2>
<details open><summary>💍 Weddings</summary><ul class="prose"><li>Weekday or Sunday dates can cut venue costs significantly.</li><li>Late-night food station instead of a second dessert.</li><li>Shared playlist from guests' RSVP song requests.</li></ul></details>
<details><summary>🎂 Birthdays &amp; milestones</summary><ul class="prose"><li>Decade-themed party for 30th, 40th, 50th birthdays.</li><li>Private chef's table for under 20 guests.</li><li>Memory wall with guests' photos and notes.</li></ul></details>
<details><summary>🏢 Corporate</summary><ul class="prose"><li>Swap one keynote for a hands-on workshop.</li><li>Volunteering half-day as team-building.</li><li>Branded photo booth that doubles as social content.</li></ul></details>
<details><summary>🎗️ Fundraisers</summary><ul class="prose"><li>Paddle raise for a single, concrete goal.</li><li>Experience-based auction items over physical goods.</li><li>Live donation tracker on screen.</li></ul></details>
<form class="tool" data-fs="Event idea / event submission" style="margin-top:20px"><h3>📅 Share your event or idea</h3><p class="src">Hosting a public event or have an idea worth featuring? Send it in.</p>
<div class="field"><label for="e_t">Event or idea</label><input id="e_t" name="event" required></div>
<div class="row"><div class="field"><label for="e_d">Date (if any)</label><input id="e_d" name="date" type="date"></div><div class="field"><label for="e_l">Location</label><input id="e_l" name="location"></div></div>
<div class="field"><label for="e_desc">Description</label><textarea id="e_desc" name="description" rows="3"></textarea></div>
<div class="row"><div class="field"><label for="e_n">Your name</label><input id="e_n" name="name" required></div><div class="field"><label for="e_e">Email</label><input id="e_e" name="email" type="email" required></div></div>
<label class="check"><input type="checkbox" name="promote" value="yes"> I'm interested in a paid promoted placement.</label>
<button class="btn btn-primary" type="submit" style="margin-top:10px">Submit →</button></form></div>
</div></section>
"""
page("events.html", "Event Ideas & Seasonal Planning Calendar | 62287.com",
     "Month-by-month event calendar and ideas for weddings, birthdays, corporate events and fundraisers — plus when to book each vendor.", events, "ideas calendar seasonal wedding birthday corporate fundraiser holiday party")

# ======================= VIDEOS =======================
topics = [("Wedding planning timeline", "wedding planning timeline checklist"), ("How to set an event budget", "how to make an event budget"),
          ("Choosing the right venue", "how to choose an event venue"), ("Catering: what to ask", "questions to ask a caterer"),
          ("DIY event décor on a budget", "diy event decor on a budget"), ("Running a corporate event", "how to plan a corporate event"),
          ("Hosting a charity gala", "how to plan a fundraising gala"), ("Day-of coordination tips", "day of coordinator tips")]
vc = "".join(f'<div class="vcard"><a class="vthumb" style="text-decoration:none" href="https://www.youtube.com/results?search_query={q.replace(" ", "+")}" target="_blank" rel="noopener">▶</a><div class="vb"><h3>{t}</h3><p class="src">Opens a curated YouTube search in a new tab.</p></div></div>' for t, q in topics)
videos = pagehead("Video hub", "Short, practical videos on planning, budgeting, décor and running the day.", "Videos") + f"""
<section><div class="wrap"><div class="vgrid" id="vlist">{vc}</div>
<div class="note" style="margin-top:24px">Create event-planning videos? <a href="{{R}}contact.html">Send them to us</a> — featured creators get a backlink and a newsletter shout-out.</div></div></section>
"""
page("videos.html", "Event Planning Video Hub | 62287.com", "Curated videos on wedding timelines, event budgets, venues, catering, décor, corporate events and fundraising galas.", videos, "videos youtube watch")

# ======================= GET STARTED =======================
gs = pagehead("Get free quotes from event vendors", "Venues, catering, photography, music, planners, décor and rentals. One form, one business day.", "Get Quotes") + f"""
<section><div class="wrap two">
<div>{wizard()}</div>
<div class="prose">
<h2>How it works</h2>
<ol><li><b>Tell us about your event</b> — 3 quick steps, about 60 seconds.</li><li><b>We review it personally</b> — no auto-blast to dozens of vendors.</li><li><b>You get up to 3 matches</b> — available on your date and within your budget.</li><li><b>You decide</b> — compare, ask questions, book or walk away.</li></ol>
<h2>What to have ready</h2>
<table><tr><th>Detail</th><th>Why vendors ask</th></tr>
<tr><td>Date (or date range)</td><td>Availability is the first filter</td></tr>
<tr><td>Guest count</td><td>Drives food, space and staffing</td></tr>
<tr><td>Budget range</td><td>Lets vendors propose the right package</td></tr>
<tr><td>Location</td><td>Travel fees and local availability</td></tr>
<tr><td>Style / must-haves</td><td>Shows whether they're the right fit</td></tr></table>
<div class="note">Are you a vendor who wants these leads? <a href="{{R}}advertise.html#partner">Become a partner</a>.</div>
</div></div></section>
"""
page("get-started.html", "Get Free Event Vendor Quotes — Venues, Catering, Photo, DJ & More | 62287.com",
     "Free quote matching for weddings, parties, corporate events and fundraisers: up to 3 vetted vendors that fit your date, guest count and budget.", gs, "quote quotes lead vendor venue catering photographer dj planner")

# ======================= ADVERTISE =======================
adv = pagehead("Advertise, sponsor &amp; partner", "Reach people actively planning weddings, parties, corporate events and fundraisers.", "Advertise") + f"""
<section><div class="wrap">
<div class="tiers">
<div class="tier"><div class="src">Vendor</div><div class="amt">$29</div><p>/month · Featured listing, gallery, lead routing</p></div>
<div class="tier"><div class="src">Category sponsor</div><div class="amt">$99</div><p>/month · Exclusive banner on one vendor category</p></div>
<div class="tier"><div class="src">Tool sponsor</div><div class="amt">$199</div><p>/month · “Presented by” on a planning calculator</p></div>
<div class="tier"><div class="src">Partner</div><div class="amt">Custom</div><p>Sitewide sponsorship, lead partnerships, contest prizes</p></div>
</div></div></section>
<section class="alt" id="partner"><div class="wrap two">
<div class="prose"><h2>Lead partnerships</h2><p>Venues, caterers, photographers, planners and rental companies can receive exclusive or shared leads from our quote form — pay per qualified lead or a flat monthly fee per category and region.</p>
<h2>Domain &amp; site partnership</h2><p>Interested in acquiring 62287.com, a revenue share or a white-label partnership? Use the <a href="https://web.works/contact" target="_blank" rel="noopener">partnership contact page</a>.</p></div>
<form class="tool" data-fs="Advertising / sponsorship inquiry"><h3>📣 Advertising inquiry</h3>
<div class="row"><div class="field"><label for="ad_co">Business</label><input id="ad_co" name="business" required></div><div class="field"><label for="ad_pkg">Interested in</label><select id="ad_pkg" name="package"><option>Featured listing</option><option>Category sponsor</option><option>Tool sponsor</option><option>Lead partnership</option><option>Contest prize sponsor</option><option>Sitewide / custom</option></select></div></div>
<div class="field"><label for="ad_budget">Monthly budget</label><select id="ad_budget" name="budget"><option>Under $100</option><option>$100–$500</option><option>$500–$2,000</option><option>$2,000+</option></select></div>
<div class="row"><div class="field"><label for="ad_n">Name</label><input id="ad_n" name="name" required></div><div class="field"><label for="ad_e">Email</label><input id="ad_e" name="email" type="email" required></div></div>
<div class="field"><label for="ad_m">Goals</label><textarea id="ad_m" name="message" rows="3"></textarea></div>
<button class="btn btn-primary" type="submit">Send inquiry →</button></form>
</div></section>
"""
page("advertise.html", "Advertise & Sponsor on 62287.com — Reach Event Planners", "Featured vendor listings, category and tool sponsorships, lead partnerships and custom packages to reach people planning events.", adv, "advertise sponsor partner leads vendors")

# ======================= SUPPORT =======================
support = pagehead("Support 62287.com", "Keep free planning tools free: donate, sponsor a prize, enter a contest or join the team.", "Support") + f"""
<section id="donate"><div class="wrap two">
<div><h2>💛 Donate</h2><p>Donations fund hosting, new planning tools, original guides, promotion, contest prizes and hiring contributors.</p>
<div class="progress" aria-label="Funding progress"><i style="width:12%"></i></div><p class="src">2026–27 operations goal — every bit helps.</p>
<div class="tiers" style="margin-top:16px">
<div class="tier" data-amt="10"><div class="amt">$10</div><p>Supporter</p></div><div class="tier" data-amt="25"><div class="amt">$25</div><p>Party starter</p></div><div class="tier" data-amt="100"><div class="amt">$100</div><p>Host</p></div><div class="tier" data-amt="500"><div class="amt">$500</div><p>Founding patron</p></div></div>
<table style="margin-top:18px"><tr><th>Where it goes</th><th>Share</th></tr><tr><td>Operations &amp; hosting</td><td>35%</td></tr><tr><td>New tools &amp; content</td><td>30%</td></tr><tr><td>Promotion &amp; marketing</td><td>20%</td></tr><tr><td>Contests &amp; prizes</td><td>15%</td></tr></table></div>
<form class="tool" data-fs="Donation pledge"><h3>Pledge your support</h3><p class="src">Submit a pledge and we'll reply with a secure payment link. 62287.com is not a charity; donations are not tax-deductible.</p>
<div class="row"><div class="field"><label for="d_amount">Amount ($)</label><input id="d_amount" name="amount" type="number" min="1" value="25" required></div><div class="field"><label for="d_freq">Frequency</label><select id="d_freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div class="field"><label for="d_use">Direct my gift to</label><select id="d_use" name="designation"><option>Where needed most</option><option>Ongoing operations</option><option>Promotions &amp; marketing</option><option>Hiring talent</option><option>Contests &amp; prizes</option></select></div>
<div class="row"><div class="field"><label for="d_n">Name</label><input id="d_n" name="name" required></div><div class="field"><label for="d_e">Email</label><input id="d_e" name="email" type="email" required></div></div>
<label class="check"><input type="checkbox" name="public_thanks" value="yes"> Thank me publicly on the supporters wall.</label>
<button class="btn btn-primary" type="submit" style="margin-top:12px">Send pledge →</button></form>
</div></section>
{AD}
<section class="alt" id="contests"><div class="wrap two">
<div class="prose"><h2>🏆 Contests &amp; prizes</h2>
<h3>Best Event Photo of the Season</h3><p>Share your best shot from a wedding, party or event you hosted or attended (with the subjects' permission). Winners are featured sitewide and receive sponsor-funded prizes; current prize details are posted here once each season's sponsors confirm.</p>
<h3>Dream Event on a Budget</h3><p>Describe how you'd throw a memorable event for 50 guests on $2,500 — in 300 words. The most creative, realistic plan wins a featured article and a sponsor prize.</p>
<h3>Official rules (summary)</h3><ul><li>No purchase necessary. Void where prohibited.</li><li>Open to legal residents of the U.S. and Canada aged 18+ (Québec residents excluded where required by law). One entry per person per contest.</li><li>Entries must be your own work; you keep copyright and grant us a licence to display your entry. Photos must have the subjects' consent.</li><li>Winners chosen by a judging panel on originality, quality and relevance; Canadian winners must answer a skill-testing question.</li><li>Winners notified by email within 14 days of close. Prizes are non-transferable; sponsors listed with each contest.</li></ul>
<p>Want to fund a prize? <a href="{{R}}advertise.html">Become a contest sponsor</a>.</p></div>
<form class="tool" data-fs="Contest entry"><h3>Enter a contest</h3>
<div class="field"><label for="ct_c">Contest</label><select id="ct_c" name="contest"><option>Best Event Photo of the Season</option><option>Dream Event on a Budget</option></select></div>
<div class="field"><label for="ct_link">Link to your photo / plan (Drive, Dropbox, etc.)</label><input id="ct_link" name="entry_link" type="url" placeholder="https://" required></div>
<div class="field"><label for="ct_desc">Title / short description</label><textarea id="ct_desc" name="description" rows="3"></textarea></div>
<div class="row"><div class="field"><label for="ct_n">Name</label><input id="ct_n" name="name" required></div><div class="field"><label for="ct_e">Email</label><input id="ct_e" name="email" type="email" required></div></div>
<label class="check"><input type="checkbox" name="rules" value="accepted" required> I'm 18+, eligible, and I accept the official rules.</label>
<button class="btn btn-primary" type="submit" style="margin-top:12px">Submit entry →</button></form>
</div></section>
<section id="careers"><div class="wrap two">
<div class="prose"><h2>💼 Careers &amp; talent</h2><p>Mostly remote and freelance to start.</p>
<table><tr><th>Role</th><th>Type</th></tr><tr><td>Event-planning writer</td><td>Freelance, per article</td></tr><tr><td>Event photographer / videographer contributor</td><td>Freelance, per feature</td></tr><tr><td>Vendor partnerships rep</td><td>Commission</td></tr><tr><td>Web &amp; SEO contributor</td><td>Remote, project-based</td></tr><tr><td>Community ambassador</td><td>Volunteer / stipend</td></tr></table></div>
<form class="tool" data-fs="Careers application"><h3>Apply or join the talent pool</h3>
<div class="field"><label for="j_role">Role</label><select id="j_role" name="role"><option>Event-planning writer</option><option>Photographer / videographer</option><option>Vendor partnerships rep</option><option>Web &amp; SEO contributor</option><option>Community ambassador</option><option>Other</option></select></div>
<div class="field"><label for="j_link">Portfolio / LinkedIn / résumé link</label><input id="j_link" name="portfolio" type="url" placeholder="https://"></div>
<div class="field"><label for="j_why">Why you?</label><textarea id="j_why" name="message" rows="3"></textarea></div>
<div class="row"><div class="field"><label for="j_n">Name</label><input id="j_n" name="name" required></div><div class="field"><label for="j_e">Email</label><input id="j_e" name="email" type="email" required></div></div>
<button class="btn btn-primary" type="submit">Apply →</button></form>
</div></section>
"""
page("support.html", "Support 62287.com — Donate, Contests & Prizes, Careers", "Support free event-planning tools: donate, enter photo and budget-event contests, sponsor prizes, or join our team.", support, "donate support contest prize careers jobs hiring volunteer")

# ======================= GUIDES =======================
guides = [
 ("event-budget-guide", "How to Build an Event Budget That Actually Holds", "Budget",
  "A step-by-step method for setting, splitting and protecting an event budget — weddings, parties and corporate events.",
  """<p>Most event budgets fail the same way: someone picks a venue first, falls in love with it, and every other decision gets squeezed. Flip the order and your budget holds.</p>
<h2>1. Set the total before you shop</h2><p>Decide what you can spend without debt or regret. Write it down. Every quote from now on is measured against that number, not against what other people spent.</p>
<h2>2. Fix the guest count range</h2><p>Guest count is the biggest cost lever. Food, drink, rentals, space and staff all scale per head. A list of 120 vs 90 guests can move a budget by a quarter.</p>
<h2>3. Split by category</h2><p>A common wedding split puts roughly 28% toward the venue and rentals, 30% toward catering and bar, about 11% to photo and video, and the remainder across music, flowers, attire, stationery, coordination and a contingency. Corporate events weight venue and AV more heavily. Our <a href="../plan.html">budget planner</a> shows the split for each event type.</p>
<h2>4. Calculate per-guest cost</h2><p>Divide the total by guests. If the result can't cover food and drink in your city, change the format — a brunch, a cocktail reception or a weekday date — before you start cutting quality everywhere.</p>
<h2>5. Get itemised quotes</h2><p>Ask every vendor for line items: service charges, gratuities, overtime rates, travel fees, cake-cutting and corkage. Hidden fees routinely add 20–25% to food and beverage totals.</p>
<h2>6. Keep a contingency</h2><p>Hold 5–10% back. Weather plans, extra guests and overtime will claim it.</p>
<h2>7. Track as you book</h2><p>Every signed contract goes into a simple tracker: category, vendor, total, deposit paid, balance due and due date. Review it weekly.</p>
<p><a href="../get-started.html">Get itemised quotes from matched vendors →</a></p>"""),
 ("choosing-a-venue", "Choosing an Event Venue: 15 Questions to Ask Before You Sign", "Venues",
  "The questions that reveal a venue's true cost and fit — capacity, minimums, inclusions, rules, timing and backup plans.",
  """<p>The venue sets your date, your capacity, your style and a big share of your budget. Ask these before signing.</p>
<h2>Capacity &amp; layout</h2><ol><li>What is the seated capacity for my layout (banquet, cocktail, theatre)? Banquet seating needs roughly 10–12 sq ft per guest.</li><li>Where do the dance floor, stage, bar and buffet go — and does capacity drop with them?</li><li>Is there a separate space for a ceremony or breakout sessions?</li></ol>
<h2>Money</h2><ol start="4"><li>Is there a food-and-beverage minimum, and what counts toward it?</li><li>What are the service charge, gratuity and tax rates?</li><li>Which items are included — tables, chairs, linens, AV, staff?</li><li>What's the deposit and payment schedule? What happens if I cancel or postpone?</li></ol>
<h2>Rules</h2><ol start="8"><li>Must I use in-house or approved caterers and bars?</li><li>Are there noise curfews, décor restrictions (candles, confetti) or outside-vendor fees?</li><li>Is event insurance required?</li></ol>
<h2>Timing &amp; logistics</h2><ol start="11"><li>When can vendors load in, and when must everything be out?</li><li>What does overtime cost per hour?</li><li>Is there parking, accessibility and a place for vendors to stage?</li></ol>
<h2>Risk</h2><ol start="14"><li>What's the rain or heat plan for outdoor spaces?</li><li>Who is my on-site contact on the day?</li></ol>
<p>Use our <a href="../plan.html">seating &amp; space calculator</a> before tours so you can spot an undersized room fast. <a href="../get-started.html">Request venue quotes →</a></p>"""),
 ("corporate-event-planning", "Planning a Corporate Event: From Objective to Run-of-Show", "Corporate",
  "A practical framework for offsites, conferences, launches and holiday parties — goals, budget, venue, agenda, AV and follow-up.",
  """<p>A corporate event is a business investment. Plan it like one: start with the outcome, not the venue.</p>
<h2>Define the objective</h2><p>Is it alignment, celebration, sales, recruiting or learning? Write one sentence and one measurable result — for example, “launch the new product to 200 partners and book 40 demos.”</p>
<h2>Budget per attendee</h2><p>Venue and AV typically take the largest share, followed by catering, speakers or entertainment, travel, marketing and staffing. Build per-attendee costs so leadership can compare formats.</p>
<h2>Pick the format</h2><ul><li><b>Offsite:</b> 15–60 people, workshops, a destination with meeting rooms.</li><li><b>Conference:</b> 100+ people, plenary plus breakouts, registration and badges.</li><li><b>Holiday party:</b> celebration first — great food, music and transport home.</li></ul>
<h2>Agenda that holds attention</h2><p>Keep sessions under 45 minutes, schedule interactive blocks after lunch, and put the most important content early in the day.</p>
<h2>AV is where events break</h2><p>Confirm projector or LED resolution, microphones, recording, Wi-Fi capacity and a technician on site. Rehearse every presentation on the actual equipment.</p>
<h2>Run-of-show</h2><p>A minute-by-minute document shared with every vendor and speaker: load-in, doors, sessions, meals, transitions and load-out, each with an owner.</p>
<h2>Measure and follow up</h2><p>Send a two-question survey within 24 hours, share recordings, and report the result against the objective you set.</p>
<p><a href="../get-started.html">Get corporate venue and AV quotes →</a></p>"""),
 ("fundraiser-gala-guide", "How to Plan a Fundraising Gala That Raises More Than It Costs", "Fundraisers",
  "Set a fundraising goal, control costs, secure sponsors and design the evening around giving moments.",
  """<p>A gala's success is net revenue, not attendance. Design every element around that number.</p>
<h2>Set the goal first</h2><p>Work backward from what the cause needs. Many organisations aim to keep costs well below a third of gross revenue; know your own target before you book anything.</p>
<h2>Sponsors pay for the event</h2><p>Offer tiered sponsorships — presenting, table, bar, dessert, auction — with clear benefits: logos, tables, speaking moments and social mentions. Ideally, sponsorships cover the hard costs so ticket sales and giving go to the mission.</p>
<h2>Price tickets and tables</h2><p>Price above cost per guest. Tables of 8–10 sold to companies are easier than individual tickets.</p>
<h2>Design the giving moments</h2><ul><li><b>Paddle raise:</b> one compelling story, one concrete goal, gift levels called from highest to lowest.</li><li><b>Auction:</b> fewer, better items. Experiences outperform objects.</li><li><b>Raffle or games:</b> check local rules on raffles and gaming licences first.</li></ul>
<h2>Control costs</h2><p>Seek in-kind donations for venue, wine, flowers and printing. Keep the programme tight — under 90 minutes of speaking.</p>
<h2>Follow up within 48 hours</h2><p>Thank donors personally, share the total raised and show what it will fund.</p>
<p><a href="../get-started.html">Get gala venue and catering quotes →</a></p>"""),
]
gcards = ""
for slug, title, tag, desc, body in guides:
    art = f"""<section class="pagehead"><div class="wrap prose"><div class="breadcrumb"><a href="{{R}}index.html">Home</a> / <a href="{{R}}guides/index.html">Guides</a> / {tag}</div><span class="tag">{tag}</span><h1>{title}</h1><p class="src">By the 62287.com editorial team · Updated {TODAY}</p></div></section>
<section><div class="wrap two"><article class="prose">{body}
<p class="src" style="margin-top:2em">General planning information only; not legal, tax or financial advice. Prices vary by region and vendor.</p></article>
<aside><div class="tool"><h3>Ready to book?</h3><p>Get up to 3 vendor quotes that fit your date, guests and budget — free.</p><a class="btn btn-primary" href="{{R}}get-started.html">Get quotes →</a></div>
<div class="ad-zone"><div class="ad-label">Advertisement</div></div>
<div class="tool"><h3>More guides</h3><ul class="prose">""" + "".join(f'<li><a href="{{R}}guides/{s}.html">{t}</a></li>' for s, t, *_ in guides if s != slug) + """</ul></div></aside></div></section>"""
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "dateModified": TODAY, "author": {"@type": "Organization", "name": BRAND}, "publisher": {"@type": "Organization", "name": BRAND}}) + "</script>"
    page(f"guides/{slug}.html", f"{title} | 62287.com", desc, art, tag.lower(), ld)
    gcards += f'<div class="card"><span class="tag">{tag}</span><h3>{title}</h3><p>{desc}</p><a class="more" href="{{R}}guides/{slug}.html">Read →</a></div>'
page("guides/index.html", "Event Planning Guides — Budgets, Venues, Corporate & Fundraisers | 62287.com",
     "In-depth event planning guides: building a budget that holds, choosing a venue, planning corporate events and running a fundraising gala.",
     pagehead("Guides", "Long-form, numbers-first guides for anyone planning an event.", "Guides") + f'<section><div class="wrap"><div class="cards">{gcards}</div></div></section>', "guides articles")
page("index.html", "62287.com — OCCUR: Free Event Planning Tools, Budgets & Vendor Quotes",
     "Plan weddings, birthdays, corporate events and fundraisers: free budget, catering, seating and timeline tools, a vendor directory and free vendor quotes.",
     home.replace('<div class="cards" id="guidecards"></div>', f'<div class="cards">{gcards}</div>'), "home occur 62287 event planning", faq_ld)

# ======================= ABOUT / CONTACT / LEGAL =======================
about = pagehead("About 62287.com", "OCCUR — an independent, numbers-first hub for planning events.", "About") + """
<section><div class="wrap prose">
<h2>Why “OCCUR”?</h2><p>Type 6-2-2-8-7 on a phone keypad and it spells O-C-C-U-R. Our job is to help events occur: planned clearly, booked on time and delivered on budget.</p>
<h2>What we do</h2><p>We publish free planning calculators, practical guides, a vendor directory and a seasonal planning calendar, and we connect planners with vetted vendors when they're ready to book.</p>
<h2>How we make money</h2><p>Display advertising (Google AdSense), featured vendor listings, sponsorships and referral fees from vendors. Editorial content is never paid for unless clearly labelled as sponsored.</p>
<h2>Our numbers</h2><p>Budget splits, per-guest figures and space ratios are widely used industry rules of thumb, presented as planning estimates. Real prices vary by city, season and vendor. Spot something off? <a href="{R}contact.html">Tell us</a>.</p>
</div></section>"""
page("about.html", "About 62287.com (OCCUR) — Independent Event Planning Hub", "Who runs 62287.com, why it's called OCCUR, how we make money and how we source our planning numbers.", about, "about occur")

contact = pagehead("Contact us", "Questions, corrections, vendor tips or partnership ideas — we reply within one business day.", "Contact") + """
<section><div class="wrap two">
<form class="tool" data-fs="Contact form"><h3>✉️ Send a message</h3>
<div class="row"><div class="field"><label for="ct_name">Name</label><input id="ct_name" name="name" required></div><div class="field"><label for="ct_mail">Email</label><input id="ct_mail" name="email" type="email" required></div></div>
<div class="field"><label for="ct_topic">Topic</label><select id="ct_topic" name="topic"><option>General question</option><option>Correction</option><option>Guide or video tip</option><option>Advertising</option><option>Partnership</option><option>Privacy request</option></select></div>
<div class="field"><label for="ct_msg">Message</label><textarea id="ct_msg" name="message" rows="5" required></textarea></div>
<button class="btn btn-primary" type="submit">Send →</button></form>
<div class="prose"><h2>Interested in this domain?</h2><p>For acquisition of 62287.com, sponsorship, advertising or partnership proposals, use our <a href="https://web.works/contact" target="_blank" rel="noopener">dedicated partnership contact page</a>.</p>
<h2>Need quotes for an event?</h2><p>The fastest route is our <a href="{R}get-started.html">free quote form</a>.</p></div>
</div></section>"""
page("contact.html", "Contact 62287.com", "Contact the 62287.com team for questions, corrections, tips, advertising and partnerships.", contact, "contact message")

privacy = pagehead("Privacy policy", f"Last updated {TODAY}.", "Privacy") + """
<section><div class="wrap prose">
<h2>Information we collect</h2><p>When you submit a form we collect the details you enter (such as name, email, phone and event details). We also collect standard technical data (browser type, pages viewed, approximate location) through cookies and similar technologies.</p>
<h2>How we use it</h2><ul><li>To respond to your request and, with your consent, share it with up to three relevant vendors.</li><li>To send newsletters you've subscribed to (unsubscribe anytime).</li><li>To operate, secure and improve the site.</li></ul>
<h2>Form processing</h2><p>Forms are delivered by a third-party form-processing service, FormSubmit, which transmits your submission to us by email.</p>
<h2>Advertising &amp; Google AdSense</h2><p>Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and/or other sites on the Internet. You may opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">www.aboutads.info</a>. Learn how Google uses data at <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">policies.google.com/technologies/partner-sites</a>.</p>
<h2>Embedded content</h2><p>Video pages link to or embed YouTube content (privacy-enhanced mode) only after you click.</p>
<h2>Your rights</h2><p>You can request access, correction or deletion of your personal information via our <a href="{R}contact.html">contact form</a> (choose “Privacy request”). Residents of Canada, California, the EEA/UK and other regions may have additional rights under local law.</p>
<h2>Children</h2><p>This site is not directed to children under 13 and we do not knowingly collect their data.</p>
<h2>Changes</h2><p>We may update this policy; the date above shows the latest version.</p>
</div></section>"""
page("privacy.html", "Privacy Policy | 62287.com", "How 62287.com collects, uses and protects your information, including cookies, Google AdSense and form submissions.", privacy, "privacy cookies adsense")

terms = pagehead("Terms of use", f"Last updated {TODAY}.", "Terms") + """
<section><div class="wrap prose">
<h2>Use of the site</h2><p>By using 62287.com you agree to these terms. Content is general planning information and is not legal, financial or professional advice.</p>
<h2>Estimates</h2><p>Calculators and cost figures are estimates. Confirm all prices, terms and availability directly with vendors, in writing.</p>
<h2>Vendors &amp; referrals</h2><p>We may refer you to independent vendors. We are not party to your contracts with them and are not responsible for their services. We may receive referral compensation.</p>
<h2>User submissions</h2><p>You keep ownership of content you submit (event ideas, contest entries) and grant us a non-exclusive licence to display it on the site and in promotions. Don't submit content you don't have rights to, or photos of people without their consent.</p>
<h2>Contests</h2><p>Each contest is governed by its official rules on the Support page. No purchase necessary. Void where prohibited.</p>
<h2>Donations</h2><p>Donations support site operations and are not tax-deductible. Pledges are voluntary and non-binding until paid.</p>
<h2>Liability</h2><p>The site is provided “as is”. To the fullest extent permitted by law, we disclaim liability for losses arising from use of the site.</p>
<h2>Contact</h2><p>Questions? Use our <a href="{R}contact.html">contact form</a>.</p>
</div></section>"""
page("terms.html", "Terms of Use | 62287.com", "Terms governing use of 62287.com, including vendor referrals, user submissions, contests and donations.", terms, "terms legal")

disc = pagehead("Trademark &amp; copyright disclosure", "Plain-English statement of what we do and don't claim.", "Disclosure") + """
<section><div class="wrap prose">
<h2>The number “62287” and the word “occur”</h2><p>“62287” is a five-digit number; on a standard telephone keypad its digits correspond to the letters of the ordinary English word “occur”. 62287.com uses the number and the word descriptively. We claim <b>no trademark rights</b> in the number 62287 or the word “occur”, and we do not intend to suggest any connection with any business, product, part number, postal code, telephone number or organisation that uses them.</p>
<h2>No affiliation</h2><p>62287.com is independent and is not affiliated with, sponsored by or endorsed by any vendor, venue, YouTube, Google or any other company mentioned on the site. All trademarks belong to their respective owners and are used only for identification.</p>
<h2>Our copyright</h2><p>Original text, design, calculators and code on this site © 62287.com. All rights reserved. You may quote brief excerpts with attribution and a link.</p>
<h2>Third-party content</h2><p>Videos are linked or embedded from YouTube and remain the property of their creators. If you believe content on this site infringes your rights, send a notice through our <a href="{R}contact.html">contact form</a> (topic: “Correction”) identifying the material, and we will review and remove it promptly where appropriate.</p>
</div></section>"""
page("disclosure.html", "Trademark & Copyright Disclosure | 62287.com", "62287.com trademark and copyright disclosure: no claim to the number 62287 or the word occur, no affiliations, and how to report concerns.", disc, "trademark copyright disclosure dmca")

ty = """<section class="pagehead"><div class="wrap" style="text-align:center"><div style="font-size:3rem">✅</div><h1>Thank you!</h1><p class="lead" style="margin:0 auto">Your <b id="tyForm">submission</b> was received. We reply within one business day.</p>
<div style="display:flex;gap:12px;justify-content:center;margin-top:22px;flex-wrap:wrap"><a class="btn btn-primary" href="{R}plan.html">Try the planning tools</a><a class="btn btn-ghost" href="{R}guides/index.html">Read the guides</a></div></div></section>"""
page("thank-you.html", "Thank You | 62287.com", "Your submission has been received.", ty, extra='<meta name="robots" content="noindex">')
nf = """<section class="pagehead"><div class="wrap" style="text-align:center"><h1>404 — page not found</h1><p class="lead" style="margin:0 auto">That page didn't occur. Try the <a href="/62287-com/index.html">home page</a> or <a href="https://62287.com/">62287.com</a>.</p></div></section>"""
page("404.html", "Page Not Found | 62287.com", "Page not found.", nf, extra='<meta name="robots" content="noindex">')

# ---------- data, sitemap, misc ----------
os.makedirs(os.path.join(OUT, "data"), exist_ok=True)
json.dump(SEARCH, open(os.path.join(OUT, "data/search.json"), "w"), indent=1)
json.dump({"_how": "Add YouTube video IDs (the part after v=) to auto-embed them at the top of the Video Hub.",
           "videos": [{"id": "", "title": "Example: wedding planning timeline", "note": "Creator name"}]}, open(os.path.join(OUT, "data/videos.json"), "w"), indent=1)
urls = "".join(f"<url><loc>{SITE}/{'' if p['u']=='index.html' else p['u']}</loc><lastmod>{TODAY}</lastmod></url>" for p in SEARCH)
open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /thank-you.html\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(OUT, "ads.txt"), "w").write("google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
json.dump({"name": "62287.com — OCCUR", "short_name": "OCCUR", "start_url": "./index.html", "display": "standalone", "background_color": "#fbfaf8", "theme_color": "#d9480f",
           "icons": [{"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, open(os.path.join(OUT, "manifest.webmanifest"), "w"), indent=1)
json.dump({"last_refresh": datetime.datetime.now(datetime.timezone.utc).isoformat()}, open(os.path.join(OUT, "data/status.json"), "w"))
print("Built", len(SEARCH) + 2, "pages")
