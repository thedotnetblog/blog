---
title: '.NET 8 en .NET 9 end of support: behandel dit als een leveringsdeadline'
date: 2026-07-19
author: 'Emiliano Montesdeoca'
description: '10 november 2026 is niet zomaar een supportdatum; het is het punt waarop uitgesteld upgraderisico expliciet wordt.'
tags:
  - dotnet
  - net10
  - security
  - platform-lifecycle
  - engineering-leadership
---

Oorspronkelijke bron: [.NET 8 and .NET 9 will reach End of Support on November 10, 2026](https://devblogs.microsoft.com/dotnet/dotnet-8-9-end-of-support/)

Deze aankondiging is eenvoudig, en teams zouden met even veel duidelijkheid moeten reageren: als je van plan bent om na 10 november 2026 te blijven leveren op .NET 8 of .NET 9, neem je bewust een besluit voor een niet-ondersteunde runtime.

Applicaties blijven draaien. Dat is niet het punt. Het punt is dat beveiligings- en onderhoudsupdates stoppen. Zodra dat gebeurt, wordt elke bekende kwetsbaarheid zonder backportpad jouw operationele aansprakelijkheid.

Mijn eigenzinnige mening: organisaties behandelen frameworkupgrades vaak als optioneel onderhoud en betalen vervolgens voor die beslissing in noodvensters, auditbevindingen en overhaaste leveranciersescalaties. Upgradeplanning zou een roadmap-item van het product moeten zijn, geen bijtaak.

Een praktische migratiehouding voor .NET-teams:

Stel het retargeten naar .NET 10 in als een gedateerd doel, niet als een open backlogitem.

Voer compatibiliteits- en regressietests nu parallel uit met featurewerk, niet in Q4.

Volg de gereedheid van afhankelijkheden en hosting als aparte werkstromen, want veel fouten gebeuren buiten het projectbestand.

Gebruik Upgrade Assistant en documentatie over breaking changes vroeg om verrassingen naar voren te halen.

Als je gedeelde bibliotheken beheert die door meerdere producten worden gebruikt, publiceer je .NET 10-supporttijdlijn dan publiekelijk binnen je organisatie. Downstream-teams hebben doorlooptijd nodig.

De markering van Visual Studio voor niet-ondersteunde componenten is operationeel ook belangrijk. Het creëert een duidelijk signaal dat toolchain-opruiming onderdeel is van compliant blijven. Teams die dit negeren, glijden meestal af naar gemengde SDK-statussen en inconsistent buildgedrag.

Eén onderbelicht detail is dat .NET 8 en .NET 9 samenkomen op dezelfde einddatum. Dat comprimeert upgradevensters voor organisaties die adoptie gefaseerd hadden, in de verwachting van meer speling. Als je naar .NET 9 bent overgestapt voor featuretoegang, land je nog steeds op dezelfde supportklif.

Voor platformleads is de beslismatrix simpel: migreer voor de deadline, of documenteer en accepteer niet-ondersteund risico met compenserende controles. Er is geen derde optie waarbij niets verandert.

Het goede nieuws is dat .NET 10 een LTS-doel is tot november 2028, wat stabiele ruimte oplevert zodra je de verhuizing voltooit.

Wacht niet tot de laatste Patch Tuesday om te beginnen. Behandel dit als een leveringsdeadline met beveiligingsimplicaties, want dat is precies wat het is.
