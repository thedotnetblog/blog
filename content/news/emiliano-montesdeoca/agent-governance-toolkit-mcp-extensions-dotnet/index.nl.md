---
title: "Agent Governance Toolkit MCP-extensies maken het veilige pad veel eenvoudiger in .NET"
date: 2026-05-21
author: "Emiliano Montesdeoca"
description: "De nieuwe Agent Governance Toolkit MCP-extensies voor .NET plaatsen beleidshandhaving, opstartscanning en responssanering direct in de MCP-serverbuilderflow. Dat is precies het secure-by-default-verhaal dat ik wil zien."
tags:
  - .NET
  - MCP
  - AI
  - Security
  - Agent Governance Toolkit
---

Een van de grootste problemen in agent-tooling op dit moment is dat het happy path meestal het onveilige pad is.

Je kunt een MCP-server opzetten. Je kunt snel tools blootstellen. Je kunt de demo laten werken.

Dan komen daarna direct de ongemakkelijke vragen:

- wie mag wat aanroepen?
- wat gebeurt er als tool-metadata kwaadaardig of misleidend is?
- wat als onveilige output rechtstreeks teruggevoerd wordt naar het model?
- hoeveel hiervan is beleid, en hoeveel is gewoon conventie?

Daarom zijn de nieuwe **Agent Governance Toolkit MCP-extensies voor .NET** belangrijk.

Ze lossen niet elk beveiligingsprobleem in het agent-ecosysteem op, maar ze doen iets heel belangrijks: ze maken de standaard .NET-builderflow veel makkelijker te verharden.

## De belangrijkste zin in de aankondiging

De bronpost zegt dat het pakket "**one-call governance**" toevoegt aan `IMcpServerBuilder`.

Dat is precies de zin waar ik me op zou richten.

Want de meeste teams falen niet in het bouwen van agent-governance door gebrek aan bewustzijn. Ze falen omdat het veilige pad meer werk is, meer bekabeling, meer aangepaste code en meer kansen om de opruiming naar later uit te stellen.

En "later" is waar risico graag woont.

## Waarom dit een goed .NET-verhaal is

Wat ik hier waardeer, is hoe natuurlijk het pakket in het bestaande buildermodel past.

In plaats van teams te dwingen tot:

- een sidecar
- een aparte proxy
- een aangepaste wrapper-architectuur
- of een vreemde alternatieve SDK

breidt het pakket de officiële C# MCP-builderflow direct uit.

Dat is belangrijk.

Als beveiliging architecturale acrobatiek vereist, daalt adoptie direct. Als beveiliging aanvoelt als een normaal onderdeel van het configureren van de server, wordt adoptie veel realistischer.

## Het dreigingsmodel is niet langer theoretisch

Eén ding dat teams naar mijn mening niet moeten onderschatten, is hoe snel MCP-gerelateerd risico echt wordt in productiesystemen.

Het bronartikel noemt vragen zoals:

- "**Moet elke geregistreerde tool aanroepbaar zijn door elke agent?**"
- "**Wat gebeurt er als een tool-beschrijving instructies bevat in de stijl van prompt-injectie?**"

Dat zijn precies de juiste vragen.

Want zodra tools het uitvoeringsoppervlak voor agents worden, genereert het systeem niet langer alleen tekst. Het neemt beslissingen die beveiligings-, betrouwbaarheids- en governance-gevolgen kunnen hebben.

Dat verandert de lat.

## Wat het pakket goed doet

De sterkste ontwerpkeuze van de extensie is dat het meerdere beveiligingslagen bundelt in één samenhangende flow:

- opstartscanning voor onveilige tooldefinities
- beleidshandhaving bij uitvoering
- identiteitsbewuste governance
- responssanering voordat content teruggaat naar de client of het model
- audit- en metrics-hooks

Dat is de juiste vorm.

Niet één grote "beveiligingsmodus". Een set specifieke controles die verschillende faalpunten in de levenscyclus dekken.

### Opstartscanning is belangrijker dan veel teams beseffen

Ik vind het vooral fijn dat onveilige tool-metadata standaard de opstart kan laten mislukken.

Dat is een sterk standpunt, en ik denk dat het het juiste is.

Hoe eerder je een vergiftigde of verdachte tooldefinitie kunt blokkeren, hoe beter. Wachten tot runtime is voor een hele categorie problemen al te laat.

### Responssanering is ook een zeer praktische laag

Een ander ondergewaardeerd punt in de aankondiging is de focus op outputsanering.

Veel teams denken na over gevaarlijke input.

Minder teams denken zorgvuldig genoeg na over gevaarlijke output die terugkomt van een tool en rechtstreeks in een agent-loop terechtkomt.

Dat is een makkelijke plek om je vingers aan te branden.

## Waar ik nog steeds zorgvuldig op zou letten

Ook al vind ik dit pakket erg goed, ik zou nog steeds op één ding letten: governance-tooling werkt alleen als teams daadwerkelijk zinvol beleid definiëren en onderhouden.

De extensie maakt het eenvoudiger om het mechanisme aan te sluiten. Dat is geweldig.

Maar teams moeten nog steeds het lastigere organisatorische werk doen van bepalen:

- welke tools toegestaan zijn
- welke agents of identiteiten ze mogen aanroepen
- wat "deny by default" echt zou moeten betekenen in hun omgeving
- hoe false positives en uitzonderingen worden afgehandeld

Dus ik zou dit pakket behandelen als een sterke handhavingslaag, niet als een vervanging voor architecturaal oordeel.

## Mijn standpunt

Dit is een van de duidelijkste **secure-by-default** .NET-agent-aankondigingen die ik in een tijd heb gezien.

Niet omdat het magie belooft, maar omdat het een categorie beveiligingswerk aanpakt die teams waarschijnlijk inconsistent zouden implementeren, en het een schonere, natuurlijkere plek geeft in de builderpijplijn.

Dat is precies het soort pakket dat ik in dit ecosysteem wil.

Het beëindigt niet het bredere governance-gesprek. Het doet iets praktischers: het maakt het veel moeilijker om te doen alsof governance de opruimtaak van iemand anders zou moeten zijn, later.

En dat is echte vooruitgang.

Oorspronkelijke post: [Announcing Agent Governance Toolkit MCP Extensions for .NET](https://devblogs.microsoft.com/dotnet/announcing-agent-governance-toolkit-mcp-extensions-for-dotnet/)