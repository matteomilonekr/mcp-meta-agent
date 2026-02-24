# Cos'e' Meta Ads Manager MCP e Perche' Ti Serve

Immagina di poter gestire tutte le tue campagne Meta Ads **parlando con un assistente AI**, senza mai aprire il Business Manager.

Meta Ads Manager MCP collega Claude direttamente al tuo account pubblicitario Meta. Questo significa che puoi dire cose come:

> "Mostrami come stanno andando le mie campagne questa settimana"

> "Crea una campagna di lead generation con budget 50 euro al giorno per l'Italia"

> "Metti in pausa tutte le campagne che spendono troppo"

...e Claude lo fa per te. In tempo reale. Sul tuo account.

---

## Cosa puoi fare

Con **36 strumenti** organizzati in **8 categorie**, copri tutto quello che fai nell'Ads Manager:

| Categoria | Strumenti | Cosa fai |
|-----------|:-:|----------|
| **Campagne** | 6 | Creare, modificare, mettere in pausa, riattivare, eliminare |
| **Ad Set** | 5 | Targeting, budget, posizionamenti, ottimizzazione |
| **Inserzioni** | 4 | Creare, modificare, eliminare le singole ads |
| **Analytics** | 5 | Performance, trend giornalieri, confronti paralleli, export CSV/JSON |
| **Audience** | 5 | Custom audience, lookalike, stime di reach |
| **Creativita'** | 4 | Creare creativi, caricare immagini, anteprima formati |
| **OAuth** | 5 | Autenticazione e gestione token |
| **Account** | 2 | Lista account e health check |

## Cosa NON devi fare

- Non devi scrivere codice
- Non devi conoscere le API di Meta
- Non devi navigare menu complicati
- Parli in italiano (o in qualsiasi lingua), Claude capisce e agisce

---

## Come funziona in pratica

```
Tu scrivi:  "Come stanno andando le mie campagne attive?"

Claude:     Recupera i dati dal tuo account Meta
            Ti mostra una tabella con impressioni, click, spesa, CTR, CPC
            Ti suggerisce cosa ottimizzare
```

Tutto avviene dentro Claude. Niente tab in piu', niente dashboard.

---

## Quanto tempo risparmi

| Attivita' | Prima (manuale) | Con Claude |
|-----------|:-:|:-:|
| Check performance mattutino | 15-20 min | 10 sec |
| Confronto tra campagne | 30 min + Excel | 10 sec |
| Creare campagna completa | 20-30 min | 1 min |
| Report mensile per cliente | 1-2 ore | 30 sec |
| Mettere in pausa campagna | 2 min + 5 click | 1 frase |
| Creare lookalike audience | 5-10 min | 1 frase |

> Se gestisci anche solo 3 clienti e dedichi 1 ora/giorno all'Ads Manager:
> **risparmi ~20 ore al mese.**

---

## Sicurezza

- Le campagne si creano **sempre in pausa** — mai attivazioni accidentali
- **Tu dai le istruzioni, Claude esegue** — nessuna azione autonoma
- Token gestiti via variabili d'ambiente — nessun segreto nel codice
- OAuth completo con token a 60 giorni rinnovabili

---

## I 36 Tool: Lista Completa

### Campagne (6)

| Tool | Cosa fa |
|------|---------|
| `list_campaigns` | Elenca tutte le campagne dell'account |
| `create_campaign` | Crea una nuova campagna (sempre in pausa) |
| `update_campaign` | Modifica nome, budget, stato di una campagna |
| `pause_campaign` | Mette in pausa una campagna |
| `resume_campaign` | Riattiva una campagna in pausa |
| `delete_campaign` | Elimina una campagna |

### Ad Set (5)

| Tool | Cosa fa |
|------|---------|
| `list_ad_sets` | Elenca gli ad set di una campagna |
| `create_ad_set` | Crea un ad set con targeting, budget, ottimizzazione |
| `update_ad_set` | Modifica un ad set esistente |
| `pause_ad_set` | Mette in pausa un ad set |
| `delete_ad_set` | Elimina un ad set |

### Inserzioni (4)

| Tool | Cosa fa |
|------|---------|
| `list_ads` | Elenca le ads di un ad set |
| `create_ad` | Crea una nuova ad collegando creative e ad set |
| `update_ad` | Modifica un'ad esistente |
| `delete_ad` | Elimina un'ad |

### Analytics (5)

| Tool | Cosa fa |
|------|---------|
| `get_insights` | Performance di campagne, ad set o ads |
| `compare_performance` | Confronta piu' campagne in parallelo |
| `get_daily_trends` | Trend giornalieri con indicatore di direzione |
| `get_attribution_data` | Dati di attribuzione per finestra |
| `export_insights` | Esporta in CSV o JSON |

### Audience (5)

| Tool | Cosa fa |
|------|---------|
| `list_audiences` | Elenca custom e lookalike audience |
| `create_custom_audience` | Crea audience da website, app, engagement |
| `create_lookalike` | Crea audience simile a una esistente |
| `estimate_audience_size` | Stima reach e impressioni |
| `delete_audience` | Elimina un'audience |

### Creativita' (4)

| Tool | Cosa fa |
|------|---------|
| `list_creatives` | Elenca le creative dell'account |
| `create_creative` | Crea una creative con immagine, testo, CTA |
| `upload_image` | Carica un'immagine da URL |
| `preview_ad` | Anteprima dell'ad su diversi formati |

### OAuth (5)

| Tool | Cosa fa |
|------|---------|
| `generate_auth_url` | Genera URL per autenticazione OAuth |
| `exchange_code_for_token` | Scambia codice OAuth per token |
| `refresh_to_long_lived_token` | Estende il token a 60 giorni |
| `get_token_info` | Mostra info e scadenza del token |
| `validate_token` | Verifica che il token sia valido |

### Account (2)

| Tool | Cosa fa |
|------|---------|
| `list_ad_accounts` | Elenca tutti gli account pubblicitari |
| `health_check` | Verifica connessione, token e stato del server |

---

## Indice della Guida

| # | Capitolo |
|---|---------|
| 00 | [Introduzione](./00-introduzione.md) — Cos'e' e perche' ti serve |
| 01 | [Installazione e Setup](./01-setup.md) — Configura tutto in 10 minuti |
| 02 | [Primi Comandi](./02-primi-comandi.md) — Inizia subito a usarlo |
| 03 | [Creare una Campagna](./03-creare-campagna.md) — Dal brief al lancio |
| 04 | [Analisi e Report](./04-analisi-report.md) — Performance, trend, export |
| 05 | [Gestire le Audience](./05-audience.md) — Custom, lookalike, stime |
| 06 | [Creativita'](./06-creativita.md) — Creativi, immagini, anteprima |
| 07 | [OAuth e Token](./07-oauth-token.md) — Generare, scambiare, rinnovare |
| 08 | [Workflow Pronti all'Uso](./08-workflow.md) — Esempi end-to-end |
| 09 | [Troubleshooting](./09-troubleshooting.md) — Problemi comuni e soluzioni |

---

**Prossimo step** -> [01 - Installazione e Setup](./01-setup.md)
