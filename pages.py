# -*- coding: utf-8 -*-
from build import *

# ============================================================ HOME
def build_index():
    quick = f'''<section class="quick-strip">
  <a href="kalender.html" class="reveal"><span class="qicon">{IC_CAL}</span><span><strong>Volgende wedstrijden</strong><span>Bekijk de kalender via Volleyscores</span></span></a>
  <a href="word-lid.html" class="reveal d1"><span class="qicon">{IC_BALL}</span><span><strong>Gratis proeftraining</strong><span>Kom een keer meetrainen</span></span></a>
  <a href="clubkledij.html" class="reveal d2"><span class="qicon">{IC_SHIRT}</span><span><strong>Clubkledij</strong><span>Shop eenvoudig via Twizzit</span></span></a>
</section>'''

    week_section = f'''<section class="section">
  <div class="section-head"><div class="reveal"><span class="eyebrow">Deze week</span><h2>Wedstrijden deze week</h2></div><a href="kalender.html" class="reveal">Volledige kalender →</a></div>
  <div id="week-matches" class="matches-list reveal d1"><div class="empty-state">Wedstrijden worden geladen…</div></div>
</section>'''

    teamcards = ""
    for cat,label,blurb,href in [
        ("jeugd","Jeugd","Van de eerste volleybalstappen tot competitie.","ploegen.html#jeugd"),
        ("dames","Dames","Competitie en teamspirit voor elk niveau.","ploegen.html#dames"),
        ("heren","Heren","Van Nationale 3 tot recreatieve Vobog.","ploegen.html#heren"),
        ("recreatie","Recreatie","Volleybal met plezier en clubgevoel.","ploegen.html#recreatie"),
    ]:
        d = {"jeugd":"d1","dames":"d2","heren":"d3","recreatie":"d4"}.get(cat,"")
        teamcards += f'''<a class="image-card reveal {d}" href="{href}">
  <div class="media logo-slot"><span class="badge">{label}</span><img src="logo.png" alt="VC Kalken logo" loading="lazy"></div>
  <div class="body"><h3>{label}</h3><p>{blurb}</p></div></a>'''

    news = f'''<section class="section warm">
  <div class="split">
    <div class="reveal">
      <span class="eyebrow">Nieuws</span>
      <h2>Clubnieuws dat snel leesbaar is</h2>
      <p class="lead">Belangrijke berichten verschijnen in duidelijke kaarten met datum, categorie en een korte samenvatting — zodat je in één oogopslag weet wat er leeft in de club.</p>
      <div class="actions"><a class="btn" href="nieuws.html">Naar nieuws</a><a class="btn ghost-dark" href="fotos.html">Fotoalbums</a></div>
    </div>
    <div class="news-feature reveal d2">
      {img("news-uitgelicht.jpg","50 jaar VC Kalken","placeholder-news.svg")}
      <div class="body"><span class="eyebrow">Uitgelicht</span><h3>VC Kalken viert 50 jaar</h3><p>Een halve eeuw volleybal in Kalken! We vierden ons gouden jubileum met een gala-avond en een groot eindeseizoensfeest met de hele clubfamilie.</p></div>
    </div>
  </div>
</section>'''

    identity = f'''<section class="section">
  <div class="section-head"><div class="reveal"><span class="eyebrow">Identiteit</span><h2>Meer dan een volleybalclub</h2></div></div>
  <p class="lead reveal" style="margin-bottom:30px">VC Kalken wil een plek zijn waar spelers groeien, trainers begeleiden, supporters verbinden en vrijwilligers het verschil maken. Sportief én warm.</p>
  <div class="values">
    <div class="value-card reveal"><span class="vicon">{IC_HEART}</span><b>Warm</b><span>Iedereen voelt zich hier welkom.</span></div>
    <div class="value-card reveal d1"><span class="vicon">{IC_STAR}</span><b>Sportief</b><span>Trainingskwaliteit, ambitie en fair play.</span></div>
    <div class="value-card reveal d2"><span class="vicon">{IC_FLAG}</span><b>Verbonden</b><span>Ploegen, supporters en vrijwilligers samen.</span></div>
  </div>
</section>'''

    cta = '''<section class="section">
  <div class="sponsor-cta reveal">
    <span class="eyebrow" style="color:var(--gold-2);justify-content:center;display:flex">Klaar om te starten?</span>
    <h2>Kom een keer gratis meetrainen</h2>
    <p>Of je nu 7 of 47 bent, beginner of ervaren: er is altijd een ploeg die bij je past. Vraag vrijblijvend een proeftraining aan.</p>
    <div class="actions" style="justify-content:center"><a class="btn" href="word-lid.html">Vraag proeftraining aan</a><a class="btn ghost" href="ploegen.html">Bekijk de ploegen</a></div>
  </div>
</section>'''

    hero = f'''<section class="hero">
  {img("hero.jpg","VC Kalken in actie","placeholder-hero.svg","hero-bg").replace('loading="lazy"','fetchpriority="high"')}
  <div class="hero-card">
    <span class="eyebrow">Welkom bij VC Kalken</span>
    <h1>Samen groeien.<br><span class="accent">Samen winnen.</span></h1>
    <p>Een warme volleybalclub in Kalken waar jeugd, dames, heren, recreanten en supporters elkaar vinden op én naast het veld.</p>
    <div class="actions"><a class="btn" href="word-lid.html">Vraag proeftraining aan</a><a class="btn ghost" href="ploegen.html">Ontdek onze ploegen</a></div>
  </div>
  <div class="hero-side">
    <img src="logo.png" alt="VC Kalken logo">
    <strong>Volleybal in Kalken</strong>
    <span>Jeugd · Dames · Heren · Recreatie</span>
    <div class="mini-stats"><div><b>20</b><small>ploegen</small></div><div><b>300+</b><small>leden</small></div></div>
  </div>
</section>'''

    teams_sec = f'''<section class="section">
  <div class="section-head"><div class="reveal"><span class="eyebrow">Ploegen</span><h2>Vind snel je plek</h2></div><a href="ploegen.html" class="reveal">Alle ploegen bekijken →</a></div>
  <div class="cards four">{teamcards}</div>
</section>'''

    ld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"SportsClub","name":"VC Kalken","alternateName":"Volleybalclub Kalken","url":"https://www.vckalken.be/","logo":"https://www.vckalken.be/logo.png","sport":"Volleyball","email":"info@vckalken.be","address":{"@type":"PostalAddress","streetAddress":"Leeweg 25","addressLocality":"Laarne","postalCode":"9270","addressRegion":"Oost-Vlaanderen","addressCountry":"BE"},"sameAs":["https://www.facebook.com/vckalken/","https://www.instagram.com/vc_kalken/"]}
