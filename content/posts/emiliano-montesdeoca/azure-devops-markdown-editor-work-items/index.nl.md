---
title: "Azure DevOps Lost Eindelijk de Markdown Editor UX op Waar Iedereen Over Klaagde"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "De Markdown-editor van Azure DevOps voor werkitems krijgt een duidelijker onderscheid tussen voorbeeld- en bewerkmodus. Het is een kleine verandering die een echte workflow-irritatie oplost."
tags:
  - azure-devops
  - devops
  - productivity
  - developer-tools
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "azure-devops-markdown-editor-work-items" >}}).*

Als je Azure Boards gebruikt, heb je dit waarschijnlijk meegemaakt: je leest door een werkitembeschrijving, misschien acceptatiecriteria bekijkend, en dan klik je per ongeluk dubbel. Boem — je bent in de bewerkingsmodus. Je wilde helemaal niets bewerken. Je was gewoon aan het lezen.

Dan Hellem [kondigde de fix aan](https://devblogs.microsoft.com/devops/improving-the-markdown-editor-for-work-items/), en het is een van die veranderingen die klein klinkt maar echt wrijving verwijdert uit je dagelijkse workflow.

## Wat er veranderd is

De Markdown-editor voor tekstuele werkitemvelden opent nu standaard in **voorbeeldmodus**. Je kunt inhoud lezen en ermee interageren — links volgen, opmaak bekijken — zonder je zorgen te maken dat je per ongeluk in de bewerkingsmodus terechtkomt.

Wanneer je daadwerkelijk wilt bewerken, klik je op het bewerkingspictogram bovenaan het veld. Wanneer je klaar bent, ga je expliciet terug naar de voorbeeldmodus.

## Waarom het meer uitmaakt dan het klinkt

De [community-feedbackthread](https://developercommunity.visualstudio.com/t/Markdown-editor-for-work-item-multi-line/10935496) hierover was lang. Het dubbelklik-om-te-bewerken-gedrag werd geïntroduceerd met de Markdown-editor in juli 2025, en de klachten begonnen bijna onmiddellijk.

## Uitrolstatus

Dit wordt al uitgerold naar een subset van klanten en breidt zich de komende twee tot drie weken uit naar iedereen.
