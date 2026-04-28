---
title: "CodeAct al Agent Framework: Com Reduir la Latència del teu Agent a la Meitat"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct col·lapsa cadenes d'eines de múltiples passos en un únic bloc de codi sandboxed — reduint la latència un 52% i l'ús de tokens un 64%. Aquí tens el que significa pels teus agents i quan fer-lo servir."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Aquest post ha estat traduït automàticament. Per a la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Hi ha un moment en tot projecte d'agents en què mires el trace i penses: "per què tarda tant això?" El model està bé. Les eines funcionen. Però hi ha set round trips per obtenir un resultat que es podria calcular d'una sola vegada.

Exactament aquest és el problema que resol CodeAct — i l'[equip d'Agent Framework acaba de publicar suport alpha](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) a través del nou paquet `agent-framework-hyperlight`.

## Què és CodeAct?

El [patró CodeAct](https://arxiv.org/abs/2402.01030) és elegantment simple: en lloc de donar al model una llista d'eines i deixar-lo cridar-les una per una, li dones una única eina `execute_code` i li permets expressar el *pla complet* com un programa Python curt. L'agent escriu el codi una vegada, el sandbox l'executa, i tornes a rebre un únic resultat consolidat.

Un pla de cinc passos que abans requeria cinc torns del model ara es converteix en un torn `execute_code` que conté un script Python que crida les teves eines via `call_tool(...)`.

El benchmark del repositori ho fa concret. Vuit usuaris, dotzenes de comandes, cinc eines. Mateix model, mateixes eines, mateix prompt — només cablejat diferent:

| Cablejat | Temps | Tokens |
|--------|------|--------|
| Tradicional | 27.81s | 6.890 |
| CodeAct | 13.23s | 2.489 |
| **Millora** | **52,4%** | **63,9%** |

## La peça de seguretat: micro-VMs de Hyperlight

El paquet `agent-framework-hyperlight` utilitza micro-VMs de [Hyperlight](https://github.com/hyperlight-dev/hyperlight). Cada crida `execute_code` obté la seva pròpia micro-VM recentment creada — amb la seva pròpia memòria, sense accés al sistema de fitxers del host més enllà del que muntes explícitament. L'arrencada es mesura en mil·lisegons.

Les teves eines segueixen executant-se al host. El *codi de pegament* generat pel model s'executa en el sandbox. Aquesta és la divisió correcta.

## Com connectar-ho

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

## Quan fer servir CodeAct (i quan no)

**Fes servir CodeAct quan:**
- La tasca encadena moltes crides petites a eines (consultes, joins, càlculs, formatació)
- Et preocupa la latència i el cost de tokens
- Vols aïllament fort per crida en codi generat pel model

**Queda't amb el tool-calling tradicional quan:**
- L'agent només fa una o dues crides a eines per torn
- Cada crida té efectes secundaris que vols aprovar individualment
- Les descripcions d'eines són escasses o ambigües

## Prova-ho ara

```bash
pip install agent-framework-hyperlight --pre
```

Consulta el [post complet al blog d'Agent Framework](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) per a cobertura més profunda.
