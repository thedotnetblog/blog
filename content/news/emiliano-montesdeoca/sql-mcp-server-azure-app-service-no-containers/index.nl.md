---
title: "SQL MCP Server op Azure App Service — Geen containers vereist"
date: 2026-05-05
author: "Emiliano Montesdeoca"
description: "SQL MCP Server kan nu draaien op Azure App Service zonder Docker of Kubernetes. Wat dit betekent voor .NET-ontwikkelaars die AI-agents bouwen die communiceren met SQL-databases."
tags:
  - Azure SQL
  - MCP
  - Azure App Service
  - Data API Builder
  - AI Agents
  - Azure
---

*Dit bericht is automatisch vertaald. Voor de originele versie, [klik hier]({{< ref "index.md" >}}).*

Eerlijk gezegd: elke keer dat ik "vereist een container" in een tutorial zie, ontsnapt er iets van een zucht. Containers zijn geweldig — totdat je team geen containerstrategie heeft, en een functie die simpel leek plotseling vastloopt op onverwachte orchestratiecomplexiteit die niemand had gepland.

Daarom trok dit mijn aandacht. SQL MCP Server kan nu draaien op Azure App Service — geen Docker, geen Kubernetes, alleen hetzelfde Data API Builder (DAB)-configuratiebestand dat je SQL-database blootstelt via MCP, REST en GraphQL.

## Wat is SQL MCP Server?

Een snelle introductie als je er nog niet bekend mee bent. SQL MCP Server zit tussen je AI-agent en SQL-database in. In plaats van de agent directe toegang tot de database te geven (een slecht idee), stelt het je tabellen en views bloot als een abstractielaag — entiteiten met gedefinieerde rechten.

Gebouwd op [Data API Builder](https://learn.microsoft.com/nl-nl/azure/data-api-builder/), wat betekent dat één configuratiebestand MCP *en* REST *en* GraphQL tegelijkertijd beheert. Je agent praat met het MCP-eindpunt. Je traditionele applicatie praat met REST of GraphQL. Dezelfde configuratie, dezelfde runtime, verschillende oppervlakken.

Dit is genuinelijk nuttig — je hoeft niet twee afzonderlijke API-lagen te onderhouden.

## Het containerprobleem (en de oplossing)

Het originele deploymentmodel van SQL MCP Server gebruikte containers. Dat werkt goed in veel teams — maar niet in allemaal. Veel .NET-teams standaardiseren op Azure App Service of VM's. Een containerruntime vereisen alleen om een SQL-eindpunt bloot te stellen, voegt wrijving toe waar niemand om vroeg.

De nieuwe walkthrough laat zien hoe je de container volledig kunt overslaan. Alles werkt via een `dab start`-commando, gehost op App Service als een standaard .NET 8-webproces.

```bash
# Installeer Data API Builder
dotnet tool install microsoft.dataapibuilder --prerelease -g

# Initialiseer de configuratie
dab init --database-type mssql --host-mode Development --connection-string "@env('SQL_CONNECTION_STRING')"

# Voeg een entiteit toe
dab add products --source dbo.products --permissions "authenticated:*"

# Configureer de App Service-authenticatieprovider
dab configure --runtime.host.authentication.provider AppService

# Start de server
dab start
```

Op dit punt heb je MCP op `/mcp`, REST en GraphQL vanuit hetzelfde proces — en niets dat in een container draait.

## Authenticatie zonder gedeelde API-sleutels

Dit is het deel dat ik het meest waardeer. Bij deployment naar App Service configureer je Microsoft Entra ID als authenticatieprovider. Geen gedeelde secrets in configuratiebestanden, geen API-sleutels om te roteren.

De verbindingsreeks blijft in App Service-omgevingsvariabelen (niet in `dab-config.json`), en het MCP-eindpunt is beveiligd door platformauthenticatie. Als je Azure-workloads al zijn afgestemd op Entra ID, past dit er natuurlijk in.

Voor lokale ontwikkeling schakel je over naar de `Simulator`-modus en STDIO-transport. Schakel terug naar de `AppService`-modus voor deployment. Schoon en expliciet.

## Deployment naar App Service

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

Deploy vervolgens je DAB-project met de codedeploymentmethode die je team al gebruikt. Het cruciale detail: dit is een **code**-deployment, geen containerdeployment.

## Waarom dit belangrijk is voor .NET-ontwikkelaars

Als je AI-agents bouwt in .NET, zal je agent vroeg of laat moeten communiceren met een database. SQL MCP Server geeft je een gestructureerde manier om dit te doen — zonder ruwe verbindingsreeksen bloot te stellen.

Bekijk de volledige walkthrough in de [originele blogpost](https://devblogs.microsoft.com/azure-sql/sql-mcp-server-app-service/) en het [GitHub-voorbeeldrepository](https://github.com/Azure-Samples/SQL-MCP-NoContainer).

## Conclusie

SQL MCP Server op App Service is een pragmatische keuze voor .NET-teams die hun agents gestructureerde SQL-datatoegang willen geven zonder een containerstrategie. Probeer het — je agents zullen het schone API-oppervlak waarderen.