</script>'''

    body = (head("Home","VC Kalken is een volleybalclub in Kalken (Laarne) voor jeugd, dames en heren. Ontdek onze ploegen, kalender, nieuws en hoe je lid wordt.","", image_card=True)
            + header("home") + "\n<main id=\"inhoud\">\n" + hero + quick + week_section + teams_sec + news + identity + cta
            + "\n</main>\n" + FOOTER.replace("</body>", ld+"\n</body>"))
    write("index.html", body)

# ============================================================ PLOEGEN
def build_ploegen():
    def group(title,gid,slugs):
        cards=""
        for i,s in enumerate(slugs):
            _,name,cat,div,blurb = team(s)
            d = f"d{(i%4)}" if i%4 else ""
            cards += f'''<a class="team-card reveal {d}" href="{s}.html">
  <div class="media"><span class="badge">{div}</span>{img(f"team-{s}.jpg",f"Ploegfoto {name}","placeholder-team.svg")}</div>
  <div class="body"><h3>{name}</h3><p>{blurb}</p><span class="more">Bekijk ploeg →</span></div></a>'''
        return f'<h2 id="{gid}" class="group-title">{title}</h2>\n<div class="cards four">{cards}</div>\n'

    heren=[t[0] for t in TEAMS if t[2]=="heren"]
    dames=[t[0] for t in TEAMS if t[2]=="dames"]
    jeugd=[t[0] for t in TEAMS if t[2]=="jeugd"]

    hero = '''<section class="page-hero">
  <span class="eyebrow">Alle ploegen</span>
  <h1>Klik op een ploeg en<br>ontdek de spelers.</h1>
  <p>Overzichtelijk per categorie: heren, dames, jeugd en recreatie. Elke ploeg heeft een eigen pagina met spelers, foto en kalenderlink.</p>
</section>'''
    sec = '<section class="section">\n'+group("Heren","heren",heren)+group("Dames","dames",dames)+group("Jeugd","jeugd",jeugd)+group("Recreatie","recreatie",RECREATIE)+'</section>'
    body = head("Ploegen","Bekijk alle ploegen van VC Kalken: heren, dames, jeugd en recreatie. Klik door naar spelers, foto en kalender.","ploegen.html")+header("ploegen")+"\n<main id=\"inhoud\">\n"+hero+sec+"\n</main>\n"+FOOTER
    write("ploegen.html",body)

# ============================================================ TEAM PAGES
def build_team(slug):
    _,name,cat,div,blurb = team(slug)
    catlabel={"heren":"Heren","dames":"Dames","jeugd":"Jeugd"}[cat]
    squad=roster(slug)
    players=""
    for i,(pname,num,pos) in enumerate(squad, start=1):
        d=f"d{(i-1)%4}" if (i-1)%4 else ""
        badge=f'<span class="num">{num}</span>' if num else ''
        posline=f'<p>{pos}</p>' if pos else ''
        players+=f'''<article class="player reveal {d}">
  <div class="avatar">{badge}{img(f"player-{slug}-{i}.jpg",f"{pname} — {name}","placeholder-player.svg",extra=' data-lightbox')}</div>
  <h3>{pname}</h3>{posline}</article>'''

    # Begeleiding & trainingsuren (alleen tonen indien bekend)
    info=TEAMINFO.get(slug)
    staff=""
    if info:
        cards=""
        tr=info.get("trainers") or []
        if tr:
            names="".join(f"<strong>{t}</strong>" for t in tr)
            cards+=f'<div class="staff-card"><span class="slabel">Trainer{"s" if len(tr)>1 else ""}</span>{names}</div>'
        if info.get("verantwoordelijke"):
            cards+=f'<div class="staff-card"><span class="slabel">Ploegverantwoordelijke</span><strong>{info["verantwoordelijke"]}</strong></div>'
        tt=info.get("training") or []
        if tt:
            rows="".join(f'<div class="train-row"><b>{d}</b><span>{h}{(" · "+loc) if loc else ""}</span></div>' for d,h,loc in tt)
            cards+=f'<div class="staff-card training"><span class="slabel">Trainingsuren</span>{rows}</div>'
        staff=f'<section class="section tight"><div class="section-head"><div class="reveal"><span class="eyebrow">Begeleiding</span><h2>Trainers &amp; training</h2></div></div><div class="staff-grid reveal">{cards}</div></section>'

    hero=f'''<section class="team-hero-v16">
  <div class="media">{img(f"team-{slug}.jpg",f"Ploegfoto {name}","placeholder-team.svg",extra=' data-lightbox')}</div>
  <div class="info">
    <span class="eyebrow">{catlabel} · {div}</span>
    <h1>{name}</h1>
    <div class="team-meta"><span>{catlabel}</span><span>{div}</span><span>VC Kalken</span></div>
    <p>{blurb}</p>
    <div class="actions"><a class="btn" href="kalender.html?team={slug}">Kalender van deze ploeg</a><a class="btn ghost-dark" target="_blank" rel="noopener" href="{teamcal(slug)}">Kalender op Volleyscores</a></div>
  </div>
