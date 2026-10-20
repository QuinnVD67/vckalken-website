#!/usr/bin/env python3
"""
Haalt de wedstrijdkalenders van VC Kalken op bij Volleyscores en schrijft
data/matches.json en data/matches.js, die de website inlaadt.

Gebruik (vanuit de hoofdmap van de website):
    python3 tools/update_matches.py

Opties:
    --ics-dir MAP   lees <slug>.ics uit een lokale map i.p.v. van internet (testen)
    --out-dir MAP   schrijf de data naar een andere map (standaard: ./data)

Werking in het kort:
  * per ploeg in tools/teams.json wordt de .ics-feed gedownload en omgezet;
  * lukt het ophalen voor een ploeg niet, dan blijven de oude wedstrijden van
    die ploeg gewoon staan (de site wordt dus nooit leeg door een storing);
  * ploegen zonder ics_id worden niet aangeraakt;
  * de bestanden worden enkel herschreven als er echt iets veranderd is,
    zodat er geen nutteloze wijzigingen ontstaan.

Exitcode 1 = geen enkele feed kon worden opgehaald (handig om een melding te krijgen).
Enkel standaardbibliotheek, Python 3.9+.
"""
import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = Path(__file__).resolve().parent / "teams.json"
FEED_URLS = (
    "https://www.volleyscores.be/calendar/team/{id}",
    "http://www.volleyscores.be/calendar/team/{id}",  # sommige feeds waren historisch enkel via http bereikbaar
)

# ------------------------------------------------------------------ tijdzone
try:
    from zoneinfo import ZoneInfo
    BRU = ZoneInfo("Europe/Brussels")
except Exception:  # bv. Windows zonder 'tzdata'-pakket
    BRU = None


def _last_sunday(year, month):
    d = dt.date(year, month, 31 if month in (3, 10) else 30)
    while d.weekday() != 6:
        d -= dt.timedelta(days=1)
    return d


def utc_to_brussels(naive_utc):
    """Zet een naïeve UTC-datetime om naar Belgische wandtijd (naïef)."""
    if BRU is not None:
        return naive_utc.replace(tzinfo=dt.timezone.utc).astimezone(BRU).replace(tzinfo=None)
    y = naive_utc.year
    start = dt.datetime.combine(_last_sunday(y, 3), dt.time(1))
    end = dt.datetime.combine(_last_sunday(y, 10), dt.time(1))
    return naive_utc + dt.timedelta(hours=2 if start <= naive_utc < end else 1)


def to_brussels(naive, tzid):
    """Naïeve datetime in zone tzid -> Belgische wandtijd (naïef)."""
    if not tzid or tzid in ("Europe/Brussels", "Europe/Amsterdam", "Europe/Paris", "Europe/Berlin"):
        return naive
    if BRU is not None:
        try:
            return naive.replace(tzinfo=ZoneInfo(tzid)).astimezone(BRU).replace(tzinfo=None)
        except Exception:
            pass
    return naive


# ------------------------------------------------------------------ ICS-parser
def unfold(text):
    return re.sub(r"\r?\n[ \t]", "", text)


def unescape(v):
    return (v.replace("\\n", "\n").replace("\\N", "\n").replace("\\,", ",")
             .replace("\\;", ";").replace("\\\\", "\\")).strip()


def parse_events(ics_text):
    """Geeft een lijst dicts {prop: (waarde, {param: waarde})} per VEVENT."""
    events, cur = [], None
    for line in unfold(ics_text).splitlines():
        if line == "BEGIN:VEVENT":
            cur = {}
        elif line == "END:VEVENT":
            if cur is not None:
                events.append(cur)
            cur = None
        elif cur is not None and ":" in line:
            head, value = line.split(":", 1)
            name, *params = head.split(";")
            pdict = {}
            for p in params:
                if "=" in p:
                    k, v = p.split("=", 1)
                    pdict[k.upper()] = v.strip('"')
            cur.setdefault(name.upper(), (value, pdict))
    return events


def parse_dt(value, params):
    """-> (datetime naïef in Belgische wandtijd, heeft_uur)"""
    v = value.strip()
    if params.get("VALUE") == "DATE" or re.fullmatch(r"\d{8}", v):
        return dt.datetime.strptime(v[:8], "%Y%m%d"), False
    if v.endswith("Z"):
        return utc_to_brussels(dt.datetime.strptime(v[:-1], "%Y%m%dT%H%M%S")), True
    naive = dt.datetime.strptime(v, "%Y%m%dT%H%M%S")
    return to_brussels(naive, params.get("TZID")), True


