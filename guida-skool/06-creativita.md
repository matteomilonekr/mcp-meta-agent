# Creativita': Immagini, Creativi e Anteprima

Le creative sono quello che le persone vedono: immagine, testo, titolo e CTA. Con Claude puoi gestire tutto il ciclo creativo senza uscire dalla chat.

---

## Vedi le Tue Creative

```
Mostrami tutte le creative del mio account
```

Claude usa `list_creatives` e ti mostra l'elenco con nome, ID, tipo e stato di ogni creative.

---

## Carica un'Immagine

Prima di creare una creative, devi caricare l'immagine sul tuo account Meta.

```
Carica questa immagine per le mie ads: https://esempio.com/promo.jpg
```

Claude usa `upload_image` e ti restituisce l'**image hash** — il codice che identifica l'immagine nel tuo account. Questo hash verra' usato nella creative.

**Requisiti dell'immagine:**
- URL pubblico (accessibile senza password)
- Formati supportati: JPG, PNG
- Il link deve essere raggiungibile dai server di Meta

---

## Crea una Creative

```
Crea una creative con:
- L'immagine appena caricata
- Testo: "Scopri come raddoppiare i tuoi lead in 30 giorni"
- Titolo: "Webinar Gratuito"
- Descrizione: "Posti limitati — iscriviti ora"
- CTA: Iscriviti
- Pagina Facebook: [il tuo Page ID]
- Link: https://esempio.com/webinar
```

Claude usa `create_creative` per assemblare tutti gli elementi in un oggetto creativo pronto per essere collegato a un'ad.

**Elementi della creative:**

| Elemento | Descrizione | Obbligatorio |
|----------|-------------|:-:|
| **Immagine** | Image hash dall'upload | Si' |
| **Testo** | Il corpo del messaggio (body text) | Si' |
| **Titolo** | Headline sotto l'immagine | Si' |
| **Descrizione** | Testo aggiuntivo sotto il titolo | No |
| **CTA** | Pulsante d'azione (Scopri di piu', Iscriviti, Acquista ora...) | Si' |
| **Page ID** | La pagina Facebook da cui pubblicare | Si' |
| **Link** | URL di destinazione | Si' |

---

## Anteprima dell'Ad

Dopo aver creato la creative e l'ad, puoi vedere come apparira':

```
Mostrami l'anteprima dell'ad su mobile
```

```
Mostrami l'anteprima su tutti i formati: feed, stories, reels
```

Claude usa `preview_ad` e ti mostra come l'inserzione apparira' nei diversi posizionamenti.

Utile per:
- Verificare che il testo non sia tagliato
- Controllare che l'immagine si veda bene su mobile
- Approvare la creative prima di attivare

---

## I 4 Tool per la Creativita'

| Tool | Cosa fa |
|------|---------|
| `list_creatives` | Elenca tutte le creative dell'account |
| `upload_image` | Carica un'immagine da URL sul tuo account Meta |
| `create_creative` | Assembla immagine, testo, titolo, CTA in un oggetto creativo |
| `preview_ad` | Mostra l'anteprima dell'ad nei vari formati |

---

## Workflow Creativo Completo

Ecco il flusso tipico per creare una creative da zero:

```
Passo 1: Carica l'immagine
         -> upload_image -> ottieni image hash

Passo 2: Crea la creative
         -> create_creative -> collega immagine + testo + CTA

Passo 3: Crea l'ad
         -> create_ad -> collega creative + ad set

Passo 4: Anteprima
         -> preview_ad -> verifica su mobile e desktop
```

Oppure dillo tutto in una volta:

```
Carica questa immagine: https://esempio.com/foto.jpg
Poi crea una creative con testo "Offerta valida fino a domenica",
titolo "Scopri l'Offerta", CTA "Acquista ora",
pagina [Page ID], link https://esempio.com/offerta.
Collegala all'ad set "Retargeting Italia".
Mostrami l'anteprima su mobile.
```

Claude esegue tutti i passaggi in sequenza.

---

**Prossimo step** -> [07 - OAuth e Token](./07-oauth-token.md)
