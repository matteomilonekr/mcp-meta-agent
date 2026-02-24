# Gestire le Audience

Le audience sono i gruppi di persone a cui mostri le tue ads. Con Claude puoi crearle, analizzarle e gestirle senza toccare il Business Manager.

---

## Vedi le Tue Audience

```
Mostrami tutte le mie audience custom e lookalike
```

```
Elenca solo le audience lookalike
```

Claude usa `list_audiences` e ti mostra nome, tipo, dimensione stimata e stato di ogni audience.

---

## Crea un'Audience Custom

Un'audience custom raccoglie persone che hanno gia' interagito con te.

```
Crea un'audience custom chiamata "Visitatori Sito 30gg"
basata sui visitatori del mio sito web degli ultimi 30 giorni
```

Claude usa `create_custom_audience` per crearla sul tuo account.

**Tipi di audience custom disponibili:**

| Tipo | Descrizione | Requisito |
|------|-------------|-----------|
| **Website** | Visitatori del tuo sito | Pixel Meta installato |
| **App** | Utenti della tua app | SDK Meta integrato |
| **Video** | Persone che hanno visto i tuoi video | Almeno 1 video pubblicato |
| **Engagement** | Interazioni con pagina/Instagram | Pagina o profilo IG collegato |
| **Customer list** | Lista clienti caricata | File CSV con email/telefono |

---

## Crea una Lookalike

Una lookalike trova persone simili a un'audience che gia' hai.

```
Crea una lookalike al 2% basata sull'audience "Clienti Top" per l'Italia
```

Claude usa `create_lookalike` per creare l'audience sul tuo account.

**Guida alle percentuali:**

| Percentuale | Descrizione | Quando usarla |
|:-:|---|---|
| **1%** | Molto simile, piccola | Conversioni, lead di qualita' |
| **2-3%** | Buon equilibrio | La scelta piu' comune |
| **5%** | Mediamente simile | Piu' reach, meno precisione |
| **10-20%** | Molto ampia | Brand awareness, reach massimo |

---

## Stima la Dimensione

Prima di creare una campagna, puoi stimare quante persone raggiungerai:

```
Stima la dimensione di un'audience:
Italia, 25-45 anni, interessi marketing digitale
```

Claude usa `estimate_audience_size` e ti dice:
- Reach giornaliero stimato
- Impressioni stimate
- Spesa giornaliera stimata

Utile per capire se il targeting e' troppo stretto o troppo ampio prima di spendere.

---

## Elimina un'Audience

```
Elimina l'audience "Test Vecchia"
```

Claude usa `delete_audience` per rimuoverla dal tuo account.

---

## I 5 Tool per le Audience

| Tool | Cosa fa |
|------|---------|
| `list_audiences` | Elenca tutte le audience dell'account |
| `create_custom_audience` | Crea audience da website, app, video, engagement |
| `create_lookalike` | Crea audience simile a una esistente |
| `estimate_audience_size` | Stima reach e impressioni prima di spendere |
| `delete_audience` | Elimina un'audience |

---

## Strategia Audience a 3 Livelli

Un approccio efficace e' costruire audience su 3 livelli:

| Livello | Tipo | Esempio |
|---------|------|---------|
| **Cold** | Lookalike + interessi | Persone simili ai tuoi clienti |
| **Warm** | Custom audience | Chi ha visitato il sito o interagito |
| **Hot** | Retargeting | Chi ha aggiunto al carrello ma non comprato |

Puoi creare tutti e 3 i livelli parlando con Claude:

```
Crea 3 audience per il mio funnel:

1. Cold: lookalike 2% basata sui miei clienti, Italia
2. Warm: custom audience visitatori sito ultimi 30 giorni
3. Hot: custom audience visitatori pagina checkout ultimi 7 giorni
```

---

**Prossimo step** -> [06 - Creativita'](./06-creativita.md)
