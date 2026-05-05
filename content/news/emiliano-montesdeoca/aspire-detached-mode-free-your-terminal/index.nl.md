---
title: "Stop met het Bewaken van je Terminal: Aspire's Losstaande Modus Verandert de Workflow"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Aspire 13.2 laat je AppHost op de achtergrond uitvoeren en je terminal terugkrijgen. Gecombineerd met nieuwe CLI-opdrachten en agentondersteuning is dit een grotere deal dan het klinkt."
tags:
  - aspire
  - dotnet
  - cli
  - developer-tools
  - coding-agents
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "aspire-detached-mode-free-your-terminal" >}}).*

Elke keer dat je een Aspire AppHost uitvoert, is je terminal weg. Vergrendeld. Bezet totdat je Ctrl+C uitvoert. Wil je een snel commando uitvoeren? Open een nieuw tabblad. Logs controleren? Nog een tabblad. Deze kleine wrijving telt snel op.

Aspire 13.2 lost dit op. James Newton-King [heeft alle details opgeschreven](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/), en eerlijk gezegd is dit een van die functies die onmiddellijk veranderen hoe je werkt.

## Losstaande modus: één commando, terminal terug

```bash
aspire start
```

Dit is de afkorting voor `aspire run --detach`. Je AppHost start op de achtergrond en je krijgt je terminal onmiddellijk terug.

## Beheren wat er draait

Op de achtergrond draaien is alleen nuttig als je daadwerkelijk kunt beheren wat er draait. Aspire 13.2 levert een volledige set CLI-opdrachten:

```bash
# Lijst alle draaiende AppHosts
aspire ps

# Inspecteer de status van een specifieke AppHost
aspire describe

# Stream logs van een draaiende AppHost
aspire logs

# Stop een specifieke AppHost
aspire stop
```

## Combineer het met de geïsoleerde modus

De losstaande modus combineert natuurlijk met de geïsoleerde modus:

```bash
aspire start --isolated
aspire start --isolated
```

Elke instantie krijgt willekeurige poorten, afzonderlijke geheimen en zijn eigen levenscyclus.

## Waarom dit groot is voor coding agents

Een coding agent die in je terminal werkt, kan nu:

1. De app starten met `aspire start`
2. De status opvragen met `aspire describe`
3. Logs controleren met `aspire logs` om problemen te diagnosticeren
4. Stoppen met `aspire stop` als klaar

`aspire agent init` uitvoeren stelt een Aspire-vaardigheidsbestand in dat agents deze opdrachten leert.

## Samenvatting

De losstaande modus is een workflow-upgrade vermomd als een eenvoudige vlag. Lees de [volledige post](https://devblogs.microsoft.com/aspire/aspire-detached-mode-and-process-management/) en haal Aspire 13.2 met `aspire update --self`.
