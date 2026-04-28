---
title: "CodeAct in Agent Framework: Hoe je de latentie van je agent halveert"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct comprimeert meerstapige tool-ketens tot één sandbox-codeblok — 52% minder latentie en 64% minder tokengebruik. Wat het betekent voor je agenten en wanneer je het gebruikt."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Dit bericht is automatisch vertaald. Voor de originele versie, [klik hier]({{< ref "index.md" >}}).*

In elk agentproject is er dat moment waarop je naar de trace kijkt en denkt: "waarom duurt dit zo lang?" Het model werkt goed. De tools doen wat ze moeten doen. Maar er zijn zeven rondes nodig voor een resultaat dat je in één keer kunt berekenen.

Dat is precies het probleem dat CodeAct oplost — en het [Agent Framework team heeft zojuist alpha-ondersteuning uitgebracht](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) via het nieuwe pakket `agent-framework-hyperlight`.

## Wat is CodeAct?

Het [CodeAct-patroon](https://arxiv.org/abs/2402.01030) is elegant eenvoudig: in plaats van het model een lijst tools te geven om één voor één aan te roepen, geef je het één `execute_code`-tool en laat je het het *hele plan* uitdrukken als een kort Python-programma.

| Aanpak | Tijd | Tokens |
|--------|------|--------|
| Traditioneel | 27,81s | 6.890 |
| CodeAct | 13,23s | 2.489 |
| **Verbetering** | **52,4%** | **63,9%** |

## Beveiliging: Hyperlight Micro-VM's

Het pakket `agent-framework-hyperlight` gebruikt [Hyperlight](https://github.com/hyperlight-dev/hyperlight) micro-VM's. Elke `execute_code`-aanroep krijgt zijn eigen verse micro-VM. Opstarten duurt milliseconden. De isolatie is vrijwel gratis.

Je tools blijven op de host draaien. De door het model gegenereerde *lijmcode* draait in de sandbox. Dat is de juiste verdeling.

## Minimale configuratie

```python
from agent_framework import Agent, tool
from agent_framework_hyperlight import HyperlightCodeActProvider

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

## Wanneer CodeAct gebruiken (en wanneer niet)

**Gebruik CodeAct wanneer:**
- De taak veel kleine tool-aanroepen aan elkaar koppelt (lookups, joins, berekeningen)
- Latentie en tokenkosten tellen
- Je sterke isolatie wil voor door het model gegenereerde code

**Blijf bij traditionele tool-calling wanneer:**
- De agent slechts één of twee tool-aanroepen per beurt maakt
- Elke aanroep bijwerkingen heeft die individueel goedgekeurd moeten worden

## Probeer het nu

```bash
pip install agent-framework-hyperlight --pre
```

Lees het [volledige bericht op de Agent Framework blog](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/).
