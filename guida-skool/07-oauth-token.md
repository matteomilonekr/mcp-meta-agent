# OAuth e Token

Il token e' la chiave che permette a Claude di accedere al tuo account Meta. Gestirlo bene significa non restare mai "chiusi fuori".

---

## Come Funziona il Token

Il token Meta ha una **durata limitata**:

| Tipo | Durata | Come ottenerlo |
|------|--------|---------------|
| Token breve | ~1 ora | Graph API Explorer |
| Token esteso | ~60 giorni | Tool `refresh_to_long_lived_token` |
| Token OAuth | ~60 giorni | Flusso OAuth completo |

---

## Verifica lo Stato del Token

```
Controlla quando scade il mio token
```

Claude usa `get_token_info` e ti dice:
- Se il token e' valido
- Quando scade
- Quali permessi ha
- A quale app e' associato

---

## Valida il Token

```
Verifica che il mio token funzioni
```

Claude usa `validate_token` per un check rapido: il token e' attivo e ha i permessi giusti?

---

## Estendi il Token a 60 Giorni

Se hai un token breve (1 ora) e vuoi estenderlo:

```
Estendi il mio token a 60 giorni
```

Claude usa `refresh_to_long_lived_token`. Richiede che `META_APP_ID` e `META_APP_SECRET` siano configurati nelle variabili d'ambiente.

> Fallo subito dopo il primo health check. Poi metti un promemoria per rinnovarlo tra 55 giorni.

---

## Flusso OAuth Completo

Se il token e' scaduto e non riesci a estenderlo, puoi ottenerne uno nuovo con il flusso OAuth:

### Passo 1: Genera l'URL di autenticazione

```
Generami un URL di autenticazione per ottenere un nuovo token
```

Claude usa `generate_auth_url` e ti da' un link. Aprilo nel browser.

### Passo 2: Autorizza l'app

Nel browser:
1. Accedi a Facebook (se non lo sei gia')
2. Autorizza l'app a gestire le tue ads
3. Verrai reindirizzato a un URL con un **codice** nei parametri

### Passo 3: Scambia il codice per il token

```
Scambia questo codice per un token: [incolla il codice qui]
```

Claude usa `exchange_code_for_token` e ottiene un nuovo token funzionante.

### Passo 4: Estendi a 60 giorni

```
Estendi il nuovo token a 60 giorni
```

---

## I 5 Tool OAuth

| Tool | Cosa fa | Quando usarlo |
|------|---------|--------------|
| `generate_auth_url` | Genera URL per login OAuth | Token scaduto, serve uno nuovo |
| `exchange_code_for_token` | Converte codice OAuth in token | Dopo aver autorizzato nel browser |
| `refresh_to_long_lived_token` | Estende il token a 60 giorni | Subito dopo ogni nuovo token |
| `get_token_info` | Mostra info, scadenza, permessi | Check periodico |
| `validate_token` | Verifica rapida se funziona | Quando qualcosa non va |

---

## Calendario Token

Per non restare mai senza accesso, segui questo calendario:

| Giorno | Azione |
|--------|--------|
| **Giorno 0** | Genera/rinnova token e estendi a 60 giorni |
| **Giorno 50** | Promemoria: il token scade tra 10 giorni |
| **Giorno 55** | Rinnova il token (`Estendi il mio token a 60 giorni`) |
| **Giorno 60** | Se non hai rinnovato: flusso OAuth completo |

> Consiglio: metti un evento ricorrente nel calendario ogni 55 giorni.

---

## Aggiornare il Token nella Configurazione

Quando ottieni un nuovo token, aggiorna il file di configurazione:

**Claude Code** (`~/.claude.json`):
```json
{
  "mcpServers": {
    "meta-ads": {
      "env": {
        "META_ACCESS_TOKEN": "IL_NUOVO_TOKEN_QUI"
      }
    }
  }
}
```

**Claude Desktop** (`~/.config/claude/claude_desktop_config.json`):
Stessa struttura, aggiorna il valore di `META_ACCESS_TOKEN`.

Poi riavvia Claude.

---

**Prossimo step** -> [08 - Workflow Pronti all'Uso](./08-workflow.md)