</section>'''
    n=len(squad)
    filled = slug in ROSTERS
    cap = (f"Voeg de spelersfoto's toe als player-{slug}-1.jpg t.e.m. player-{slug}-{n}.jpg (in de volgorde hieronder)."
           if filled else
           f"Vervang de voorbeeldnamen, posities en foto's door de echte ploeggegevens (player-{slug}-1.jpg t.e.m. -{n}.jpg).")
    sec=f'''<section class="section">
  <div class="section-head"><div class="reveal"><span class="eyebrow">Selectie</span><h2>Spelers</h2></div><p class="reveal">{cap}</p></div>
  <div class="players-grid">{players}</div>
</section>'''
    body=head(name,f"{name} ({div}) bij VC Kalken. Bekijk de spelers, ploegfoto en link naar de kalender.",f"{slug}.html",image_card=True)+header("ploegen")+"\n<main id=\"inhoud\">\n"+hero+staff+sec+"\n</main>\n"+FOOTER
    write(f"{slug}.html",body)

# ============================================================ NIEUWS
def build_nieuws():
    items=[
        ("Evenement · 22/08/2026","BBQ met Sparta Laarne","VC Kalken en basketbalclub Sparta Laarne slaan de handen in elkaar: samen aan 't vuur op zaterdag 22 augustus vanaf 17u aan Sporthal Laarne. Iedereen welkom!"),
        ("Jeugd · 4 april 2026","Jongens U15 winnen de Oost-Vlaamse beker","Onze jongens U15 kroonden zich tot winnaar van de Oost-Vlaamse beker. Een prachtige bekroning voor het team, de trainers en de hele jeugdwerking."),
        ("Club · mei 2026","50 jaar VC Kalken gevierd in stijl","Een halve eeuw volleybal in Kalken! We vierden ons gouden jubileum met een gala-avond en een onvergetelijk eindeseizoensfeest met de hele clubfamilie."),
        ("Jeugd · maart 2026","Jeugdsportfonds-labels voor VC Kalken","Onze jeugdopleiding is officieel bekroond: VC Kalken ontving opnieuw meerdere Jeugdsportfonds-labels van Volley Vlaanderen."),
        ("Club · 2026","Jubileumgin voor 50 jaar VCK","Klink mee op onze 50ste verjaardag met de unieke jubileumgin. Gelimiteerde oplage met genummerde flessen, volledig ten voordele van de clubwerking."),
        ("Club · voorjaar 2026","Stickerboek van VC Kalken","Verzamel al onze spelers en ploegen in het eigen VCK-stickerboek. Wie zijn boek nog niet vol heeft, kon terecht op de ruilbeurs in de sporthal."),
    ]
    cards=""
    for i,(cat,t,p) in enumerate(items):
        d=f"d{i%3}" if i%3 else ""
        cards+=f'''<article class="news-card reveal {d}" data-article="{i+1}" tabindex="0" role="button" aria-haspopup="dialog" aria-label="Lees meer: {t}">
  <div class="media">{img(f"news-{i+1}.jpg",t,"placeholder-news.svg")}</div>
  <div class="body"><span class="cat"><span class="dot"></span>{cat}</span><h2>{t}</h2><p>{p}</p><span class="read">Lees meer →</span></div></article>'''
    hero='''<section class="page-hero"><span class="eyebrow">Nieuws</span><h1>Belangrijke clubupdates,<br>snel gevonden.</h1><p>Duidelijke nieuwskaarten met datum, categorie en korte samenvatting — zodat je in één oogopslag weet wat er leeft in de club.</p></section>'''
    modal='''<div class="news-modal" id="newsModal" hidden>
  <div class="news-modal-card" role="dialog" aria-modal="true" aria-labelledby="newsModalTitle">
    <button type="button" class="news-modal-close" aria-label="Sluiten">&times;</button>
    <img id="newsModalImg" src="" alt="">
    <div class="news-modal-body">
      <span class="cat"><span class="dot"></span><span id="newsModalCat"></span></span>
      <h2 id="newsModalTitle"></h2>
      <div class="news-modal-text" id="newsModalText"></div>
    </div>
  </div>
