---
title: "Azure Developer CLI wordt steeds meer een betere inner-looptool"
date: 2026-06-28
author: "Emiliano Montesdeoca"
description: "De releases van mei en juni 2026 voor Azure Developer CLI voegen veel toe, maar de grootste waarde zit in hoe ze de dagelijkse loop verbeteren: beter toolbeheer, veiligere provisioning, sterkere extensieondersteuning en praktischere uitvoeringsworkflows."
tags:
  - Azure Developer CLI
  - azd
  - Azure
  - Developer Tools
  - .NET
---

*Dit artikel is automatisch vertaald. Voor de oorspronkelijke versie, [klik hier]({{< ref "index.md" >}}).*

Grote CLI-overzichten kunnen vermoeiend zijn om te lezen omdat ze grote workflowverbeteringen en kleine fixes samen proppen in één tekstmuur.

Dus hier is mijn korte versie: de recente **Azure Developer CLI**-updates zijn belangrijk omdat `azd` steeds meer een **betere inner-looptool** wordt, niet alleen een deployment-wrapper.

Dat is de belangrijkste verschuiving.

## Toolbeheer wordt onderdeel van het product, niet van een zijtaak

Een van mijn favoriete toevoegingen zijn de nieuwe `azd tool`-commando's.

Alles wat setup-frictie vermindert, is het waard om op te letten, vooral in projecten waar een werkende omgeving afhangt van een mix van SDK's, CLI's, Docker, Bicep en extensies.

Als de tool nu kan helpen om die afhankelijkheden direct te ontdekken, installeren, controleren en updaten, dan haalt dat veel van de vervelende foutmodi weg die nieuwkomers vaak als eerste treffen.

Dat is echte waarde.

## `azd exec` lijkt ook belangrijker dan het klinkt

Op het eerste gezicht kan `azd exec` op een kleine gemaksfunctie lijken.

Ik vind van niet.

Commando's uitvoeren met de volledige `azd`-omgevingcontext, inclusief secret-oplossing, is precies het soort mogelijkheid dat lokale automatisering en scripting veel schoner maakt.

Dat vermindert de behoefte aan extra glue-scripts en helpt uitvoering consistent te houden tussen omgevingen.

Dat is een praktische winst.

## Veiliger provisioning en beter annuleringsgedrag zijn onderschatte verbeteringen

De release bevat ook wijzigingen rond provisioning-afhankelijkheden, afhandeling van annulering en deployment-gedrag, dingen die misschien niet glamoureus lijken maar zeer welkom zijn.

Interactieve annuleringsprompts, betere afhankelijkheidsmodellering en een duidelijkere deploymentstatus zijn precies het soort verbeteringen die een CLI betrouwbaar laten aanvoelen wanneer je met echte Azure-resources werkt.

En vertrouwen is bij dit soort tools een groot punt.

## Mijn indruk

Hoe meer `azd` verbetert in setup, scripting, deploymentveiligheid en extensieondersteuning, hoe meer het aanvoelt als iets dat je in je dagelijkse loop kunt houden in plaats van alleen vlak voor een deployment aan te raken.

Dat is de juiste richting.

Voor teams die cloud-native of AI-gedreven apps op Azure bouwen, maakt dit de CLI nuttiger op de plek waar het het meest telt: tijdens de echte ontwikkeling.

Originele post: [Azure Developer CLI (azd) – May and June 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/)