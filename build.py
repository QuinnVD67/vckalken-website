# -*- coding: utf-8 -*-
"""Generate the VC Kalken v16 website."""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.vckalken.be"

# ---------------------------------------------------------------- helpers
def img(src, alt, ph, cls="", extra=""):
    """Real photo slot with branded SVG fallback."""
    c = f' class="{cls}"' if cls else ""
    return (f'<img src="assets/img/{src}" alt="{alt}"{c} loading="lazy" '
            f'onerror="this.onerror=null;this.src=\'assets/img/{ph}\'"{extra}>')

# ---------------------------------------------------------------- team data
TEAMS = [
    # slug, name, cat, division, blurb
    ("heren-a","Heren A","heren","Nationale 3","Onze hoogst spelende herenploeg met competitieve ambitie in Nationale 3."),
    ("heren-b","Heren B","heren","Promo 2","Een gedreven herenploeg die week na week knokt in Promo 2."),
    ("heren-c","Heren C","heren","Promo 3A","Ploeg in Promo 3A met focus op groei, plezier en teamspirit."),
    ("heren-vobog","Heren Vobog","heren","Vobog","Recreatieve herencompetitie met clubgevoel en ambitie."),
    ("dames-a","Dames A","dames","Promo 1","Damesploeg met sterke clubwerking en wedstrijdfocus in Promo 1."),
    ("dames-b","Dames B","dames","Promo 3A","Een mix van inzet, ervaring en groei in een hechte ploeg."),
    ("dames-c","Dames C","dames","Promo 4B","Toegankelijke competitieve damesploeg met veel goesting."),
    ("dames-vobog","Dames Vobog","dames","Vobog","Recreatief volleybal met echt wedstrijdgevoel."),
    ("volleybalschool","Volleybalschool","jeugd","Startwerking","Voor de allerjongste spelers die volleybal stap voor stap ontdekken."),
    ("gemengd-a-u11","Gemengd A U11","jeugd","U11","Gemengde jeugdploeg waar spelplezier centraal staat."),
    ("gemengd-b-u11","Gemengd B U11","jeugd","U11","Gemengde jeugdploeg U11 vol beweging en enthousiasme."),
    ("gemengd-u11-2","Gemengd U11 2","jeugd","U11","Extra U11-ploeg zodat elke jonge speler kan spelen."),
    ("gemengd-u13","Gemengd U13","jeugd","U13","Jeugdploeg met aandacht voor techniek en spelinzicht."),
    ("meisjes-u13","Meisjes U13","jeugd","U13","Meisjesploeg U13 die samen groeit en samen wint."),
    ("jongens-u15-a","Jongens U15 A","jeugd","U15","Jongensploeg U15 A met competitieve drive."),
    ("jongens-u15-b","Jongens U15 B","jeugd","U15","Jongensploeg U15 B met focus op ontwikkeling."),
    ("jongens-u17","Jongens U17","jeugd","U17/U19","Jongensploeg U17/U19 in de provinciale competitie."),
    ("meisjes-u15-a","Meisjes U15 A","jeugd","U15","Meisjesploeg U15 A vol ambitie en teamspirit."),
    ("meisjes-u15-b","Meisjes U15 B","jeugd","U15","Meisjesploeg U15 B die elke training beter wordt."),
    ("meisjes-u17-a","Meisjes U17 A","jeugd","U17","Meisjesploeg U17 A op weg naar het hoogste jeugdniveau."),
    ("meisjes-u17-b","Meisjes U17 B","jeugd","U17","Meisjesploeg U17 B met passie voor de sport."),
]
RECREATIE = ["heren-vobog","dames-vobog"]
POSITIONS = ["Setter","Hoofdaanvaller","Midden","Libero","Opposite","Hoekspeler","Midden","Hoekspeler"]