</div>'''
    sec=f'<section class="section"><div class="news-grid">{cards}</div></section>'+modal
    body=head("Nieuws","Het laatste nieuws van VC Kalken: clubupdates, wedstrijden, jeugd, clubkledij en evenementen.","nieuws.html")+header("nieuws")+"\n<main id=\"inhoud\">\n"+hero+sec+"\n</main>\n"+FOOTER
    write("nieuws.html",body)

# ============================================================ KALENDER
CLUB_CAL = CLUB_DIRECT  # browseable Volleyscores-pagina van VC Kalken
def build_kalender():
    teamopts = '<option value="">Alle ploegen</option>\n'
    for s,name,cat,div,_ in TEAMS:
        teamopts += f'        <option value="{s}">{name} · {div}</option>\n'
    hero='''<section class="page-hero"><span class="eyebrow">Kalender</span><h1>Alle ploegen,<br>één kalender.</h1><p>Ouders en supporters hoeven enkel hier te kijken: kies je ploeg en filter snel op <strong>thuis</strong> of <strong>uit</strong>. De live en officiële gegevens komen rechtstreeks van Volleyscores.</p></section>'''
    shell=f'''<section class="section">
  <div class="calendar-shell">
    <aside class="calendar-aside">
      <h2>Filter kalender</h2>
      <p class="muted">Kies een ploeg of zoek op tegenstander, sporthal of reeks.</p>
      <label for="teamFilter">Ploeg</label>
      <select id="teamFilter">
        {teamopts.strip()}
      </select>
      <label for="periodFilter">Toon</label>
      <select id="periodFilter"><option value="upcoming">Komende wedstrijden</option><option value="past">Gespeelde wedstrijden</option><option value="all">Alle wedstrijden</option></select>
      <label for="catFilter">Categorie</label>
      <select id="catFilter"><option value="">Alle categorieën</option><option value="heren">Heren</option><option value="dames">Dames</option><option value="jeugd">Jeugd</option></select>
      <label for="locFilter">Thuis / uit</label>
      <select id="locFilter"><option value="">Alles</option><option value="home">Thuis</option><option value="away">Uit</option><option value="neutral">Volleyscores-link</option></select>
      <label for="searchMatch">Zoeken</label>
      <input id="searchMatch" type="search" placeholder="bv. Gent, Veldmeers, Heren B…">
      <div id="matchCount" class="calendar-count">Wedstrijden laden…</div>
      <div id="dataUpdated" class="source-note"></div>
      <a class="btn" style="width:100%;margin-top:14px" target="_blank" rel="noopener" href="{CLUB_CAL}">Volleyscores.be openen</a>
      <p class="source-note">Elke ploeg heeft hiernaast zijn eigen officiële Volleyscores-kalender met alle thuis- en uitwedstrijden. Tip: open die op je smartphone om te synchroniseren met je agenda.</p>
    </aside>
    <div class="calendar-main-v13">
      <div class="loc-toggle" id="locToggle" role="group" aria-label="Filter thuis of uit">
        <button type="button" data-loc="">Alle wedstrijden</button>
        <button type="button" data-loc="home">Thuis</button>
        <button type="button" data-loc="away">Uit</button>
      </div>
      <div class="calendar-actions">
        <a class="btn soft" target="_blank" rel="noopener" href="{CLUB_CAL}">Live bron openen</a>
        <a class="btn danger outline" href="contact.html?type=kalender">Fout melden</a>
      </div>
      <div id="matches" class="matches-list"></div>
    </div>
  </div>
</section>'''
    body=head("Kalender","Bekijk de volledige wedstrijdkalender van VC Kalken op één plek. Filter per ploeg en op thuis/uit; live gegevens via Volleyscores.","kalender.html")+header("kalender")+"\n<main id=\"inhoud\">\n"+hero+shell+"\n</main>\n"+FOOTER
    write("kalender.html",body)

# ============================================================ FOTOS
def build_fotos():
    cards=""
    for i,yr in enumerate([2026,2025,2024,2023,2022,2021,2020,2019]):
        d=f"d{i%4}" if i%4 else ""
        cards+=f'''<a class="album-card reveal {d}" href="#">
  {img(f"album-{yr}.jpg",f"Fotoalbum {yr}","placeholder-album.svg",extra=' data-lightbox')}
  <div class="body"><span class="yr">{yr}</span><h2>Fotoalbum {yr}</h2><p>Wedstrijden · activiteiten · sfeerbeelden</p></div></a>'''
    hero='''<section class="page-hero"><span class="eyebrow">Fotoalbums</span><h1>Herbeleef elk seizoen<br>per jaartal.</h1><p>Maak de club zichtbaar met fotoalbums van wedstrijden, activiteiten, tornooien en Unkerzak. Voeg je albumcovers toe als album-2026.jpg, album-2025.jpg, …</p></section>'''
    sec=f'<section class="section"><div class="album-grid">{cards}</div></section>'
    body=head("Fotoalbums","Bekijk de fotoalbums van VC Kalken per seizoen: wedstrijden, activiteiten en sfeerbeelden.","fotos.html")+header("club")+"\n<main id=\"inhoud\">\n"+hero+sec+"\n</main>\n"+FOOTER
    write("fotos.html",body)

# ============================================================ CLUB
def build_club():
    hero='''<section class="page-hero"><span class="eyebrow">Identiteit</span><h1>Een club met<br>ambitie en warmte.</h1><p>VC Kalken is meer dan wedstrijden spelen. Het is leren, groeien, engagement opnemen en samen club maken.</p></section>'''
    grid=f'''<section class="section">
  <div class="identity-grid">
    <div class="lead-card reveal"><span class="eyebrow" style="color:var(--gold-2)">Waar we voor staan</span><h2>Een duidelijke, warme en sportieve club</h2><p>Spelers voelen zich welkom, ouders vinden snel de juiste informatie en iedereen krijgt de kans om te groeien — op het veld en daarbuiten.</p></div>
    <div class="value-card reveal d1"><span class="vicon">{IC_HEART}</span><b>Warm</b><span>Iedereen voelt zich welkom.</span></div>
    <div class="value-card reveal d2"><span class="vicon">{IC_STAR}</span><b>Sportief</b><span>Trainingskwaliteit en fair play.</span></div>
    <div class="value-card reveal d1"><span class="vicon">{IC_FLAG}</span><b>Verbonden</b><span>Vrijwilligers, supporters en ploegen samen.</span></div>
    <div class="value-card reveal d2"><span class="vicon">{IC_BALL}</span><b>Ambitieus</b><span>We willen elke dag een beetje beter worden.</span></div>
  </div>
