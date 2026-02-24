# Analisi e Report

Questa e' probabilmente la parte che userai di piu'. Invece di navigare grafici e tabelle nel Business Manager, chiedi a Claude e hai la risposta in secondi.

---

## Panoramica Veloce

```
Come stanno andando le mie campagne attive?
```

```
Dammi un riepilogo delle performance dell'ultima settimana
```

Claude usa `get_insights` per recuperare tutti i dati in tempo reale.

---

## Metriche Specifiche

Puoi chiedere qualsiasi combinazione di metriche:

```
Mostrami CTR, CPC, CPM e conversioni
delle campagne attive negli ultimi 30 giorni
```

**Metriche disponibili:**
- **Reach**: quante persone hanno visto l'ad
- **Impressioni**: quante volte l'ad e' stata mostrata
- **Click**: quanti click ha ricevuto
- **CTR**: percentuale di click sulle impressioni
- **CPC**: costo per click
- **CPM**: costo per 1000 impressioni
- **Spesa**: quanto hai speso
- **Frequenza**: quante volte mediamente una persona ha visto l'ad
- **Conversioni**: azioni completate (lead, acquisti, ecc.)
- **ROAS**: ritorno sulla spesa pubblicitaria

---

## Periodi di Tempo

Puoi usare linguaggio naturale per i periodi:

```
Performance di oggi
```

```
Confronto tra questa settimana e la settimana scorsa
```

```
Dati degli ultimi 90 giorni
```

```
Performance del mese di gennaio
```

```
Dal 1 al 15 febbraio 2026
```

Il server supporta tutti i 20 preset di date di Meta (`last_7d`, `last_30d`, `last_90d`, ecc.) — Claude sceglie quello giusto automaticamente.

---

## Confronta piu' Campagne

```
Confronta le campagne "Brand", "Lead Gen" e "Retargeting"
sugli ultimi 30 giorni
```

Claude usa `compare_performance` e analizza tutte le campagne **in parallelo** (non una alla volta), mostrandoti una tabella comparativa side-by-side. Utile per capire dove spostare il budget.

---

## Trend Giornalieri

```
Mostrami i trend giornalieri della campagna "Lead Gen" dell'ultimo mese
```

Claude usa `get_daily_trends` e ti mostra:
- I dati giorno per giorno
- Un indicatore di direzione: **in crescita**, **stabile** o **in calo**

Perfetto per capire se una campagna sta migliorando o peggiorando.

---

## Attribuzione

```
Mostrami i dati di attribuzione della campagna "Vendite"
```

Claude usa `get_attribution_data` e ti mostra le conversioni suddivise per finestra di attribuzione:
- Click entro 1 giorno
- Click entro 7 giorni
- Visualizzazione entro 1 giorno

---

## Breakdown per Segmento

Puoi spacchettare i dati per segmento:

```
Mostrami le performance divise per eta' e genere
```

```
Performance per posizionamento (Feed, Stories, Reels)
```

```
Risultati per dispositivo (mobile vs desktop)
```

---

## Esporta in CSV o JSON

```
Esporta in CSV le performance di tutte le campagne
dell'ultimo trimestre con breakdown per eta'
```

```
Esporta in JSON i dati delle campagne attive dell'ultimo mese
```

Claude usa `export_insights` e genera il file nel formato richiesto. Puoi poi aprire il CSV in Excel o Google Sheets, o usare il JSON per integrazioni.

---

## I 5 Tool di Analytics

| Tool | Quando usarlo |
|------|--------------|
| `get_insights` | Performance generali di campagne, ad set o ads |
| `compare_performance` | Confronto side-by-side tra piu' campagne |
| `get_daily_trends` | Andamento giorno per giorno con direzione |
| `get_attribution_data` | Capire quali finestre di attribuzione convertono |
| `export_insights` | Generare file CSV/JSON per report o analisi esterne |

---

**Prossimo step** -> [05 - Gestire le Audience](./05-audience.md)
