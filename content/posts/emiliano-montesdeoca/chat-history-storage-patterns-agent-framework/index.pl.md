---
title: "Gdzie Twój Agent Pamięta Rzeczy? Praktyczny Przewodnik po Przechowywaniu Historii Czatu"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Zarządzane przez usługę czy klienta? Liniowe czy z rozgałęzieniami? Decyzja architektoniczna, która decyduje o tym, co naprawdę może robić Twój agent AI — z przykładami kodu w C# i Python."
tags:
  - Agent Framework
  - AI
  - Agents
  - Architecture
  - CSharp
  - Python
---

*Ten post został automatycznie przetłumaczony. Aby zobaczyć oryginalną wersję, [kliknij tutaj]({{< ref "index.md" >}}).*

Budując agenta AI, większość energii poświęcasz na model, narzędzia i prompty. Pytanie *gdzie żyje historia rozmowy* wydaje się szczegółem implementacyjnym — ale jest jedną z najważniejszych decyzji architektonicznych, jakie podejmiesz.

Decyduje o tym, czy użytkownicy mogą rozgałęziać rozmowy, cofać odpowiedzi, wznawiać sesje po restarcie oraz czy Twoje dane kiedykolwiek opuszczają Twoją infrastrukturę. [Zespół Agent Framework opublikował szczegółową analizę](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/).

## Dwa podstawowe wzorce

**Zarządzane przez usługę**: usługa AI przechowuje stan rozmowy. Twoja aplikacja trzyma referencję, a usługa automatycznie dołącza odpowiednią historię do każdego żądania.

**Zarządzane przez klienta**: Twoja aplikacja utrzymuje pełną historię i wysyła odpowiednie wiadomości z każdym żądaniem. Usługa jest bezstanowa. Kontrolujesz wszystko.

## Jak Agent Framework to abstrahuje

```csharp
AgentSession session = await agent.CreateSessionAsync();
var first = await agent.RunAsync("Mam na imię Alice.", session);
var second = await agent.RunAsync("Jak mam na imię?", session);
```

```python
session = agent.create_session()
first = await agent.run("Mam na imię Alice.", session=session)
second = await agent.run("Jak mam na imię?", session=session)
```

## Szybki przegląd dostawców

| Dostawca | Przechowywanie | Model | Kompaktowanie |
|----------|---------|-------|------------|
| OpenAI/Azure Chat Completions | Klient | N/A | Ty |
| Foundry Agent Service | Usługa | Liniowy | Usługa |
| Responses API (domyślnie) | Usługa | Rozgałęziający | Usługa |
| Anthropic Claude, Ollama | Klient | N/A | Ty |

## Jak wybrać

1. **Potrzebujesz rozgałęzień lub „cofnij"?** → Responses API zarządzane przez usługę
2. **Potrzebujesz suwerenności danych?** → Zarządzane przez klienta z backendem DB
3. **Prosty chatbot?** → Liniowe zarządzane przez usługę wystarczy

Przeczytaj [pełny post](https://devblogs.microsoft.com/agent-framework/chat-history-storage-patterns-in-microsoft-agent-framework/) po kompletne drzewo decyzyjne.
