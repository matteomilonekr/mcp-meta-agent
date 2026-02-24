# Installazione e Setup

Segui questi passaggi per collegare Claude al tuo account Meta Ads.

Tempo stimato: ~10 minuti.

---

## Passo 1: Crea il Token Meta

Il token e' la "chiave" che permette a Claude di accedere al tuo account pubblicitario.

1. Vai su [developers.facebook.com](https://developers.facebook.com/)
2. Clicca **"Le mie app"** in alto a destra, poi **"Crea app"**
3. Scegli il tipo **Business**
4. Dai un nome alla tua app (es. "Claude Ads Manager") e clicca **Crea**
5. Nella dashboard dell'app, cerca **Marketing API** e clicca **Configura**
6. Vai su **Strumenti > Graph API Explorer** (dal menu a sinistra)
7. In alto, seleziona la tua app dal menu a tendina
8. Clicca **"Genera token di accesso"**
9. Quando ti chiede i permessi, seleziona:
   - `ads_management`
   - `ads_read`
10. Clicca **Genera** e **copia il token** (e' una stringa lunga)

> Questo token dura solo 1 ora. Non preoccuparti: dopo il setup lo estenderemo a 60 giorni.

---

## Passo 2: Installa il Server MCP

Hai 3 modi per installare. Scegli quello che preferisci.

### Opzione A — Da GitHub (consigliata)

```bash
pip install git+https://github.com/matteomilonekr/meta-ads-manager.git
```

### Opzione B — Clone locale

```bash
git clone https://github.com/matteomilonekr/meta-ads-manager.git
cd meta-ads-manager
pip install -e .
```

### Opzione C — Via uvx (senza installazione permanente)

```bash
uvx --from git+https://github.com/matteomilonekr/meta-ads-manager.git meta-ads-manager
```

**Requisiti**: Python 3.12 o superiore. Se non lo hai, scaricalo da [python.org](https://www.python.org/downloads/).

---

## Passo 3: Configura Claude

Il server funziona sia con **Claude Desktop** che con **Claude Code**.

### Opzione A — Claude Code

Apri il file:
```
~/.claude.json
```

Aggiungi la configurazione MCP:

```json
{
  "mcpServers": {
    "meta-ads": {
      "command": "python",
      "args": ["-m", "meta_ads_mcp.server"],
      "env": {
        "META_ACCESS_TOKEN": "INCOLLA_QUI_IL_TUO_TOKEN",
        "META_APP_ID": "INCOLLA_QUI_IL_TUO_APP_ID",
        "META_APP_SECRET": "INCOLLA_QUI_IL_TUO_APP_SECRET"
      }
    }
  }
}
```

Se hai installato via uvx, usa questa configurazione invece:

```json
{
  "mcpServers": {
    "meta-ads": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/matteomilonekr/meta-ads-manager.git", "meta-ads-manager"],
      "env": {
        "META_ACCESS_TOKEN": "INCOLLA_QUI_IL_TUO_TOKEN",
        "META_APP_ID": "INCOLLA_QUI_IL_TUO_APP_ID",
        "META_APP_SECRET": "INCOLLA_QUI_IL_TUO_APP_SECRET"
      }
    }
  }
}
```

### Opzione B — Claude Desktop

Apri il file di configurazione:

**Mac:**
```
~/.config/claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

Aggiungi la stessa configurazione JSON mostrata sopra.

---

### Variabili d'ambiente

| Variabile | Obbligatoria | Dove trovarla |
|-----------|:-:|---------------|
| `META_ACCESS_TOKEN` | Si' | Graph API Explorer (Passo 1) |
| `META_APP_ID` | Opzionale* | developers.facebook.com > La tua app > Impostazioni > Generale |
| `META_APP_SECRET` | Opzionale* | developers.facebook.com > La tua app > Impostazioni > Generale |


> *APP_ID e APP_SECRET sono opzionali per l'uso base, ma **servono per il flusso OAuth** e per estendere il token a 60 giorni.

---

## Passo 4: Verifica che Funzioni

Riavvia Claude, poi scrivi:

```
Fammi un health check
```

Se tutto e' configurato correttamente, Claude ti rispondera' con:
- Il tuo nome utente Meta
- Il numero di account pubblicitari collegati
- Lo stato della connessione alle API

> Se usi Claude Code, puoi verificare che il server sia visibile con il comando `/mcp` nella CLI.

---

## Passo 5: Estendi il Token a 60 Giorni

Subito dopo il primo health check, scrivi:

```
Estendi il mio token a 60 giorni
```

Claude usera' il tool `refresh_to_long_lived_token` e il tuo token durera' 2 mesi invece di 1 ora.

> Metti un promemoria nel calendario per rinnovarlo tra 55 giorni.

---

## Come funziona sotto il cofano

```
+--------------+     MCP      +-------------------+     HTTPS     +-----------+
|    Claude    | <----------> | Meta Ads Server   | <-----------> |  Meta API |
| (tu parli)  |   (STDIO)    |  (36 tools)       |  (Graph v23)  | (i tuoi   |
|              |              |                   |               |  account) |
+--------------+              +-------------------+               +-----------+
```

Claude non "simula" le risposte. Esegue chiamate reali alle API di Meta sul tuo account.

---

## Repository GitHub

Il codice sorgente e' su GitHub:

**https://github.com/matteomilonekr/meta-ads-manager**

- 134 test di integrazione
- 94% code coverage
- Licenza open source

Se trovi bug o vuoi contribuire, apri una issue o una pull request.

---

**Prossimo step** -> [02 - Primi Comandi](./02-primi-comandi.md)