</section>'''
    split=f'''<section class="section warm">
  <div class="split">
    <div class="news-feature reveal">{img("club-sfeer.jpg","Sfeerbeeld VC Kalken","placeholder-news.svg")}<div class="body"><span class="eyebrow">De club</span><h3>Thuis in Sporthal Veldmeers</h3><p>In Laarne (deelgemeente Kalken) bouwen we al jaren aan een hechte volleybalfamilie voor jong en oud.</p></div></div>
    <div class="reveal d2"><span class="eyebrow">Meedoen</span><h2>Word deel van VC Kalken</h2><p class="lead">Als speler, supporter of vrijwilliger: er is altijd een plek voor jou. Kom langs, leer de club kennen en voel meteen de sfeer.</p><div class="actions"><a class="btn" href="word-lid.html">Word lid</a><a class="btn ghost-dark" href="contact.html">Contacteer ons</a></div></div>
  </div>
</section>'''
    body=head("Club","Ontdek de identiteit van VC Kalken: een warme, sportieve en verbonden volleybalclub in Kalken (Laarne).","club.html")+header("club")+"\n<main id=\"inhoud\">\n"+hero+grid+split+"\n</main>\n"+FOOTER
    write("club.html",body)

# ============================================================ CONTACT
def build_contact():
    hero='''<section class="page-hero"><span class="eyebrow">Contact &amp; aanvragen</span><h1>We helpen je<br>graag verder.</h1><p>Kies hieronder waarvoor je ons contacteert. Het formulier vult zich automatisch aan en bouwt een nette mail op — jij hoeft enkel je gegevens in te vullen.</p></section>'''
    reasons=f'''<section class="section tight">
  <div class="reason-cards">
    <button type="button" class="reason-card reveal" data-reason="Proeftraining aanvragen"><span class="ricon">{IC_BALL}</span><strong>Proeftraining</strong><span>Gratis eens meetrainen</span></button>
    <button type="button" class="reason-card reveal d1" data-reason="Vraag over kalender"><span class="ricon">{IC_CAL}</span><strong>Kalendervraag</strong><span>Uren &amp; wedstrijden</span></button>
    <button type="button" class="reason-card reveal d2" data-reason="Vraag over clubkledij"><span class="ricon">{IC_SHIRT}</span><strong>Clubkledij</strong><span>Bestellen &amp; maten</span></button>
    <button type="button" class="reason-card reveal d3" data-reason="Algemene vraag"><span class="ricon">{IC_HEART}</span><strong>Andere vraag</strong><span>We helpen je graag</span></button>
  </div>
