---
title: "Microsoft Agent Framework osiąga wersję 1.0 — co naprawdę ważne dla programistów .NET"
date: 2026-04-03
author: "Emiliano Montesdeoca"
description: "Microsoft Agent Framework 1.0 jest gotowy do produkcji ze stabilnym API, orkiestracją wieloagentową i łącznikami dla każdego głównego dostawcy AI. Oto co musisz wiedzieć jako programista .NET."
tags:
  - agent-framework
  - dotnet
  - ai
  - semantic-kernel
  - azure-openai
  - multi-agent
---

> *Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "agent-framework-1-0-production-ready" >}}).*

Jeśli śledzisz historię Agent Framework od wczesnych dni Semantic Kernel i AutoGen, ta wiadomość jest znacząca. Microsoft Agent Framework właśnie [osiągnął wersję 1.0](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/) — gotowy do produkcji, stabilne API, zobowiązanie do długoterminowego wsparcia. Jest dostępny zarówno dla .NET, jak i Python i naprawdę gotowy na prawdziwe obciążenia.

Pominę hałas ogłoszenia i skupię się na tym, co ważne, jeśli budujesz aplikacje oparte na AI w .NET.

## Krótka wersja

Agent Framework 1.0 łączy to, co kiedyś było Semantic Kernel i AutoGen, w jeden otwarty SDK. Jedna abstrakcja agenta. Jeden silnik orkiestracji. Wielu dostawców AI. Jeśli skakałeś między Semantic Kernel dla wzorców enterprise i AutoGen dla przepływów pracy wieloagentowych klasy badawczej, możesz przestać. To jest teraz jeden SDK.

## Pierwsze kroki są niemal wstydliwie proste

Oto działający agent w .NET:

```csharp
// dotnet add package Microsoft.Agents.AI.OpenAI --prerelease
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Foundry;
using Azure.Identity;

var agent = new AIProjectClient(endpoint: "https://your-project.services.ai.azure.com")
    .GetResponsesClient("gpt-5.3")
    .AsAIAgent(
        name: "HaikuBot",
        instructions: "You are an upbeat assistant that writes beautifully."
    );

Console.WriteLine(await agent.RunAsync("Write a haiku about shipping 1.0."));
```

To wszystko. Kilka linii i masz agenta AI działającego przeciwko Azure Foundry. Odpowiednik w Python jest równie zwięzły. Dodawaj narzędzia funkcji, rozmowy wieloturowe i streaming w miarę potrzeb — powierzchnia API skaluje się bez dziwactw.

## Orkiestracja wieloagentowa — to jest prawdziwa sprawa

Pojedynczy agent jest w porządku dla demonstracji, ale scenariusze produkcyjne zazwyczaj wymagają koordynacji. Agent Framework 1.0 dostarcza przetestowane w boju wzorce orkiestracji prosto z Microsoft Research i AutoGen:

- **Sekwencyjne** — agenty przetwarzają po kolei (autor → recenzent → redaktor)
- **Współbieżne** — rozgałęź do wielu agentów równolegle, zbierz wyniki
- **Przekazywanie** — jeden agent deleguje do innego na podstawie intencji
- **Czat grupowy** — wielu agentów dyskutuje i dochodzi do rozwiązania
- **Magentic-One** — wzorzec wieloagentowy klasy badawczej z MSR

Wszystkie wspierają streaming, punkty kontrolne, zatwierdzenia przez człowieka w pętli oraz wstrzymanie/wznowienie. Część dotycząca punktów kontrolnych jest kluczowa — długo działające przepływy pracy przeżywają ponowne uruchomienie procesu. Dla nas, programistów .NET, którzy budowali trwałe przepływy pracy z Azure Functions, to brzmi znajomo.

## Funkcje, które mają największe znaczenie

Oto moja lista tego, co warto znać:

**Haki middleware.** Wiesz, jak ASP.NET Core ma potoki middleware? Ten sam koncept, ale dla wykonania agenta. Przechwytuj każdy etap — dodawaj bezpieczeństwo treści, logowanie, zasady zgodności — bez dotykania promptów agenta. To właśnie sprawia, że agenty są gotowe na środowisko enterprise.

**Podłączalna pamięć.** Historia rozmów, trwały stan klucz-wartość, wyszukiwanie wektorowe. Wybierz backend: Foundry Agent Service, Mem0, Redis, Neo4j lub własny. Pamięć to właśnie to, co zmienia bezstanowe wywołanie LLM w agenta, który naprawdę zapamiętuje kontekst.

**Deklaratywne agenty YAML.** Zdefiniuj instrukcje, narzędzia, pamięć i topologię orkiestracji agenta w wersjonowanych plikach YAML. Ładuj i uruchamiaj jednym wywołaniem API. To zmienia zasady gry dla zespołów, które chcą iterować zachowanie agentów bez ponownego wdrażania kodu.

**Wsparcie A2A i MCP.** MCP (Model Context Protocol) pozwala agentom dynamicznie odkrywać i wywoływać zewnętrzne narzędzia. A2A (protokół Agent-to-Agent) umożliwia współpracę między różnymi środowiskami uruchomieniowymi — twoje agenty .NET mogą koordynować z agentami działającymi w innych frameworkach. Wsparcie A2A 1.0 pojawi się wkrótce.

## Funkcje podglądowe warte obserwowania

Niektóre funkcje zostały dostarczone jako podgląd w 1.0 — działające, ale API może się ewoluować:

- **DevUI** — lokalny debugger w przeglądarce do wizualizacji wykonania agenta, przepływów wiadomości i wywołań narzędzi w czasie rzeczywistym. Pomyśl Application Insights, ale dla rozumowania agenta.
- **GitHub Copilot SDK i Claude Code SDK** — używaj Copilot lub Claude jako narzędzia agenta bezpośrednio z kodu orkiestracji. Skomponuj agenta zdolnego do kodowania obok innych agentów w tym samym przepływie pracy.
- **Agent Harness** — konfigurowalne lokalne środowisko uruchomieniowe dające agentom dostęp do powłoki, systemu plików i pętli wiadomości. Pomyśl agenty kodujące i wzorce automatyzacji.
- **Skills** — pakiety wielokrotnego użytku z możliwościami domeny, które od razu dają agentom ustrukturyzowane umiejętności.

## Migracja z Semantic Kernel lub AutoGen

Jeśli masz istniejący kod Semantic Kernel lub AutoGen, dostępne są dedykowane asystenty migracji, które analizują kod i generują plany migracji krok po kroku. [Przewodnik migracji z Semantic Kernel](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-semantic-kernel) i [przewodnik migracji z AutoGen](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen) prowadzą przez wszystko.

Jeśli korzystałeś z pakietów RC, uaktualnienie do 1.0 to tylko zmiana wersji.

## Podsumowanie

Agent Framework 1.0 to kamień milowy produkcji, na który czekały zespoły enterprise. Stabilne API, wsparcie dla wielu dostawców, wzorce orkiestracji działające w skali i ścieżki migracji zarówno z Semantic Kernel, jak i AutoGen.

Framework jest [w pełni open source na GitHub](https://github.com/microsoft/agent-framework), a możesz zacząć już dziś z `dotnet add package Microsoft.Agents.AI`. Sprawdź [przewodnik szybkiego startu](https://learn.microsoft.com/en-us/agent-framework/get-started/) i [przykłady](https://github.com/microsoft/agent-framework), by zabrać się do pracy.

Jeśli czekałeś na sygnał "bezpieczne do użycia w produkcji" — to jest właśnie ten moment.
