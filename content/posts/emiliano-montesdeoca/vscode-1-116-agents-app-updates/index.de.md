---
title: "VS Code 1.116 — Agents App Bekommt Tastaturnavigation und Dateikontext-Vervollständigungen"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 konzentriert sich auf die Verfeinerung der Agents App — dedizierte Tastenkürzel, Barrierefreiheitsverbesserungen, Dateikontext-Vervollständigungen und CSS @import Link-Auflösung."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *Dieser Beitrag wurde automatisch übersetzt. Die Originalversion finden Sie [hier]({{< ref "vscode-1-116-agents-app-updates.md" >}}).*

VS Code 1.116 ist das April 2026-Release, und obwohl es leichter ausfällt als einige neuere Updates, sind die Änderungen fokussiert und bedeutsam — besonders wenn ihr die Agents App täglich nutzt.

Hier ist, was gelandet ist, basierend auf den [offiziellen Release Notes](https://code.visualstudio.com/updates/v1_116).

## Verbesserungen der Agents App

Die Agents App reift weiter mit Usability-Verfeinerungen, die im täglichen Workflow einen echten Unterschied machen:

**Dedizierte Tastenkürzel** — ihr könnt jetzt die Changes-Ansicht, den Dateibaum innerhalb von Changes und die Chat-Personalisierungsansicht mit dedizierten Befehlen und Tastenkürzeln fokussieren. Wenn ihr bisher in der Agents App herumgeklickt habt, bringt das vollständig tastaturgesteuerte Workflows.

**Barrierefreiheits-Hilfedialog** — das Drücken von `Alt+F1` im Chat-Eingabefeld öffnet jetzt einen Barrierefreiheits-Hilfedialog, der verfügbare Befehle und Tastenkürzel anzeigt. Screenreader-Nutzer können auch die Ausführlichkeit der Ansagen steuern. Gute Barrierefreiheit nützt allen.

**Dateikontext-Vervollständigungen** — tippt `#` im Agents App Chat, um Dateikontext-Vervollständigungen für euren aktuellen Workspace auszulösen. Das ist eine dieser kleinen Quality-of-Life-Verbesserungen, die jede Interaktion beschleunigen — keine vollständigen Dateipfade mehr beim Verweisen auf Code.

## CSS `@import` Link-Auflösung

Schön für Frontend-Entwickler: VS Code löst jetzt CSS `@import`-Referenzen auf, die node_modules-Pfade verwenden. Ihr könnt durch Imports wie `@import "some-module/style.css"` mit `Ctrl+Klick` navigieren, wenn ihr Bundler nutzt. Klein, aber es eliminiert einen Reibungspunkt in CSS-Workflows.

## Fazit

VS Code 1.116 dreht sich um Verfeinerung — die Agents App navigierbarer, barrierefreier und tastaturfreundlicher zu machen. Wenn ihr viel Zeit in der Agents App verbringt (und ich vermute, das tun viele von uns), summieren sich diese Änderungen.

Schaut euch die [vollständigen Release Notes](https://code.visualstudio.com/updates/v1_116) für die komplette Liste an.
