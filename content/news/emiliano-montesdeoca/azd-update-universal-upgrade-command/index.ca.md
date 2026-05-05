---
title: "azd update: una comanda per controlar tots els vostres gestors de paquets"
date: 2026-04-15
author: "Emiliano Montesdeoca"
description: "L'Azure Developer CLI ara té una ordre d'actualització universal que funciona independentment de com l'hagueu instal·lat: winget, Homebrew, Chocolatey o script d'instal·lació."
tags:
  - azure
  - azd
  - developer-tools
  - cli
---

Sabeu que el missatge "Hi ha una versió nova d'azd disponible" que apareix cada poques setmanes? El que descarteu perquè no recordeu si vau instal·lar `azd` mitjançant winget, Homebrew o aquell script curl que vau executar fa sis mesos? Sí, finalment s'ha arreglat.

Microsoft acaba d'enviar [`azd update`](https://devblogs.microsoft.com/azure-sdk/azd-update/): una ordre única que actualitza l'Azure Developer CLI a la darrera versió, independentment de com l'haveu instal·lat originalment. Windows, macOS, Linux, no importa. Una ordre.

## Com funciona

```bash
azd update
```

Això és tot. Si voleu un accés anticipat a noves funcions, podeu canviar a la creació diària d'insiders:

```bash
azd update --channel daily
azd update --channel stable
```

L'ordre detecta el vostre mètode d'instal·lació actual i utilitza el mecanisme d'actualització adequat sota el capó. No més "espera, he fet servir winget o choco en aquesta màquina?"

## La petita captura

`azd update` s'envia a partir de la versió 1.23.x. Si teniu una versió anterior, haureu de fer una darrera actualització manual mitjançant el vostre mètode d'instal·lació original. Després d'això, `azd update` s'encarrega de tot el futur.

Comproveu la vostra versió actual amb `azd version`. Si necessiteu una instal·lació nova, els [documents d'instal·lació](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) us cobreixen.

## Per què és important

Aquesta és una petita millora de la qualitat de vida, però per a aquells de nosaltres que utilitzem `azd` diàriament per desplegar agents d'IA i aplicacions Aspire a Azure, mantenir-se al dia significa menys moments "aquest error ja s'ha solucionat a la darrera versió". Una cosa menys per pensar.

Llegiu l'[anunci complet](https://devblogs.microsoft.com/azure-sdk/azd-update/) i la [immersió més profunda](https://blog.jongallant.com/2026/04/azd-update) de Jon Gallant per a més context.
