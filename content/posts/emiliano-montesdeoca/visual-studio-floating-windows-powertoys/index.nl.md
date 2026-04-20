---
title: "Die Visual Studio Zwevende Vensters Instelling die Je Niet Kende (Maar Zou Moeten Kennen)"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Een verborgen Visual Studio-instelling geeft je volledige controle over zwevende vensters — onafhankelijke taakbalkitems, correct gedrag op meerdere monitoren en perfecte FancyZones-integratie. Één dropdown verandert alles."
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

> *Dit bericht is automatisch vertaald. Voor het origineel, [klik hier]({{< ref "visual-studio-floating-windows-powertoys" >}}).*

Als je meerdere monitoren gebruikt met Visual Studio (en eerlijk gezegd, wie doet dat tegenwoordig niet), heb je waarschijnlijk de ergernis ervaren: zwevende toolvensters verdwijnen als je de hoofd-IDE minimaliseert, ze blijven altijd bovenop alles staan, en ze verschijnen niet als aparte taakbalkknoppen. Het werkt voor sommige workflows, maar voor multi-monitoropstellingen is het frustrerend.

Mads Kristensen van het Visual Studio-team [deelde een weinig bekende instelling](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) die volledig verandert hoe zwevende vensters zich gedragen. Één dropdown. Dat is alles.

## De instelling

**Tools > Options > Environment > Windows > Floating Windows**

De dropdown "These floating windows are owned by the main window" heeft drie opties:

- **None** — volledige onafhankelijkheid. Elk zwevend venster krijgt zijn eigen taakbalkvermelding en gedraagt zich als een normaal Windows-venster.
- **Tool Windows** (standaard) — documenten zweven vrij, toolvensters blijven gebonden aan de IDE.
- **Documents and Tool Windows** — klassiek Visual Studio-gedrag, alles gebonden aan het hoofdvenster.

## Waarom "None" de juiste keuze is voor multi-monitoropstellingen

Stel het in op **None** en plotseling gedragen al je zwevende toolvensters en documenten zich als echte Windows-applicaties. Ze verschijnen in de taakbalk, blijven zichtbaar als je het hoofd-Visual Studio-venster minimaliseert, en dringen zich niet meer naar voren.

Combineer dit met **PowerToys FancyZones** en het is een game changer. Maak aangepaste indelingen over je monitoren, snap je Solution Explorer naar één zone, debugger naar een andere, en codebestanden waar je wilt. Alles blijft op zijn plek, alles is onafhankelijk toegankelijk.

## Snelle aanbevelingen

- **Multi-monitor power users**: Stel in op **None**, combineer met FancyZones
- **Occasionele zwevende vensters**: **Tool Windows** (standaard) is een solide middenweg
- **Traditionele workflow**: **Documents and Tool Windows** houdt alles klassiek

Pro tip: **Ctrl + dubbelklikken** op de titelbalk van een toolvenster om het direct te laten zweven of te docken. Geen herstart nodig na het wijzigen van de instelling.

## Afronding

Het is een van die "Ik kan niet geloven dat ik dit niet wist" instellingen. Als zwevende vensters in Visual Studio je ooit hebben geërgerd, ga dit nu wijzigen.

Lees het [volledige bericht](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) voor details en screenshots.
