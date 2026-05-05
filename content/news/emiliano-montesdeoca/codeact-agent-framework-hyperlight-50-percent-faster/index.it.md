---
title: "CodeAct in Agent Framework: Come Dimezzare la Latenza del tuo Agente"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct comprime catene di strumenti in più fasi in un unico blocco di codice sandboxed — riducendo la latenza del 52% e l'utilizzo dei token del 64%. Cosa significa per i tuoi agenti e quando usarlo."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "index.md" >}}).*

C'è quel momento in ogni progetto di agenti in cui guardi il trace e pensi: "perché ci vuole così tanto?" Il modello funziona bene. Gli strumenti funzionano. Ma ci sono sette round trip per ottenere un risultato che potresti calcolare in una sola volta.

Questo è esattamente il problema che CodeAct risolve — e il [team di Agent Framework ha appena pubblicato il supporto alpha](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) tramite il nuovo pacchetto `agent-framework-hyperlight`.

## Cos'è CodeAct?

Il [pattern CodeAct](https://arxiv.org/abs/2402.01030) è elegantemente semplice: invece di dare al modello una lista di strumenti da chiamare uno alla volta, gli dai un unico strumento `execute_code` e lo lasci esprimere l'*intero piano* come un breve programma Python. L'agente scrive il codice una volta, la sandbox lo esegue, e ottieni un singolo risultato consolidato.

| Approccio | Tempo | Token |
|--------|------|--------|
| Tradizionale | 27,81s | 6.890 |
| CodeAct | 13,23s | 2.489 |
| **Miglioramento** | **52,4%** | **63,9%** |

## La componente di sicurezza: Micro-VM Hyperlight

Il pacchetto `agent-framework-hyperlight` utilizza micro-VM di [Hyperlight](https://github.com/hyperlight-dev/hyperlight). Ogni chiamata `execute_code` ottiene la propria micro-VM appena creata. L'avvio si misura in millisecondi. L'isolamento è praticamente gratuito.

I tuoi strumenti continuano a girare sull'host. Il *codice collante* generato dal modello gira nella sandbox. Questa è la divisione giusta.

## Configurazione minima

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

@tool
def get_weather(city: str) -> dict[str, float | str]:
    """Return the current weather for a city."""
    return {"city": city, "temperature_c": 21.5, "conditions": "partly cloudy"}

codeact = HyperlightCodeActProvider(
    tools=[get_weather],
    approval_mode="never_require",
)

agent = Agent(
    client=client,
    name="CodeActAgent",
    instructions="You are a helpful assistant.",
    context_providers=[codeact],
)
```

## Quando usare CodeAct (e quando no)

**Usa CodeAct quando:**
- Il task concatena molte piccole chiamate a strumenti (lookup, join, calcoli)
- La latenza e il costo dei token contano
- Vuoi un isolamento forte per chiamata sul codice generato dal modello

**Resta con il tool-calling tradizionale quando:**
- L'agente fa solo una o due chiamate a strumenti per turno
- Ogni chiamata ha effetti collaterali da approvare individualmente
- Le descrizioni degli strumenti sono scarse o ambigue

## Provalo ora

```bash
pip install agent-framework-hyperlight --pre
```

Leggi il [post completo sul blog di Agent Framework](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) per una copertura più approfondita.
