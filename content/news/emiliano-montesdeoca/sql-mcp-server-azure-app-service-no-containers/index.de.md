---
title: "SQL MCP Server auf Azure App Service — Ohne Container"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "Der SQL MCP Server läuft jetzt auf Azure App Service ohne Docker oder Kubernetes. Was das für .NET-Entwickler bedeutet, die KI-Agenten mit SQL-Datenbanken verbinden."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*Dieser Beitrag wurde automatisch übersetzt. Die Originalversion findest du [hier]({{< ref "index.md" >}}).*

Ehrlich gesagt: Jedes Mal, wenn ich "erfordert einen Container" in einem Tutorial lese, seufze ich innerlich. Container sind großartig — bis dein Team keine Container-Strategie hat und eine scheinbar einfache Funktion hinter Orchestrierungsaufwand steckt, den niemand eingeplant hatte.

Deshalb hat mich das hier aufhorchen lassen. Der SQL MCP Server läuft jetzt auf Azure App Service — ohne Docker, ohne Kubernetes, nur mit derselben Data API Builder (DAB)-Konfiguration, die deine SQL-Datenbank über MCP, REST und GraphQL bereitstellt.

## Was ist der SQL MCP Server?

Kurzer Kontext, falls du ihn noch nicht kennst. Der SQL MCP Server sitzt zwischen deinem KI-Agenten und deiner SQL-Datenbank. Statt dem Agenten direkten Datenbankzugriff zu geben (was eine schreckliche Idee wäre), stellt er Tabellen und Views als Abstraktionsschicht bereit — Entitäten mit definierten Berechtigungen.

Er basiert auf [Data API Builder](https://learn.microsoft.com/de-de/azure/data-api-builder/), was bedeutet, dass eine einzige Konfigurationsdatei MCP *und* REST *und* GraphQL gleichzeitig bereitstellt. Dein Agent spricht mit dem MCP-Endpoint. Deine klassische Anwendung spricht mit REST oder GraphQL. Gleiche Config, gleiche Runtime, unterschiedliche Oberflächen.

Das ist wirklich nützlich. Du pflegst nicht zwei separate API-Schichten.

## Das Container-Problem (und die Lösung)

Das ursprüngliche Bereitstellungsmodell für den SQL MCP Server waren Container. Das funktioniert in vielen Teams gut — aber nicht in allen. Viele .NET-Teams standardisieren auf Azure App Service oder VMs. Einen Container-Runtime nur für einen SQL-Endpoint zu benötigen, fügt Reibung hinzu, die niemand angefordert hat.

Das neue Walkthrough zeigt, wie man den Container komplett überspringt. Alles läuft mit einem `dab start`-Befehl, gehostet auf App Service als standardmäßiger .NET 8-Webprozess.

```bash
# Data API Builder installieren
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Konfiguration initialisieren
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Eine Entität hinzufügen
dab add products --source dbo.products --permissions "authenticated:*"

# App Service Auth-Provider konfigurieren
dab configure --runtime.host.authentication.provider AppService

# Server starten
dab start
```

Jetzt hast du MCP unter `/mcp`, REST und GraphQL aus demselben Prozess, und nichts läuft in einem Container.

## Authentifizierung ohne geteilte API-Schlüssel

Das ist der Teil, den ich am meisten schätze. Bei der Bereitstellung auf App Service konfigurierst du Microsoft Entra ID als Authentifizierungsanbieter. Keine geteilten Geheimnisse in Konfigurationsdateien, keine API-Schlüssel, die rotiert werden müssen.

Der Connection String bleibt in einer App Service-Umgebungsvariable (nicht in `dab-config.json`), und der MCP-Endpoint ist durch Plattform-Authentifizierung geschützt. Wenn du bereits auf Entra ID in deinen Azure-Workloads ausgerichtet bist, fügt sich das natürlich ein.

Für die lokale Entwicklung wechselst du in den `Simulator`-Modus und STDIO-Transport. Vor dem Deployment wechselst du zurück in den `AppService`-Modus. Klar und explizit.

## Bereitstellung auf App Service

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

Dann deployst du dein DAB-Projekt über deinen bevorzugten Code-Deployment-Weg. Das Entscheidende: Es ist ein **Code**-Deployment, kein Container-Deployment.

## Warum das für .NET-Entwickler wichtig ist

Wenn du KI-Agenten in .NET baust, wird dein Agent irgendwann mit einer Datenbank kommunizieren müssen. Der SQL MCP Server bietet eine strukturierte Möglichkeit, das zu tun, ohne rohe Connection Strings preiszugeben.

Das vollständige Walkthrough findest du im [Originalbeitrag](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) und im [Beispiel-Repository auf GitHub](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## Fazit

Der SQL MCP Server auf App Service ist eine solide pragmatische Option für .NET-Teams, die ihren Agenten strukturierten SQL-Datenzugriff geben möchten, ohne eine Container-Strategie zu benötigen. Probier es aus — deine Agenten werden die saubere API-Oberfläche zu schätzen wissen.
