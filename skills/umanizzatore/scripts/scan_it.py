#!/usr/bin/env python3
"""scan_it.py - scansione deterministica dei segnali di scrittura IA in italiano.

Le regole stanno in ../regole.json, non in questo file. Ogni regola deve dichiarare
la sua base:

  "fonte"       cita uno o più id del blocco "fonti" (studio, wiki, istituzione)
  "preferenza"  scelta della casa: serve "decisa" (data AAAA-MM-GG) e "motivo"

Ogni regola dichiara anche:

  "forza"  "da solo" (basta un'occorrenza) o "debole da solo" (conta solo
           insieme ad altri segnali nello stesso passaggio)
  "dati"   su quali modelli e in che anno è stato osservato, così si vede
           quando una regola invecchia; per una preferenza, "preferenza"

Una regola senza base valida non viene caricata: lo script si ferma e dice quale.
Così nel catalogo non entra niente che non sia documentato o deciso di proposito.

Uso:
  python3 scan_it.py FILE [FILE ...]
  cat bozza.md | python3 scan_it.py -
  python3 scan_it.py --json bozza.md       # output leggibile da macchina
  python3 scan_it.py --strict bozza.md     # exit 1 se trova qualcosa (per gli hook)
  python3 scan_it.py --check               # valida solo regole.json

Per ignorare un uso voluto, metti `umanizza-ignora` sulla riga.
Il testo nei blocchi di codice (```) e nel codice inline non viene scansionato.
"""

import argparse
import json
import re
import sys
from pathlib import Path

RULES_PATH = Path(__file__).resolve().parent.parent / "regole.json"
IGNORE_MARK = "umanizza-ignora"
FORZE = ("da solo", "debole da solo")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
INLINE_CODE_RE = re.compile(r"`[^`]*`")


def load_rules(path=RULES_PATH):
    """Carica e valida regole.json. Ritorna (fonti, regole compilate)."""
    data = json.loads(path.read_text(encoding="utf-8"))
    fonti = data.get("fonti", {})
    errors = []

    for fid, f in fonti.items():
        for field in ("titolo", "url", "consultata"):
            if not f.get(field):
                errors.append(f"fonte {fid}: manca '{field}'")

    compiled = []
    seen = set()
    for i, r in enumerate(data.get("regole", [])):
        rid = r.get("id") or f"#{i}"
        if rid in seen:
            errors.append(f"regola {rid}: id duplicato")
        seen.add(rid)
        for field in ("id", "etichetta", "correzione", "pattern", "base", "forza", "dati"):
            if not r.get(field):
                errors.append(f"regola {rid}: manca '{field}'")
        if r.get("forza") and r["forza"] not in FORZE:
            errors.append(f"regola {rid}: forza '{r['forza']}' non valida (usa {' o '.join(FORZE)})")
        base = r.get("base")
        if base == "fonte":
            ids = r.get("fonti") or []
            if not ids:
                errors.append(f"regola {rid}: base 'fonte' senza 'fonti'")
            for fid in ids:
                if fid not in fonti:
                    errors.append(f"regola {rid}: fonte '{fid}' non esiste nel blocco fonti")
        elif base == "preferenza":
            if not DATE_RE.match(r.get("decisa", "")):
                errors.append(f"regola {rid}: preferenza senza data 'decisa' (AAAA-MM-GG)")
            if not r.get("motivo"):
                errors.append(f"regola {rid}: preferenza senza 'motivo'")
        elif base:
            errors.append(f"regola {rid}: base '{base}' non valida (usa 'fonte' o 'preferenza')")
        try:
            pats = [re.compile(p, re.IGNORECASE) for p in r.get("pattern", [])]
        except re.error as e:
            errors.append(f"regola {rid}: regex non valida: {e}")
            pats = []
        compiled.append({**r, "_pats": pats})

    if errors:
        sys.exit("regole.json non valido:\n  " + "\n  ".join(errors))
    return fonti, compiled


def scan_text(text, rules, name):
    hits = []
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or IGNORE_MARK in line:
            continue
        visible = INLINE_CODE_RE.sub("", line)
        for r in rules:
            for pat in r["_pats"]:
                for m in pat.finditer(visible):
                    hits.append({
                        "file": name, "riga": lineno, "regola": r["id"],
                        "trovato": m.group(0), "testo": line.strip(),
                    })
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="*")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--regole", type=Path, default=RULES_PATH)
    args = ap.parse_args()

    fonti, rules = load_rules(args.regole)
    if args.check:
        n_f = sum(r["base"] == "fonte" for r in rules)
        print(f"regole.json valido: {len(rules)} regole ({n_f} da fonte, "
              f"{len(rules) - n_f} preferenze), {len(fonti)} fonti.")
        return 0
    if not args.files:
        ap.error("indica almeno un file, oppure - per stdin")
    if not rules:
        print("nessuna regola in regole.json: il catalogo è ancora vuoto.", file=sys.stderr)

    hits = []
    for f in args.files:
        text = sys.stdin.read() if f == "-" else Path(f).read_text(encoding="utf-8")
        hits += scan_text(text, rules, "<stdin>" if f == "-" else f)

    if args.json:
        print(json.dumps(hits, ensure_ascii=False, indent=2))
    else:
        by_rule = {r["id"]: r for r in rules}
        if not hits:
            print("pulito: nessun segnale meccanico trovato."
                  " I segnali di struttura e di ritmo vanno letti a occhio.")
        for rid in dict.fromkeys(h["regola"] for h in hits):
            r = by_rule[rid]
            group = [h for h in hits if h["regola"] == rid]
            print(f"\n{rid}  ({len(group)})  {r['etichetta']}")
            print(f"  forza: {r['forza']}  ·  dati: {r['dati']}")
            print(f"  correzione: {r['correzione']}")
            print(f"  base: {r['base']}" + (f" ({', '.join(r['fonti'])})" if r["base"] == "fonte"
                                          else f" (decisa {r['decisa']})"))
            for h in group:
                print(f"    {h['file']}:{h['riga']}  [{h['trovato']}]  {h['testo'][:100]}")
        if hits:
            print(f"\ntotale: {len(hits)} segnali")
    return 1 if (args.strict and hits) else 0


if __name__ == "__main__":
    sys.exit(main())
