# Evidenze

Cosa sappiamo, con che forza, e cosa manca. Ricerca del 2026-09-28. Le regole dello
scanner (`../regole.json`) e il catalogo (`segnali.md`) citano gli id usati qui.

**In sintesi: la base di prove è sottile.** Due studi quantitativi, ciascuno su un solo
genere; un gruppo di lavori qualitativi di linguisti italiani; qualche commento di
istituzioni. Nessuno studio ordina i segnali italiani tra loro, tra modelli o tra generi.
Gran parte dei dati viene da modelli del 2023-2024.

Legenda della verifica:
- **controllato**: il dato è stato riletto nel testo della fonte.
- **da agente**: riportato dalla ricerca, non riletto a mano. Da ricontrollare prima di
  costruirci una regola.

## Fonti usate

### meier2026 · rivista peer-reviewed · CC BY-NC-SA 4.0

Meier, F. (2026). *Marking intersubjectivity in human-written and AI-generated editorials
published in Il Foglio.* AI-Linguistica 3(1). https://doi.org/10.62408/ai-ling.v3i1.65

- Corpus: 25 editoriali di *Il Foglio AI* contro 25 editoriali umani non firmati di
  *Il Foglio*, aprile-maggio 2025. Il modello non è dichiarato.
- Testi IA: 10.573 parole in 649 frasi. Umani: 8.547 parole in 302 frasi. Le frasi IA
  sono molto più corte. **controllato**
- Marcatori di negazione e contrasto ("disclaim"): 34,6 contro 20,7 ogni 1.000 parole.
  **controllato**
- Coppie negazione + controbattuta ("non X, ma Y") almeno una volta in ogni editoriale
  IA, quasi assenti negli umani. **controllato**
- *Eppure*: 9 occorrenze, tutte nei testi IA. **controllato**
- Marcatori di obbligo circa tre volte più frequenti nell'IA; "dobbiamo" come appello al
  lettore. **controllato**
- Concessione e poi "Ma" ("Punire Le Pen, sì. Ma…", "Vero. Ma…"): negli editoriali IA
  la concessione apre spesso una controbattuta con *ma*. L'articolo la presenta come
  differenza dagli umani ma non dà un conteggio. **controllato**
- *Però* come inciso a metà frase: 8 occorrenze, solo negli umani. Marcatori di
  controaspettativa: 11 tipi negli umani contro 5 nell'IA, che generalizza *ma*.
  **controllato**

### sciandra2026 · rivista peer-reviewed · CC BY-NC-ND 4.0

Sciandra, Dal Cero, Cortelazzo, Tuzzi (2026). *AI detection in Italian essays through
different text representations and adversarial robustness evaluation.* Scientific Reports
16, 21499. https://www.nature.com/articles/s41598-026-51613-9

- Corpus: 500 temi di studenti universitari italiani e 500 temi scritti da ChatGPT
  (GPT-3.5) sugli stessi titoli, raccolti nel 2024. **controllato**
- Parole funzionali più importanti per il classificatore: *conclusione* spinge verso IA;
  *perché*, *si*, *non* verso umano. **controllato**
- Nell'esempio SHAP del modello BERT spiccano *in conclusione*, *inoltre*, *tuttavia*
  (un solo testo mostrato). **controllato**
- Tabella 1, medie IA contro umano: meno variabilità nella lunghezza delle frasi (dev.
  std. 7,08 contro 14,01 token), frase più lunga più corta, più frasi, più parole lunghe,
  meno avverbi e pronomi. **controllato**
- Unire frasi corte in frasi lunghe bastava a far classificare come umani metà dei testi
  analizzati (con il modello basato sui tratti del testo). **controllato**

### antonelli2025 · rivista, saggio qualitativo · CC BY-SA 4.0

Antonelli, G. (2025). *Storia brevissima (ma molto intensa) dell'IA-taliano.* Lingue e
Culture dei Media 9(1): 4-50. https://doi.org/10.54103/2532-1803/29341

- Prove ripetute da novembre 2023 a giugno 2025 su ChatGPT, Copilot, Gemini, Claude.
  Niente conteggi.
- Connettivi (*pertanto*, *inoltre*, *tuttavia*, *in ogni caso*) messi sistematicamente
  in evidenza, soprattutto in ChatGPT-3.5. **controllato**
- Aperture che danno ragione: "Hai ragione" (ChatGPT 3.5, Copilot), "Non sbagli affatto"
  (ChatGPT 4.0), "Hai pienamente ragione" (Claude), "Hai perfettamente ragione!"
  (Gemini). **controllato**
- In registro social: emoji "quasi uno per rigo" e almeno cinque hashtag, almeno uno in
  inglese (Copilot, Claude, ChatGPT; Gemini diverso). **controllato**
- Coppie coordinate, "non X, ma Y" e "non solo… ma anche" simmetrici nella scrittura
  creativa; grassetto. **da agente**
- Errori di grammatica e interferenze dall'inglese "quasi scomparsi" nel 2025: le regole
  su errori e calchi rischiano di essere vecchie. **da agente**

### cicero2023 · rivista peer-reviewed, qualitativo

