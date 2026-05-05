---
title: "azd + GitHub Copilot: AI-gedreven projectopzet en slimme foutoplossing"
date: 2026-04-21
author: "Emiliano Montesdeoca"
description: "De Azure Developer CLI integreert nu met GitHub Copilot om projectinfrastructuur te genereren en deployment-fouten op te lossen — zonder de terminal te verlaten."
tags:
  - Azure
  - azd
  - GitHub Copilot
  - Azure Developer CLI
  - Bicep
  - Infrastructure as Code
  - Developer Tooling
---

> *Dit artikel is automatisch vertaald. Voor de originele Engelse versie, [klik hier]({{< ref "index.md" >}}).*

Ken je dat moment waarop je een bestaande app naar Azure wilt deployen en je naar een lege `azure.yaml` staart, terwijl je probeert te herinneren of je Express API Container Apps of App Service moet gebruiken? Dat moment is zojuist een stuk korter geworden.

De Azure Developer CLI (`azd`) integreert nu met GitHub Copilot op twee concrete manieren: AI-ondersteunde projectscaffolding tijdens `azd init`, en intelligente foutoplossing wanneer deployments mislukken. Beide functies blijven volledig in de terminal.

## Setup met Copilot tijdens azd init

Wanneer je `azd init` uitvoert, is er nu een optie "Set up with GitHub Copilot (Preview)". Selecteer die en Copilot analyseert je codebase om de `azure.yaml`, infrastructuursjablonen en Bicep-modules te genereren — gebaseerd op je echte code.

```
azd init
# Selecteer: "Set up with GitHub Copilot (Preview)"
```

Vereisten:

- **azd 1.23.11 of nieuwer** — controleer met `azd version` of update met `azd update`
- **Actief GitHub Copilot-abonnement** (Individual, Business of Enterprise)
- **GitHub CLI (`gh`)** — `azd` vraagt om login als dat nodig is

Wat ik echt nuttig vind: het werkt in beide richtingen. Bouw je van de grond af? Copilot helpt je de juiste Azure-services vanaf het begin te configureren. Heb je een bestaande app die je wilt deployen? Wijs Copilot daarop en het genereert de configuratie zonder dat je iets hoeft te herstructureren.

### Wat het eigenlijk doet

Stel je hebt een Node.js Express API met een PostgreSQL-afhankelijkheid. In plaats van handmatig te kiezen tussen Container Apps en App Service en dan Bicep van de grond af te schrijven, detecteert Copilot je stack en genereert:

- Een `azure.yaml` met de juiste `language`-, `host`- en `build`-instellingen
- Een Bicep-module voor Azure Container Apps
- Een Bicep-module voor Azure Database for PostgreSQL

En het voert voorafgaande controles uit voor wijzigingen — verifieert dat je git-werkdirectory schoon is, vraagt van tevoren toestemming voor MCP-servertools. Niets gebeurt zonder dat je precies weet wat er gaat veranderen.

## Foutoplossing met Copilot

Deployment-fouten zijn onvermijdelijk. Ontbrekende parameters, toestemmingsproblemen, SKU-beschikbaarheid — en het foutbericht vertelt je zelden het enige dat je echt moet weten: *hoe je het oplost*.

Zonder Copilot ziet de lus er zo uit: kopieer de fout → zoek in docs → lees drie irrelevante Stack Overflow-antwoorden → voer wat `az` CLI-opdrachten uit → probeer opnieuw en hoop. Met Copilot geïntegreerd in `azd` stort deze lus in. Wanneer een `azd`-opdracht mislukt, biedt het onmiddellijk vier opties:

- **Explain** — uitleg in begrijpelijke taal van wat er mis ging
- **Guidance** — stapsgewijze instructies om het probleem op te lossen
- **Diagnose and Guide** — volledige analyse + Copilot past de oplossing toe (met jouw goedkeuring) + optioneel opnieuw proberen
- **Skip** — zelf afhandelen

Het cruciale punt: Copilot heeft al context over je project, de mislukte opdracht en de foutdetails. Zijn suggesties zijn specifiek voor *jouw situatie*.

### Een standaardgedrag instellen

Als je altijd dezelfde optie kiest, sla de interactieve prompt over:

```
azd config set copilot.errorHandling.category troubleshoot
```

Waarden: `explain`, `guidance`, `troubleshoot`, `fix`, `skip`. Je kunt ook automatisch herstellen en opnieuw proberen inschakelen:

```
azd config set copilot.errorHandling.fix allow
```

Op elk moment terug naar de interactieve modus:

```
azd config unset copilot.errorHandling.category
```

## Samenvatting

Voer `azd update` uit voor de nieuwste versie en probeer `azd init` op je volgende project.

Lees de [originele aankondiging hier](https://devblogs.microsoft.com/azure-sdk/azd-copilot-integration/).
