# Problemi Comuni e Soluzioni

Se qualcosa non funziona, cerca il tuo problema qui sotto.

---

## "Token expired" o "Token scaduto"

**Cosa significa**: La chiave di accesso al tuo account Meta e' scaduta.

**Come risolverlo**:
1. Se hai configurato APP_ID e APP_SECRET, scrivi a Claude:
   ```
   Rinnova il mio token per 60 giorni
   ```
2. Se non funziona, genera un nuovo token da [Graph API Explorer](https://developers.facebook.com/tools/explorer/) e aggiorna il file di configurazione.
3. Puoi anche usare il flusso OAuth completo:
   ```
   Generami un URL di autenticazione per ottenere un nuovo token
   ```

> Vedi il capitolo [07 - OAuth e Token](./07-oauth-token.md) per la procedura completa.

---

## "Permission denied" o "Permessi insufficienti"

**Cosa significa**: Il token non ha i permessi necessari.

**Come risolverlo**: Rigenera il token assicurandoti di selezionare sia `ads_management` che `ads_read` nei permessi.

---

## "Account not found" o "Account non trovato"

**Cosa significa**: L'ID account che stai usando non e' corretto.

**Come risolverlo**:
```
Mostrami tutti i miei account pubblicitari
```
Cerca l'ID corretto nella lista. Ha il formato `act_` seguito da numeri (es. `act_123456789`).

---

## Claude non risponde ai comandi Meta Ads

**Cosa significa**: Il server MCP non e' avviato o non e' configurato correttamente.

**Come risolverlo**:
1. Verifica che il file di configurazione sia scritto correttamente (attenzione alle virgolette e alle virgole nel JSON)
2. Riavvia Claude Desktop / Claude Code
3. Scrivi `Fammi un health check` per verificare la connessione

**Per Claude Code**: verifica che il server sia visibile con il comando `/mcp` nella CLI.

**File di configurazione da controllare:**

| Client | File |
|--------|------|
| Claude Code | `~/.claude.json` |
| Claude Desktop (Mac) | `~/.config/claude/claude_desktop_config.json` |
| Claude Desktop (Windows) | `%APPDATA%\Claude\claude_desktop_config.json` |

---

## "Rate limit" o "Troppe richieste"

**Cosa significa**: Hai fatto troppe richieste alle API Meta in poco tempo.

**Come risolverlo**: Aspetta qualche minuto e riprova. Il server ha un sistema di rate limiting intelligente per-account che gestisce automaticamente i limiti, ma in casi estremi puo' capitare.

---

## L'immagine non si carica

**Cosa significa**: L'URL dell'immagine non e' accessibile o il formato non e' supportato.

**Come risolverlo**:
- Assicurati che l'URL sia pubblico (non protetto da password)
- Usa formati standard: JPG, PNG
- Verifica che il link funzioni aprendolo nel browser
- L'immagine deve essere raggiungibile dai server di Meta

---

## Non trovo l'App ID o l'App Secret

1. Vai su [developers.facebook.com](https://developers.facebook.com/)
2. Clicca su **"Le mie app"** in alto
3. Seleziona la tua app
4. Vai su **Impostazioni > Generale**
5. Troverai sia l'**ID app** che la **Chiave segreta** dell'app

---

## Le metriche non tornano

Se i numeri che vedi in Claude non corrispondono al Business Manager:

- Verifica di usare lo **stesso periodo di tempo**
- Controlla la **finestra di attribuzione** (1 giorno click vs 7 giorni click)
- Il Business Manager a volte mostra dati con ritardo — Claude usa le API in tempo reale

```
Mostrami i dati di attribuzione della campagna "[nome]"
per confrontare le diverse finestre
```

---

## La campagna non si attiva

Possibili cause:
- **Budget mancante**: se la campagna usa CBO, verifica che il budget sia impostato a livello campagna
- **Creative mancante**: l'ad deve avere una creative collegata
- **Audience troppo piccola**: Meta potrebbe non riuscire a consegnare
- **Pagina non collegata**: la creative deve essere associata a una pagina Facebook

```
Mostrami i dettagli della campagna "[nome]" per capire cosa manca
```

---

## Errori di creazione ad set

Se `create_ad_set` fallisce:
- Verifica che il **campaign ID** sia corretto
- Se la campagna usa CBO, **non impostare** il budget sull'ad set
- Controlla che il targeting sia valido (paese, eta', interessi esistenti)
- L'ottimizzazione deve essere coerente con l'obiettivo della campagna

---

## Errori comuni nel JSON di configurazione

I problemi piu' frequenti nel file di configurazione:

```json
// SBAGLIATO - virgola in piu' dopo l'ultimo elemento
{
  "mcpServers": {
    "meta-ads": {
      "env": {
        "META_ACCESS_TOKEN": "token",  // <-- virgola di troppo
      }
    }
  }
}

// CORRETTO
{
  "mcpServers": {
    "meta-ads": {
      "env": {
        "META_ACCESS_TOKEN": "token"
      }
    }
  }
}
```

---

## Ho ancora problemi

Se nessuna di queste soluzioni funziona:

1. Scrivi a Claude: `Fammi un health check completo`
2. Fai uno screenshot del risultato
3. Condividilo nella community Skool e ti aiuteremo
4. Puoi anche aprire una issue su GitHub: https://github.com/matteomilonekr/meta-ads-manager

---

**Torna all'indice** -> [00 - Introduzione](./00-introduzione.md)
