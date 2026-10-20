# Automatische wedstrijdkalender

De kalenderpagina en het blokje "Wedstrijden deze week" op de homepage lezen hun
gegevens uit `data/matches.js`. Dat bestand wordt **niet met de hand** onderhouden:
`tools/update_matches.py` maakt het aan op basis van de officiële agendafeeds van
Volleyscores (één per ploeg, met het volledige seizoen).

## Eenmalig instellen (GitHub)

1. Zet de map van de website in een GitHub-repository (de inhoud van de zip in de root).
2. Controleer onder *Settings → Actions → General → Workflow permissions* dat
   "Read and write permissions" aanstaat.
3. Klaar. `.github/workflows/update-matches.yml` draait elke 3 uur en commit enkel als er
   iets veranderd is. Wil je meteen testen: tabblad *Actions → Wedstrijden bijwerken → Run workflow*.

Hoeft de site na een commit nog gepubliceerd te worden (GitHub Pages, Netlify of Cloudflare
Pages doen dat vanzelf), dan is er verder niets te doen. Staat de site op gewone
webhosting met FTP, dan moet er nog een uploadstap bij: laat het weten.

## Zelf draaien

```
python3 tools/update_matches.py
```

Heb je geen internet of wil je testen? `--ics-dir map` leest `<ploeg>.ics` uit een lokale map.

## Wat als er iets misgaat?

- Mislukt het ophalen voor één ploeg, dan blijven de oude wedstrijden van die ploeg staan.
- Mislukken alle feeds, dan staat de workflow op rood (GitHub stuurt dan een mail).
- De site toont onderaan de filters wanneer de kalender voor het laatst gewijzigd is.

## Aanpassen

`tools/teams.json`: per ploeg het nummer uit de Volleyscores-agendalink
(`volleyscores.be/calendar/team/<nummer>`), de categorie en de reeksnaam.
Nieuw seizoen of nieuwe ploeg? Pas de nummers aan of voeg een regel toe.
Ploegen zonder `ics_id` (bv. Vobog, U11) worden niet overschreven: wedstrijden die je
voor die ploegen met de hand in `data/matches.json` zet, blijven staan.
