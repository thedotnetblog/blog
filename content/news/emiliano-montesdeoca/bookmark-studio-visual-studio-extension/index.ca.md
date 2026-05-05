---
title: "Bookmark Studio aporta la navegació i l'ús compartit basats en ranures als marcadors de Visual Studio"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "La nova extensió de Bookmark Studio de Mads Kristensen afegeix navegació per ranures de teclat, un gestor d'adreces d'interès, colors, etiquetes i capacitats d'exportació/compartiment als marcadors de Visual Studio."
tags:
  - visual-studio
  - extensions
  - productivity
  - developer-tools
---

Els marcadors a Visual Studio sempre han estat... bé. En establiu un, navegueu al següent, oblideu quin marcador és quin. Funcionen, però mai han estat el tipus de funció que podríeu dir poderosa.

Mads Kristensen acaba de [publicar Bookmark Studio](https://devblogs.microsoft.com/visualstudio/bookmark-studio-evolving-bookmarks-in-visual-studio/), una extensió experimental que omple exactament els buits que probablement us heu trobat si feu servir els marcadors amb regularitat.

## Navegació basada en ranures

L'addició bàsica: ara les adreces d'interès es poden assignar a les ranures 1–9 i passar directament a `Alt+Shift+1` a `Alt+Shift+9`. Les adreces d'interès noves obtenen automàticament la següent ranura disponible, de manera que, en la majoria dels casos, la navegació ràpida funciona sense cap configuració.

Sembla senzill, però canvia les adreces d'interès de "Tinc algunes adreces d'interès en algun lloc" a "L'espai 3 és el meu controlador de l'API, l'espai 5 és la capa de servei, l'espai 7 és la prova". Aquest tipus de memòria espacial fa que la navegació sigui gairebé instantània durant les sessions de treball concentrades.

## El gestor d'adreces d'interès

Una nova finestra d'eines mostra totes les vostres adreces d'interès en un sol lloc amb un filtratge per nom, fitxer, ubicació, color o ranura. Fes doble clic o navega amb el teclat per saltar a qualsevol marcador.

Si alguna vegada heu tingut més de cinc o sis adreces d'interès i heu perdut la pista de quins, només val la pena instal·lar l'extensió.

## Organització amb etiquetes, colors i carpetes

Opcionalment, les adreces d'interès poden tenir etiquetes, colors i agrupar-se en carpetes. Res d'això és necessari: el vostre flux de treball de marcador actual continua funcionant. Però quan esteu depurant un problema complex o explorant una base de codi desconeguda, poder codificar amb colors i etiquetar les vostres adreces d'interès afegeix un context útil.

Totes les metadades s'emmagatzemen per solució, de manera que la vostra organització d'adreces d'interès persisteix entre les sessions.

## Exporta i comparteix

Aquesta és la funció que no sabia que volia. Bookmark Studio us permet exportar les adreces d'interès com a text sense format, Markdown o CSV. Això vol dir que pots:

- Incloeu camins d'adreces d'interès a les descripcions de la sol·licitud d'extracció
- Compartiu la investigació amb els companys d'equip
- Mou els conjunts d'adreces d'interès entre repositoris o branques

Els marcadors deixen de ser una eina de navegació en solitari i comencen a ser una manera de comunicar-se "aquí teniu el camí a través d'aquest codi".

## Adreces d'interès que fan un seguiment del moviment del codi

Bookmark Studio fa un seguiment de les adreces d'interès en relació al text al qual estan ancorats, de manera que no es desviïn cap a línies incorrectes mentre editeu. Si alguna vegada heu establert adreces d'interès durant una sessió de depuració i heu fet que tots apunten a les línies equivocades després d'un refactor, això ho soluciona.

## Tancant

Bookmark Studio no reinventa res. Es necessita una funció que ha estat "prou bona" ​​durant anys i la fa realment útil per al desenvolupament centrat. La navegació per ranures, el Gestor d'adreces d'interès i les capacitats d'exportació són els més destacats.

Agafeu-lo del [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.BookmarkStudio) i proveu-ho.
