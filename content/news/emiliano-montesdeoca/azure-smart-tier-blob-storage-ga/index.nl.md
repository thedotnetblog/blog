---
title: "Azure Smart Tier is GA — Automatische Blob Storage Kostenoptimalisatie Zonder Levenscyclusregels"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "Azure Blob Storage smart tier is nu algemeen beschikbaar en verplaatst objecten automatisch tussen hot-, cool- en cold-lagen op basis van werkelijke toegangspatronen."
tags:
  - azure
  - storage
  - blob-storage
  - cost-optimization
  - cloud-native
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "azure-smart-tier-blob-storage-ga" >}}).*

Als je ooit tijd hebt besteed aan het afstemmen van Azure Blob Storage-levenscyclusbeleid en dit zag instorten wanneer toegangspatronen veranderden, is dit voor jou. Microsoft heeft zojuist de [algemene beschikbaarheid van smart tier](https://azure.microsoft.com/en-us/blog/optimize-object-storage-costs-automatically-with-smart-tier-now-generally-available/) voor Azure Blob en Data Lake Storage aangekondigd.

## Wat smart tier eigenlijk doet

Smart tier evalueert continu de tijd van laatste toegang van elk object in je opslagaccount. Frequent geraadpleegde gegevens blijven in hot, inactieve gegevens worden na 30 dagen naar cool verplaatst, daarna na nog eens 60 dagen naar cold. Wanneer gegevens opnieuw worden geopend, worden ze direct terug gepromoveerd naar hot.

Geen levenscyclusregels om te configureren. Geen handmatige afstemming.

Tijdens de preview meldde Microsoft dat **meer dan 50% van de door smart tier beheerde capaciteit automatisch naar koelere lagen is verschoven**.

## Waarom dit belangrijk is voor .NET-ontwikkelaars

Praktische scenario's:
- **Applicatietelemetrie en logboeken** — hot bij foutopsporing, zelden geopend na een paar weken
- **Datapijplijnen en ETL-uitvoer** — intensief benaderd tijdens verwerking, daarna meestal cold
- **Door gebruikers gegenereerde content** — recente uploads zijn hot, oudere content koelt geleidelijk af

## De afweging

De tieringregels van smart tier zijn statisch (30 dagen → cool, 90 dagen → cold). Als je aangepaste drempels nodig hebt, zijn levenscyclusregels nog steeds de weg te gaan.
