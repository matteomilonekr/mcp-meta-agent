# Primi Comandi: Inizia Subito

Hai configurato tutto. Ora vediamo cosa puoi chiedere a Claude fin da subito.

Non devi memorizzare nomi tecnici: **scrivi quello che vuoi in italiano** e Claude sa quale strumento usare.

---

## Scopri i Tuoi Account

La prima cosa da fare e' scoprire quali account pubblicitari hai collegati:

```
Mostrami tutti i miei account pubblicitari
```

Claude usera' il tool `list_ad_accounts` e ti mostrera' una lista con:
- Nome dell'account
- ID (lo userai per le prossime richieste)
- Stato (attivo, disabilitato, ecc.)
- Valuta e fuso orario

> Salva l'ID del tuo account principale (ha il formato `act_123456789`). Ti servira' spesso.

---

## Guarda le Tue Campagne

```
Elenca tutte le campagne attive
```

Oppure per vedere anche quelle in pausa:

```
Mostrami tutte le campagne, sia attive che in pausa
```

Claude usa `list_campaigns` e ti restituisce nome, ID, stato, obiettivo e budget di ogni campagna.

---

## Controlla Come Stanno Andando

```
Come stanno andando le mie campagne negli ultimi 7 giorni?
```

```
Mostrami CTR, CPC e spesa totale delle campagne attive dell'ultimo mese
```

```
Quali sono le 3 campagne con il CTR piu' alto?
```

Claude usa `get_insights` e ti risponde con una tabella chiara:

| Campagna | Spesa | Risultati | Costo/Risultato | Trend |
|----------|-------|-----------|-----------------|-------|
| Lead Gen Webinar | 210 EUR | 42 lead | 5.00 EUR | +12% |
| Retargeting Shop | 150 EUR | 18 acquisti | 8.33 EUR | -5% |
| Brand Awareness | 300 EUR | 45K reach | 6.67 CPM | stabile |

---

## Confronta le Performance

```
Confronta le campagne "Brand Awareness" e "Lead Gen Gennaio"
sugli ultimi 30 giorni
```

Claude usa `compare_performance` e analizza in **parallelo** (non una alla volta), mostrandoti una tabella comparativa con tutte le metriche.

---

## Vedi i Trend

```
Mostrami i trend giornalieri della campagna principale dell'ultima settimana
```

Claude usa `get_daily_trends` e ti dira' se la spesa, il CTR e il CPC sono in crescita, stabili o in calo.

---

## Esporta i Dati

```
Esporta in CSV le performance di tutte le campagne dell'ultimo trimestre
```

Claude usa `export_insights` e genera un file CSV pronto per Excel, Google Sheets o per il cliente.

---

## Comandi Rapidi di Emergenza

Se qualcosa non va e devi agire in fretta:

```
Metti in pausa la campagna [nome o ID]
```

```
Metti in pausa tutte le campagne attive
```

```
Riattiva la campagna [nome o ID]
```

Claude usa `pause_campaign` e `resume_campaign` — azione immediata.

---

## Come Claude Sceglie il Tool Giusto

Non devi mai dire "usa il tool get_insights". Scrivi in linguaggio naturale e Claude mappa automaticamente:

| Tu scrivi | Claude usa |
|-----------|-----------|
| "Mostrami le campagne" | `list_campaigns` |
| "Come stanno andando?" | `get_insights` |
| "Confronta queste due" | `compare_performance` |
| "Trend della settimana" | `get_daily_trends` |
| "Esporta in CSV" | `export_insights` |
| "Metti in pausa" | `pause_campaign` |
| "Verifica il token" | `validate_token` |

---

**Prossimo step** -> [03 - Creare una Campagna](./03-creare-campagna.md)