def split_teams(summary):
    """'Thuis - Bezoekers' splitsen, ook als een ploegnaam zelf ' - ' bevat
    (bv. 'Vamos STEKENE - SINT-GILLIS-WAAS (S) - VC KALKEN (S)')."""
    parts = [p.strip() for p in re.split(r"\s+-\s+", summary)]
    if len(parts) == 2:
        return parts[0], parts[1]
    if len(parts) < 2:
        return summary.strip(), ""
    k = next((i for i, p in enumerate(parts) if "kalken" in p.lower()), None)
    if k is None:
        mid = len(parts) // 2
        return " - ".join(parts[:mid]), " - ".join(parts[mid:])
    if k == 0:
        return parts[0], " - ".join(parts[1:])
    if k == len(parts) - 1:
        return " - ".join(parts[:k]), parts[k]
    return " - ".join(parts[:k + 1]), " - ".join(parts[k + 1:])


NUMBER_RE = re.compile(r"\b[A-Z0-9]{2,}(?:-[A-Za-z0-9]{1,4})*-\d{3,4}\b")


def event_to_match(ev, team, club_url):
    summary = unescape(ev.get("SUMMARY", ("", {}))[0])
    if not summary or "DTSTART" not in ev:
        return None
    start, has_time = parse_dt(*ev["DTSTART"])
    home, away = split_teams(summary)
    desc = unescape(ev.get("DESCRIPTION", ("", {}))[0])
    hall = unescape(ev.get("LOCATION", ("", {}))[0])
    status = ev.get("STATUS", ("", {}))[0].strip().upper()
    cancelled = status == "CANCELLED" or "afgelast" in (summary + " " + desc).lower()
    m = NUMBER_RE.search(desc) or NUMBER_RE.search(summary)
    return {
        "team": team["slug"],
        "cat": team["cat"],
        "date": start.strftime("%d/%m/%Y"),
        "time": start.strftime("%H:%M") if has_time else "",
        "iso": start.strftime("%Y-%m-%dT%H:%M"),
        "home": home,
        "away": away,
        "hall": hall,
        "league": team["league"],
        "number": m.group(0) if m else "",
        "loc": "home" if "kalken" in home.lower() else "away",
        "cancelled": bool(cancelled),
        "url": club_url,
    }


# ------------------------------------------------------------------ ophalen
def download(team_id):
    last = None
    for template in FEED_URLS:
        url = template.format(id=team_id)
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "vckalken-website-updater/1.0"})
                with urllib.request.urlopen(req, timeout=30) as r:
                    return r.read().decode("utf-8", errors="replace")
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                last = e
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"ophalen mislukt ({last})")


def load_previous(out_dir):
    p = out_dir / "matches.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"matches": []}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ics-dir", type=Path)
    ap.add_argument("--out-dir", type=Path, default=ROOT / "data")
    args = ap.parse_args()

    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    club_url = cfg["club_url"]
    teams = cfg["teams"]
    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    previous = load_previous(out_dir)
    old = previous.get("matches", [])
    feed_slugs = {t["slug"] for t in teams if t.get("ics_id")}
    result = [m for m in old if m.get("team") not in feed_slugs]  # ploegen zonder feed blijven staan
    ok = failed = 0

    for team in teams:
        if not team.get("ics_id"):
            continue
        slug = team["slug"]
        previous_team = [m for m in old if m.get("team") == slug]
        try:
            if args.ics_dir:
                text = (args.ics_dir / f"{slug}.ics").read_text(encoding="utf-8")
            else:
                text = download(team["ics_id"])
            if "BEGIN:VCALENDAR" not in text:
                raise RuntimeError("antwoord is geen agenda-bestand")
            fresh = [m for m in (event_to_match(e, team, club_url) for e in parse_events(text)) if m]
            if not fresh and previous_team:
                raise RuntimeError("feed is leeg, oude gegevens blijven behouden")
            result.extend(fresh)
            ok += 1
            print(f"  ok   {slug:15s} {len(fresh):3d} wedstrijden")
        except Exception as e:
            failed += 1
            result.extend(previous_team)
            print(f"  FOUT {slug:15s} {e} ({len(previous_team)} oude wedstrijden behouden)", file=sys.stderr)

    result.sort(key=lambda m: (m["iso"], m["team"]))
    if result == old and previous.get("updated"):
        payload = {"updated": previous["updated"], "matches": result}  # tijdstip enkel wijzigen bij echte wijzigingen
    else:
        now = dt.datetime.now(BRU) if BRU else dt.datetime.now()
        payload = {"updated": now.strftime("%Y-%m-%dT%H:%M"), "matches": result}

    files = {
        "matches.json": json.dumps(payload, ensure_ascii=False, indent=1) + "\n",
        "matches.js": "/* Automatisch gegenereerd door tools/update_matches.py. Niet met de hand aanpassen. */\n"
                      "window.VCK_DATA = " + json.dumps(payload, ensure_ascii=False) + ";\n",
    }
    changed = []
    for name, content in files.items():  # enkel schrijven als de inhoud echt verschilt
        path = out_dir / name
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8")
            changed.append(name)
    if changed:
        print(f"Bijgewerkt: {len(result)} wedstrijden ({ok} feeds ok, {failed} mislukt).")
    else:
        print(f"Geen wijzigingen ({ok} feeds ok, {failed} mislukt).")

    return 1 if ok == 0 and failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
