---
title: "VS Code 1.116: l'aplicació d'agents obté la navegació per teclat i la finalització del context dels fitxers"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 se centra en la poliment de l'aplicació Agents: combinacions de tecles dedicades, millores d'accessibilitat, completacions de context de fitxers i resolució d'enllaços CSS @import."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

VS Code 1.116 és la versió d'abril de 2026 i, tot i que és més lleuger que algunes actualitzacions recents, els canvis són enfocats i significatius, sobretot si feu servir l'aplicació Agents diàriament.

Aquí teniu el que va arribar, basat en les [notes oficials de la versió](https://code.visualstudio.com/updates/v1_116).

## Millores de l'aplicació d'agents

L'aplicació Agents continua madurant amb un poliment d'usabilitat que marca una diferència real en els fluxos de treball diaris:

**Combinacions de tecles dedicades**: ara podeu centrar la vista Canvis, l'arbre de fitxers dins de Canvis i la vista Personalitzacions de xat amb ordres dedicades i dreceres de teclat. Si heu fet clic per l'aplicació Agents per navegar, això ofereix fluxos de treball complets basats en el teclat.

**Diàleg d'ajuda d'accessibilitat**: prement `Alt+F1` al quadre d'entrada del xat ara s'obre un diàleg d'ajuda d'accessibilitat que mostra les ordres i les combinacions de tecles disponibles. Els usuaris de lectors de pantalla també poden controlar la verbositat dels anuncis. Una bona accessibilitat beneficia a tothom.

**Completacions de context de fitxer**: escriviu `#` al xat de l'aplicació Agents per activar les finalitzacions de context de fitxer a l'abast del vostre espai de treball actual. Aquesta és una d'aquelles petites millores de qualitat de vida que acceleren cada interacció; ja no cal escriure els camins complets dels fitxers quan es fa referència al codi.

## CSS `@import` resolució d'enllaç

Una bona per als desenvolupadors d'interfície: ara VS Code resol les referències CSS `@import` que utilitzen camins node_modules. Podeu `Ctrl+click` mitjançant importacions com `@import "some-module/style.css"` quan utilitzeu agrupadors. Petit però elimina un punt de fricció en els fluxos de treball CSS.

## Tancant

VS Code 1.116 tracta de perfeccionament, fent que l'aplicació Agents sigui més navegable, més accessible i més amigable amb el teclat. Si passeu molt de temps a l'aplicació Agents (i sospito que molts de nosaltres ho estem), aquests canvis s'acumulen.

Consulteu les [notes completes de la versió](https://code.visualstudio.com/updates/v1_116) per obtenir la llista completa.
