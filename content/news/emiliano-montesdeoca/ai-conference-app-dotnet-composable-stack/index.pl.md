---
title: "Budowanie aplikacji konferencyjnej z AI przy użyciu składanego stosu .NET"
date: 2026-05-06
author: "Emiliano Montesdeoca"
description: "Microsoft zbudował ConferencePulse — aplikację Blazor dla konferencji na żywo — łącząc Microsoft.Extensions.AI, DataIngestion, VectorData, MCP i Agent Framework. Oto jak elementy do siebie pasują."
tags:
  - .NET
  - AI
  - Architecture
  - Developer Productivity
---

*Ten post został automatycznie przetłumaczony. Kliknij [tutaj]({{< ref "index.md" >}}), aby zobaczyć oryginalną wersję.*

[Budowanie aplikacji konferencyjnej z AI przy użyciu składanego stosu .NET](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) — Microsoft zbudował ConferencePulse, aplikację Blazor Server do sesji konferencyjnych na żywo, łącząc pięć bibliotek rozszerzeń .NET. Była używana na MVP Summit.

## Co robi ConferencePulse

ConferencePulse działa podczas sesji na żywo i zapewnia: ankiety generowane przez AI z treści sesji, pytania i odpowiedzi od publiczności z potokiem RAG pobierającym z bazy wiedzy na żywo, automatycznie generowane spostrzeżenia oraz podsumowania sesji produkowane przez wiele równoczesnych agentów AI. Stos to .NET 10, Blazor Server, Aspire, podzielony na pięć projektów: Web, Core, Ingestion, Agents, Mcp i AppHost.

## Microsoft.Extensions.AI: jedna abstrakcja dla wszystkiego

`IChatClient` to ujednolicona abstrakcja — konfiguruje się ją raz i ten sam interfejs działa dla Azure OpenAI, OpenAI, Anthropic lub dowolnego innego dostawcy. Sześć linii, aby uzyskać w pełni skonfigurowanego klienta z wywoływaniem funkcji, śledzeniem OpenTelemetry i oprogramowaniem pośredniczącym do logowania:

```csharp
services.AddChatClient(new AzureOpenAIClient(...).GetChatClient("gpt-4o"))
    .UseFunctionInvocation()
    .UseOpenTelemetry()
    .UseLogging();
```

Ten sam `IChatClient` jest ponownie używany później w kroku wzbogacania pozyskiwania danych — bez potrzeby oddzielnego klienta.

## Potok DataIngestion

Treść sesji przepływa przez potok: `MarkdownReader` → `HeaderChunker` (500 tokenów, 50 tokenów nakładki) → `SummaryEnricher` + `KeywordEnricher` → `VectorStoreWriter` (Qdrant). Wzbogacacze używają tego samego `IChatClient` do generowania streszczeń i wyodrębniania słów kluczowych przed indeksowaniem. Pytania publiczności, pary pytań i odpowiedzi oraz wyniki ankiet są pozyskiwane w czasie rzeczywistym w miarę postępu sesji — baza wiedzy rośnie podczas rozmowy.

## VectorData: wyszukiwanie niezależne od dostawcy

`VectorStoreCollection.SearchAsync()` działa tak samo niezależnie od tego, czy magazyn bazowy to Qdrant czy Azure AI Search. Wyszukiwanie hybrydowe (wektory + pełny tekst) jest obsługiwane. Potok RAG dla pytań i odpowiedzi publiczności odpytuje tę kolekcję i otrzymuje odpowiednie fragmenty do przekazania jako kontekst do klienta czatu.

## MCP: treść sesji jako narzędzia

Treść sesji jest udostępniana przez MCP, dzięki czemu każdy klient zgodny z MCP może uzyskać do niej dostęp. Zarówno serwer, jak i klient są zaimplementowane — serwer udostępnia wiedzę z sesji jako narzędzia MCP, a klient umożliwia wywoływanie tych narzędzi z wnętrza potoku agenta.

## Agent Framework: równoległa wieloagentowa podsumowanie

Podsumowanie sesji jest generowane przez trzech agentów działających równocześnie — `PollSummaryAgent`, `QuestionSummaryAgent` i `InsightSummaryAgent` — a następnie scalane. Używa to wzorca czatu grupowego lub równoległego wykonywania z Microsoft Agent Framework. Każdy agent obsługuje jeden aspekt; orkiestrator scala dane wyjściowe.

## Zasada projektowania

Post zawiera punkt wart zapamiętania: używaj najprostszego narzędzia, które pasuje. Bezpośrednie wywołania `IChatClient` dla prostych zadań generowania. Wywołania narzędzi/funkcji do wyodrębniania danych strukturalnych. Pełne agenty tylko wtedy, gdy potrzebujesz autonomicznego wieloetapowego rozumowania. Warstwowanie bibliotek to wymusza — możesz używać `Microsoft.Extensions.AI` bez pobierania pełnego Agent Framework.

Zobacz [pełny post](https://devblogs.microsoft.com/dotnet/building-ai-conference-app-dotnet-composable-stack/) po kompletną strukturę projektu i linki do źródeł.
