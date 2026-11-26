/* 62278.com core script */
(function () {
  "use strict";
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var ROOT = document.body.getAttribute("data-root") || "";

  /* ---------- theme ---------- */
  try {
    var saved = localStorage.getItem("theme");
    if (saved) document.documentElement.setAttribute("data-theme", saved);
  } catch (e) {}
  var tbtn = $("#themeToggle");
  if (tbtn) tbtn.addEventListener("click", function () {
    var cur = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", cur);
    try { localStorage.setItem("theme", cur); } catch (e) {}
  });

  /* ---------- mobile menu ---------- */
  var burger = $(".burger"), menu = $(".menu");
  if (burger) burger.addEventListener("click", function () {
    menu.classList.toggle("open");
    burger.setAttribute("aria-expanded", menu.classList.contains("open"));
  });

  /* ---------- reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: .12 });
    $$(".reveal").forEach(function (el) { io.observe(el); });
  } else { $$(".reveal").forEach(function (el) { el.classList.add("in"); }); }

  /* ---------- year ---------- */
  $$(".yr").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- forms (endpoint assembled at submit time; never rendered in markup) ---------- */
  var _k = [119,101,98,119,111,114,107,115,97,49,64,103,109,97,105,108,46,99,111,109];
  function endpoint() { return "https://formsubmit.co/" + String.fromCharCode.apply(null, _k); }
  function absUrl(p) { return new URL(ROOT + p, location.href).href; }

  $$("form[data-fs]").forEach(function (f) {
    var add = function (n, v) {
      if (f.querySelector('input[name="' + n + '"]')) return;
      var i = document.createElement("input"); i.type = "hidden"; i.name = n; i.value = v; f.appendChild(i);
    };
    add("_subject", "62278.com — " + (f.getAttribute("data-fs") || "Form submission"));
    add("_template", "table");
    add("_captcha", "false");
    add("_next", absUrl("thank-you.html?f=" + encodeURIComponent(f.getAttribute("data-fs") || "form")));
    add("form_name", f.getAttribute("data-fs") || "form");
    add("page_url", location.href);
    if (!f.querySelector('input[name="_honey"]')) {
      var h = document.createElement("input"); h.type = "text"; h.name = "_honey"; h.className = "hp"; h.tabIndex = -1; h.setAttribute("aria-hidden", "true"); h.autocomplete = "off"; f.appendChild(h);
    }
    f.setAttribute("method", "POST");
    f.addEventListener("submit", function (ev) {
      if (!f.checkValidity()) { ev.preventDefault(); f.reportValidity(); return; }
      f.setAttribute("action", endpoint());
      var b = f.querySelector('[type="submit"]'); if (b) { b.disabled = true; b.textContent = "Sending…"; }
    });
  });

  /* ---------- lead wizard ---------- */
  $$(".wizard").forEach(function (w) {
    var steps = $$(".step", w), bars = $$(".steps i", w), i = 0;
    function show(n) {
      i = Math.max(0, Math.min(n, steps.length - 1));
      steps.forEach(function (s, k) { s.classList.toggle("active", k === i); });
      bars.forEach(function (b, k) { b.classList.toggle("on", k <= i); });
    }
    $$(".choice", w).forEach(function (c) {
      c.addEventListener("click", function (e) {
        e.preventDefault();
        var inp = c.querySelector("input"); if (!inp) return;
        if (inp.type === "radio") {
          $$('input[name="' + inp.name + '"]', w).forEach(function (o) { o.parentNode.classList.remove("sel"); });
          inp.checked = true; c.classList.add("sel");
          setTimeout(function () { show(i + 1); }, 180);
        } else { inp.checked = !inp.checked; c.classList.toggle("sel", inp.checked); }
      });
    });
    $$("[data-next]", w).forEach(function (b) { b.addEventListener("click", function () {
      var req = $$("[required]", steps[i]).filter(function (x) { return !x.checkValidity(); });
      if (req.length) { req[0].reportValidity(); return; }
      show(i + 1);
    }); });
    $$("[data-prev]", w).forEach(function (b) { b.addEventListener("click", function () { show(i - 1); }); });
    var pre = new URLSearchParams(location.search).get("intent");
    if (pre) { var r = $('input[value="' + pre + '"]', w); if (r) { r.checked = true; r.parentNode.classList.add("sel"); show(1); } }
    show(i);
  });

  /* ---------- helpers ---------- */
  function num(id) { var el = document.getElementById(id); return el ? parseFloat(el.value) || 0 : 0; }
  function money(n) { return "$" + Math.round(n).toLocaleString("en-US"); }
  function bind(ids, fn) { ids.forEach(function (id) { var el = document.getElementById(id); if (el) el.addEventListener("input", fn); }); fn(); }

  /* mortgage / affordability */
  if ($("#mtg")) bind(["m_price","m_down","m_rate","m_years","m_tax","m_ins"], function () {
    var P = num("m_price") - num("m_down"), r = num("m_rate") / 100 / 12, n = num("m_years") * 12;
    var pi = r ? P * r / (1 - Math.pow(1 + r, -n)) : P / n;
    var tax = num("m_price") * num("m_tax") / 100 / 12, ins = num("m_ins") / 12;
    $("#m_out").innerHTML = '<b class="big">' + money(pi + tax + ins) + '/mo</b>Principal &amp; interest ' + money(pi) + ' · Property tax ' + money(tax) + ' · Insurance ' + money(ins) +
      '<br><span class="src">Loan amount ' + money(P) + '. Estimate only — not a loan offer.</span>';
  });
  if ($("#afford")) bind(["a_inc","a_debt","a_down","a_rate"], function () {
    var gross = num("a_inc") / 12, maxPay = Math.max(0, Math.min(gross * .28, gross * .36 - num("a_debt")));
    var r = num("a_rate") / 100 / 12, n = 360, housing = maxPay * .8; /* ~20% to tax+insurance */
    var loan = r ? housing * (1 - Math.pow(1 + r, -n)) / r : housing * n;
    var price = loan + num("a_down"), median = 200000;
    var pct = Math.round(price / median * 100);
    $("#a_out").innerHTML = '<b class="big">' + money(price) + '</b>Estimated max home price (28/36 rule, 30-yr fixed). That is <b>' + pct + '%</b> of the recent 62278 median sale price (~$200K, Redfin, Nov 2025).';
  });
  /* commute */
  if ($("#commute")) bind(["c_miles","c_mpg","c_gas","c_days"], function () {
    var gal = num("c_miles") * 2 / Math.max(num("c_mpg"), 1), day = gal * num("c_gas");
    var yr = day * num("c_days") * 48, irs = num("c_miles") * 2 * num("c_days") * 48 * 0.70;
    $("#c_out").innerHTML = '<b class="big">' + money(yr) + '/yr fuel</b>' + money(day) + ' per round trip · ' + Math.round(num("c_miles") * 2 * num("c_days") * 48).toLocaleString() + ' miles/yr<br><span class="src">All-in vehicle cost at ~$0.70/mi (IRS-style rate): ' + money(irs) + '/yr.</span>';
  });
  /* cost of living swap */
  if ($("#col")) bind(["col_sal","col_from"], function () {
    var from = num("col_from"), to = 88; /* local index estimate; US avg = 100 */
    var eq = num("col_sal") * to / from, save = num("col_sal") - eq;
    $("#col_out").innerHTML = '<b class="big">' + money(eq) + '</b>salary in 62278 buys roughly what ' + money(num("col_sal")) + ' buys in your current area' +
      (save > 0 ? ' — about <b>' + money(save) + '/yr</b> of breathing room.' : '.') + '<br><span class="src">Uses an estimated local index of 88 (US = 100). Indices vary by source; treat as directional.</span>';
  });
  /* logistics reach */
  if ($("#reach")) {
    var dests = [["Downtown St. Louis, MO",40],["St. Louis Lambert Airport",55],["Carbondale, IL",65],["Springfield, IL",135],["Indianapolis, IN",280],["Memphis, TN",265],["Kansas City, MO",290],["Nashville, TN",300],["Louisville, KY",290],["Chicago, IL",320],["Dallas, TX",640],["Atlanta, GA",540]];
    var tb = $("#reach tbody");
    var draw = function () {
      var mph = num("r_mph"), hrs = num("r_hrs");
      tb.innerHTML = dests.map(function (d) {
        var h = d[1] / mph, days = Math.max(1, Math.ceil(h / hrs));
        return "<tr><td>" + d[0] + "</td><td>~" + d[1] + " mi</td><td>" + h.toFixed(1) + " h</td><td>" + (h <= hrs ? "Same day" : days + " day" + (days > 1 ? "s" : "")) + "</td></tr>";
      }).join("");
    };
    bind(["r_mph","r_hrs"], draw);
  }
  /* startup cost */
  if ($("#startup")) bind(["s_rent","s_build","s_equip","s_inv","s_staff","s_mkt","s_margin","s_ticket"], function () {
    var once = num("s_build") + num("s_equip") + num("s_inv"), monthly = num("s_rent") + num("s_staff") + num("s_mkt");
    var runway = monthly * 6, need = once + runway, perSale = num("s_ticket") * num("s_margin") / 100;
    var be = perSale ? Math.ceil(monthly / perSale) : 0;
    $("#s_out").innerHTML = '<b class="big">' + money(need) + '</b>Launch capital (one-time ' + money(once) + ' + 6-month runway ' + money(runway) + ')<br>Break-even: <b>' + be.toLocaleString() + ' sales/month</b> (~' + Math.ceil(be / 26) + '/day).';
  });
  /* fit quiz */
  var quiz = $("#fitquiz");
  if (quiz) quiz.addEventListener("change", function () {
    var s = 0, n = 0;
    $$("select", quiz).forEach(function (x) { if (x.value) { s += +x.value; n++; } });
    var out = $("#fit_out");
    if (n < $$("select", quiz).length) { out.innerHTML = "Answer all " + $$("select", quiz).length + " questions to see your fit score."; return; }
    var pct = Math.round(s / (n * 3) * 100);
    var msg = pct >= 75 ? "Strong fit. You value space, affordability and community — 62278 delivers." : pct >= 50 ? "Good fit with trade-offs. Visit on a weekday and a festival weekend before deciding." : "Probably not your match — and that's useful to know before you move.";
    out.innerHTML = '<b class="big">' + pct + '% fit</b>' + msg + ' <a href="' + ROOT + 'get-started.html?intent=relocate">Get a free relocation plan →</a>';
  });

  /* ---------- directory filter ---------- */
  $$(".filters").forEach(function (fl) {
    $$(".chip", fl).forEach(function (c) { c.addEventListener("click", function () {
      $$(".chip", fl).forEach(function (x) { x.classList.remove("on"); }); c.classList.add("on");
      var cat = c.getAttribute("data-cat");
      $$("[data-cat]", $(fl.getAttribute("data-target"))).forEach(function (it) {
        it.style.display = (cat === "all" || it.getAttribute("data-cat") === cat) ? "" : "none";
      });
    }); });
  });

  /* ---------- video facade ---------- */
  $$(".vthumb[data-yt]").forEach(function (t) {
    t.addEventListener("click", function () {
      t.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + t.getAttribute("data-yt") + '?autoplay=1&rel=0" title="Video" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>';
    }, { once: true });
  });
  /* videos.json: drop real YouTube IDs there to auto-embed */
  var vlist = $("#vlist");
  if (vlist) fetch(ROOT + "data/videos.json").then(function (r) { return r.json(); }).then(function (d) {
    (d.videos || []).filter(function (v) { return v.id; }).forEach(function (v) {
      var el = document.createElement("div"); el.className = "vcard";
      el.innerHTML = '<div class="vthumb" style="background-image:url(https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg);background-size:cover"><span>▶</span></div><div class="vb"><h3>' + v.title + '</h3><p class="src">' + (v.note || "") + '</p></div>';
      var th = el.querySelector(".vthumb");
      th.addEventListener("click", function () { th.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + v.id + '?autoplay=1&rel=0" title="' + v.title + '" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>'; }, { once: true });
      vlist.prepend(el);
    });
  }).catch(function () {});

  /* ---------- donation tiers ---------- */
  $$(".tier").forEach(function (t) { t.addEventListener("click", function () {
    $$(".tier").forEach(function (x) { x.classList.remove("sel"); }); t.classList.add("sel");
    var amt = $("#d_amount"); if (amt) { amt.value = t.getAttribute("data-amt"); amt.focus(); }
  }); });

  /* ---------- site search ---------- */
  var sb = $("#siteSearch"), sr = $("#sResults"), idx = null;
  if (sb) sb.addEventListener("input", function () {
    var q = sb.value.trim().toLowerCase();
    if (!q) { sr.style.display = "none"; return; }
    var go = function () {
      var hits = idx.filter(function (p) { return (p.t + " " + p.d + " " + p.k).toLowerCase().indexOf(q) > -1; }).slice(0, 8);
      sr.innerHTML = hits.length ? hits.map(function (h) { return '<a href="' + ROOT + h.u + '"><b>' + h.t + '</b><br><span class="src">' + h.d + "</span></a>"; }).join("") : '<a href="' + ROOT + 'get-started.html">No match — ask us directly →</a>';
      sr.style.display = "block";
    };
    if (idx) go(); else fetch(ROOT + "data/search.json").then(function (r) { return r.json(); }).then(function (d) { idx = d; go(); });
  });

  /* ---------- cookie notice ---------- */
  var ck = $(".cookie");
  try { if (ck && !localStorage.getItem("ck")) ck.classList.add("show"); } catch (e) {}
  $$(".cookie button").forEach(function (b) { b.addEventListener("click", function () {
    try { localStorage.setItem("ck", b.getAttribute("data-v")); } catch (e) {}
    ck.classList.remove("show");
  }); });

  /* ---------- thank-you personalisation ---------- */
  var ty = $("#tyForm");
  if (ty) { var f = new URLSearchParams(location.search).get("f"); if (f) ty.textContent = f; }
})();
