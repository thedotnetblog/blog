---
title: "Trwałe Przepływy Pracy w Microsoft Agent Framework: Od In-Memory do Azure Functions"
date: 2026-05-31
author: "Emiliano Montesdeoca"
description: "Model programowania przepływów pracy MAF obsługuje teraz trwałe wykonanie wspierane przez Durable Task — oto jak budować kompozytowalne przepływy pracy agentów, które przeżywają ponowne uruchomienie procesów i skalują się na Azure Functions."
tags:
  - Agent Framework
  - .NET
  - Azure Functions
  - Durable Task
  - AI
  - Workflows
---

Jeden z problemów z wczesnymi przepływami pracy agentów AI: są kruche. Długotrwały wieloetapowy przepływ pracy powiązany z jednym procesem oznacza, że ponowne uruchomienie procesu = utrata stanu. W przypadku prostych demonstracji jest to w porządku. W przypadku obciążeń produkcyjnych już nie.

Model programowania przepływów pracy Microsoft Agent Framework obsługuje teraz **trwałe wykonanie**, wspierane przez framework Durable Task, z hostingiem Azure Functions. Oto jak działa model programowania i dlaczego historia trwałości jest ważna.

## Podstawowe Elementy Składowe

**Executor'y** są fundamentalną jednostką pracy. Każdy jest typowany — przyjmuje określone dane wejściowe i produkuje określone dane wyjściowe:

```csharp
using Microsoft.Agents.AI.Workflows;

internal sealed class OrderLookup()
    : Executor<OrderCancelRequest, Order>("OrderLookup")
{
    public override async ValueTask<Order> HandleAsync(
        OrderCancelRequest message,
        IWorkflowContext context,
        CancellationToken cancellationToken = default)
    {
        // wyszukaj zamówienie, zwróć je
        return new Order(Id: message.OrderId, ...);
    }
}
```

**Przepływy pracy** łączą executor'y w grafach skierowanych za pomocą fluent buildera. Framework obsługuje wykonanie, przepływ danych między krokami i propagację błędów.

Możesz modelować:
- Sekwencyjne łańcuchy (krok A → krok B → krok C)
- Równoległy fan-out/fan-in (uruchamiać agentów A, B, C równolegle, agregować wyniki)
- Warunkowe rozgałęzianie
- Zatwierdzenia human-in-the-loop (wstrzymanie przepływu pracy, oczekiwanie na zewnętrzny sygnał)

## Runner In-Memory do Lokalnego Rozwoju

Rozpoczęcie jest szybkie:

```csharp
dotnet add package Microsoft.Agents.AI
dotnet add package Microsoft.Agents.AI.Workflows
```

Główny pakiet zawiera lekki runner w procesie. Bez zewnętrznych zależności, bez bazy danych, bez zasobów Azure. Świetnie sprawdza się do lokalnego rozwoju i testów jednostkowych.

## Dodawanie Trwałości z Durable Task

Gdy przepływ pracy musi przeżyć ponowne uruchomienie procesu — bo jest długotrwały, bo ma kroki human-in-the-loop, bo jest rozproszony na wielu równoległych wywołaniach agentów — runner in-memory nie wystarczy.

Integracja Durable Task w MAF przechowuje stan przepływu pracy w Azure Storage. Jeśli proces zostanie uruchomiony ponownie, przepływ pracy wznawia się od miejsca, w którym się zatrzymał. Model programowania pozostaje taki sam; wystarczy tylko wymienić runner.

```csharp
dotnet add package Microsoft.Agents.AI.Workflows.DurableTask
```

Te same executor'y, ten sam graf przepływu pracy — wspierany przez trwały stan.

## Hosting Azure Functions

Trzecia warstwa to hosting Azure Functions. Twój przepływ pracy staje się aplikacją Function: wyzwól przepływ pracy przez endpoint HTTP, a trwałe środowisko wykonawcze obsługuje skalowanie, stan i niezawodność.

Oznacza to, że wieloagentowy przepływ pracy z równoległymi wywołaniami, gałęziami warunkowymi i zatwierdzeniami ludzkimi może skalować się w bezserwerowym środowisku Functions bez niestandardowego zarządzania stanem.

## Dlaczego To Jest Ważne

Kombinacja jest znacząca dla prawdziwych systemów AI:

- **Równoległe wywołania agentów** — dystrybucja do wielu wyspecjalizowanych agentów jednocześnie bez blokowania, agregacja wyników gdy wszyscy zakończą
- **Długotrwałe procesy** — przepływy pracy obejmujące zatwierdzenia ludzi lub zdarzenia zewnętrzne mogą wstrzymywać się i wznawiać przez godziny lub dni
- **Skalowanie** — Azure Functions skaluje wykonanie poziomo; framework Durable Task zarządza koordynacją równoległego stanu

Jeśli budujesz przepływy pracy MAF wykraczające poza proste lokalne demo, to jest droga do wykonania o jakości produkcyjnej.

Oryginalny post: [Durable Workflows in the Microsoft Agent Framework](https://devblogs.microsoft.com/dotnet/durable-workflows-in-microsoft-agent-framework/)