</section>'''
    info='''<div class="info-block reveal">
      <h2>Praktische gegevens</h2>
      <p><strong>Adres</strong><br>Sporthal Veldmeers<br>Leeweg 25, 9270 Laarne<br><span class="muted">(gemeente Laarne, deelgemeente Kalken)</span></p>
      <p><strong>E-mail</strong><br><a href="mailto:info@vckalken.be">info@vckalken.be</a> <button type="button" class="copy-mail" data-copy="info@vckalken.be">Kopieer</button></p>
      <p><strong>Volg ons</strong><br><a href="https://www.facebook.com/vckalken/" target="_blank" rel="noopener">Facebook</a> · <a href="https://www.instagram.com/vc_kalken/" target="_blank" rel="noopener">Instagram</a></p>
      <div class="actions" style="margin-top:8px"><a class="btn ghost-dark" href="https://www.google.com/maps/search/?api=1&query=Leeweg+25,+9270+Laarne" target="_blank" rel="noopener">Route via Maps</a><a class="btn soft" href="mailto:info@vckalken.be">Mail rechtstreeks</a></div>
    </div>'''
    form='''<form id="contactForm" class="form-card reveal d1" novalidate>
      <h2>Stuur een bericht</h2>
      <p class="muted" style="margin-top:-4px">Velden met <span class="req">*</span> zijn verplicht.</p>
      <div class="form-grid">
        <label class="full"><span>Waarvoor contacteer je ons? <span class="req">*</span></span>
          <select name="type" required>
            <option value="Proeftraining aanvragen">Proeftraining aanvragen</option>
            <option value="Vraag over kalender">Vraag over kalender</option>
            <option value="Fout in kalender melden">Fout in kalender melden</option>
            <option value="Vraag over clubkledij">Vraag over clubkledij</option>
            <option value="Algemene vraag">Algemene vraag</option>
          </select>
        </label>
        <label><span>Naam <span class="req">*</span></span><input name="naam" autocomplete="name" required placeholder="Voor- en achternaam"></label>
        <label><span>E-mail <span class="req">*</span></span><input name="email" type="email" autocomplete="email" required placeholder="naam@email.be"></label>
        <label>Telefoon<input name="telefoon" autocomplete="tel" placeholder="0470 00 00 00"></label>
        <label>Geboortedatum / geboortejaar<input name="leeftijd" placeholder="bv. 2012 of 15/03/2012"></label>
        <label class="full">Ploeg of onderwerp
          <select name="ploeg">
            <option>Nog niet zeker / algemeen</option>
            <option>Heren A</option><option>Heren B - Promo 2</option><option>Heren C - Promo 3A</option><option>Heren Vobog</option>
            <option>Dames A</option><option>Dames B</option><option>Dames C</option><option>Dames Vobog</option>
            <option>Volleybalschool</option><option>Gemengd A U11</option><option>Gemengd B U11</option><option>Gemengd U11 2</option><option>Gemengd U13</option>
            <option>Meisjes U13</option><option>Jongens U15 A</option><option>Jongens U15 B</option><option>Meisjes U15 A</option><option>Meisjes U15 B</option><option>Meisjes U17 A</option><option>Meisjes U17 B</option>
            <option>Kalender</option><option>Clubkledij</option><option>Unkerzak</option><option>Sponsors</option>
          </select>
        </label>
        <label class="full">Bericht<textarea name="bericht" rows="5" placeholder="Waarmee kunnen we je helpen? Vermeld bv. een gewenste trainingsdag."></textarea></label>
      </div>
      <details class="mail-details"><summary>Bekijk de mail die wordt opgebouwd</summary>
        <div class="mail-preview"><pre id="mailPreview">Vul het formulier in om de voorbeeldmail te zien.</pre></div>
      </details>
      <button class="btn" type="submit">Verstuur via e-mail</button>
      <div class="form-confirm" id="contactConfirm" hidden><strong>Bijna klaar!</strong> Je e-mailprogramma opent met een ingevulde mail — klik daar nog op <em>verzenden</em>. <span class="muted">Opent er niets? Mail dan rechtstreeks naar <a href="mailto:info@vckalken.be">info@vckalken.be</a>.</span></div>
    </form>'''
    sec=f'<section class="section" style="padding-top:20px"><div class="contact-grid">{info}{form}</div></section>'
    body=head("Contact","Contacteer VC Kalken voor een proeftraining, vraag over de kalender of clubkledij. Adres: Sporthal Veldmeers, Laarne.","contact.html")+header("contact")+"\n<main id=\"inhoud\">\n"+hero+reasons+sec+"\n</main>\n"+FOOTER
    write("contact.html",body)

# ============================================================ WORD LID
def build_wordlid():
    hero='''<section class="page-hero"><span class="eyebrow">Aanvraagformulier</span><h1>Vraag een proeftraining<br>of info aan.</h1><p>Vul alles duidelijk in. De mail wordt automatisch overzichtelijk opgebouwd zodat VC Kalken meteen ziet voor wie, welke ploeg en welke vraag het gaat.</p></section>'''
    form='''<form id="clubForm" class="form-card reveal">
      <h2>Gegevens speler</h2>\n      <p class="muted" style="margin-top:-4px">Velden met <span class="req">*</span> zijn verplicht.</p>
      <div class="form-grid">
        <label><span>Naam speler <span class="req">*</span></span><input name="naam" autocomplete="name" required placeholder="Voor- en achternaam"></label>
        <label>Geboortedatum<input name="geboorte" type="date"></label>
        <label><span>E-mail <span class="req">*</span></span><input name="email" type="email" autocomplete="email" required placeholder="naam@email.be"></label>
        <label>Telefoon<input name="telefoon" autocomplete="tel"></label>
        <label class="full">Gewenste ploeg
          <select name="ploeg">
            <option>Nog niet zeker</option>
            <option>Heren A - Nationale 3</option><option>Heren B - Promo 2</option><option>Heren C - Promo 3A</option><option>Heren Vobog</option>
            <option>Dames A</option><option>Dames B</option><option>Dames C</option><option>Dames Vobog</option>
            <option>Volleybalschool</option><option>Gemengd A U11</option><option>Gemengd B U11</option><option>Gemengd U11 2</option><option>Gemengd U13</option>
            <option>Meisjes U13</option><option>Jongens U15 A</option><option>Jongens U15 B</option><option>Meisjes U15 A</option><option>Meisjes U15 B</option><option>Meisjes U17 A</option><option>Meisjes U17 B</option>
          </select>
        </label>
        <label class="full">Ervaring
          <select name="ervaring"><option>Geen ervaring</option><option>1 jaar</option><option>2-3 jaar</option><option>Meer dan 3 jaar</option><option>Vorige club</option></select>
        </label>
      </div>
      <label>Extra boodschap<textarea name="boodschap" rows="5" placeholder="Wanneer kan je komen meetrainen? Zijn er vragen of opmerkingen?"></textarea></label>
      <div class="mail-preview"><h3>Zo wordt de mail opgebouwd</h3><pre id="mailPreview">Vul het formulier in om de voorbeeldmail te zien.</pre></div>
      <button class="btn" type="submit">Maak duidelijke mail naar VC Kalken</button>
      <p class="muted" style="margin-top:10px">Later kan dit formulier gekoppeld worden aan info@vckalken.be of een formulierplugin.</p>
    </form>'''
    sec=f'<section class="section">{form}</section>'
    body=head("Word lid","Vraag een gratis proeftraining of meer info aan bij VC Kalken. Vul het formulier in en we nemen contact op.","word-lid.html")+header()+"\n<main id=\"inhoud\">\n"+hero+sec+"\n</main>\n"+FOOTER
    write("word-lid.html",body)

# ============================================================ SPONSORS
def build_sponsors():
    hero='''<section class="page-hero"><span class="eyebrow">Sponsors</span><h1>Samen sterker<br>met onze partners.</h1><p>Onze sponsors maken het clubleven mee mogelijk. Wil jij ook partner worden van VC Kalken? Neem gerust contact op.</p></section>'''
    cards=""
    for i in range(1,9):
        d=f"d{i%4}" if i%4 else ""
        cards+=f'<a class="sponsor reveal {d}" href="contact.html?type=sponsor" aria-label="Word sponsor van VC Kalken"><img src="assets/img/sponsor-{i}.png" alt="Sponsor {i}" loading="lazy" onerror="this.onerror=null;this.parentElement.classList.add(\'empty\');this.replaceWith(Object.assign(document.createElement(\'span\'),{{textContent:\'Jouw logo hier?\'}}))"></a>'
    cta='''<div class="sponsor-cta reveal"><span class="eyebrow" style="color:var(--gold-2);justify-content:center;display:flex">Partner worden?</span><h2>Steun VC Kalken</h2><p>Zin om je onderneming te verbinden aan een warme, lokale en sportieve club? We bekijken graag samen welk pakket bij jou past.</p><div class="actions" style="justify-content:center"><a class="btn" href="contact.html?type=sponsor">Word sponsor</a></div></div>'''
    sec=f'<section class="section"><div class="cards four">{cards}</div>{cta}</section>'
    body=head("Sponsors","Bekijk de sponsors en partners van VC Kalken en ontdek hoe je de club kan steunen.","sponsors.html")+header("club")+"\n<main id=\"inhoud\">\n"+hero+sec+"\n</main>\n"+FOOTER
    write("sponsors.html",body)

# ============================================================ CLUBKLEDIJ
def build_clubkledij():
    TW="https://static.twizzit.com/v2/public/form/6717a279ba581ef9e9a359ba213eb3df"
    hero=f'''<section class="page-hero"><span class="eyebrow">Clubkledij</span><h1>VC Kalken clubshop</h1><p>Bestel je clubkledij eenvoudig via het officiële Twizzit-formulier. Eerst de shopknop, dan de categorieën en tot slot hoe bestellen werkt.</p><div class="actions"><a class="btn" target="_blank" rel="noopener" href="{TW}">Open Twizzit-webshop</a><a class="btn ghost-dark" href="contact.html?type=clubkledij">Vraag over clubkledij</a></div></section>'''
    intro=f'''<section class="section tight"><div class="shop-info-card reveal"><img src="logo.png" alt="VC Kalken logo"><div><span class="eyebrow">Officiële clubuitstraling</span><h2>Voor spelers, trainers en supporters</h2><p>Gebruik de clubshop voor trainingskledij, vrije tijd, wedstrijdmateriaal en accessoires. Echte productfoto's, prijzen en maten kunnen later ingevuld worden, terwijl de bestelknoppen naar Twizzit blijven verwijzen.</p></div></div></section>'''
    products=[("Vest","Training","Trainingsvest","Voor training, opwarming en verplaatsingen."),("Shirt","Club","T-shirt","Comfortabel shirt met VC Kalken-uitstraling."),("Hoodie","Vrije tijd","Hoodie","Warme hoodie voor spelers en supporters."),("Short","Wedstrijd","Sportshort","Ideaal voor trainingen en wedstrijden."),("Broek","Training","Trainingsbroek","Voor opwarming, training en clubmomenten."),("Tas","Accessoire","Sporttas","Handig voor schoenen, kledij en uitrusting.")]
    pcards=""
    for i,(vis,tag,t,p) in enumerate(products):
        d=f"d{i%3}" if i%3 else ""
        pcards+=f'<article class="product-card reveal {d}"><div class="product-visual">{vis}</div><div><span class="tag">{tag}</span><h3>{t}</h3><p>{p}</p><a href="{TW}" target="_blank" rel="noopener">Bestel via Twizzit →</a></div></article>'
    grid=f'''<section class="section"><div class="section-head"><div class="reveal"><span class="eyebrow">Overzicht</span><h2>Kies je categorie</h2></div><a class="btn small reveal" target="_blank" rel="noopener" href="{TW}">Bestellen via Twizzit</a></div><div class="product-grid">{pcards}</div></section>'''
    steps=f'''<section class="section"><div class="steps-card reveal"><div><span class="eyebrow" style="color:var(--gold-2)">Bestellen</span><h2>Hoe werkt het?</h2><p>Zo blijft bestellen eenvoudig en duidelijk voor leden en ouders.</p></div><ol><li>Klik op <strong>Open Twizzit-webshop</strong>.</li><li>Kies je artikel, maat en aantal.</li><li>Vul je gegevens in en bevestig je bestelling.</li><li>Je ontvangt verdere info van de club over levering.</li></ol></div></section>'''
    body=head("Clubkledij","Bestel de officiële clubkledij van VC Kalken via de Twizzit-webshop: vesten, shirts, hoodies en meer.","clubkledij.html")+header("club")+"\n<main id=\"inhoud\">\n"+hero+intro+grid+steps+"\n</main>\n"+FOOTER
    write("clubkledij.html",body)

