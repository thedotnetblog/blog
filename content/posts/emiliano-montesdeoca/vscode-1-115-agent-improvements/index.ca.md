---
title: "VS Code 1.115: notificacions de terminal en segon pla, mode d'agent SSH i més"
date: 2026-04-06
author: "Emiliano Montesdeoca"
description: "VS Code 1.115 ofereix notificacions de terminal en segon pla per als agents, allotjament d'agents remots SSH, enganxament de fitxers als terminals i seguiment d'edició conscient de la sessió. Això és el que importa per als desenvolupadors de.NET."
tags:
  - vscode
  - developer-tools
  - copilot
  - ai
  - remote-development
---

VS Code 1.115 acaba de [sortir](https://code.visualstudio.com/updates/v1_115) i, tot i que és una versió més lleugera pel que fa a les funcions de titular, les millores relacionades amb l'agent són realment útils si treballeu amb assistents de codificació d'IA diàriament.

Permeteu-me destacar el que realment val la pena saber.

## Els terminals de fons parlen amb els agents

Aquesta és la característica destacada. Els terminals de fons ara notifiquen automàticament als agents quan es completen les ordres, inclòs el codi de sortida i la sortida del terminal. Les sol·licituds d'entrada als terminals de fons també es detecten i s'envien a l'usuari.

Per què importa això? Si heu utilitzat el mode d'agent de Copilot per executar ordres de compilació o suites de proves en segon pla, coneixeu el dolor de "Ja s'ha acabat?" — Els terminals de fons eren essencialment de foc i oblidar. Ara l'agent rep una notificació quan el vostre `dotnet build` o `dotnet test` s'acabi, veu la sortida i pot reaccionar en conseqüència. És un petit canvi que fa que els fluxos de treball impulsats per agents siguin significativament més fiables.

També hi ha una nova eina `send_to_terminal` que permet als agents enviar ordres a terminals en segon pla amb la confirmació de l'usuari, solucionant el problema en què `run_in_terminal` amb un temps d'espera traslladaria els terminals a segon pla i els faria només de lectura.

## Allotjament d'agent remot SSH

VS Code ara admet la connexió a màquines remotes mitjançant SSH, instal·lant automàticament la CLI i iniciant-la en mode d'amfitrió de l'agent. Això significa que les vostres sessions d'agent d'IA poden orientar-se directament a entorns remots, cosa que és útil per als desenvolupadors de.NET que creen i proveu en servidors Linux o màquines virtuals en núvol.

## Edita el seguiment a les sessions d'agent

Les edicions de fitxers fetes durant les sessions de l'agent ara es fan un seguiment i es restauren, amb diferències, desfer/refer i restauració de l'estat. Si un agent fa canvis al vostre codi i alguna cosa va malament, podeu veure exactament què ha canviat i revertir-lo. Tranquil·litat per deixar que els agents modifiquin la vostra base de codi.

## Coneixement de la pestanya del navegador i altres millores

Algunes addicions més de qualitat de vida:

- **Seguiment de pestanyes del navegador**: ara el xat pot fer un seguiment i enllaçar amb les pestanyes del navegador obertes durant una sessió, de manera que els agents poden fer referència a les pàgines web que esteu mirant
- **Fitxer enganxat al terminal**: enganxeu fitxers (incloses les imatges) al terminal amb Ctrl+V, arrossegueu i deixeu anar o feu clic amb el botó dret.
- **Cobertura de prova al minimapa**: ara els indicadors de cobertura de prova es mostren al minimapa per obtenir una visió visual ràpida
- **Pinch-to-zoom a Mac**: el navegador integrat admet gestos de pessigar-to-zoom
- **Drets de Copilot a Sessions**: la barra d'estat mostra la informació d'ús a la vista Sessions
- **Favicon a Anar al fitxer**: les pàgines web obertes mostren favicons a la llista de selecció ràpida

## Tancant

VS Code 1.115 és una versió incremental, però les millores de l'agent (notificacions de terminal en segon pla, allotjament d'agents SSH i seguiment d'edició) afegeixen una experiència notablement més fluida per al desenvolupament assistit per IA. Si utilitzeu el mode d'agent de Copilot per a projectes.NET, aquests són els tipus de correccions de qualitat de vida que redueixen la fricció diàriament.

Consulteu les [notes completes de la versió](https://code.visualstudio.com/updates/v1_115) per a cada detall.
