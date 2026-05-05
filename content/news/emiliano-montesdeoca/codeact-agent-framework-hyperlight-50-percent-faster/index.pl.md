---
title: "CodeAct w Agent Framework: Jak zmniejszyć opóźnienie agenta o połowę"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "CodeAct kompresuje wieloetapowe łańcuchy narzędzi do jednego izolowanego bloku kodu — zmniejszając opóźnienie o 52% i zużycie tokenów o 64%."
tags:
  - Agent Framework
  - AI
  - Agents
  - Hyperlight
  - Python
  - MCP
---

*Ten post został przetłumaczony automatycznie. Aby zobaczyć oryginalną wersję, [kliknij tutaj]({{< ref "index.md" >}}).*

W każdym projekcie agentów przychodzi moment, gdy patrzysz na ślad i myślisz: „Dlaczego to tak długo trwa?" Model działa dobrze. Narzędzia działają. Ale jest siedem rund komunikacji, żeby uzyskać wynik, który można obliczyć za jednym razem.

To właśnie problem, który rozwiązuje CodeAct — a [zespół Agent Framework właśnie wydał wsparcie alfa](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/) przez nowy pakiet `agent-framework-hyperlight`.

## Czym jest CodeAct?

[Wzorzec CodeAct](https://arxiv.org/abs/2402.01030) jest elegancko prosty: zamiast dawać modelowi listę narzędzi do wywoływania jedno po drugim, dajesz mu jedno narzędzie `execute_code` i pozwalasz wyrazić *cały plan* jako krótki program w Pythonie.

| Podejście | Czas | Tokeny |
|--------|------|--------|
| Tradycyjne | 27,81s | 6 890 |
| CodeAct | 13,23s | 2 489 |
| **Poprawa** | **52,4%** | **63,9%** |

## Bezpieczeństwo: Mikro-VM Hyperlight

Pakiet `agent-framework-hyperlight` używa mikro-VM [Hyperlight](https://github.com/hyperlight-dev/hyperlight). Każde wywołanie `execute_code` otrzymuje własną, świeżo utworzoną mikro-VM. Uruchomienie mierzone jest w milisekundach. Izolacja jest praktycznie bezpłatna.

Twoje narzędzia nadal działają na hoście. Kod kleju wygenerowany przez model działa w piaskownicy. To właściwy podział.

## Minimalna konfiguracja

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

## Kiedy używać CodeAct (a kiedy nie)

**Używaj CodeAct, gdy:**
- Zadanie łączy wiele małych wywołań narzędzi (wyszukiwania, łączenia, obliczenia)
- Ważne są opóźnienie i koszt tokenów
- Potrzebujesz silnej izolacji dla kodu generowanego przez model

**Zostań przy tradycyjnym wywołaniu narzędzi, gdy:**
- Agent robi tylko jedno lub dwa wywołania na turę
- Każde wywołanie ma skutki uboczne wymagające indywidualnego zatwierdzenia
- Opisy narzędzi są skąpe lub niejednoznaczne

## Wypróbuj teraz

```bash
pip install agent-framework-hyperlight --pre
```

Przeczytaj [pełny post na blogu Agent Framework](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/).
