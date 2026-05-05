---
title: "GPT-5.5 Jest Tutaj i Trafia do Azure Foundry — Co Muszą Wiedzieć Deweloperzy .NET"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "GPT-5.5 jest ogólnie dostępny w Microsoft Foundry. Ewolucja od GPT-5 do 5.5, co naprawdę się poprawiło i jak zacząć używać go w swoich agentach już dziś."
tags:
  - AI
  - Foundry
  - Azure
  - Agent Framework
  - GPT-5
---

*Ten post został automatycznie przetłumaczony. Aby zobaczyć oryginalną wersję, [kliknij tutaj]({{< ref "index.md" >}}).*

Microsoft właśnie ogłosił, że [GPT-5.5 jest ogólnie dostępny w Microsoft Foundry](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/). Jeśli budujesz agentów na Azure, to jest aktualizacja, na którą czekałeś.

## Ewolucja GPT-5

- **GPT-5**: połączył rozumowanie i szybkość w jednym systemie
- **GPT-5.4**: silniejsze rozumowanie wieloetapowe, wczesne możliwości agentyczne dla enterprise
- **GPT-5.5**: głębsze rozumowanie w długim kontekście, bardziej niezawodne wykonanie agentyczne, lepsza wydajność tokenów

## Co naprawdę się zmieniło

**Ulepszone kodowanie agentyczne**: GPT-5.5 utrzymuje kontekst w dużych bazach kodu, diagnozuje awarie architektoniczne i przewiduje wymagania testowe. Model rozumuje, na *co jeszcze* wpływa poprawka, zanim zadziała.

**Wydajność tokenów**: Wyższa jakość danych wyjściowych przy mniejszej liczbie tokenów i mniej prób. Bezpośrednio obniżone koszty i opóźnienia w produkcji.

## Cennik

| Model | Wejście ($/M tokenów) | Pamięć podręczna | Wyjście ($/M tokenów) |
|-------|-------------------|--------------|---------------------|
| GPT-5.5 | $5,00 | $0,50 | $30,00 |
| GPT-5.5 Pro | $30,00 | $3,00 | $180,00 |

## Dlaczego Foundry jest ważny

Foundry Agent Service umożliwia definiowanie agentów w YAML lub połączenie ich z Microsoft Agent Framework, GitHub Copilot SDK, LangGraph lub OpenAI Agents SDK — i uruchamianie ich jako izolowanych hostowanych agentów z trwałym systemem plików, tożsamością Microsoft Entra i cenami scale-to-zero.

```csharp
AIAgent agent = aiProjectClient
    .AsAIAgent("gpt-5.5", instructions: "Jesteś pomocnym asystentem.", name: "MójAgent");
```

Sprawdź [pełne ogłoszenie](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/).
