---
title: "De Maart-update van Visual Studio Laat Je Eigen Copilot-agenten Bouwen — en de find_symbol Tool Is een Grote Stap"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "De maart 2026-update van Visual Studio brengt aangepaste Copilot-agenten, herbruikbare agentvaardigheden, een taalvriendelijke find_symbol-tool en Copilot-ondersteunde profilering vanuit Test Explorer. Dit is wat er toe doet."
tags:
  - visual-studio
  - github-copilot
  - dotnet
  - ai
  - developer-tools
  - profiling
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "visual-studio-march-2026-custom-copilot-agents" >}}).*

Visual Studio heeft zojuist zijn meest significante Copilot-update tot nu toe ontvangen. Mark Downie [kondigde de maartrelease aan](https://devblogs.microsoft.com/visualstudio/visual-studio-march-update-build-your-own-custom-agents/), en de kop is aangepaste agenten — maar eerlijk gezegd, de `find_symbol`-tool die verder verborgen zit, is mogelijk de functie die je workflow het meest verandert.

Laat me uitleggen wat er echt is.

## Aangepaste Copilot-agenten in je repository

Wil je dat Copilot de codestandaarden van je team volgt, je build-pipeline uitvoert of je interne documentatie raadpleegt? Nu kun je precies dat bouwen.

Aangepaste agenten worden gedefinieerd als `.agent.md`-bestanden die je in `.github/agents/` in je repository plaatst. Elke agent heeft volledige toegang tot werkruimtebewustzijn, codebegrip, tools, je voorkeursmodel en MCP-verbindingen met externe services.

Dit is hetzelfde patroon dat VS Code heeft ondersteund — en het is geweldig om te zien dat Visual Studio bijhoudt.

## Agentvaardigheden: herbruikbare instructiepakketten

Vaardigheden worden automatisch opgehaald uit `.github/skills/` in je repository of `~/.copilot/skills/` in je profiel.

## find_symbol: taalbewuste navigatie voor agenten

Dit is waar het echt interessant wordt. De nieuwe `find_symbol`-tool geeft de agentmodus van Copilot echte, door de taalservice aangedreven symboolnavigatie. In plaats van code als tekst te doorzoeken, kan de agent:

- Alle verwijzingen naar een symbool door je project vinden
- Toegang krijgen tot type-informatie, declaraties en bereikmetadata
- Aanroeplocaties navigeren met volledige taalbewustzijn

Wat dit in de praktijk betekent: als je Copilot vraagt een methode te refactoren of een parameterhandtekening bij alle aanroeplocaties bij te werken, kan het de structuur van je code echt zien.

## Tests profileren met Copilot

Er is nu een **Profile with Copilot**-opdracht in het contextmenu van Test Explorer. Selecteer een test, klik op profileren, en de Profiling Agent voert hem automatisch uit en analyseert de prestaties.

## Afsluiting

Aangepaste agenten en vaardigheden zijn de kop, maar `find_symbol` is de stille hit — het verandert fundamenteel hoe nauwkeurig Copilot kan zijn bij het refactoren van .NET-code. Download [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/downloads/) om alles uit te proberen.
