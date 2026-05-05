---
title: "L'avaluació de la modernització de GitHub Copilot és la millor eina de migració que encara no feu servir"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "L'extensió de modernització de GitHub Copilot no només suggereix canvis de codi, sinó que produeix una avaluació completa de la migració amb problemes accionables, comparacions d'objectius d'Azure i un flux de treball col·laboratiu. Heus aquí per què el document d'avaluació és la clau de tot."
tags:
  - dotnet
  - azure
  - github-copilot
  - modernization
  - migration
  - aspnet-core
---

Migrar una aplicació.NET Framework heretada a.NET moderna és una d'aquestes tasques que tothom sap que hauria de fer, però ningú vol començar. Mai és només "canviar el marc objectiu". Són les API que van desaparèixer, paquets que ja no existeixen, models d'allotjament que funcionen d'una manera completament diferent i un milió de petites decisions sobre què contener, què reescriure i què deixar en pau.

Jeffrey Fritz acaba de publicar una [immersió profunda en l'avaluació de la modernització de GitHub Copilot](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/), i sincerament? Aquesta és la millor eina de migració que he vist per a.NET. No a causa de la generació de codi, això és ara l'aposta de la taula. Pel document d'avaluació que elabora.

## No és només un motor de suggeriments de codi

L'extensió VS Code segueix un model **Avaluar → Planificar → Executar**. La fase d'avaluació analitza tota la vostra base de codi i produeix un document estructurat que ho recull tot: què cal canviar, quins recursos d'Azure proveir, quin model de desplegament utilitzar. Tot el que hi ha a baix (infraestructura com a codi, contenidors, manifestos de desplegament) depèn del que troba l'avaluació.

L'avaluació s'emmagatzema a `.github/modernize/assessment/` del vostre projecte. Cada execució produeix un informe independent, de manera que creeu un historial i podeu fer un seguiment de com evoluciona la vostra postura de migració a mesura que solucioneu els problemes.

## Dues maneres de començar

**Avaluació recomanada**: el camí ràpid. Trieu entre dominis seleccionats (actualització de Java/.NET, preparació al núvol, seguretat) i obteniu resultats significatius sense tocar la configuració. Ideal per a una primera mirada a on es troba la teva aplicació.

**Avaluació personalitzada**: el camí objectiu. Configureu exactament què voleu analitzar: càlcul objectiu (App Service, AKS, Container Apps), sistema operatiu objectiu, anàlisi de contenidors. Trieu diversos objectius d'Azure per comparar els enfocaments de migració de manera conjunta.

Aquesta visió de comparació és realment útil. Una aplicació amb 3 problemes obligatoris per a App Service pot tenir 7 per a AKS. Veure tots dos ajuda a impulsar la decisió d'allotjament abans de comprometre's amb una ruta de migració.

## El desglossament del problema és accionable

Cada problema ve amb un nivell de criticitat:

- **Obligatori**: s'ha de solucionar o la migració falla
- **Potencial**: pot afectar la migració, necessita el judici humà
- **Opcional**: millores recomanades, no bloquejaran la migració

I cada problema enllaça amb fitxers i números de línia afectats, proporciona una descripció detallada del que està malament i per què és important per a la vostra plataforma objectiu, ofereix passos concrets de correcció (no només "arreglar-ho") i inclou enllaços a documentació oficial.

Podeu lliurar problemes individuals als desenvolupadors i aquests tenen tot el que necessiten per actuar. Aquesta és la diferència entre una eina que us diu "hi ha un problema" i una que us indica com resoldre'l.

## Els camins d'actualització coberts

Específicament per a.NET:
-.NET Framework →.NET 10
- ASP.NET → ASP.NET Core

Cada camí d'actualització té regles de detecció que coneixen quines API s'han eliminat, quins patrons no tenen cap equivalent directe i quins problemes de seguretat necessiten atenció.

Per als equips que gestionen diverses aplicacions, també hi ha una CLI que admet avaluacions per lots multirepositori: cloneu tots els repositoris, avalueu-los tots, obteniu informes per aplicació i una visualització de cartera agregada.

## La meva opinió

Si esteu asseguts en aplicacions heretades de.NET Framework (i siguem reals, la majoria dels equips empresarials ho són), aquesta és *l'eina* per començar. Només el document d'avaluació val la pena el temps: converteix un vague "hauríem de modernitzar" en una llista concreta i prioritzada d'elements de treball amb camins clars.

El flux de treball col·laboratiu també és intel·ligent: exporteu avaluacions, compartiu amb el vostre equip, importeu-les sense tornar-les a executar. Revisions d'arquitectura on els que prenen les decisions no són els que executen les eines? Coberta.

## Tancant

L'avaluació de la modernització de GitHub Copilot transforma la migració.NET d'un projecte aterridor i indefinit a un procés estructurat i rastrejable. Comenceu amb una avaluació recomanada per veure on us trobeu i, a continuació, utilitzeu avaluacions personalitzades per comparar els objectius d'Azure i crear el vostre pla de migració.

Llegiu el [tutorial complet](https://devblogs.microsoft.com/dotnet/your-migrations-source-of-truth-the-modernization-assessment/) i agafeu l'[extensió del codi VS](https://aka.ms/ghcp-appmod/vscode-ext) per provar-ho a la vostra pròpia base de codi.