# ---------------------------------------------------------------- player rosters
# Vul hier per ploeg de echte spelers in als (naam, positie).
# Zolang een ploeg leeg is, toont de site nette "Speler 1..8"-plaatshouders.
# Voorbeeld:
#   "heren-a": [("Jan Janssens","Setter"), ("Pieter Peeters","Libero"), ...],
ROSTERS = {
    "heren-a": [
        ("Lars De Vylder","10","Receptie-Hoek"),
        ("Leander Rombaut","","Libero"),
        ("Dieter Vernaeve","","Opposite"),
        ("Robin Roels","2","Opposite"),
        ("Lander Reynvoet","3","Passeur"),
        ("Xander De Bruycker","4","Midden"),
        ("Dieter De Schuyteneer","7","Midden"),
        ("Seppe Imschoot","8","Receptie-Hoek"),
        ("Karel Haenebalcke","9","Passeur"),
        ("Thibaud Acke","11","Receptie-Hoek"),
        ("Stijn Lachat","14","Midden"),
        ("Mathias De Wilde","15","Receptie-Hoek"),
        ("Jeroen De Bruycker","17","Libero"),
    ],
    "heren-b": [
        ("Chiel De Sutter","","Receptie-Hoek"),
        ("Lars De Vylder","","Receptie-Hoek"),
        ("Dmytro Hruzdiev","",""),
        ("Bavo Legiest","","Receptie-Hoek"),
        ("Quinn Van Deun","","Opposite"),
        ("Elias De Smet","1","Midden"),
        ("Jens Van Hoorde","2","Passeur"),
        ("Siemen Heyndrickx","3","Opposite"),
        ("Jorre Wielandt","7","Receptie-Hoek"),
        ("Giliam Rombaut","8","Receptie-Hoek"),
        ("Arne Stroobant","9","Receptie-Hoek"),
        ("Jarne Ben Ayache","12","Receptie-Hoek"),
        ("Niels Van Duerm","14","Midden"),
    ],
    "heren-c": [
        ("Thure Belpaeme","",""),
        ("Seppe D'hondt","",""),
        ("Iljo De Vylder","",""),
        ("Mathijs Defoort","",""),
        ("Viktor Denkens","",""),
        ("Rien Devriendt","",""),
        ("Floris Kersschot","",""),
        ("Dmytro Muliar","",""),
        ("Perre Ponnet","",""),
        ("Seppe Ponnet","",""),
        ("Mathias Raemdonck","",""),
        ("Mathis Van Damme","",""),
        ("Quinn Van Deun","",""),
        ("Victor Vanherck","",""),
    ],
    "dames-a": [
        ("Lou Blanchaert","",""),
        ("Cato De Coessemaeker","",""),
        ("Fran De Waegemaeker","",""),
        ("Joske Rasschaert","",""),
        ("Elke Roels","",""),
        ("Jana Roels","",""),
        ("Eline Van Acker","",""),
        ("Eline Van Damme","",""),
        ("Amber Van de Putte","",""),
        ("Aline Van Den Heuvel","",""),
        ("Olivia Van Gaever","",""),
        ("Louise Vanden Abbeele","",""),
        ("Heleen Wochnik","",""),
    ],
    "dames-b": [
        ("Roos Andries","",""),
        ("Ruth Baeteman","",""),
        ("Sofie Bryse","",""),
        ("Caroline Defoort","",""),
        ("Anouck Ketels","",""),
        ("Louise Léonard","",""),
        ("Flora Lippens","",""),
        ("Britte Rasschaert","",""),
        ("Myrthe Snoeck","",""),
        ("Rhone Snoeck","",""),
        ("Nina Staelens","",""),
        ("Janne Verhaeghen","",""),
        ("Jozefien Vuylsteke","",""),
        ("Lotte Weymans","",""),
    ],
    "dames-c": [
        ("Noa Honraet","1","Midden"),
        ("Lena Dierickx","2","Opposite"),
        ("Elien Bryse","3","Receptie-Hoek"),
        ("Laure Van Damme","4","Passeur"),
        ("Flore Gallee","5","Receptie-Hoek"),
        ("Luka Schelkens","6","Passeur"),
        ("Lyssa De Weirdt","7","Opposite"),
        ("Bo D'haene","8","Receptie-Hoek"),
        ("Anke Stroobandt","9","Receptie-Hoek"),
        ("Kiana Slabbynck","10","Midden"),
        ("Ilona Van Lysebeth","11","Midden"),
        ("Janne Neus","12","Passeur"),
        ("Yelina Monprofit","13","Libero"),
        ("Lana Gijsbers","14","Receptie-Hoek"),
        ("Janne Schelkens","15","Libero"),
    ],
}

