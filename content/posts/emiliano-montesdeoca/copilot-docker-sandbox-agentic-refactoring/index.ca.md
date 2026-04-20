---
title: "Docker Sandbox permet als agents Copilot refactoritzar el vostre codi sense posar en risc la vostra màquina"
date: 2026-04-17
author: "Emiliano Montesdeoca"
description: "Docker Sandbox ofereix als agents de GitHub Copilot una microVM segura per funcionar amb refactorització: sense sol·licituds de permís, sense risc per al vostre amfitrió. Heus aquí per què això ho canvia tot per a la modernització de.NET a gran escala."
tags:
  - github-copilot
  - docker
  - modernization
  - developer-tools
  - ai
---

Si heu utilitzat el mode d'agent de Copilot per a qualsevol cosa més enllà de petites edicions, coneixeu el dolor. Cada escriptura de fitxers, cada ordre del terminal: un altre indicador de permís. Ara imagineu-ho fent servir 50 projectes. No és divertit.

L'equip d'Azure acaba de publicar una publicació sobre [Docker Sandbox for GitHub Copilot agents](https://devblogs.microsoft.com/all-things-azure/best-of-both-worlds-for-agentic-refactoring-github-copilot-microvms-via-docker-sandbox/), i sincerament, aquesta és una de les millores d'eines d'agents més pràctiques que he vist. Utilitza microVMs per oferir a Copilot un entorn totalment aïllat on es pot desenredar: instal·lar paquets, executar compilacions, executar proves, sense tocar el vostre sistema amfitrió.

## Què us ofereix realment Docker Sandbox

La idea bàsica és senzilla: engegueu una microVM lleugera amb un entorn Linux complet, sincronitzeu-hi el vostre espai de treball i deixeu que l'agent Copilot operi lliurement a l'interior. Quan s'hagi acabat, torna a canviar la sincronització.

Això és el que fa que sigui més que "executar coses en un contenidor":

- **Sincronització bidireccional de l'espai de treball** que conserva camins absoluts. L'estructura del vostre projecte sembla idèntica dins del sandbox. No hi ha errors de compilació relacionats amb el camí.
- **Dimoni Docker privat** que s'executa dins de la microVM. L'agent pot construir i executar contenidors sense muntar mai el sòcol Docker del vostre host. Això és un gran problema per a la seguretat.
- **Proxis de filtratge HTTP/HTTPS** que controlen a què pot arribar l'agent a la xarxa. Tu decideixes quins registres i punts finals es permeten. Atacs a la cadena de subministrament d'un canalla `npm install` dins del sandbox? Bloquejat.
- **Mode YOLO** — sí, així l'anomenen. L'agent s'executa sense sol·licituds de permís perquè literalment no pot danyar el vostre amfitrió. Tota acció destructiva està continguda.

## Per què els desenvolupadors.NET haurien de preocupar-se

Penseu en el treball de modernització que tants equips s'enfronten ara mateix. Teniu una solució.NET Framework amb 30 projectes i l'heu de traslladar a.NET 9. Això són centenars de canvis de fitxers: fitxers de projecte, actualitzacions d'espais de noms, substitucions d'API, migracions NuGet.

Amb Docker Sandbox, podeu apuntar un agent Copilot a un projecte, deixar-lo refactoritzar lliurement dins de la microVM, executar `dotnet build` i `dotnet test` per validar i acceptar només els canvis que funcionen realment. No hi ha cap risc que accidentalment destrueixi el vostre entorn de desenvolupament local mentre experimenteu.

La publicació també descriu l'execució d'una **flota d'agents paral·lels**, cadascun en el seu propi sandbox, abordant diferents projectes simultàniament. Per a grans solucions.NET o arquitectures de microserveis, això suposa un estalvi de temps enorme. Un agent per servei, tots en funcionament aïllat, tots validats de manera independent.

## L'angle de seguretat és important

Això és el que la majoria de la gent passa per alt: quan deixeu que un agent d'IA executi ordres arbitràries, hi confieu amb tota la vostra màquina. Docker Sandbox canvia aquest model. L'agent obté total autonomia dins d'un entorn d'ús. El servidor intermediari de xarxa garanteix que només es pot extreure de fonts aprovades. El vostre sistema de fitxers amfitrió, el dimoni Docker i les credencials no es toquen.

Per als equips amb requisits de compliment, i això és la majoria de les botigues.NET empresarials, aquesta és la diferència entre "no podem utilitzar IA agència" i "podem adoptar-la de manera segura".

## Per emportar

Docker Sandbox resol la tensió fonamental de la codificació agentica: els agents necessiten llibertat per ser útils, però la llibertat a la vostra màquina amfitriona és perillosa. Les microVM us ofereixen tots dos. Si esteu planejant qualsevol refactorització o modernització de.NET a gran escala, val la pena configurar-la ara. La combinació de la intel·ligència de codi de Copilot amb un entorn d'execució segur és exactament el que els equips de producció estaven esperant.
