---
title: "VS Code 1.120: Contrasenyes Segures, Selector de Mida de Context, Metadades GitHub a l'Agent Host"
date: 2026-06-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.120 és una versió enfocada als usuaris de Copilot: gestió segura de sol·licituds de contraseny, selector de mida de context del model, metadades de PR de GitHub a les sessions d'agent i gestió d'arxius de sessió."
tags:
  - VS Code
  - GitHub Copilot
  - Developer Tools
---

VS Code 1.120 s'ha llançat amb un conjunt de millores de l'agent Copilot que són petites individualment, però notablement millors en l'ús diari.

## Detecció Segura de Sol·licituds de Contraseny a Terminals d'Agent

Quan un agent Copilot executa una ordre de terminal que desencadena una sol·licitud de contraseny o frase de pas, VS Code ara ho detecta i mostra un diàleg de confirmació. El diàleg enfoca el terminal perquè puguis escriure el secret directament — i, de manera crucial, els secrets mai no es dirigeixen a través del model.

Aquesta és una millora de seguretat significativa. Anteriorment, els agents que executaven ordres que desencadenaven sol·licituds d'autenticació podien crear situacions en les quals els usuaris podrien exposar credencials inadvertidament. L'anunci del lector de pantalla significa que els usuaris d'accessibilitat també reben la notificació.

## Selector de Mida de Context al Selector de Model

Un nou selector de mida de context et permet seleccionar quant context usa el model per a una sessió. Els models diferents tenen mides de finestra de context diferents, i alguns fluxos de treball es beneficien de limitar-la (latència més baixa, cost més baix) o maximitzar-la (bases de codi complexes, sessions de llarga durada).

## Metadades de PR de GitHub a les Sessions d'Agent Host

Per a les sessions amb el suport d'un repositori GitHub, VS Code ara mostra metadades de GitHub — incloent-hi un botó de pull request — a la interfície d'usuari de l'agent host. Menys canvis de context cap al navegador o l'extensió de GitHub quan estàs treballant en una PR.

## Gestió d'Arxiu de Sessions de Xat

Dues millores per al Quick Pick de sessions:
- Les sessions arxivades estan ocultes per defecte (menys desordre visual)
- La cerca encara coincideix amb les sessions arxivades, de manera que pots recuperar-ne una per títol

Les sessions també s'agrupen per ordre de recència per defecte, la qual cosa facilita la recerca del treball recent.

## Descoberta de Connectors CLI de Copilot

VS Code ara descobreix automàticament els connectors de Copilot CLI instal·lats per l'usuari des de `~/.copilot/installed-plugins/`. Si has configurat WinUI o altres habilitats d'agent específiques del domini, es reconeixen sense configuració manual.

## API d'Editor de Diff Personalitzat (Vista Prèvia)

Per als autors d'extensions: una nova API proposada `customDiffEditorProvider` permet a les extensions renderitzar un diff unificat en un únic webview amb accés tant als documents originals com als modificats, en comptes de dues vistes d'editor personalitzades una al costat de l'altra.

Publicació original: [Visual Studio Code 1.120](https://code.visualstudio.com/updates/v1_120)
