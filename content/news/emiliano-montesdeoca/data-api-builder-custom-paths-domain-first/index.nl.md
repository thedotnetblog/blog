---
title: 'Data API Builder Custom Paths: Ontwerp API's voor Mensen, Niet voor Tabellen'
date: 2026-07-17
author: 'Emiliano Montesdeoca'
description: 'Samengestelde REST-paden in DAB zijn een kleine functie met grote architecturale impact voor domeingericht API-ontwerp.'
tags:
  - data-api-builder
  - azure-sql
  - rest-api
  - api-design
  - dotnet
---

Originele bron: [Compose your API surface with Data API builder custom paths](https://devblogs.microsoft.com/azure-sql/data-api-builder-custom-rest-paths/)

De nieuwe ondersteuning voor samengestelde REST-paden in Data API Builder lijkt misschien een kleine configuratieverbetering, maar het lost eigenlijk een aloude spanning in API-ontwerp op: databasestructuur die lekt in het ontwerp van openbare endpoints.

Standaard entiteitgebaseerde routes zijn geweldig voor snelle starts. Ze zijn vaak verkeerd voor langetermijnproduct-API's. Echte systemen hebben routestructuren nodig die aansluiten bij bedrijfsconcepten, eigenaarsgrenzen en de mentale modellen van gebruikers.

Daarom is deze DAB-wijziging belangrijk. Je kunt het gemak van gegenereerde API's behouden terwijl je een schonere domeinfirst-oppervlakte presenteert.

Mijn uitgesproken mening is simpel: als je API-padstructuur in productie ruwe tabelnamen weerspiegelt, optimaliseer je meestal voor backend-gemak ten koste van duidelijkheid voor clients.

Met aangepaste paden kunnen teams betere grenzen modelleren, zoals verkoop, facturatie, ondersteuning of partnerspecifieke oppervlaktes. Dit vervangt geen goed API-beheer, maar geeft DAB-gebruikers een praktische manier om routeontwerp af te stemmen op producttaal.

Praktische richtlijnen voor teams die deze functie adopteren:

Definieer een naamgevingsbeleid voordat je ad-hoc paden toevoegt. Inconsistente subsegmenten worden rommel op de lange termijn.

Wijs endpoints toe aan begrensde contexten, niet aan organisatieschema's. Teams veranderen; domeinsemantiek moet stabiel zijn.

Behandel padstructuur als onderdeel van je versioneringsstrategie en documenteer breaking changes expliciet.

Valideer autorisatiegedrag langs aangepaste routestructuren, zodat routehelderheid gepaard gaat met beveiligingshelderheid.

Wat ik waardeer aan DAB in het algemeen is het hefboommodel: je krijgt paginering, filtering, projectie en andere endpointmechanismen zonder repetitieve controllercode te schrijven. Aangepaste paden maken die hefboom productiegerichter door een van de grootste bezwaren van API-architecten weg te nemen.

Er is één kanttekening. Een betere padsamenstelling kan teams verleiden om te veel te snel bloot te geven omdat genereren makkelijk aanvoelt. Beveiligingen blijven belangrijk: houd entiteitblootstelling doelbewust, pas beleid centraal toe en vermijd het bouwen van onbedoelde openbare contracten uit interne schema-experimenten.

Voor .NET-organisaties onderleveringsdruk is deze functie een productiviteitsversneller als deze met discipline wordt gebruikt. Je kunt sneller werken dan handgemaakte API-lagen terwijl je toch een samenhangend en bedrijfsvriendelijk endpoint-oppervlak behoudt.

Bottom line: DAB aangepaste paden gaan niet over het mooier maken van URL's. Ze gaan over het heroveren van API-ontwerpintentie terwijl de operationele efficiëntie van gegenereerde endpoints behouden blijft.