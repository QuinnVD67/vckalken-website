/* ============================================================
   VC Kalken — site interactions (v16)
   ============================================================ */
(function () {
  "use strict";

  /* ---------------- Site search ---------------- */
  const pages = [
    { title: "Home", url: "index.html", keywords: "home start" },
    {
      title: "Ploegen",
      url: "ploegen.html",
      keywords: "ploegen teams overzicht",
    },
    {
      title: "Kalender",
      url: "kalender.html",
      keywords: "kalender wedstrijden agenda",
    },
    {
      title: "Nieuws",
      url: "nieuws.html",
      keywords: "nieuws updates berichten",
    },
    { title: "Club", url: "club.html", keywords: "club identiteit over" },
    {
      title: "Clubkledij",
      url: "clubkledij.html",
      keywords: "clubkledij shop kledij twizzit",
    },
    {
      title: "Unkerzak",
      url: "unkerzak.html",
      keywords: "unkerzak activiteit",
    },
    {
      title: "Verzekering",
      url: "verzekering.html",
      keywords: "verzekering ongeval ongevalsaangifte blessure formulier",
    },
    {
      title: "Fotoalbums",
      url: "fotos.html",
      keywords: "fotoalbums foto's beelden",
    },
    {
      title: "Contact",
      url: "contact.html",
      keywords: "contact aanvraag mail",
    },
    {
      title: "Word lid",
      url: "word-lid.html",
      keywords: "word lid proeftraining inschrijven",
    },
    { title: "Sponsors", url: "sponsors.html", keywords: "sponsors partners" },
    { title: "Heren A", url: "heren-a.html", keywords: "heren a nationale 3" },
    { title: "Heren B", url: "heren-b.html", keywords: "heren b promo 2" },
    { title: "Heren C", url: "heren-c.html", keywords: "heren c promo 3a" },
    {
      title: "Heren Vobog",
      url: "heren-vobog.html",
      keywords: "heren vobog recreatie",
    },
    { title: "Dames A", url: "dames-a.html", keywords: "dames a" },
    { title: "Dames B", url: "dames-b.html", keywords: "dames b" },
    { title: "Dames C", url: "dames-c.html", keywords: "dames c" },
    {
      title: "Dames Vobog",
      url: "dames-vobog.html",
      keywords: "dames vobog recreatie",
    },
    {
      title: "Volleybalschool",
      url: "volleybalschool.html",
      keywords: "volleybalschool jeugd start",
    },
    {
      title: "Gemengd A U11",
      url: "gemengd-a-u11.html",
      keywords: "gemengd a u11 jeugd",
    },
    {
      title: "Gemengd B U11",
      url: "gemengd-b-u11.html",
      keywords: "gemengd b u11 jeugd",
    },
    {
      title: "Gemengd U11 2",
      url: "gemengd-u11-2.html",
      keywords: "gemengd u11 2 jeugd",
    },
    {
      title: "Gemengd U13",
      url: "gemengd-u13.html",
      keywords: "gemengd u13 jeugd",
    },
    {
      title: "Meisjes U13",
      url: "meisjes-u13.html",
      keywords: "meisjes u13 jeugd",
    },
    {
      title: "Jongens U15 A",
      url: "jongens-u15-a.html",
      keywords: "jongens u15 a jeugd",
    },
    {
      title: "Jongens U15 B",
      url: "jongens-u15-b.html",
      keywords: "jongens u15 b jeugd",
    },
    {
      title: "Meisjes U15 A",
      url: "meisjes-u15-a.html",
      keywords: "meisjes u15 a jeugd",
    },
    {
      title: "Meisjes U15 B",
      url: "meisjes-u15-b.html",
      keywords: "meisjes u15 b jeugd",
    },
    {
      title: "Meisjes U17 A",
      url: "meisjes-u17-a.html",
      keywords: "meisjes u17 a jeugd",
    },
    {
      title: "Meisjes U17 B",
      url: "meisjes-u17-b.html",
      keywords: "meisjes u17 b jeugd",
    },
  ];
  function score(q, t) {
    q = q.toLowerCase().trim();
    t = t.toLowerCase();
    if (!q) return 0;
    if (t.includes(q)) return 100 - q.length;
    let s = 0,
      qi = 0;
    for (const ch of t) {
      if (ch === q[qi]) {
        s += 5;
        qi++;
      }
    }
    return qi === q.length ? s : 0;
  }
  const input = document.getElementById("siteSearch");
  const results = document.getElementById("searchResults");
  if (input && results) {
    input.addEventListener("input", () => {
      const q = input.value;
      const found = pages
        .map((p) => ({ ...p, s: score(q, p.title + " " + p.keywords) }))
        .filter((p) => p.s > 0)
        .sort((a, b) => b.s - a.s)
        .slice(0, 6);
      results.innerHTML = found
        .map(
          (p) =>
            `<a href="${p.url}"><strong>${p.title}</strong><br><small>Ga naar pagina</small></a>`,
        )
        .join("");
      results.style.display = found.length ? "block" : "none";
    });
    // Enter opent het eerste resultaat, Escape sluit de resultatenlijst
    input.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        const first = results.querySelector("a");
        if (first) {
          e.preventDefault();
          window.location.href = first.getAttribute("href");
        }
      } else if (e.key === "Escape") {
        results.style.display = "none";
        input.blur();
      }
    });
    document.addEventListener("click", (e) => {
      if (!e.target.closest(".search-wrap")) results.style.display = "none";
    });
  }

  /* ---------------- Mobile nav ---------------- */
  const navToggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".main-nav");
  if (navToggle && nav) {
    navToggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
      navToggle.setAttribute(
        "aria-label",
        open ? "Menu sluiten" : "Menu openen",
      );
    });
    // Sluit het mobiele menu met Escape
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.setAttribute("aria-label", "Menu openen");
        navToggle.focus();
      }
    });
  }

  /* ---------------- Sticky header shadow ---------------- */
  const header = document.querySelector(".site-header");
  if (header) {
    const onScroll = () =>
      header.classList.toggle("scrolled", window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------------- Scroll reveal ---------------- */
  const reveals = document.querySelectorAll(".reveal");
  if (reveals.length) {
    if ("IntersectionObserver" in window) {
      const io = new IntersectionObserver(
        (entries) => {
          entries.forEach((en) => {
            if (en.isIntersecting) {
              en.target.classList.add("in");
              io.unobserve(en.target);
            }
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px -40px 0px" },
      );
      reveals.forEach((el) => io.observe(el));
    } else {
      reveals.forEach((el) => el.classList.add("in"));
    }
  }

  /* ---------------- Animated counters ---------------- */
  const counters = document.querySelectorAll("[data-count]");
  function animateCount(el) {
    const target = parseFloat(el.getAttribute("data-count"));
    const pre = el.getAttribute("data-prefix") || "";
    const suf = el.getAttribute("data-suffix") || "";
    if (
      window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches
    ) {
      el.textContent = pre + target + suf;
      return;
    }
    const dur = 1100;
    const start = performance.now();
    function tick(now) {
      const p = Math.min((now - start) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = pre + Math.round(target * eased) + suf;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  if (counters.length && "IntersectionObserver" in window) {
    const co = new IntersectionObserver(
      (entries) => {
        entries.forEach((en) => {
          if (en.isIntersecting) {
            animateCount(en.target);
            co.unobserve(en.target);
          }
        });
      },
      { threshold: 0.5 },
    );
    counters.forEach((c) => co.observe(c));
  }

  /* ---------------- Back to top ---------------- */
  const toTop = document.querySelector(".to-top");
  if (toTop) {
    const tog = () => toTop.classList.toggle("show", window.scrollY > 600);
    tog();
    window.addEventListener("scroll", tog, { passive: true });
    toTop.addEventListener("click", () =>
      window.scrollTo({ top: 0, behavior: "smooth" }),
    );
  }

  /* ---------------- Lightbox ---------------- */
  const lb = document.getElementById("lightbox");
  if (lb) {
    const lbImg = lb.querySelector("img");
    const open = (src, alt) => {
      lbImg.src = src;
      lbImg.alt = alt || "";
      lb.classList.add("open");
      document.body.style.overflow = "hidden";
    };
    const close = () => {
      lb.classList.remove("open");
      document.body.style.overflow = "";
      lbImg.src = "";
    };
    document.querySelectorAll("[data-lightbox]").forEach((im) => {
      im.style.cursor = "zoom-in";
      im.addEventListener("click", () => open(im.currentSrc || im.src, im.alt));
    });
    lb.addEventListener("click", (e) => {
      if (e.target === lb || e.target.classList.contains("close")) close();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") close();
    });
  }

  /* ---------------- Calendar ----------------
     Per-team usable calendar. Echte wedstrijden staan in realMatches;
     voor elke ploeg is er altijd minstens één kaart met de Volleyscores-link,
     zodat filteren per ploeg altijd een resultaat geeft. Vervang gerust de
     'Te koppelen'-kaarten door echte wedstrijden of een ploeg-specifieke
     Volleyscores-URL (veld url).                                            */
  // === Officiële VC Kalken kalenders op Volleyscores ========================
  // Per ploeg de eigen Volleyscores-kalender (door de club aangeleverd). Zo
  // moeten ouders enkel op de Kalken-pagina kijken: kies je ploeg, klik door
  // naar de live kalender en filter daar op thuis/uit. Nieuwe ploeg of nieuw
  // seizoen? Pas gewoon de juiste regel hieronder aan.
  const VS = "https://www.volleyscores.be/direct/O-1464"; // browseable Volleyscores-pagina van VC Kalken
  // Let op: TEAM_URL hieronder zijn .ics-agendafeeds (voor smartphone-/Google-
  // agenda-synchronisatie), GEEN webpagina's. Ze worden niet meer gebruikt voor
  // de "Open Volleyscores"-knop (die opent altijd de browseable clubpagina VS),
  // maar blijven staan als bron voor een eventuele "voeg toe aan agenda"-knop.
  const TEAM_URL = {
    "heren-a": "https://www.volleyscores.be/calendar/team/105856", // NAT3H-A
    "heren-b": "https://www.volleyscores.be/calendar/team/102358", // OHP2
    "heren-c": "https://www.volleyscores.be/calendar/team/102360", // OHP3A
    "dames-a": "https://www.volleyscores.be/calendar/team/102361", // ODP1
    "dames-b": "https://www.volleyscores.be/calendar/team/102362", // ODP3A
    "dames-c": "https://www.volleyscores.be/calendar/team/102363", // ODP4B
    "meisjes-u17-a": "https://www.volleyscores.be/calendar/team/102373", // OMU17 A
    "meisjes-u17-b": "https://www.volleyscores.be/calendar/team/102374", // OMU17 B
    "meisjes-u15-a": "https://www.volleyscores.be/calendar/team/102371", // OMU15 A
    "meisjes-u15-b": "https://www.volleyscores.be/calendar/team/102372", // OMU15 B
    "meisjes-u13": "https://www.volleyscores.be/calendar/team/102370", // OMU13
    "jongens-u15-a": "https://www.volleyscores.be/calendar/team/102368", // OJU15
    "gemengd-u13": "https://www.volleyscores.be/calendar/team/102367", // OJU13
    "jongens-u17": "https://www.volleyscores.be/calendar/team/102369", // OJU17/U19
  };
  const teamUrl = (s) => VS; // "Open Volleyscores" wijst altijd naar de browseable clubpagina
  // Wedstrijden komen uit data/matches.js. Dat bestand wordt automatisch
  // bijgewerkt door tools/update_matches.py (zie tools/README.md).
  const DATA = window.VCK_DATA || { updated: "", matches: [] };
  const realMatches = (DATA.matches || [])
    .slice()
    .sort((a, b) => (a.iso || "").localeCompare(b.iso || ""));
  const MATCH_MS = 3 * 60 * 60 * 1000; // een wedstrijd telt 3u na de start als 'gespeeld'
  const startOf = (m) => new Date(m.iso || "");
  const isPast = (m) => startOf(m).getTime() + MATCH_MS < Date.now();
  // Alle ploegen (slug, naam, categorie, reeks) — gebruikt voor de "open live kalender"-kaarten.
  const teamDefs = [
    { slug: "heren-b", name: "Heren B", cat: "heren", league: "Promo 2" },
    { slug: "heren-c", name: "Heren C", cat: "heren", league: "Promo 3A" },
    { slug: "heren-vobog", name: "Heren Vobog", cat: "heren", league: "Vobog" },
    { slug: "dames-a", name: "Dames A", cat: "dames", league: "Promo 1" },
    { slug: "dames-b", name: "Dames B", cat: "dames", league: "Promo 3A" },
    { slug: "dames-c", name: "Dames C", cat: "dames", league: "Promo 4B" },
    { slug: "dames-vobog", name: "Dames Vobog", cat: "dames", league: "Vobog" },
    {
      slug: "volleybalschool",
      name: "Volleybalschool",
      cat: "jeugd",
      league: "Startwerking",
    },
    {
      slug: "gemengd-a-u11",
      name: "Gemengd A U11",
      cat: "jeugd",
      league: "U11",
    },
    {
      slug: "gemengd-b-u11",
      name: "Gemengd B U11",
      cat: "jeugd",
      league: "U11",
    },
    {
      slug: "gemengd-u11-2",
      name: "Gemengd U11 2",
      cat: "jeugd",
      league: "U11",
    },
    { slug: "gemengd-u13", name: "Gemengd U13", cat: "jeugd", league: "U13" },
    { slug: "meisjes-u13", name: "Meisjes U13", cat: "jeugd", league: "U13" },
    {
      slug: "jongens-u15-a",
      name: "Jongens U15 A",
      cat: "jeugd",
      league: "U15",
    },
    {
      slug: "jongens-u15-b",
      name: "Jongens U15 B",
      cat: "jeugd",
      league: "U15",
    },
    {
      slug: "jongens-u17",
      name: "Jongens U17",
      cat: "jeugd",
      league: "U17/U19",
    },
    {
      slug: "meisjes-u15-a",
      name: "Meisjes U15 A",
      cat: "jeugd",
      league: "U15",
    },
    {
      slug: "meisjes-u15-b",
      name: "Meisjes U15 B",
      cat: "jeugd",
      league: "U15",
    },
    {
      slug: "meisjes-u17-a",
      name: "Meisjes U17 A",
      cat: "jeugd",
      league: "U17",
    },
    {
      slug: "meisjes-u17-b",
      name: "Meisjes U17 B",
      cat: "jeugd",
      league: "U17",
    },
  ];
  const teamsWithData = new Set(realMatches.map((m) => m.team));
  const linkCards = teamDefs
    .filter((t) => !teamsWithData.has(t.slug))
    .map((t) => {
      const own = Object.prototype.hasOwnProperty.call(TEAM_URL, t.slug);
      return {
        date: own ? "Volledige kalender" : "Te koppelen",
        time: "Via Volleyscores",
        team: t.slug,
        cat: t.cat,
        home: t.name,
        away: own
          ? "Bekijk alle wedstrijden + thuis/uit op Volleyscores"
          : "Open de live kalender op Volleyscores.be",
        hall: "Officiële VC Kalken-kalender",
        league: t.league,
        number: "",
        loc: "neutral",
        url: VS,
        link: true,
      };
    });
  const matches = realMatches.concat(linkCards);
  function renderMatches() {
    const box = document.querySelector("#matches");
    if (!box) return;
    const team = (document.querySelector("#teamFilter") || {}).value || "";
    const cat = (document.querySelector("#catFilter") || {}).value || "";
    const loc = (document.querySelector("#locFilter") || {}).value || "";
    const period =
      (document.querySelector("#periodFilter") || {}).value || "upcoming";
    const q = (
      (document.querySelector("#searchMatch") || {}).value || ""
    ).toLowerCase();
    const filtered = matches.filter(
      (m) =>
        (!team || m.team === team) &&
        (!cat || m.cat === cat) &&
        (!loc || m.loc === loc) &&
        (m.link ||
          period === "all" ||
          (period === "past" ? isPast(m) : !isPast(m))) &&
        `${m.home} ${m.away} ${m.hall} ${m.league} ${m.number}`
          .toLowerCase()
          .includes(q),
    );
    if (period === "past")
      filtered.sort(
        (a, b) =>
          (b.iso || "").localeCompare(a.iso || "") ||
          (a.link ? 1 : 0) - (b.link ? 1 : 0),
      );
    const count = document.querySelector("#matchCount");
    const real = filtered.filter((m) => !m.link).length;
    if (count) count.textContent = `${real} wedstrijd(en) gevonden`;
    box.innerHTML =
      filtered
        .map((m) => {
          const tag = m.cancelled
            ? "Afgelast"
            : m.loc === "home"
              ? "Thuis"
              : m.loc === "away"
                ? "Uit"
                : "Link";
          const sub = m.number || (m.link ? "Volleyscores" : "");
          return `<article class="match ${m.loc}${m.cancelled ? " cancelled" : ""}"><div class="date">${m.date}<small>${m.time}</small><div class="league">${sub}</div></div><div class="teams">${m.home}<small>tegen / info</small>${m.away}<small>${m.hall}</small><div class="league">${m.league}</div></div><span class="tag">${tag}</span><a class="btn vs-link" target="_blank" rel="noopener" href="${m.url}">Open Volleyscores</a></article>`;
        })
        .join("") ||
      '<div class="empty-state">Geen wedstrijden gevonden met deze filters.</div>';
    const note = document.querySelector("#dataUpdated");
    if (note && DATA.updated) {
      const d = new Date(DATA.updated);
      if (!isNaN(d))
        note.textContent =
          "Kalender laatst aangepast op " +
          d.toLocaleString("nl-BE", {
            day: "numeric",
            month: "long",
            hour: "2-digit",
            minute: "2-digit",
          }) +
          ".";
    }
  }
  [
    "teamFilter",
    "catFilter",
    "locFilter",
    "periodFilter",
    "searchMatch",
  ].forEach((id) => {
    const el = document.querySelector("#" + id);
    if (el)
      el.addEventListener("input", () => {
        renderMatches();
        syncLocToggle();
      });
  });

  // Prominente Thuis/Uit-snelknoppen (gekoppeld aan het locFilter-keuzemenu)
  const locToggle = document.getElementById("locToggle");
  function syncLocToggle() {
    if (!locToggle) return;
    const cur = (document.querySelector("#locFilter") || {}).value || "";
    locToggle
      .querySelectorAll("button")
      .forEach((b) =>
        b.classList.toggle("active", (b.dataset.loc || "") === cur),
      );
  }
  if (locToggle) {
    locToggle.addEventListener("click", (e) => {
      const btn = e.target.closest("button");
      if (!btn) return;
      const lf = document.querySelector("#locFilter");
      if (lf) lf.value = btn.dataset.loc || "";
      renderMatches();
      syncLocToggle();
    });
  }

  // Deep links: kalender.html?team=heren-a&cat=heren&loc=home
  if (document.querySelector("#matches")) {
    const cp = new URLSearchParams(location.search);
    [
      ["team", "#teamFilter"],
      ["cat", "#catFilter"],
      ["loc", "#locFilter"],
    ].forEach(([k, sel]) => {
      const v = cp.get(k),
        el = document.querySelector(sel);
      if (v && el) el.value = v;
    });
  }
  renderMatches();
  syncLocToggle();

  /* ---------------- "Wedstrijden deze week" widget (homepage) ---------------- */
  function parseDMY(d) {
    const [dd, mm, yyyy] = d.split("/").map(Number);
    return new Date(yyyy, mm - 1, dd);
  }
  function renderWeekWidget() {
    const box = document.querySelector("#week-matches");
    if (!box) return;
    const now = new Date();
    const offset = (now.getDay() + 6) % 7; // 0 = maandag
    const monday = new Date(
      now.getFullYear(),
      now.getMonth(),
      now.getDate() - offset,
    );
    const sunday = new Date(
      monday.getFullYear(),
      monday.getMonth(),
      monday.getDate() + 6,
      23,
      59,
      59,
    );
    const weekMatches = realMatches
      .map((m) => ({ ...m, _d: parseDMY(m.date) }))
      .filter((m) => m._d >= monday && m._d <= sunday)
      .sort((a, b) => a._d - b._d || a.time.localeCompare(b.time));
    if (!weekMatches.length) {
      box.innerHTML =
        '<div class="empty-state">Deze week staan er geen wedstrijden gepland. <a href="kalender.html">Bekijk de volledige kalender →</a></div>';
      return;
    }
    box.innerHTML = weekMatches
      .map(
        (m) =>
          `<article class="match ${m.loc}${m.cancelled ? " cancelled" : ""}"><div class="date">${m.date.slice(0, 5)}<small>${m.time}</small></div><div class="teams">${m.home} <span class="vs">–</span> ${m.away}<div class="league">${m.league}${m.hall ? " · " + m.hall : ""}</div></div><span class="tag">${m.cancelled ? "Afgelast" : m.loc === "home" ? "Thuis" : "Uit"}</span></article>`,
      )
      .join("");
  }
  renderWeekWidget();

  /* ---------------- Word-lid form (clubForm) ---------------- */
  const clubForm = document.getElementById("clubForm");
  function buildClubMail() {
    if (!clubForm) return "";
    const d = Object.fromEntries(new FormData(clubForm).entries());
    return `==================================================
NIEUWE AANVRAAG VIA VCKALKEN.BE
==================================================

PERSOONLIJKE GEGEVENS
--------------------------------------------------
Naam speler: ${d.naam || "-"}
Geboortedatum: ${d.geboorte || "-"}

CONTACTGEGEVENS
--------------------------------------------------
E-mail: ${d.email || "-"}
Telefoon: ${d.telefoon || "-"}

INTERESSE
--------------------------------------------------
Gewenste ploeg: ${d.ploeg || "-"}
Volleybalervaring: ${d.ervaring || "-"}

BOODSCHAP
--------------------------------------------------
${d.boodschap || "-"}

==================================================
Automatisch opgesteld via www.vckalken.be
==================================================`;
  }
  if (clubForm) {
    const prev = document.getElementById("mailPreview");
    clubForm.addEventListener("input", () => {
      if (prev) prev.textContent = buildClubMail();
    });
    clubForm.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!clubForm.reportValidity()) return;
      const d = Object.fromEntries(new FormData(clubForm).entries());
      const subject = encodeURIComponent(
        `Nieuwe aanvraag VC Kalken - ${d.ploeg || "ploeg onbekend"} - ${d.naam || "naam onbekend"}`,
      );
      const body = encodeURIComponent(buildClubMail());
      window.location.href = `mailto:info@vckalken.be?subject=${subject}&body=${body}`;
    });
  }

  /* ---------------- Contact form ---------------- */
  const contactForm = document.getElementById("contactForm");
  function buildContactMail() {
    if (!contactForm) return "";
    const d = Object.fromEntries(new FormData(contactForm).entries());
    const msg = `==================================================
NIEUW BERICHT VIA VCKALKEN.BE
==================================================

TYPE AANVRAAG
--------------------------------------------------
${d.type || "-"}

PERSOONLIJKE GEGEVENS
--------------------------------------------------
Naam: ${d.naam || "-"}
E-mail: ${d.email || "-"}
Telefoon: ${d.telefoon || "-"}
Geboortedatum / geboortejaar: ${d.leeftijd || "-"}

PLOEG OF ONDERWERP
--------------------------------------------------
${d.ploeg || "-"}

BERICHT
--------------------------------------------------
${d.bericht || "-"}

==================================================
Automatisch opgesteld via www.vckalken.be
==================================================`;
    const prev = document.getElementById("mailPreview");
    if (prev) prev.textContent = msg;
    return msg;
  }
  if (contactForm) {
    // Preselect type from ?type= query (e.g. contact.html?type=kalender)
    const params = new URLSearchParams(location.search);
    const tmap = {
      kalender: "Vraag over kalender",
      clubkledij: "Vraag over clubkledij",
      sponsor: "Algemene vraag",
      proeftraining: "Proeftraining aanvragen",
    };
    const want = tmap[params.get("type")];
    if (want) {
      const sel = contactForm.querySelector('select[name="type"]');
      if (sel)
        Array.from(sel.options).forEach((o) => {
          if (o.value === want) sel.value = want;
        });
    }
    contactForm.addEventListener("input", buildContactMail);
    buildContactMail();

    // Quick-reason cards: preselect the request type + scroll to the form
    const typeSel = contactForm.querySelector('select[name="type"]');
    document.querySelectorAll(".reason-card").forEach((card) => {
      card.addEventListener("click", () => {
        const r = card.dataset.reason;
        if (typeSel && r) {
          Array.from(typeSel.options).forEach((o) => {
            if (o.value === r) typeSel.value = r;
          });
          buildContactMail();
        }
        document
          .querySelectorAll(".reason-card")
          .forEach((c) => c.classList.remove("sel"));
        card.classList.add("sel");
        contactForm.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });

    contactForm.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!contactForm.reportValidity()) return;
      const d = Object.fromEntries(new FormData(contactForm).entries());
      const subject = encodeURIComponent(
        `VC Kalken - ${d.type || "aanvraag"} - ${d.ploeg || "algemeen"}`,
      );
      const body = encodeURIComponent(buildContactMail());
      const confirm = document.getElementById("contactConfirm");
      if (confirm) confirm.hidden = false;
      window.location.href = `mailto:info@vckalken.be?subject=${subject}&body=${body}`;
    });
  }

  /* ---------------- Verzekering / ongeval melden ---------------- */
  const insForm = document.getElementById("verzekeringForm");
  function buildInsMail() {
    if (!insForm) return "";
    const d = Object.fromEntries(new FormData(insForm).entries());
    const msg = `==================================================
ONGEVALMELDING VIA VCKALKEN.BE
==================================================

SPELER
--------------------------------------------------
Naam: ${d.naam || "-"}
Ploeg: ${d.ploeg || "-"}

CONTACT
--------------------------------------------------
E-mail: ${d.email || "-"}
Telefoon: ${d.telefoon || "-"}

ONGEVAL
--------------------------------------------------
Datum: ${d.datum || "-"}
Omschrijving:
${d.omschrijving || "-"}

==================================================
Automatisch opgesteld via www.vckalken.be
==================================================`;
    const prev = document.getElementById("mailPreview");
    if (prev) prev.textContent = msg;
    return msg;
  }
  if (insForm) {
    insForm.addEventListener("input", buildInsMail);
    buildInsMail();
    insForm.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!insForm.reportValidity()) return;
      const d = Object.fromEntries(new FormData(insForm).entries());
      const subject = encodeURIComponent(
        `Ongevalmelding VC Kalken - ${d.naam || "naam onbekend"} - ${d.ploeg || "ploeg onbekend"}`,
      );
      const body = encodeURIComponent(buildInsMail());
      const confirm = document.getElementById("contactConfirm");
      if (confirm) confirm.hidden = false;
      window.location.href = `mailto:info@vckalken.be?subject=${subject}&body=${body}`;
    });
  }

  /* ---------------- Nieuws: uitvergrote weergave ----------------
     Klik op een nieuwstegel opent een groot venster met de volledige
     tekst, overgenomen van de originele clubsite (vckalken.be).      */
  const NEWS_ARTICLES = {
    1: {
      cat: "Evenement · 22/08/2026",
      title: "BBQ met Sparta Laarne",
      img: "assets/img/news-1.jpg",
      html: `<p>Stavros, de uitbater van de cafetaria in de sporthal, organiseert op zaterdag 22 augustus een grote barbecue. De opbrengst gaat volledig naar de jeugdwerking van VC Kalken en basketbalclub Sparta Laarne — als club zetten we onze schouders graag mee onder dit initiatief.</p>
<ul><li>Volwassenen: € 30 (3 vlees · 1 vis · koud buffet)</li><li>Kinderen tot 12 jaar: € 15</li><li>Vanaf 17u in Sporthal Laarne</li></ul>
<p>Samen sterk, samen aan 't vuur — iedereen welkom!</p>`,
    },
    2: {
      cat: "Jeugd · 4 april 2026",
      title: "Jongens U15 winnen de Oost-Vlaamse beker",
      img: "assets/img/news-2.jpg",
      html: `<p>Op zaterdag 4 april namen onze U15-jongens het in de finale van de beker van Oost-Vlaanderen op tegen Dakwerken De Vos Denderhoutem. Ze wonnen de spannende eerste set met 21-25. In set 2 trok Denderhoutem aan het langste eind met een duidelijke 25-13.</p>
<p>Toch lieten onze jongens het hoofd niet hangen en wonnen ze sets 3 en 4 met duidelijke cijfers.</p>
<ul><li>Uitslag: 1 - 3</li><li>Setstanden: 21/25 · 25/13 · 16/25 · 14/25</li></ul>
<p>Proficiat aan het team en de trainers!</p>`,
    },
    3: {
      cat: "Club · mei 2026",
      title: "50 jaar VC Kalken gevierd in stijl",
      img: "assets/img/news-3.jpg",
      html: `<p>Een halve eeuw volleybal in Kalken! In ons jubileumjaar trokken we alle registers open: op zaterdag 9 mei sloten we het feestjaar af met een groot eindeseizoensfeest in zaal Skala, samen met spelers, ouders, partners en supporters.</p>
<p>Eerder vierden we ook al met een stijlvol gala-event met als thema "Touch of Gold" en een gala-match van onze Heren A in Nationale 3.</p>
<p>Bedankt aan iedereen die VC Kalken 50 jaar lang mee heeft groot gemaakt — op naar de volgende 50!</p>`,
    },
    4: {
      cat: "Jeugd · maart 2026",
      title: "Jeugdsportfonds-labels voor VC Kalken",
      img: "assets/img/news-4.jpg",
      html: `<p>VC Kalken behaalde dit jaar opnieuw meerdere Jeugdsportfonds-labels van Volley Vlaanderen. Een mooie erkenning voor onze blijvende inzet voor een kwalitatieve, veilige en toegankelijke jeugdwerking.</p>
<p>Behaalde labels:</p>
<ul><li><strong>Volley4All</strong> — volleybal voor iedereen, met oog voor plezier én ontwikkeling</li>
<li><strong>Talentenlabel</strong> — extra begeleiding en groeikansen voor spelers met ambitie</li>
<li><strong>Integriteitslabel</strong> — een veilige, respectvolle en positieve sportomgeving</li>
<li><strong>Beachlabel</strong> — structureel beachvolleybal als aanvulling op onze zaalwerking</li></ul>
<p>Dank aan al onze trainers, vrijwilligers en spelers!</p>`,
    },
    5: {
      cat: "Club · 2026",
      title: "Jubileumgin voor 50 jaar VCK",
      img: "assets/img/news-5.jpg",
      html: `<p>Eenmalige actie voor ons 50-jarig jubileum: klink op onze 50ste verjaardag met deze unieke, herbal infused gin. Gelimiteerde oplage met genummerde flessen.</p>
<ul><li>Prijs: € 50 — de opbrengst gaat volledig naar de clubwerking</li><li>Bestellen kan via <a href="mailto:vokam@vckalken.be">vokam@vckalken.be</a></li></ul>
<p class="fineprint">Alcoholmisbruik schaadt de gezondheid.</p>`,
    },
    6: {
      cat: "Club · voorjaar 2026",
      title: "Stickerboek van VC Kalken",
      img: "assets/img/placeholder-news.svg",
      html: `<p>Het langverwachte VCK-stickerboek werd een voltreffer! Van 22 januari tot 18 maart kon je bij Spar Kalken stickers sparen van al onze spelers en ploegen.</p>
<p>De spaaractie is intussen afgelopen, maar voor wie zijn stickerboek nog niet vol heeft, organiseerden we een ruilbeurs in de sporthal. Hou onze kanalen in de gaten voor een volgende editie!</p>`,
    },
  };
  const newsModal = document.getElementById("newsModal");
  if (newsModal) {
    const mImg = document.getElementById("newsModalImg");
    const mCat = document.getElementById("newsModalCat");
    const mTitle = document.getElementById("newsModalTitle");
    const mText = document.getElementById("newsModalText");
    const mClose = newsModal.querySelector(".news-modal-close");
    let lastFocus = null;
    const openNews = (id) => {
      const a = NEWS_ARTICLES[id];
      if (!a) return;
      lastFocus = document.activeElement;
      mImg.src = a.img;
      mImg.alt = a.title;
      mImg.onerror = () => {
        mImg.onerror = null;
        mImg.src = "assets/img/placeholder-news.svg";
      };
      mCat.textContent = a.cat;
      mTitle.textContent = a.title;
      mText.innerHTML = a.html;
      newsModal.hidden = false;
      document.body.style.overflow = "hidden";
      mClose.focus();
    };
    const closeNews = () => {
      newsModal.hidden = true;
      document.body.style.overflow = "";
      if (lastFocus) lastFocus.focus();
    };
    document.querySelectorAll(".news-card[data-article]").forEach((cardEl) => {
      cardEl.addEventListener("click", () => openNews(cardEl.dataset.article));
      cardEl.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openNews(cardEl.dataset.article);
        }
      });
    });
    mClose.addEventListener("click", closeNews);
    newsModal.addEventListener("click", (e) => {
      if (e.target === newsModal) closeNews();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !newsModal.hidden) closeNews();
    });
  }

  /* ---------------- Copy e-mail buttons ---------------- */
  document.querySelectorAll(".copy-mail").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const txt = btn.dataset.copy || "info@vckalken.be";
      try {
        await navigator.clipboard.writeText(txt);
      } catch (e) {}
      const old = btn.textContent;
      btn.textContent = "Gekopieerd!";
      btn.classList.add("done");
      setTimeout(() => {
        btn.textContent = old;
        btn.classList.remove("done");
      }, 1600);
    });
  });
})();
