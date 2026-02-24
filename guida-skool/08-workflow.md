# Workflow Pronti all'Uso

Ecco dei workflow completi che puoi copiare e incollare direttamente in Claude. Sono pensati per le situazioni piu' comuni.

---

## Audit Settimanale (5 minuti -> 30 secondi)

Fallo ogni lunedi' mattina per avere il polso della situazione.

**Passo 1** — Panoramica
```
Mostrami tutte le campagne attive con le performance degli ultimi 7 giorni.
Ordina per spesa decrescente.
```

**Passo 2** — Trova i problemi
```
Quali campagne hanno un CPC superiore alla media?
Quali hanno un CTR sotto l'1%?
```

**Passo 3** — Confronta le migliori
```
Confronta le 3 campagne con piu' conversioni
```

**Passo 4** — Esporta
```
Esporta il report completo in CSV
```

---

## Lancio Nuova Campagna (da zero a pronta in 2 minuti)

**Passo 1** — Stima l'audience
```
Stima quante persone posso raggiungere in Italia,
donne 25-45, interessate a [il tuo settore]
```

**Passo 2** — Crea tutto in un colpo
```
Crea una campagna completa:
- Nome: "[Nome Campagna]"
- Obiettivo: lead generation
- Budget: [X] euro al giorno
- Targeting: [il targeting che hai stimato]
- Immagine: [URL immagine]
- Testo: "[il tuo copy]"
- CTA: [Scopri di piu' / Iscriviti / Acquista ora]
```

**Passo 3** — Verifica
```
Mostrami l'anteprima dell'ad su mobile
```

**Passo 4** — Attiva
```
Attiva la campagna "[Nome Campagna]"
```

---

## Ottimizzazione Giornaliera

Da fare ogni giorno quando hai campagne attive importanti.

```
Mostrami i trend giornalieri delle campagne attive degli ultimi 5 giorni.
Evidenzia quelle con CPC in aumento o CTR in calo.
```

Se trovi problemi:

```
Metti in pausa l'ad set "[nome]" che sta performando male
```

```
Modifica il budget della campagna "[nome]" a [nuovo importo] euro al giorno
```

---

## Report Mensile per il Cliente

Un singolo prompt per generare tutto:

```
Dammi un report completo dell'account per il mese scorso:
- Spesa totale
- Impressioni e reach totali
- CTR e CPC medi
- Conversioni totali e costo per conversione
- Le 3 campagne migliori e le 3 peggiori
- Trend settimanale del mese
- Esporta tutto in CSV
```

**Da 1-2 ore a 30 secondi.**

---

## Confronto A/B tra Campagne

```
Confronta le campagne "[Versione A]" e "[Versione B]"
sugli ultimi 14 giorni.
Dimmi quale ha il costo per lead piu' basso
e quale ha il CTR migliore.
```

---

## Costruzione Funnel Audience

Crea un'architettura audience completa in un colpo:

```
Per il mio account, crea queste 3 audience:

1. COLD - Lookalike 2% basata su "Clienti Ultimo Anno", Italia
2. WARM - Custom audience visitatori sito ultimi 30 giorni
3. HOT - Custom audience visitatori pagina checkout ultimi 7 giorni

Poi stima la dimensione di ciascuna.
```

---

## Pulizia Account

Ogni tanto fai pulizia delle campagne vecchie:

```
Mostrami tutte le campagne in pausa da piu' di 30 giorni
```

```
Elimina le campagne "[lista nomi]"
```

```
Mostrami le audience che non sono collegate a nessun ad set
```

---

## Setup Completo da Zero per un Nuovo Cliente

Workflow end-to-end per quando prendi in gestione un nuovo account:

**Passo 1** — Panoramica account
```
Fammi un health check.
Poi mostrami tutti gli account pubblicitari disponibili.
```

**Passo 2** — Analisi storico
```
Mostrami tutte le campagne dell'ultimo trimestre con performance complete.
Quali hanno funzionato meglio? Quali sono state uno spreco?
```

**Passo 3** — Audit audience
```
Mostrami tutte le audience esistenti.
Quali sono ancora valide? Quali sono troppo vecchie?
```

**Passo 4** — Crea nuove audience
```
Crea una lookalike 2% basata sull'audience con piu' conversioni, per l'Italia.
Stima la dimensione.
```

**Passo 5** — Lancia la prima campagna
```
Crea una campagna completa:
- Nome: "[Cliente] - Test Iniziale"
- Obiettivo: [in base all'analisi]
- Budget: [X] euro al giorno
- Usa la lookalike appena creata
- [Immagine e copy]
```

**Passo 6** — Esporta tutto
```
Esporta in CSV il report storico e le audience attuali.
Mi servono per la presentazione al cliente.
```

---

## Gestione Token

Ogni 50-55 giorni:

```
Controlla quando scade il mio token
```

```
Rinnova il mio token per altri 60 giorni
```

> Metti un promemoria ricorrente nel calendario.

---

**Prossimo step** -> [09 - Problemi Comuni e Soluzioni](./09-troubleshooting.md)