# Begeleiding & trainingsuren per ploeg (optioneel).
TEAMINFO = {
    "heren-b": {
        "trainers": ["Jente De Wyn", "Steven De Smet"],
        "verantwoordelijke": "Patricia Van Mossevelde",
        "training": [("Maandag", "19:00 – 21:00", "Sporthal Laarne · Terrein B'"),
                     ("Woensdag", "20:30 – 22:30", "Sporthal Laarne · Terrein A")],
    },
    "heren-c": {
        "trainers": ["Elias De Smet"],
        "verantwoordelijke": "Wouter Defoort",
        "training": [("Dinsdag", "20:00 – 22:00", ""),
                     ("Vrijdag", "20:00 – 22:00", "")],
    },
    "dames-a": {
        "trainers": ["Evelyne De Wael"],
        "verantwoordelijke": "",
        "training": [("Maandag", "20:00 – 22:00", "Sporthal Laarne · Terrein C"),
                     ("Donderdag", "20:00 – 22:00", "Sporthal Laarne · Terrein B")],
    },
    "dames-b": {
        "trainers": ["Robin Roels"],
        "verantwoordelijke": "",
        "training": [("Maandag", "20:00 – 22:00", "Sporthal Laarne · Terrein B"),
                     ("Woensdag", "20:00 – 22:00", "Sporthal Laarne · Terrein F")],
    },
    "dames-c": {
        "trainers": ["Jente De Wyn", "Steven De Smet"],
        "verantwoordelijke": "",
        "training": [("Dinsdag", "20:00 – 22:00", "Sporthal Laarne · Terrein C"),
                     ("Woensdag", "20:00 – 22:00", "Sporthal Laarne")],
    },
}

def roster(slug):
    """Echte selectie indien ingevuld, anders generieke plaatshouders.
    Levert tuples (naam, nummer, positie)."""
    r = ROSTERS.get(slug)
    if r:
        out = []
        for item in r:
            if len(item) == 3: out.append(item)
            elif len(item) == 2: out.append((item[0], "", item[1]))
            else: out.append((item[0], "", ""))
        return out
    return [(f"Speler {i+1}", str(i+1), POSITIONS[i % len(POSITIONS)]) for i in range(8)]

# ---------------------------------------------------------------- Volleyscores
# Belangrijk: de links hieronder (VS_BASE + "calendar/team/...") zijn
# .ics-agendafeeds, bedoeld om te synchroniseren met een smartphone-/Google-
# agenda — GEEN webpagina's. In een browser geopend doen ze schijnbaar niets.
# Ze blijven hier staan zodat je ze eventueel kan gebruiken voor een
# "voeg toe aan mijn agenda"-functie. Voor een klikbare, leesbare pagina
# gebruiken we CLUB_DIRECT: de officiële, browseable Volleyscores-pagina
# van VC Kalken met alle ploegen en wedstrijden.
VS_BASE = "https://www.volleyscores.be/"
CLUB_DIRECT = "https://www.volleyscores.be/direct/O-1464"  # VC Kalken op Volleyscores (browseable)
TEAM_CAL = {
    "heren-a":       VS_BASE + "calendar/team/105856",  # NAT3H-A  · VC Kalken A
    "heren-b":       VS_BASE + "calendar/team/102358",  # OHP2     · VC Kalken B
    "heren-c":       VS_BASE + "calendar/team/102360",  # OHP3A    · VC Kalken C
    "dames-a":       VS_BASE + "calendar/team/102361",  # ODP1     · VC Kalken A
    "dames-b":       VS_BASE + "calendar/team/102362",  # ODP3A    · VC Kalken B
    "dames-c":       VS_BASE + "calendar/team/102363",  # ODP4B    · VC Kalken C
    "meisjes-u17-a": VS_BASE + "calendar/team/102373",  # OMU17N1R1b · VC Kalken A
    "meisjes-u17-b": VS_BASE + "calendar/team/102374",  # OMU17N3R1e · VC Kalken B
    "meisjes-u15-a": VS_BASE + "calendar/team/102371",  # OMU15N1R1b · VC Kalken A
    "meisjes-u15-b": VS_BASE + "calendar/team/102372",  # OMU15N3R1f · VC Kalken B
    "meisjes-u13":   VS_BASE + "calendar/team/102370",  # OMU13N3R1e · VC Kalken
    "jongens-u15-a": VS_BASE + "calendar/team/102368",  # OJU15N1R1  · VC Kalken
    "gemengd-u13":   VS_BASE + "calendar/team/102367",  # OJU13N1R1  · VC Kalken
    # Jongens U17/U19 (OJU17U19N1R1b, team 102369) -> zie jongens-u17 indien toegevoegd
    "jongens-u17":   VS_BASE + "calendar/team/102369",
}
def teamcal(slug):
    return CLUB_DIRECT

