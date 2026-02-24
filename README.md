# Meta Ads MCP Server

Gestisci **tutte le tue campagne Meta/Facebook Ads** direttamente da Claude, senza aprire Business Manager.

Un MCP server che espone **36 tools** per creare, analizzare e ottimizzare campagne pubblicitarie su Facebook e Instagram tramite il Model Context Protocol.

> Built for [Scalers+](https://www.skool.com/scalers) community.
> Python rewrite of [brijr/meta-mcp](https://github.com/brijr/meta-mcp) with 15+ bug fixes, async support, and typed models.

---

## Cosa puoi fare

| Categoria | Tools | Operazioni |
|-----------|:-----:|------------|
| **Campagne** | 6 | Listare, creare, aggiornare, mettere in pausa, riattivare, eliminare |
| **Ad Sets** | 5 | Listare, creare con targeting e budget, aggiornare, pausare, eliminare |
| **Ads** | 4 | Listare, creare (linking creative + ad set), aggiornare, eliminare |
| **Analytics** | 5 | Insights con date range, confronto parallelo multi-campagna, export CSV/JSON, trend giornalieri, attribution windows |
| **Audiences** | 5 | Custom audience, lookalike, stima dimensione, listare, eliminare |
| **Creatives** | 4 | Listare, creare con immagine/video + CTA, upload immagini, preview |
| **OAuth** | 5 | Auth URL, code exchange, long-lived token (60gg), info token, validazione |
| **Account** | 2 | Lista ad account accessibili, health check server + API |

**36 tools totali** — copertura completa del workflow Meta Ads.

---

## Quick Start

### 1. Installa

```bash
pip install -e .
```

### 2. Configura

```bash
export META_ACCESS_TOKEN="your_token_here"

# Opzionale (per OAuth flows)
export META_APP_ID="your_app_id"
export META_APP_SECRET="your_app_secret"
```

### 3. Avvia

**STDIO** (per Claude Code / Claude Desktop):
```bash
python -m meta_ads_mcp.server
```

**HTTP** (per mcp-use, web clients, Inspector UI):
```bash
python -c "from meta_ads_mcp.server import mcp; mcp.run(transport='streamable-http', port=8000)"
```

Con debug mode (abilita Inspector UI su `/inspector`, docs su `/docs`):
```bash
python -c "from meta_ads_mcp.server import mcp; mcp.run(transport='streamable-http', port=8000, debug=True)"
```

### 4. Connetti a Claude

**Claude Code** — aggiungi a `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "meta-ads": {
      "command": "python",
      "args": ["-m", "meta_ads_mcp.server"],
      "cwd": "/path/to/meta-ads-mcp",
      "env": {
        "META_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

**Claude Desktop** — stesso formato in `~/.config/claude/claude_desktop_config.json`.

### 5. Usa con mcp-use (programmatico)

```python
from mcp_use import MCPClient
from mcp_use.client.config import MCPServerConfig

config = MCPServerConfig(
    url="http://localhost:8000/mcp",
    transport="streamable-http",
)
client = MCPClient(config={"mcpServers": {"meta-ads": config}})

async with client.session("meta-ads") as session:
    tools = await session.list_tools()
    result = await session.call_tool("health_check", {})
    print(result)
```

---

## Come ottenere il Token Meta

**Opzione A — Manuale:**
1. Vai su [Meta for Developers](https://developers.facebook.com/)
2. Crea un'app (tipo Business)
3. Aggiungi il prodotto **Marketing API**
4. Genera un User Access Token con permessi `ads_management` e `ads_read`
5. Usa il tool `refresh_to_long_lived_token` per estenderlo a 60 giorni

**Opzione B — OAuth integrato:**
```
generate_auth_url → apri nel browser → exchange_code_for_token → refresh_to_long_lived_token
```

---

## Tools Reference

### Campaigns (6 tools)

| Tool | Descrizione |
|------|-------------|
| `list_campaigns` | Lista campagne con filtri per stato e obiettivo. Output markdown o JSON. |
| `create_campaign` | Crea campagna (PAUSED di default). Supporta tutti gli obiettivi Meta (CONVERSIONS, TRAFFIC, LEADS, etc.) e bid strategy (LOWEST_COST, COST_CAP, BID_CAP). |
| `update_campaign` | Aggiorna nome, stato, budget, schedule, bid strategy. |
| `pause_campaign` | Metti in pausa una campagna attiva. |
| `resume_campaign` | Riattiva una campagna in pausa. |
| `delete_campaign` | Elimina una campagna. |

### Ad Sets (5 tools)

| Tool | Descrizione |
|------|-------------|
| `list_ad_sets` | Lista ad set per account o campagna. Mostra budget, targeting, ottimizzazione. |
| `create_ad_set` | Crea ad set con targeting, budget, optimization goal, billing event. Rileva automaticamente CBO (Campaign Budget Optimization) e gestisce il budget di conseguenza. |
| `update_ad_set` | Aggiorna targeting, budget, schedule, promoted object. Valida JSON prima dell'invio. |
| `pause_ad_set` | Metti in pausa un ad set. |
| `delete_ad_set` | Elimina un ad set. |

### Ads (4 tools)

| Tool | Descrizione |
|------|-------------|
| `list_ads` | Lista ads per account, campagna o ad set. Include status, preview URL, metriche. |
| `create_ad` | Crea ad collegando una creative a un ad set. |
| `update_ad` | Aggiorna stato, nome o creative di un ad. |
| `delete_ad` | Elimina un ad. |

### Analytics (5 tools)

| Tool | Descrizione |
|------|-------------|
| `get_insights` | Metriche di performance con date range personalizzate o preset (last_7d, last_30d, etc.). Breakdowns per age, gender, country, placement. Tutti i 20 Meta date preset supportati. |
| `compare_performance` | Confronto side-by-side di multiple campagne/ad set/ads. Esecuzione **parallela** via `asyncio.gather()` per massima velocita. |
| `export_insights` | Esporta dati in formato **CSV** o **JSON**. Pronto per analisi esterne. |
| `get_daily_trends` | Breakdown giornaliero con indicatore di trend (up/down/stable) per spend, impressions, clicks, conversions. |
| `get_attribution_data` | Analisi per attribution window (1d_click, 7d_click, 28d_click, 1d_view). |

### Audiences (5 tools)

| Tool | Descrizione |
|------|-------------|
| `list_audiences` | Lista custom e lookalike audience con dimensione stimata (lower/upper bound). |
| `create_custom_audience` | Crea audience personalizzata (website, app, customer file, video viewers, etc.). |
| `create_lookalike` | Crea lookalike da audience sorgente con country e ratio personalizzabili. |
| `estimate_audience_size` | Stima reach per una targeting spec senza creare nulla. |
| `delete_audience` | Elimina un'audience. API call reale (non stub come nell'originale). |

### Creatives (4 tools)

| Tool | Descrizione |
|------|-------------|
| `list_creatives` | Lista creative dell'account (default 25 per evitare limiti API). |
| `create_creative` | Crea creative con object_story_spec (immagine/video + CTA + link). |
| `upload_image` | Upload immagine da URL, restituisce hash per uso nelle creative. |
| `preview_ad` | Preview di una creative in vari formati (desktop feed, mobile feed, stories, etc.). |

### OAuth (5 tools)

| Tool | Descrizione |
|------|-------------|
| `generate_auth_url` | Genera URL di autorizzazione Facebook OAuth. |
| `exchange_code_for_token` | Scambia authorization code per access token. |
| `refresh_to_long_lived_token` | Converte token short-lived in long-lived (60 giorni). |
| `get_token_info` | Info dettagliate: validita, scopi, scadenza, app ID. |
| `validate_token` | Validazione rapida — controlla se il token funziona. |

### Account (2 tools)

| Tool | Descrizione |
|------|-------------|
| `list_ad_accounts` | Lista tutti gli ad account accessibili con stato, currency, timezone. |
| `health_check` | Check salute server + connettivita API Meta. |

---

## Architettura

```
meta_ads_mcp/
├── server.py          # mcp-use server con lifespan management
├── client.py          # Client HTTP async (httpx) con retry + rate limiting
├── auth.py            # Gestione token, OAuth flows
├── models/
│   └── common.py      # Enum, costanti, field defaults, date presets
├── tools/             # 36 MCP tools organizzati in 8 moduli
│   ├── campaigns.py   # 6 tools
│   ├── ad_sets.py     # 5 tools
│   ├── ads.py         # 4 tools
│   ├── analytics.py   # 5 tools
│   ├── audiences.py   # 5 tools
│   ├── creatives.py   # 4 tools
│   ├── oauth.py       # 5 tools
│   ├── account.py     # 2 tools
│   └── _helpers.py    # Utility condivise (get_client, safe_get, normalize_account_id)
└── utils/
    ├── errors.py      # Gerarchia errori tipizzata (MetaApiError, AuthError, RateLimitError)
    ├── rate_limiter.py # Sistema scoring per-account con backoff automatico
    ├── pagination.py   # Paginazione cursor + URL fallback
    └── formatting.py   # Tabelle markdown, formattazione currency/numeri/percentuali
```

---

## Tech Stack

| Componente | Tecnologia |
|------------|------------|
| Runtime | Python 3.12+ |
| MCP Framework | [mcp-use](https://manufact.com/docs/python/server/compatibility) (FastMCP compatibile) |
| HTTP Client | httpx (async) |
| Validation | Pydantic v2 |
| Meta API | Graph API v23.0 |
| Testing | pytest + pytest-asyncio + respx |
| Transport | STDIO, Streamable HTTP, SSE |

---

## Miglioramenti rispetto all'originale

Rewrite completo da TypeScript a Python con 15+ fix critici:

| Problema | Originale (TypeScript) | Questa versione |
|----------|----------------------|-----------------|
| Tool stub | `delete_audience`, `update_audience` non fanno nulla | Tutti i tools fanno API call reali |
| compare_performance | Sequenziale O(n) | Parallelo via `asyncio.gather()` |
| Rate limit | Classificato erroneamente come auth error | Priorita codice (4, 17 prima di OAuthException) |
| Paginazione | Si blocca quando manca il cursor nell'URL | Supporta cursor + URL fallback |
| Date presets | Mancano `last_7d`, `last_30d`, `last_90d` | Tutti i 20 preset Meta inclusi |
| Types | `any` ovunque | Pydantic models + enum tipizzati |
| JWT secret | Hardcoded di default | Non necessario (solo STDIO) |
| Logging | `console.log` inquina STDIO | Python logging su stderr |
| API version | Inconsistente v22/v23 | Singola costante `META_API_VERSION` |
| CBO handling | Nessun controllo | Rileva CBO e salta budget ad-set level |
| Audience size | Campo deprecato `approximate_count` | Usa `lower_bound` / `upper_bound` |
| JSON validation | Nessuna | Valida targeting/promoted_object prima dell'invio |

---

## Sviluppo

```bash
# Installa con dipendenze dev
pip install -e ".[dev]"

# Esegui test (134 test, 94% coverage)
pytest -v

# Test con coverage
pytest --cov=meta_ads_mcp --cov-report=term-missing

# Test completo di tutti i tools (richiede META_ACCESS_TOKEN reale)
python test_all_tools.py
```

### Debug e Inspector

Con mcp-use in debug mode ottieni:

| Endpoint | Descrizione |
|----------|-------------|
| `/inspector` | UI interattiva per testare i tools |
| `/docs` | Documentazione auto-generata |
| `/openmcp.json` | Metadata OpenMCP |

```bash
python -c "from meta_ads_mcp.server import mcp; mcp.run(transport='streamable-http', debug=True)"
# Apri http://localhost:8000/inspector
```

---

## Licenza

Copyright (c) 2026 Matteo Milone. Tutti i diritti riservati.

Questo software e il relativo codice sorgente sono di proprieta esclusiva di Matteo Milone.
Non e consentito copiare, modificare, distribuire, sublicenziare o utilizzare questo software,
in tutto o in parte, senza autorizzazione scritta esplicita da parte dell'autore.

Per richieste di licenza: contattare Matteo Milone.
