---
title: "Die Visual Studio Floating-Windows-Einstellung, die Du Nicht Kanntest (Aber Kennen Solltest)"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "Eine versteckte Visual Studio-Einstellung gibt dir volle Kontrolle über schwebende Fenster — unabhängige Taskleisten-Einträge, richtiges Multi-Monitor-Verhalten und perfekte FancyZones-Integration. Ein Dropdown ändert alles."
tags:
  - visual-studio
  - developer-tools
  - productivity
  - powertoys
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "visual-studio-floating-windows-powertoys.md" >}}).*

Wenn ihr mehrere Monitore mit Visual Studio verwendet (und ehrlich gesagt, wer macht das heutzutage nicht?), habt ihr wahrscheinlich schon die Frustration erlebt: Schwebende Toolfenster verschwinden, wenn ihr das Haupt-IDE minimiert, sie bleiben immer über allem anderen, und sie tauchen nicht als separate Taskleisten-Buttons auf. Das funktioniert für manche Workflows, aber für Multi-Monitor-Setups ist es nervig.

Mads Kristensen vom Visual Studio Team [teilte eine kaum bekannte Einstellung](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/), die komplett verändert, wie sich schwebende Fenster verhalten. Ein Dropdown. Das war's.

## Die Einstellung

**Tools > Options > Environment > Windows > Floating Windows**

Das Dropdown "These floating windows are owned by the main window" hat drei Optionen:

- **None** — volle Unabhängigkeit. Jedes schwebende Fenster bekommt seinen eigenen Taskleisten-Eintrag und verhält sich wie ein normales Windows-Fenster.
- **Tool Windows** (Standard) — Dokumente schweben frei, Toolfenster bleiben an die IDE gebunden.
- **Documents and Tool Windows** — klassisches Visual Studio-Verhalten, alles an das Hauptfenster gebunden.

## Warum "None" der richtige Weg für Multi-Monitor-Setups ist

Stellt es auf **None** und plötzlich verhalten sich alle eure schwebenden Tool- und Dokumentfenster wie echte Windows-Anwendungen. Sie erscheinen in der Taskleiste, bleiben sichtbar wenn ihr das Visual Studio-Hauptfenster minimiert, und hören auf, sich vor alles andere zu drängen.

Kombiniert das mit **PowerToys FancyZones** und es ist ein Game Changer. Erstellt benutzerdefinierte Layouts über eure Monitore, dockt euren Solution Explorer in eine Zone, Debugger in eine andere, und Code-Dateien wohin ihr wollt. Alles bleibt an Ort und Stelle, alles ist unabhängig erreichbar, und euer Arbeitsplatz fühlt sich organisiert an statt chaotisch.

## Schnelle Empfehlungen

- **Multi-Monitor-Poweruser**: Auf **None** setzen, mit FancyZones kombinieren
- **Gelegentliche Floater**: **Tool Windows** (Standard) ist ein guter Mittelweg
- **Traditioneller Workflow**: **Documents and Tool Windows** hält alles klassisch

Profi-Tipp: **Ctrl + Doppelklick** auf die Titelleiste eines beliebigen Toolfensters, um es sofort zu lösen oder anzudocken. Kein Neustart nötig nach dem Ändern der Einstellung.

## Fazit

Es ist eine dieser "Ich kann nicht glauben, dass ich das nicht wusste"-Einstellungen. Wenn euch schwebende Fenster in Visual Studio jemals genervt haben, geht das jetzt sofort ändern.

Lest den [vollständigen Post](https://devblogs.microsoft.com/visualstudio/take-full-control-of-your-floating-windows-in-visual-studio/) für Details und Screenshots.