# ============================================================ UNKERZAK
def build_unkerzak():
    hero=f'''<section class="page-hero image">{img("unkerzak.jpg","Unkerzak sfeerbeeld","placeholder-hero.svg","hero-bg")}<span class="eyebrow">Unkerzak</span><h1>Sfeer, clubgevoel<br>en samenkomen.</h1><p>Een herkenbaar stukje VC Kalken dat een eigen, warme plaats verdient op de website.</p></section>'''
    split=f'''<section class="section"><div class="split"><div class="reveal"><span class="eyebrow">Traditie</span><h2>Wat is de Unkerzak?</h2><p class="lead">Deze pagina houdt de Unkerzak zichtbaar als clubactiviteit. Plaats hier de uitleg, praktische info, datum, locatie, inschrijvingen en foto's van vorige edities.</p><div class="actions"><a class="btn" href="fotos.html">Bekijk fotoalbums</a></div></div><div class="info-block reveal d2"><h2>Praktische info</h2><p><strong>Waar?</strong> Kalken</p><p><strong>Voor wie?</strong> Spelers, ouders, supporters en sympathisanten</p><p><strong>Info?</strong> Voeg hier de officiële tekst van de club toe.</p></div></div></section>'''
    body=head("Unkerzak","De Unkerzak van VC Kalken: een warme clubtraditie met sfeer en samenhorigheid.","unkerzak.html",image_card=True)+header("club")+"\n<main id=\"inhoud\">\n"+hero+split+"\n</main>\n"+FOOTER
    write("unkerzak.html",body)

