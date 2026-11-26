#!/usr/bin/env python3
"""Static site generator for 62278.com. Run: python3 build.py  (writes HTML into repo root)."""
import json, os, datetime

SITE = "https://62278.com"
BRAND = "62278.com"
ADS = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
TODAY = datetime.date.today().isoformat()
OUT = os.path.dirname(os.path.abspath(__file__))
SEARCH = []

NAV = [("index.html", "Home"), ("live.html", "Live & Move"), ("business.html", "Business"),
       ("directory.html", "Directory"), ("events.html", "Events"), ("guides/index.html", "Guides"),
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
<meta name="theme-color" content="#c2185b">
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
    items.append(f'<li><a class="cta" href="{root}get-started.html">Get Matched Free</a></li>')
    return f"""<body data-root="{root}">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><a href="https://web.works/contact" rel="noopener" target="_blank">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership →</a></div>
<header class="site"><div class="wrap nav">
<a class="brand" href="{root}index.html"><span class="logo">62</span><span>62278<small>Red Bud &amp; Metro-East Hub</small></span></a>
<nav aria-label="Main"><ul class="menu">{''.join(items)}</ul></nav>
<div style="display:flex;gap:8px"><button class="icon-btn" id="themeToggle" aria-label="Toggle dark mode">◐</button><button class="icon-btn burger" aria-label="Open menu" aria-expanded="false">☰</button></div>
</div></header>
<main id="main">"""


def footer(root):
    return f"""</main>
<div class="wrap ad-zone"><div class="ad-label">Advertisement</div></div>
<footer class="site"><div class="wrap">
<div class="fgrid">
<div><a class="brand" href="{root}index.html" style="color:#fff"><span class="logo">62</span><span>62278.com</span></a>
<p style="margin-top:14px;font-size:.92rem">An independent guide to living, working and building a business in the 62278 area — Red Bud, Illinois and the Metro-East countryside southeast of St. Louis.</p>
<form data-fs="Newsletter signup" style="display:flex;gap:8px;margin-top:10px"><input type="email" name="email" placeholder="Your email" required aria-label="Email for newsletter"><button class="btn btn-primary btn-sm" type="submit">Join</button></form>
<p style="font-size:.75rem;margin-top:6px">Weekly local digest. Unsubscribe anytime.</p></div>
<div><h4>Explore</h4><ul><li><a href="{root}live.html">Live &amp; relocate</a></li><li><a href="{root}business.html">Business &amp; site selection</a></li><li><a href="{root}directory.html">Local directory</a></li><li><a href="{root}events.html">Events calendar</a></li><li><a href="{root}guides/index.html">Guides</a></li><li><a href="{root}videos.html">Video hub</a></li><li><a href="{root}tools.html">Free calculators</a></li></ul></div>
<div><h4>Get involved</h4><ul><li><a href="{root}get-started.html">Get matched (free)</a></li><li><a href="{root}advertise.html">Advertise &amp; sponsor</a></li><li><a href="{root}support.html#donate">Donate</a></li><li><a href="{root}support.html#contests">Contests &amp; prizes</a></li><li><a href="{root}support.html#careers">Careers &amp; talent</a></li><li><a href="{root}directory.html#list">List your business</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="{root}about.html">About</a></li><li><a href="{root}contact.html">Contact</a></li><li><a href="{root}privacy.html">Privacy policy</a></li><li><a href="{root}terms.html">Terms of use</a></li><li><a href="{root}disclosure.html">Trademark &amp; copyright disclosure</a></li><li><a href="https://web.works/contact" target="_blank" rel="noopener">Buy / partner on this domain</a></li></ul></div>
</div>
<div class="legal">© <span class="yr"></span> 62278.com. All rights reserved. Independent publication — not affiliated with, endorsed by, or operated by the City of Red Bud, Randolph County, the State of Illinois or the U.S. Postal Service. ZIP Code™ is a trademark of the USPS. Figures are estimates from cited public sources; verify before making financial decisions. <a href="{root}disclosure.html">Full disclosure</a>.</div>
</div></footer>
<div class="cookie" role="dialog" aria-label="Cookie notice"><b>Cookies &amp; ads.</b> We use cookies for analytics and to show ads (Google AdSense), which may be personalised. See our <a href="{root}privacy.html">privacy policy</a>.<div style="display:flex;gap:8px;margin-top:10px"><button class="btn btn-primary btn-sm" data-v="all">Accept</button><button class="btn btn-ghost btn-sm" data-v="essential">Essential only</button></div></div>
<div class="sticky-cta"><a href="{root}get-started.html">🏡 Free local match — homes, services, business sites →</a></div>
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
def wizard(fs="Lead — Get Matched"):
    opts = [("buy", "🏡 Buy a home"), ("sell", "💰 Sell a home"), ("rent", "🔑 Rent"), ("relocate", "🚚 Relocate here"),
            ("business-site", "🏭 Business site / expansion"), ("contractor", "🛠️ Hire a local pro"),
            ("mortgage", "🏦 Mortgage / refinance"), ("insurance", "🛡️ Insurance quote"), ("advertise", "📣 Advertise to locals")]
    ch = "".join(f'<label class="choice"><input type="radio" name="intent" value="{v}" required>{l}</label>' for v, l in opts)
    return f"""<form class="wizard" data-fs="{fs}" id="match">
<div class="steps"><i></i><i></i><i></i></div>
<div class="step active"><h3>What can we help you with?</h3><p class="src">Pick one — takes 30 seconds. Free, no obligation.</p><div class="choices">{ch}</div></div>
<div class="step"><h3>A few details</h3>
<div class="row"><div class="field"><label for="w_time">Timeline</label><select id="w_time" name="timeline" required><option value="">Select…</option><option>ASAP / within 30 days</option><option>1–3 months</option><option>3–6 months</option><option>6–12 months</option><option>Just researching</option></select></div>
<div class="field"><label for="w_budget">Budget / value range</label><select id="w_budget" name="budget"><option value="">Select…</option><option>Under $150K</option><option>$150K–$250K</option><option>$250K–$400K</option><option>$400K–$750K</option><option>$750K+</option><option>Not applicable</option></select></div></div>
<div class="field"><label for="w_area">Area of interest</label><select id="w_area" name="area"><option>Red Bud (62278)</option><option>Elsewhere in Randolph County</option><option>Monroe County (Waterloo / Columbia)</option><option>St. Clair County / Metro-East</option><option>Flexible</option></select></div>
<div class="field"><label for="w_note">Anything specific? (optional)</label><textarea id="w_note" name="details" rows="3" placeholder="e.g. 3-bed with acreage near Route 3, or 2-acre lot for light manufacturing"></textarea></div>
<div style="display:flex;gap:10px"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div></div>
<div class="step"><h3>Where should we send your match?</h3>
<div class="row"><div class="field"><label for="w_name">Full name</label><input id="w_name" name="name" required autocomplete="name"></div>
<div class="field"><label for="w_email">Email</label><input id="w_email" type="email" name="email" required autocomplete="email"></div></div>
<div class="row"><div class="field"><label for="w_phone">Phone (optional, faster)</label><input id="w_phone" type="tel" name="phone" autocomplete="tel"></div>
<div class="field"><label for="w_contact">Best way to reach you</label><select id="w_contact" name="preferred_contact"><option>Email</option><option>Phone call</option><option>Text</option></select></div></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request by 62278.com and up to 3 vetted local partners. No spam; consent isn't a condition of purchase. See <a href="{{R}}privacy.html">privacy</a>.</label>
<div style="display:flex;gap:10px;margin-top:14px"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="submit" class="btn btn-primary">Get my free match ✓</button></div></div>
<div class="trust"><span>🔒 Private &amp; secure</span><span>⚡ Reply within 1 business day</span><span>💸 100% free for you</span></div>
</form>"""


# ======================= HOME =======================
home = f"""
<section class="hero"><div class="wrap grid">
<div><span class="eyebrow">ZIP 62278 · Red Bud, Illinois</span>
<h1>Small-town living. Big-city reach. <span style="color:var(--bud)">One ZIP code.</span></h1>
<p class="lead">The independent hub for moving to, investing in and doing business in the 62278 area — 36 miles southeast of St. Louis, where three state highways, a river port and a ready-to-build business park meet.</p>
<div class="actions"><a class="btn btn-primary" href="{{R}}get-started.html">Get matched free →</a><a class="btn btn-ghost" href="{{R}}tools.html">Try the calculators</a></div>
<div class="searchbox" style="max-width:520px;margin-top:22px"><input id="siteSearch" type="search" placeholder="Search guides, tools, events… (try “mortgage”, “business park”)" aria-label="Search site"><div class="sresults" id="sResults"></div></div>
</div>
<div class="zipcard reveal"><div class="src">Snapshot</div><div class="zip">62278</div><div style="font-weight:700">Red Bud · Randolph County · IL</div>
<div class="statgrid">
<div class="stat"><b>6,425</b><span>ZIP-area residents (ACS 2023)</span></div>
<div class="stat"><b>$85,017</b><span>Median household income (ACS 2023)</span></div>
<div class="stat"><b>~$200K</b><span>Median home sale (Redfin, Nov 2025)</span></div>
<div class="stat"><b>36 mi</b><span>to St. Louis, MO</span></div>
</div><p class="src" style="margin-top:10px">Sources: U.S. Census ACS 5-yr (via Population Review), Redfin, City of Red Bud. <a href="{{R}}about.html#data">Methodology</a></p></div>
</div></section>
{AD}
<section><div class="wrap">
<div class="sec-head reveal"><span class="eyebrow">What you can do here</span><h2>Everything 62278, in one place</h2><p>Built for four kinds of visitors: movers, home buyers and sellers, business owners scouting a site, and locals who want to grow.</p></div>
<div class="cards">
<div class="card reveal"><div class="ic">🏡</div><h3>Live &amp; relocate</h3><p>Cost of living, housing, schools, healthcare and commute math versus St. Louis — honest trade-offs, not brochure copy.</p><a class="more" href="{{R}}live.html">Relocation guide →</a></div>
<div class="card reveal"><div class="ic">🏭</div><h3>Business &amp; site selection</h3><p>Business park lots, Foreign Trade Zone 31, river-port and highway access, incentives — plus a logistics-reach calculator.</p><a class="more" href="{{R}}business.html">Build here →</a></div>
<div class="card reveal"><div class="ic">📇</div><h3>Local directory</h3><p>Contractors, healthcare, food, ag services and pros across the 62278 area. Free basic listings for local businesses.</p><a class="more" href="{{R}}directory.html">Browse directory →</a></div>
<div class="card reveal"><div class="ic">🧮</div><h3>Free calculators</h3><p>Mortgage, affordability, commute cost, cost-of-living swap, startup capital and break-even — all in your browser.</p><a class="more" href="{{R}}tools.html">Open tools →</a></div>
<div class="card reveal"><div class="ic">🎉</div><h3>Events &amp; traditions</h3><p>Chocolate Walk, Firemen's Picnic, Christmas Walk and the lighted parade — a year-round community calendar.</p><a class="more" href="{{R}}events.html">See the calendar →</a></div>
<div class="card reveal"><div class="ic">▶️</div><h3>Video hub</h3><p>Curated video guides on small-town relocation, Metro-East real estate and launching a local business.</p><a class="more" href="{{R}}videos.html">Watch →</a></div>
</div></div></section>

<section class="alt" id="get-matched"><div class="wrap two">
<div class="reveal"><span class="eyebrow">Free local matching</span><h2>Tell us what you need. We'll connect you with the right local pro.</h2>
<p>One short form routes you to a vetted agent, lender, contractor, insurer or economic-development contact — whoever actually fits your request. You'll hear back within one business day.</p>
<ul class="prose"><li><b>Buyers &amp; sellers:</b> local market pricing, not national averages.</li><li><b>Businesses:</b> lot availability, utilities and incentive questions routed to the right people.</li><li><b>Homeowners:</b> up to 3 quotes from local trades — you choose.</li></ul>
<p class="src">We may earn a referral fee from partners. That never costs you anything and never changes who we recommend.</p></div>
<div class="reveal">{wizard()}</div>
</div></section>
{AD}
<section><div class="wrap two">
<div class="reveal"><span class="eyebrow">Why 62278</span><h2>The case in four numbers</h2>
<table><tr><th>Factor</th><th>62278 area</th><th>Why it matters</th></tr>
<tr><td>Median home sale</td><td>~$200K</td><td>Entry price far below most metro suburbs (Redfin, Nov 2025)</td></tr>
<tr><td>Days on market</td><td>~43–46</td><td>Competitive, but buyers still have time to inspect</td></tr>
<tr><td>Highways</td><td>IL-3, 154, 159</td><td>Three state routes cross in town</td></tr>
<tr><td>Business park</td><td>50.58 acres</td><td>Ready-to-build light industrial / commercial lots</td></tr></table>
<p class="src">Sources: Redfin 62278 housing market; City of Red Bud economic development.</p></div>
<div class="reveal"><div class="tool" id="fitquiz"><h3>🎯 Is 62278 a fit for you?</h3>
<div class="field"><label>How much do you want space &amp; yard?</label><select><option value="">Select…</option><option value="3">A lot — acreage dream</option><option value="2">A decent yard</option><option value="0">Don't care</option></select></div>
<div class="field"><label>Your work setup</label><select><option value="">Select…</option><option value="3">Remote / hybrid</option><option value="2">Commute to St. Louis is OK</option><option value="1">Local job or business</option><option value="0">Need a big-city office daily</option></select></div>
<div class="field"><label>Nightlife &amp; dining expectations</label><select><option value="">Select…</option><option value="3">Quiet evenings, local spots</option><option value="2">Happy to drive for big nights out</option><option value="0">Need it walking distance</option></select></div>
<div class="field"><label>Housing budget priority</label><select><option value="">Select…</option><option value="3">Get more house for less</option><option value="2">Balanced</option><option value="0">Price doesn't matter</option></select></div>
<div class="result" id="fit_out">Answer all 4 questions to see your fit score.</div></div></div>
</div></section>

<section class="alt"><div class="wrap">
<div class="sec-head"><span class="eyebrow">Latest guides</span><h2>Read before you decide</h2></div>
<div class="cards">
<div class="card"><span class="tag">Relocation</span><h3>Moving from St. Louis to a small Illinois town</h3><p>Taxes, commute, schools, and what you'll miss — a numbers-first checklist.</p><a class="more" href="{{R}}guides/moving-from-st-louis.html">Read →</a></div>
<div class="card"><span class="tag">Business</span><h3>How to choose a small-town industrial site</h3><p>Utilities, zoning, workforce and logistics — the 12 questions to ask first.</p><a class="more" href="{{R}}guides/small-town-site-selection.html">Read →</a></div>
<div class="card"><span class="tag">Homes</span><h3>Buying a home in a competitive small market</h3><p>Why ~45 days on market still rewards preparation — offers, inspections, financing.</p><a class="more" href="{{R}}guides/buying-a-home-small-market.html">Read →</a></div>
<div class="card"><span class="tag">Main Street</span><h3>Launching a Main Street business</h3><p>Capital, break-even and local marketing for a storefront in a 4,000-person town.</p><a class="more" href="{{R}}guides/main-street-business-launch.html">Read →</a></div>
</div></div></section>

<section><div class="wrap">
<div class="sec-head"><span class="eyebrow">FAQ</span><h2>Quick answers</h2></div>
<details><summary>What is 62278?</summary><p>62278 is the ZIP Code for Red Bud, Illinois, in the northwest corner of Randolph County, about 36 miles southeast of St. Louis, Missouri. This site is an independent guide to that area.</p></details>
<details><summary>Is this the official city website?</summary><p>No. 62278.com is an independent publication. For permits, utilities and official notices use the City of Red Bud's own website and offices.</p></details>
<details><summary>How much do homes cost in 62278?</summary><p>Redfin reported a median sale price of about $200K in November 2025, up roughly 26% year over year. Small markets swing month to month, so ask a local agent for current comps.</p></details>
<details><summary>Is the matching service really free?</summary><p>Yes. Partners may pay us a referral fee; you pay nothing and are never obligated to hire anyone.</p></details>
<details><summary>Can I advertise or sponsor this site?</summary><p>Yes — see <a href="{{R}}advertise.html">Advertise &amp; sponsor</a>, or use the contact link at the top of any page for domain, sponsorship and partnership inquiries.</p></details>
</div></section>
"""
faq_ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "WebSite", "name": BRAND, "url": SITE, "potentialAction": {"@type": "SearchAction", "target": SITE + "/?q={q}", "query-input": "required name=q"}},
    {"@type": "Organization", "name": BRAND, "url": SITE, "logo": SITE + "/assets/img/favicon.svg"},
    {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": "What is 62278?", "acceptedAnswer": {"@type": "Answer", "text": "62278 is the ZIP Code for Red Bud, Illinois, in Randolph County, about 36 miles southeast of St. Louis."}},
        {"@type": "Question", "name": "How much do homes cost in 62278?", "acceptedAnswer": {"@type": "Answer", "text": "Redfin reported a median sale price of about $200K in November 2025."}}]}]}) + "</script>"
page("index.html", "62278.com | Live, Move & Do Business in Red Bud, Illinois (ZIP 62278)",
     "Independent guide to ZIP 62278 — Red Bud, IL: homes, cost of living, business sites, local directory, events, free calculators and free local matching.",
     home, "home red bud 62278 zip", faq_ld)

# ======================= LIVE =======================
live = pagehead("Living in 62278: the honest relocation guide", "Housing, money, schools, healthcare and commute — what life in Red Bud and the surrounding countryside actually looks like.", "Live &amp; Move") + f"""
<section><div class="wrap two">
<div class="prose">
<h2>The short version</h2>
<p>Red Bud is a city of about 3,800 people (2020 census) at the center of a wider 62278 ZIP area of roughly 6,400 residents. It sits where Illinois Routes 3, 154 and 159 meet, inside commuting range of St. Louis, with a local hospital, a community-college campus, parks, a pool and a public golf course.</p>
<p>The trade is simple: <b>more house and quieter streets for less money, in exchange for a longer drive to big-city jobs, airports and nightlife.</b> If that trade suits you, 62278 is one of the better-value corners of the Metro-East.</p>
<h2>Housing</h2>
<p>Redfin put the 62278 median sale price at about <b>$200K in November 2025</b>, up about 26% year over year, with homes selling in roughly 43–46 days. Census ACS 2023 estimates put the median home value near <b>$181,500</b>. Translation: prices are rising fast from a low base, and well-priced homes don't sit long.</p>
<ul><li><b>Stock:</b> older brick homes near downtown, newer subdivisions on the edges, and rural acreage across the county.</li><li><b>Rentals:</b> limited — start early, and consider Waterloo or Columbia as backups.</li><li><b>Tip:</b> get pre-approved before touring; competitive listings often go to the first clean offer.</li></ul>
<h2>Money</h2>
<p>The ACS 2023 median household income for the ZIP area is about <b>$85,017</b>. With lower housing costs than most metro suburbs, that income stretches further — but Illinois property taxes are real, so budget them explicitly (see the mortgage calculator).</p>
<h2>Healthcare, schools &amp; services</h2>
<ul><li>Red Bud Regional Hospital serves the town; larger specialty systems are in the St. Louis area.</li><li>Public schools are run by the local district; Southwestern Illinois College (SWIC) operates a Red Bud campus with manufacturing and healthcare programs.</li><li>Red Bud Public Library, city pool, splash pad, parks and the North County Country Club golf course cover everyday recreation.</li></ul>
<h2>Commute</h2>
<p>Downtown St. Louis is about 40 driving miles away. Plan for 50–60 minutes each way depending on traffic and bridge. Use the commute calculator to price it honestly — a daily commute can cost several thousand dollars a year in fuel alone.</p>
<div class="note">Considering the move? <a href="{{R}}get-started.html?intent=relocate">Get a free relocation match</a> — we'll connect you with a local agent and answer neighborhood questions.</div>
</div>
<div>
<div class="tool" id="afford"><h3>🏠 What can I afford?</h3>
<div class="field"><label for="a_inc">Annual household income ($)</label><input id="a_inc" type="number" value="85000"></div>
<div class="row"><div class="field"><label for="a_debt">Monthly debts ($)</label><input id="a_debt" type="number" value="450"></div><div class="field"><label for="a_down">Down payment ($)</label><input id="a_down" type="number" value="25000"></div></div>
<div class="field"><label for="a_rate">Mortgage rate (%)</label><input id="a_rate" type="number" step="0.05" value="6.5"></div>
<div class="result" id="a_out"></div></div>
<div style="height:20px"></div>
<div class="tool" id="col"><h3>💵 Cost-of-living swap</h3>
<div class="field"><label for="col_sal">Your current salary ($)</label><input id="col_sal" type="number" value="90000"></div>
<div class="field"><label for="col_from">Where you live now</label><select id="col_from"><option value="100">U.S. average area</option><option value="97">St. Louis metro (est.)</option><option value="118">Chicago metro (est.)</option><option value="150">Coastal big city (est.)</option><option value="105">Mid-size suburb (est.)</option></select></div>
<div class="result" id="col_out"></div></div>
<div style="height:20px"></div>
<div class="tool" id="commute"><h3>🚗 Commute cost</h3>
<div class="row"><div class="field"><label for="c_miles">One-way miles</label><input id="c_miles" type="number" value="40"></div><div class="field"><label for="c_mpg">Vehicle MPG</label><input id="c_mpg" type="number" value="27"></div></div>
<div class="row"><div class="field"><label for="c_gas">Gas $/gal</label><input id="c_gas" type="number" step="0.01" value="3.10"></div><div class="field"><label for="c_days">Days/week</label><input id="c_days" type="number" value="5"></div></div>
<div class="result" id="c_out"></div></div>
</div></div></section>
{AD}
<section class="alt"><div class="wrap"><div class="sec-head"><h2>Neighbors worth comparing</h2><p>If 62278 inventory is tight, these nearby areas are common alternatives.</p></div>
<table><tr><th>Area</th><th>Feel</th><th>Best for</th></tr>
<tr><td>Red Bud (62278)</td><td>Historic small town, festivals, everyday services</td><td>Value + community</td></tr>
<tr><td>Waterloo (Monroe Co.)</td><td>Larger town, more retail</td><td>Shorter St. Louis commute</td></tr>
<tr><td>Columbia (Monroe Co.)</td><td>Suburban edge of the metro</td><td>Commuters prioritising time</td></tr>
<tr><td>Rural Randolph County</td><td>Farmland, acreage, river bluffs</td><td>Space, hobby farms, privacy</td></tr></table></div></section>
"""
page("live.html", "Living in Red Bud, IL 62278 — Cost of Living, Housing & Relocation Guide | 62278.com",
     "Honest relocation guide to ZIP 62278: home prices, income, healthcare, schools, commute to St. Louis, plus affordability, cost-of-living and commute calculators.", live, "relocate move housing cost of living commute schools")

# ======================= BUSINESS =======================
biz = pagehead("Build your business in 62278", "Ready-to-build lots, Foreign Trade Zone access, river, rail and highway logistics — and a workforce pipeline between two university systems.", "Business") + f"""
<section><div class="wrap two">
<div class="prose">
<h2>The location pitch, in plain numbers</h2>
<ul><li><b>Red Bud Business Park:</b> 50.58 acres bought by the city in 2017, planned as light-industrial/commercial lots of roughly 1–4 acres, with gas, water, sewer and fiber internet.</li>
<li><b>Foreign Trade Zone 31:</b> the city sits inside FTZ 31, which can defer or reduce duties for qualifying import/export operations.</li>
<li><b>Roads:</b> IL-3, 154 and 159 cross in town; the city cites reach to about 80% of the U.S. population within a two-day truck drive.</li>
<li><b>River:</b> the Kaskaskia Regional Port District's Dock #2 is about a five-minute drive, giving barge access to the Mississippi system.</li>
<li><b>Talent:</b> positioned between SIU Edwardsville and SIU Carbondale, with SWIC's Red Bud campus training manufacturing and healthcare workers.</li>
<li><b>Incentives:</b> the city advertises loan programs, sales-tax rebate incentives and an enterprise zone; state programs stack on top. Eligibility varies — confirm with the city.</li></ul>
<p class="src">Sources: City of Red Bud economic development pages and Red Bud Business Park profile guide. Verify current lot availability directly with the city.</p>
<h2>Who it fits</h2>
<p>Light manufacturing, fabrication, ag-processing, distribution serving the St. Louis metro, contractors' yards, and service businesses priced out of Metro-East suburbs. It is a weaker fit for operations needing a large on-site labor pool from day one or daily air freight.</p>
</div>
<div><form class="wizard" data-fs="Lead — Business site inquiry" id="siteform">
<h3>🏭 Site-selection inquiry</h3><p class="src">We route qualified projects to the right economic-development, real-estate and finance contacts.</p>
<div class="row"><div class="field"><label for="b_co">Company</label><input id="b_co" name="company" required></div><div class="field"><label for="b_ind">Industry</label><input id="b_ind" name="industry" placeholder="e.g. metal fabrication"></div></div>
<div class="row"><div class="field"><label for="b_ac">Acres needed</label><select id="b_ac" name="acres"><option>Under 1</option><option>1–2</option><option>2–4</option><option>4+</option><option>Existing building</option></select></div><div class="field"><label for="b_jobs">Jobs created (est.)</label><input id="b_jobs" name="jobs" type="number" min="0"></div></div>
<div class="row"><div class="field"><label for="b_inv">Capital investment</label><select id="b_inv" name="investment"><option>Under $500K</option><option>$500K–$2M</option><option>$2M–$10M</option><option>$10M+</option></select></div><div class="field"><label for="b_when">Target start</label><select id="b_when" name="timeline"><option>0–6 months</option><option>6–12 months</option><option>12–24 months</option><option>Exploring</option></select></div></div>
<div class="row"><div class="field"><label for="b_name">Your name</label><input id="b_name" name="name" required></div><div class="field"><label for="b_email">Work email</label><input id="b_email" name="email" type="email" required></div></div>
<div class="field"><label for="b_phone">Phone</label><input id="b_phone" name="phone" type="tel"></div>
<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about this project.</label>
<button class="btn btn-primary" type="submit" style="margin-top:12px">Request site info →</button></form></div>
</div></section>
{AD}
<section class="alt"><div class="wrap two">
<div class="tool" id="reach"><h3>🚛 Logistics reach from 62278</h3>
<div class="row"><div class="field"><label for="r_mph">Avg truck speed (mph)</label><input id="r_mph" type="number" value="55"></div><div class="field"><label for="r_hrs">Driving hours/day</label><input id="r_hrs" type="number" value="11"></div></div>
<table><thead><tr><th>Destination</th><th>Distance</th><th>Drive</th><th>Delivery</th></tr></thead><tbody></tbody></table>
<p class="src">Approximate road miles from Red Bud; planning estimate only.</p></div>
<div class="tool" id="startup"><h3>📈 Startup capital &amp; break-even</h3>
<div class="row"><div class="field"><label for="s_build">Build-out / fit-out ($)</label><input id="s_build" type="number" value="40000"></div><div class="field"><label for="s_equip">Equipment ($)</label><input id="s_equip" type="number" value="35000"></div></div>
<div class="row"><div class="field"><label for="s_inv">Opening inventory ($)</label><input id="s_inv" type="number" value="15000"></div><div class="field"><label for="s_rent">Rent/mortgage per month ($)</label><input id="s_rent" type="number" value="2200"></div></div>
<div class="row"><div class="field"><label for="s_staff">Payroll per month ($)</label><input id="s_staff" type="number" value="9000"></div><div class="field"><label for="s_mkt">Marketing &amp; other per month ($)</label><input id="s_mkt" type="number" value="1500"></div></div>
<div class="row"><div class="field"><label for="s_ticket">Avg sale ($)</label><input id="s_ticket" type="number" value="45"></div><div class="field"><label for="s_margin">Gross margin (%)</label><input id="s_margin" type="number" value="55"></div></div>
<div class="result" id="s_out"></div></div>
</div></section>
"""
page("business.html", "Business & Site Selection in Red Bud, IL 62278 — Business Park, FTZ 31, Logistics | 62278.com",
     "Site-selection guide for ZIP 62278: Red Bud Business Park lots, Foreign Trade Zone 31, river port and highway access, incentives, logistics and break-even calculators.", biz, "business park industrial site selection ftz incentives logistics")

# ======================= DIRECTORY =======================
cats = [("home", "Home services", ["General contractors & remodelers", "Roofing & gutters", "HVAC & plumbing", "Electricians", "Landscaping & lawn care"]),
        ("realestate", "Real estate & finance", ["Real-estate agents & brokers", "Mortgage lenders & credit unions", "Home inspectors", "Title & closing services", "Insurance agents"]),
        ("health", "Health & wellness", ["Hospital & clinics", "Dentists & eye care", "Pharmacies", "Fitness & YMCA programs", "Senior care"]),
        ("food", "Food & drink", ["Cafés & coffee", "Pizza & family dining", "Bars & grills", "Bakeries & sweets", "Catering"]),
        ("ag", "Agriculture & industry", ["Farm supply & equipment", "Ag services & custom harvest", "Machine shops & fabrication", "Trucking & logistics", "Grain & elevators"]),
        ("pro", "Professional services", ["Accountants & tax prep", "Attorneys", "Marketing & web design", "IT & computer repair", "Printing & signs"])]
cards = "".join(f'<div class="card" data-cat="{c}"><h3>{n}</h3><ul class="prose" style="font-size:.95rem">' + "".join(f"<li>{x}</li>" for x in items) +
                f'</ul><a class="more" href="{{R}}get-started.html?intent=contractor">Request quotes →</a></div>' for c, n, items in cats)
chips = '<button class="chip on" data-cat="all">All</button>' + "".join(f'<button class="chip" data-cat="{c}">{n}</button>' for c, n, _ in cats)
directory = pagehead("62278 Local Directory", "Find trusted local businesses across Red Bud and the surrounding countryside — or get your own business listed free.", "Directory") + f"""
<section><div class="wrap">
<div class="filters" data-target="#dirgrid">{chips}</div>
<div class="cards" id="dirgrid">{cards}</div>
<p class="note" style="margin-top:20px">Listings are being verified category by category. Need someone now? <a href="{{R}}get-started.html?intent=contractor">Request up to 3 quotes</a> and we'll match you directly.</p>
</div></section>
{AD}
<section class="alt" id="list"><div class="wrap two">
<div class="prose"><h2>List your business — free</h2><p>Local customers search here before they search anywhere else. A basic listing is free. Featured listings add a logo, photos, a priority position and lead routing from our matching form.</p>
<table><tr><th>Plan</th><th>Includes</th><th>Price</th></tr><tr><td>Basic</td><td>Name, category, phone, website</td><td>Free</td></tr><tr><td>Featured</td><td>Top placement, logo, photos, lead routing</td><td>From $29/mo</td></tr><tr><td>Category sponsor</td><td>Exclusive category banner + all Featured perks</td><td>From $99/mo</td></tr></table></div>
<form class="tool" data-fs="Directory listing request"><h3>📇 Add / claim a listing</h3>
<div class="field"><label for="l_biz">Business name</label><input id="l_biz" name="business" required></div>
<div class="row"><div class="field"><label for="l_cat">Category</label><select id="l_cat" name="category">{''.join(f'<option>{n}</option>' for _, n, _ in cats)}</select></div><div class="field"><label for="l_plan">Plan</label><select id="l_plan" name="plan"><option>Basic (free)</option><option>Featured</option><option>Category sponsor</option></select></div></div>
<div class="row"><div class="field"><label for="l_phone">Business phone</label><input id="l_phone" name="phone" type="tel"></div><div class="field"><label for="l_web">Website</label><input id="l_web" name="website" type="url" placeholder="https://"></div></div>
<div class="row"><div class="field"><label for="l_name">Your name</label><input id="l_name" name="name" required></div><div class="field"><label for="l_email">Email</label><input id="l_email" name="email" type="email" required></div></div>
<button class="btn btn-primary" type="submit">Submit listing →</button></form>
</div></section>
"""
page("directory.html", "62278 Local Business Directory — Red Bud, IL Contractors, Health, Food & Services | 62278.com",
     "Browse local businesses in the 62278 area — home services, real estate, health, food, agriculture and professional services — or list your business free.", directory, "directory contractors plumbers restaurants listing")

# ======================= EVENTS =======================
events = pagehead("Events &amp; traditions in 62278", "A year in Red Bud: festivals, holiday walks and community nights. Dates shift each year — confirm with organisers before you go.", "Events") + f"""
<section><div class="wrap two">
<div class="timeline">
<div class="ev"><div class="month">February</div><h3>Chocolate Walk</h3><p>Downtown shops and sweets — a winter favourite for couples and friends.</p></div>
<div class="ev"><div class="month">Spring</div><h3>Redbud bloom season</h3><p>The town takes its name from the native redbud tree, which blooms in spring — the best time for photos (and our photo contest).</p></div>
<div class="ev"><div class="month">Summer</div><h3>Red Bud Firemen's Picnic</h3><p>A long-running community tradition with food, rides, games and music — the 97th edition was held recently.</p></div>
<div class="ev"><div class="month">Summer</div><h3>Parks, pool &amp; concerts</h3><p>Concerts, markets and family events in Ratz Park and Lincoln Park; the city pool and splash pad keep kids busy.</p></div>
<div class="ev"><div class="month">September</div><h3>Hops and Hogs Brew-B-Que</h3><p>Craft beer and barbecue in town — check the regional visitors guide for the date.</p></div>
<div class="ev"><div class="month">October</div><h3>Witches Night Out</h3><p>A Halloween-season shopping night downtown.</p></div>
<div class="ev"><div class="month">Late November</div><h3>Lighted Parade &amp; Tree Lighting</h3><p>The official start of the holiday season.</p></div>
<div class="ev"><div class="month">December</div><h3>Red Bud Christmas Walk</h3><p>Christmas market, shopping bingo and local tastings across downtown.</p></div>
</div>
<div><form class="tool" data-fs="Event submission"><h3>📅 Submit an event</h3><p class="src">Organisers: get your event in front of local readers. Free for community and non-profit events.</p>
<div class="field"><label for="e_t">Event name</label><input id="e_t" name="event" required></div>
<div class="row"><div class="field"><label for="e_d">Date</label><input id="e_d" name="date" type="date" required></div><div class="field"><label for="e_l">Location</label><input id="e_l" name="location"></div></div>
<div class="field"><label for="e_desc">Description</label><textarea id="e_desc" name="description" rows="3"></textarea></div>
<div class="row"><div class="field"><label for="e_n">Your name</label><input id="e_n" name="name" required></div><div class="field"><label for="e_e">Email</label><input id="e_e" name="email" type="email" required></div></div>
<label class="check"><input type="checkbox" name="promote" value="yes"> I'm interested in a paid promoted placement.</label>
<button class="btn btn-primary" type="submit" style="margin-top:10px">Submit event →</button></form>
<div class="note" style="margin-top:20px">Event sponsors get logo placement on this calendar and in the weekly digest. <a href="{{R}}advertise.html">See sponsor options</a>.</div></div>
</div></section>
"""
page("events.html", "Red Bud, IL Events Calendar — Festivals & Traditions in 62278 | 62278.com",
     "Annual events in Red Bud, Illinois (62278): Chocolate Walk, Firemen's Picnic, Brew-B-Que, Christmas Walk, lighted parade and more. Submit your event free.", events, "events festivals christmas walk picnic calendar")

# ======================= VIDEOS =======================
topics = [("Small-town relocation: pros &amp; cons", "moving to a small town pros and cons"), ("First-time home buyer walkthrough", "first time home buyer guide"),
          ("Mortgage pre-approval explained", "mortgage pre approval explained"), ("Choosing an industrial site", "industrial site selection tips"),
          ("Foreign Trade Zones in 5 minutes", "foreign trade zone explained"), ("Starting a Main Street business", "how to start a small town business"),
          ("Southern Illinois road trips", "southern illinois things to do"), ("St. Louis Metro-East living", "metro east illinois living")]
vc = "".join(f'<div class="vcard"><a class="vthumb" style="text-decoration:none" href="https://www.youtube.com/results?search_query={q.replace(" ", "+")}" target="_blank" rel="noopener">▶</a><div class="vb"><h3>{t}</h3><p class="src">Opens a curated YouTube search in a new tab.</p></div></div>' for t, q in topics)
videos = pagehead("62278 Video Hub", "Short, useful videos on moving, buying, financing and building a business in a small Midwestern town.", "Videos") + f"""
<section><div class="wrap"><div class="vgrid" id="vlist">{vc}</div>
<div class="note" style="margin-top:24px">Make a video about Red Bud or the Metro-East? <a href="{{R}}contact.html">Send it to us</a> — featured creators get a backlink and a shout-out in the weekly digest.</div></div></section>
"""
page("videos.html", "62278 Video Hub — Relocation, Real Estate & Small Business Videos | 62278.com",
     "Curated videos on small-town relocation, home buying, mortgages, site selection and starting a Main Street business near Red Bud, Illinois.", videos, "videos youtube watch")

# ======================= TOOLS =======================
tools = pagehead("Free calculators", "Run the numbers before you move, buy or launch. Everything runs privately in your browser.", "Tools") + f"""
<section><div class="wrap two">
<div class="tool" id="mtg"><h3>🏦 Mortgage payment</h3>
<div class="row"><div class="field"><label for="m_price">Home price ($)</label><input id="m_price" type="number" value="200000"></div><div class="field"><label for="m_down">Down payment ($)</label><input id="m_down" type="number" value="20000"></div></div>
<div class="row"><div class="field"><label for="m_rate">Rate (%)</label><input id="m_rate" type="number" step="0.05" value="6.5"></div><div class="field"><label for="m_years">Term (years)</label><select id="m_years"><option>30</option><option>20</option><option>15</option></select></div></div>
<div class="row"><div class="field"><label for="m_tax">Property tax (% of value/yr)</label><input id="m_tax" type="number" step="0.05" value="2.0"></div><div class="field"><label for="m_ins">Insurance ($/yr)</label><input id="m_ins" type="number" value="1400"></div></div>
<div class="result" id="m_out"></div><a class="btn btn-primary btn-sm" style="margin-top:12px" href="{{R}}get-started.html?intent=mortgage">Get real rate quotes →</a></div>
<div class="tool" id="afford"><h3>🏠 Affordability</h3>
<div class="field"><label for="a_inc">Annual household income ($)</label><input id="a_inc" type="number" value="85000"></div>
<div class="row"><div class="field"><label for="a_debt">Monthly debts ($)</label><input id="a_debt" type="number" value="450"></div><div class="field"><label for="a_down">Down payment ($)</label><input id="a_down" type="number" value="25000"></div></div>
<div class="field"><label for="a_rate">Rate (%)</label><input id="a_rate" type="number" step="0.05" value="6.5"></div>
<div class="result" id="a_out"></div></div>
</div>
<div class="wrap two" style="margin-top:28px">
<div class="tool" id="commute"><h3>🚗 Commute cost</h3>
<div class="row"><div class="field"><label for="c_miles">One-way miles</label><input id="c_miles" type="number" value="40"></div><div class="field"><label for="c_mpg">MPG</label><input id="c_mpg" type="number" value="27"></div></div>
<div class="row"><div class="field"><label for="c_gas">Gas $/gal</label><input id="c_gas" type="number" step="0.01" value="3.10"></div><div class="field"><label for="c_days">Days/week</label><input id="c_days" type="number" value="5"></div></div>
<div class="result" id="c_out"></div></div>
<div class="tool" id="col"><h3>💵 Cost-of-living swap</h3>
<div class="field"><label for="col_sal">Current salary ($)</label><input id="col_sal" type="number" value="90000"></div>
<div class="field"><label for="col_from">Where you live now</label><select id="col_from"><option value="100">U.S. average area</option><option value="97">St. Louis metro (est.)</option><option value="118">Chicago metro (est.)</option><option value="150">Coastal big city (est.)</option></select></div>
<div class="result" id="col_out"></div></div>
</div></section>
{AD}
<section class="alt"><div class="wrap"><p class="warn">Calculators give estimates for planning only. They are not financial, tax or lending advice. Rates, taxes and insurance vary by property and lender.</p>
<p>For business math — logistics reach, startup capital and break-even — see the <a href="{{R}}business.html#reach">business tools</a>.</p></div></section>
"""
page("tools.html", "Free Mortgage, Affordability, Commute & Cost-of-Living Calculators | 62278.com",
     "Free calculators for movers and buyers in the 62278 area: mortgage payment with Illinois property tax, affordability vs local median price, commute cost and cost-of-living swap.", tools, "calculator mortgage affordability commute cost of living tools")

# ======================= GET STARTED (lead gen) =======================
gs = pagehead("Get matched with the right local pro — free", "Homes, mortgages, insurance, contractors, business sites and advertising. One form, one business day.", "Get Matched") + f"""
<section><div class="wrap two">
<div>{wizard()}</div>
<div class="prose">
<h2>How it works</h2>
<ol><li><b>Tell us what you need</b> — 3 quick steps, about 60 seconds.</li><li><b>We review it personally</b> — no auto-blast to dozens of companies.</li><li><b>You get up to 3 matches</b> — local, vetted, and relevant to your request.</li><li><b>You decide</b> — no obligation, ever.</li></ol>
<h2>Who we match you with</h2>
<table><tr><th>You need</th><th>We connect you to</th></tr>
<tr><td>Buy / sell / rent</td><td>Agents active in the 62278 market</td></tr>
<tr><td>Mortgage / refi</td><td>Local lenders &amp; credit unions</td></tr>
<tr><td>Insurance</td><td>Independent agents (home, auto, farm, business)</td></tr>
<tr><td>Contractor</td><td>Licensed, insured local trades</td></tr>
<tr><td>Business site</td><td>Economic-development &amp; commercial real-estate contacts</td></tr>
<tr><td>Advertising</td><td>Our sponsorship team</td></tr></table>
<div class="note">Are you a local pro who wants these leads? <a href="{{R}}advertise.html#partner">Become a partner</a>.</div>
</div></div></section>
"""
page("get-started.html", "Get Matched Free — Local Agents, Lenders, Contractors & Business Sites in 62278 | 62278.com",
     "Free matching for the 62278 area: real-estate agents, mortgage lenders, insurance, contractors and business-site contacts. One short form, reply in one business day.", gs, "lead quote agent lender contractor insurance match")

# ======================= ADVERTISE =======================
adv = pagehead("Advertise, sponsor &amp; partner", "Reach movers, home buyers, business owners and locals in the 62278 area — at small-town prices.", "Advertise") + f"""
<section><div class="wrap">
<div class="tiers">
<div class="tier"><div class="src">Directory</div><div class="amt">$29</div><p>/month · Featured listing, logo, photos, lead routing</p></div>
<div class="tier"><div class="src">Category sponsor</div><div class="amt">$99</div><p>/month · Exclusive banner on one directory category</p></div>
<div class="tier"><div class="src">Event sponsor</div><div class="amt">$149</div><p>/event · Logo on calendar + digest mention</p></div>
<div class="tier"><div class="src">Site partner</div><div class="amt">Custom</div><p>Sitewide sponsorship, lead partnerships, contest prizes</p></div>
</div></div></section>
<section class="alt" id="partner"><div class="wrap two">
<div class="prose"><h2>Lead partnerships</h2><p>Agents, lenders, insurers and contractors can receive exclusive or shared leads from our matching form. Pay per qualified lead or a flat monthly fee for a category.</p>
<h2>Domain &amp; site partnership</h2><p>Interested in acquiring 62278.com, a revenue share, or a white-label partnership? Use the <a href="https://web.works/contact" target="_blank" rel="noopener">partnership contact page</a>.</p></div>
<form class="tool" data-fs="Advertising / sponsorship inquiry"><h3>📣 Advertising inquiry</h3>
<div class="row"><div class="field"><label for="ad_co">Business</label><input id="ad_co" name="business" required></div><div class="field"><label for="ad_pkg">Interested in</label><select id="ad_pkg" name="package"><option>Featured listing</option><option>Category sponsor</option><option>Event sponsor</option><option>Lead partnership</option><option>Contest prize sponsor</option><option>Sitewide / custom</option></select></div></div>
<div class="field"><label for="ad_budget">Monthly budget</label><select id="ad_budget" name="budget"><option>Under $100</option><option>$100–$500</option><option>$500–$2,000</option><option>$2,000+</option></select></div>
<div class="row"><div class="field"><label for="ad_n">Name</label><input id="ad_n" name="name" required></div><div class="field"><label for="ad_e">Email</label><input id="ad_e" name="email" type="email" required></div></div>
<div class="field"><label for="ad_m">Goals</label><textarea id="ad_m" name="message" rows="3"></textarea></div>
<button class="btn btn-primary" type="submit">Send inquiry →</button></form>
</div></section>
"""
page("advertise.html", "Advertise & Sponsor on 62278.com — Reach Red Bud & Metro-East Customers",
     "Featured listings, category and event sponsorships, lead partnerships and custom packages to reach movers, buyers and business owners in the 62278 area.", adv, "advertise sponsor partner leads")

# ======================= SUPPORT =======================
support = pagehead("Support 62278.com", "Keep an independent local guide free: donate, sponsor a contest prize, join the team, or enter a contest.", "Support") + f"""
<section id="donate"><div class="wrap two">
<div><h2>💗 Donate</h2><p>Donations fund hosting, local reporting, photography, promotion of local events, contest prizes and hiring local contributors.</p>
<div class="progress" aria-label="Funding progress"><i style="width:18%"></i></div><p class="src">2026 operations goal — every bit helps.</p>
<div class="tiers" style="margin-top:16px">
<div class="tier" data-amt="10"><div class="amt">$10</div><p>Supporter</p></div><div class="tier" data-amt="25"><div class="amt">$25</div><p>Neighbor</p></div><div class="tier" data-amt="100"><div class="amt">$100</div><p>Champion</p></div><div class="tier" data-amt="500"><div class="amt">$500</div><p>Founding patron</p></div></div>
<table style="margin-top:18px"><tr><th>Where it goes</th><th>Share</th></tr><tr><td>Operations &amp; hosting</td><td>35%</td></tr><tr><td>Local content &amp; contributors</td><td>30%</td></tr><tr><td>Promotion &amp; marketing</td><td>20%</td></tr><tr><td>Contests &amp; prizes</td><td>15%</td></tr></table></div>
<form class="tool" data-fs="Donation pledge"><h3>Pledge your support</h3><p class="src">Submit a pledge and we'll reply with a secure payment link. 62278.com is not a charity; donations are not tax-deductible.</p>
<div class="row"><div class="field"><label for="d_amount">Amount ($)</label><input id="d_amount" name="amount" type="number" min="1" value="25" required></div><div class="field"><label for="d_freq">Frequency</label><select id="d_freq" name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div class="field"><label for="d_use">Direct my gift to</label><select id="d_use" name="designation"><option>Where needed most</option><option>Ongoing operations</option><option>Promotions &amp; marketing</option><option>Hiring local talent</option><option>Contests &amp; prizes</option></select></div>
<div class="row"><div class="field"><label for="d_n">Name</label><input id="d_n" name="name" required></div><div class="field"><label for="d_e">Email</label><input id="d_e" name="email" type="email" required></div></div>
<label class="check"><input type="checkbox" name="public_thanks" value="yes"> Thank me publicly on the supporters wall.</label>
<button class="btn btn-primary" type="submit" style="margin-top:12px">Send pledge →</button></form>
</div></section>
{AD}
<section class="alt" id="contests"><div class="wrap two">
<div class="prose"><h2>🏆 Contests &amp; prizes</h2>
<h3>Redbud Season Photo Contest</h3><p>Capture spring in the 62278 area — redbud blooms, Main Street, farms, festivals. Winners are featured sitewide and receive sponsor-funded prizes (local gift cards and featured placement). Current prize details are posted here once each season's sponsors confirm.</p>
<h3>Best Small Business Pitch</h3><p>Pitch a business idea for Red Bud's downtown or business park in 300 words. Finalists get a free Featured listing for a year and a mentoring call.</p>
<h3>Official rules (summary)</h3><ul><li>No purchase necessary. Void where prohibited.</li><li>Open to legal U.S. residents 18+. One entry per person per contest.</li><li>Entries must be your own original work; you keep copyright and grant us a licence to display your entry.</li><li>Winners chosen by a judging panel on originality, quality and relevance; notified by email within 14 days of close.</li><li>Prizes are non-transferable; sponsors are listed with each contest.</li></ul>
<p>Want to fund a prize? <a href="{{R}}advertise.html">Become a contest sponsor</a>.</p></div>
<form class="tool" data-fs="Contest entry"><h3>Enter a contest</h3>
<div class="field"><label for="ct_c">Contest</label><select id="ct_c" name="contest"><option>Redbud Season Photo Contest</option><option>Best Small Business Pitch</option></select></div>
<div class="field"><label for="ct_link">Link to your photo / pitch (Drive, Dropbox, etc.)</label><input id="ct_link" name="entry_link" type="url" placeholder="https://" required></div>
<div class="field"><label for="ct_desc">Title / short description</label><textarea id="ct_desc" name="description" rows="3"></textarea></div>
<div class="row"><div class="field"><label for="ct_n">Name</label><input id="ct_n" name="name" required></div><div class="field"><label for="ct_e">Email</label><input id="ct_e" name="email" type="email" required></div></div>
<label class="check"><input type="checkbox" name="rules" value="accepted" required> I'm 18+, a U.S. resident, and I accept the official rules.</label>
<button class="btn btn-primary" type="submit" style="margin-top:12px">Submit entry →</button></form>
</div></section>
<section id="careers"><div class="wrap two">
<div class="prose"><h2>💼 Careers &amp; talent</h2><p>We hire locally and remotely, mostly freelance to start.</p>
<table><tr><th>Role</th><th>Type</th></tr><tr><td>Local correspondent (events, business news)</td><td>Freelance, per article</td></tr><tr><td>Photographer / videographer</td><td>Freelance, per shoot</td></tr><tr><td>Advertising sales rep</td><td>Commission</td></tr><tr><td>Web &amp; SEO contributor</td><td>Remote, project-based</td></tr><tr><td>Community ambassador</td><td>Volunteer / stipend</td></tr></table></div>
<form class="tool" data-fs="Careers application"><h3>Apply or join the talent pool</h3>
<div class="field"><label for="j_role">Role</label><select id="j_role" name="role"><option>Local correspondent</option><option>Photographer / videographer</option><option>Advertising sales rep</option><option>Web &amp; SEO contributor</option><option>Community ambassador</option><option>Other</option></select></div>
<div class="field"><label for="j_link">Portfolio / LinkedIn / résumé link</label><input id="j_link" name="portfolio" type="url" placeholder="https://"></div>
<div class="field"><label for="j_why">Why you?</label><textarea id="j_why" name="message" rows="3"></textarea></div>
<div class="row"><div class="field"><label for="j_n">Name</label><input id="j_n" name="name" required></div><div class="field"><label for="j_e">Email</label><input id="j_e" name="email" type="email" required></div></div>
<button class="btn btn-primary" type="submit">Apply →</button></form>
</div></section>
"""
page("support.html", "Support 62278.com — Donate, Contests & Prizes, Careers | 62278.com",
     "Support the independent 62278 guide: donate to operations and promotion, enter photo and business-pitch contests, sponsor prizes, or join our team.", support, "donate support contest prize careers jobs hiring volunteer")

# ======================= GUIDES =======================
guides = [
 ("moving-from-st-louis", "Moving from St. Louis to a Small Illinois Town: A Numbers-First Checklist", "Relocation",
  "Thinking about trading a St. Louis address for small-town Illinois? Here's the checklist for taxes, commute, housing, schools and lifestyle.",
  """<p>Every year, St. Louis-area households look across the river for more space and a lower price per square foot. Towns like Red Bud (ZIP 62278), about 36 miles southeast of the city, are a common destination. The move can be a great deal — if you run the numbers first.</p>
<h2>1. Price the commute honestly</h2><p>Downtown St. Louis is roughly 40 road miles from Red Bud. At 27 MPG and $3.10 a gallon, a five-day round-trip commute burns about $2,200 of fuel a year — and closer to $13,000 a year once wear, insurance and depreciation are counted at an all-in rate of about $0.70 per mile. Hybrid schedules change the maths dramatically: at two office days a week, that cost falls by 60%.</p>
<h2>2. Compare property tax, not just price</h2><p>Illinois property taxes are among the highest in the country as a share of home value. A cheaper house can still carry a tax bill similar to a pricier Missouri home. Ask for the last two tax bills on any listing and plug them into the <a href="../tools.html">mortgage calculator</a>.</p>
<h2>3. Check income tax and paycheck effects</h2><p>Illinois has a flat state income tax; Missouri's is graduated, and the City of St. Louis adds an earnings tax for residents and people who work in the city. If you keep a city job, you may still owe the city earnings tax. Confirm with a tax professional before you move.</p>
<h2>4. Housing: move fast, inspect carefully</h2><p>Redfin's 62278 data showed a median sale price around $200K in late 2025, with homes selling in about six to seven weeks. Older homes near downtown can need roofs, electrical and drainage work — budget an inspection plus a 10% repair cushion.</p>
<h2>5. Healthcare and schools</h2><p>Red Bud has a regional hospital for everyday and emergency care; major specialists remain in the St. Louis area. Visit the local schools in person and ask about class sizes, transportation and activities.</p>
<h2>6. Lifestyle: try before you buy</h2><p>Spend a weekday evening and a festival weekend in town. Small-town life is quieter, more community-centred and less anonymous — which some people love and others don't.</p>
<h2>Bottom line</h2><p>The move works best for remote or hybrid workers, families who want space, and buyers priced out of inner-ring suburbs. If you need a daily downtown commute and big-city nightlife, factor those costs in before you sign.</p>"""),
 ("small-town-site-selection", "How to Choose a Small-Town Industrial Site: 12 Questions to Ask First", "Business",
  "A practical checklist for evaluating small-town industrial and commercial lots: utilities, zoning, logistics, workforce, incentives and risk.",
  """<p>Small-town business parks can offer cheaper land, faster approvals and incentives that metro sites can't match. They also carry risks — thin labour pools, limited utilities and slower services. Use these twelve questions before you commit.</p>
<h2>Utilities &amp; infrastructure</h2><ol><li><b>Power:</b> What capacity is available at the lot line, and who provides it? Municipal utilities can sometimes move faster than investor-owned ones.</li><li><b>Water &amp; sewer:</b> Main sizes and treatment capacity matter for process water. A 10-inch water main and 8-inch sanitary sewer suit most light industry.</li><li><b>Gas:</b> Pressure and line size for heating and processes.</li><li><b>Broadband:</b> Is fibre at the lot, or only nearby?</li></ol>
<h2>Logistics</h2><ol start="5"><li><b>Highway access:</b> How many turns from your dock to a state or interstate route?</li><li><b>River, rail and air:</b> Is barge or rail access close enough to matter for your freight? A port dock five minutes away can cut bulk costs.</li><li><b>Trade zones:</b> Is the site inside a Foreign Trade Zone? FTZ status can defer or reduce duties on imported inputs.</li></ol>
<h2>People</h2><ol start="8"><li><b>Labour shed:</b> How many workers live within a 30-minute drive, and who else is hiring them?</li><li><b>Training:</b> Is there a community-college campus with programmes you can shape?</li></ol>
<h2>Money &amp; risk</h2><ol start="10"><li><b>Incentives:</b> Enterprise zones, sales-tax rebates on building materials, revolving loan funds and state grants can stack — get them in writing.</li><li><b>Zoning &amp; covenants:</b> Confirm permitted uses, setbacks, outdoor storage rules and noise limits.</li><li><b>Flood &amp; soil:</b> Pull flood maps and order a geotechnical report early.</li></ol>
<h2>Applying it to 62278</h2><p>The Red Bud Business Park is a useful test case: about 50 acres of light-industrial/commercial lots, utilities and fibre, location within FTZ 31, and a river-port dock nearby. Run the twelve questions against it and against two competing sites — the comparison is the decision. <a href="../business.html">Request site information</a>.</p>"""),
 ("buying-a-home-small-market", "Buying a Home in a Competitive Small Market: A Practical Playbook", "Homes",
  "How to win a house in a small, fast-rising market without overpaying: pre-approval, comps, offers, inspections and appraisal gaps.",
  """<p>Small markets behave differently from big ones. With only a handful of listings a month, a single sale can swing the median price, and a good house can draw several offers in a weekend. Here's how to compete without overpaying.</p>
<h2>Get fully pre-approved, not pre-qualified</h2><p>A pre-approval with income and assets verified tells a seller your financing is real. In a small town, sellers and agents often know local lenders by name — a local pre-approval can carry extra weight.</p>
<h2>Read comps like an appraiser</h2><p>When the market moves 20%+ in a year, last year's sales understate value and this month's headline median can overstate it. Ask your agent for the five closest sales in the last 90 days, adjusted for size, condition and lot.</p>
<h2>Write a clean offer</h2><ul><li>Offer a realistic closing date that suits the seller.</li><li>Keep the inspection contingency, but shorten the window.</li><li>Consider an appraisal-gap clause you can actually afford.</li><li>Include a short, genuine note if the seller is a long-time owner — it still matters in small towns.</li></ul>
<h2>Never skip the inspection</h2><p>Older Midwestern homes commonly hide foundation cracks, outdated wiring, aging furnaces and drainage issues. A $400–$600 inspection is the cheapest insurance you'll buy.</p>
<h2>Budget the whole payment</h2><p>Include Illinois property tax and homeowners insurance. Our <a href="../tools.html">mortgage calculator</a> estimates the full monthly cost, and the affordability tool compares your budget to the local median.</p>
<p><a href="../get-started.html?intent=buy">Get matched with a local agent →</a></p>"""),
 ("main-street-business-launch", "Launching a Main Street Business in a Small Town: Capital, Break-Even and Marketing", "Main Street",
  "A realistic guide to opening a storefront in a town of about 4,000 people: start-up capital, break-even maths and local marketing that works.",
  """<p>Main Street businesses thrive on loyalty and fail on maths. In a town of roughly 4,000 people, your customer base is your neighbours, the surrounding farms and visitors drawn by events. Plan accordingly.</p>
<h2>Size the market first</h2><p>A café in a 4,000-person town with 6,000 more in the ZIP area does not need to win everyone — it needs a few hundred regulars. Estimate how many of them you need, at what average ticket, to cover costs.</p>
<h2>Calculate launch capital</h2><p>Add build-out, equipment and opening inventory, then add six months of fixed costs as runway. Most closures come from running out of cash before regulars form, not from bad products. Our <a href="../business.html#startup">startup calculator</a> does this in seconds.</p>
<h2>Know your break-even</h2><p>Break-even sales per month = fixed monthly costs ÷ (average sale × gross margin). If that number requires more daily customers than the street sees, change the model before you sign a lease.</p>
<h2>Use the town's calendar</h2><p>Festival weekends — chocolate walks, Christmas walks, summer picnics — can deliver a month of foot traffic in two days. Plan inventory, staffing and promotions around them.</p>
<h2>Market like a local</h2><ul><li>Claim your free directory listing and your map profiles.</li><li>Sponsor a youth team or a community event.</li><li>Collect emails at the register; a weekly note beats paid ads in small towns.</li><li>Partner with neighbouring shops on joint promotions.</li></ul>
<h2>Find the money</h2><p>Ask the city about loan programmes and sales-tax rebate incentives, and talk to the Illinois Small Business Development Center network for free advising. <a href="../directory.html#list">List your business free →</a></p>"""),
]
gcards = ""
for slug, title, tag, desc, body in guides:
    art = f"""<section class="pagehead"><div class="wrap prose"><div class="breadcrumb"><a href="{{R}}index.html">Home</a> / <a href="{{R}}guides/index.html">Guides</a> / {tag}</div><span class="tag">{tag}</span><h1>{title}</h1><p class="src">By the 62278.com editorial team · Updated {TODAY}</p></div></section>
<section><div class="wrap two"><article class="prose">{body}
<p class="src" style="margin-top:2em">Information is general and for planning only; it is not legal, tax or financial advice.</p></article>
<aside><div class="tool"><h3>Need a local expert?</h3><p>Get matched with an agent, lender, contractor or business-site contact — free.</p><a class="btn btn-primary" href="{{R}}get-started.html">Get matched →</a></div>
<div class="ad-zone"><div class="ad-label">Advertisement</div></div>
<div class="tool"><h3>More guides</h3><ul class="prose">""" + "".join(f'<li><a href="{{R}}guides/{s}.html">{t}</a></li>' for s, t, *_ in guides if s != slug) + """</ul></div></aside></div></section>"""
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc, "dateModified": TODAY, "author": {"@type": "Organization", "name": BRAND}, "publisher": {"@type": "Organization", "name": BRAND}}) + "</script>"
    page(f"guides/{slug}.html", f"{title} | 62278.com", desc, art, tag.lower(), ld)
    gcards += f'<div class="card"><span class="tag">{tag}</span><h3>{title}</h3><p>{desc}</p><a class="more" href="{{R}}guides/{slug}.html">Read →</a></div>'
page("guides/index.html", "Guides — Relocation, Homes & Small Business in the 62278 Area | 62278.com",
     "In-depth guides on moving from St. Louis, buying in a competitive small market, choosing an industrial site and launching a Main Street business.",
     pagehead("Guides", "Long-form, numbers-first guides for movers, buyers and business owners.", "Guides") + f'<section><div class="wrap"><div class="cards">{gcards}</div></div></section>', "guides articles")

# ======================= ABOUT / CONTACT / LEGAL =======================
about = pagehead("About 62278.com", "An independent, numbers-first guide to ZIP 62278 and the countryside southeast of St. Louis.", "About") + """
<section><div class="wrap prose">
<h2>What we do</h2><p>62278.com helps people decide whether to live, buy or build in the 62278 area — Red Bud, Illinois and its surroundings — and connects them with local professionals when they're ready. We publish practical guides, free calculators, a local directory and an events calendar.</p>
<h2>Who we are</h2><p>An independent digital publisher. We are not a government body and have no affiliation with the City of Red Bud, Randolph County, the State of Illinois or the U.S. Postal Service.</p>
<h2 id="data">Data &amp; methodology</h2><ul><li><b>Population, income, home value:</b> U.S. Census Bureau American Community Survey 2023 5-year estimates for ZCTA 62278 (via Population Review); 2020 census for the city of Red Bud.</li><li><b>Home sale prices &amp; days on market:</b> Redfin 62278 housing market page (November 2025).</li><li><b>Business park, FTZ, logistics, incentives:</b> City of Red Bud economic development materials.</li><li><b>Cost-of-living index:</b> an estimate used for directional comparisons only.</li></ul>
<p>We refresh figures periodically. Spot something outdated? <a href="{R}contact.html">Tell us</a>.</p>
<h2>How we make money</h2><p>Display advertising (Google AdSense), sponsorships, featured listings and referral fees from partners. Editorial content is never paid for unless clearly labelled as sponsored.</p>
</div></section>"""
page("about.html", "About 62278.com — Independent Guide to Red Bud, IL & ZIP 62278", "Who runs 62278.com, how we source our data and how the site is funded.", about, "about methodology data")

contact = pagehead("Contact us", "Questions, corrections, story tips or partnership ideas — send a message and we'll reply within one business day.", "Contact") + """
<section><div class="wrap two">
<form class="tool" data-fs="Contact form"><h3>✉️ Send a message</h3>
<div class="row"><div class="field"><label for="ct_name">Name</label><input id="ct_name" name="name" required></div><div class="field"><label for="ct_mail">Email</label><input id="ct_mail" name="email" type="email" required></div></div>
<div class="field"><label for="ct_topic">Topic</label><select id="ct_topic" name="topic"><option>General question</option><option>Correction / data update</option><option>Story or video tip</option><option>Advertising</option><option>Partnership</option><option>Privacy request</option></select></div>
<div class="field"><label for="ct_msg">Message</label><textarea id="ct_msg" name="message" rows="5" required></textarea></div>
<button class="btn btn-primary" type="submit">Send →</button></form>
<div class="prose"><h2>Interested in this domain?</h2><p>For acquisition of 62278.com, sponsorship, advertising or partnership proposals, use our <a href="https://web.works/contact" target="_blank" rel="noopener">dedicated partnership contact page</a>.</p>
<h2>Official city services</h2><p>We can't process permits, utility bills or official requests. Please contact the relevant government office directly.</p></div>
</div></section>"""
page("contact.html", "Contact 62278.com", "Contact the 62278.com team for questions, corrections, tips, advertising and partnerships.", contact, "contact email message")

privacy = pagehead("Privacy policy", f"Last updated {TODAY}.", "Privacy") + """
<section><div class="wrap prose">
<h2>Information we collect</h2><p>When you submit a form we collect the details you enter (such as name, email, phone and your request). We also collect standard technical data (browser type, pages viewed, approximate location) through cookies and similar technologies.</p>
<h2>How we use it</h2><ul><li>To respond to your request and, with your consent, share it with up to three relevant local partners.</li><li>To send newsletters you've subscribed to (unsubscribe anytime).</li><li>To operate, secure and improve the site.</li></ul>
<h2>Form processing</h2><p>Forms are delivered by a third-party form-processing service, FormSubmit, which transmits your submission to us by email.</p>
<h2>Advertising &amp; Google AdSense</h2><p>Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and/or other sites on the Internet. You may opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">www.aboutads.info</a>. Learn how Google uses data at <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">policies.google.com/technologies/partner-sites</a>.</p>
<h2>Embedded content</h2><p>Video pages may load content from YouTube (in privacy-enhanced mode) only after you click play.</p>
<h2>Your rights</h2><p>You can request access, correction or deletion of your personal information via our <a href="{R}contact.html">contact form</a> (choose “Privacy request”). Residents of California, the EEA/UK and other regions may have additional rights under local law.</p>
<h2>Children</h2><p>This site is not directed to children under 13 and we do not knowingly collect their data.</p>
<h2>Changes</h2><p>We may update this policy; the date above shows the latest version.</p>
</div></section>"""
page("privacy.html", "Privacy Policy | 62278.com", "How 62278.com collects, uses and protects your information, including cookies, Google AdSense and form submissions.", privacy, "privacy cookies adsense gdpr ccpa")

terms = pagehead("Terms of use", f"Last updated {TODAY}.", "Terms") + """
<section><div class="wrap prose">
<h2>Use of the site</h2><p>By using 62278.com you agree to these terms. Content is provided for general information only and is not legal, financial, tax, real-estate or professional advice.</p>
<h2>Accuracy</h2><p>We cite public sources and update periodically, but figures may be outdated or estimated. Verify important information independently.</p>
<h2>Third parties &amp; referrals</h2><p>We may refer you to independent partners. We are not responsible for their services, and any agreement you make is between you and them. We may receive referral compensation.</p>
<h2>User submissions</h2><p>You keep ownership of content you submit (event listings, contest entries) and grant us a non-exclusive licence to display it on the site and in promotions. Don't submit content you don't have rights to.</p>
<h2>Contests</h2><p>Each contest is governed by its official rules on the Support page. No purchase necessary. Void where prohibited.</p>
<h2>Donations</h2><p>Donations support site operations and are not tax-deductible. Pledges are voluntary and non-binding until paid.</p>
<h2>Liability</h2><p>The site is provided “as is”. To the fullest extent permitted by law, we disclaim liability for losses arising from use of the site.</p>
<h2>Contact</h2><p>Questions? Use our <a href="{R}contact.html">contact form</a>.</p>
</div></section>"""
page("terms.html", "Terms of Use | 62278.com", "Terms governing use of 62278.com, including referrals, user submissions, contests and donations.", terms, "terms legal")

disc = pagehead("Trademark &amp; copyright disclosure", "Plain-English statement of what we do and don't claim.", "Disclosure") + """
<section><div class="wrap prose">
<h2>The number “62278”</h2><p>“62278” is a five-digit number and the U.S. ZIP Code assigned to Red Bud, Illinois. 62278.com uses it descriptively to identify the geographic area this site covers. We claim <b>no trademark rights</b> in the number 62278 and do not intend to suggest any connection with any business, product, part number or organisation that also uses this number.</p>
<h2>No affiliation</h2><p>62278.com is independent and is not affiliated with, sponsored by or endorsed by the City of Red Bud, the Red Bud Chamber of Commerce, Randolph County, the State of Illinois, the United States Postal Service, Redfin, the U.S. Census Bureau, YouTube or Google. ZIP Code™ is a trademark of the United States Postal Service. All other trademarks belong to their respective owners and are used only for identification.</p>
<h2>Our copyright</h2><p>Original text, design, calculators and code on this site © 62278.com. All rights reserved. You may quote brief excerpts with attribution and a link.</p>
<h2>Third-party content</h2><p>Statistics are facts drawn from cited public sources and summarised in our own words. Videos are embedded or linked from YouTube and remain the property of their creators. If you believe content on this site infringes your rights, send a notice through our <a href="{R}contact.html">contact form</a> (topic: “Correction”) identifying the material, and we will review and remove it promptly where appropriate.</p>
</div></section>"""
page("disclosure.html", "Trademark & Copyright Disclosure | 62278.com", "62278.com trademark and copyright disclosure: no claim to the number 62278, no government affiliation, and how to report concerns.", disc, "trademark copyright disclosure dmca")

ty = """<section class="pagehead"><div class="wrap" style="text-align:center"><div style="font-size:3rem">✅</div><h1>Thank you!</h1><p class="lead" style="margin:0 auto">Your <b id="tyForm">submission</b> was received. We reply within one business day.</p>
<div style="display:flex;gap:12px;justify-content:center;margin-top:22px;flex-wrap:wrap"><a class="btn btn-primary" href="{R}tools.html">Try our free calculators</a><a class="btn btn-ghost" href="{R}guides/index.html">Read the guides</a></div></div></section>"""
page("thank-you.html", "Thank You | 62278.com", "Your submission has been received.", ty, extra='<meta name="robots" content="noindex">')
nf = """<section class="pagehead"><div class="wrap" style="text-align:center"><h1>404 — page not found</h1><p class="lead" style="margin:0 auto">That page wandered off. Try the <a href="/62278-com/index.html">home page</a> or <a href="https://62278.com/">62278.com</a>.</p></div></section>"""
page("404.html", "Page Not Found | 62278.com", "Page not found.", nf, extra='<meta name="robots" content="noindex">')

# ---------- data, sitemap, misc ----------
os.makedirs(os.path.join(OUT, "data"), exist_ok=True)
json.dump(SEARCH, open(os.path.join(OUT, "data/search.json"), "w"), indent=1)
vp = os.path.join(OUT, "data/videos.json")
if not os.path.exists(vp):
    json.dump({"_how": "Add YouTube video IDs (the part after v=) to auto-embed them at the top of the Video Hub.",
               "videos": [{"id": "", "title": "Example: Red Bud walking tour", "note": "Creator name"}]}, open(vp, "w"), indent=1)
urls = "".join(f"<url><loc>{SITE}/{'' if p['u']=='index.html' else p['u']}</loc><lastmod>{TODAY}</lastmod></url>" for p in SEARCH)
open(os.path.join(OUT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /thank-you.html\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(OUT, "ads.txt"), "w").write("google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
json.dump({"name": "62278.com", "short_name": "62278", "start_url": "./index.html", "display": "standalone", "background_color": "#fbfaf8", "theme_color": "#c2185b",
           "icons": [{"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, open(os.path.join(OUT, "manifest.webmanifest"), "w"), indent=1)
json.dump({"last_refresh": datetime.datetime.now(datetime.timezone.utc).isoformat()}, open(os.path.join(OUT, "data/status.json"), "w"))
print("Built", len(SEARCH) + 2, "pages")