def team(slug):
    return next(t for t in TEAMS if t[0]==slug)

# ---------------------------------------------------------------- shared chrome
def head(title, desc, canon, og_img="logo.png", image_card=False):
    tw = "summary_large_image" if image_card else "summary"
    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | VC Kalken</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{SITE}/{canon}" />
  <link rel="icon" type="image/png" href="logo.png" />
  <link rel="apple-touch-icon" href="logo.png" />
  <meta name="theme-color" content="#0a2342" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="nl_BE" />
  <meta property="og:site_name" content="VC Kalken" />
  <meta property="og:title" content="{title} | VC Kalken" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{SITE}/{canon}" />
  <meta property="og:image" content="{SITE}/{og_img}" />
  <meta name="twitter:card" content="{tw}" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
  <script>document.documentElement.classList.add("js")</script>
  <link rel="stylesheet" href="styles.css" />
  <script defer src="data/matches.js"></script>
  <script defer src="script.js"></script>
</head>
<body><a class="skip-link" href="#inhoud">Ga naar inhoud</a>'''

def header(active=""):
    def cur(slug):
        return ' aria-current="page"' if active == slug else ""
    return f'''<header class="site-header">
  <a class="brand" href="index.html" aria-label="VC Kalken home">
    <img src="logo.png" alt="VC Kalken logo" />
    <span><strong>VC Kalken</strong><small>Samen groeien. Samen winnen.</small></span>
  </a>
  <button type="button" class="nav-toggle" aria-label="Menu openen" aria-expanded="false" aria-controls="mainNav">&#9776;</button>
  <nav class="main-nav" id="mainNav" aria-label="Hoofdnavigatie">
    <a href="index.html"{cur("home")}>Home</a>
    <div class="nav-item has-menu">
      <a href="ploegen.html"{cur("ploegen")}>Ploegen</a>
      <div class="mega-menu">
        <div><h4>Heren</h4><a href="heren-a.html">Heren A</a><a href="heren-b.html">Heren B · Promo 2</a><a href="heren-c.html">Heren C · Promo 3A</a><a href="heren-vobog.html">Heren Vobog</a></div>
        <div><h4>Dames</h4><a href="dames-a.html">Dames A</a><a href="dames-b.html">Dames B</a><a href="dames-c.html">Dames C</a><a href="dames-vobog.html">Dames Vobog</a></div>
        <div><h4>Jeugd</h4><a href="volleybalschool.html">Volleybalschool</a><a href="gemengd-u13.html">Gemengd U13</a><a href="jongens-u15-a.html">Jongens U15 A</a><a href="meisjes-u17-a.html">Meisjes U17 A</a><a href="ploegen.html#jeugd">Alle jeugd →</a></div>
        <div class="menu-cta"><h4>Nieuwe speler?</h4><p>Vind je ploeg en kom gratis meetrainen.</p><a class="btn small" href="word-lid.html">Proeftraining</a></div>
      </div>
    </div>
    <a href="kalender.html"{cur("kalender")}>Kalender</a>
    <a href="nieuws.html"{cur("nieuws")}>Nieuws</a>
    <div class="nav-item has-menu">
      <a href="club.html"{cur("club")}>Club</a>
      <div class="small-menu"><h4>Over de club</h4><a href="club.html">Identiteit</a><a href="clubkledij.html">Clubkledij</a><a href="verzekering.html">Verzekering</a><a href="unkerzak.html">Unkerzak</a><a href="fotos.html">Fotoalbums</a><a href="sponsors.html">Sponsors</a></div>
    </div>
    <a class="nav-pill" href="contact.html"{cur("contact")}>Contact</a>
    <div class="search-wrap">
      <input id="siteSearch" type="search" placeholder="Zoek pagina…" autocomplete="off" aria-label="Zoeken" />
      <div id="searchResults" class="search-results"></div>
    </div>
  </nav>
