# Segnali in italiano

Il catalogo italiano. Si aggiunge ai 26 schemi di `humanizer` (v3.1.0), non li
sostituisce: quelli descrivono scelte di default che valgono in ogni lingua. Qui c'è
solo ciò che una fonte nomina in italiano, oppure una preferenza della casa dichiarata
come tale. Le fonti sono in [evidenze.md](evidenze.md).

**Nessuna classifica.** Nessuna fonte ordina i segnali italiani tra loro. L'ordine qui
sotto segue la forza delle prove: prima i dati quantitativi recenti, poi i qualitativi,
poi quelli vecchi.

## 1. Segnali che lo scanner trova

Stanno in `../regole.json`. Qui solo l'elenco e il legame con `humanizer`.

| id | Segnale | humanizer | Forza | Fonti |
|---|---|---|---|---|
| `non-x-ma-y` | "non X, ma Y", "non solo X, ma (anche) Y" | §1 | da solo | meier2026, antonelli2025 |
| `apertura-servile` | "Hai (pienamente) ragione", "Non sbagli affatto" a inizio testo | §22 | da solo | antonelli2025 |
| `cornice-chat` | "Sarò felice di aiutarti", "Spero che… ti aiutino", "non esitare a chiedere" | §22 | da solo | cicero2023 |
| `concessione-poi-ma` | "Sì. Ma…", "Vero. Ma…" | §1, §5 | debole | meier2026 |
| `eppure` | "eppure" come controbattuta | §1 | debole | meier2026 |
| `dobbiamo` | obbligo rivolto al lettore | nessuno | debole | meier2026 |
| `in-conclusione` | "In conclusione", "Quindi, in breve" | §13, §2 | debole | sciandra2026, cicero2023 |
| `connettivo-in-testa` | Pertanto, Inoltre, Tuttavia, In ogni caso a inizio frase | nessuno | debole | antonelli2025, crusca2026, sciandra2026 |
| `lineetta-lunga` | "—" invece di "–" | §8 | debole | treccani-lineetta (norma, non prova di IA) |

"Da solo" basta una volta. "Debole" conta solo se nello stesso passaggio ci sono altri
segnali, come i *weak alone* di `humanizer`.

## 2. Segnali da leggere a occhio

Nessuna regex li prende in modo affidabile.

- **Frasi tutte della stessa misura.** Nei temi di GPT-3.5 la lunghezza delle frasi varia
  circa la metà che negli umani, e la frase più lunga è più corta (sciandra2026). Negli
  editoriali IA le frasi sono molto più corte (meier2026). Alterna frasi brevi e lunghe;
  unire due frasi corte è la modifica che più spesso sposta un testo verso l'umano.
- **Pochi avverbi e pronomi, parole lunghe.** Il tema IA usa meno avverbi e pronomi e più
  parole oltre i 7 caratteri (sciandra2026). Non è una regola da applicare parola per
  parola: è un sintomo di prosa nominale e astratta.
- **Pochi tipi di connettivo avversativo.** L'IA ripete *ma* ed *eppure*; gli umani
  variano, e usano *però* come inciso (meier2026).
- **Coppie e terne coordinate.** "La grammatica e la sintassi", tre aggettivi di fila
  (antonelli2025; De Cesare 2026 via recensione). Corrisponde a `humanizer` §6.
- **Gerundio irrelato in coda.** "…, lasciando un'eredità di mistero" (crusca2026). È la
  forma italiana di `humanizer` §15.
- **Stesso soggetto a ogni frase** ("Il miele è… Il miele è…") e **"Questo processo…"** che
  riassume la frase prima (cicero2023). Corrisponde a `humanizer` §7.
- **Emoji quasi a ogni riga e cinque o più hashtag**, almeno uno in inglese, nei testi
  social (antonelli2025). Corrisponde a `humanizer` §20.

## 3. Segnali probabilmente vecchi

Osservati su modelli del 2023-2024. Antonelli riporta che errori e interferenze
dall'inglese erano quasi scomparsi nel 2025. Non farne regole senza dati nuovi.

- Virgola seriale prima di "e", mesi con la maiuscola ("7 Marzo 1908"), prestiti e
  parole inesistenti ("mentoreggiare"): GPT-4, De Cesare 2026 via recensione.
- Calchi come "fece un desiderio", "guardò intorno": Cicero 2025, su un testo tradotto.
- Errori di accordo e coordinazioni zoppe ("sia… che"): ChatGPT-4o, Tavosanis 2025, che
  avverte che gli errori non distinguono IA e umani.

## 4. Schemi di `humanizer` da tarare sull'italiano

- **§8 Lineette.** In italiano le lineette doppie per un inciso sono normali
  (treccani-lineetta). Non togliere "–" di regola; segnala solo "—" e la lineetta
  singola che aggancia una frase.
- **§10 Composti col trattino.** Regola dell'ortografia inglese. Nessuna fonte italiana
  raccolta: non applicarla all'italiano.
- **§12 Parole.** L'elenco è inglese. Per l'italiano non esiste ancora uno studio di
  frequenza: l'elenco italiano è vuoto finché non lo riempiamo.
- **§21 Virgolette curve.** Le convenzioni italiane sulle virgolette non sono state
  ricercate: non applicare finché non c'è una fonte.

Tutti gli altri schemi valgono così come sono. Gli esempi sono in inglese: cerca la
costruzione equivalente.

## 5. Preferenze della casa

Scelte nostre, dichiarate come tali, con data e motivo. Vanno anche in `../regole.json`
con `"base": "preferenza"` quando si possono cercare con una regex.

*(vuoto)*
