/* 62287.com (OCCUR) core script */
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
    add("_subject", "62287.com — " + (f.getAttribute("data-fs") || "Form submission"));
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

  /* ---------- event budget split ---------- */
  var SPLITS = {
    wedding: [["Venue & rentals",.28],["Catering & bar",.30],["Photo & video",.11],["Music / DJ / band",.07],["Flowers & décor",.09],["Attire & beauty",.06],["Stationery & favours",.03],["Planner / coordinator",.03],["Contingency",.03]],
    corporate: [["Venue & AV",.32],["Catering & bar",.30],["Speakers / entertainment",.12],["Marketing & signage",.08],["Staffing & security",.06],["Travel & transport",.07],["Contingency",.05]],
    birthday: [["Venue / space",.25],["Food & cake",.35],["Entertainment",.15],["Décor & balloons",.12],["Invites & favours",.06],["Contingency",.07]],
    fundraiser: [["Venue",.25],["Catering",.30],["Auction / raffle prizes",.10],["AV & entertainment",.12],["Marketing",.10],["Staffing",.06],["Contingency",.07]]
  };
  if ($("#budget")) bind(["b_total","b_type","b_guests"], function () {
    var t = num("b_total"), g = Math.max(num("b_guests"), 1), rows = SPLITS[$("#b_type").value] || SPLITS.wedding;
    $("#b_out").innerHTML = '<b class="big">' + money(t / g) + ' per guest</b><table>' + rows.map(function (r) {
      return "<tr><td>" + r[0] + "</td><td>" + Math.round(r[1] * 100) + "%</td><td><b>" + money(t * r[1]) + "</b></td></tr>"; }).join("") +
      '</table><span class="src">Rule-of-thumb split for planning. Shift money toward what your guests will remember most.</span>';
  });
  /* ---------- catering & bar ---------- */
  if ($("#cater")) bind(["k_guests","k_food","k_drink","k_hours","k_svc"], function () {
    var g = num("k_guests"), food = g * num("k_food"), drinks = g * num("k_drink"), sub = food + drinks, svc = sub * num("k_svc") / 100;
    var servings = Math.ceil(g * (num("k_hours") + 1)), bottles = Math.ceil(servings / 5);
    $("#k_out").innerHTML = '<b class="big">' + money(sub + svc) + '</b>Food ' + money(food) + ' · Bar ' + money(drinks) + ' · Service &amp; gratuity ' + money(svc) +
      '<br>Plan ~<b>' + servings.toLocaleString() + ' drinks</b> (1 per guest per hour + 1) — about <b>' + bottles + '</b> bottles of wine-equivalent.';
  });
  /* ---------- seating & space ---------- */
  if ($("#seat")) bind(["s_guests","s_per","s_style"], function () {
    var g = num("s_guests"), tables = Math.ceil(g / Math.max(num("s_per"), 1)), sq = g * num("s_style");
    $("#s_out").innerHTML = '<b class="big">' + tables + ' tables</b>Space needed: about <b>' + Math.round(sq).toLocaleString() + ' sq ft</b> (' + Math.round(sq * 0.0929).toLocaleString() + ' m²) before stage, bar and dance floor.';
  });
  /* ---------- countdown & checklist ---------- */
  if ($("#countdown")) {
    var dIn = $("#t_date");
    if (dIn && !dIn.value) { var d0 = new Date(); d0.setMonth(d0.getMonth() + 6); dIn.value = d0.toISOString().slice(0, 10); }
    var steps = [[365,"Set budget, guest estimate and date window"],[300,"Book venue (and planner, if using one)"],[240,"Book photographer, caterer and music"],[180,"Send save-the-dates; book florist & rentals"],[120,"Finalise menu tasting & décor plan"],[60,"Send invitations; order cake & signage"],[30,"Confirm vendors, timeline and seating"],[14,"Final headcount to caterer"],[7,"Share run-of-show with every vendor"],[1,"Prep payments, tips and emergency kit"]];
    var draw = function () {
      var ev = new Date(dIn.value + "T12:00:00"), now = new Date(), left = Math.ceil((ev - now) / 864e5);
      if (isNaN(left)) return;
      $("#t_out").innerHTML = '<b class="big">' + (left >= 0 ? left + " days to go" : "Event date has passed") + '</b><table>' + steps.map(function (s) {
        var due = new Date(ev - s[0] * 864e5), late = due < now;
        return "<tr><td>" + due.toLocaleDateString("en-US",{month:"short",day:"numeric",year:"numeric"}) + "</td><td>" + (late ? "⚠️ " : "✅ ") + s[1] + "</td></tr>"; }).join("") + "</table>";
    };
    dIn.addEventListener("input", draw); draw();
  }
  /* ---------- event style quiz ---------- */
  var quiz = $("#fitquiz");
  if (quiz) quiz.addEventListener("change", function () {
    var v = $$("select", quiz).map(function (x) { return x.value; });
    var out = $("#fit_out");
    if (v.indexOf("") > -1) { out.innerHTML = "Answer all " + v.length + " questions to see your event style."; return; }
    var s = v.reduce(function (a, b) { return a + (+b); }, 0);
    var style = s >= 9 ? ["Grand celebration","Full-service venue, live band, planner. Book 10–12 months out."] : s >= 6 ? ["Stylish & social","Restaurant buyout or loft, DJ, food stations. Book 4–6 months out."] : ["Intimate & personal","Private dining room or backyard, curated menu, one great photographer. 6–10 weeks is enough."];
    out.innerHTML = '<b class="big">' + style[0] + '</b>' + style[1] + ' <a href="' + ROOT + 'get-started.html">Get matched with vendors →</a>';
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