</header>'''

FOOTER = '''<footer class="footer">
  <section class="footer-hero reveal">
    <img src="logo.png" alt="VC Kalken logo" />
    <div>
      <h2>VC Kalken voelt als thuiskomen.</h2>
      <p>Een warme volleybalclub voor jeugd, dames, heren, recreanten, supporters en vrijwilligers.</p>
    </div>
    <a class="btn" href="word-lid.html">Word lid</a>
  </section>
  <section class="footer-grid">
    <div><h3>Ploegen</h3><a href="ploegen.html">Alle ploegen</a><a href="heren-a.html">Heren A · Nationale 3</a><a href="heren-b.html">Heren B · Promo 2</a><a href="dames-a.html">Dames A</a><a href="volleybalschool.html">Volleybalschool</a></div>
    <div><h3>Club</h3><a href="club.html">Identiteit</a><a href="clubkledij.html">Clubkledij</a><a href="verzekering.html">Verzekering</a><a href="unkerzak.html">Unkerzak</a><a href="fotos.html">Fotoalbums</a></div>
    <div><h3>Praktisch</h3><a href="kalender.html">Kalender</a><a href="https://www.volleyscores.be/" target="_blank" rel="noopener">Volleyscores.be</a><a href="word-lid.html">Word lid</a><a href="contact.html">Contact</a></div>
    <div><h3>Contact</h3><p>Sporthal Veldmeers<br>Leeweg 25, 9270 Laarne<br><a href="mailto:info@vckalken.be">info@vckalken.be</a></p><p class="socials"><a href="https://www.facebook.com/vckalken/" target="_blank" rel="noopener">Facebook</a> · <a href="https://www.instagram.com/vc_kalken/" target="_blank" rel="noopener">Instagram</a> · <a href="https://www.volleyvlaanderen.be/" target="_blank" rel="noopener">Volley Vlaanderen</a></p></div>
  </section>
  <div class="footer-bottom">© 2026 VC Kalken · Volleybalclub Kalken (Laarne)</div>
</footer>
<button class="to-top" aria-label="Naar boven">&#8593;</button>
<div class="lightbox" id="lightbox"><button class="close" aria-label="Sluiten">&times;</button><img src="" alt=""></div>
</body>
</html>'''

def write(name, body):
    open(os.path.join(OUT,name),"w",encoding="utf-8").write(body)
    print("wrote",name)

# ---------------------------------------------------------------- ICONS
IC_CAL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="3"/><path d="M3 9h18M8 2v4M16 2v4"/></svg>'
IC_SHIRT='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 3l5 3-2 4-2-1v11H7V9L5 10 3 6l5-3 2 2h4z"/></svg>'
IC_STAR='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3l2.7 5.5 6 .9-4.3 4.2 1 6-5.4-2.8L6.6 19.6l1-6L3.3 9.4l6-.9z"/></svg>'
IC_HEART='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20s-7-4.6-9.3-9C1 7.5 3 4 6.5 4 9 4 12 7 12 7s3-3 5.5-3C21 4 23 7.5 21.3 11 19 15.4 12 20 12 20z"/></svg>'
IC_FLAG='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 21V4m0 0c3-2 6 2 9 0s5-1 5-1v9s-2 1-5 1-6-2-9 0"/></svg>'
IC_BALL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 3a15 15 0 0 0 0 18M3.5 9A15 15 0 0 1 20 14M20.5 9A15 15 0 0 0 4 14"/></svg>'
IC_SHIELD='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3l8 3v6c0 4.5-3.2 7.5-8 9-4.8-1.5-8-4.5-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>'
IC_DOC='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2h8l4 4v16H6z"/><path d="M14 2v4h4M9 13h6M9 17h6"/></svg>'

print("done defining")
