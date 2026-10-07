---
title: "Els Camins Personalitzats de Data API Builder et Permeten Dissenyar APIs per a Humans, No per a Taules"
date: 2026-07-17
author: "Emiliano Montesdeoca"
description: "Els camins REST compostos a DAB són una funció petita amb un gran impacte arquitectònic per al disseny d'APIs orientat a domini."
tags:
  - data-api-builder
  - azure-sql
  - rest-api
  - api-design
  - dotnet
---

Font original: [Compose your API surface with Data API builder custom paths](https://devblogs.microsoft.com/azure-sql/data-api-builder-custom-rest-paths/)

El nou suport per a camins REST compostos a Data API Builder pot semblar una millora de configuració menor, però realment resol una tensió de disseny d'APIs de llarga durada: la topologia de la base de dades filtrant-se al disseny d'endpoints públics.

Les rutes basades en entitats per defecte són genials per a inicis ràpids. Sovint són incorrectes per a APIs de producte a llarg termini. Els sistemes reals necessiten estructures de ruta que coincideixin amb conceptes de negoci, límits de propietat i models mentals dels consumidors.

Per això importa aquest canvi a DAB. Podeu mantenir la comoditat d'API generada mentre presenteu una superfície de domini més neta.

La meva opinió és simple: si l'estructura dels vostres camins d'API reflecteix noms de taules en brut a producció, normalment esteu optimitzant per a la comoditat del backend a costa de la claredat del client.

Amb els camins personalitzats, els equips poden modelar millors límits, com ara vendes, facturació, suport o superfícies específiques de soci. Això no substitueix la governança adequada d'API, però dóna als usuaris de DAB una manera pràctica d'alinear el disseny de rutes amb el llenguatge del producte.

Guia pràctica per als equips que adoptin aquesta funció:

Definiu una política de noms abans d'afegir camins ad hoc. Els subsegments inconsistents es converteixen en desordre a llarg termini.

Mapa els endpoints a contextos delimitats, no a organigrames. Els equips canvien; la semàntica del domini hauria de ser estable.

Tracteu l'estructura de camins com a part de la vostra estratègia de versionat i documenteu els canvis trencadors explícitament.

Valideu el comportament d'autorització al llarg de les estructures de ruta personalitzades perquè la claredat de la ruta vagi acompanyada de claredat de seguretat.

El que aprecio a DAB en general és el model de palanquejament: obteniu paginació, filtratge, projecció i altres mecàniques d'endpoint sense escriure codi de controlador repetitiu. Els camins personalitzats fan que aquest palanquejament sigui més preparat per a producció reduint una de les objeccions més grans dels arquitectes d'API.

Hi ha un advertiment. Una millor composició de camins pot temptar els equips a exposar massa massa ràpid perquè la generació se sent fàcil. Les barreres de protecció encara importen: mantingueu l'exposició d'entitats deliberada, apliqueu polítiques de manera centralitzada i eviteu construir contractes públics accidentals a partir d'experiments interns d'esquema.

Per a les organitzacions .NET sota pressió de lliurament, aquesta funció és un desbloqueig de productivitat si s'utilitza amb disciplina. Podeu moure-us més ràpid que les capes d'API fetes a mà mentre preserveu una superfície d'endpoint coherent i amigable per al negoci.

Conclusió: els camins personalitzats de DAB no van d'embellir URLs. Van de recuperar la intenció del disseny d'API mentre es manté l'eficiència operativa dels endpoints generats.