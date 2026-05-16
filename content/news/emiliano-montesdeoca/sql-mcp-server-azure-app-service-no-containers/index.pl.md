---
title: "SQL MCP Server na Azure App Service — bez kontenerów"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "SQL MCP Server może teraz działać na Azure App Service bez Dockera ani Kubernetes. Co to oznacza dla deweloperów .NET budujących agentów AI komunikujących się z bazami SQL."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*Ten post został przetłumaczony automatycznie. Aby zobaczyć oryginalną wersję, [kliknij tutaj]({{< ref "index.md" >}}).*

Szczerze mówiąc: za każdym razem, gdy w tutorialu widzę „wymaga kontenera", coś we mnie wzdycha. Kontenery są świetne — dopóki twój zespół nie ma strategii kontenerowej, a funkcja, która wydawała się prosta, nagle blokuje się na nieoczekiwanej złożoności orkiestracji, której nikt nie zaplanował.

Dlatego to przykuło moją uwagę. SQL MCP Server może teraz działać na Azure App Service — bez Dockera, bez Kubernetes, tylko z tym samym plikiem konfiguracyjnym Data API Builder (DAB), który eksponuje twoją bazę danych SQL przez MCP, REST i GraphQL.

## Czym jest SQL MCP Server?

Krótkie wprowadzenie, jeśli jeszcze nie kojarzysz. SQL MCP Server siedzi pomiędzy twoim agentem AI a bazą danych SQL. Zamiast dawać agentowi bezpośredni dostęp do bazy (kiepski pomysł), eksponuje twoje tabele i widoki jako warstwę abstrakcji — encje z zdefiniowanymi uprawnieniami.

Zbudowany na [Data API Builder](https://learn.microsoft.com/pl-pl/azure/data-api-builder/), co oznacza, że jeden plik konfiguracyjny zarządza MCP *i* REST *i* GraphQL jednocześnie. Agent komunikuje się z endpointem MCP. Tradycyjna aplikacja komunikuje się z REST lub GraphQL. Ta sama konfiguracja, to samo środowisko uruchomieniowe, różne powierzchnie.

To naprawdę przydatne — nie musisz utrzymywać dwóch oddzielnych warstw API.

## Problem z kontenerami (i rozwiązanie)

Pierwotny model wdrożenia SQL MCP Server używał kontenerów. Działa dobrze w wielu zespołach — ale nie we wszystkich. Wiele zespołów .NET standardyzuje na Azure App Service lub maszynach wirtualnych. Wymaganie środowiska uruchomieniowego kontenerów tylko po to, żeby wyeksponować endpoint SQL, dodaje tarcia, o które nikt nie prosił.

Nowy przewodnik pokazuje, jak całkowicie pominąć kontener. Wszystko działa przez polecenie `dab start`, hostowane na App Service jako standardowy proces webowy .NET 8.

```bash
# Zainstaluj Data API Builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Zainicjuj konfigurację
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Dodaj encję
dab add products --source dbo.products --permissions "authenticated:*"

# Skonfiguruj dostawcę uwierzytelniania App Service
dab configure --runtime.host.authentication.provider AppService

# Uruchom serwer
dab start
```

W tym momencie masz MCP pod `/mcp`, REST i GraphQL z tego samego procesu — i nic nie działa w kontenerze.

## Uwierzytelnianie bez wspólnych kluczy API

To jest ta część, którą cenię najbardziej. Wdrażając na App Service, konfigurujesz Microsoft Entra ID jako dostawcę uwierzytelniania. Żadnych wspólnych sekretów w plikach konfiguracyjnych, żadnych kluczy API do rotacji.

Ciąg połączenia pozostaje w zmiennych środowiskowych App Service (nie w `dab-config.json`), a endpoint MCP jest chroniony uwierzytelnianiem platformy. Jeśli twoje obciążenia Azure są już zintegrowane z Entra ID, to naturalnie pasuje.

Do lokalnego developmentu przełącz się na tryb `Simulator` i transport STDIO. Wróć do trybu `AppService` przed wdrożeniem. Czysto i jednoznacznie.

## Wdrożenie na App Service

```bash
az appservice plan create \
  --name <plan-name> \
  --resource-group <resource-group> \
  --sku B1 \
  --is-linux

az webapp create \
  --name <app-name> \
  --resource-group <resource-group> \
  --plan <plan-name> \
  --runtime "DOTNETCORE:8.0"

az webapp config set \
  --name <app-name> \
  --resource-group <resource-group> \
  --startup-file "dab start"
```

Następnie wdróż swój projekt DAB metodą wdrożenia kodu, której twój zespół już używa. Kluczowy szczegół: to wdrożenie **kodu**, nie kontenera.

## Dlaczego to ważne dla deweloperów .NET

Jeśli budujesz agentów AI w .NET, prędzej czy później agent będzie musiał komunikować się z bazą danych. SQL MCP Server daje ci ustrukturyzowany sposób, żeby to zrobić — bez eksponowania surowych ciągów połączenia.

Sprawdź pełny przewodnik w [oryginalnym poście](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) i [przykładowym repozytorium na GitHub](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## Podsumowanie

SQL MCP Server na App Service to praktyczny wybór dla zespołów .NET, które chcą dać agentom ustrukturyzowany dostęp do danych SQL bez strategii kontenerowej. Wypróbuj — twoi agenci docenią czysty interfejs API.
