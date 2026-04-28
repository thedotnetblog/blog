---
title: "CodeAct im Agent Framework: Wie du die Latenz deines Agenten halbierst"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct fasst mehrstufige Tool-Chains in einem einzigen sandboxed Code-Block zusammen — 52% weniger Latenz und 64% weniger Token-Verbrauch. Was das für deine Agenten bedeutet und wann du es einsetzen solltest."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Dieser Beitrag wurde automatisch übersetzt. Zur Originalversion [hier klicken]({{< ref "index.md" >}}).*

Es gibt diesen Moment in jedem Agenten-Projekt, wo man auf den Trace schaut und denkt: „Warum dauert das so lange?" Das Modell ist gut. Die Tools funktionieren. Aber es gibt sieben Round Trips für ein Ergebnis, das man in einem Schritt berechnen könnte.

Genau dieses Problem löst CodeAct — und das [Agent Framework Team hat soeben Alpha-Unterstützung dafür veröffentlicht](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) mit dem neuen Paket `agent-framework-hyperlight`.

## Was ist CodeAct?

Das [CodeAct-Muster](https://arxiv.org/abs/2402.01030) ist elegant einfach: Statt dem Modell eine Liste von Tools zu geben und sie einzeln aufrufen zu lassen, gibst du ihm ein einziges `execute_code`-Tool und lässt es den *gesamten Plan* als kurzes Python-Programm ausdrücken. Der Agent schreibt den Code einmal, die Sandbox führt ihn aus, und du erhältst ein einziges konsolidiertes Ergebnis zurück.

Ein Fünf-Schritte-Plan, der früher fünf Modell-Turns benötigte, wird zu einem einzigen `execute_code`-Turn mit einem Python-Script, das deine Tools über `call_tool(...)` aufruft.

| Verdrahtung | Zeit | Tokens |
|--------|------|--------|
| Traditionell | 27,81s | 6.890 |
| CodeAct | 13,23s | 2.489 |
| **Verbesserung** | **52,4%** | **63,9%** |

## Die Sicherheitskomponente: Hyperlight Micro-VMs

Das Paket `agent-framework-hyperlight` verwendet [Hyperlight](https://github.com/hyperlight-dev/hyperlight) Micro-VMs. Jeder `execute_code`-Aufruf erhält eine eigene frisch erstellte Micro-VM — mit eigenem Speicher, ohne Zugriff auf das Host-Dateisystem außer dem, was du explizit mountest. Der Start wird in Millisekunden gemessen. Die Isolierung ist im Grunde kostenlos.

Deine Tools laufen weiterhin auf dem Host. Der modellgenerierte *Klebecode* läuft in der Sandbox. Das ist die richtige Aufteilung.

## Einrichtung

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

## Wann CodeAct verwenden (und wann nicht)

**CodeAct verwenden, wenn:**
- Die Aufgabe viele kleine Tool-Aufrufe verkettet (Lookups, Joins, Berechnungen)
- Latenz und Token-Kosten wichtig sind
- Du starke Isolierung für modellgenerierten Code willst

**Beim traditionellen Tool-Calling bleiben, wenn:**
- Der Agent nur ein oder zwei Tool-Aufrufe pro Turn macht
- Jeder Aufruf Nebeneffekte hat, die einzeln genehmigt werden sollen
- Tool-Beschreibungen spärlich oder mehrdeutig sind

## Jetzt ausprobieren

```bash
pip install agent-framework-hyperlight --pre
```

Den vollständigen Beitrag findest du im [Agent Framework Blog](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/).
