# umanizzatore

*Bozza.* Le skill per togliere i segni della scrittura IA dai testi **in italiano**,
per [Claude Code](https://code.claude.com/docs/en/skills) e altri agenti che leggono
`SKILL.md`.

È un fork di [humanizer-stack](https://github.com/NulightJens/humanizer-stack), con
[humanizer](https://github.com/blader/humanizer) aggiornato alla v3.1.0 e un livello
italiano nuovo.

## Perché un livello italiano

Gli strumenti che esistono sono tarati sull'inglese. Gli schemi di `humanizer`
descrivono scelte di default e valgono in ogni lingua, ma gli esempi, l'elenco di
parole e gli scanner sono inglesi: su un copione italiano gli scanner di humanizer-stack
trovano soltanto le lineette.

E alcune regole inglesi in italiano sono sbagliate. La più nota: "ogni trattino è un
segnale di IA". In italiano le lineette doppie per un inciso sono normali (Treccani).

## La regola

**Nel catalogo entra solo ciò che una fonte nomina in italiano, oppure una preferenza
dichiarata come tale, con data e motivo.** Lo scanner non carica una regola senza base.
Articoli SEO e liste di "parole che tradiscono ChatGPT" non contano come fonti.

Le prove sono poche: due studi quantitativi (Meier 2026 su editoriali del *Foglio*,
Sciandra et al. 2026 su temi universitari), alcuni lavori qualitativi di linguisti
italiani, la Crusca e la Treccani. Nessuna classifica dei segnali italiani esiste. Il
quadro completo, con quello che manca, è in
[`skills/umanizzatore/references/evidenze.md`](skills/umanizzatore/references/evidenze.md).

## Cosa c'è

```
skills/
  umanizzatore/                 il livello italiano (nuovo)
    SKILL.md                    il metodo: humanizer → catalogo italiano → structural-humanizer
    regole.json                 regole dello scanner, ognuna con fonte o preferenza
    references/segnali.md       il catalogo: scansionabili, a occhio, vecchi, da tarare
    references/evidenze.md      le fonti, cosa dicono, cosa è stato controllato
    scripts/scan_it.py          scanner deterministico
  humanizer/                    blader/humanizer v3.1.0, invariato (git subtree)
  structural-humanizer/         da humanizer-stack, invariato
scripts/copy_scan.py            scanner inglese di humanizer-stack, invariato
docs/
  PIPELINE.md                   come si concatenano i passaggi
  copy-tells-en.md              i segnali inglesi dei testi promozionali, da humanizer-stack
```

## Installazione

```bash
git clone <questo repo> umanizzatore
cd umanizzatore
./install.sh                  # umanizzatore + structural-humanizer
./install.sh --with-humanizer # anche humanizer, se non lo hai già come plugin
```

## Uso

```
umanizza questo post
togli l'effetto IA da script.md
```

Scanner:

```bash
python3 skills/umanizzatore/scripts/scan_it.py bozza.md
python3 skills/umanizzatore/scripts/scan_it.py --json bozza.md
python3 skills/umanizzatore/scripts/scan_it.py --strict bozza.md   # exit 1 se trova qualcosa
python3 skills/umanizzatore/scripts/scan_it.py --check             # valida regole.json
```

`umanizza-ignora` su una riga la esclude.

## Aggiornare dagli originali

```bash
git subtree pull --prefix=skills/humanizer blader main --squash   # humanizer
git fetch stack && git merge stack/main                           # humanizer-stack
```

## Limiti

- Le regole vengono da modelli del 2023-2025 e da pochi generi (temi, editoriali,
  risposte di chatbot). Nessuna fonte riguarda copioni video o post social brevi.
- Lo scanner trova la parte meccanica. Ritmo, forma e contenuto vuoto li vede solo chi
  legge.
- Lo scopo non è ingannare i rilevatori. È un testo che suoni scritto da una persona
  con un punto di vista, perché una persona l'ha scritto.

## Licenze

MIT per il lavoro di questo repo. Parti con termini a monte, incluso materiale
CC BY-SA 4.0. Vedi [ATTRIBUTION.md](ATTRIBUTION.md).