Cicero, F. (2023). *L'italiano delle intelligenze artificiali generative.* Italiano
LinguaDue 15(2): 733-761. https://doi.org/10.54103/2037-3597/21990

- ChatGPT-3.5, Bing Chat, Bard, 2023.
- Cornice rituale: "Sarò felice di aiutarti…", "Spero che questi suggerimenti ti
  aiutino…", "Se hai altre domande o richieste, non esitare a chiedere." **controllato**
- Riepilogo finale divulgativo: "Quindi, in breve, …". **controllato**
- "Questo processo…" che riassume la frase prima. **controllato** (esempio in un testo
  ChatGPT)
- Testi informativi di 200-300 parole in 7-10 paragrafi brevi, elenchi frequenti;
  stesso soggetto ripetuto in ogni frase; poca subordinazione; gerundi sul modello
  inglese. **da agente**

### crusca2026 · istituzione

Palermo, M. (2026). *Sui testi generati dall'intelligenza artificiale. Verso un nuovo
rapporto tra norma e uso?* Accademia della Crusca.
https://accademiadellacrusca.it/it/contenuti/sui-testi-generati-dallintelligenza-artificiale-verso-un-nuovo-rapporto-tra-norma-e-uso/46422

- "generoso ricorso a connettivi di raccordo tra le frasi" (cita Antonelli 2026).
  **controllato**
- Diffusione delle subordinate col gerundio irrelato rispetto al soggetto della
  principale. **controllato**
- Articolo omesso ("ci vediamo settimana prossima") presentato come corretto. **controllato**

### treccani-lineetta · istituzione, norma tipografica

Treccani, Magazine Lingua italiana, *I punti della situazione*, parte 9.
https://www.treccani.it/magazine/lingua_italiana/articoli/scritto_e_parlato/punteggiatura9.html

- Le lineette doppie per un inciso sono italiano normale. La pagina usa la lineetta
  corta "–" (187 volte, 2 volte la lunga). **controllato**
- La lineetta singola "è poco frequente e spesso è percepita come un calco interpuntivo
  dall'inglese". **controllato**
- Conseguenza: la regola inglese "ogni trattino è un segnale" non vale in italiano.
  Nessuno studio misura le lineette nell'italiano generato: la regola dello scanner è una
  norma tipografica, non una prova di IA.

## Fonti trovate ma non usate per le regole

- **Wikipedia in italiano, [WP:IA](https://it.wikipedia.org/wiki/Wikipedia:Intelligenza_artificiale)**
  (linea guida, CC BY-SA 4.0). Non c'è un equivalente di "Signs of AI writing" né un
  progetto di pulizia. La pagina dice di cercare allucinazioni e fonti che non
  sostengono il testo; sullo stile nota solo il tono sicuro e assertivo. **da agente**
- **De Cesare (2026)**, *L'italiano sintetico dell'intelligenza artificiale generativa*,
  Cesati. Letto solo tramite la recensione di Gualdo su Treccani (2026-04-28): frasi
  principali, strutture binarie e ternarie, coppie di aggettivi, "non solo… ma",
  esplicitezza e ridondanza, pochi connettivi, virgola seriale prima di "e", mesi in
  maiuscolo, prestiti e parole inesistenti (GPT-4). Fonte secondaria: da leggere
  direttamente prima di farne regole. **da agente**
- **Tavosanis (2025)**, *Grammatica generata*, AI-Linguistica 2(2): 18 deviazioni
  grammaticali in 7.039 token di ChatGPT-4o; avverte che gli errori non separano bene
  testi IA e umani. **da agente**
- **Cicero (2025)**, *Esercizi di stile*, AI-Linguistica 2(2): calchi dall'inglese in un
  libro per bambini generato, ma tradotto dall'inglese, quindi il dato è confuso.
  **da agente**
- **Garassino et al. (2024)**, AI-Linguistica 1(1): slogan con verbi di cambiamento
  ("dobbiamo costruire il nostro futuro") nei testi politici di ChatGPT-3.5. **da agente**
- **Puccetti et al. (ACL 2024)**: 93 valutatori distinguono notizie italiane generate al
  64% nel caso migliore. **da agente**
- **DeSegMa-IT, EVALITA 2026**: rilevatori, nessuna analisi dei tratti. **da agente**

## Non sono prove

Articoli divulgativi, SEO e liste del tipo "le parole che tradiscono ChatGPT": non si
usano per le regole. Esempi trovati: pezzi su OpenAI e la lineetta (tuttotech.net,
punto-informatico.it), proftext.com, ihal.it, libero.it, fondazioneleonardo.com, una
guida su Substack scritta con l'IA, marcomunich.com, il repo GitHub
mario-montanari/italiano-scrittura-anti-ai.

## Cosa manca

- Un elenco italiano di segnali mantenuto da una comunità (come WikiProject AI Cleanup).
- Uno studio di frequenza lessicale sull'italiano dopo ChatGPT (l'equivalente di *delve*).
- Qualsiasi classifica dei segnali tra modelli recenti e tra generi.
- Dati su lineette, grassetto ed elenchi nell'italiano generato dai modelli del 2025-2026.
- Qualsiasi dato su testi brevi da social o copioni video.
