---
title: "Bookmark Studio trae navegación por slots y compartir a los marcadores de Visual Studio"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "La nueva extensión Bookmark Studio de Mads Kristensen añade navegación por slots con teclado, un gestor de marcadores, colores, etiquetas y capacidades de exportación a Visual Studio."
tags:
  - visual-studio
  - extensions
  - productivity
  - developer-tools
---

> *Este post fue traducido automáticamente. Para la versión original, [haz clic aquí]({{< ref "bookmark-studio-visual-studio-extension.md" >}}).*

Los marcadores en Visual Studio siempre han sido... aceptables. Pones uno, navegas al siguiente, olvidas cuál es cuál. Funcionan, pero nunca han sido una función que llamarías poderosa.

Mads Kristensen acaba de [lanzar Bookmark Studio](https://devblogs.microsoft.com/visualstudio/bookmark-studio-evolving-bookmarks-in-visual-studio/), una extensión experimental que llena exactamente los vacíos que probablemente has encontrado si usas marcadores regularmente.

## Navegación por slots

Los marcadores se pueden asignar a slots del 1 al 9 y saltar directamente con `Alt+Shift+1` hasta `Alt+Shift+9`. Los nuevos marcadores obtienen automáticamente el siguiente slot disponible.

## El Gestor de Marcadores

Una nueva ventana de herramientas muestra todos tus marcadores en un solo lugar con filtrado por nombre, archivo, ubicación, color o slot.

## Organización con etiquetas, colores y carpetas

Los marcadores pueden tener opcionalmente etiquetas, colores y agruparse en carpetas. Toda la metadata se almacena por solución.

## Exportar y compartir

Bookmark Studio permite exportar marcadores como texto plano, Markdown o CSV. Puedes incluir rutas de marcadores en descripciones de PR o compartir caminos de investigación con compañeros.

## Marcadores que siguen al código

Bookmark Studio rastrea los marcadores relativos al texto al que están anclados, así que no se desplazan a líneas incorrectas mientras editas.

## Para cerrar

Bookmark Studio no reinventa nada. Toma una función que ha sido "suficiente" durante años y la hace genuinamente útil. Descárgalo del [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.BookmarkStudio).
