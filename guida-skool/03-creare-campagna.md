# Creare una Campagna Completa

Puoi creare un'intera campagna Meta Ads parlando con Claude. Una campagna completa ha 4 livelli:

```
Campagna  ->  Ad Set  ->  Creative  ->  Ad
```

Non devi ricordare questa struttura: Claude ti guidera' passo passo.

---

## Il Modo Semplice: Dillo e Basta

Il modo piu' veloce e' descrivere quello che vuoi in linguaggio naturale:

```
Crea una campagna di lead generation per il mio account:
- Nome: "Promo Febbraio 2026"
- Budget giornaliero: 30 euro
- Targeting: Italia, donne 25-45 anni
- Usa questa immagine: https://esempio.com/promo.jpg
- Testo: "Scopri la nostra offerta esclusiva"
- CTA: Scopri di piu'
```

Claude creera' tutto: campagna, ad set, creative e ad. Tutto in pausa, pronto per essere attivato quando vuoi.

**Zero click nell'Ads Manager.**

---

## Il Modo Passo-Passo

Se preferisci avere piu' controllo, puoi procedere un pezzo alla volta.

### 1. Crea la Campagna

```
Crea una campagna chiamata "Test Febbraio"
con obiettivo lead generation e budget 50 euro al giorno
```

Claude usa `create_campaign`. La campagna nasce sempre in stato PAUSED.

**Obiettivi disponibili** (dilli in italiano, Claude capisce):
- Notorieta' del brand
- Interazione / Engagement
- Generazione lead
- Vendite
- Traffico al sito
- Installazioni app

### 2. Crea l'Ad Set

```
Aggiungi un ad set alla campagna "Test Febbraio":
- Nome: "Donne Italia 25-45"
- Targeting: Italia, donne, 25-45 anni, interessi: fitness
- Ottimizzazione: lead
```

Claude usa `create_ad_set` con targeting spec, budget e ottimizzazione.

### 3. Carica un'Immagine

```
Carica questa immagine per le mie ads: https://esempio.com/foto.jpg
```

Claude usa `upload_image` e ti restituisce l'hash da usare nella creative.

### 4. Crea la Creative

```
Crea una creative con:
- L'immagine appena caricata
- Testo: "Prova gratuita per 7 giorni"
- Titolo: "Inizia Ora"
- CTA: Iscriviti
- Pagina Facebook: [il tuo Page ID]
```

Claude usa `create_creative` per assemblare il pezzo creativo.

### 5. Crea l'Ad

```
Crea un'ad che collega la creative appena creata all'ad set "Donne Italia 25-45"
```

Claude usa `create_ad` per collegare creative e ad set.

### 6. Anteprima

```
Mostrami l'anteprima dell'ad su mobile e desktop
```

Claude usa `preview_ad` e ti mostra come apparira' l'inserzione nei diversi posizionamenti.

### 7. Attiva (quando sei pronto)

```
Attiva la campagna "Test Febbraio"
```

Claude usa `resume_campaign` per passare dallo stato PAUSED ad ACTIVE.

---

## Gestione Budget

Puoi usare il budget sia a livello di campagna (CBO) che di ad set:

**Budget a livello di campagna (CBO):**
```
Crea una campagna con budget giornaliero di 100 euro
distribuito automaticamente tra gli ad set
```

**Budget a livello di ad set:**
```
Crea un ad set con budget giornaliero di 30 euro
```

> Non devi preoccuparti dei centesimi: quando dici "50 euro", Claude converte automaticamente in centesimi (5000) come richiesto dall'API.
> Se la campagna usa CBO, Claude lo rileva e non ti chiede il budget sull'ad set.

---

## I Tool Coinvolti nel Workflow

Ecco la sequenza completa dei tool che Claude usa dietro le quinte:

```
1. create_campaign      ->  Crea la campagna (PAUSED)
2. create_ad_set        ->  Crea l'ad set con targeting
3. upload_image         ->  Carica l'immagine
4. create_creative      ->  Assembla la creative
5. create_ad            ->  Collega creative + ad set
6. preview_ad           ->  Mostra l'anteprima
7. resume_campaign      ->  Attiva (solo quando lo dici tu)
```

---

## Cose da Sapere

- Le campagne vengono **sempre create in pausa** — nessun rischio di spesa accidentale
- Claude ti chiede conferma prima di attivare qualsiasi cosa
- Puoi modificare qualsiasi elemento dopo la creazione con `update_campaign`, `update_ad_set` e `update_ad`
- Puoi eliminare elementi sbagliati con `delete_campaign`, `delete_ad_set` e `delete_ad`

---

**Prossimo step** -> [04 - Analisi e Report](./04-analisi-report.md)
