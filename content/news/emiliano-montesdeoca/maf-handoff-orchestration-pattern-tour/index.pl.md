---
title: "Wzorzec Handoff: Gdy Jeden Agent To Za Mało"
date: 2026-06-01
author: "Emiliano Montesdeoca"
description: "Wzorzec orkiestracji Handoff w Microsoft Agent Framework pozwala agentom decydować, kto obsługuje następną turę — bez utraty kontekstu rozmowy ani naruszania reguł topologii."
tags:
  - Agent Framework
  - AI
  - .NET
  - Multi-agent
  - Orchestration
---

W pewnym momencie każdy system wieloagentowy przerasta prosty router. Pierwszym sygnałem jest zazwyczaj sytuacja, gdy specjalistyczny agent musi zadać pytanie uzupełniające lub w połowie tury uświadamia sobie, że powinien kontynuować inny agent. Stały pipeline zawodzi w tym miejscu. Router jednorazowy zawodzi w tym miejscu.

To właśnie problem, który wzorzec orkiestracji Handoff w Microsoft Agent Framework jest zaprojektowany do rozwiązania.

## Jak Działa Handoff

Deweloper deklaruje graf: oto agenci, oto krawędzie między nimi. Framework robi resztę — syntetyzuje narzędzie handoff dla każdej krawędzi wychodzącej i wstrzykuje je do każdego agenta. Gdy agent zdecyduje się przekazać kontrolę, wywołuje narzędzie. Framework wymusza topologię.

Trzy rzeczy odróżniają to od zwykłego wzajemnego wywoływania agentów:

1. **Jeden wspólny transkrypt** — agent odbierający widzi pełną historię rozmowy. Bez zaczynania od zera.
2. **Wymuszanie topologii** — agent może wykonać handoff tylko do zadeklarowanych celów. Błędy routingu są wykrywane podczas tworzenia, nie w środowisku produkcyjnym.
3. **Naturalne zakończenie** — gdy aktywny agent kończy swoją turę bez wywoływania narzędzia handoff, workflow oddaje kontrolę użytkownikowi. Bez pollingu, bez jawnych warunków wyjścia.

## Minimalny Przykład

W .NET budowanie workflow handoff wygląda tak:

```csharp
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Workflows;

AIAgent triage = chatClient.AsAIAgent(
    instructions: "Route to the right specialist.",
    name: "Triage");

AIAgent billing = chatClient.AsAIAgent(
    instructions: "Handle billing questions.",
    name: "Billing");

AIAgent tech = chatClient.AsAIAgent(
    instructions: "Handle technical support.",
    name: "Tech");

var workflow = HandoffWorkflow.Create()
    .Add(triage, targets: [billing, tech])
    .Add(billing, targets: [triage])
    .Add(tech, targets: [triage, billing]);
```

Triage może wysyłać do każdego ze specjalistów. Obaj specjaliści mogą odsyłać z powrotem do triage. Graf jest acykliczny, ale obsługuje krawędzie wsteczne gdy są potrzebne ("potrzebuję więcej informacji" → powrót do badań).

## Kiedy Używać Handoff (i Kiedy Nie)

Handoff to dobry wybór gdy:

- **Własność może zmienić się w połowie rozmowy** — agent może uświadomić sobie, że jest złym specjalistą
- **Krawędzie wsteczne mają znaczenie** — może być konieczne ponowne odwiedzenie poprzedniego kroku bez restartu
- **Decyzje routingu są subtelne** — decyzja o wykonaniu handoff jest kontekstualna i lepiej podejmowana przez model niż typowane predykaty

*Nie* jest właściwym wyborem gdy:

- Twój pipeline jest stały i sekwencyjny — użyj workflow `Sequential`
- Każdy krok jest niezależny — agenci dzielący transkrypt, którego potrzebował tylko jeden z nich, to po prostu szum
- Potrzebujesz rygorystycznych gwarancji przetwarzania — niedeterminizm routingu opartego na modelu nie jest tym, czego chcesz

## Krawędzie Wsteczne i Human-in-the-Loop

Jedną z najciekawszych form, które Handoff umożliwia, są prawdziwe krawędzie wsteczne. Agent może zdecydować "nie mam wystarczających informacji" i przekierować z powrotem do kroku badawczego — nie za pomocą zakodowanej pętli, lecz dlatego, że model decyduje, że to właściwa decyzja.

Interakcje human-in-the-loop komponują się naturalnie. Gdy specjalista potrzebuje danych wejściowych od użytkownika, workflow oddaje kontrolę użytkownikowi za pomocą domyślnej pętli tur, zbiera odpowiedź i wznawia pracę z pełnym kontekstem. Agent nigdy nie stracił rozmowy.

## Podsumowanie

Handoff to jeden z tych wzorców, które wyglądają prosto, ale umożliwiają wiele po zinternalizowaniu: zdecentralizowany routing, wspólny kontekst, wymuszona topologia, naturalne zakończenie. To właściwy następny krok, gdy Twoi agenci zaczynają mówić "właściwie, ktoś inny powinien to obsłużyć."

Przeczytaj pełny przewodnik w oryginalnym wpisie: [A Tour of the Handoff Orchestration Pattern](https://devblogs.microsoft.com/agent-framework/a-tour-of-handoff-orchestration-pattern/)
