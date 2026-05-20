---
title: "Twój agent AI ma problem z tożsamością (i oto szablon, który go rozwiązuje)"
date: 2026-05-20
author: "Emiliano Montesdeoca"
description: "Nowy szablon azd od Curity i Microsoft pokazuje, jak budować agentów AI używających krótkotrwałych tokenów OAuth z precyzyjnymi zakresami — aby agenci nigdy nie mogli zobaczyć danych, których nie powinni widzieć."
tags:
  - Azure Developer CLI
  - AI
  - Security
  - OAuth
  - Agents
  - Azure
---

W każdym projekcie agenta AI jest taki moment: demo działa idealnie, agent interpretuje język naturalny, wywołuje właściwe API, zwraca właściwe dane. Potem zaczynasz myśleć o prawdziwych użytkownikach.

Co powstrzymuje sesję agenta jednego użytkownika przed zobaczeniem danych innego użytkownika? Co się stanie, jeśli agent zostanie oszukany przez wstrzyknięcie promptu? Co jeśli wywołuje narzędzie w nieoczekiwany sposób?

To nie są przypadki graniczne. To są decyzje projektowe, które musisz podjąć przed wydaniem.

Nowy szablon `azd` od Curity i Microsoft daje ci działające odniesienie dokładnie do tego problemu.

## Podstawowy problem: Uwierzytelnianie ≠ Autoryzacja

Większość przykładów agentów dobrze obsługuje uwierzytelnianie użytkowników. Słabo obsługuje autoryzację. Wiedza *kim* jest użytkownik nie mówi ci *jakie dane* powinien zobaczyć.

Tradycyjna aplikacja kliencka wykonuje przewidywalne wywołania API. Agent AI jest niedeterministyczny — interpretuje język naturalny i decyduje, co wywołać. Może być kreatywny. Może też się mylić. A jeśli zostanie zmanipulowany przez wstrzyknięcie promptu, potrzebujesz reguł, które nie opierają się na dobrym zachowaniu AI.

Rozwiązanie zademonstrowane przez ten szablon: **krótkotrwałe tokeny niosące dokładnie właściwe informacje dla każdego skoku**.

## Jak działa łańcuch tokenów

Szablon używa tokenów dostępu OAuth 2.0 z wymianą tokenów, aby zawęzić uprawnienia na każdym etapie. Token użytkownika jest wymieniany dwukrotnie przed dotarciem do serwera MCP:

1. **Pierwsza wymiana** — zawęża zakres i konwertuje nieprzejrzysty token na JWT
2. **Druga wymiana** — dodaje tożsamość agenta i nowych odbiorców dla skoku serwera MCP

Jak wygląda token serwera MCP:

```json
{
  "scope": "stocks/read",
  "sub": "62c839b8...",
  "aud": "https://mcp.demo.example",
  "customer_id": "178",
  "region": "USA"
}
```

`customer_id` jest osadzony w tokenie przez serwer autoryzacji, nie przekazywany jako parametr kontrolowany przez agenta. API sprawdza token, a nie instrukcje agenta.

To oznacza: nawet jeśli ktoś oszuka agenta, aby próbował pobrać dane innego klienta, token tego nie autoryzuje.

## Co wdraża szablon

Kilkoma poleceniami `azd` otrzymujesz:

- Backend agenta na Microsoft Foundry (C#, SDK Microsoft A2A i MCP)
- Serwer MCP eksponujący przykładowe API portfolio
- Curity Identity Server jako serwer autoryzacji, wraz z Entra ID do uwierzytelniania
- Zewnętrzne i wewnętrzne bramy API obsługujące wymianę tokenów i rejestrowanie audytu
- Bicep dla całej infrastruktury Azure: Container Apps, VNet, ACR, Azure AI Foundry, Key Vault, Azure SQL Database, przechowywanie

Cały wzorzec jest możliwy do inspekcji i dostosowania.

## Zasada projektowa warta zapożyczenia

Nawet jeśli nie używasz Curity, wzorzec jest przenośny: **agenci nigdy nie powinni mieć stałego dostępu do API**. Każda akcja powinna używać krótkotrwałego tokenu z minimalnym zakresem niezbędnym dla tego konkretnego wywołania, wydanego dla konkretnej tożsamości agenta, niosącego roszczenia, których API potrzebuje do podejmowania decyzji autoryzacyjnych.

To wytrzymuje kreatywnych agentów, błędy i wstrzyknięcia promptów w sposób, w jaki "tylko upewnij się, że agent nie robi złych rzeczy" nigdy nie wytrzyma.

## Podsumowanie

Wzorce bezpieczeństwa dla agentów AI są nadal opracowywane w całej branży. Ten szablon jest jedną z najbardziej kompletnych implementacji referencyjnych, jakie widziałem — obejmuje rzeczywisty przepływ autoryzacji, nie tylko uwierzytelnianie.

Oryginalny post: [Least privilege AI agents: A new azd template from Curity and Microsoft](https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/)
