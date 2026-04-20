---
title: "Aspire 13.2 Brengt een Docs CLI — en je AI-Agent Kan die Ook Gebruiken"
date: 2026-04-04
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 voegt aspire docs toe — een CLI voor het zoeken, doorbladeren en lezen van officiële documentatie zonder je terminal te verlaten. Werkt ook als tool voor AI-agents."
tags:
  - aspire
  - dotnet
  - cli
  - ai
  - developer-tools
  - documentation
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "aspire-docs-cli-ai-skills" >}}).*

Ken je dat moment waarop je diep in een Aspire AppHost zit, integraties bekabelt, en je precies moet controleren welke parameters de Redis-integratie verwacht? Je alt-tabbt naar je browser, zoekt op aspire.dev. Context verloren.

Aspire 13.2 heeft [een oplossing daarvoor gepubliceerd](https://devblogs.microsoft.com/aspire/aspire-docs-in-your-terminal/). De `aspire docs` CLI laat je zoeken in officiële Aspire-documentatie, er doorheen bladeren en het lezen, direct vanuit je terminal.

## Drie opdrachten, nul browsertabbladen

```bash
# Lijst alle docs
aspire docs list

# Zoek een onderwerp
aspire docs search "redis"

# Lees een volledige pagina
aspire docs get redis-integration

# Slechts één sectie
aspire docs get redis-integration --section "Add Redis resource"
```

## De AI-agent invalshoek

Dezelfde `aspire docs`-opdrachten werken als tools voor AI-agents. In plaats van Aspire API's te verzinnen op basis van verouderde trainingsdata, kan de agent `aspire docs search "postgres"` aanroepen en de officiële integratiedocumentatie lezen.

## Samenvatting

`aspire docs` is een kleine functie die een echt probleem netjes oplost. Bekijk [David Pine's diepgaande analyse](https://davidpine.dev/posts/aspire-docs-mcp-tools/).