# ============================================================ VERZEKERING
# Vervang dit door de echte ongevalsaangifte van de club (PDF).
INSURANCE_PDF = "assets/verzekering-ongevalsaangifte.pdf"
VV_INSURANCE = "https://www.volleyvlaanderen.be/"
def build_verzekering():
    hero=f'''<section class="page-hero"><span class="eyebrow">Verzekering</span><h1>Een ongeval?<br>Zo ben je verzekerd.</h1><p>Elk lid van VC Kalken is via Volley Vlaanderen verzekerd voor sportongevallen tijdens trainingen en wedstrijden. Hieronder vind je het aangifteformulier en wat je precies moet doen.</p><div class="actions"><a class="btn" href="{INSURANCE_PDF}" target="_blank" rel="noopener">Download ongevalsaangifte (PDF)</a><a class="btn ghost-dark" href="#aangifte">Ongeval melden</a></div></section>'''

    steps=f'''<section class="section">
  <div class="steps-card reveal">
    <div><span class="eyebrow" style="color:var(--gold-2)">Stap voor stap</span><h2>Wat te doen bij een ongeval?</h2><p>Volg deze stappen zodat je aangifte vlot en op tijd in orde is.</p><div class="actions"><a class="btn" href="{INSURANCE_PDF}" target="_blank" rel="noopener">Download formulier</a></div></div>
    <ol>
      <li>Download het <strong>ongevalsaangifteformulier</strong> (knop hierboven) of vraag het aan de club.</li>
      <li>Vul je persoonlijke gegevens in op het eerste luik.</li>
      <li>Laat het <strong>medisch getuigschrift</strong> invullen door je (huis)arts.</li>
      <li>Bezorg het volledig ingevulde formulier <strong>binnen de 8 dagen</strong> aan de club via <a href="mailto:info@vckalken.be" style="color:var(--gold-2)">info@vckalken.be</a>.</li>
      <li>Bewaar alle medische bewijzen en betalingsbewijzen voor de terugbetaling.</li>
    </ol>
  </div>
</section>'''

    info=f'''<section class="section tight">
  <div class="cards two">
    <div class="value-card reveal"><span class="vicon">{IC_SHIELD}</span><b>Wie is verzekerd?</b><span>Alle aangesloten leden zijn via Volley Vlaanderen verzekerd voor lichamelijke ongevallen tijdens club­activiteiten.</span></div>
    <div class="value-card reveal d1"><span class="vicon">{IC_DOC}</span><b>Welke kosten?</b><span>Na tussenkomst van het ziekenfonds behandelt de sportverzekering het resterende saldo volgens de polisvoorwaarden.</span></div>
  </div>
  <p class="muted reveal" style="margin-top:18px">Meer info en de officiële polisvoorwaarden vind je bij <a href="{VV_INSURANCE}" target="_blank" rel="noopener">Volley Vlaanderen</a>. Vragen? Mail gerust naar <a href="mailto:info@vckalken.be">info@vckalken.be</a>.</p>
</section>'''

    form='''<section class="section" id="aangifte">
  <form id="verzekeringForm" class="form-card reveal" novalidate>
    <h2>Ongeval melden bij de club</h2>
    <p class="muted" style="margin-top:-4px">Laat ons weten dat er een ongeval gebeurde. We bezorgen je dan snel het formulier en de verdere stappen. Velden met <span class="req">*</span> zijn verplicht.</p>
    <div class="form-grid">
      <label><span>Naam speler <span class="req">*</span></span><input name="naam" autocomplete="name" required placeholder="Voor- en achternaam"></label>
      <label>Ploeg<input name="ploeg" placeholder="bv. Heren B / Meisjes U15 A"></label>
      <label><span>E-mail <span class="req">*</span></span><input name="email" type="email" autocomplete="email" required placeholder="naam@email.be"></label>
      <label>Telefoon<input name="telefoon" autocomplete="tel" placeholder="0470 00 00 00"></label>
      <label class="full">Datum van het ongeval<input name="datum" type="date"></label>
      <label class="full">Korte beschrijving<textarea name="omschrijving" rows="4" placeholder="Wat is er gebeurd? Welke blessure?"></textarea></label>
    </div>
    <details class="mail-details"><summary>Bekijk de mail die wordt opgebouwd</summary>
      <div class="mail-preview"><pre id="mailPreview">Vul het formulier in om de voorbeeldmail te zien.</pre></div>
    </details>
    <button class="btn" type="submit">Verstuur melding</button>
    <div class="form-confirm" id="contactConfirm" hidden><strong>Bijna klaar!</strong> Je e-mailprogramma opent met een ingevulde mail — klik daar nog op <em>verzenden</em>. <span class="muted">Opent er niets? Mail dan rechtstreeks naar <a href="mailto:info@vckalken.be">info@vckalken.be</a>.</span></div>
  </form>
</section>'''

    body=head("Verzekering","Verzekering en ongevalsaangifte bij VC Kalken: download het formulier, volg de stappen en meld een sportongeval bij de club.","verzekering.html")+header("club")+"\n<main id=\"inhoud\">\n"+hero+steps+info+form+"\n</main>\n"+FOOTER
    write("verzekering.html",body)

# ============================================================ RUN
def run():
    build_index(); build_ploegen()
    for t in TEAMS: build_team(t[0])
    build_nieuws(); build_kalender(); build_fotos(); build_club()
    build_contact(); build_wordlid(); build_sponsors(); build_clubkledij(); build_unkerzak()
    build_verzekering()
    print("ALL PAGES GENERATED")

if __name__=="__main__":
    run()
