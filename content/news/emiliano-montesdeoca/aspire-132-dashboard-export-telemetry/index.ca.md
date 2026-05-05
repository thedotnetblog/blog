---
title: "El tauler de control de l'Aspire 13.2 acaba de tenir una API de telemetria i ho canvia tot"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: ".NET Aspire 13.2 ofereix una exportació de telemetria més intel·ligent, una API programable per a traces i registres i millores de visualització de GenAI. Heus aquí per què això és important per al vostre flux de treball de depuració."
tags:
  - aspire
  - dotnet
  - opentelemetry
  - dashboard
  - observability
  - ai
---

Si heu estat creant aplicacions distribuïdes amb.NET Aspire, ja sabeu que el tauler és el millor de tota l'experiència. Tots els vostres rastres, registres i mètriques en un sol lloc: sense Jaeger extern, sense configuració de Seq, sense moments "deixa'm comprovar l'altre terminal".

Aspire 13.2 l'acaba de millorar significativament. James Newton-King [va anunciar l'actualització](https://devblogs.microsoft.com/aspire/aspire-dashboard-improvements-export-and-telemetry/), i sincerament? Només l'exportació de telemetria i les funcions de l'API mereixen l'actualització.

## Exporta la telemetria com una persona sensata

Aquest és l'escenari que tots hem viscut: esteu depurant un problema distribuït, finalment el reproduïu després de vint minuts de configuració i ara heu de compartir el que va passar amb el vostre equip. Abans? Captures de pantalla. Copia i enganxa ID de traça. L'embolic habitual.

Aspire 13.2 afegeix un diàleg adequat **Gestiona els registres i la telemetria** on podeu:

- Esborra tota la telemetria (útil abans d'un intent de reproducció)
- Exporteu la telemetria seleccionada a un fitxer ZIP en format estàndard OTLP/JSON
- Torneu a importar aquest ZIP a qualsevol tauler de control d'Aspire més tard

Aquesta última part és la característica assassina. Reproduïu un error, exporteu la telemetria, l'adjunteu al vostre element de treball i el vostre company d'equip pot importar-lo al seu propi tauler per veure exactament el que heu vist. No més "pots reproduir-lo a la teva màquina?"

Les traces, els intervals i els registres individuals també reben una opció "Exporta JSON" als seus menús contextuals. Necessites compartir un rastre específic? Feu clic amb el botó dret, copieu JSON i enganxeu-lo a la vostra descripció de PR. Fet.

## L'API de telemetria és el veritable canvi de joc

Això és el que m'emociona més. El tauler ara exposa una API HTTP a `/api/telemetry` per consultar dades de telemetria amb programació. Punts finals disponibles:

- `GET /api/telemetry/resources`: llista els recursos amb telemetria
- `GET /api/telemetry/spans`: la consulta s'estén amb filtres
- `GET /api/telemetry/logs`: registres de consultes amb filtres
- `GET /api/telemetry/traces` — llista traces
- `GET /api/telemetry/traces/{traceId}`: obteniu tots els intervals d'un rastre específic

Tot torna en format OTLP JSON. Això impulsa les noves ordres CLI `aspire agent mcp` i `aspire otel`, però la implicació real és més gran: ara podeu crear eines, scripts i integracions d'agents d'IA que consulten directament la telemetria de la vostra aplicació.

Imagineu un agent de codificació d'IA que pugui mirar les vostres traces distribuïdes reals mentre es depura. Això ja no és hipotètic: això és el que permet aquesta API.

## La telemetria GenAI es fa pràctica

Si esteu creant aplicacions basades en IA amb Semantic Kernel o Microsoft.Extensions.AI, apreciareu el visualitzador de telemetria GenAI millorat. Aspire 13.2 afegeix:

- Descripcions d'eines d'IA representades com a Markdown
- Un botó dedicat GenAI a la pàgina de traces per accedir ràpidament a traces d'IA
- Millor gestió d'errors per a JSON GenAI truncat o no estàndard
- Navegació fent clic per ressaltar entre definicions d'eines

La publicació del bloc esmenta que el xat de VS Code Copilot, la CLI de Copilot i l'OpenCode admeten la configuració d'un `OTEL_EXPORTER_OTLP_ENDPOINT`. Apunteu-los al tauler de control d'Aspire i podreu veure literalment els vostres agents d'IA pensar en temps real mitjançant la telemetria. Aquesta és una experiència de depuració que no trobareu enlloc més.

## Tancant

Aspire 13.2 fa que el tauler de control sigui "una bona interfície d'usuari de depuració" a una "plataforma d'observabilitat programable". Només el flux de treball d'exportació/importació estalvia temps real en la depuració distribuïda i l'API de telemetria obre la porta als diagnòstics assistits per IA.

Si ja esteu a Aspire, actualitzeu-lo. Si no ho feu, aquesta és una bona raó per consultar [aspire.dev](https://aspire.dev) i veure de què es tracta.
