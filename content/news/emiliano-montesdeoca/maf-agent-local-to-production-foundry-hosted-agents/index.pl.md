---
title: "Twój Lokalny Agent MAF Właśnie Znalazł Dom w Produkcji"
date: 2026-05-30
author: "Emiliano Montesdeoca"
description: "Foundry Hosted Agents daje agentowi Microsoft Agent Framework tożsamość, skalowanie, trwałość sesji i obserwowalność bez dodatkowej konfiguracji. Oto jak wygląda to w praktyce."
tags:
  - Agent Framework
  - Foundry
  - Azure
  - AI
  - Deployment
---

Sprawienie, żeby agent działał lokalnie, to zabawna część. Trudna część to wszystko, co następuje potem: wdrożenie go bez utraty zdrowego rozsądku, zarządzanie sesjami, konfiguracja tożsamości, podłączenie obserwowalności. Zwykle oznacza to dużo niestandardowej infrastruktury.

Foundry Hosted Agents właśnie usunął większość tej infrastruktury dla użytkowników Microsoft Agent Framework (MAF).

## Co Naprawdę Robi Foundry Hosted Agents

Gdy wdrażasz agenta MAF do Foundry Hosted Agents, platforma obsługuje zaskakująco długą listę rzeczy, które w innym przypadku musiałbyś zbudować samodzielnie:

- **Skalowanie do zera** — agent nie kosztuje nic, gdy jest bezczynny i automatycznie wraca do działania
- **Izolowane sandbox'y VM na sesję** — każda sesja użytkownika dostaje własny sandbox z trwałością systemu plików, która przeżywa zdarzenia skalowania w dół
- **Wbudowane Entra ID** — każdy agent dostaje własną tożsamość, aby wywoływać modele Foundry, Toolbox i usługi Azure bez sekretów wbudowanych w obraz
- **Wersjonowane wdrożenia** — każde wdrożenie to niezmienny snapshot z obsługą blue/green i canary rollout
- **Obserwowalność bez konfiguracji** — `APPLICATIONINSIGHTS_CONNECTION_STRING` jest wstrzykiwane w czasie wykonywania, aby ślady OpenTelemetry MAF automatycznie trafiały do App Insights

Ten ostatni jest naprawdę wygodny. Bez dodatkowego okablowania, bez dodatkowej konfiguracji. Ślady po prostu się pojawiają.

## Różnica w Kodzie Jest Minimalna

To właśnie najbardziej cenię w tej integracji. Nie przepisujesz swojego agenta. Wystarczy go opakować:

**W .NET:**

```csharp
using Microsoft.Agents.AI.Foundry.Hosting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();

app.Run();
```

**W Python:**

```python
server = ResponsesHostServer(agent)
server.run()
```

To wszystko. Ta sama logika, którą testowałeś lokalnie, jest tym, co działa w produkcji. Platforma opakuje ją w infrastrukturę zarządzania sesjami, tożsamością i skalowaniem.

## Dwa Protokoły, Jeden Agent

Hosted Agents obsługują dwa style endpointów:

- **Responses** (`/responses`) — kompatybilny z OpenAI, zarządza historią konwersacji i streamingiem. Dobry domyślny wybór dla agentów w kształcie czatu.
- **Invocations** (`/invocations`) — definiujesz schemat żądania/odpowiedzi. Dobry do przepływów pracy bez konwersacji.

Jeśli budujesz coś, co wygląda jak rozmowa, zacznij od Responses. Jeśli budujesz agenta w kształcie API, który przyjmuje strukturyzowane dane wejściowe i zwraca strukturyzowane dane wyjściowe, Invocations daje ci elastyczność.

## Przepływ Wdrożenia z `azd`

Gdy uruchomisz `azd up` z agentem MAF:

1. Opcjonalnie tworzy projekt Foundry i wdraża model
2. Pakuje twój kod i przesuwa obraz do Azure Container Registry
3. Aprowizuje zasoby obliczeniowe z obrazu ACR
4. Przypisuje agentowi dedykowane Entra ID
5. Udostępnia stabilny endpoint (`https://{project_endpoint}/agents/{agent_name}`)
6. Obsługuje wszystko inne od tego momentu

Sesje trwają do 30 dni. Bezczynne zasoby obliczeniowe są deprowizowane po 15 minutach i transparentnie przywracane przy następnym żądaniu. Z perspektywy agenta nic się nie zmieniło.

## Podsumowanie

Odległość między "działa lokalnie" a "działa w produkcji" była historycznie długa i bolesna dla agentów AI. Foundry Hosted Agents + MAF znacznie zmniejsza tę lukę. Jeśli masz już lokalnego agenta zbudowanego z Agent Framework, warto spróbować już dziś.

Zespół mówi, że GA wkrótce nadejdzie — to jest obecnie w podglądzie. Sprawdź [dokumentację integracji MAF Hosted Agent](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) i [przykłady .NET](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents), aby zacząć.

Oryginalny artykuł: [From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)
