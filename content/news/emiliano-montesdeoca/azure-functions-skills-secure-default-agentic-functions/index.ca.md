---
title: "Azure Functions Skills Potser Són la Manera Més Ràpida de Posar les Functions Agèntiques al Camí Correcte"
date: 2026-05-18
author: "Emiliano Montesdeoca"
description: "La nova previsualització d'azure-functions-skills és interessant perquè fa més que bastir codi. Ensenya als agents de codificació a construir Azure Functions amb patrons actuals, identitat gestionada i valors predeterminats conscients del desplegament."
tags:
  - Azure Functions
  - AI
  - MCP
  - GitHub Copilot
  - Azure
---

Un dels problemes més comuns amb el codi al núvol generat per IA és que sembla plausible mentre segueix estant lleugerament endarrerit respecte a la realitat.

El codi compila. La funció es desplega. La mostra sembla bé.

Després notes els detalls:

- models de programació obsolets
- secrets hardcodejats al projecte
- males eleccions d'escalat
- cap disseny basat en identitat
- manca de validació abans del desplegament

Això és exactament per què **azure-functions-skills** em sembla útil.

La previsualització no és només un altre ajudant de scaffolding. Intenta resoldre un problema molt més important: fer que els agents de codificació produeixin **solucions d'Azure Functions actuals i segures per defecte** en lloc de primers esborranys que semblen decents però estan operativament desactualitzats.

## L'article font és refrescantment honest sobre el mode de fallada

Una part de l'article original que m'agrada molt és com de directe és sobre el problema.

Diu que els agents genèrics sovint "**deixen claus hardcodejades, cadenes de connexió i altres secrets a la teva funció perquè els netegis després**."

Aquest és exactament el tipus de frase que vull en un article com aquest.

Perquè anomena el problema real en lloc de pretendre que la bretxa és petita.

No es tracta de si els agents poden escriure codi en absolut. Poden.

Es tracta de si poden escriure **codi d'Azure que sigui sensat per a producció**.

Aquest és un llistó diferent.

## El valor real és ensenyar a l'agent millors hàbits

El que em va cridar l'atenció no és només l'ordre d'instal·lació o el catàleg d'skills.

És la idea que el plugin dóna a l'agent:

- patrons actuals d'Azure Functions
- valors predeterminats d'identitat gestionada
- guia per a Flex Consumption
- integració amb la plantilla d'Azure MCP
- skills de desplegament i validació
- una passada "doctor" abans d'enviar

Això importa perquè moltes fallades de codificació d'IA passen a la bretxa entre la **generació de codi genèrica** i la **correcció específica de la plataforma**.

I aquesta bretxa és on els equips perden temps.

## Per què això se sent oportú

A mesura que més equips utilitzen GitHub Copilot CLI, Claude Code, VS Code i fluxos similars per construir aplicacions al núvol, la peça que falta sovint no és la generació de codi en brut.

És el context.

Més específicament:

- quin és el model d'hostatjament actual?
- quina és la història d'auth preferida?
- quins patrons escalen en aquesta plataforma?
- què s'ha de validar abans de desplegar?

Aquestes són exactament les àrees on les "agent skills" comencen a tenir més sentit que llançar un model més gran al problema.

## La idea del `doctor` és especialment intel·ligent

Si hagués de triar una cosa de l'anunci que crec que els equips acabaran apreciant més, probablement és l'ordre `doctor`.

L'article font diu que els defectes de codi i la configuració incorrecta representen "**aproximadament el 53%**" dels incidents de suport d'Azure Functions en la seva anàlisi interna.

Aquest número importa.

Perquè significa que l'equip de plataforma no està endevinant on viu el dolor. Estan construint al voltant d'un patró de fallada molt concret.

I, honestament, aquest és el tipus de pensament de producte que em mereix més confiança:

- identificar els errors recurrents més cars
- detectar-los abans del desplegament
- fer que el camí bo sigui més fàcil que el dolent

Així és com millores l'experiència del desenvolupador de manera significativa.

## La meva opinió

Aquest és exactament el tipus de capa d'eines que espero que es torni més comuna.

No perquè els agents necessitin més hype, sinó perquè necessiten **millors vies** quan apunten a plataformes reals com Azure Functions.

La part més intel·ligent d'aquesta previsualització és que no només ajuda els agents a escriure codi. Els ajuda a escriure codi **actual, conscient d'Azure, conscient d'identitat i conscient de desplegament**.

Aquesta és una ambició molt més útil.

I per als equips que construeixen càrregues de treball serverless o habilitades per agents a Azure, això fa que valgui la pena seguir aquesta previsualització molt de prop.

Article original: [Introducing azure-functions-skills: An AI-Era Workspace for Azure Functions (Preview)](https://devblogs.microsoft.com/azure-sdk/introducing-azure-functions-skills-ai-era-workspace/)