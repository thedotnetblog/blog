---
title: "Bookmark Studio bringt Slot-basierte Navigation und Sharing zu Visual Studio Bookmarks"
date: 2026-04-02
author: "Emiliano Montesdeoca"
description: "Mads Kristensens neue Bookmark Studio Extension fügt tastaturgesteuerte Slot-Navigation, einen Bookmark Manager, Farben, Labels und Export-Funktionen zu Visual Studio Bookmarks hinzu."
tags:
  - visual-studio
  - extensions
  - productivity
  - developer-tools
---

> *Dieser Beitrag wurde automatisch übersetzt. Für die Originalversion [klicke hier]({{< ref "bookmark-studio-visual-studio-extension.md" >}}).*

Bookmarks in Visual Studio waren schon immer... okay. Du setzt eines, navigierst zum nächsten, vergisst welches welches ist. Sie funktionieren, aber sie waren nie eine Funktion, die man als mächtig bezeichnen würde.

Mads Kristensen hat gerade [Bookmark Studio veröffentlicht](https://devblogs.microsoft.com/visualstudio/bookmark-studio-evolving-bookmarks-in-visual-studio/), eine experimentelle Extension, die genau die Lücken füllt, auf die du wahrscheinlich gestoßen bist.

## Slot-basierte Navigation

Bookmarks können Slots 1–9 zugewiesen und direkt mit `Alt+Shift+1` bis `Alt+Shift+9` angesprungen werden. Neue Bookmarks bekommen automatisch den nächsten verfügbaren Slot.

## Der Bookmark Manager

Ein neues Tool-Fenster zeigt alle Bookmarks mit Filterung nach Name, Datei, Ort, Farbe oder Slot.

## Organisation mit Labels, Farben und Ordnern

Bookmarks können optional Labels, Farben haben und in Ordner gruppiert werden. Alle Metadaten werden pro Solution gespeichert.

## Exportieren und Teilen

Bookmark Studio ermöglicht den Export als Klartext, Markdown oder CSV. Bookmark-Pfade in PR-Beschreibungen einbinden oder Untersuchungspfade mit Teamkollegen teilen.

## Bookmarks die dem Code folgen

Bookmark Studio verfolgt Bookmarks relativ zum verankerten Text, sodass sie nicht auf falsche Zeilen driften.

## Zusammenfassung

Bookmark Studio erfindet nichts neu. Es nimmt ein Feature, das jahrelang „gut genug" war, und macht es wirklich nützlich. Hol es dir vom [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.BookmarkStudio).
