---
title: "De Moderniseringsbeoordelingstool van GitHub Copilot Is het Beste Migratiehulpmiddel Dat Je Nog Niet Gebruikt"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "De moderniseringsextensie van GitHub Copilot stelt niet alleen codewijzigingen voor — het produceert een volledige migratiebeoordeling met uitvoerbare problemen, Azure-doelvergelijkingen en een collaboratieve workflow."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "dotnet-modernization-assessment-github-copilot" >}}).*

Het migreren van een legacy .NET Framework-app naar modern .NET is een van die taken die iedereen weet dat ze moeten doen maar niemand wil beginnen.

Jeffrey Fritz heeft zojuist een [diepgaande analyse van de moderniseringsbeoordelingstool van GitHub Copilot](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) gepubliceerd.

## Het is niet alleen een code-suggestie-engine

De VS Code-extensie volgt een **Beoordeel → Plan → Uitvoer**-model. De beoordelingsfase analyseert je volledige codebase en produceert een gestructureerd document dat alles vastlegt.

De beoordeling wordt opgeslagen onder `.github/modernize/assessment/`. Elke run produceert een onafhankelijk rapport.

## Twee manieren om te starten

**Aanbevolen beoordeling** — het snelle pad. Kies uit gecureerde domeinen (Java/.NET Upgrade, Cloud Readiness, Security).

**Aangepaste beoordeling** — het gerichte pad. Configureer exact wat te analyseren: doelcomputing (App Service, AKS, Container Apps), doelbesturingssysteem, containerisatieanalyse.

## De probleemindeling is uitvoerbaar

Elk probleem heeft een kriticiteitsniveau:

- **Verplicht** — moet worden opgelost of migratie mislukt
- **Potentieel** — kan migratie beïnvloeden, vereist menselijk oordeel
- **Optioneel** — aanbevolen verbeteringen, blokkeert migratie niet

## Mijn mening

Als je legacy .NET Framework-apps hebt, is dit *het* hulpmiddel om mee te beginnen.

Lees de [volledige walkthrough](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) en download de [VS Code-extensie](https://aka.ms/ghcp-appmod/vscode-ext).
