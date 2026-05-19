---
title: "Private Endpoints, VNets, NSG's — Aspire Beheert het Netwerk Nu"
date: 2026-05-19
author: "Emiliano Montesdeoca"
description: "De nieuwe Azure enterprise-netwerkondersteuning van Aspire laat je VNets, private endpoints, NAT-gateways, NSG's en Network Security Perimeters direct in AppHost modelleren — zonder infrastructuurdrift."
tags:
  - Aspire
  - Azure
  - Networking
  - Security
  - .NET
---

Ik heb dit scenario te vaak gezien. De app is klaar. De demo is geweldig. Dan verschijnt de beveiligingschecklist: haal opslag uit het publieke internet, draai binnen een VNet, lever uitgaande IP's voor de allowlist van de partner, bewijs dat alleen de juiste subnetten met de juiste services communiceren.

Op dat punt beginnen het applicatiemodel en het infrastructuurmodel uit elkaar te lopen op manieren die pijnlijk te onderhouden zijn.

De nieuwe Azure enterprise-netwerkondersteuning van Aspire pakt dit direct aan. Je beschrijft de vorm van het netwerk in AppHost naast de resources die het gebruiken.

## Bouwblokken

Dit is waarvoor elk Azure-netwerkconcept dient, samengevat:

| Functie | Wanneer gebruiken | Waarom het belangrijk is |
|---------|------------|----------------|
| Virtueel netwerk | Wanneer je privé-adresruimte nodig hebt | Netwerkgrens voor subnetten, private endpoints en routing |
| Subnet | Wanneer je workloads binnen een VNet moet scheiden | Elk deel van het systeem krijgt zijn eigen adresbereik en beleidsoppervlak |
| Gedelegeerd subnet | Wanneer een platformservice (bijv. ACA) het subnet moet beheren | Laat de service beheerde infrastructuur veilig in je VNet plaatsen |
| NAT-gateway | Wanneer je voorspelbare uitgaande publieke IP's nodig hebt | Stabiel adres voor allowlists en audits |
| Private endpoint | Wanneer je een PaaS-resource privé toegankelijk wil maken | Plaatst een privé-IP voor die service in je VNet, verwijdert publieke blootstelling |
| NSG | Wanneer je verkeersregels op subnetniveau nodig hebt | Expliciete toestaan/weigeren voor inkomend en uitgaand verkeer per subnet |

## Beschrijven in AppHost

De sleutelverandering hier is dat je het netwerk *naast* de resources modelleert die het gebruiken, niet in een apart Bicep-bestand dat in de loop van de tijd afwijkt van het applicatiemodel.

Vanuit AppHost kun je:

- VNets en subnetten aanmaken met `AddVirtualNetwork()` en `AddSubnet()`
- Een NAT-gateway aan subnetten koppelen voor stabiele uitgaande IP's
- Private endpoints aanmaken voor opslag, Key Vault, SQL en andere PaaS-services
- NSG's definiëren met inkomende en uitgaande beveiligingsregels
- Network Security Perimeters configureren voor beleid over resources heen

Het resultaat is dat wanneer je `azd up` uitvoert, de infrastructuur overeenkomt met wat het applicatiemodel zegt dat het nodig heeft. Niet wat een handmatig onderhouden sjabloon zegt.

## Waarom Dit Belangrijk Is voor Echte Applicaties

Een paar dingen die veel eenvoudiger worden zodra het netwerk gemodelleerd is in Aspire:

**Private endpoints voor Key Vault en opslag** — je beschrijft `WithPrivateEndpoint()` op die resources, en Aspire regelt de DNS-zoneconfiguratie en het koppelen van endpoints. De app verandert nooit.

**Consistente uitgaande IP's** — voeg een NAT-gateway toe aan het relevante subnet, en elk uitgaand verzoek van je app gaat via een bekend, stabiel IP. Partners kunnen het op de allowlist zetten. Auditors kunnen het volgen.

**NSG-regels vanuit code** — in plaats van in de portal te klikken of een Bicep-fragment te onderhouden, leven je beveiligingsregels in AppHost naast de resources die ze beschermen.

Dit is het type integratie dat demo's niet opwindend maakt, maar productiesystemen onderhoudbaar.

## Conclusie

Netwerkbeveiliging die laat in de projectlevenscyclus verschijnt, is een opgelost probleem als je het vanaf het begin samen met de applicatie modelleert. De enterprise-netwerkondersteuning van Aspire maakt dit mogelijk zonder een apart infrastructuurtraject.

Volledige details in de originele post: [Securing Azure apps with Aspire enterprise networking](https://devblogs.microsoft.com/aspire/aspire-azure-enterprise-networking/)
