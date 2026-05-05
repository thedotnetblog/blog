---
title: "VS Code 1.116 — L'App Agents Ottiene Navigazione da Tastiera e Completamenti per il Contesto dei File"
date: 2026-04-10
author: "Emiliano Montesdeoca"
description: "VS Code 1.116 si concentra sulla rifinitura dell'app Agents — scorciatoie da tastiera dedicate, miglioramenti dell'accessibilità, completamenti per il contesto dei file e risoluzione dei link CSS @import."
tags:
  - vscode
  - developer-tools
  - agents
  - accessibility
---

> *Questo post è stato tradotto automaticamente. Per la versione originale, [clicca qui]({{< ref "vscode-1-116-agents-app-updates.md" >}}).*

VS Code 1.116 è il rilascio di aprile 2026, e sebbene sia più leggero di alcuni aggiornamenti recenti, i cambiamenti sono mirati e significativi — specialmente se usate l'app Agents quotidianamente.

Ecco cosa è arrivato, in base alle [note di rilascio ufficiali](https://code.visualstudio.com/updates/v1_116).

## Miglioramenti dell'app Agents

L'app Agents continua a maturare con un polishing dell'usabilità che fa una vera differenza nei flussi di lavoro quotidiani:

**Scorciatoie da tastiera dedicate** — ora potete mettere a fuoco la vista Changes, l'albero dei file all'interno di Changes e la vista delle Personalizzazioni della Chat con comandi e scorciatoie da tastiera dedicati. Se cliccavate ovunque nell'app Agents per navigare, questo porta flussi di lavoro completamente controllabili da tastiera.

**Dialogo di aiuto per l'accessibilità** — premere `Alt+F1` nella casella di input della chat ora apre un dialogo di aiuto per l'accessibilità che mostra i comandi e le scorciatoie disponibili. Gli utenti di screen reader possono anche controllare la verbosità degli annunci. Una buona accessibilità beneficia tutti.

**Completamenti per il contesto dei file** — digitate `#` nella chat dell'app Agents per attivare i completamenti per il contesto dei file limitati al vostro workspace corrente. Questa è una di quelle piccole migliorie della qualità della vita che velocizzano ogni interazione — niente più percorsi completi dei file quando si referenzia il codice.

## Risoluzione dei link CSS `@import`

Ottimo per gli sviluppatori frontend: VS Code ora risolve i riferimenti CSS `@import` che usano percorsi di node_modules. Potete fare `Ctrl+clic` attraverso import come `@import "some-module/style.css"` quando usate bundler. Piccolo ma elimina un punto di attrito nei workflow CSS.

## Conclusione

VS Code 1.116 riguarda il raffinamento — rendere l'app Agents più navigabile, più accessibile e più amichevole con la tastiera. Se passate molto tempo nell'app Agents (e sospetto che molti di noi lo facciano), questi cambiamenti si sommano.

Consultate le [note di rilascio complete](https://code.visualstudio.com/updates/v1_116) per l'elenco completo.
