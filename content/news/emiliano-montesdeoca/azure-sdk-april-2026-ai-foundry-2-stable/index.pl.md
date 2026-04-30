---
title: "Azure SDK: kwiecień 2026, AI Foundry 2.0 i to, co deweloperzy .NET powinni wiedzieć"
date: 2026-04-25
author: "Emiliano Montesdeoca"
description: "Wydanie Azure SDK z kwietnia 2026 przynosi stabilne Azure.AI.Projects 2.0.0 z ważnymi zmianami łamiącymi zgodność, krytyczne poprawki bezpieczeństwa dla Cosmos DB i falę nowych bibliotek Provisioning dla .NET."
tags:
  - "Azure SDK"
  - "AI Foundry"
  - "Azure"
  - ".NET"
  - "NuGet"
---

*Ten post został automatycznie przetłumaczony. Aby przejść do oryginału, [kliknij tutaj]({{< ref "index.md" >}}).*

Miesięczne wydania SDK łatwo przeoczyć. To ma kilka rzeczy, na które warto zwrócić uwagę — zwłaszcza jeśli budujesz z AI Foundry, używasz Cosmos DB w Javie albo przygotowujesz infrastrukturę z kodu .NET.

## Azure.AI.Projects 2.0.0 — zmiany łamiące zgodność, które mają sens

Pakiet NuGet `Azure.AI.Projects` osiąga stabilne 2.0.0 z kilkoma istotnymi zmianami architektury. Jeśli korzystasz już z preview, to właśnie się zmieniło:

- **Podział namespace'ów**: Evaluations przeniesiono do `Azure.AI.Projects.Evaluation`, a operacje memory do `Azure.AI.Projects.Memory`. Trzeba zaktualizować `using`.
- **Zmienione nazwy typów**: `Insights` → `ProjectInsights`, `Schedules` → `ProjectSchedules`, `Evaluators` → `ProjectEvaluators`, `Trigger` → `ScheduleTrigger`
- **Konwencje nazewnictwa**: właściwości logiczne teraz konsekwentnie stosują konwencję `Is*`

To ten rodzaj zmian łamiących zgodność, który boli raz, a potem wydaje się po prostu słuszny. Jeśli budowałeś na preview, zaktualizuj importy i pozwól kompilatorowi wskazać resztę.

Dobra wiadomość: teraz to stabilne. Możesz już naprawdę polegać na tym API.

## Cosmos DB Java: krytyczna poprawka bezpieczeństwa (RCE)

To poważna sprawa. Biblioteka Java Cosmos DB (`azure-cosmos`) w wersji 4.79.0 zawiera krytyczną poprawkę bezpieczeństwa dla **Remote Code Execution vulnerability (CWE-502)**.

Problem dotyczył deserializacji Java w `CosmosClientMetadataCachesSnapshot`, `AsyncCache` i `DocumentCollection`. Poprawka zastępuje deserializację Java serializacją opartą na JSON, eliminując całą klasę ataków deserializacyjnych.

Jeśli masz jakiekolwiek usługi Java korzystające z Azure Cosmos DB, zaktualizuj natychmiast do 4.79.0. To nie jest opcjonalne.

## Nowe biblioteki Provisioning dla .NET

W tym miesiącu kilka stabilnych bibliotek Provisioning trafiło do wersji 1.0.0 — to biblioteki, które pozwalają definiować infrastrukturę Azure w kodzie C# zamiast w szablonach ARM lub Bicep:

- [Azure.Provisioning.Network 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.Network/1.0.0)
- [Azure.Provisioning.PrivateDns 1.0.0](https://www.nuget.org/packages/Azure.Provisioning.PrivateDns/1.0.0)

Kilka kolejnych jest w beta.1 i obejmuje API Management, Batch, Compute, Monitor, MySQL oraz Security Center. Jeśli robisz infrastructure-as-code z .NET — szczególnie z wdrożeniami Aspire — te biblioteki są twoim punktem wejścia.

## Azure AI Agents Java: 2.0.0 GA

Biblioteka Java Azure AI Agents również osiąga w tym miesiącu general availability. Najważniejsze zmiany łamiące zgodność:

- Kilka typów enum przeniesiono do klas opartych na `ExpandableStringEnum` (bardziej elastyczne dla nowych wartości)
- Klasy modeli `*Param` przemianowano na `*Parameter`
- `MCPToolConnectorId` → `McpToolConnectorId` (spójna wielkość liter)
- Nowy overload wygody dla `beginUpdateMemories`

## Na koniec

Nagłówek dla deweloperów .NET w tym miesiącu jest prosty: `Azure.AI.Projects 2.0.0` staje się stable — jeśli budujesz z AI Foundry, to czas przypiąć stabilną wersję i zaktualizować importy. Dla zespołów Java używających Cosmos DB aktualizacja bezpieczeństwa jest pilna.

Pełne notatki wydania są na [aka.ms/azsdk/releases](https://aka.ms/azsdk/releases). Oryginalny wpis: [Azure SDK Release (April 2026)](https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-april-2026/).