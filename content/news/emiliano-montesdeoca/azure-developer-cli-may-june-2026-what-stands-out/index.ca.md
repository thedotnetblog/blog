---
title: "L'Azure Developer CLI continua convertint-se en una millor eina de l'inner loop"
date: 2026-06-28
author: "Emiliano Montesdeoca"
description: "Les versions de maig i juny de 2026 de l'Azure Developer CLI afegeixen molt, però el valor més gran és com milloren el bucle diari: millor gestió d'eines, provisió més segura, suport més fort per a extensions i fluxos d'execució més pràctics."
tags:
  - Azure Developer CLI
  - azd
  - Azure
  - Developer Tools
  - .NET
---

*Aquest article s'ha traduït automàticament. Per veure la versió original, [fes clic aquí]({{< ref "index.md" >}}).*

Els grans resumidors de CLI poden ser esgotadors de llegir perquè barregen millores de flux de treball importants amb petits retocs en una sola paret de text.

Així que aquí tens la meva versió curta: les darreres actualitzacions de l'**Azure Developer CLI** importen perquè `azd` continua convertint-se en una **millor eina de l'inner loop**, no només en un embolcall de desplegament.

Aquest és el canvi important.

## La gestió d'eines està passant a formar part del producte, no d'una tasca lateral

Una de les meves addicions preferides són les noves ordres `azd tool`.

Qualsevol cosa que redueixi la fricció de configuració val la pena, especialment en projectes on un entorn funcional depèn d'una barreja de SDKs, CLIs, Docker, Bicep i extensions.

Si ara l'eina pot ajudar a descobrir, instal·lar, comprovar i actualitzar aquestes dependències directament, elimina molts dels modes de fallada molestos que solen afectar primer els nouvinguts.

Això sí que és valor real.

## `azd exec` també sembla més important del que sona

D'entrada, `azd exec` pot semblar una petita comoditat.

Jo no ho crec.

Executar ordres amb tot el context de l'entorn `azd`, incloent-hi la resolució de secrets, és exactament el tipus de capacitat que fa que l'automatització local i l'scripting siguin molt més nets.

Això redueix la necessitat d'scripts d'unió addicionals i ajuda a mantenir l'execució consistent entre entorns.

Això és una victòria pràctica.

## La provisió més segura i el millor comportament de cancel·lació són millores infravalorades

L'actualització també inclou canvis sobre les dependències de provisió, el maneig de la cancel·lació i el comportament del desplegament, coses que potser no semblen glamuroses però que són molt benvingudes.

Les sol·licituds de cancel·lació interactives, una millor modelització de dependències i un estat de desplegament més clar són el tipus de millores que fan que el CLI sembli fiable quan treballes amb recursos reals d'Azure.

I la confiança és molt important en eines com aquesta.

## La meva lectura

Com més millora `azd` en configuració, scripting, seguretat de desplegament i suport d'extensions, més se sent com una cosa que pots mantenir en el teu bucle diari en lloc de tocar només just abans del desplegament.

Aquesta és la direcció correcta.

Per als equips que construeixen aplicacions cloud-native o impulsades per IA a Azure, això fa que el CLI sigui més útil allà on més importa: durant el desenvolupament real.

Publicació original: [Azure Developer CLI (azd) – May and June 2026](https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/)