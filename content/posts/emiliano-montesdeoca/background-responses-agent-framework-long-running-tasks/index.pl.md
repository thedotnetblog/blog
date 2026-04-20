---
title: "Odpowiedzi w Tle w Microsoft Agent Framework: Koniec z Lękiem Przed Timeoutem"
date: 2026-03-26
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework umożliwia teraz odciążanie długotrwałych zadań AI za pomocą tokenów kontynuacji. Oto jak działają odpowiedzi w tle i dlaczego mają znaczenie dla Twoich agentów .NET."
tags:
  - dotnet
  - ai
  - agent-framework
  - azure
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "background-responses-agent-framework-long-running-tasks" >}}).*

Jeśli budowałeś cokolwiek z modelami rozumowania jak o3 lub GPT-5.2, znasz ten ból. Twój agent zaczyna przetwarzać złożone zadanie, klient czeka, a gdzieś między "to jest w porządku" a "czy to się zawiesiło?" połączenie przekracza czas.

Microsoft Agent Framework właśnie dostarczył [odpowiedzi w tle](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) — i szczerze mówiąc, to jedna z tych funkcji, która powinna istnieć od pierwszego dnia.

## Problem z blokującymi wywołaniami

W tradycyjnym wzorcu żądanie-odpowiedź klient blokuje się do momentu zakończenia przez agenta. Odpowiedzi w tle odwracają to do góry nogami.

## Jak działają tokeny kontynuacji

Zamiast blokować, uruchamiasz zadanie agenta i otrzymujesz z powrotem **token kontynuacji**. Pomyśl o tym jak o numerku w garderob. Przepływ jest prosty:

1. Wyślij żądanie z `AllowBackgroundResponses = true`
2. Jeśli agent obsługuje przetwarzanie w tle, otrzymujesz token kontynuacji
3. Odpytuj według harmonogramu, aż token wróci jako `null`

```csharp
AgentRunOptions options = new()
{
    AllowBackgroundResponses = true
};

AgentSession session = await agent.CreateSessionAsync();
AgentResponse response = await agent.RunAsync(
    "Write a detailed market analysis for the Q4 product launch.", session, options);

while (response.ContinuationToken is not null)
{
    await Task.Delay(TimeSpan.FromSeconds(2));
    options.ContinuationToken = response.ContinuationToken;
    response = await agent.RunAsync(session, options);
}

Console.WriteLine(response.Text);
```

## Kiedy faktycznie tego używać

- **Złożone zadania rozumowania** — wieloetapowe analizy, głębokie badania
- **Długa generacja treści** — szczegółowe raporty, wieloczęściowe dokumenty
- **Nierezualne sieci** — klienci mobilni, wdrożenia brzegowe
- **Asynchroniczne wzorce UX** — prześlij zadanie, zrób coś innego, wróć po wyniki

Sprawdź [pełną dokumentację](https://devblogs.microsoft.com/agent-framework/handling-long-running-operations-with-background-responses/) po kompletny opis API.
